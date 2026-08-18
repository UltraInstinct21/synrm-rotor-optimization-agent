"""Slash command registry and handlers for motor-deepagent CLI (No-Emoji)."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Callable

from rich.panel import Panel
from rich.table import Table
from rich.text import Text

if TYPE_CHECKING:
    from apps.cli.app import MotorCLI

COMMANDS: dict[str, dict] = {}


def command(name: str, help: str, category: str = "General"):  # noqa: A002
    """Decorator to register a slash command."""

    def decorator(fn: Callable) -> Callable:
        COMMANDS[name] = {"fn": fn, "help": help, "category": category}
        return fn

    return decorator


def dispatch(cli: MotorCLI, raw: str) -> bool | None:  # noqa: ANN001
    """Parse and run a slash command. Returns False to exit REPL."""
    parts = raw.split(maxsplit=1)
    name = parts[0].lstrip("/").lower()
    args = parts[1] if len(parts) > 1 else ""

    if name in COMMANDS:
        return COMMANDS[name]["fn"](cli, args)

    cli.console.print(
        f"  [bold red]Unknown command:[/bold red] [yellow]/{name}[/yellow]  "
        f"[dim cyan]— type /help for available commands[/dim cyan]"
    )
    return None


# ── Built-in commands ────────────────────────────────────────────────


@command("help", "Show available commands organized by category", "General")
def cmd_help(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    table = Table(title="[bold bright_cyan][HELP] Available Slash Commands[/bold bright_cyan]", border_style="cyan", show_header=True)
    table.add_column("Command", style="bold cyan", no_wrap=True)
    table.add_column("Category", style="dim cyan", no_wrap=True)
    table.add_column("Description", style="white")

    for name, info in sorted(COMMANDS.items()):
        table.add_row(f"/{name}", info["category"], info["help"])

    cli.console.print()
    cli.console.print(table)
    cli.console.print("  [dim]Tip: Use tab completion when typing slash commands.[/dim]\n")


@command("exit", "Exit the CLI session", "General")
@command("quit", "Exit the CLI session", "General")
def cmd_exit(cli: MotorCLI, args: str) -> bool:  # noqa: ANN001
    cli.console.print("\n  [bold bright_cyan]Goodbye! Session saved successfully.[/bold bright_cyan]\n")
    return False


@command("clear", "Clear the terminal screen and display header", "General")
def cmd_clear(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    cli.console.clear()
    from apps.cli.theme import render_banner
    from src.tools.search import get_hitl_enabled

    render_banner(
        cli.console,
        session_id=cli.current_session.id,
        model_name=cli.model_name,
        hitl_enabled=get_hitl_enabled(),
        tool_count=len(cli.tools) if cli.tools else 6,
        expanded_view=cli.expanded_view,
    )


@command("version", "Show version and environment summary", "General")
def cmd_version(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    cli.console.print("  [bold bright_cyan]motor-deepagent[/bold bright_cyan] [dim cyan]v0.1.0[/dim cyan] — Deep Agents Motor Engineering Assistant")


@command("expanded", "Toggle expanded tool call details view (Ctrl+O)", "View")
@command("verbose", "Toggle expanded tool call details view (Ctrl+O)", "View")
def cmd_expanded(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    cli.expanded_view = not cli.expanded_view
    status = "[bold green]ENABLED[/bold green]" if cli.expanded_view else "[dim white]DISABLED[/dim white]"
    cli.console.print(f"  [cyan][INFO] Tool Call Expanded Details View:[/cyan] {status} [dim](Ctrl+O)[/dim]")


@command("hitl", "Toggle Human-In-The-Loop approval mode for web search (on/off)", "Config")
def cmd_hitl(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    from src.tools.search import set_hitl_enabled, get_hitl_enabled

    clean_args = args.strip().lower()
    if clean_args in ("on", "true", "1", "enable"):
        set_hitl_enabled(True)
    elif clean_args in ("off", "false", "0", "disable"):
        set_hitl_enabled(False)
    else:
        current = get_hitl_enabled()
        set_hitl_enabled(not current)

    status = "[bold green]ENABLED[/bold green]" if get_hitl_enabled() else "[dim white]DISABLED[/dim white]"
    cli.console.print(f"  [yellow][HITL] Human-In-The-Loop Web Approval:[/yellow] {status}")


def _save_env_var(key: str, value: str) -> None:
    """Set environment variable in memory and persist to .env file."""
    os.environ[key] = value
    env_path = Path(__file__).resolve().parents[2] / ".env"
    lines = []
    if env_path.exists():
        lines = env_path.read_text(encoding="utf-8").splitlines()

    updated = False
    new_lines = []
    for line in lines:
        if line.startswith(f"{key}=") or line.startswith(f"# {key}="):
            new_lines.append(f"{key}={value}")
            updated = True
        else:
            new_lines.append(line)

    if not updated:
        new_lines.append(f"{key}={value}")

    env_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


@command("key", "Set or view API keys (e.g., /key tavily tvly-xxx)", "Config")
@command("tavily", "Set Tavily web search API key (e.g., /tavily tvly-xxx)", "Config")
def cmd_key(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    parts = args.strip().split(maxsplit=1)
    service = parts[0].lower() if parts else "tavily"
    key_val = parts[1] if len(parts) > 1 else ""

    if service.startswith("tvly-") and not key_val:
        key_val = service
        service = "tavily"

    if service in ("tavily", "web", "search"):
        if key_val:
            _save_env_var("TAVILY_API_KEY", key_val)
            cli.console.print("  [bold green]✅ Tavily API Key updated and saved to .env file![/bold green]")
        else:
            curr = os.getenv("TAVILY_API_KEY")
            status = f"[bold green]Configured ({curr[:8]}...)[/bold green]" if curr else "[bold red]Missing[/bold red]"
            cli.console.print(f"  [yellow]Tavily Web Search API Key:[/yellow] {status}")
            cli.console.print("  [dim]To set key: /key tavily tvly-your-api-key OR edit TAVILY_API_KEY in D:\\SRM\\Agent\\.env[/dim]")
            cli.console.print("  [dim]Get a free API key at https://tavily.com[/dim]")
    else:
        cli.console.print("  [yellow]Usage: /key tavily <your_api_key>[/yellow]")


@command("todo", "Manage session TODO tasks (list, add, done, clear)", "Tasks")
@command("todos", "Manage session TODO tasks (list, add, done, clear)", "Tasks")
def cmd_todo(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    from apps.cli.display import format_todos_panel
    parts = args.strip().split(maxsplit=1)
    sub = parts[0].lower() if parts else "list"
    rest = parts[1] if len(parts) > 1 else ""

    if sub == "add" and rest:
        item = cli.current_session.add_todo(rest)
        cli.console.print(f"  [bold green]✅ Added task #{item['id']}:[/bold green] {item['task']}")
    elif sub in ("done", "complete", "completed") and rest:
        if cli.current_session.update_todo(rest, "completed"):
            cli.console.print(f"  [bold green]✓ Marked task #{rest} as COMPLETED.[/bold green]")
        else:
            cli.console.print(f"  [bold red]❌ Task #{rest} not found.[/bold red]")
    elif sub == "clear":
        cli.current_session.clear_todos()
        cli.console.print("  [dim]Cleared all session TODO tasks.[/dim]")
    else:
        todos = cli.current_session.get_todos()
        if not todos:
            cli.console.print("  [dim]No tasks attached to current session. Usage: /todo add <task>, /todo done <id>, /todo clear[/dim]")
        else:
            panel_str = format_todos_panel(todos, width=cli.console.width - 4)
            cli.console.print(f"\n{panel_str}\n")


@command("model", "Show or switch the active LLM model", "Config")
def cmd_model(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    if args:
        cli.model_name = args.strip()
        cli._agent = None  # Force rebuild on next query
        cli.console.print(
            f"  [bold green]Model switched -> [bright_cyan]{cli.model_name}[/bright_cyan][/bold green]  "
            f"[dim](Agent will re-initialize on next query)[/dim]"
        )
    else:
        cli.console.print(f"  Active Model: [bold bright_cyan]{cli.model_name}[/bold bright_cyan]")
        cli.console.print("  [dim]Usage: /model <model_name>[/dim]")


@command("tools", "Browse available agent tools and capabilities", "Config")
def cmd_tools(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    cli._ensure_agent()
    table = Table(title="[bold bright_cyan][TOOLS] Loaded Agent Tools[/bold bright_cyan]", border_style="cyan")
    table.add_column("Tool Name", style="bold cyan", no_wrap=True)
    table.add_column("Description", style="white")

    for t in cli.tools:
        desc = getattr(t, "description", "").strip().split("\n")[0][:80]
        table.add_row(t.name, desc)

    cli.console.print()
    cli.console.print(table)
    cli.console.print(f"  [dim cyan]Total {len(cli.tools)} tools registered[/dim cyan]\n")


@command("session", "Manage sessions (list, load <id>, new, export)", "Session")
def cmd_session(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    parts = args.strip().split(maxsplit=1)
    sub = parts[0].lower() if parts else "list"
    sub_arg = parts[1] if len(parts) > 1 else ""

    if sub == "list":
        sessions = cli.session_store.list_sessions(limit=10)
        table = Table(title="[bold bright_cyan][SESSIONS] Recent Sessions[/bold bright_cyan]", border_style="cyan")
        table.add_column("Active", style="bold yellow", justify="center")
        table.add_column("Session ID", style="bold cyan")
        table.add_column("Messages", justify="right", style="green")
        table.add_column("Title / First Prompt", style="white")

        for s in sessions:
            is_curr = "*" if s.id == cli.current_session.id else ""
            table.add_row(is_curr, s.id, str(s.message_count), s.title)

        cli.console.print()
        cli.console.print(table)
        cli.console.print("  [dim]Switch session: /session load <id> | New session: /session new[/dim]\n")

    elif sub == "new":
        cli.current_session = cli.session_store.new()
        cli.console.print(f"  [bold green]Started new session:[/bold green] [bold yellow]{cli.current_session.id}[/bold yellow]")

    elif sub == "load":
        if not sub_arg:
            cli.console.print("  [yellow]Usage: /session load <session_id>[/yellow]")
            return
        loaded = cli.session_store.load_session(sub_arg.strip())
        if loaded:
            cli.current_session = loaded
            cli.console.print(f"  [bold green]Loaded session:[/bold green] [bold yellow]{loaded.id}[/bold yellow] ({loaded.message_count} messages)")
        else:
            cli.console.print(f"  [bold red]Session '{sub_arg}' not found.[/bold red]")

    elif sub == "export":
        out_dir = Path.home() / ".motor-deepagent" / "exports"
        out_path = out_dir / f"session_{cli.current_session.id}.md"
        if sub_arg:
            out_path = Path(sub_arg.strip())
        exported = cli.current_session.export_markdown(out_path)
        cli.console.print(f"  [bold green]Exported session to:[/bold green] [underline]{exported}[/underline]")

    else:
        cli.console.print("  [yellow]Unknown session subcommand. Options: list, load <id>, new, export[/yellow]")


@command("history", "Show conversation message log for active session", "Session")
def cmd_history(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    if not cli.current_session.messages:
        cli.console.print("  [dim]No messages in active session yet.[/dim]")
        return

    cli.console.print(f"\n  [bold cyan][HISTORY] Active Session ({cli.current_session.id})[/bold cyan]\n")
    for msg in cli.current_session.messages:
        role = msg["role"]
        content = msg["content"][:120].replace("\n", " ")
        if role == "user":
            cli.console.print(f"  [bold bright_blue]User:[/bold bright_blue] {content}")
        else:
            cli.console.print(f"  [bold bright_cyan]Agent:[/bold bright_cyan] [dim]{content}[/dim]")
    cli.console.print()


@command("config", "Display agent and session configuration overview", "Config")
def cmd_config(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    from src.tools.search import get_hitl_enabled
    from apps.cli.theme import check_motorcad_env

    cli._ensure_agent()
    table = Table.grid(padding=(0, 2))
    table.add_column(style="bold cyan")
    table.add_column(style="white")

    table.add_row("LLM Model:", cli.model_name)
    table.add_row("Motor-CAD Status:", check_motorcad_env())
    table.add_row("HITL Approval Mode:", "ENABLED" if get_hitl_enabled() else "DISABLED")
    table.add_row("Expanded View:", f"{cli.expanded_view} (Ctrl+O)")
    table.add_row("Active Tools:", f"{len(cli.tools)} registered")
    table.add_row("Active Session ID:", cli.current_session.id)
    table.add_row("Session Messages:", str(cli.current_session.message_count))
    table.add_row("Session File Path:", str(cli.current_session.path))

    panel = Panel(table, title="[bold bright_cyan][CONFIG] System Overview[/bold bright_cyan]", border_style="cyan", padding=(1, 2))
    cli.console.print()
    cli.console.print(panel)
    cli.console.print()


@command("system", "Display detailed environment diagnostics", "General")
@command("sys", "Display detailed environment diagnostics", "General")
def cmd_system(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    from apps.cli.theme import check_motorcad_env

    table = Table(title="[bold bright_cyan][DIAGNOSTICS] Environment & System[/bold bright_cyan]", border_style="cyan")
    table.add_column("Component", style="bold cyan")
    table.add_column("Details", style="white")

    table.add_row("Python Version", sys.version.split()[0])
    table.add_row("Operating System", sys.platform)
    table.add_row("Motor-CAD Install", check_motorcad_env())
    table.add_row("OpenAI API Key", "Configured" if os.getenv("OPENAI_API_KEY") else "Missing")
    table.add_row("Tavily API Key", "Configured" if os.getenv("TAVILY_API_KEY") else "Missing / HITL Enabled")
    table.add_row("Project Root", str(Path(__file__).resolve().parent.parent.parent))

    cli.console.print()
    cli.console.print(table)
    cli.console.print()


@command("copy", "Copy the last assistant response to clipboard", "General")
def cmd_copy(cli: MotorCLI, args: str) -> None:  # noqa: ANN001
    last_assistant_msg = ""
    for msg in reversed(cli.current_session.messages):
        if msg.get("role") == "assistant" and msg.get("content"):
            last_assistant_msg = msg["content"]
            break

    if not last_assistant_msg:
        cli.console.print("  [yellow]No assistant response available to copy.[/yellow]")
        return

    try:
        import pyperclip

        pyperclip.copy(last_assistant_msg)
        cli.console.print("  [bold green][COPY] Last assistant response copied to clipboard.[/bold green]")
    except Exception:
        # Fallback if pyperclip is not installed
        out_file = Path.home() / ".motor-deepagent" / "exports" / "last_response.txt"
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(last_assistant_msg, encoding="utf-8")
        cli.console.print(f"  [yellow]pyperclip not installed. Saved last response to:[/yellow] [underline]{out_file}[/underline]")
