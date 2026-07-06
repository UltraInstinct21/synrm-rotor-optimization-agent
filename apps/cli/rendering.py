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