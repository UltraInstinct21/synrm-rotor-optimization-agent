"""Phase 4 — Design Node: parse .mot, discover variables, set parameters."""

import os
from datetime import datetime

from agent.state import AgentState
from agent.nodes.optimization import optimization_sub_node
from agent.tools.pymotorcad import (
    launch_motorcad,
    discover_variables,
    safe_set,
    save_backup,
    show_magnetic_context,
)
from agent.tools.rotor import ALLOWED_BARRIER_VARIABLES, check_geometry_constraints, default_barrier_params
from agent.memory import load_best_params, save_optimization_result


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


def _log(state: AgentState, msg: str) -> None:
    phase = state.get("phase", "?")
    print(f"  [{phase:<12}] {msg}")


def design_node(state: AgentState) -> AgentState:
    """Execute Phase 4: explore .mot, discover variables, set parameters."""
    # HITL skip check — user declined optimization at approval gate
    if state.get("approval", {}).get("proceed", True) is False:
        state["phase"] = "design"
        state["phase_status"]["design"] = {
            "status": "skipped",
            "error": "User skipped optimization at approval gate",
        }
        _log(state, "optimization skipped by user at approval gate")
        return state

    state["phase"] = "design"
    state["phase_status"]["design"] = {"status": "running", "error": None}
    errors = []
    opt_failed = False

    # Long-term memory: seed barrier_params from prior run, if available
    store = state.get("_store")
    if store:
        _log(state, "checking long-term memory for prior params...")
        remembered = load_best_params(store, state.get("motor_spec", {}))
        if remembered and not state.get("barrier_params"):
            state["barrier_params"] = remembered
            _log(state, f"seeded barrier_params from prior run ({len(remembered)} keys)")
            errors.append(f"Memory: seeded barrier_params from prior run ({len(remembered)} keys)")
        else:
            _log(state, "no prior params found in memory")

    # 1. Parse .mot file (no PyMotorCAD needed for parsing)
    mot_path = state.get("mot_file_path", _get_default_mot_path())
    _log(state, f"parsing .mot file: {os.path.basename(mot_path)}...")
    try:
        sections = _parse_mot_file(mot_path)
        state["mot_sections"] = sections
        _log(state, f".mot parsed: {len(sections)} sections found")
    except Exception as e:
        errors.append(f"Failed to parse .mot: {e}")
        sections = {}
        _log(state, f"failed to parse .mot: {e}")

    # 2. Try PyMotorCAD for variable discovery + parameter setting
    mc = None
    try:
        _log(state, "launching Motor-CAD...")
        mc = launch_motorcad(mot_path)
        if mc:
            _log(state, "Motor-CAD connected, discovering variables...")
            # AGENTS.md Rule 1: discover before first use
            vars_found = _try_discover_variables(mc)
            state["pymotorcad_vars"] = vars_found
            _log(state, f"discovered {len(vars_found)} variables")

            # AGENTS.md Rule 4: save backup before making changes
            _log(state, "saving backup .mot before changes...")
            backup_path = save_backup(mc, mot_path)
            _log(state, f"backup saved: {os.path.basename(backup_path)}")
            errors.append(f"Backup saved to: {backup_path}")

            # Capture magnetic context before any changes
            _log(state, "capturing magnetic context...")
            ctx = show_magnetic_context(mc)
            state["derived_params"]["pre_change_context"] = ctx

            _log(state, "setting barrier parameters in Motor-CAD...")
            bp = state.get("barrier_params") or default_barrier_params()
            check_geometry_constraints(bp)
            for var in ALLOWED_BARRIER_VARIABLES:
                safe_set(mc, var, bp[var])
            _log(state, "barrier parameters set successfully")
        else:
            _log(state, "Motor-CAD not available (graceful degradation)")
    except Exception as e:
        errors.append(f"PyMotorCAD error (non-fatal): {e}")
        _log(state, f"PyMotorCAD error (non-fatal): {e}")
        # Graceful degradation: continue with parsed .mot data

    # 3. Optimization sub-node — failure here marks design as failed
    _log(state, "starting optimization sub-node...")
    try:
        bp = state.get("barrier_params") or default_barrier_params()
        check_geometry_constraints(bp)
        state["barrier_params"] = bp
        optimization_update = optimization_sub_node(state)
        state.update(optimization_update)
        n_results = len(optimization_update.get("optimization_results", []))
        _log(state, f"optimization complete: {n_results} results")

        # Save results to long-term memory
        if store and optimization_update.get("optimization_results"):
            _log(state, "saving best result to long-term memory...")
            save_optimization_result(
                store,
                state.get("motor_spec", {}),
                bp,
                optimization_update["optimization_results"],
            )
    except Exception as e:
        errors.append(f"Optimization error: {e}")
        opt_failed = True
        _log(state, f"optimization failed: {e}")

    # Mark status: optimization failure → failed; PyMotorCAD-only failure → done (degraded)
    status = "failed" if opt_failed else "done"
    state["phase_status"]["design"] = {
        "status": status,
        "error": "; ".join(errors) if (opt_failed and errors) else None,
    }
    _log(state, f"design phase {status}" + (f" ({len(errors)} warnings)" if errors else ""))
    state["error_log"] = state.get("error_log", [])
    for err in errors:
        state["error_log"].append({
            "phase": "design",
            "error": err,
            "timestamp": datetime.now().isoformat(),
        })

    return state
