"""Tavily Internet Search Tool with Human-In-The-Loop (HITL) approval.

Routing: use this for web / up-to-date / external info (IEEE papers, news,
general questions). For LOCAL project knowledge use `wiki_tool` (single fact)
or `research_subgraph` (multi-source synthesis over workspace/wiki only).
"""

from __future__ import annotations

import json
import os
from typing import Any

from langchain_core.tools import tool

import threading

# Process-wide HITL flag (NOT thread-local): the CLI toggle (/hitl) and the
# agent execution path must observe the same value even when they run on
# different threads or inside asyncio tasks. Guarded by a lock.
_hitl_lock = threading.Lock()
_hitl_enabled: bool = True


def set_hitl_enabled(enabled: bool) -> None:
    """Set global HITL approval mode for external web searches."""
    global _hitl_enabled
    with _hitl_lock:
        _hitl_enabled = bool(enabled)


def get_hitl_enabled() -> bool:
    """Get current HITL approval state."""
    with _hitl_lock:
        return _hitl_enabled


def _headless_approval_default() -> bool:
    """Auto-approve when no interactive terminal exists (servers, tests).

    Controlled by MOTOR_DEEPAGENT_AUTO_APPROVE_SEARCH=1. Defaults to False so
    interactive CLI sessions keep prompting.
    """
    return os.getenv("MOTOR_DEEPAGENT_AUTO_APPROVE_SEARCH", "").lower() in ("1", "true", "yes")


@tool
def tavily_search(
    query: str,
    max_results: int = 5,
    topic: str = "general",
) -> str:
    """Search the WEB for external / up-to-date info (IEEE, benchmarks, news, general Q&A).

    Do NOT use for local project knowledge: single Motor-CAD facts go to
    `wiki_tool(action="search")`; multi-doc local synthesis goes to
    `research_subgraph`. Web search needs human approval per call unless the
    session enabled auto-approve (/hitl off or A[l]ways).

    Args:
        query: Search query string for the web (non-empty, max ~500 chars).
        max_results: Maximum results to return (clamped 1-10, default 5).
        topic: Search topic category ('general' or 'news').

    Returns:
        JSON string containing search results (title, url, snippet) or HITL rejection notice.
    """
    if not query or not query.strip():
        return json.dumps({"status": "error", "error": "query parameter cannot be empty."}, indent=2)
    query = query.strip()[:500]
    try:
        max_results = max(1, min(int(max_results), 10))
    except (TypeError, ValueError):
        return json.dumps({"status": "error", "error": "max_results must be an integer."}, indent=2)
    if topic not in ("general", "news"):
        topic = "general"

    # Human-In-The-Loop Approval Check (decoupled from CLI so headless
    # runtimes — run.py, tests, langgraph server — don't import prompt_toolkit
    # at module scope and don't crash).
    if get_hitl_enabled():
        approved: bool | None = None
        try:
            from apps.cli.theme import get_console
            from apps.cli.display import request_hitl_approval

            console = get_console()
            approved = request_hitl_approval(
                console=console,
                tool_name="tavily_search",
                details={"query": query, "topic": topic},
            )
        except Exception:
            # No interactive console (server/test/headless): fall back to env.
            approved = _headless_approval_default()
            if not approved:
                return json.dumps({
                    "status": "rejected",
                    "reason": "No interactive terminal for HITL approval. Set MOTOR_DEEPAGENT_AUTO_APPROVE_SEARCH=1 or run via CLI with /hitl.",
                    "query": query,
                }, indent=2)
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
