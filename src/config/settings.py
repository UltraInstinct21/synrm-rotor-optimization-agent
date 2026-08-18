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

REFERENCE_MOT: Path = PROJECT_ROOT / "SynRM_45kW_IE5.mot"

# ── LLM / Opencode ────────────────────────────────────────────────────
LLM_API_KEY: str | None = os.getenv("OPENCODE_API_KEY")
LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", "https://opencode.ai/zen/v1")
LLM_MODEL: str = os.getenv("LLM_MODEL", "deepseek-v4-flash-free")

MODEL_DEFAULT: str = os.getenv("MODEL_DEFAULT", LLM_MODEL)
MODEL_RESEARCH: str = os.getenv("MODEL_RESEARCH", LLM_MODEL)
MODEL_SYNTHESIS: str = os.getenv("MODEL_SYNTHESIS", LLM_MODEL)

# ── Agent Execution Settings ──────────────────────────────────────────
RECURSION_LIMIT: int = int(os.getenv("RECURSION_LIMIT", "100"))

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
    """Return a LangChain ChatOpenAI pointed at Opencode with retries and timeout protection."""
    from langchain_openai import ChatOpenAI

    api_key = LLM_API_KEY or os.getenv("OPENCODE_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "No API key found. Set OPENCODE_API_KEY or OPENAI_API_KEY in your environment or .env file."
        )


    return ChatOpenAI(
        model=model or MODEL_DEFAULT,
        base_url=LLM_BASE_URL,
        api_key=api_key,
        temperature=0.3,
        max_retries=3,
        request_timeout=60.0,
    )


__all__ = [
    "PROJECT_ROOT",
    "WORKSPACE_ROOT",
    "WIKI_ROOT",
    "MOTORCAD_MOT_DIR",
    "REFERENCE_MOT",
    "LLM_API_KEY",
    "LLM_BASE_URL",
    "LLM_MODEL",
    "MODEL_DEFAULT",
    "MODEL_RESEARCH",
    "MODEL_SYNTHESIS",
    "RECURSION_LIMIT",
    "get_llm",
    "load_config",
]
