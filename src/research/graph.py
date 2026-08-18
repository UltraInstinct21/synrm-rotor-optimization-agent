"""Streamlined LangGraph research pipeline using Functional API (@entrypoint).

Optimized Pipeline:
    normalize_question -> collect_context -> synthesize_research_report

Reduces LLM API calls from 5 per research query down to 2, drastically lowering
latency, cost, and rate-limit consumption while maintaining structured output quality.
"""

from __future__ import annotations

from typing import Any

from langgraph.func import entrypoint

from src.research.nodes.normalize_question import normalize_question
from src.research.nodes.collect_context import collect_context
from src.research.nodes.synthesize_research_report import synthesize_research_report
from src.research.state import ResearchState, make_initial_state


@entrypoint()
async def _research_pipeline(state: ResearchState) -> dict[str, Any]:
    """Run the optimized 2-stage research pipeline."""
    _step(state, normalize_question)
    _step(state, collect_context)
    _step(state, synthesize_research_report)

    return state.get("report", {
        "question": state.get("question", ""),
        "summary": "Research pipeline completed but produced no report.",
        "confidence": "low",
    })


def _step(state: ResearchState, node_fn) -> None:
    """Apply a node's updates to state in-place with error trapping."""
    try:
        updates = node_fn(state)
        if updates and isinstance(updates, dict):
            for k, v in updates.items():
                if isinstance(v, list) and isinstance(state.get(k), list):
                    state[k].extend(v)
                else:
                    state[k] = v
    except Exception as e:
        node_name = getattr(node_fn, "__name__", str(node_fn))
        state.setdefault("errors", []).append(f"Step '{node_name}' failed: {e}")


async def run_research(question: str) -> dict[str, Any]:
    """Run the optimized research pipeline end-to-end with robust error handling."""
    if not question or not question.strip():
        return {
            "question": "",
            "summary": "Error: Research question cannot be empty.",
            "confidence": "low",
        }
    state = make_initial_state(question)
    try:
        return await _research_pipeline.ainvoke(state)
    except Exception as e:
        return {
            "question": question,
            "summary": f"Research pipeline encountered an unexpected error: {e}",
            "confidence": "low",
            "error": str(e),
        }
