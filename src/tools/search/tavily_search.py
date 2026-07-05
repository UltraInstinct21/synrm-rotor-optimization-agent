"""Tavily web search tool for the Agents SDK."""

from __future__ import annotations

import os

import httpx
from agents import function_tool, RunContextWrapper
from markdownify import markdownify

from src.config import settings


def _get_tavily_key() -> str:
    """Return the Tavily API key from settings or env."""
    key = os.getenv("TAVILY_API_KEY")
    if not key:
        raise ValueError(
            "TAVILY_API_KEY not set. Add it to .env or set the env var."
        )
    return key


def _fetch_webpage(url: str, timeout: float = 10.0) -> str:
    """Fetch a URL and convert HTML to markdown."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        )
    }
    try:
        r = httpx.get(url, headers=headers, timeout=timeout, follow_redirects=True)
        r.raise_for_status()
        return markdownify(r.text)
    except Exception as exc:
        return f"Error fetching {url}: {exc}"


@function_tool
async def tavily_search(
    ctx: RunContextWrapper,
    query: str,
    max_results: int = 3,
    topic: str = "general",
) -> str:
    """Search the web for information on a given query.

    Uses Tavily to discover relevant URLs, then fetches and returns full
    webpage content as markdown.

    Args:
        query: Search query to execute.
        max_results: Maximum number of results to return (default 3, max 10).
        topic: Topic filter - 'general', 'news', or 'finance' (default 'general').

    Returns:
        Formatted search results with full webpage content.
    """
    # Import client here to keep module-level import optional.
    from tavily import TavilyClient

    client = TavilyClient(api_key=_get_tavily_key())
    try:
        search_results = client.search(
            query,
            max_results=min(max_results, 10),
            topic=topic,
        )
    except Exception as exc:
        return f"Tavily search failed: {exc}"

    raw_results = search_results.get("results", [])
    if not raw_results:
        return f"No results found for '{query}'."

    parts: list[str] = []
    for result in raw_results:
        url = result.get("url", "")
        title = result.get("title", "")
        content = _fetch_webpage(url) if url else "No URL."
        parts.append(f"## {title}\n**URL:** {url}\n\n{content}\n---")

    return (
        f"Found {len(parts)} result(s) for '{query}':\n\n"
        + "\n".join(parts)
    )
