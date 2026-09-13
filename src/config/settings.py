"""Project-wide configuration — paths, model defaults."""

from __future__ import annotations

import os
from pathlib import Path

# ── Project root ──────────────────────────────────────────────────────
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent
WORKSPACE_ROOT: Path = PROJECT_ROOT / "workspace"

# ── Disable LangSmith tracing by default ──────────────────────────────
if os.getenv("LANGSMITH_TRACING", "").lower() != "true":
    os.environ["LANGSMITH_TRACING"] = "false"
    os.environ["LANGCHAIN_TRACING_V2"] = "false"

# ── Wiki paths (legacy — knowledge now in Deep Agents memory) ─────────
WIKI_ROOT: Path = WORKSPACE_ROOT / "wiki"

# ── Motor-CAD paths ───────────────────────────────────────────────────
MOTORCAD_MOT_DIR: Path | None = (
    Path(os.getenv("MOTORCAD_SCRIPT_DIR", r"D:\SRM\Motor _CAD\ScriptFiles"))
    if os.path.exists(os.getenv("MOTORCAD_SCRIPT_DIR", r"D:\SRM\Motor _CAD\ScriptFiles"))
    else None
)

# Reference .mot model is project-specific: resolved from the active project
# folder's models/ dir (see src/config/projects.py). This env override exists
# for one-off runs; it is NOT a committed machine-specific default.
_REFERENCE_MOT_ENV = os.getenv("MOTORCAD_REFERENCE_MOT", "").strip()
REFERENCE_MOT: Path | None = Path(_REFERENCE_MOT_ENV) if _REFERENCE_MOT_ENV else None

# ── LLM providers (per-provider credential adapters) ──────────────────
# The agent is a DIRECT client (static Bearer key per provider). It does NOT
# do session/OAuth flows and must not spoof app client context: server-side
# entitlement (plan, free-tier app binding, quota) is enforced provider-side
# and no local code can override it. Zen free-tier models, for example, answer
# "free tier can only be used in OpenCode" to direct API calls by design.
# Switch providers with LLM_PROVIDER instead of fighting the gate.
LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "zen").strip().lower() or "zen"

PROVIDER_PROFILES: dict[str, dict] = {
    "zen": {
        # OpenCode Zen provider — supports paid & free tier models.
        # Free-tier models require x-session-id and opencode User-Agent headers.
        "key_env": "OPENCODE_API_KEY",
        "key_fallback_env": "OPENAI_API_KEY",
        "key_prefix_hint": "sk-",
        "default_base_url": "https://opencode.ai/zen/v1",
        "default_model": "nemotron-3-ultra-free",
        "fallback_models": (
            "nemotron-3-ultra-free",
            "nemotron-3.5-lightning-free",
            "mimo-v2.5-free",
            "deepseek-v4-flash-free",
        ),
    },
    "openrouter": {
        # Static key (sk-or-v1-...); free :free models work via plain API.
        "key_env": "OPENROUTER_API_KEY",
        "key_fallback_env": "",
        "key_prefix_hint": "sk-or-v1-",
        "default_base_url": "https://openrouter.ai/api/v1",
        "default_model": "openrouter/free",
        "fallback_models": ("openrouter/free",),
    },
    "nim": {
        # NVIDIA NIM: free build.nvidia.com key, OpenAI-compatible API.
        # Catalogue verified public; default verified live 2026-09-12.
        "key_env": "NVIDIA_NIM_API_KEY",
        "key_fallback_env": "",
        "key_prefix_hint": "nvapi-",
        "default_base_url": "https://integrate.api.nvidia.com/v1",
        "default_model": "nvidia/nemotron-3-super-120b-a12b",
        "fallback_models": (
            "nvidia/nemotron-3-super-120b-a12b",
            "deepseek-ai/deepseek-v4-flash-0731",
        ),
    },
    "groq": {
        # Groq: free-tier API key, OpenAI-compatible endpoint.
        "key_env": "GROQ_API_KEY",
        "key_fallback_env": "",
        "key_prefix_hint": "gsk_",
        "default_base_url": "https://api.groq.com/openai/v1",
        "default_model": "llama-3.3-70b-versatile",
        "fallback_models": ("llama-3.3-70b-versatile",),
    },
}

