"""Slash command registry — dispatch table and shared context."""

from __future__ import annotations

import importlib
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, Awaitable

if TYPE_CHECKING:
    from apps.cli.session import Session
    from apps.cli.rendering import Renderer


@dataclass
class CommandContext:
    """Shared context passed to every command handler."""
    session: "Session"
    renderer: "Renderer"
    registry: "CommandRegistry"


# Command handler signature: async def run(ctx, args) -> None
CommandHandler = Callable[[CommandContext, str], Awaitable[None]]


@dataclass
class CommandEntry:
    """A registered slash command."""
    name: str           # e.g. "/wiki"
    description: str    # one-line help text
    handler: CommandHandler
    usage: str = ""     # e.g. "/wiki read <page>"


class CommandRegistry:
    """Dispatch table mapping /commands to handler functions."""

    def __init__(self) -> None:
        self._commands: dict[str, CommandEntry] = {}

    def register(self, name: str, description: str, handler: CommandHandler, usage: str = "") -> None:
        """Register a command handler."""
        self._commands[name] = CommandEntry(
            name=name, description=description, handler=handler, usage=usage,
        )

    def get(self, command: str) -> CommandEntry | None:
        """Look up a command by name (with or without /)."""
        key = command if command.startswith("/") else f"/{command}"
        return self._commands.get(key)

    @property
    def all(self) -> list[CommandEntry]:
        """All registered commands."""
        return list(self._commands.values())

    @property
    def names(self) -> list[str]:
        """All command names for autocomplete."""
        return sorted(self._commands.keys())


def register_all(registry: CommandRegistry, ctx: CommandContext) -> None:
    """Import and register all command modules."""
    modules = {
        "/help":     ("apps.cli.commands.system",   "handle_help"),
        "/clear":    ("apps.cli.commands.system",   "handle_clear"),
        "/compact":  ("apps.cli.commands.system",   "handle_compact"),
        "/model":    ("apps.cli.commands.system",   "handle_model"),
        "/status":   ("apps.cli.commands.system",   "handle_status"),
        "/quit":     ("apps.cli.commands.system",   "handle_quit"),
        "/wiki":     ("apps.cli.commands.wiki",     "run"),
        "/motor":    ("apps.cli.commands.motor",    "run"),
        "/research": ("apps.cli.commands.research", "run"),
        "/run":      ("apps.cli.commands.run",      "run"),
        "/memory":   ("apps.cli.commands.memory",   "run"),
    }
    descriptions = {
        "/help":     "Show available commands",
        "/clear":    "Clear screen (keep session)",
        "/compact":  "Summarize & compress conversation",
        "/model":    "Show or switch LLM model",
        "/status":   "Show session stats",
        "/quit":     "Exit the CLI",
        "/wiki":     "Wiki operations: list, read, search",
        "/motor":    "Motor-CAD: status, launch, load, run, extract, set, sweep, close",
        "/research": "Run research subgraph on a query",
        "/run":      "Execute a Python script",
        "/memory":   "Memory: store, search, list, forget",
    }
    for name, (mod_path, func_name) in modules.items():
        mod = importlib.import_module(mod_path)
        handler = getattr(mod, func_name)
        registry.register(name, descriptions.get(name, ""), handler)