"""Tests for LLM fallback invocation and startup preflight (offline-safe)."""

from __future__ import annotations

import pytest

from src.config import settings
from src.config.preflight import run_preflight


class _Boom:
    def invoke(self, messages):
        raise RuntimeError("rate limited")


class _FakeClient:
    def __init__(self, result=None, error=None):
        self._result = result
        self._error = error

    def invoke(self, messages):
        if self._error:
            raise self._error
        return self._result


def test_fallback_uses_next_model():
    made = []

    def factory(name):
        made.append(name)
        return _FakeClient(result=f"ok:{name}")

    out = settings.invoke_with_fallback(_Boom(), ["hi"],
                                        fallback_models=("fb-1", "fb-2"),
                                        llm_factory=factory)
    assert out == "ok:fb-1"
    assert made == ["fb-1"]


def test_fallback_skips_failed_and_raises_last():
    def factory(name):
        return _FakeClient(error=ValueError(f"bad:{name}"))

    with pytest.raises(ValueError, match="bad:fb-2"):
        settings.invoke_with_fallback(_Boom(), ["hi"],
                                      fallback_models=("fb-1", "fb-2"),
                                      llm_factory=factory)


def test_primary_success_no_fallback_used():
    made = []

    def factory(name):  # pragma: no cover
        made.append(name)
        return _FakeClient(result="x")

    assert settings.invoke_with_fallback(_FakeClient(result="primary"), ["hi"],
                                         llm_factory=factory) == "primary"
    assert made == []


def test_preflight_structure():
    results = run_preflight()
    assert isinstance(results, list) and len(results) >= 5
    for r in results:
        assert {"check", "level", "message"} <= set(r)
        assert r["level"] in ("ok", "warn", "error")


def test_preflight_missing_key_is_error(monkeypatch):
    monkeypatch.delenv("OPENCODE_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(settings, "_read_opencode_auth_key", lambda: "")
    # settings caches LLM_API_KEY at import; preflight reads env directly.
    results = {r["check"]: r for r in run_preflight()}
    assert results["LLM API key"]["level"] == "error"


def test_preflight_bad_key_format_warns(monkeypatch):
    monkeypatch.setenv("OPENCODE_API_KEY", "bad-prefix-key")
    results = {r["check"]: r for r in run_preflight()}
    assert results["LLM API key"]["level"] == "warn"
    assert "sk-" in results["LLM API key"]["message"]


def test_preflight_bad_spec_is_error(monkeypatch, tmp_path):
    from src.config import projects as projectsmod

    bad = tmp_path / "bad.json"
    bad.write_text("{not json", encoding="utf-8")
    monkeypatch.setenv("MOTOR_SPEC", str(bad))
    # Neutralize project-first resolution so the bad legacy override is reached.
    monkeypatch.setattr(projectsmod, "get_active_slug", lambda: None)
    monkeypatch.delenv("MOTOR_PROJECT", raising=False)
    results = {r["check"]: r for r in run_preflight()}
    assert results["Machine spec"]["level"] == "error"


def test_preflight_flags_unknown_default_model(monkeypatch):
    import json as _json
    import urllib.request as _urlrequest

    payload = _json.dumps({"data": [{"id": "real-model"}]}).encode()

    class _Resp:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return payload

    monkeypatch.setenv("MODEL_DEFAULT", "ghost-model-zzz")
    monkeypatch.setattr(_urlrequest, "urlopen", lambda *a, **k: _Resp())
    results = {r["check"]: r for r in run_preflight()}
    assert results["Zen catalogue"]["level"] == "warn"
    assert "ghost-model-zzz" in results["Zen catalogue"]["message"]


def test_error_card_500_tip():
    from unittest.mock import MagicMock

    from apps.cli.theme import render_error_card

    console = MagicMock()
    render_error_card(console, RuntimeError("Error code: 500 - Internal server error"))
    panel = console.print.call_args_list[1].args[0]
    assert "/model" in panel.renderable.plain