LLM_API_KEY: str | None = os.getenv("OPENCODE_API_KEY")
LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", "https://opencode.ai/zen/v1")
LLM_MODEL: str = os.getenv("LLM_MODEL", "nemotron-3-ultra-free")

MODEL_DEFAULT: str = os.getenv("MODEL_DEFAULT", LLM_MODEL)
MODEL_RESEARCH: str = os.getenv("MODEL_RESEARCH", LLM_MODEL)
MODEL_SYNTHESIS: str = os.getenv("MODEL_SYNTHESIS", LLM_MODEL)


def _read_opencode_auth_key() -> str:
    """Read OpenCode credentials from ~/.local/share/opencode/account.json if present."""
    try:
        acct_path = Path.home() / ".local" / "share" / "opencode" / "account.json"
        if acct_path.is_file():
            import json as _json

            data = _json.loads(acct_path.read_text(encoding="utf-8"))
            active_id = data.get("active", {}).get("opencode")
            if active_id and active_id in data.get("accounts", {}):
                return data["accounts"][active_id].get("credential", {}).get("key", "").strip()
    except Exception:
        pass
    return ""


def resolve_provider(name: str = "") -> dict:
    """Resolve the active provider profile: {name, base_url, api_key, headers}.

    Base URL rule: an explicit LLM_BASE_URL wins, EXCEPT when it is just the
    shipped Zen default while another provider is selected (so switching is a
    one-var change: LLM_PROVIDER=openrouter). Raises a naming-the-right-var
    ValueError when the provider key is missing.
    """
    provider = (name or os.getenv("LLM_PROVIDER", "") or LLM_PROVIDER).strip().lower() or "zen"
    profile = PROVIDER_PROFILES.get(provider)
    if profile is None:
        known = ", ".join(sorted(PROVIDER_PROFILES))
        raise ValueError(f"Unknown LLM_PROVIDER '{provider}'. Known: {known}.")

    key_env: str = profile["key_env"]
    api_key = os.getenv(key_env, "").strip()
    fallback_env: str = profile.get("key_fallback_env", "")
    if not api_key and fallback_env:
        api_key = os.getenv(fallback_env, "").strip()
    if not api_key and provider == "zen":
        api_key = _read_opencode_auth_key()
    if not api_key:
        raise ValueError(
            f"No API key for provider '{provider}'. Set {key_env} in your environment or .env file."
        )

    explicit_base = os.getenv("LLM_BASE_URL", "").strip()
    if explicit_base and not (
        provider != "zen" and explicit_base.rstrip("/") == PROVIDER_PROFILES["zen"]["default_base_url"]
    ):
        base_url = explicit_base
    else:
        base_url = profile["default_base_url"]

    headers: dict[str, str] = {}
    if provider == "openrouter":
        referer = os.getenv("OPENROUTER_REFERER", "").strip()
        title = os.getenv("OPENROUTER_TITLE", "").strip()
        if referer:
            headers["HTTP-Referer"] = referer
        if title:
            headers["X-Title"] = title
    elif provider == "zen":
        session_id = os.getenv("OPENCODE_SESSION_ID", "").strip()
        if not session_id:
            import uuid as _uuid

            session_id = f"ses_{_uuid.uuid4().hex[:16]}"
        headers["x-session-id"] = session_id
        headers["User-Agent"] = "opencode/1.18.30"

    return {"name": provider, "profile": profile, "base_url": base_url,
            "api_key": api_key, "headers": headers, "key_env": key_env}

