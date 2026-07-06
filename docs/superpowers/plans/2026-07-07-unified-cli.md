# Unified CLI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the basic REPL (`apps/cli/`) and Textual TUI (`apps/tui/`) with a single Claude Code style CLI using Rich + prompt_toolkit, with slash commands for all subsystems.

**Architecture:** Command module pattern. Core REPL loop in `app.py` dispatches to handler modules in `commands/`. Each command group (wiki, motor, research, etc.) is a separate file. Streaming output via Rich `Live` panels. Session state persisted to `.motor-deepagent/`.

**Tech Stack:** Rich (rendering), prompt_toolkit (input), asyncio, existing `src/agent/runtime.py` streaming infrastructure.

## Global Constraints

- Python >=3.13 (from pyproject.toml)
- Rich and prompt_toolkit added to dependencies
- All existing `src/tools/` and `src/agent/runtime.py` APIs consumed as-is (no modifications)
- Windows cp1252 terminal compatibility (no emoji in panel borders, use ASCII)
- `.motor-deepagent/` directory for session persistence (gitignored)

## File Structure

```
apps/cli/                          # NEW unified CLI (replaces old CLI + TUI)
├── __init__.py                    #   empty
├── __main__.py                    #   entry: python -m apps.cli
├── app.py                         #   REPL loop, prompt_toolkit, dispatch
├── session.py                     #   Session state, persistence, history
├── rendering.py                   #   Rich console, panels, markdown, tables
├── streaming.py                   #   Token stream handler, spinner, live display
└── commands/
    ├── __init__.py                #   register_all() + CommandRegistry
    ├── chat.py                    #   Default handler (no /prefix)
    ├── wiki.py                    #   /wiki list|read|search
    ├── motor.py                   #   /motor status|launch|load|run|extract|set|sweep|close
    ├── research.py                #   /research <query>
    ├── run.py                     #   /run <script>
    ├── memory.py                  #   /memory store|search|list|forget
    └── system.py                  #   /help, /clear, /compact, /model, /status, /quit
```

---

### Task 1: Dependencies + Scaffold

**Files:**
- Modify: `pyproject.toml` (add rich, prompt_toolkit)
- Create: `apps/cli/__init__.py` (empty)
- Create: `apps/cli/__main__.py`
- Create: `apps/cli/commands/__init__.py`
- Create: `apps/cli/commands/chat.py` (stub)
- Create: `apps/cli/commands/wiki.py` (stub)
- Create: `apps/cli/commands/motor.py` (stub)
- Create: `apps/cli/commands/research.py` (stub)
- Create: `apps/cli/commands/run.py` (stub)
- Create: `apps/cli/commands/memory.py` (stub)
- Create: `apps/cli/commands/system.py` (stub)

- [ ] **Step 1: Add dependencies to pyproject.toml**

In `pyproject.toml`, add `rich` and `prompt_toolkit` to the main `dependencies` list:

```python
dependencies = [
    "pydantic>=2.0",
    "python-dotenv>=1.0",
    "openai>=1.50",
    "openai-agents>=0.1",
    "langgraph>=0.4.0,<2.0.0",
    "langchain-core>=0.3.0",
    "textual>=2.0",
    "rich>=13.0",
    "prompt_toolkit>=3.0",
]
```

- [ ] **Step 2: Install new dependencies**

Run: `pip install rich prompt_toolkit`

- [ ] **Step 3: Create directory structure**

```bash
mkdir -p apps/cli/commands
```

- [ ] **Step 4: Create __init__.py files**

`apps/cli/__init__.py`:
```python
"""Unified CLI — motor-deepagent terminal engineering assistant."""
```

`apps/cli/commands/__init__.py`:
```python
"""Slash command modules for the CLI REPL."""
```

- [ ] **Step 5: Create __main__.py entry point**

`apps/cli/__main__.py`:
```python
"""Entry point for `python -m apps.cli`."""

from apps.cli.app import main

if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Create stub command modules**

Each stub follows this pattern. Create all 7:

`apps/cli/commands/chat.py`:
```python
"""Default chat handler — routes input through the agent graph."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle free-form chat input (no /prefix)."""
    pass
```

`apps/cli/commands/wiki.py`:
```python
"""Wiki commands — /wiki list|read|search."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /wiki commands."""
    pass
