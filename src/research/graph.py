"""LangGraph research pipeline using the Functional API (@entrypoint).

Nodes run sequentially:
    normalize -> collect_context -> source_selection -> read_extract
        -> [synthesize_claims if claims exist] -> build_report
"""

from __future__ import annotations

from typing import Any

from langgraph.func import entrypoint

from src.research.nodes.normalize_question import normalize_question
from src.research.nodes.collect_context import collect_context
from src.research.nodes.source_selection import source_selection
from src.research.nodes.read_extract import read_extract
from src.research.nodes.synthesize_claims import synthesize_claims
from src.research.nodes.build_report import build_report
from src.research.state import ResearchState, make_initial_state


@entrypoint()
async def _research_pipeline(state: ResearchState) -> dict[str, Any]:
    """Run the research pipeline — async entrypoint, sequential nodes."""
    _step(state, normalize_question)
    _step(state, collect_context)
    _step(state, source_selection)
    _step(state, read_extract)

    if state.get("extracted_claims"):
        _step(state, synthesize_claims)

    _step(state, build_report)

    return state.get("report", {
        "question": state.get("question", ""),
        "summary": "Research pipeline completed but produced no report.",
        "confidence": "low",
    })


def _step(state: ResearchState, node_fn) -> None:
    """Apply a node's updates to state in-place."""
    state.update(node_fn(state))


async def run_research(question: str) -> dict[str, Any]:
    """Run the research pipeline end-to-end."""
    state = make_initial_state(question)
    return await _research_pipeline.ainvoke(state)
