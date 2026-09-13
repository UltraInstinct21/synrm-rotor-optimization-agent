"""Theme definitions, color palettes, and dynamic Rich visual components for motor-deepagent CLI (No-Emoji, High-Performance)."""

from __future__ import annotations

import os
import time
from typing import Any
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.theme import Theme
from rich.markdown import Markdown

# Custom Rich theme for clean, high-contrast CLI aesthetics
MOTOR_THEME = Theme({
    # Brand & Headers
    "brand.primary": "bold bright_cyan",
    "brand.secondary": "bold cyan",
    "brand.accent": "bold magenta",
    "brand.version": "dim cyan",
    # User / Agent Roles
    "role.user": "bold bright_blue",
    "role.assistant": "bold bright_cyan",
    "role.system": "bold yellow",
    # Status Indicators
    "status.online": "bold green",
    "status.offline": "bold red",
    "status.warning": "bold yellow",
    "status.info": "cyan",
    # Tools
    "tool.name": "bold bright_cyan",
    "tool.label": "cyan",
    "tool.param": "dim cyan",
    "tool.success": "bold green",
    "tool.error": "bold red",
    # UI Elements
    "ui.border": "cyan",
    "ui.dim": "bright_black",
    "ui.highlight": "bold white",
})

# Environment check caching to prevent redundant disk I/O
_MOTORCAD_CACHE: tuple[float, str] | None = None


_CONSOLE: Console | None = None

def get_console() -> Console:
    """Return the singleton Console instance configured with the custom MOTOR_THEME."""
    global _CONSOLE
    if _CONSOLE is None:
        _CONSOLE = Console(theme=MOTOR_THEME, highlight=True)
    return _CONSOLE


def check_motorcad_env(cache_ttl_sec: float = 30.0) -> str:
    """Cached check for Motor-CAD executable environment."""
    global _MOTORCAD_CACHE
    now = time.time()
    if _MOTORCAD_CACHE is not None:
        last_time, cached_val = _MOTORCAD_CACHE
        if now - last_time < cache_ttl_sec:
            return cached_val

    mc_exe = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
    result = "Connected (v2025.1)" if os.path.exists(mc_exe) else "Standby / Ready"
    _MOTORCAD_CACHE = (now, result)
    return result


def render_banner(
    console: Console,
    session_id: str = "new",
    model_name: str = "default",
    hitl_enabled: bool = False,
    tool_count: int | None = None,
    expanded_view: bool = False,
) -> None:
    """Render dynamic, responsive motor-deepagent banner and status header without emojis."""
    mc_status = check_motorcad_env()
    hitl_str = "[bold green]ENABLED[/bold green]" if hitl_enabled else "[dim white]DISABLED[/dim white]"
    expanded_str = "[bold cyan]ON[/bold cyan]" if expanded_view else "[dim white]OFF[/dim white]"
    try:
        from src.config.projects import get_active_slug as _get_active_slug

        _slug = _get_active_slug() or "none"
    except Exception:
        _slug = "none"
    project_str = f"[bold cyan]{_slug}[/bold cyan]"

    term_width = console.width
    is_compact = term_width < 70

    # Clean Header Title
    header_title = Text.from_markup(
        " [bold bright_cyan]M O T O R - D E E P A G E N T[/bold bright_cyan]  [dim cyan]v0.1.0[/dim cyan]\n"
        " [dim white]Terminal-First Motor Engineering & Deep Agents Optimization AI[/dim white]"
    )

    # Dynamic Grid based on terminal width
    table = Table.grid(expand=True, padding=(0, 1 if is_compact else 2))
    if is_compact:
        table.add_column(justify="left", style="dim cyan")
        table.add_column(justify="left")
        table.add_row("Model:", f"[bold white]{model_name}[/bold white]")
        table.add_row("Motor-CAD:", f"[bold green]{mc_status}[/bold green]")
        table.add_row("Session:", f"[bold yellow]{session_id}[/bold yellow]")
        table.add_row("Project:", project_str)
        table.add_row("HITL Web:", hitl_str)
        if tool_count is not None:
            table.add_row("Tools:", f"[bold cyan]{tool_count} active[/bold cyan]")
        table.add_row("Expanded:", expanded_str)
    else:
        table.add_column(justify="left", style="dim cyan")
        table.add_column(justify="left")
        table.add_column(justify="left", style="dim cyan")
        table.add_column(justify="left")
        table.add_row(
            "Model:", f"[bold white]{model_name}[/bold white]",
            "Motor-CAD:", f"[bold green]{mc_status}[/bold green]",
        )
        table.add_row(
            "Session:", f"[bold yellow]{session_id}[/bold yellow]",
            "HITL Web:", hitl_str,
        )
        table.add_row("Project:", project_str)
        if tool_count is not None:
            table.add_row(
                "Tools:", f"[bold cyan]{tool_count} active[/bold cyan]",
                "Expanded:", expanded_str,
            )
        else:
            table.add_row("Expanded:", expanded_str)

    content = Table.grid(expand=True)
    content.add_column()
    content.add_row(header_title)
    content.add_row(Text(""))
    content.add_row(table)

    panel = Panel(
        content,
        border_style="bright_cyan",
        padding=(1, 2) if not is_compact else (0, 1),
        title="[bold bright_cyan]ANSYS MOTOR-CAD AI AGENT[/bold bright_cyan]",
        subtitle="[dim white]Type /help for commands | Ctrl+O for logs | Ctrl+C to interrupt[/dim white]",
        subtitle_align="center",
    )
    console.print()
    console.print(panel)
    console.print()


