"""Default chat handler — routes input through the agent graph."""

from __future__ import annotations
from typing import TYPE_CHECKING

from apps.cli.streaming import StreamHandler
from src.agent.runtime import run_request_graph_streamed

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle free-form chat input (no /prefix)."""
    if not args.strip():
        return

    ctx.session.stats.request_count += 1
    ctx.session.save_message("user", args)

    handler = StreamHandler(ctx.renderer)
    synthesis = await handler.handle_stream(
        run_request_graph_streamed(args, thread_id=ctx.session.thread_id)
    )

    if synthesis:
        ctx.session.save_message("assistant", synthesis)