"""Motor-CAD launcher — start, load models, and run analyses.

Provides:
- ``launch_motorcad()`` — start or connect to Motor-CAD.
- ``load_model()`` — open a .mot file.
- ``run_magnetic()`` — run electromagnetic analysis.
- ``close_motorcad()`` — clean shutdown.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Any

from src.tools.motorcad.get_results import extract_results
from src.tools.motorcad.set_parameters import save_checkpoint, set_parameter
from src.domain.motor.result_models import ElectromagneticResult

_MC_INSTANCE: Any | None = None


def launch_motorcad(
    visible: bool = False,
    model_path: str | Path | None = None,
) -> Any:
    """Launch (or connect to) a Motor-CAD instance.

    Parameters
    ----------
    visible : bool
        Whether to show the Motor-CAD GUI.
    model_path : str | Path, optional
        .mot file to load on startup.

    Returns
    -------
    Motor-CAD COM instance (``ansys.motorcad.core``).
    """
    global _MC_INSTANCE

    try:
        from ansys.motorcad.core import MotorCAD

        mc = MotorCAD(visible=visible)
        _MC_INSTANCE = mc

        if model_path:
            mc.load_from_file(str(model_path))

        return mc

    except ImportError:
        print("  ⚠️  ansys.motorcad.core not installed. Cannot launch Motor-CAD.")
        return None
    except Exception as e:
        print(f"  ⚠️  Motor-CAD launch failed: {e}")
        return None


def load_model(mc_instance: Any | None = None, path: str | Path | None = None) -> bool:
    """Load a .mot model into a Motor-CAD instance."""
    mc = mc_instance or _MC_INSTANCE
    if not mc:
        return False
    if not path:
        path = Path.cwd() / "SynRM_45kW_IE5.mot"

    try:
        mc.load_from_file(str(path))
        return True
    except Exception as e:
        print(f"  ⚠️  Load model failed: {e}")
        return False


def run_magnetic(mc_instance: Any | None = None) -> bool:
    """Run the electromagnetic analysis context.

    Per anti-hallucination rules: calls ``show_magnetic_context()`` first.
    """
    mc = mc_instance or _MC_INSTANCE
    if not mc:
        return False

    try:
        mc.show_magnetic_context()
        return True
    except Exception as e:
        print(f"  ⚠️  Magnetic analysis failed: {e}")
        return False


def run_and_extract(
    mc_instance: Any | None = None,
) -> ElectromagneticResult | None:
    """Run magnetic analysis and extract results.

    Returns ElectromagneticResult or None on failure.
    """
    mc = mc_instance or _MC_INSTANCE
    if not mc:
        return None

    if not run_magnetic(mc):
        return None

    return extract_results(mc)


def close_motorcad(mc_instance: Any | None = None) -> None:
    """Close Motor-CAD cleanly."""
    global _MC_INSTANCE
    mc = mc_instance or _MC_INSTANCE
    if mc:
        try:
            mc.quit()
        except Exception:
            pass
    _MC_INSTANCE = None
