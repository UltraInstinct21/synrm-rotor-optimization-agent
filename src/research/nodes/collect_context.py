"""Node 2: Collect context — scan wiki, local docs, and notes for relevant sources."""

from __future__ import annotations

from pathlib import Path

from src.config import settings
from src.research.state import ResearchState


def _list_wiki_pages(wiki_root: Path) -> list[Path]:
    """Return all .md files under wiki root."""
    if not wiki_root.exists():
        return []
    return sorted(wiki_root.rglob("*.md"))


def _read_page(path: Path) -> str | None:
    """Read a wiki page, returning None on failure or oversized files."""
    try:
        if path.stat().st_size > 1_048_576:  # Skip files > 1MB
            return None
        return path.read_text(encoding="utf-8", errors="ignore")
    except (OSError, IOError):
        return None


def collect_context(state: ResearchState) -> dict:
    """Gather candidate sources from the wiki and local docs."""
    domain_terms = state.get("domain_terms", [])
    question = state.get("normalized_question") or state.get("question", "")
    question_lower = question.lower()

    wiki_sources: list[dict[str, str]] = []
    wiki_root = settings.WIKI_ROOT

    # Scan wiki pages for relevance.
    for page_path in _list_wiki_pages(wiki_root):
        content = _read_page(page_path)
        if not content:
            continue

        title = page_path.stem.replace("_", " ").lower()
        content_lower = content.lower()
        matches = any(
            term.lower() in content_lower or term.lower() in title
            for term in domain_terms + [question_lower]
        )

        if matches:
            wiki_sources.append({
                "title": page_path.stem.replace("_", " ").title(),
                "type": "wiki",
                "path_or_url": str(page_path),
                "content_snippet": content[:2000],
            })

    msg = f"Collected {len(wiki_sources)} candidate wiki sources."

    return {
        "wiki_context": wiki_sources,
        "all_collected_sources": wiki_sources,
        "messages": [msg],
    }