```

`apps/cli/commands/motor.py`:
```python
"""Motor-CAD commands — /motor status|launch|load|run|extract|set|sweep|close."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /motor commands."""
    pass
```

`apps/cli/commands/research.py`:
```python
"""Research command — /research <query>."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /research command."""
    pass
```

`apps/cli/commands/run.py`:
```python
"""Run commands — /run <script>."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /run command."""
    pass
```

`apps/cli/commands/memory.py`:
```python
"""Memory commands — /memory store|search|list|forget."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /memory commands."""
    pass
```

`apps/cli/commands/system.py`:
```python
"""System commands — /help, /clear, /compact, /model, /status, /quit."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle system commands."""
    pass
```

- [ ] **Step 7: Commit**

```bash
git add pyproject.toml apps/cli/
git commit -m "feat(cli): scaffold unified CLI with command modules

Add Rich/prompt_toolkit dependencies. Create directory structure
and stub command modules for chat, wiki, motor, research, run,
memory, and system."
```

---

### Task 2: Session State

**Files:**
- Create: `apps/cli/session.py`
- Create: `.motor-deepagent/` directory

**Interfaces:**
- Produces: `Session` dataclass used by all commands via `CommandContext`

- [ ] **Step 1: Create session.py**

`apps/cli/session.py`:
```python
"""Session state — conversation history, Motor-CAD connection, stats."""

from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.config import settings

SESSION_DIR = settings.PROJECT_ROOT / ".motor-deepagent"
HISTORY_DIR = SESSION_DIR / "history"


@dataclass
class SessionStats:
    """Per-session counters."""
    request_count: int = 0
    total_tokens: int = 0
    start_time: float = field(default_factory=lambda: datetime.now(timezone.utc).timestamp())


@dataclass
class Session:
    """Persistent session state across REPL restarts."""
    conversation_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    thread_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    model: str = ""
    motor_instance: Any = field(default=None, repr=False)
    stats: SessionStats = field(default_factory=SessionStats)
    history: list[dict[str, Any]] = field(default_factory=list)

    # ── Persistence ───────────────────────────────────────────────

    def save(self) -> None:
        """Persist session metadata to disk."""
        SESSION_DIR.mkdir(parents=True, exist_ok=True)
        meta = {
            "conversation_id": self.conversation_id,
            "thread_id": self.thread_id,
            "model": self.model,
            "stats": {
                "request_count": self.stats.request_count,
                "total_tokens": self.stats.total_tokens,
                "start_time": self.stats.start_time,
            },
        }
        (SESSION_DIR / "session.json").write_text(
            json.dumps(meta, indent=2), encoding="utf-8"
        )

    def save_message(self, role: str, content: str) -> None:
        """Append a message to the conversation history file."""
        HISTORY_DIR.mkdir(parents=True, exist_ok=True)
        msg = {
            "role": role,
            "content": content,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        history_file = HISTORY_DIR / f"{self.conversation_id}.jsonl"
        with open(history_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(msg) + "\n")

    @classmethod
    def load(cls, model: str = "") -> Session:
        """Load the last session or create a new one."""
        meta_path = SESSION_DIR / "session.json"
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                stats = SessionStats(
                    request_count=meta.get("stats", {}).get("request_count", 0),
                    total_tokens=meta.get("stats", {}).get("total_tokens", 0),
                    start_time=meta.get("stats", {}).get("start_time", 0),
                )
                return cls(
                    conversation_id=meta["conversation_id"],
                    thread_id=meta["thread_id"],
                    model=model or meta.get("model", ""),
                    stats=stats,
                )
            except (json.JSONDecodeError, KeyError):
                pass
        return cls(model=model)

    def uptime_str(self) -> str:
        """Human-readable uptime."""
        elapsed = datetime.now(timezone.utc).timestamp() - self.stats.start_time
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        if minutes > 60:
            hours = minutes // 60
            minutes = minutes % 60
            return f"{hours}h {minutes}m"
        return f"{minutes}m {seconds}s"
```

- [ ] **Step 2: Create .motor-deepagent/.gitignore**

`.motor-deepagent/.gitignore`:
```
history/
```

- [ ] **Step 3: Commit**

```bash
git add apps/cli/session.py .motor-deepagent/.gitignore
git commit -m "feat(cli): add session state with persistence

Session tracks conversation_id, thread_id, model, Motor-CAD
instance, and stats. Persists to .motor-deepagent/session.json."
```

---

### Task 3: Command Registry

**Files:**
- Modify: `apps/cli/commands/__init__.py`

**Interfaces:**
- Produces: `CommandRegistry`, `CommandContext` used by `app.py` and all commands

- [ ] **Step 1: Implement CommandRegistry**

`apps/cli/commands/__init__.py`:
```python
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
        "/help":    ("apps.cli.commands.system",   "handle_help"),
        "/clear":   ("apps.cli.commands.system",   "handle_clear"),
        "/compact": ("apps.cli.commands.system",   "handle_compact"),
        "/model":   ("apps.cli.commands.system",   "handle_model"),
        "/status":  ("apps.cli.commands.system",   "handle_status"),
        "/quit":    ("apps.cli.commands.system",   "handle_quit"),
        "/wiki":    ("apps.cli.commands.wiki",     "run"),
        "/motor":   ("apps.cli.commands.motor",    "run"),
        "/research":("apps.cli.commands.research", "run"),
        "/run":     ("apps.cli.commands.run",      "run"),
        "/memory":  ("apps.cli.commands.memory",   "run"),
    }
    descriptions = {
        "/help":    "Show available commands",
        "/clear":   "Clear screen (keep session)",
        "/compact": "Summarize & compress conversation",
        "/model":   "Show or switch LLM model",
        "/status":  "Show session stats",
        "/quit":    "Exit the CLI",
        "/wiki":    "Wiki operations: list, read, search",
        "/motor":   "Motor-CAD: status, launch, load, run, extract, set, sweep, close",
        "/research":"Run research subgraph on a query",
        "/run":     "Execute a Python script",
        "/memory":  "Memory: store, search, list, forget",
    }
    for name, (mod_path, func_name) in modules.items():
        mod = importlib.import_module(mod_path)
        handler = getattr(mod, func_name)
        registry.register(name, descriptions.get(name, ""), handler)
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/commands/__init__.py
git commit -m "feat(cli): add CommandRegistry and CommandContext

