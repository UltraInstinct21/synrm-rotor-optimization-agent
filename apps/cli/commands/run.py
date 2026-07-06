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