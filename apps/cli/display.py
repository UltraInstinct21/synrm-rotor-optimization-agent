"""Rich rendering helpers — clean text output, dynamic tool timing badges, and expanded details (No-Emoji)."""

from __future__ import annotations

import json
import time
from typing import Any

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text

from apps.cli.theme import (
    get_tool_label,
    render_user_query,
    render_assistant_header,
    render_error_card,
)


def render_markdown(content: str) -> Markdown | Text:
    """Render markdown with Rich's Markdown renderer."""
    try:
        if content.strip():
            return Markdown(content, code_theme="monokai")
    except Exception:
        pass
    return Text(content)


def render_user_message(console: Console, text: str) -> None:
    """Render user query message."""
    render_user_query(console, text)


def render_thinking_start(console: Console) -> Any:
    """Start an animated thinking indicator."""
    status = console.status(" [dim cyan]Analyzing query and planning steps...[/dim cyan]", spinner="dots")
    status.start()
    return status


def render_thinking_stop(status_obj: Any) -> None:
    """Stop the thinking indicator."""
    try:
        status_obj.stop()
    except Exception:
        pass


def render_tool_start(
    console: Console,
    tool_name: str,
    tool_input: Any = None,
    expanded: bool = False,
) -> float:
    """Render start of a tool call without emojis. Returns start timestamp."""
    label = get_tool_label(tool_name)
    start_time = time.time()

    if expanded:
        console.print(f"\n  [bold cyan]{label} Executing Tool:[/bold cyan] [bold bright_cyan]{tool_name}[/bold bright_cyan]")
        if tool_input is not None:
            try:
                inp_dict = json.loads(tool_input) if isinstance(tool_input, str) else tool_input
                formatted = json.dumps(inp_dict, indent=2)
                syntax = Syntax(formatted, "json", theme="monokai", word_wrap=True)
                console.print(Panel(syntax, title=f"[bold cyan]Input Parameters ({tool_name})[/bold cyan]", border_style="cyan", padding=(0, 1)))
            except Exception:
                console.print(Panel(str(tool_input)[:2000], title=f"[bold cyan]Input ({tool_name})[/bold cyan]", border_style="cyan", padding=(0, 1)))
    else:
        # Compact preview snippet of input parameters
        input_preview = ""
        if tool_input:
            try:
                inp_dict = json.loads(tool_input) if isinstance(tool_input, str) else tool_input
                if isinstance(inp_dict, dict) and inp_dict:
                    first_val = list(inp_dict.values())[0]
                    first_str = str(first_val).replace("\n", " ")
                    if len(first_str) > 40:
                        first_str = first_str[:37] + "..."
                    first_key = list(inp_dict.keys())[0]
                    input_preview = f" [dim cyan]({first_key}={first_str})[/dim cyan]"
            except Exception:
                pass
        console.print(f"  [dim cyan]{label} Running [bold cyan]{tool_name}[/bold cyan]{input_preview}...[/dim cyan]")

    return start_time


def render_tool_end(
    console: Console,
    tool_name: str,
    tool_output: Any = None,
    status: str = "done",
    expanded: bool = False,
    start_time: float | None = None,
) -> None:
    """Render completion of a tool call without emojis."""
    label = get_tool_label(tool_name)
    duration_str = ""
    if start_time is not None:
        elapsed = time.time() - start_time
        duration_str = f" [dim]({elapsed:.2f}s)[/dim]"

    if expanded:
        style = "bold green" if status == "done" else "bold red"
        badge = "[OK]" if status == "done" else "[FAIL]"
        console.print(f"  [{style}]{badge} Tool Completed: [bold]{tool_name}[/bold] ({status.upper()}){duration_str}[/{style}]")
        if tool_output is not None:
            out_str = str(tool_output)
            try:
                out_json = json.loads(out_str)
                formatted = json.dumps(out_json, indent=2)
                syntax = Syntax(formatted, "json", theme="monokai", word_wrap=True)
                console.print(Panel(syntax, title=f"[{style}]Output Payload ({tool_name})[/{style}]", border_style="green" if status == "done" else "red", padding=(0, 1)))
            except Exception:
                console.print(Panel(out_str[:3000], title=f"[{style}]Output Payload ({tool_name})[/{style}]", border_style="green" if status == "done" else "red", padding=(0, 1)))
        console.print()
    else:
        hint = " [dim cyan](Ctrl+O for details)[/dim cyan]"
        if status == "done":
            console.print(f"  [bold green][OK] {label} {tool_name}[/bold green]{duration_str}{hint}")
        else:
            console.print(f"  [bold red][FAIL] {label} {tool_name} failed[/bold red]{duration_str}{hint}")