Registry maps /commands to async handler functions. register_all()
imports all command modules and wires them up."
```

---

### Task 4: Rendering

**Files:**
- Create: `apps/cli/rendering.py`

**Interfaces:**
- Produces: `Renderer` class used by `app.py` and all commands via `CommandContext`

- [ ] **Step 1: Create rendering.py**

`apps/cli/rendering.py`:
```python
"""Rich rendering — panels, tables, markdown, code blocks."""

from __future__ import annotations

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


class Renderer:
    """Wraps a Rich Console for consistent output across all commands."""

    def __init__(self) -> None:
        self.console = Console(highlight=False)

    # ── Basic output ──────────────────────────────────────────────

    def print(self, *args, **kwargs) -> None:
        self.console.print(*args, **kwargs)

    def newline(self) -> None:
        self.console.print()

    # ── Header ────────────────────────────────────────────────────

    def print_header(self, model: str = "") -> None:
        """Render the startup header."""
        self.console.print()
        self.console.rule("[bold]motor-deepagent[/bold] >> terminal engineering assistant")
        if model:
            self.console.print(f"  model: [cyan]{model}[/cyan]")
        self.console.print()

    # ── Phase panels ──────────────────────────────────────────────

    def panel_classify(self, category: str) -> None:
        """Render the classify phase panel."""
        icons = {
            "repo_coding": "code",
            "wiki_maintenance": "wiki",
            "research": "research",
            "experiment": "experiment",
            "question": "question",
            "mixed": "mixed",
        }
        icon = icons.get(category, "?")
        self.console.print(Panel(
            f"[cyan]{category}[/cyan]  ({icon})",
            title="[bold]classify[/bold]",
            border_style="cyan",
            expand=False,
        ))

    def panel_execute(self, label: str, content: str) -> None:
        """Render an execution phase panel."""
        self.console.print(Panel(
            content,
            title=f"[bold]{label}[/bold]",
            border_style="yellow",
        ))

    def panel_synthesis(self, content: str) -> None:
        """Render the synthesis panel."""
        self.console.print(Panel(
            Markdown(content) if content.strip() else "[dim]No synthesis.[/dim]",
            title="[bold]synthesis[/bold]",
            border_style="green",
        ))

    def panel_error(self, message: str) -> None:
        """Render an error panel."""
        self.console.print(Panel(
            f"[red]{message}[/red]",
            title="[bold red]error[/bold red]",
            border_style="red",
        ))

    # ── Markdown rendering ────────────────────────────────────────

    def markdown(self, text: str) -> None:
        """Render markdown text with syntax highlighting."""
        self.console.print(Markdown(text))

    # ── Tables ────────────────────────────────────────────────────

    def table(self, title: str, columns: list[str], rows: list[list[str]]) -> Table:
        """Create and print a Rich table."""
        t = Table(title=title, show_header=True, header_style="bold")
        for col in columns:
            t.add_column(col)
        for row in rows:
            t.add_row(*row)
        self.console.print(t)
        return t

    # ── Status bar ────────────────────────────────────────────────

    def status_bar(self, model: str, request_count: int, uptime: str) -> None:
        """Render the bottom status bar."""
        self.console.rule(
            f"model: [cyan]{model}[/cyan] | "
            f"requests: [yellow]{request_count}[/yellow] | "
            f"uptime: [green]{uptime}[/green]"
        )

    # ── Spinner context (used by streaming) ───────────────────────

    def spinner(self, message: str):
        """Return a Rich spinner context manager."""
        from rich.status import Status
        return self.console.status(message, spinner="dots")
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/rendering.py
git commit -m "feat(cli): add Rich renderer with panels, tables, markdown

