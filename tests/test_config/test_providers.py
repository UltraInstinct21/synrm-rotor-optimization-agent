"""Tests for per-provider credential adapters (offline-safe)."""

from __future__ import annotations

import pytest

from src.config import settings


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for var in ("LLM_PROVIDER", "LLM_BASE_URL", "OPENCODE_API_KEY", "OPENAI_API_KEY",
                "OPENROUTER_API_KEY", "OPENROUTER_REFERER", "OPENROUTER_TITLE",
                "NVIDIA_NIM_API_KEY", "GROQ_API_KEY"):
        monkeypatch.delenv(var, raising=False)
    settings.clear_models_cache()
    yield
    settings.clear_models_cache()


def test_zen_default(monkeypatch):
    monkeypatch.setenv("OPENCODE_API_KEY", "oc-test")
    p = settings.resolve_provider()
    assert p["name"] == "zen"
    assert p["base_url"] == "https://opencode.ai/zen/v1"
    assert p["api_key"] == "oc-test"
    assert "x-session-id" in p["headers"]
    assert p["headers"]["User-Agent"] == "opencode/1.18.30"


def test_zen_falls_back_to_openai_key(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-openai")
    assert settings.resolve_provider()["api_key"] == "sk-openai"


def test_missing_key_names_right_var(monkeypatch):
    monkeypatch.setattr(settings, "_read_opencode_auth_key", lambda: "")
    with pytest.raises(ValueError, match="OPENCODE_API_KEY"):
        settings.resolve_provider()


def test_openrouter_switch_is_one_var(monkeypatch):
    # Shipped .env pins LLM_BASE_URL to zen; selecting openrouter must still
    # route to OpenRouter without touching the URL.
    monkeypatch.setenv("LLM_PROVIDER", "openrouter")
    monkeypatch.setenv("LLM_BASE_URL", "https://opencode.ai/zen/v1")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-v1-test")
    p = settings.resolve_provider()
    assert p["base_url"] == "https://openrouter.ai/api/v1"
    assert p["api_key"] == "sk-or-v1-test"


def test_openrouter_optional_headers(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "openrouter")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-v1-test")
    monkeypatch.setenv("OPENROUTER_REFERER", "https://example.com")
    monkeypatch.setenv("OPENROUTER_TITLE", "motor-agent")
    headers = settings.resolve_provider()["headers"]
    assert headers == {"HTTP-Referer": "https://example.com", "X-Title": "motor-agent"}


def test_explicit_custom_base_url_wins(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "openrouter")
    monkeypatch.setenv("LLM_BASE_URL", "https://my-gateway.local/v1")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-v1-test")
    assert settings.resolve_provider()["base_url"] == "https://my-gateway.local/v1"


def test_unknown_provider(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "nope")
    monkeypatch.setenv("OPENCODE_API_KEY", "oc-test")
    with pytest.raises(ValueError, match="Unknown LLM_PROVIDER"):
        settings.resolve_provider()


def test_get_llm_uses_provider(monkeypatch):
    import langchain_openai

    captured = {}
    real = langchain_openai.ChatOpenAI

    def fake(**kwargs):
        captured.update(kwargs)
        return real(model="x", base_url="https://openrouter.ai/api/v1",
                    api_key="sk-or-v1-test")

    monkeypatch.setenv("LLM_PROVIDER", "openrouter")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-v1-test")
    monkeypatch.setattr(langchain_openai, "ChatOpenAI", fake)
    settings.get_llm("openrouter/free")
    assert captured["base_url"] == "https://openrouter.ai/api/v1"
    assert captured["model"] == "openrouter/free"


def test_models_url_follows_provider(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "openrouter")
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-v1-test")
    assert settings._zen_models_url() == "https://openrouter.ai/api/v1/models"


def test_nim_profile(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "nim")
    monkeypatch.setenv("NVIDIA_NIM_API_KEY", "nvapi-test")
    p = settings.resolve_provider()
    assert p["base_url"] == "https://integrate.api.nvidia.com/v1"
    assert p["api_key"] == "nvapi-test"
    assert settings._zen_models_url() == "https://integrate.api.nvidia.com/v1/models"


def test_groq_profile(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "groq")
    monkeypatch.setenv("GROQ_API_KEY", "gsk_test")
    p = settings.resolve_provider()
    assert p["base_url"] == "https://api.groq.com/openai/v1"
    assert p["key_env"] == "GROQ_API_KEY"


def test_groq_missing_key_names_var(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "groq")
    with pytest.raises(ValueError, match="GROQ_API_KEY"):
        settings.resolve_provider()