# Conservative context-window assumption for proxied/unnamed models. deepagents'
# SummarizationMiddleware reads this from llm.profile; without it the middleware
# falls back to a 170k-token trigger that can overflow the real endpoint.
MODEL_MAX_INPUT_TOKENS: int = int(os.getenv("MODEL_MAX_INPUT_TOKENS", "65536"))

# ── Opencode Zen model discovery ────────────────────────────────────
# GET <LLM_BASE_URL>/models is an OpenAI-compatible public catalogue (no key
# required; the key is still sent when configured in case an account can reach
# more models). Results are cached in-memory for ZEN_MODELS_TTL_SECONDS.
ZEN_MODELS_TTL_SECONDS: int = int(os.getenv("ZEN_MODELS_TTL_SECONDS", "3600"))
ZEN_MODELS_TIMEOUT_SECONDS: int = int(os.getenv("ZEN_MODELS_TIMEOUT_SECONDS", "15"))

# Safety net when the catalogue is unreachable (outage / offline / DNS).
# Synced from https://opencode.ai/zen/v1/models; env-configured defaults are
# appended dynamically so a custom default is never unselectable.
_FALLBACK_ZEN_MODELS: tuple[str, ...] = (
    "deepseek-v4-flash-free",
    "deepseek-v4-flash",
    "muse-spark-1.3-contributor-free",
    "muse-spark-1.3",
    "gpt-5.5",
    "gpt-5.4-mini",
    "gpt-5-nano",
    "claude-haiku-4-5",
    "claude-sonnet-4-5",
    "gemini-3-flash",
    "gemini-3.5-flash-lite",
    "qwen3.6-plus",
    "kimi-k2.5",
)

_models_cache: list[str] | None = None
_models_cache_ts: float = 0.0
_models_cache_source: str = "fallback"


def _zen_models_url() -> str:
    """Derive the OpenAI-compatible /models URL from the active provider base URL."""
    try:
        base = resolve_provider()["base_url"]
    except ValueError:
        base = os.getenv("LLM_BASE_URL", LLM_BASE_URL)
    base = base.rstrip("/")
    if base.endswith("/models"):
        return base
    return base + "/models"


def _parse_models_payload(raw: bytes) -> list[str]:
    """Parse an OpenAI-compatible {object:list, data:[{id}]} payload."""
    import json as _json

    payload = _json.loads(raw.decode("utf-8", "replace"))
    data = payload.get("data") if isinstance(payload, dict) else payload
    ids: list[str] = []
    if isinstance(data, list):
        for entry in data:
            model_id = entry.get("id") if isinstance(entry, dict) else entry
            if isinstance(model_id, str) and model_id.strip():
                ids.append(model_id.strip())
    # Preserve catalogue order, drop duplicates.
    return list(dict.fromkeys(ids))


def _request_models_json(url: str, api_key: str | None, timeout: int) -> bytes:
    """GET the catalogue, retrying anonymously on 401/403 (public endpoint)."""
    import urllib.error as _urlerror
    import urllib.request as _urlrequest

    def _get(headers: dict) -> bytes:
        req = _urlrequest.Request(url, headers={"User-Agent": "motor-deepagent", **headers})
        with _urlrequest.urlopen(req, timeout=timeout) as resp:
            return resp.read()

    if api_key:
        try:
            return _get({"Authorization": f"Bearer {api_key}"})
        except _urlerror.HTTPError as e:
            if e.code not in (401, 403):
                raise
    return _get({})


