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