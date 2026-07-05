"""Motor-domain models — geometry, parameters, results, and optimization."""

from src.domain.motor.geometry_models import (
    MotorDesign,
    RatingConfig,
    RotorGeometry,
    StatorGeometry,
    WindingConfig,
)
from src.domain.motor.parameter_mapping import (
    design_to_motorcad_params,
    get_map_for_domain,
    validate_parameter,
)
from src.domain.motor.result_models import (
    ComparisonResult,
    ElectromagneticResult,
)

__all__ = [
    "MotorDesign",
    "StatorGeometry",
    "RotorGeometry",
    "WindingConfig",
    "RatingConfig",
    "ElectromagneticResult",
    "ComparisonResult",
    "design_to_motorcad_params",
    "validate_parameter",
    "get_map_for_domain",
]