Renderer wraps Rich Console for consistent output. Supports phase
panels (classify, execute, synthesis, error), markdown, tables,
and spinner context."
```

---

### Task 5: Streaming Handler

**Files:**
- Create: `apps/cli/streaming.py`

**Interfaces:**
- Consumes: `Renderer` from Task 4
- Produces: `StreamHandler` used by `commands/chat.py`

- [ ] **Step 1: Create streaming.py**

`apps/cli/streaming.py`:
```python
"""Streaming output — process events from run_request_graph_streamed."""

from __future__ import annotations

from typing import Any

from apps.cli.rendering import Renderer


class StreamHandler:
    """Processes streaming events from the agent graph and renders them."""

    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer
        self._current_label: str = ""

    async def handle_stream(self, stream) -> str:
        """Consume an async event stream and render each event.

        Parameters
        ----------
        stream : AsyncIterator[dict]
            From run_request_graph_streamed() or run_request_streamed().

        Returns
        -------
        str : The final synthesis text.
        """
        synthesis = ""
        async for event in stream:
            etype = event.get("type", "")

            if etype == "category":
                self.renderer.panel_classify(event["data"])

            elif etype == "info":
                label = event.get("label", "info")
                data = event.get("data", "")
                self.renderer.panel_execute(label, data)

            elif etype == "token":
                # Token streaming — handled separately by the REPL
                pass

            elif etype == "synthesis":
                synthesis = event.get("data", "")

            elif etype == "error":
                self.renderer.panel_error(event.get("data", "Unknown error"))

        if synthesis:
            self.renderer.panel_synthesis(synthesis)

        return synthesis

    def render_tokens(self, tokens: list[str]) -> str:
        """Join collected tokens into a single string."""
        return "".join(tokens)
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/streaming.py
git commit -m "feat(cli): add streaming event handler

StreamHandler consumes async events from the agent graph and
renders classify/execute/synthesis/error panels."
```

---

### Task 6: System Commands

**Files:**
- Modify: `apps/cli/commands/system.py`

**Interfaces:**
- Consumes: `CommandContext` from Task 3
- Produces: `handle_help`, `handle_clear`, `handle_compact`, `handle_model`, `handle_status`, `handle_quit`

- [ ] **Step 1: Implement system commands**

`apps/cli/commands/system.py`:
```python
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
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/commands/system.py
git commit -m "feat(cli): implement system commands

