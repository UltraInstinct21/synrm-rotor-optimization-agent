"""Wiki Manager — read, select, merge, and update wiki pages."""

from __future__ import annotations

from pathlib import Path

from src.artifacts.wiki_update_plan import WikiUpdatePlan
from src.config import settings


def list_pages(wiki_root: Path | None = None) -> list[Path]:
    """Return all markdown pages under *wiki_root* sorted by path."""
    root = wiki_root or settings.WIKI_ROOT
    if not root.exists():
        return []
    return sorted(root.rglob("*.md"))


def read_page(path: Path | str) -> str | None:
    """Return the text content of a wiki page, or None if missing."""
    p = Path(path) if isinstance(path, str) else path
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8")


def page_summary(path: Path) -> dict:
    """Return a lightweight summary of a wiki page (path, title, size)."""
    title = path.stem.replace("_", " ").title()
    size = path.stat().st_size if path.exists() else 0
    return {
        "path": str(path.relative_to(settings.WIKI_ROOT)),
        "title": title,
        "size_bytes": size,
    }


def apply_update_plan(plan: WikiUpdatePlan, wiki_root: Path | None = None) -> list[str]:
    """Execute a WikiUpdatePlan — create/update pages.

    Returns a list of status messages describing what was done.

    This is a *structured* updater: it appends new sections and flags
    sections that need manual review.  It does NOT do free-form LLM
    rewrites of entire pages by default.
    """
    root = wiki_root or settings.WIKI_ROOT
    messages: list[str] = []

    for section in plan.new_sections:
        page_path = root / section.page
        if not page_path.suffix:
            page_path = page_path.with_suffix(".md")

        page_path.parent.mkdir(parents=True, exist_ok=True)

        heading = section.heading.lstrip("#").strip()
        content = f"\n## {heading}\n\n{section.content_summary}\n"

        if page_path.exists():
            existing = page_path.read_text(encoding="utf-8")
            if heading in existing:
                messages.append(
                    f"⚠️  Section '{heading}' already exists in {section.page}. "
                    "Manual merge recommended."
                )
            else:
                page_path.write_text(existing.rstrip() + "\n" + content, encoding="utf-8")
                messages.append(f"✅  Appended section '{heading}' to {section.page}")
        else:
            frontmatter = f"---\ntitle: {heading}\ncreated: {plan.created_at}\n---\n"
            page_path.write_text(frontmatter + content, encoding="utf-8")
            messages.append(f"✅  Created new page {section.page} with section '{heading}'")

    for edit in plan.edits_to_existing_sections:
        page_path = root / edit.page
        if not page_path.suffix:
            page_path = page_path.with_suffix(".md")

        if not page_path.exists():
            messages.append(f"⚠️  Cannot edit — {edit.page} does not exist")
            continue

        messages.append(
            f"📝  Manual review needed for '{edit.heading}' in {edit.page}: "
            f"{edit.change_summary}"
        )

    return messages
