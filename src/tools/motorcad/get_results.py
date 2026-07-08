"""Motor-CAD result extraction tools — read outputs from a running instance."""

from __future__ import annotations

from typing import Any

from langchain_core.tools import tool

from src.domain.motor.result_models import ElectromagneticResult

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

_MC_INSTANCE: Any | None = None


def set_mc_instance(mc: Any) -> None:
    global _MC_INSTANCE
    _MC_INSTANCE = mc


def _get_mc() -> Any:
    if _MC_INSTANCE is None:
        raise RuntimeError("Motor-CAD is not running. Call motorcad_launch first.")
    return _MC_INSTANCE


def _safe_get(mc: Any, var_name: str) -> float | None:
    try:
        return float(mc.get_variable(var_name))
    except Exception:
        return None


def extract_results(mc: Any) -> ElectromagneticResult:
    """Read all electromagnetic results (used internally by tools)."""
    try:
        available = mc.get_variable_names()
    except Exception:
        available = []

    raw: dict[str, float | None] = {}
    for mc_var, model_field in _RESULT_VARIABLES.items():
        raw[model_field] = _safe_get(mc, mc_var) if mc_var in available else None

    return ElectromagneticResult(**raw)


@tool
def motorcad_get_variables() -> str:
    """List all available Motor-CAD variable names in the current context."""
    mc = _get_mc()
    try:
        names = mc.get_variable_names()
        return "\n".join(sorted(names))
    except Exception as e:
        return f"ERROR: Could not get variables: {e}"


@tool
def motorcad_extract_results() -> str:
    """Extract all electromagnetic results as JSON.

    Returns torque, efficiency, power factor, inductances, and losses.
    Must run electromagnetic analysis first (motorcad_run_magnetic).
    """
    mc = _get_mc()
    result = extract_results(mc)
    return result.model_dump_json(indent=2)
