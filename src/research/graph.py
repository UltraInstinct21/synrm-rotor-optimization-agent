"""LangGraph research subgraph compilation.

Builds a linear StateGraph:
  normalize → collect_context → source_selection → read_extract → synthesize → build_report
"""

from __future__ import annotations

import asyncio
from typing import Any

from langgraph.graph import END, StateGraph

from src.research.nodes.normalize_question import normalize_question
from src.research.nodes.collect_context import collect_context
from src.research.nodes.source_selection import source_selection
from src.research.nodes.read_extract import read_extract
from src.research.nodes.synthesize_claims import synthesize_claims
from src.research.nodes.build_report import build_report
from src.research.state import ResearchState, make_initial_state


def build_research_graph() -> StateGraph:
    """Build the research LangGraph.

    Returns a compiled graph ready for ``invoke()`` or ``ainvoke()``.
    """
    builder = StateGraph(ResearchState)

    # Add nodes.
    builder.add_node("normalize_question", normalize_question)
    builder.add_node("collect_context", collect_context)
    builder.add_node("source_selection", source_selection)
    builder.add_node("read_extract", read_extract)
    builder.add_node("synthesize_claims", synthesize_claims)
    builder.add_node("build_report", build_report)

    # Linear flow with shortcuts.
    builder.set_entry_point("normalize_question")

    builder.add_edge("normalize_question", "collect_context")
    builder.add_edge("collect_context", "source_selection")
    builder.add_edge("source_selection", "read_extract")

    # If no sources were selected, skip synthesis and go straight to empty report.
    def _has_sources(state: ResearchState) -> str:
        if state.get("selected_sources"):
            return "synthesize_claims"
        return "build_report"

    builder.add_conditional_edges(
        "read_extract",
        lambda s: "synthesize_claims" if s.get("extracted_claims") else "build_report",
        {
            "synthesize_claims": "synthesize_claims",
            "build_report": "build_report",
        },
    )

    builder.add_edge("synthesize_claims", "build_report")
    builder.add_edge("build_report", END)

    return builder.compile()


# ── Compiled singleton ────────────────────────────────────────────────
_research_graph: Any | None = None


def get_research_graph() -> Any:
    """Return the compiled research graph (cached)."""
    global _research_graph
    if _research_graph is None:
        _research_graph = build_research_graph()
    return _research_graph


async def run_research(question: str) -> dict[str, Any]:
    """Run the research subgraph end-to-end for a question.

    This is the main entry point called from the orchestrator.
    """
    import functools

    graph = get_research_graph()
    initial = make_initial_state(question)

    # LangGraph's ainvoke — run in thread pool to avoid blocking.
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None,
        functools.partial(graph.invoke, initial),
    )

    # Return the report dict from the final state.
    return result.get("report", {
        "question": question,
        "summary": "Research graph completed but produced no report.",
        "confidence": "low",
    })
