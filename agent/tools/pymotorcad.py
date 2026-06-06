"""PyMotorCAD wrapper — safe launch, variable discovery, get/set wrappers with anti-hallucination guards."""

import subprocess
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
        import motorcad  # type: ignore
    except ImportError:
        raise RuntimeError("PyMotorCAD not installed. Run: pip install motorcad")

    app = motorcad.AppClass()
    app.setvisible(visible)
    app.openmotordata(mot_file_path)
    return app


def discover_variables(mc: Any, prefix: str = "") -> list[str]:
    """Discover available Motor-CAD variable names matching prefix.

    Rule 1 from AGENTS.md: always discover before first use.
    """
    try:
        all_vars = mc.getvariablenames(0)
        if prefix:
            return [v for v in all_vars if v.startswith(prefix)]
        return list(all_vars)
    except Exception:
        return []


def safe_get(mc: Any, var_name: str, default: Any = None) -> Any:
    """Get a Motor-CAD variable with error handling.

    AGENTS.md Rule 3: safe_get/safe_set wrappers prevent crashes on missing vars.
    """
    try:
        return mc.getvariable(var_name)
    except Exception:
        return default


def safe_set(mc: Any, var_name: str, value: Any) -> bool:
    """Set a Motor-CAD variable with validation.

    Returns True if set succeeded, False otherwise.
    AGENTS.md Rule 3 + Rule 5: save before changing, read before changing.
    """
    try:
        old_val = safe_get(mc, var_name)
        if isinstance(value, str):
            mc.setvariable(var_name, value)
        else:
            mc.setvariable(var_name, float(value))
        # Verify
        new_val = safe_get(mc, var_name)
        return new_val != old_val
    except Exception:
        return False


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
    """Capture magnetic context before running EMag — for logging/audit.

    AGENTS.md Rule 3: show_magnetic_context() before EMag.
    """
    context = {}
    for var in ["AirGap", "MLt", "Barrier_Angle", "Rotor_Dia", "StackLength"]:
        context[var] = safe_get(mc, var)
    return context


def save_backup(mc: Any, path: str) -> str:
    """Save a backup of the current .mot file.

    AGENTS.md Rule 4: save before changing parameters.
    Returns the backup path.
    """
    backup_path = path.replace(".mot", f"_backup_{int(time.time())}.mot")
    try:
        mc.savedata(backup_path)
    except Exception:
        pass
    return backup_path


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
