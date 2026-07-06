"""Wiki commands — /wiki list|read|search."""

from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING

from rich.table import Table
from src.config import settings
from src.tools.wiki.update_wiki import list_pages, read_page, page_summary

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /wiki commands."""
    parts = args.strip().split(maxsplit=1)
    subcmd = parts[0] if parts else "list"
    rest = parts[1] if len(parts) > 1 else ""

    if subcmd == "list":
        await _list_pages(ctx)
    elif subcmd == "read":
        await _read_page(ctx, rest)
    elif subcmd == "search":
        await _search_pages(ctx, rest)
    else:
        ctx.renderer.print("[yellow]Usage:[/yellow] /wiki list | /wiki read <page> | /wiki search <query>")



async def _list_pages(ctx: CommandContext) -> None:
    """List all wiki pages in a table."""
    pages = list_pages()
    if not pages:
        ctx.renderer.print("[dim]No wiki pages found.[/dim]")
        return

    t = Table(title="Wiki Pages", show_header=True, header_style="bold")
    t.add_column("Page", style="cyan")
    t.add_column("Title")
    t.add_column("Size", justify="right")
    for p in pages:
        info = page_summary(p)
        t.add_row(info["path"], info["title"], f"{info['size_bytes']} B")
    ctx.renderer.console.print(t)


async def _read_page(ctx: CommandContext, page: str) -> None:
    """Read and display a wiki page."""
    if not page:
        ctx.renderer.print("[yellow]Usage:[/yellow] /wiki read <page-path>")
        return
    page_path = settings.WIKI_ROOT / page
    if not page_path.suffix:
        page_path = page_path.with_suffix(".md")
    content = read_page(page_path)
    if content is None:
        ctx.renderer.print(f"[red]Page not found:[/red] {page}")
        return
    ctx.renderer.markdown(content)


async def _search_pages(ctx: CommandContext, query: str) -> None:
    """Search wiki pages for a query string."""
    if not query:
        ctx.renderer.print("[yellow]Usage:[/yellow] /wiki search <query>")
        return
    pages = list_pages()
    matches = []
    for p in pages:
        content = read_page(p)
        if content and query.lower() in content.lower():
            info = page_summary(p)
            for line in content.split("\n"):
                if query.lower() in line.lower():
                    matches.append((info["path"], line.strip()[:100]))
                    break

    if not matches:
        ctx.renderer.print(f"[dim]No matches for '{query}'.[/dim]")
        return

    t = Table(title=f"Search: {query}", show_header=True, header_style="bold")
    t.add_column("Page", style="cyan")
    t.add_column("Match")
    for path, line in matches:
        t.add_row(path, line)
    ctx.renderer.console.print(t)