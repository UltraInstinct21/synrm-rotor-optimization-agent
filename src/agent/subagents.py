"""Subagent definitions — configurations for each delegated subsystem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

from src.tools.filesys import read_file, write_file, grep_files, list_directory
from src.tools.memory import (
    store_memory,
    search_memory,
    list_memories,
    forget_memory,
)
from src.tools.search import tavily_search
from src.tools.shell import run_shell


@dataclass
class SubagentConfig:
    """Configuration for a single subagent/subsystem.

    Attrs mirror what the DeepAgent SDK's Agent constructor expects.
    """

    name: str
    instructions: str
    tools: list[Callable] = field(default_factory=list)
    model: str = ""
    handoffs: list[str] = field(default_factory=list)


# ── Built-in subagents ────────────────────────────────────────────────

REPO_CODING_AGENT = SubagentConfig(
    name="RepoCodingAgent",
    instructions=(
        "You are the Repo Coding Subagent. Inspect code, find relevant files, "
        "make targeted edits, and run lightweight validation. "
        "Always inspect before editing. Keep changes minimal. "
        "Return a CodeReport with files_inspected, files_changed, diff_summary, "
        "and follow_up_needed.\n\n"
        "You have filesystem tools (read_file, write_file, grep_files, list_directory) "
        "and memory tools available. Use filesystem tools to inspect and edit code. "
        "Use memory tools to remember facts across sessions."
    ),
    tools=[read_file, write_file, grep_files, list_directory,
           store_memory, search_memory, list_memories, forget_memory],
)

WIKI_MANAGER_AGENT = SubagentConfig(
    name="WikiManager",
    instructions=(
        "You are the Wiki Manager — the durable knowledge curator. "
        "Read current wiki pages, select correct targets for new knowledge, "
        "merge findings cleanly, and record open questions separately. "
        "Do not dump raw output — normalize before writing.\n\n"
        "Use filesystem tools (read_file, write_file, list_directory, grep_files) "
        "to read and update wiki pages. Use memory tools to track what pages "
        "you've read and updated across sessions."
    ),
    tools=[read_file, write_file, grep_files, list_directory,
           store_memory, search_memory, list_memories, forget_memory],
)

RESEARCH_AGENT = SubagentConfig(
    name="ResearchSubgraph",
    instructions=(
        "You are the Research Subgraph. Search and read multiple sources, "
        "extract claims/equations/constraints, compare conflicting sources, "
        "and return a structured ResearchReport. "
        "Do not write to the wiki directly.\n\n"
        "Use tavily_search to find web sources and papers. "
        "Use filesystem tools to read local docs. "
        "Use memory tools to cache source evaluations across research runs."
    ),
    tools=[tavily_search, read_file, grep_files,
           store_memory, search_memory, list_memories, forget_memory],
)

EXPERIMENT_RUNNER_AGENT = SubagentConfig(
    name="ExperimentRunner",
    instructions=(
        "You are the Experiment Runner. Execute scripts, collect outputs, "
        "extract metrics, and return an ExperimentReport. "
        "Do not edit code — only execute and observe.\n\n"
        "Use run_shell to execute commands and scripts. "
        "Use read_file and list_directory to inspect script contents and "
        "output files before reporting results."
    ),
    tools=[run_shell, read_file, list_directory, grep_files],
)

# ── Registry ──────────────────────────────────────────────────────────
REGISTRY: dict[str, SubagentConfig] = {
    "RepoCodingAgent": REPO_CODING_AGENT,
    "WikiManager": WIKI_MANAGER_AGENT,
    "ResearchSubgraph": RESEARCH_AGENT,
    "ExperimentRunner": EXPERIMENT_RUNNER_AGENT,
}
