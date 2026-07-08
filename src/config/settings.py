"""Project-wide configuration — paths, model defaults."""

from __future__ import annotations

import os
from pathlib import Path

# ── Project root ──────────────────────────────────────────────────────
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent
WORKSPACE_ROOT: Path = PROJECT_ROOT / "workspace"

# ── Wiki paths (legacy — knowledge now in Deep Agents memory) ─────────
WIKI_ROOT: Path = WORKSPACE_ROOT / "wiki"

# ── Motor-CAD paths ───────────────────────────────────────────────────
MOTORCAD_MOT_DIR: Path | None = (
    Path(r"D:\SRM\Motor _CAD\ScriptFiles")
    if os.path.exists(r"D:\SRM\Motor _CAD\ScriptFiles")
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

# ── LLM client factory ────────────────────────────────────────────────


def get_llm(model: str | None = None) -> "ChatOpenAI":
    """Return a LangChain ChatOpenAI pointed at Opencode."""
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=model or MODEL_DEFAULT,
        base_url=LLM_BASE_URL,
        api_key=LLM_API_KEY or os.getenv("OPENCODE_API_KEY") or "sk-placeholder",
        temperature=0.3,
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
    "get_llm",
]
