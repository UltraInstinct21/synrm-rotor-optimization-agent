"""Spec compliance scoring — computed pass/fail, never eyeballed.

Derives shaft power / efficiency from torque + input power + speed, then
checks every spec target. Lower objective is better.
"""

from __future__ import annotations

import math

from src.motor.spec import MachineSpec, load_active_spec


def derive_metrics(results: dict, speed_rpm: float) -> dict:
    """Derive shaft_power_w / efficiency_pct / output_power_kw when possible."""
    metrics = dict(results)
    try:
        torque = float(results.get("torque", math.nan))
        input_pwr = float(results.get("input_power_w", math.nan))
    except (TypeError, ValueError):
        return metrics
    if math.isnan(torque) or math.isnan(input_pwr):
        return metrics
    shaft_pwr = torque * float(speed_rpm) * 2 * math.pi / 60.0
    metrics["shaft_power_w"] = shaft_pwr
    metrics["output_power_kw"] = shaft_pwr / 1000.0
    metrics["efficiency_pct"] = (shaft_pwr / input_pwr * 100.0) if input_pwr > 0 else 0.0
    return metrics


def score_candidate(results: dict, spec: MachineSpec | None = None,
                    spec_path: str = "") -> dict:
    """Score a result dict against spec targets.

    results keys (all optional, missing targets are marked missing/failed):
      torque, input_power_w, speed_rpm, power_factor, efficiency_pct,
      output_power_kw (last two need not be given — derived when possible).
    Returns {"objective": float, "checks": [...], "all_passed": bool}.
    """
    spec = spec or load_active_spec(spec_path)
    if not isinstance(results, dict):
        return {"objective": float("inf"), "checks": [], "all_passed": False,
                "error": "results must be an object"}

    speed = results.get("speed_rpm", spec.operating_point.get("Shaft_Speed_[RPM]", 3000))
    try:
        speed = float(speed)
    except (TypeError, ValueError):
        speed = 3000.0
    metrics = derive_metrics(results, speed)

    objective = 0.0
    checks: list[dict] = []
    for target in spec.targets:
        key = target["key"]
        value = metrics.get(key)
        check: dict = {"key": key, "label": target.get("label", key),
                       "value": value}
        if value is None:
            check.update({"value": None, "passed": False, "reason": "not reported"})
            objective += 100.0  # heavy penalty for unreported targets
            checks.append(check)
            continue
        try:
            v = float(value)
        except (TypeError, ValueError):
            check.update({"passed": False, "reason": f"non-numeric: {value!r}"})
            objective += 100.0
            checks.append(check)
            continue
        check["value"] = v
        if "tol_pct" in target:
            t = float(target["target"])
            dev_pct = abs(v - t) / abs(t) * 100.0 if t != 0 else abs(v) * 100.0
            passed = dev_pct <= float(target["tol_pct"])
            check.update({"target": t, "tol_pct": target["tol_pct"],
                          "dev_pct": round(dev_pct, 3), "passed": passed})
            objective += dev_pct
        else:  # minimum requirement
            minimum = float(target["min"])
            shortfall = max(0.0, (minimum - v) / abs(minimum) * 100.0) if minimum != 0 else max(0.0, minimum - v)
            passed = v >= minimum
            check.update({"min": minimum, "shortfall_pct": round(shortfall, 3), "passed": passed})
            objective += shortfall * 2.0  # minima violations hurt double
        checks.append(check)

    return {"objective": round(objective, 4), "checks": checks,
            "all_passed": all(c.get("passed") for c in checks) and bool(checks)}


__all__ = ["derive_metrics", "score_candidate"]