def fetch_zen_models(force_refresh: bool = False) -> tuple[list[str], str]:
    """Return (model_ids, source) where source is live|cache|fallback.

    Uses the in-memory cache when fresh unless force_refresh=True. Never
    raises: total failure yields the fallback list with source='fallback'.
    """
    import time as _time

    global _models_cache, _models_cache_ts, _models_cache_source

    ttl = int(os.getenv("ZEN_MODELS_TTL_SECONDS", str(ZEN_MODELS_TTL_SECONDS)))
    if (
        not force_refresh
        and _models_cache is not None
        and (_time.time() - _models_cache_ts) < max(ttl, 0)
    ):
        return list(_models_cache), _models_cache_source

    try:
        try:
            provider = resolve_provider()
            api_key = provider["api_key"]
        except ValueError:
            api_key = os.getenv("OPENCODE_API_KEY") or os.getenv("OPENAI_API_KEY")
        timeout = int(os.getenv("ZEN_MODELS_TIMEOUT_SECONDS", str(ZEN_MODELS_TIMEOUT_SECONDS)))
        ids = _parse_models_payload(_request_models_json(_zen_models_url(), api_key, timeout))
        if not ids:
            raise ValueError("empty model catalogue")
        _models_cache, _models_cache_ts, _models_cache_source = ids, _time.time(), "live"
        return list(ids), "live"
    except Exception:
        # Serve stale cache if we have it, else the fallback net.
        if _models_cache is not None:
            return list(_models_cache), _models_cache_source
        fallback = list(dict.fromkeys(
            list(_FALLBACK_ZEN_MODELS)
            + [m for m in (os.getenv("LLM_MODEL", ""), os.getenv("MODEL_DEFAULT", ""), LLM_MODEL, MODEL_DEFAULT) if m]
        ))
        _models_cache, _models_cache_ts, _models_cache_source = fallback, _time.time(), "fallback"
        return list(fallback), "fallback"


def get_available_models(force_refresh: bool = False) -> list[str]:
    """Return known Zen model ids (live catalogue, cache, or fallback)."""
    models, _ = fetch_zen_models(force_refresh=force_refresh)
    return models


def peek_cached_models() -> list[str]:
    """Return cached model ids without any network I/O (for tab completion)."""
    return list(_models_cache) if _models_cache is not None else []


def clear_models_cache() -> None:
    """Invalidate the in-memory model catalogue (tests, /model refresh)."""
    global _models_cache, _models_cache_ts, _models_cache_source
    _models_cache, _models_cache_ts, _models_cache_source = None, 0.0, "fallback"


def resolve_model_name(name: str, models: list[str] | None = None) -> tuple[str | None, list[str]]:
    """Resolve user input to a catalogue id.

    Returns (resolved_id_or_None, suggestions). Matching order: exact,
    case-insensitive exact, then unique prefix (also case-insensitive).
    Ambiguous prefixes return None + the candidate list.
    """
    candidates = models if models is not None else get_available_models()
    query = (name or "").strip()
    if not query:
        return None, []
    if query in candidates:
        return query, [query]
    lowered = {m.lower(): m for m in candidates}
    if query.lower() in lowered:
        return lowered[query.lower()], [lowered[query.lower()]]
    prefix_hits = [m for m in candidates if m.lower().startswith(query.lower())]
    if len(prefix_hits) == 1:
        return prefix_hits[0], prefix_hits
    if prefix_hits:
        return None, prefix_hits[:10]
    # Last resort: substring matches to guide the user.
    contains = [m for m in candidates if query.lower() in m.lower()][:10]
    return None, contains

# ── Agent Execution Settings ──────────────────────────────────────────
def get_recursion_limit() -> int | None:
    """Return explicit LangGraph recursion limit, or None to use the framework default.
    Opt-in via $MOTOR_RECURSION_LIMIT (legacy $RECURSION_LIMIT also honored)."""
    for _name in ("MOTOR_RECURSION_LIMIT", "RECURSION_LIMIT"):
        _raw = os.getenv(_name, "")
        if not _raw:
            continue
        try:
            _val = int(str(_raw).strip())
        except (ValueError, TypeError):
            return None
        return _val if _val > 0 else None
    return None

# ── Config file loading ───────────────────────────────────────────────
_config_cache: dict | None = None