def render_user_query(console: Console, text: str) -> None:
    """Render formatted user input block without emojis."""
    console.print()
    user_header = Text(" USER ", style="bold white on blue")
    console.print(user_header, f" [bold bright_white]{text}[/bold bright_white]")
    console.print()


def render_assistant_header(console: Console) -> None:
    """Render assistant response header without emojis."""
    header = Text(" MOTOR-DEEPAGENT ", style="bold white on cyan")
    console.print(header)


def get_tool_label(tool_name: str) -> str:
    """Map tool name to a clean text label prefix."""
    name = tool_name.lower()
    if "motorcad" in name or "run_file" in name or "execution" in name:
        return "[MOTORCAD]"
    elif "research" in name or "subgraph" in name:
        return "[RESEARCH]"
    elif "search" in name or "tavily" in name:
        return "[SEARCH]"
    elif "todo" in name or "task" in name:
        return "[TODO]"
    elif "wiki" in name:
        return "[WIKI]"
    elif any(k in name for k in ("file", "create", "read", "write", "edit", "grep", "glob", "ls")):
        return "[FILE]"
    return "[TOOL]"


def render_error_card(console: Console, error: Exception) -> None:
    """Render structured error details card without emojis."""
    error_type = type(error).__name__
    error_msg = str(error) or "An unknown error occurred during execution."

    tip = "Tip: Check connection, model key, or type /help for commands."
    lowered = f"{error_type} {error_msg}".lower()
    if "500" in lowered or "internal server error" in lowered:
        tip = ("Tip: The model backend returned 500 — usually an unknown/deprecated "
               "model id or a provider outage. Run /model list and switch to a live "
               "model (e.g. /model deepseek-v4-flash-free), then retry.")
    elif "401" in lowered or "403" in lowered or "unauthorized" in lowered or "forbidden" in lowered or "invalid api key" in lowered or "access denied" in lowered:
        tip = ("Tip: Authentication failed (401/403) — your OPENCODE_API_KEY looks invalid, "
               "expired, or blocked at the edge. Opencode keys start with 'oc-...'. Grab a fresh "
               "key from your opencode.ai dashboard, put it in .env, restart, and /preflight.")
    elif "429" in lowered or "rate limit" in lowered:
        tip = ("Tip: Rate limited — wait a minute and retry, or /model switch to "
               "a different model.")

    content = Text()
    content.append(f"Type: {error_type}\n", style="bold red")
    content.append(f"Details: {error_msg}\n\n", style="white")
    content.append(tip, style="dim yellow")

    panel = Panel(
        content,
        title="[bold red][ERROR] Execution Failed[/bold red]",
        border_style="red",
        padding=(1, 2),
    )
    console.print()
    console.print(panel)
    console.print()
