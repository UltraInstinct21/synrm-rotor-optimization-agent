"""Motor-CAD launcher tools — start, load models, and run analyses."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from langchain_core.tools import tool

from src.config.settings import REFERENCE_MOT


_MC_INSTANCE: Any | None = None


def _get_mc() -> Any:
    """Return the active Motor-CAD instance or raise."""
    if _MC_INSTANCE is None:
        raise RuntimeError("Motor-CAD is not running. Call motorcad_launch first.")
    return _MC_INSTANCE


@tool
def motorcad_launch(visible: bool = False, model_path: str = "") -> str:
    """Launch or connect to a Motor-CAD instance.

    Args:
        visible: Whether to show the Motor-CAD GUI.
        model_path: Optional .mot file to load on startup. Defaults to reference model.
    """
    global _MC_INSTANCE

    try:
        from ansys.motorcad.core import MotorCAD

        mc = MotorCAD(visible=visible)
        _MC_INSTANCE = mc

        path = model_path or str(REFERENCE_MOT)
        if path and Path(path).exists():
            mc.load_from_file(path)
            return f"Motor-CAD launched and loaded {path}"
        return "Motor-CAD launched (no model loaded)"

    except ImportError:
        return "ERROR: ansys.motorcad.core not installed. Cannot launch Motor-CAD."
    except Exception as e:
        return f"ERROR: Motor-CAD launch failed: {e}"


@tool
def motorcad_load_model(path: str = "") -> str:
    """Load a .mot model file into Motor-CAD.

    Args:
        path: Path to .mot file. Defaults to reference model.
    """
    mc = _get_mc()
    target = path or str(REFERENCE_MOT)

    try:
        mc.load_from_file(target)
        return f"Loaded {target}"
    except Exception as e:
        return f"ERROR: Load failed: {e}"


@tool
def motorcad_run_magnetic() -> str:
    """Run electromagnetic analysis. Calls show_magnetic_context() per anti-hallucination rules."""
    mc = _get_mc()

    try:
        mc.show_magnetic_context()
        return "Electromagnetic analysis completed"
    except Exception as e:
        return f"ERROR: Magnetic analysis failed: {e}"


@tool
def motorcad_run_and_extract() -> str:
    """Run electromagnetic analysis and extract all results as JSON.

    Returns torque, efficiency, power factor, inductances, and losses.
    """
    mc = _get_mc()

    try:
        mc.show_magnetic_context()
    except Exception as e:
        return f"ERROR: Magnetic analysis failed: {e}"

    from src.tools.motorcad.get_results import extract_results

    result = extract_results(mc)
    return result.model_dump_json(indent=2)


@tool
def motorcad_close() -> str:
    """Close Motor-CAD cleanly."""
    global _MC_INSTANCE
    mc = _MC_INSTANCE
    if mc:
        try:
            mc.quit()
        except Exception:
            pass
    _MC_INSTANCE = None
    return "Motor-CAD closed"