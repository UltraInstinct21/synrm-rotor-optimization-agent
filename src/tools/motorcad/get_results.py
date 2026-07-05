"""Motor-CAD result extraction — read outputs from a running Motor-CAD instance.

Anti-hallucination rules:
- Always call ``get_variable_names()`` before accessing specific variables.
- Read ALL results before changing parameters.
"""

from __future__ import annotations

from typing import Any

from src.domain.motor.result_models import ElectromagneticResult

# Known Motor-CAD variable names for the magnetic context.
_RESULT_VARIABLES: dict[str, str] = {
    "Torque": "torque_nm",
    "Efficiency": "efficiency_pct",
    "Power Factor": "power_factor",
    "Speed": "speed_rpm",
    "Output Power": "output_power_kw",
    "Ld": "ld_mh",
    "Lq": "lq_mh",
    "Saliency Ratio": "saliency",
    "Iron Loss": "iron_loss_w",
    "Copper Loss": "copper_loss_w",
    "Magnet Loss": "magnet_loss_w",
    "Mechanical Loss": "mechanical_loss_w",
}


def get_available_variables(mc_instance: Any) -> list[str]:
    """Discover available variables — ALWAYS call before get/set."""
    try:
        return mc_instance.get_variable_names()
    except Exception:
        return []


def safe_get(mc_instance: Any, var_name: str) -> float | None:
    """Safely get a Motor-CAD variable value, returning None on failure."""
    try:
        val = mc_instance.get_variable(var_name)
        return float(val)
    except Exception:
        return None


def extract_results(mc_instance: Any) -> ElectromagneticResult:
    """Read all electromagnetic results from a Motor-CAD instance.

    1. Discovers available variables.
    2. Reads every mapped result variable.
    3. Returns an ElectromagneticResult with found values.
    """
    available = get_available_variables(mc_instance)
    raw: dict[str, float | None] = {}

    for mc_var, model_field in _RESULT_VARIABLES.items():
        if mc_var in available:
            raw[model_field] = safe_get(mc_instance, mc_var)
        else:
            raw[model_field] = None

    return ElectromagneticResult(**raw)
