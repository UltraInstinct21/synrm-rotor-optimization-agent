"""Research Subgraph wrapper — wraps the LangGraph research pipeline for Deep Agents."""
from __future__ import annotations

import json

from langchain_core.tools import tool


@tool
async def research_subgraph(question: str) -> str:
    """Research a motor engineering question using the LangGraph research pipeline.

    Use this tool when you need to find technical information about motor design,
    materials, manufacturing processes, or engineering standards.
    """
    from src.research.graph import run_research

    if not question or not question.strip():
        return json.dumps({
            "status": "error",
            "error": "Question parameter cannot be empty.",
        }, indent=2)

    try:
        result = await run_research(question)
        return json.dumps(result, indent=2, default=str)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Failed to execute research subgraph: {e}",
            "question": question,
        }, indent=2)


__all__ = ["research_subgraph"]