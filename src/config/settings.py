"""Project-wide configuration — paths, model defaults, backend settings."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

# ── Project root ──────────────────────────────────────────────────────
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent
WORKSPACE_ROOT: Path = PROJECT_ROOT / "workspace"

# ── Wiki paths ────────────────────────────────────────────────────────
WIKI_ROOT: Path = WORKSPACE_ROOT / "wiki"
EXPERIMENTS_ROOT: Path = WORKSPACE_ROOT / "experiments"
RESEARCH_CACHE: Path = WORKSPACE_ROOT / "research_cache"
SCRATCH_ROOT: Path = WORKSPACE_ROOT / "scratch"

# Legacy wiki (external reference wiki used before this project existed)
LEGACY_WIKI_ROOT: Path | None = (
    Path(r"D:\SRM\Motor _CAD\ScriptFiles\wiki")
    if os.path.exists(r"D:\SRM\Motor _CAD\ScriptFiles\wiki")
    else None
)

# ── Motor-CAD paths ───────────────────────────────────────────────────
MOTORCAD_MOT_DIR: Path | None = (
    Path(r"D:\SRM\Motor _CAD\ScriptFiles")
    if os.path.exists(r"D:\SRM\Motor _CAD\ScriptFiles")
    else None
)

# Reference files shipped with this project
REFERENCE_MOT: Path = PROJECT_ROOT / "SynRM_45kW_IE5.mot"
REFERENCE_OPTIMIZER: Path = PROJECT_ROOT / "optimize_synrm_v4.py"

# ── LLM / Opencode ────────────────────────────────────────────────────
LLM_API_KEY: str | None = os.getenv("OPENCODE_API_KEY")
LLM_BASE_URL: str = "https://opencode.ai/zen/v1"
LLM_MODEL: str = "deepseek-v4-flash-free"

# Model per subsystem
MODEL_DEFAULT: str = LLM_MODEL
MODEL_RESEARCH: str = LLM_MODEL
MODEL_SYNTHESIS: str = LLM_MODEL
MODEL_CALCULATE: str = LLM_MODEL
MODEL_DESIGN: str = LLM_MODEL

# ── Agent configuration ───────────────────────────────────────────────
AgentMode = Literal["auto", "manual", "approval"]

ORCHESTRATOR_INSTRUCTIONS: str = """\
You are the **motor-deepagent** orchestrator — a terminal-first engineering assistant.

Your job is to:
1. Understand the user's request.
2. Classify the task (repo/coding, wiki, research, experiment, or mixed).
3. Build a high-level plan.
4. Delegate to the appropriate subsystem (RepoCodingAgent, WikiManager, ResearchSubgraph, ExecutionLayer).
5. Synthesize a final response for the user.

You have access to:
- Repo Coding Subagent for code inspection and edits.
- Wiki Manager for durable project knowledge.
- Research Subgraph for structured multi-source research.
- Experiment Runner for executing scripts and collecting results.

**Rules:**
- Always inspect before editing.
- Keep changes minimal and preserve existing style.
- Surface uncertainty rather than guessing.
- Return structured artifact summaries in your responses.
"""

# ── Filesystem backend (for DeepAgent SDK CompositeBackend) ───────────
# These map virtual paths to real filesystem locations.
BACKEND_ROUTES: dict[str, str] = {
    "/workspace/": str(PROJECT_ROOT / "workspace"),
    "/repo/": str(PROJECT_ROOT),
}


# ── LLM client factory ────────────────────────────────────────────────


def get_llm_client() -> OpenAI:
    """Return an OpenAI-compatible client pointed at Opencode."""
    from openai import OpenAI

    api_key = LLM_API_KEY or os.getenv("OPENCODE_API_KEY") or "sk-placeholder"
    return OpenAI(base_url=LLM_BASE_URL, api_key=api_key)


__all__ = [
    "PROJECT_ROOT",
    "WORKSPACE_ROOT",
    "WIKI_ROOT",
    "EXPERIMENTS_ROOT",
    "RESEARCH_CACHE",
    "SCRATCH_ROOT",
    "LEGACY_WIKI_ROOT",
    "MOTORCAD_MOT_DIR",
    "REFERENCE_MOT",
    "REFERENCE_OPTIMIZER",
    "LLM_API_KEY",
    "LLM_BASE_URL",
    "LLM_MODEL",
    "MODEL_DEFAULT",
    "MODEL_RESEARCH",
    "MODEL_SYNTHESIS",
    "MODEL_CALCULATE",
    "MODEL_DESIGN",
    "get_llm_client",
]
