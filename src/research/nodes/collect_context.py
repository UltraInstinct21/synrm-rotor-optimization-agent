"""Node 2: Collect context — scan wiki, local docs, and notes for relevant sources."""

from __future__ import annotations

import re
from pathlib import Path

from src.config import settings
from src.research.state import ResearchState

# Mirror wiki_tool: never scan the ~13k per-parameter detail sheets (64 MB).
# Category sheets already name every parameter; exact sheets are fetched on
# demand via wiki_tool read.
_SKIP_DIRS = {"parameters"}
_MAX_SOURCES = 8
_SNIPPET_CHARS = 2000


def _list_wiki_pages(wiki_root: Path) -> list[Path]:
    """Return all indexed .md files under wiki root (skips detail sheets)."""
    if not wiki_root.exists():
        return []
    pages: list[Path] = []
    for p in sorted(wiki_root.rglob("*.md")):
        try:
            if any(part in _SKIP_DIRS for part in p.relative_to(wiki_root).parts):
                continue
            pages.append(p)
        except (OSError, ValueError):
            continue
    return pages


def _read_page(path: Path) -> str | None:
    """Read a wiki page, returning None on failure or oversized files."""
    try:
        if path.stat().st_size > 1_048_576:  # Skip files > 1MB
            return None
        return path.read_text(encoding="utf-8", errors="ignore")
    except (OSError, IOError):
        return None


def _tokenize(text: str) -> set[str]:
    return {t.lower() for t in re.findall(r"[A-Za-z][A-Za-z0-9_\-]+", text) if len(t) > 2}


def collect_context(state: ResearchState) -> dict:
    """Gather top-ranked candidate sources from the wiki (no web access)."""
    domain_terms = [t for t in state.get("domain_terms", []) if t]
    question = state.get("normalized_question") or state.get("question", "")
    query_tokens = _tokenize(question)
    term_tokens = {t.lower() for t in domain_terms}

    wiki_sources: list[dict[str, str]] = []
    wiki_root = settings.WIKI_ROOT

    # Scan indexed wiki pages and score by token overlap + exact-phrase hits.
    scored: list[tuple[int, Path, str]] = []
    for page_path in _list_wiki_pages(wiki_root):
        content = _read_page(page_path)
        if not content:
            continue
        content_lower = content.lower()
        title = page_path.stem.replace("_", " ")
        title_lower = title.lower()
        overlap = len(query_tokens & _tokenize(content_lower)) + len(term_tokens & _tokenize(content_lower))
        phrase_hits = sum(1 for t in list(term_tokens) + [question.lower()] if t and t in content_lower)
        title_hits = sum(1 for t in list(term_tokens) + list(query_tokens) if t and t in title_lower)
        score = overlap + phrase_hits * 2 + title_hits * 3
        if score > 0:
            scored.append((score, page_path, content))

    # Deterministic rank: score desc, then shorter path (category sheets win).
    scored.sort(key=lambda item: (-item[0], len(str(item[1]))))
    for score, page_path, content in scored[:_MAX_SOURCES]:
        wiki_sources.append({
            "title": page_path.stem.replace("_", " ").title(),
            "type": "wiki",
            "path_or_url": str(page_path),
            "content_snippet": content[:_SNIPPET_CHARS],
            "relevance_score": str(score),
        })

    msg = f"Collected {len(wiki_sources)} candidate wiki sources (scored from indexed pages, detail sheets skipped)."

    return {
        "wiki_context": wiki_sources,
        "all_collected_sources": wiki_sources,
        "messages": [msg],
    }
