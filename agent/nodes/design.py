"""Phase 4 — Design Node: parse .mot, discover variables, set parameters."""

import os
from datetime import datetime

from agent.state import AgentState
from agent.tools.pymotorcad import (
    launch_motorcad,
    discover_variables,
    safe_get,
    safe_set,
    save_backup,
    show_magnetic_context,
)


def _parse_mot_file(path: str) -> dict[str, dict]:
    """Parse a .mot file into section->param->value dict.

    .mot files use INI-like section headers [SectionName].
    Returns {section: {param: value, ...}, ...}
    """
    sections = {}
    current_section = "_header"
    sections[current_section] = {}

    if not os.path.exists(path):
        return sections

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith(";"):
                continue
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1]
                sections[current_section] = {}
            elif "=" in line and current_section:
                key, _, val = line.partition("=")
                sections[current_section][key.strip()] = val.strip()

    return sections


def _try_discover_variables(mc) -> list[str]:
    """Discover Motor-CAD variable names with fallback."""
    try:
        return discover_variables(mc)
    except Exception:
        return []


def _get_default_mot_path() -> str:
    """Default .mot file path if none in state."""
    return "D:/SRM/Agent/SynRM_45kW_IE5.mot"


def design_node(state: AgentState) -> AgentState:
    """Execute Phase 4: explore .mot, discover variables, set parameters."""
    state["phase"] = "design"
    state["phase_status"]["design"] = {"status": "running", "error": None}
    errors = []

    # 1. Parse .mot file (no PyMotorCAD needed for parsing)
    mot_path = state.get("mot_file_path", _get_default_mot_path())
    try:
        sections = _parse_mot_file(mot_path)
        state["mot_sections"] = sections
    except Exception as e:
        errors.append(f"Failed to parse .mot: {e}")
        sections = {}

    # 2. Try PyMotorCAD for variable discovery + parameter setting
    mc = None
    try:
        mc = launch_motorcad(mot_path)
        if mc:
            # AGENTS.md Rule 1: discover before first use
            vars_found = _try_discover_variables(mc)
            state["pymotorcad_vars"] = vars_found

            # AGENTS.md Rule 4: save backup before making changes
            backup_path = save_backup(mc, mot_path)
            errors.append(f"Backup saved to: {backup_path}")

            # Capture magnetic context before any changes
            ctx = show_magnetic_context(mc)
            state["derived_params"]["pre_change_context"] = ctx

            # Set winding parameters from state if available
            wp = state.get("winding_params", {})
            for var, val in wp.items():
                # Only set if we have a numeric value
                if isinstance(val, (int, float)):
                    safe_set(mc, var, val)

            # Set barrier parameters
            bp = state.get("barrier_params", {})
            for var, val in bp.items():
                if isinstance(val, (int, float)):
                    safe_set(mc, var, val)

    except Exception as e:
        errors.append(f"PyMotorCAD error (non-fatal): {e}")
        # Graceful degradation: continue with parsed .mot data

    # Mark done (success even if PyMotorCAD unavailable — we have parsed sections)
    state["phase_status"]["design"] = {"status": "done", "error": None}
    state["error_log"] = state.get("error_log", [])
    for err in errors:
        state["error_log"].append({
            "phase": "design",
            "error": err,
            "timestamp": datetime.now().isoformat(),
        })

    return state
