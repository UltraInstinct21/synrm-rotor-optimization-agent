"""Node 2: Collect context — scan wiki, local docs, and notes for relevant sources."""

from __future__ import annotations

from pathlib import Path

from langchain_core.messages import HumanMessage, SystemMessage

from src.config import settings
from src.research.state import ResearchState
from src.tools.wiki import list_pages, read_page


def collect_context(state: ResearchState) -> dict:
    """Gather candidate sources from the wiki and local docs.

    For Phase 2, this reads wiki pages whose titles match domain terms.
    Future versions may add web search, PDF reading, etc.
    """
    domain_terms = state.get("domain_terms", [])
    question = state.get("normalized_question", state["question"])
    question_lower = question.lower()

    wiki_sources: list[dict[str, str]] = []
    wiki_root = settings.WIKI_ROOT

    # Scan wiki pages for relevance.
    for page_path in list_pages(wiki_root):
        content = read_page(page_path)
        if not content:
            continue

        title = page_path.stem.replace("_", " ").lower()
        rel_path = str(page_path.relative_to(wiki_root))

        # Check if any domain term or question keyword appears.
        content_lower = content.lower()
        matches = any(
            term.lower() in content_lower or term.lower() in title
            for term in domain_terms + [question_lower]
        )

        if matches or len(domain_terms) == 0:
            wiki_sources.append(
                {
                    "title": page_path.stem.replace("_", " ").title(),
                    "type": "wiki",
                    "path_or_url": str(page_path),
                    "content_snippet": content[:2000],
                }
            )

    # Check legacy wiki too.
    legacy = settings.LEGACY_WIKI_ROOT
    if legacy and legacy.exists():
        for md_file in legacy.rglob("*.md"):
            if not md_file.is_file():
                continue
            try:
                text = md_file.read_text(encoding="utf-8", errors="ignore")
                if any(term.lower() in text.lower() for term in domain_terms):
                    wiki_sources.append(
                        {
                            "title": md_file.stem.replace("_", " ").title(),
                            "type": "wiki",
                            "path_or_url": str(md_file),
                            "content_snippet": text[:2000],
                        }
                    )
            except Exception:
                pass

    return {
        "wiki_context": wiki_sources,
        "all_collected_sources": wiki_sources,
        "messages": [
            SystemMessage(
                content=f"Collected {len(wiki_sources)} candidate wiki sources."
            ),
        ],
    }
