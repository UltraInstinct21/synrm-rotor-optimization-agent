"""Motor-CAD parameter setting — safe wrappers with validation and checkpoints.

Anti-hallucination rules:
- Call ``get_variable_names()`` before any set.
- Save checkpoint before changing rotor params.
- Validate ranges before setting.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from src.domain.motor.parameter_mapping import validate_parameter


def safe_get(mc_instance: Any, var_name: str) -> float | None:
    """Safely read a variable, returning None on failure."""
    try:
        return float(mc_instance.get_variable(var_name))
    except Exception:
        return None


def safe_set(mc_instance: Any, var_name: str, value: float) -> tuple[bool, str]:
    """Set a Motor-CAD variable with safety checks.

    Steps:
    1. Verify the variable exists via ``get_variable_names()``.
    2. Set the value.
    3. Verify the set by reading back.

    Returns (success, message).
    """
    try:
        # Step 1: verify variable exists.
        available = mc_instance.get_variable_names()
        if var_name not in available:
            return (False, f"Variable '{var_name}' not found in Motor-CAD instance")

        # Step 2: set.
        mc_instance.set_variable(var_name, value)

        # Step 3: read back.
        readback = mc_instance.get_variable(var_name)
        if abs(float(readback) - value) > 1e-6:
            return (False, f"Set verify failed: {var_name} = {readback} (expected {value})")

        return (True, f"{var_name} = {value} OK")

    except Exception as e:
        return (False, f"Failed to set {var_name}: {e}")


def save_checkpoint(mc_instance: Any, path: str | Path | None = None) -> str:
    """Save a checkpoint .mot file before making rotor changes.

    Returns the checkpoint file path.
    """
    if path is None:
        path = Path.cwd() / "best_so_far.mot"
    path = Path(path)

    try:
        mc_instance.save_to_file(str(path))
        return str(path)
    except Exception as e:
        return f"Checkpoint save failed: {e}"


def set_parameter(
    mc_instance: Any,
    var_name: str,
    value: float,
    domain: str = "stator",
    checkpoint_before: bool = False,
) -> tuple[bool, str]:
    """Set a single Motor-CAD parameter with validation.

    Parameters
    ----------
    mc_instance : Any
        Motor-CAD COM instance.
    var_name : str
        Motor-CAD variable name.
    value : float
        Target value.
    domain : str
        Domain for range validation (stator, rotor, winding, rating).
    checkpoint_before : bool
        Save a checkpoint before setting (recommended for rotor params).

    Returns
    -------
    (success, message)
    """
    # Validate range.
    valid, msg = validate_parameter(var_name, value, domain=domain)
    if not valid:
        return False, msg

    # Checkpoint.
    if checkpoint_before and "rotor" in domain.lower():
        save_checkpoint(mc_instance)

    # Set.
    return safe_set(mc_instance, var_name, value)
