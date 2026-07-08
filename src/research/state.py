"""Research state — TypedDict for the research subgraph."""

from __future__ import annotations

from typing import Any, TypedDict


class ResearchState(TypedDict):
    """State carried through the research subgraph nodes."""

    question: str
    normalized_question: str
    domain_terms: list[str]
    wiki_context: list[dict[str, str]]
    local_docs_context: list[dict[str, str]]
    all_collected_sources: list[dict[str, str]]
    selected_sources: list[dict[str, str]]
    extracted_claims: list[str]
    extracted_equations: list[str]
    extracted_notes: list[str]
    synthesized_claims: list[str]
    conflicts: list[str]
    report_summary: str
    report_confidence: str
    report: dict[str, Any]
    messages: list[str]


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