/help renders command table, /clear wipes screen, /compact
clears history, /model switches LLM, /status shows stats,
/quit saves and exits."
```

---

### Task 7: Chat Command

**Files:**
- Modify: `apps/cli/commands/chat.py`

**Interfaces:**
- Consumes: `CommandContext` from Task 3, `StreamHandler` from Task 5
- Uses: `run_request_graph_streamed()` from `src/agent/runtime.py`

- [ ] **Step 1: Implement chat handler**

`apps/cli/commands/chat.py`:
```python
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
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/commands/chat.py
git commit -m "feat(cli): implement chat command with streaming

Routes user input through run_request_graph_streamed(), renders
classify/execute/synthesis panels via StreamHandler."
```

---

### Task 8: Wiki Commands

**Files:**
- Modify: `apps/cli/commands/wiki.py`

**Interfaces:**
- Consumes: `CommandContext` from Task 3
- Uses: `list_pages()`, `read_page()`, `page_summary()` from `src/tools/wiki/update_wiki.py`

- [ ] **Step 1: Implement wiki commands**

`apps/cli/commands/wiki.py`:
```python
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
    # Try with and without .md extension
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
            # Find the matching line
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
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/commands/wiki.py
git commit -m "feat(cli): implement wiki commands

/wiki list shows all pages in a table, /wiki read displays
markdown content, /wiki search finds matching lines."
```

---

### Task 9: Motor Commands

**Files:**
- Modify: `apps/cli/commands/motor.py`

**Interfaces:**
- Consumes: `CommandContext` from Task 3
- Uses: `src/tools/motorcad/run_motorcad.py`, `get_results.py`, `set_parameters.py`
- State: `ctx.session.motor_instance` persists across commands

- [ ] **Step 1: Implement motor commands**

`apps/cli/commands/motor.py`:
```python
"""Motor-CAD commands — /motor status|launch|load|run|extract|set|sweep|close."""

from __future__ import annotations

from typing import TYPE_CHECKING

from rich.table import Table

