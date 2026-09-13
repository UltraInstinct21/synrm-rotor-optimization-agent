"""Tests for Opencode Zen model discovery and the /model command (offline-safe)."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

from src.config import settings


@pytest.fixture(autouse=True)
def _clean_cache():
    settings.clear_models_cache()
    yield
    settings.clear_models_cache()


def _payload(ids: list[str]) -> bytes:
    return json.dumps({"object": "list", "data": [{"id": i} for i in ids]}).encode()


def test_fetch_live_parses_ids():
    with patch.object(settings, "_request_models_json", return_value=_payload(["gpt-5", "claude-x"])) as m:
        models, source = settings.fetch_zen_models()
    assert models == ["gpt-5", "claude-x"]
    assert source == "live"
    assert m.call_count == 1


def test_fetch_uses_cache_without_network():
    with patch.object(settings, "_request_models_json", return_value=_payload(["a"])) as m:
        settings.fetch_zen_models()
        models, source = settings.fetch_zen_models()
    assert m.call_count == 1  # second call served from cache
    assert models == ["a"]
    assert source == "live"


def test_fetch_force_refresh_bypasses_cache():
    with patch.object(settings, "_request_models_json", return_value=_payload(["a"])) as m:
        settings.fetch_zen_models()
        settings.fetch_zen_models(force_refresh=True)
    assert m.call_count == 2


def test_fetch_failure_yields_fallback():
    with patch.object(settings, "_request_models_json", side_effect=OSError("offline")):
        models, source = settings.fetch_zen_models()
    assert source == "fallback"
    assert len(models) > 0
    assert settings.MODEL_DEFAULT in models or settings.LLM_MODEL in models


def test_fetch_anonymous_retry_on_401():
    import os
    import urllib.error as urlerror

    err = urlerror.HTTPError("url", 401, "Unauthorized", {}, None)
    anon_resp = MagicMock()
    anon_resp.__enter__.return_value = anon_resp
    anon_resp.__exit__.return_value = False
    anon_resp.read.return_value = _payload(["anon-model"])
    with patch.dict(os.environ, {"OPENCODE_API_KEY": "sk-test-key"}), patch(
        "urllib.request.urlopen", side_effect=[err, anon_resp]
    ):
        models, source = settings.fetch_zen_models()
    assert models == ["anon-model"]
    assert source == "live"


def test_parse_tolerates_bare_list():
    ids = settings._parse_models_payload(json.dumps([{"id": "x-1"}]).encode())
    assert ids == ["x-1"]


def test_parse_dedupes_preserving_order():
    raw = json.dumps({"data": [{"id": "b"}, {"id": "a"}, {"id": "b"}]}).encode()
    assert settings._parse_models_payload(raw) == ["b", "a"]


def test_resolve_exact_and_case_insensitive():
    catalog = ["gpt-5", "Claude-X"]
    assert settings.resolve_model_name("gpt-5", catalog) == ("gpt-5", ["gpt-5"])
    assert settings.resolve_model_name("claude-x", catalog) == ("Claude-X", ["Claude-X"])


def test_resolve_unique_prefix():
    catalog = ["gpt-5", "gpt-5.4-mini", "claude-x"]
    assert settings.resolve_model_name("claude", catalog) == ("claude-x", ["claude-x"])
    resolved, suggestions = settings.resolve_model_name("gpt-5", ["gpt-5", "gpt-5.4-mini"])
    assert resolved == "gpt-5"  # exact wins over prefix


def test_resolve_ambiguous_prefix_returns_suggestions():
    catalog = ["gpt-5", "gpt-5.4-mini", "gpt-5-nano"]
    resolved, suggestions = settings.resolve_model_name("gpt-5", catalog)
    assert resolved == "gpt-5"  # exact match wins
    resolved, suggestions = settings.resolve_model_name("gpt-", catalog)
    assert resolved is None
    assert set(suggestions) == {"gpt-5", "gpt-5.4-mini", "gpt-5-nano"}


def test_resolve_unknown_suggests_substrings():
    catalog = ["gpt-5", "claude-x"]
    resolved, suggestions = settings.resolve_model_name("zzz", catalog)
    assert resolved is None
    assert suggestions == []
    resolved, suggestions = settings.resolve_model_name("cla", catalog)
    assert resolved == "claude-x"


def test_resolve_empty():
    assert settings.resolve_model_name("", ["a"]) == (None, [])


def test_peek_cached_models_no_network():
    assert settings.peek_cached_models() == []
    with patch.object(settings, "_request_models_json", return_value=_payload(["m1"])):
        settings.fetch_zen_models()
    assert settings.peek_cached_models() == ["m1"]


def _make_cli():
    from apps.cli.app import MotorCLI

    cli = MotorCLI()
    cli.console = MagicMock()
    return cli


def test_cmd_model_list_renders_table():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["m1", "m2"], "live")):
        dispatch(cli, "/model")
    cli.console.print.assert_called()
    assert cli.model_name == "default"  # listing does not switch


def test_cmd_model_list_subcommand():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["m1"], "live")) as m:
        dispatch(cli, "/model list")
    m.assert_called_once_with(force_refresh=False)


def test_cmd_model_refresh_forces_fetch():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["m1"], "live")) as m:
        dispatch(cli, "/model refresh")
    m.assert_called_once_with(force_refresh=True)


def test_cmd_model_switch_exact():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["gpt-5", "claude-x"], "live")):
        dispatch(cli, "/model claude-x")
    assert cli.model_name == "claude-x"
    assert cli._agent is None


def test_cmd_model_switch_by_number():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["gpt-5", "claude-x"], "live")):
        dispatch(cli, "/model 2")
    assert cli.model_name == "claude-x"


def test_cmd_model_switch_unique_prefix():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["gpt-5", "claude-x"], "live")):
        dispatch(cli, "/model claude")
    assert cli.model_name == "claude-x"


def test_cmd_model_unknown_does_not_switch():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["gpt-5"], "live")):
        dispatch(cli, "/model nope-nope")
    assert cli.model_name == "default"


def test_cmd_model_fallback_warning():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch.object(settings, "fetch_zen_models", return_value=(["m1"], "fallback")):
        dispatch(cli, "/model")
    printed = " ".join(str(c) for c in cli.console.print.call_args_list)
    assert "fallback" in printed.lower()
