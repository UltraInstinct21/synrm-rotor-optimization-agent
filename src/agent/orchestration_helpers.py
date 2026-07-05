"""Orchestration helpers — task classification, plan building, artifact handoff."""

from __future__ import annotations

from typing import Literal

from src.artifacts import (
    CodeReport,
    ExperimentReport,
    ResearchReport,
    WikiUpdatePlan,
)

# ── Task classification ───────────────────────────────────────────────

TaskCategory = Literal[
    "repo_coding",
    "wiki_maintenance",
    "research",
    "experiment",
    "mixed",
    "question",
]


def classify_request(request: str) -> TaskCategory:
    """Roughly classify a user request by keyword matching.

    This is a simple heuristic — the orchestrator agent will refine it.
    """
    req_lower = request.lower()

    has_code_keywords = any(
        kw in req_lower
        for kw in [
            "inspect",
            "find",
            "code",
            "function",
            "class",
            "module",
            "edit",
            "patch",
            "refactor",
            "implement",
            "add",
            "modify",
            "change",
            "fix",
            "bug",
            "config",
        ]
    )
    has_wiki_keywords = any(
        kw in req_lower
        for kw in ["wiki", "note", "document", "page", "update wiki", "knowledge"]
    )
    has_research_keywords = any(
        kw in req_lower
        for kw in [
            "research",
            "paper",
            "read",
            "compare",
            "source",
            "formula",
            "equation",
            "convention",
        ]
    )
    has_experiment_keywords = any(
        kw in req_lower
        for kw in [
            "run",
            "experiment",
            "script",
            "execute",
            "sweep",
            "simulate",
            "result",
            "output",
        ]
    )

    # Count how many categories match
    matches = sum(
        [has_code_keywords, has_wiki_keywords, has_research_keywords, has_experiment_keywords]
    )
    if matches > 1:
        return "mixed"
    if has_code_keywords:
        return "repo_coding"
    if has_wiki_keywords:
        return "wiki_maintenance"
    if has_research_keywords:
        return "research"
    if has_experiment_keywords:
        return "experiment"
    return "question"


# ── Artifact handoff ──────────────────────────────────────────────────


def research_to_wiki_candidates(report: ResearchReport) -> list[str]:
    """Extract wiki update suggestions from a ResearchReport."""
    return report.recommended_wiki_updates


def code_to_wiki_candidates(report: CodeReport) -> list[str]:
    """Extract wiki update suggestions from a CodeReport."""
    return report.wiki_update_candidates


def experiment_to_wiki_candidates(report: ExperimentReport) -> list[str]:
    """Extract wiki logging suggestions from an ExperimentReport."""
    return report.notes_for_wiki
