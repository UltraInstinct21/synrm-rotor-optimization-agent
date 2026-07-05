"""Research state — LangGraph TypedDict for the research subgraph."""

from __future__ import annotations

from typing import Annotated, Any, TypedDict

from langgraph.graph.message import add_messages


class ResearchState(TypedDict):
    """State carried through the research subgraph nodes."""

    # ── Input ───────────────────────────────────────────────────────
    question: str
    """Original user research question."""

    # ── Normalize ───────────────────────────────────────────────────
    normalized_question: str
    """Clarified, scoped version of the question."""
    domain_terms: list[str]
    """Key engineering terms identified in the question."""

    # ── Collect context ─────────────────────────────────────────────
    wiki_context: list[dict[str, str]]
    """Relevant wiki pages read: [{path, title, content_snippet}]."""
    local_docs_context: list[dict[str, str]]
    """Relevant local docs/notes found."""
    all_collected_sources: list[dict[str, str]]
    """Merged list of candidate sources: [{title, type, path_or_url}]."""

    # ── Source selection ────────────────────────────────────────────
    selected_sources: list[dict[str, str]]
    """Subset of sources chosen for deep reading."""

    # ── Read / extract ──────────────────────────────────────────────
    extracted_claims: list[str]
    """Claims extracted from deep reading."""
    extracted_equations: list[str]
    """Equations/formulas extracted."""
    extracted_notes: list[str]
    """Free-form extraction notes."""

    # ── Synthesize ──────────────────────────────────────────────────
    synthesized_claims: list[str]
    """Claims after cross-source merging."""
    conflicts: list[str]
    """Disagreements or uncertainties between sources."""

    # ── Build report ────────────────────────────────────────────────
    report_summary: str
    """Final high-level summary."""
    report_confidence: str
    """high | medium | low"""
    report: dict[str, Any]
    """Final ResearchReport-compatible dict."""

    # ── Messages ────────────────────────────────────────────────────
    messages: Annotated[list, add_messages]
    """LangGraph message list (for tracing)."""


def make_initial_state(question: str) -> ResearchState:
    """Return a fresh ResearchState with defaults."""
    return {
        "question": question,
        "normalized_question": "",
        "domain_terms": [],
        "wiki_context": [],
        "local_docs_context": [],
        "all_collected_sources": [],
        "selected_sources": [],
        "extracted_claims": [],
        "extracted_equations": [],
        "extracted_notes": [],
        "synthesized_claims": [],
        "conflicts": [],
        "report_summary": "",
        "report_confidence": "medium",
        "report": {},
        "messages": [],
    }
