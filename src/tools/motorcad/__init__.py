"""Motor-CAD tools for Deep Agents.

These tools wrap PyMotorCAD operations with anti-hallucination safeguards.
Deep Agents discovers them via the [tools] packages config.
"""

from src.tools.motorcad.run_motorcad import (
    motorcad_launch,
    motorcad_load_model,
    motorcad_run_magnetic,
    motorcad_run_and_extract,
    motorcad_close,
)
from src.tools.motorcad.set_parameters import (
    motorcad_safe_get,
    motorcad_safe_set,
    motorcad_set_parameter,
    motorcad_save_checkpoint,
)
from src.tools.motorcad.get_results import (
    motorcad_get_variables,
    motorcad_extract_results,
)

__all__ = [
    "motorcad_launch",
    "motorcad_load_model",
    "motorcad_run_magnetic",
    "motorcad_run_and_extract",
    "motorcad_close",
    "motorcad_safe_get",
    "motorcad_safe_set",
    "motorcad_set_parameter",
    "motorcad_save_checkpoint",
    "motorcad_get_variables",
    "motorcad_extract_results",
]