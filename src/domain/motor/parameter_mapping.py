"""Parameter mapping — translate between MotorDesign models and Motor-CAD variable names.

Provides functions to:
- Discover available Motor-CAD variables for a given context.
- Map Pydantic model fields to Motor-CAD variable names.
- Validate parameter ranges before setting.
"""

from __future__ import annotations

from src.domain.motor.geometry_models import (
    MotorDesign,
    RatingConfig,
    RotorGeometry,
    StatorGeometry,
    WindingConfig,
)

# ── Motor-CAD variable name mappings ──────────────────────────────────
# Format: (model_field_path) → (motorcad_variable_name, unit, min, max)

STATOR_MAP: dict[str, tuple[str, str, float, float]] = {
    "outer_diameter_mm": ("Stator_OD", "mm", 50, 1000),
    "inner_diameter_mm": ("Stator_ID", "mm", 30, 900),
    "core_length_mm": ("Stack_Length", "mm", 10, 1000),
    "number_of_slots": ("Slot_Number", "", 12, 144),
}

ROTOR_MAP: dict[str, tuple[str, str, float, float]] = {
    "outer_diameter_mm": ("Rotor_OD", "mm", 20, 900),
    "inner_diameter_mm": ("Rotor_ID", "mm", 10, 500),
    "airgap_mm": ("Airgap_Length", "mm", 0.2, 5.0),
    "barrier_layers": ("Barrier_Layers", "", 2, 8),
}

WINDING_MAP: dict[str, tuple[str, str, float, float]] = {
    "turns_per_coil": ("Turns_Per_Coil", "", 1, 100),
    "parallel_paths": ("Parallel_Paths", "", 1, 8),
    "fill_factor": ("Fill_Factor", "", 0.2, 0.8),
    "wire_diameter_mm": ("Wire_Diameter", "mm", 0.1, 5.0),
}

RATING_MAP: dict[str, tuple[str, str, float, float]] = {
    "power_kw": ("Rated_Power", "kW", 0.1, 10000),
    "speed_rpm": ("Rated_Speed", "rpm", 1, 50000),
    "voltage_v": ("DC_Link_Voltage", "V", 10, 10000),
}


def get_map_for_domain(domain: str) -> dict[str, tuple[str, str, float, float]]:
    """Return the parameter map for a given domain name."""
    maps = {
        "stator": STATOR_MAP,
        "rotor": ROTOR_MAP,
        "winding": WINDING_MAP,
        "rating": RATING_MAP,
    }
    return maps.get(domain, {})


def design_to_motorcad_params(design: MotorDesign) -> dict[str, float]:
    """Flatten a MotorDesign into Motor-CAD variable → value pairs.

    Only includes mapped fields.  Values are validated against range limits.
    """
    params: dict[str, float] = {}

    _map_model("stator", design.stator, STATOR_MAP, params)
    _map_model("rotor", design.rotor, ROTOR_MAP, params)
    _map_model("winding", design.winding, WINDING_MAP, params)
    _map_model("rating", design.rating, RATING_MAP, params)

    return params


def _map_model(
    prefix: str,
    model_obj: object,
    mapping: dict[str, tuple[str, str, float, float]],
    params: dict[str, float],
) -> None:
    for field_path, (mc_var, _unit, _min_val, _max_val) in mapping.items():
        value = getattr(model_obj, field_path, None)
        if value is not None:
            params[mc_var] = float(value)


def validate_parameter(mc_var: str, value: float, domain: str = "stator") -> tuple[bool, str]:
    """Check a parameter value against its allowed range.

    Returns (valid, message).
    """
    mapping = get_map_for_domain(domain)
    for _, (var_name, unit, min_val, max_val) in mapping.items():
        if var_name == mc_var:
            if value < min_val or value > max_val:
                return (
                    False,
                    f"{mc_var}={value}{unit} outside range [{min_val}, {max_val}]{unit}",
                )
            return True, f"{mc_var}={value}{unit} OK"
    return True, f"{mc_var}: no validation rule (unknown parameter)"