def load_config() -> dict:
    """Load config.toml from project root, with caching."""
    global _config_cache
    if _config_cache is not None:
        return _config_cache
    config_path = PROJECT_ROOT / "config.toml"
    if config_path.exists():
        try:
            import tomllib
        except ModuleNotFoundError:
            try:
                import tomli as tomllib  # Python < 3.11 fallback
            except ModuleNotFoundError:
                _config_cache = {}
                return _config_cache
        try:
            with open(config_path, "rb") as f:
                _config_cache = tomllib.load(f)
        except Exception:
            _config_cache = {}
    else:
        _config_cache = {}
    return _config_cache

# ── LLM client factory ────────────────────────────────────────────────


def get_llm(model: str | None = None) -> "ChatOpenAI":
    """Return a LangChain ChatOpenAI pointed at the active provider with retries and timeout protection."""
    from langchain_openai import ChatOpenAI

    provider = resolve_provider()
    kwargs: dict = dict(
        model=model or MODEL_DEFAULT,
        base_url=provider["base_url"],
        api_key=provider["api_key"],
        temperature=0.3,
        max_retries=3,
        request_timeout=120.0,
    )
    if provider["headers"]:
        kwargs["default_headers"] = provider["headers"]
    llm = ChatOpenAI(**kwargs)
    # Expose the context window so deepagents' SummarizationMiddleware uses
    # fraction-based triggers instead of its 170k-token no-profile fallback.
    llm.profile = {"max_input_tokens": MODEL_MAX_INPUT_TOKENS}
    return llm


# ── LLM fallback ────────────────────────────────────────────────────────
# On retryable errors (rate limit, outage), fall back to cheap provider
# models instead of aborting the session. Used by the research subgraph and
# any caller that prefers degraded service over failure. NOTE: fallback only
# retries within the same provider — it cannot cross server-side entitlement
# gates (plan/free-tier binding); those need a provider switch, not a retry.
FALLBACK_MODELS: tuple[str, ...] = (
    "deepseek-v4-flash-free",
    "muse-spark-1.3-contributor-free",
)


def _provider_fallback_models() -> tuple[str, ...]:
    try:
        provider = os.getenv("LLM_PROVIDER", "") or LLM_PROVIDER
        profile = PROVIDER_PROFILES.get(provider.strip().lower() or "zen")
        if profile:
            return tuple(profile.get("fallback_models", ())) or FALLBACK_MODELS
    except Exception:
        pass
    return FALLBACK_MODELS


def invoke_with_fallback(llm, messages, fallback_models: tuple[str, ...] | None = None,
                         llm_factory=None):
    """Invoke llm; on failure retry with cheap fallback models in order.

    llm_factory(model_name) builds a replacement client (defaults to get_llm,
    injectable for tests). Raises the LAST error if every model fails.
    """
    factory = llm_factory or get_llm
    last_error: Exception | None = None
    try:
        return llm.invoke(messages)
    except Exception as e:
        last_error = e
    for fallback in (fallback_models or _provider_fallback_models()):
        try:
            return factory(fallback).invoke(messages)
        except Exception as e:
            last_error = e
    raise last_error  # type: ignore[misc]


__all__ = [
    "PROJECT_ROOT",
    "WORKSPACE_ROOT",
    "WIKI_ROOT",
    "MOTORCAD_MOT_DIR",
    "REFERENCE_MOT",
    "LLM_API_KEY",
    "LLM_BASE_URL",
    "LLM_MODEL",
    "LLM_PROVIDER",
    "PROVIDER_PROFILES",
    "resolve_provider",
    "MODEL_DEFAULT",
    "MODEL_RESEARCH",
    "MODEL_SYNTHESIS",
    "MODEL_MAX_INPUT_TOKENS",
    "get_recursion_limit",
    "ZEN_MODELS_TTL_SECONDS",
    "ZEN_MODELS_TIMEOUT_SECONDS",
    "FALLBACK_MODELS",
    "get_llm",
    "invoke_with_fallback",
    "load_config",
    "fetch_zen_models",
    "get_available_models",
    "peek_cached_models",
    "clear_models_cache",
    "resolve_model_name",
]
