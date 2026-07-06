"""Memory commands — /memory store|search|list|forget."""

from __future__ import annotations

from typing import TYPE_CHECKING

from rich.table import Table

from src.tools.memory.memory_tools import store_memory, search_memory, list_memories, forget_memory

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /memory commands."""
    parts = args.strip().split(maxsplit=2)
    subcmd = parts[0] if parts else "list"

    if subcmd == "store":
        if len(parts) < 3:
            ctx.renderer.print("[yellow]Usage:[/yellow] /memory store <key> <value>")
            return
        result = store_memory(parts[1], parts[2])
        ctx.renderer.print(f"[green]Stored: {parts[1]}[/green]")

    elif subcmd == "search":
        query = parts[1] if len(parts) > 1 else ""
        if not query:
            ctx.renderer.print("[yellow]Usage:[/yellow] /memory search <query>")
            return
        results = search_memory(query)
        if not results:
            ctx.renderer.print(f"[dim]No memories found for '{query}'.[/dim]")
            return
        t = Table(title=f"Memories: {query}", show_header=True, header_style="bold")
        t.add_column("Key", style="cyan")
        t.add_column("Content")
        for mem in results[:20]:
            t.add_row(mem.get("key", "?"), mem.get("content", "")[:80])
        ctx.renderer.console.print(t)

    elif subcmd == "list":
        results = list_memories()
        if not results:
            ctx.renderer.print("[dim]No memories stored.[/dim]")
            return
        t = Table(title="Memory Namespaces", show_header=True, header_style="bold")
        t.add_column("Namespace", style="cyan")
        t.add_column("Count", justify="right")
        for ns in results:
            t.add_row(ns.get("namespace", "default"), str(ns.get("count", 0)))
        ctx.renderer.console.print(t)

    elif subcmd == "forget":
        key = parts[1] if len(parts) > 1 else ""
        if not key:
            ctx.renderer.print("[yellow]Usage:[/yellow] /memory forget <key>")
            return
        forget_memory(key)
        ctx.renderer.print(f"[green]Forgotten: {key}[/green]")

    else:
        ctx.renderer.print("[yellow]Usage:[/yellow] /memory <store|search|list|forget>")