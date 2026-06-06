"""Obsidian-style wiki reader/writer for knowledge graph persistence."""

import os
import re
from datetime import datetime
from typing import Literal

WIKI_DIR = r"D:\SRM\Motor _CAD\ScriptFiles\wiki"

PageType = Literal["entity", "concept", "source", "synthesis", "query"]


def _type_dir(page_type: PageType) -> str:
    mapping = {
        "entity": "entities",
        "concept": "concepts",
        "source": "sources",
        "synthesis": "synthesis",
        "query": "queries",
    }
    return os.path.join(WIKI_DIR, mapping[page_type])


def _slugify(title: str) -> str:
    """Convert a title to a kebab-case filename slug."""
    s = title.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")[:80]


def page_path(title: str, page_type: PageType) -> str:
    """Full path for a wiki page by title and type."""
    return os.path.join(_type_dir(page_type), f"{_slugify(title)}.md")


def read_page(title: str, page_type: PageType) -> str | None:
    """Read a wiki page by title. Returns None if not found."""
    path = page_path(title, page_type)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return None


def write_page(
    title: str,
    page_type: PageType,
    content: str,
    tags: list[str] | None = None,
    relations: list[str] | None = None,
    source_count: int = 0,
) -> str:
    """Write a wiki page with YAML frontmatter.

    Returns the file path written.
    """
    path = page_path(title, page_type)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    frontmatter = [
        "---",
        f'title: "{title}"',
        f"type: {page_type}",
        f'created: "{datetime.now().strftime("%Y-%m-%d %H:%M")}"',
    ]
    if tags:
        frontmatter.append(f"tags: [{', '.join(tags)}]")
    if source_count:
        frontmatter.append(f"source_count: {source_count}")

    frontmatter.append("---")
    frontmatter.append("")
    frontmatter.append(f"# {title}")
    frontmatter.append("")

    # Append relations as wikilinks at bottom
    body = content.strip()
    if relations:
        body += "\n\n## Relations\n"
        for rel in relations:
            body += f"- [[{rel}]]\n"

    full_content = "\n".join(frontmatter) + body

    with open(path, "w", encoding="utf-8") as f:
        f.write(full_content)

    return path


def update_index():
    """Regenerate index.md from current wiki state."""
    counts = {}
    for pt in ("entities", "concepts", "sources", "synthesis", "queries"):
        d = os.path.join(WIKI_DIR, pt)
        if os.path.isdir(d):
            counts[pt] = len([f for f in os.listdir(d) if f.endswith(".md")])
        else:
            counts[pt] = 0

    total = sum(counts.values())
    lines = [
        "# Wiki Index",
        "",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Total pages: {total}*",
        "",
    ]
    for pt, count in counts.items():
        cap = pt.capitalize()
        lines.append(f"**{cap} ({count})**")
        d = os.path.join(WIKI_DIR, pt)
        if os.path.isdir(d):
            for fn in sorted(os.listdir(d)):
                if fn.endswith(".md"):
                    slug = fn[:-3]
                    lines.append(f"- [[{slug.replace('-', ' ').title()}]]")
        lines.append("")

    path = os.path.join(WIKI_DIR, "index.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path
