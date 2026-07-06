"""Research command — /research <query>."""

from __future__ import annotations

from typing import TYPE_CHECKING

from apps.cli.streaming import StreamHandler
from src.agent.runtime import run_request_graph_streamed

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /research command — delegates through the agent graph."""
    if not args.strip():
        ctx.renderer.print("[yellow]Usage:[/yellow] /research <query>")
        return

    ctx.session.stats.request_count += 1
    # Prepend "research:" to hint at the category
    query = args.strip()
    handler = StreamHandler(ctx.renderer)
    synthesis = await handler.handle_stream(
        run_request_graph_streamed(f"research: {query}", thread_id=ctx.session.thread_id)
    )
    if synthesis:
        ctx.session.save_message("assistant", synthesis)