def render_tool_call(console: Console, tool_name: str, status: str = "running") -> None:
    """Backward compatible wrapper for tool call rendering."""
    if status == "running":
        render_tool_start(console, tool_name, expanded=False)
    else:
        render_tool_end(console, tool_name, status=status, expanded=False)


def render_error(console: Console, error: Exception) -> None:
    """Render structured exception card."""
    render_error_card(console, error)


def request_hitl_approval(
    console: Console,
    tool_name: str,
    details: dict[str, Any],
) -> bool:
    """Render an unmissable, high-contrast HITL approval card and capture user approval with a styled prompt."""
    from rich.panel import Panel
    from rich.table import Table

    grid = Table.grid(padding=(0, 1))
    grid.add_column(style="bold yellow", width=14)
    grid.add_column(style="bold white")

    grid.add_row("Action:", f"[bold bright_cyan]{tool_name}[/bold bright_cyan]")
    for k, v in details.items():
        grid.add_row(f"{k.capitalize()}:", f"\"{v}\"")

    grid.add_row("", "")
    grid.add_row(
        "Choices:",
        "[bold green][Y]es (Approve Once)[/bold green]  "
        "[bold red][N]o (Decline)[/bold red]  "
        "[bold cyan][A]lways (Approve Session)[/bold cyan]"
    )

    panel = Panel(
        grid,
        title="[bold black on yellow] 🚨 HUMAN-IN-THE-LOOP APPROVAL REQUIRED 🚨 [/bold black on yellow]",
        subtitle="[bold yellow]Agent paused — Decision required[/bold yellow]",
        border_style="yellow bold",
        padding=(1, 2),
    )

    console.print("\a")  # Terminal alert bell
    console.print()
    console.print(panel)

    try:
        from prompt_toolkit import prompt as pt_prompt
        from prompt_toolkit.styles import Style
        style = Style.from_dict({"hitl": "ansibrightyellow bold"})
        ans = pt_prompt([("class:hitl", "  HITL Decision [Y/n/a] > ")], style=style).strip().lower()
    except Exception:
        try:
            ans = input("  HITL Decision [Y/n/a] > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            ans = "n"

    if ans in ("a", "always"):
        from src.tools.search import set_hitl_enabled
        set_hitl_enabled(False)
        console.print("  [bold green]✅ APPROVED — Auto-approval enabled for rest of session.[/bold green]\n")
        return True
    elif ans in ("y", "yes", ""):
        console.print("  [bold green]✅ APPROVED by user.[/bold green]\n")
        return True
    else:
        console.print("  [bold red]❌ DECLINED by user.[/bold red]\n")
        return False


def format_todos_panel(todos: list[dict], width: int = 75) -> str:
    """Format TODO items into a clean, multi-line card attached above the input prompt line."""
    if not todos:
        return ""

    completed = sum(1 for t in todos if t.get("status") == "completed")
    total = len(todos)
    header = f" Session Tasks ({completed}/{total} Completed) "

    box_w = max(width, 60)
    lines = []
    lines.append(f"┌─{header}" + "─" * max(0, box_w - len(header) - 3) + "┐")
    for item in todos[:6]:
        st = item.get("status", "pending")
        task_text = item.get("task", "")
        max_t_len = box_w - 14
        if len(task_text) > max_t_len:
            task_text = task_text[:max_t_len - 3] + "..."
        if st == "completed":
            badge = "[✓]"
            suffix = ""
        elif st == "in_progress":
            badge = "[▶]"
            suffix = " (In Progress)"
        else:
            badge = "[ ]"
            suffix = ""

        content_str = f" {badge} {item['id']}. {task_text}{suffix}"
        lines.append(f"│{content_str:<{box_w - 2}}│")

    if total > 6:
        extra_str = f" │ ... (+{total - 6} more tasks)"
        lines.append(f"{extra_str:<{box_w - 1}}│")

    lines.append("└" + "─" * (box_w - 2) + "┘")
    return "\n".join(lines)

