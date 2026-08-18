"""Tavily Internet Search Tool with Human-In-The-Loop (HITL) approval."""

from __future__ import annotations

import json
import os
import sys
from typing import Any

from langchain_core.tools import tool

import threading

_hitl_local = threading.local()
_hitl_local.enabled = True


def set_hitl_enabled(enabled: bool) -> None:
    """Set global HITL approval mode for external web searches."""
    _hitl_local.enabled = enabled


def get_hitl_enabled() -> bool:
    """Get current HITL approval state."""
    return getattr(_hitl_local, 'enabled', True)


@tool
def tavily_search(
    query: str,
    max_results: int = 5,
    topic: str = "general",
) -> str:
    """Search the web for ANY information (general questions, news, technical topics, non-motor topics, etc.).

    Args:
        query: Search query string for the web.
        max_results: Maximum number of search results to return (default 5).
        topic: Search topic category ('general' or 'news').

    Returns:
        JSON string containing search results (title, url, snippet) or HITL rejection notice.
    """
    # Human-In-The-Loop Approval Check
    if get_hitl_enabled():
        from apps.cli.theme import get_console
        from apps.cli.display import request_hitl_approval

        console = get_console()
        approved = request_hitl_approval(
            console=console,
            tool_name="tavily_search",
            details={"query": query, "topic": topic},
        )
        if not approved:
            return json.dumps({
                "status": "rejected",
                "reason": "Web search request was declined by the human user in HITL approval check.",
                "query": query,
            }, indent=2)

    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return json.dumps({
            "status": "error",
            "error": "TAVILY_API_KEY is not set. Please set TAVILY_API_KEY in your environment or .env file.",
            "query": query,
        }, indent=2)

    try:
        from tavily import TavilyClient

        client = TavilyClient(api_key=api_key)
        res = client.search(query=query, max_results=max_results, topic=topic)
        results = res.get("results", [])

        parsed_results = [
            {
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "snippet": r.get("content", ""),
            }
            for r in results
        ]

        return json.dumps({
            "status": "success",
            "query": query,
            "results_count": len(parsed_results),
            "results": parsed_results,
        }, indent=2)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Tavily search failed: {e}",
            "query": query,
        }, indent=2)


__all__ = ["tavily_search", "set_hitl_enabled", "get_hitl_enabled"]
