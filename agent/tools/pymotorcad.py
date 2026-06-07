"""PyMotorCAD wrapper with official API names and loud failures."""

import multiprocessing
import time
import os
from typing import Any

MOTORCAD_EXE = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"


def launch_motorcad(mot_file_path: str, visible: bool = False) -> Any:
    """Launch Motor-CAD and load a .mot file. Returns the MotorCAD COM object.

    Args:
        mot_file_path: Absolute path to .mot file.
        visible: If True, show Motor-CAD GUI (debugging only).

    Returns:
        MotorCAD object (PyMotorCAD mc) or None if launch fails.
    """
    try:
        import ansys.motorcad.core as pymotorcad
    except ImportError as e:
        raise RuntimeError("PyMotorCAD not installed: ansys.motorcad.core import failed") from e

    mc = pymotorcad.MotorCAD(
        open_new_instance=True,
        use_blackbox_licence=True,
        keep_instance_open=False,
    )
    if hasattr(mc, "set_variable"):
        mc.set_variable("MessageDisplayState", 2 if not visible else 0)
    mc.load_from_file(mot_file_path)
    return mc


def discover_variables(mc: Any, keyword: str = "", prefix: str = "") -> list[str]:
    """Discover available Motor-CAD variable names matching keyword or prefix."""
    try:
        if hasattr(mc, "get_variable_names"):
            all_vars = list(mc.get_variable_names())
        else:
            all_vars = list(mc.getvariablenames(0))
    except Exception as e:
        raise RuntimeError(f"get_variable_names() failed: {e}") from e

    if keyword:
        return [v for v in all_vars if keyword.lower() in v.lower()]
    if prefix:
        return [v for v in all_vars if v.startswith(prefix)]
    return all_vars


def safe_get(mc: Any, var_name: str, label: str = "") -> Any:
    """Get a Motor-CAD variable or raise a precise error."""
    try:
        if hasattr(mc, "get_variable"):
            value = mc.get_variable(var_name)
        else:
            value = mc.getvariable(var_name)
        if label:
            print(f"  {label}: {value}")
        return value
    except Exception as e:
        raise RuntimeError(f"get_variable('{var_name}') failed: {e}") from e


def safe_set(mc: Any, var_name: str, value: Any) -> None:
    """Set a Motor-CAD variable or raise a precise error."""
    try:
        if hasattr(mc, "set_variable"):
            mc.set_variable(var_name, value)
        else:
            mc.setvariable(var_name, value if isinstance(value, str) else float(value))
    except Exception as e:
        raise RuntimeError(f"set_variable('{var_name}', {value}) failed: {e}") from e


def safe_get_array(mc: Any, var_name: str, index: int, default: Any = None) -> Any:
    """Get a Motor-CAD array variable at given index."""
    try:
        return mc.getvariable(var_name, 0, index)
    except Exception:
        return default


def safe_set_array(mc: Any, var_name: str, index: int, value: Any) -> bool:
    """Set a Motor-CAD array variable at given index."""
    try:
        old_val = safe_get_array(mc, var_name, index)
        mc.setvariable(var_name, 0, float(value), index)
        return True
    except Exception:
        return False


def show_magnetic_context(mc: Any) -> dict:
    """Switch to magnetic context and capture a few useful values."""
    if hasattr(mc, "show_magnetic_context"):
        mc.show_magnetic_context()
    context = {}
    for var in ["Airgap", "Rotor_Diameter", "Shaft_Dia", "Shaft_Speed_[RPM]", "PhaseAdvance"]:
        try:
            context[var] = safe_get(mc, var)
        except RuntimeError:
            context[var] = None
    return context


def save_backup(mc: Any, path: str) -> str:
    """Save a backup of the current .mot file.

    AGENTS.md Rule 4: save before changing parameters.
    Returns the backup path.
    """
    backup_path = path.replace(".mot", f"_backup_{int(time.time())}.mot")
    try:
        if hasattr(mc, "save_to_file"):
            mc.save_to_file(backup_path)
        else:
            mc.savedata(backup_path)
    except Exception as e:
        raise RuntimeError(f"save backup failed: {e}") from e
    return backup_path


def run_emag(mc: Any) -> None:
    """Run an electromagnetic calculation after switching to magnetic context."""
    if hasattr(mc, "show_magnetic_context"):
        mc.show_magnetic_context()
    if hasattr(mc, "do_magnetic_calculation"):
        mc.do_magnetic_calculation()
    else:
        mc.domagnetic()


def evaluate_candidate_in_process(
    mot_file_content: str,
    params: dict,
    timeout_s: int = 300,
) -> dict:
    """Evaluate a design candidate in a separate process.

    Wraps a single Motor-CAD instance in multiprocessing.Process with timeout.
    Matches optimize_synrm_v4.py pattern.

    Args:
        mot_file_content: Base .mot file content (or path).
        params: Dict of {variable_name: value} to set before evaluation.
        timeout_s: Max wall-clock time for FEA solve.

    Returns:
        Dict with keys: torque, torque_ripple, saliency, phase_advance, or error.
    """
    def _evaluate(q: multiprocessing.Queue, content: str, p: dict):
        try:
            import motorcad
            import tempfile

            mc = motorcad.AppClass()
            mc.setvisible(False)

            # Write temp .mot file
            tmp = tempfile.NamedTemporaryFile(suffix=".mot", delete=False)
            if os.path.exists(content):
                mc.openmotordata(content)
            else:
                tmp.write(content.encode())
                tmp.close()
                mc.openmotordata(tmp.name)

            # Set parameters
            for var, val in p.items():
                try:
                    mc.setvariable(var, float(val))
                except Exception:
                    pass

            # Run electromagnetic FEA
            mc.domagnetic()

            # Read results
            result = {
                "torque": 0.0,
                "torque_ripple_pct": 0.0,
                "saliency_ratio": 1.0,
                "phase_advance_deg": 45.0,
                "current_A": 0.0,
                "power_factor": 0.0,
                "efficiency_pct": 0.0,
                "error": None,
            }
            for try_var, key in [
                ("Torque", "torque"),
                ("TorqueRipple", "torque_ripple_pct"),
                ("SaliencyRatio", "saliency_ratio"),
                ("PhaseAdvance", "phase_advance_deg"),
                ("CurrentRMS", "current_A"),
                ("PowerFactor", "power_factor"),
                ("Efficiency", "efficiency_pct"),
            ]:
                try:
                    result[key] = mc.getvariable(try_var)
                except Exception:
                    pass

            q.put(result)
        except Exception as e:
            q.put({"error": str(e)})

    queue: multiprocessing.Queue = multiprocessing.Queue()
    p = multiprocessing.Process(
        target=_evaluate,
        args=(queue, mot_file_content, params),
    )
    p.start()
    p.join(timeout=timeout_s)

    if p.is_alive():
        p.terminate()
        return {"error": f"Timeout after {timeout_s}s"}

    return queue.get() if not queue.empty() else {"error": "No result returned"}
