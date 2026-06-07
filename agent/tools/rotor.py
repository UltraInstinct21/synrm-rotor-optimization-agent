"""Rotor barrier guardrails, scoring, and result logging."""

import csv
import math
import os
import time
from typing import Any

SHAFT_DIA_MM = 80.0
ROTOR_DIA_MM = 214.0
TARGET_TORQUE_NM = 143.0
TARGET_EFFICIENCY_PCT = 96.0
RATED_SPEED_RPM = 3000.0

ALLOWED_BARRIER_VARIABLES = (
    "L1_Diameter",
    "L1_Bridge_Thickness",
    "L1_Web_Thickness",
    "L1_Outer_Angle_Offset",
    "L1_Outer_Thickness",
    "L1_Inner_Thickness",
    "L2_Diameter",
    "L2_Bridge_Thickness",
    "L2_Web_Thickness",
    "L3_Diameter",
    "L3_Bridge_Thickness",
    "L3_Web_Thickness",
)

SEARCH_RANGES = {
    "L1_Diameter": (90.0, 115.0),
    "L1_Bridge_Thickness": (1.0, 6.0),
    "L1_Web_Thickness": (5.0, 30.0),
    "L1_Outer_Angle_Offset": (-20.0, 0.0),
    "L1_Outer_Thickness": (2.0, 8.0),
    "L1_Inner_Thickness": (2.0, 8.0),
    "L2_Diameter": (120.0, 150.0),
    "L2_Bridge_Thickness": (1.0, 6.0),
    "L2_Web_Thickness": (20.0, 70.0),
    "L3_Diameter": (145.0, 175.0),
    "L3_Bridge_Thickness": (1.0, 6.0),
    "L3_Web_Thickness": (50.0, 100.0),
}

BASELINE_BARRIER_PARAMS = {
    "L1_Diameter": 100,
    "L1_Bridge_Thickness": 4,
    "L1_Web_Thickness": 17,
    "L1_Outer_Angle_Offset": -10,
    "L1_Outer_Thickness": 4,
    "L1_Inner_Thickness": 5,
    "L2_Diameter": 130,
    "L2_Bridge_Thickness": 5,
    "L2_Web_Thickness": 50,
    "L3_Diameter": 160,
    "L3_Bridge_Thickness": 5,
    "L3_Web_Thickness": 82,
}


def default_barrier_params() -> dict[str, float | int]:
    """Return the Motor-CAD GUI baseline for the 12 allowed barrier variables."""
    return dict(BASELINE_BARRIER_PARAMS)


def check_geometry_constraints(params: dict[str, Any]) -> bool:
    """Validate allowed rotor barrier variables and mechanical constraints."""
    unknown = sorted(set(params) - set(ALLOWED_BARRIER_VARIABLES))
    if unknown:
        raise ValueError(f"Rotor parameter(s) not allowed: {', '.join(unknown)}")

    missing = [name for name in ALLOWED_BARRIER_VARIABLES if name not in params]
    if missing:
        raise ValueError(f"Missing rotor parameter(s): {', '.join(missing)}")

    if not float(params["L1_Diameter"]) > SHAFT_DIA_MM:
        raise ValueError("L1_Diameter must be greater than Shaft_Dia")
    if not float(params["L1_Diameter"]) < float(params["L2_Diameter"]):
        raise ValueError("L1_Diameter < L2_Diameter required")
    if not float(params["L2_Diameter"]) < float(params["L3_Diameter"]):
        raise ValueError("L2_Diameter < L3_Diameter required")
    if not float(params["L3_Diameter"]) < ROTOR_DIA_MM:
        raise ValueError("L3_Diameter must be less than Rotor_Diameter")

    for layer in ("L1", "L2", "L3"):
        key = f"{layer}_Bridge_Thickness"
        if float(params[key]) < 1.0:
            raise ValueError(f"{key} must be >= 1 mm")

    if float(params["L3_Diameter"]) + float(params["L1_Outer_Thickness"]) >= ROTOR_DIA_MM:
        raise ValueError("L3_Diameter + L1_Outer_Thickness must be < 214 mm")

    for name, value in params.items():
        lo, hi = SEARCH_RANGES[name]
        if not lo <= float(value) <= hi:
            raise ValueError(f"{name}={value} outside search range {lo}..{hi}")

    return True


def shaft_power_w(torque_nm: float, speed_rpm: float = RATED_SPEED_RPM) -> float:
    """Calculate shaft power from torque and speed."""
    return torque_nm * speed_rpm * 2 * math.pi / 60.0


def efficiency_pct(torque_nm: float, input_power_w: float) -> float:
    """Calculate efficiency percent from shaft torque and input power."""
    if input_power_w <= 0:
        return 0.0
    return shaft_power_w(torque_nm) / input_power_w * 100.0


def objective(
    results: dict[str, Any],
    target_torque: float = TARGET_TORQUE_NM,
    target_efficiency_pct: float = TARGET_EFFICIENCY_PCT,
) -> float:
    """Lower-is-better score for torque error and IE5 efficiency shortfall."""
    torque = float(results.get("ShaftTorque", results.get("torque", 0)) or 0)
    efficiency = float(
        results.get("Efficiency", results.get("MotorEfficiency", results.get("efficiency_pct", 0))) or 0
    )
    torque_error = abs(torque - target_torque) / target_torque
    eff_penalty = max(0.0, target_efficiency_pct - efficiency)
    return torque_error * 100.0 + eff_penalty


def log_result(
    csv_path: str,
    iteration: int | str,
    params: dict[str, Any],
    torque: float,
    input_power: float,
    shaft_power: float,
    efficiency: float,
    extra: dict[str, Any] | None = None,
) -> None:
    """Append one Motor-CAD result row immediately after reading results."""
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    row = {
        "iteration": iteration,
        "timestamp": time.time(),
        **params,
        "ShaftTorque": torque,
        "InputPower": input_power,
        "ShaftPower": shaft_power,
        "Efficiency": efficiency,
        **(extra or {}),
    }
    write_header = not os.path.exists(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row.keys()))
        if write_header:
            writer.writeheader()
        writer.writerow(row)
