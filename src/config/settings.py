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

# ── LLM / OpenRouter ──────────────────────────────────────────────────
OPENROUTER_API_KEY: str | None = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

# Model per subsystem (matching the old project's convention)
MODEL_DEFAULT: str = "qwen/qwq-32b:free"
MODEL_RESEARCH: str = "qwen/qwq-32b:free"
MODEL_SYNTHESIS: str = "nousresearch/hermes-3-llama-3.1-405b:free"
MODEL_CALCULATE: str = "google/gemini-2.0-flash-exp:free"
MODEL_DESIGN: str = "qwen/qwq-32b:free"

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