from src.config import settings

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /motor commands."""
    parts = args.strip().split(maxsplit=2)
    subcmd = parts[0] if parts else "status"

    handlers = {
        "status": _status,
        "launch": _launch,
        "load": _load,
        "run": _run_analysis,
        "extract": _extract,
        "set": _set_param,
        "sweep": _sweep,
        "close": _close,
    }
    handler = handlers.get(subcmd)
    if handler:
        await handler(ctx, parts[1:] if len(parts) > 1 else [])
    else:
        ctx.renderer.print("[yellow]Usage:[/yellow] /motor <status|launch|load|run|extract|set|sweep|close>")


async def _status(ctx: CommandContext, args: list[str]) -> None:
    """Show Motor-CAD connection status."""
    mc = ctx.session.motor_instance
    if mc:
        ctx.renderer.print("[green]Motor-CAD: connected[/green]")
    else:
        ctx.renderer.print("[dim]Motor-CAD: not connected[/dim]")
        ctx.renderer.print("[dim]Run /motor launch to start.[/dim]")


async def _launch(ctx: CommandContext, args: list[str]) -> None:
    """Launch Motor-CAD."""
    from src.tools.motorcad.run_motorcad import launch_motorcad

    visible = "--visible" in args
    mot_file = settings.REFERENCE_MOT if settings.REFERENCE_MOT.exists() else None

    with ctx.renderer.spinner("Launching Motor-CAD..."):
        mc = launch_motorcad(visible=visible, model_path=mot_file)

    if mc:
        ctx.session.motor_instance = mc
        ctx.renderer.print("[green]Motor-CAD launched successfully.[/green]")
    else:
        ctx.renderer.panel_error("Failed to launch Motor-CAD. Is it installed?")


async def _load(ctx: CommandContext, args: list[str]) -> None:
    """Load a .mot model file."""
    mc = ctx.session.motor_instance
    if not mc:
        ctx.renderer.print("[red]Motor-CAD not connected. Run /motor launch first.[/red]")
        return

    from src.tools.motorcad.run_motorcad import load_model

    path = args[0] if args else str(settings.REFERENCE_MOT)
    with ctx.renderer.spinner(f"Loading {path}..."):
        ok = load_model(mc, path)

    if ok:
        ctx.renderer.print(f"[green]Loaded: {path}[/green]")
    else:
        ctx.renderer.panel_error(f"Failed to load {path}")


async def _run_analysis(ctx: CommandContext, args: list[str]) -> None:
    """Run magnetic analysis."""
    mc = ctx.session.motor_instance
    if not mc:
        ctx.renderer.print("[red]Motor-CAD not connected. Run /motor launch first.[/red]")
        return

    from src.tools.motorcad.run_motorcad import run_magnetic

    with ctx.renderer.spinner("Running magnetic analysis..."):
        ok = run_magnetic(mc)

    if ok:
        ctx.renderer.print("[green]Magnetic analysis complete.[/green]")
    else:
        ctx.renderer.panel_error("Magnetic analysis failed.")


async def _extract(ctx: CommandContext, args: list[str]) -> None:
    """Extract and display results."""
    mc = ctx.session.motor_instance
    if not mc:
        ctx.renderer.print("[red]Motor-CAD not connected. Run /motor launch first.[/red]")
        return

    from src.tools.motorcad.get_results import extract_results

    with ctx.renderer.spinner("Extracting results..."):
        result = extract_results(mc)

    if not result:
        ctx.renderer.panel_error("No results available.")
        return

    t = Table(title="Electromagnetic Results", show_header=True, header_style="bold")
    t.add_column("Metric", style="cyan")
    t.add_column("Value", justify="right")
    for field_name in ["torque_nm", "efficiency_pct", "power_factor",
                        "ld_mh", "lq_mh", "saliency",
                        "iron_loss_w", "copper_loss_w"]:
        val = getattr(result, field_name, None)
        display_val = f"{val:.4f}" if val is not None else "N/A"
        t.add_row(field_name.replace("_", " ").title(), display_val)
    ctx.renderer.console.print(t)


async def _set_param(ctx: CommandContext, args: list[str]) -> None:
    """Set a Motor-CAD parameter: /motor set <var> <value>."""
    mc = ctx.session.motor_instance
    if not mc:
        ctx.renderer.print("[red]Motor-CAD not connected. Run /motor launch first.[/red]")
        return
    if len(args) < 2:
        ctx.renderer.print("[yellow]Usage:[/yellow] /motor set <variable> <value>")
        return

    from src.tools.motorcad.set_parameters import set_parameter

    var_name = args[0]
    try:
        value = float(args[1])
    except ValueError:
        ctx.renderer.print(f"[red]Invalid value: {args[1]}[/red]")
        return

    with ctx.renderer.spinner(f"Setting {var_name} = {value}..."):
        ok, msg = set_parameter(mc, var_name, value, domain="rotor", checkpoint_before=True)

    if ok:
        ctx.renderer.print(f"[green]{msg}[/green]")
    else:
        ctx.renderer.panel_error(msg)


async def _sweep(ctx: CommandContext, args: list[str]) -> None:
    """Parameter sweep: /motor sweep <var>=<lo>-<hi> [steps=N]."""
    ctx.renderer.print("[dim]Sweep mode: use the agent chat to run full sweeps.[/dim]")
    ctx.renderer.print("[dim]Example: 'sweep L1_Diameter from 85 to 100 in 5 steps'[/dim]")


async def _close(ctx: CommandContext, args: list[str]) -> None:
    """Close Motor-CAD connection."""
    mc = ctx.session.motor_instance
    if not mc:
        ctx.renderer.print("[dim]Motor-CAD not connected.[/dim]")
        return

    from src.tools.motorcad.run_motorcad import close_motorcad

    close_motorcad(mc)
    ctx.session.motor_instance = None
    ctx.renderer.print("[green]Motor-CAD closed.[/green]")
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/commands/motor.py
git commit -m "feat(cli): implement motor commands

/motor status|launch|load|run|extract|set|sweep|close.
Persistent Motor-CAD instance via session.motor_instance."
```

---

### Task 10: Research + Run + Memory Commands

**Files:**
- Modify: `apps/cli/commands/research.py`
- Modify: `apps/cli/commands/run.py`
- Modify: `apps/cli/commands/memory.py`

**Interfaces:**
- Consumes: `CommandContext` from Task 3

- [ ] **Step 1: Implement research command**

`apps/cli/commands/research.py`:
```python
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
```

- [ ] **Step 2: Implement run command**

`apps/cli/commands/run.py`:
```python
"""Run commands — /run <script>."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from src.tools.execution.run_script import run_python_script

if TYPE_CHECKING:
    from apps.cli.commands import CommandContext


