"""Research Subgraph wrapper — wraps the LangGraph research pipeline for Deep Agents."""
from __future__ import annotations

import json

from langchain_core.tools import tool

_MAX_REPORT_CHARS = 12000
# Must match the actual report dict keys produced by synthesize_research_report.
_TRUNCATABLE_LIST_KEYS = (
    "sources",
    "extracted_claims",
    "equations_or_constraints",
    "conflicts_or_uncertainties",
    "recommended_wiki_updates",
    "recommended_code_targets",
    "domain_terms",
    "messages",
)


def _truncate_report(result: dict) -> str:
    """Serialize the report, trimming oversized list fields to cap the payload."""
    text = json.dumps(result, indent=2, default=str)
    if len(text) <= _MAX_REPORT_CHARS:
        return text

    trimmed = dict(result)
    for key in _TRUNCATABLE_LIST_KEYS:
        value = trimmed.get(key)
        if isinstance(value, list) and len(value) > 5:
            trimmed[key] = value[:5] + [f"... truncated ({len(value) - 5} more)"]
    text = json.dumps(trimmed, indent=2, default=str)
    if len(text) > _MAX_REPORT_CHARS:
        text = text[:_MAX_REPORT_CHARS] + "\n... [report truncated to fit context]"
    return text


@tool
async def research_subgraph(question: str) -> str:
    """Synthesize a LOCAL-only technical answer from workspace/wiki (no web).

    Use ONLY for genuine multi-source questions that need combining SEVERAL
    wiki documents (e.g. barrier geometry + constraints + workflow). For a
    single fact or parameter name use `wiki_tool(action="search")`; for web /
    up-to-date info use `tavily_search`.

    Args:
        question: Research question (non-empty). Be specific; include exact
            parameter names when relevant.

    Returns:
        Truncated JSON research report (summary, claims, equations, conflicts,
        confidence, sources).
    """
    from src.research.graph import run_research

    if not question or not question.strip():
        return json.dumps({
            "status": "error",
            "error": "Question parameter cannot be empty.",
        }, indent=2)

    try:
        result = await run_research(question)
        return _truncate_report(result if isinstance(result, dict) else {"report": result})
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Failed to execute research subgraph: {e}",
            "question": question,
        }, indent=2)


__all__ = ["research_subgraph"]