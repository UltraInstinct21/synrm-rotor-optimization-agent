"""Startup preflight — validate the environment BEFORE the first agent turn.

Checks (each returns level ok|warn|error + message):
- LLM API key present (error — nothing works without it).
- Opencode Zen catalogue reachable (warn — falls back to cached list).
- Active machine spec loads (error — validate/score/ledger depend on it).
- Reference .mot model file exists (warn — only needed for Motor-CAD runs).
- workspace/ writable (error — scratch + ledger need it).
- Tavily key present (warn — web search only).

render_preflight(console, results) prints a compact panel. Never raises.
"""

from __future__ import annotations

import os
from pathlib import Path


def run_preflight() -> list[dict]:
    results: list[dict] = []

    try:
        from src.config import settings

        provider = settings.resolve_provider()
        key_env = provider["key_env"]
        hint = provider["profile"].get("key_prefix_hint", "")
        results.append({"check": "LLM provider", "level": "ok",
                        "message": f"{provider['name']} via {provider['base_url']} (key: {key_env})"})
        if hint and not provider["api_key"].startswith(hint):
            results.append({"check": "LLM API key", "level": "warn",
                            "message": f"{key_env} has an unexpected format ({provider['name']} keys "
                                       f"start with '{hint}') — auth failures likely; refresh it from "
                                       f"your provider dashboard"})
        else:
            results.append({"check": "LLM API key", "level": "ok",
                            "message": f"{key_env} is set"})
    except ValueError as e:
        results.append({"check": "LLM provider", "level": "error", "message": str(e)})
        results.append({"check": "LLM API key", "level": "error",
                        "message": "No provider key — set it in .env"})

    try:
        from src.config import settings

        try:
            import urllib.request as _urlrequest

            req = _urlrequest.Request(
                settings._zen_models_url(), headers={"User-Agent": "motor-deepagent"})
            with _urlrequest.urlopen(req, timeout=8) as resp:
                raw = resp.read()
            try:
                ids = settings._parse_models_payload(raw)
                default = os.getenv("MODEL_DEFAULT", "") or settings.MODEL_DEFAULT
                if default in ids:
                    results.append({"check": "Zen catalogue", "level": "ok",
                                    "message": f"model catalogue reachable; default '{default}' is live"})
                else:
                    results.append({"check": "Zen catalogue", "level": "warn",
                                    "message": f"reachable, but default model '{default}' is NOT in the "
                                               f"live catalogue ({len(ids)} models) — run /model list and switch"})
            except Exception:
                results.append({"check": "Zen catalogue", "level": "ok",
                                "message": "model catalogue reachable (/model lists live data)"})
        except Exception as e:
            results.append({"check": "Zen catalogue", "level": "warn",
                            "message": f"unreachable ({e}); /model serves fallback list"})
    except Exception as e:
        results.append({"check": "Zen catalogue", "level": "warn", "message": str(e)})

    try:
        from src.motor.spec import load_active_spec, resolve_active_spec_path

        spec = load_active_spec()
        results.append({"check": "Machine spec", "level": "ok",
                        "message": f"{spec.project} [{spec.machine_type}] "
                                   f"({len(spec.params)} params, {len(spec.targets)} targets) "
                                   f"from {resolve_active_spec_path()}"})
    except Exception as e:
        results.append({"check": "Machine spec", "level": "error",
                        "message": f"cannot load active spec: {e}"})

    try:
        from src.config.projects import get_active_slug, project_dir

        slug = get_active_slug()
        if slug and project_dir(slug).exists():
            results.append({"check": "Active project", "level": "ok",
                            "message": f"{slug} at {project_dir(slug)}"})
        elif slug:
            results.append({"check": "Active project", "level": "warn",
                            "message": f"'{slug}' selected but folder missing — /project list"})
        else:
            results.append({"check": "Active project", "level": "warn",
                            "message": "none selected — pick one with /project use or create via /project new"})
    except Exception as e:
        results.append({"check": "Active project", "level": "warn", "message": str(e)})

    try:
        from src.config.settings import REFERENCE_MOT

        candidates: list = []
        try:
            from src.config.projects import active_project_dir

            _apd = active_project_dir()
            if _apd is not None:
                candidates.extend(sorted((_apd / "models").glob("*.mot")))
        except Exception:
            pass
        if REFERENCE_MOT is not None:
            candidates.append(REFERENCE_MOT)
        found = next((c for c in candidates if c.exists()), None)
        if found is not None:
            results.append({"check": "Reference model", "level": "ok",
                            "message": str(found)})
        elif REFERENCE_MOT is not None:
            results.append({"check": "Reference model", "level": "warn",
                            "message": f"{REFERENCE_MOT} not found — Motor-CAD runs need a .mot in the project models/"})
        else:
            results.append({"check": "Reference model", "level": "warn",
                            "message": "no .mot in the active project models/ — Motor-CAD runs need one"})
    except Exception as e:
        results.append({"check": "Reference model", "level": "warn", "message": str(e)})

    try:
        from src.config.settings import WORKSPACE_ROOT

        probe = WORKSPACE_ROOT / ".write_probe"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink(missing_ok=True)
        results.append({"check": "Workspace", "level": "ok",
                        "message": f"{WORKSPACE_ROOT} writable"})
    except Exception as e:
        results.append({"check": "Workspace", "level": "error",
                        "message": f"workspace not writable: {e}"})

    if os.getenv("TAVILY_API_KEY"):
        results.append({"check": "Web search", "level": "ok",
                        "message": "TAVILY_API_KEY is set"})
    else:
        results.append({"check": "Web search", "level": "warn",
                        "message": "TAVILY_API_KEY missing — web search disabled (/key tavily ...)"})

    try:
        exe = Path(os.getenv("MOTORCAD_EXE", r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"))
        if exe.exists():
            results.append({"check": "Motor-CAD", "level": "ok", "message": str(exe)})
        else:
            results.append({"check": "Motor-CAD", "level": "warn",
                            "message": f"{exe} not found — solves will fail until installed"})
    except Exception as e:
        results.append({"check": "Motor-CAD", "level": "warn", "message": str(e)})

    return results


def render_preflight(console, results: list[dict]) -> None:
    """Print a compact preflight panel (failures highlighted, never raises)."""
    try:
        from rich.table import Table

        table = Table(title="[bold bright_cyan][PREFLIGHT] Environment[/bold bright_cyan]",
                      border_style="cyan", show_header=True)
        table.add_column("Check", style="bold cyan", no_wrap=True)
        table.add_column("Status", justify="center")
        table.add_column("Details", style="white")
        for r in results:
            level = r.get("level", "warn")
            badge = ("[bold green]OK[/bold green]" if level == "ok"
                     else "[bold red]FAIL[/bold red]" if level == "error"
                     else "[bold yellow]WARN[/bold yellow]")
            table.add_row(r.get("check", "?"), badge, str(r.get("message", ""))[:100])
        console.print()
        console.print(table)
        errors = sum(1 for r in results if r.get("level") == "error")
        if errors:
            console.print(f"  [bold red]{errors} blocking issue(s) — fix before Motor-CAD runs.[/bold red]\n")
        else:
            console.print("  [dim]Preflight clean. Re-run anytime with /preflight.[/dim]\n")
    except Exception:
        pass


__all__ = ["render_preflight", "run_preflight"]