async def run(ctx: CommandContext, args: str) -> None:
    """Handle /run command."""
    if not args.strip():
        ctx.renderer.print("[yellow]Usage:[/yellow] /run <script.py> [args...]")
        return

    parts = args.strip().split()
    script = parts[0]
    script_args = parts[1:] if len(parts) > 1 else None

    script_path = Path(script)
    if not script_path.exists():
        ctx.renderer.print(f"[red]Script not found:[/red] {script}")
        return

    with ctx.renderer.spinner(f"Running {script.name}..."):
        report = run_python_script(script_path, args=script_args)

    if report.result == "success":
        ctx.renderer.print(f"[green]Script completed successfully.[/green]")
        if report.outputs.get("logs"):
            ctx.renderer.print("[dim]Output:[/dim]")
            ctx.renderer.print(report.outputs["logs"][0][:2000])
    else:
        ctx.renderer.panel_error(f"Script failed: {report.workflow_name}")
        if report.outputs.get("logs"):
            ctx.renderer.print(report.outputs["logs"][0][:1000])
```

- [ ] **Step 3: Implement memory commands**

`apps/cli/commands/memory.py`:
```python
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
```

- [ ] **Step 4: Commit**

```bash
git add apps/cli/commands/research.py apps/cli/commands/run.py apps/cli/commands/memory.py
git commit -m "feat(cli): implement research, run, and memory commands

/research delegates through agent graph, /run executes scripts,
/memory stores/searches/lists/forgets facts."
```

---

### Task 11: Core REPL

**Files:**
- Create: `apps/cli/app.py`

**Interfaces:**
- Consumes: `CommandRegistry`, `CommandContext`, `register_all()` from Task 3
- Consumes: `Session` from Task 2
- Consumes: `Renderer` from Task 4
- Produces: `main()` entry point called by `__main__.py`

- [ ] **Step 1: Create app.py**

`apps/cli/app.py`:
```python
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
    # Load .env
    env_path = settings.PROJECT_ROOT / ".env"
    load_dotenv(env_path, override=False)

    if not settings.LLM_API_KEY:
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
                entry = ctx.registry.get("/help")  # just need any entry
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
```

- [ ] **Step 2: Commit**

```bash
git add apps/cli/app.py
git commit -m "feat(cli): implement core REPL with prompt_toolkit

REPL loop with slash command dispatch, autocomplete, streaming
chat output, and session persistence. Entry point for python -m apps.cli."
```

---

### Task 12: Cleanup Old Files

**Files:**
- Remove: `apps/cli/main.py` (old entry point)
- Remove: `apps/cli/chat.py` (old REPL)
- Remove: `apps/cli/display.py` (old display)
- Remove: `apps/tui/` (entire Textual TUI)

- [ ] **Step 1: Remove old CLI files**

```bash
git rm apps/cli/main.py apps/cli/chat.py apps/cli/display.py
```

- [ ] **Step 2: Remove old TUI**

```bash
git rm -r apps/tui/
```

- [ ] **Step 3: Update pyproject.toml scripts**

In `pyproject.toml`, remove the TUI entry point:

```toml
# DELETE this line:
# motor-deepagent-tui = "apps.tui.app:main"
```

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore(cli): remove old CLI and TUI, replaced by unified CLI

Remove apps/cli/main.py, chat.py, display.py and apps/tui/.
New entry point is python -m apps.cli."
```

---

### Task 13: Verify End-to-End

**Files:**
- None (verification only)

- [ ] **Step 1: Run help command**

```bash
python -m apps.cli /help
```

Expected: Rich table with all commands printed.

- [ ] **Step 2: Run status command**

```bash
python -m apps.cli /status
```

Expected: Session stats displayed.

- [ ] **Step 3: Run single-shot chat**

```bash
python -m apps.cli "what is the project about"
```

Expected: Classify panel, synthesis panel with response.

- [ ] **Step 4: Run interactive REPL**

```bash
python -m apps.cli
```

Expected: Header, prompt `>`, can type `/help`, chat, `/wiki list`, etc.

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "feat(cli): unified CLI complete

Claude Code style terminal CLI with Rich rendering, streaming,
slash commands for wiki/motor/research/run/memory, session
persistence, and prompt_toolkit autocomplete."
```
