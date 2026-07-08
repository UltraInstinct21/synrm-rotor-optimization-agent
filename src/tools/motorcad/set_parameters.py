"""Motor-CAD parameter setting tools — safe wrappers with validation and checkpoints.

Anti-hallucination rules:
- Call ``get_variable_names()`` before any set.
- Save checkpoint before changing rotor params.
- Validate ranges before setting.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from langchain_core.tools import tool
from src.domain.motor.parameter_mapping import validate_parameter

from src.config.settings import REFERENCE_MOT

def _get_mc() -> Any:
    if _MC_INSTANCE is None:
        raise RuntimeError("Motor-CAD is not running. Call motorcad_launch first.")
    return _MC_INSTANCE


# Module-level instance holder (shared with run_motorcad.py via process global)
_MC_INSTANCE: Any | None = None


def set_mc_instance(mc: Any) -> None:
    """Set the module-level Motor-CAD instance."""
    global _MC_INSTANCE
    _MC_INSTANCE = mc


@tool
def motorcad_safe_get(var_name: str) -> str:
    """Read a variable from Motor-CAD. Returns the float value or 'Not found'."""
    mc = _get_mc()
    try:
        val = float(mc.get_variable(var_name))
        return str(val)
    except Exception:
        return f"Not found: {var_name}"


@tool
def motorcad_safe_set(var_name: str, value: float) -> str:
    """Set a Motor-CAD variable with verification (read-back check).

    Anti-hallucination: verifies variable exists via get_variable_names(),
    sets the value, then reads back to confirm.
    """
    mc = _get_mc()
    try:
        # Step 1: verify variable exists.
        available = mc.get_variable_names()
        if var_name not in available:
            return f"ERROR: Variable '{var_name}' not found in Motor-CAD"

        # Step 2: set.
        mc.set_variable(var_name, value)

        # Step 3: read back.
        readback = mc.get_variable(var_name)
        if abs(float(readback) - value) > 1e-6:
            return f"ERROR: Set verify failed: {var_name} = {readback} (expected {value})"

        return f"{var_name} = {value} OK"
    except Exception as e:
        return f"ERROR: Failed to set {var_name}: {e}"


@tool
def motorcad_set_parameter(var_name: str, value: float, domain: str = "stator", checkpoint_before: bool = False) -> str:
    """Set a Motor-CAD parameter with domain validation and optional checkpoint.

    Validates against known ranges (stator/rotor/winding/rating domains).
    Saves checkpoint before rotor changes if requested.

    Args:
        var_name: Motor-CAD variable name.
        value: Target value.
        domain: Validation domain — stator, rotor, winding, or rating.
        checkpoint_before: Save a .mot checkpoint before setting (recommended for rotor params).
    """
    mc = _get_mc()

    valid, msg = validate_parameter(var_name, value, domain=domain)
    if not valid:
        return f"ERROR: {msg}"

    if checkpoint_before and "rotor" in domain.lower():
        try:
            mc.save_to_file(str(Path.cwd() / "best_so_far.mot"))
        except Exception:
            pass  # non-fatal

    # Delegate to safe_set logic inline
    try:
        available = mc.get_variable_names()
        if var_name not in available:
            return f"ERROR: Variable '{var_name}' not found"

        mc.set_variable(var_name, value)
        readback = mc.get_variable(var_name)
        if abs(float(readback) - value) > 1e-6:
            return f"ERROR: Set verify failed: {var_name} = {readback} (expected {value})"

        return f"{var_name} = {value} OK"
    except Exception as e:
        return f"ERROR: Failed to set {var_name}: {e}"


@tool
def motorcad_save_checkpoint(path: str = "") -> str:
    """Save a .mot checkpoint file before making changes.

    Args:
        path: Checkpoint file path. Defaults to 'best_so_far.mot' in cwd.
    """
    mc = _get_mc()
    target = path or str(Path.cwd() / "best_so_far.mot")

    try:
        mc.save_to_file(target)
        return f"Checkpoint saved: {target}"
    except Exception as e:
        return f"ERROR: Checkpoint save failed: {e}"