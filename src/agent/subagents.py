"""Subagent definitions — configurations for each delegated subsystem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class SubagentConfig:
    """Configuration for a single subagent/subsystem.

    Attrs mirror what the DeepAgent SDK's Agent constructor expects.
    """

    name: str
    instructions: str
    tools: list[Callable] = field(default_factory=list)
    model: str = "qwen/qwq-32b:free"
    handoffs: list[str] = field(default_factory=list)


# ── Built-in subagents ────────────────────────────────────────────────

REPO_CODING_AGENT = SubagentConfig(
    name="RepoCodingAgent",
    instructions=(
        "You are the Repo Coding Subagent. Inspect code, find relevant files, "
        "make targeted edits, and run lightweight validation. "
        "Always inspect before editing. Keep changes minimal. "
        "Return a CodeReport with files_inspected, files_changed, diff_summary, "
        "and follow_up_needed."
    ),
    # Tools will be attached by the builder based on the runtime context.
)

WIKI_MANAGER_AGENT = SubagentConfig(
    name="WikiManager",
    instructions=(
        "You are the Wiki Manager — the durable knowledge curator. "
        "Read current wiki pages, select correct targets for new knowledge, "
        "merge findings cleanly, and record open questions separately. "
        "Do not dump raw output — normalize before writing."
    ),
)

RESEARCH_AGENT = SubagentConfig(
    name="ResearchSubgraph",
    instructions=(
        "You are the Research Subgraph. Search and read multiple sources, "
        "extract claims/equations/constraints, compare conflicting sources, "
        "and return a structured ResearchReport. "
        "Do not write to the wiki directly."
    ),
)

EXPERIMENT_RUNNER_AGENT = SubagentConfig(
    name="ExperimentRunner",
    instructions=(
        "You are the Experiment Runner. Execute scripts, collect outputs, "
        "extract metrics, and return an ExperimentReport. "
        "Do not edit code — only execute and observe."
    ),
)

# ── Registry ──────────────────────────────────────────────────────────
REGISTRY: dict[str, SubagentConfig] = {
    "RepoCodingAgent": REPO_CODING_AGENT,
    "WikiManager": WIKI_MANAGER_AGENT,
    "ResearchSubgraph": RESEARCH_AGENT,
    "ExperimentRunner": EXPERIMENT_RUNNER_AGENT,
}
