"""System commands — /help, /clear, /compact, /model, /status, /quit."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from rich.table import Table

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def handle_help(ctx: CommandContext, args: str) -> None:
    """Show all available commands in a table."""
    t = Table(title="Commands", show_header=True, header_style="bold")
    t.add_column("Command", style="cyan")
    t.add_column("Description")
    t.add_column("Usage", style="dim")
    for cmd in ctx.registry.all:
        t.add_row(cmd.name, cmd.description, cmd.usage)
    t.add_row("(any text)", "Chat with the agent", "")
    ctx.renderer.console.print(t)


async def handle_clear(ctx: CommandContext, args: str) -> None:
    """Clear the terminal screen."""
    ctx.renderer.console.clear()


async def handle_compact(ctx: CommandContext, args: str) -> None:
    """Summarize conversation and compress history."""
    count = len(ctx.session.history)
    if count == 0:
        ctx.renderer.print("[dim]No conversation to compact.[/dim]")
        return
    ctx.renderer.print(f"[yellow]Compacting {count} messages...[/yellow]")
    # For now, clear history and keep a summary note
    ctx.session.history.clear()
    ctx.session.save()
    ctx.renderer.print("[green]Conversation compacted. History cleared.[/green]")


async def handle_model(ctx: CommandContext, args: str) -> None:
    """Show or switch the active LLM model."""
    if args.strip():
        ctx.session.model = args.strip()
        ctx.session.save()
        ctx.renderer.print(f"[green]Model switched to: [cyan]{args.strip()}[/cyan][/green]")
    else:
        ctx.renderer.print(f"Current model: [cyan]{ctx.session.model}[/cyan]")
        ctx.renderer.print("[dim]Usage: /model <model-name>[/dim]")



async def handle_status(ctx: CommandContext, args: str) -> None:
    """Show session stats."""
    s = ctx.session.stats
    ctx.renderer.print(f"  Conversation: [cyan]{ctx.session.conversation_id}[/cyan]")
    ctx.renderer.print(f"  Thread:       [cyan]{ctx.session.thread_id}[/cyan]")
    ctx.renderer.print(f"  Model:        [cyan]{ctx.session.model}[/cyan]")
    ctx.renderer.print(f"  Requests:     [yellow]{s.request_count}[/yellow]")
    ctx.renderer.print(f"  Uptime:       [green]{ctx.session.uptime_str()}[/green]")
    mc = ctx.session.motor_instance
    motor_status = "[green]connected[/green]" if mc else "[dim]not connected[/dim]"
    ctx.renderer.print(f"  Motor-CAD:    {motor_status}")


async def handle_quit(ctx: CommandContext, args: str) -> None:
    """Exit the CLI cleanly."""
    ctx.session.save()
    ctx.renderer.print("[dim]Goodbye.[/dim]")
    sys.exit(0)