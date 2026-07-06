"""Core REPL — prompt input, dispatch to commands, streaming output."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory

from apps.cli.commands import CommandContext, CommandRegistry, register_all
from apps.cli.rendering import Renderer
from apps.cli.session import Session
from src.config import settings


class SlashCompleter(Completer):
    """Autocomplete for /slash commands."""

    def __init__(self, registry: CommandRegistry) -> None:
        self.registry = registry

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if not text.startswith("/"):
            return
        for name in self.registry.names:
            if name.startswith(text):
                yield Completion(name, start_position=-len(text))


def main() -> None:
    """CLI entry point."""
    # Load .env — must happen before settings reads env vars
    env_path = settings.PROJECT_ROOT / ".env"
    load_dotenv(env_path, override=False)

    # Re-read API key after dotenv load (settings cached None at import time)
    import os
    api_key = os.getenv("OPENCODE_API_KEY")
    if not api_key:
        print("  WARNING: OPENCODE_API_KEY not set. Set it in .env.", file=sys.stderr)
        sys.exit(1)

    # Initialize
    renderer = Renderer()
    session = Session.load(model=settings.MODEL_DEFAULT)
    registry = CommandRegistry()
    ctx = CommandContext(session=session, renderer=renderer, registry=registry)
    register_all(registry, ctx)

    # Check for single-shot mode
    if len(sys.argv) > 1:
        request = " ".join(sys.argv[1:])
        asyncio.run(_single_shot(ctx, request))
        return

    # Interactive REPL
    asyncio.run(_repl(ctx))


async def _single_shot(ctx: CommandContext, request: str) -> None:
    """Process a single request and exit."""
    # Route slash commands to the registry
    if request.startswith("/"):
        parts = request.split(maxsplit=1)
        cmd_name = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        entry = ctx.registry.get(cmd_name)
        if entry:
            await entry.handler(ctx, args)
        else:
            ctx.renderer.print(f"[red]Unknown command:[/red] {cmd_name}")
    else:
        from apps.cli.commands.chat import run as chat_run
        await chat_run(ctx, request)


async def _repl(ctx: CommandContext) -> None:
    """Interactive REPL loop."""
    renderer = ctx.renderer
    session = ctx.session

    renderer.print_header(model=session.model)

    # prompt_toolkit session with autocomplete
    prompt_session = PromptSession(
        history=InMemoryHistory(),
        completer=SlashCompleter(ctx.registry),
        complete_while_typing=True,
    )

    try:
        while True:
            try:
                user_input = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: prompt_session.prompt("  > "),
                )
            except KeyboardInterrupt:
                continue
            except EOFError:
                break

            text = user_input.strip()
            if not text:
                continue

            # Parse command
            if text.startswith("/"):
                parts = text.split(maxsplit=1)
                cmd_name = parts[0]
                args = parts[1] if len(parts) > 1 else ""

                entry = ctx.registry.get(cmd_name)
                if entry:
                    try:
                        await entry.handler(ctx, args)
                    except SystemExit:
                        break
                    except Exception as e:
                        renderer.panel_error(str(e))
                else:
                    renderer.print(f"[red]Unknown command:[/red] {cmd_name}")
                    renderer.print("[dim]Type /help for available commands.[/dim]")
            else:
                # Default: chat
                from apps.cli.commands.chat import run as chat_run
                try:
                    await chat_run(ctx, text)
                except Exception as e:
                    renderer.panel_error(str(e))

            renderer.newline()

    except KeyboardInterrupt:
        pass
    finally:
        session.save()
        renderer.print("[dim]Session saved. Goodbye.[/dim]")
