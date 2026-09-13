"""Geometry validation — single source of truth for parameter constraints.

Generated Motor-CAD scripts (and the agent) MUST validate candidates through
here BEFORE an expensive solve, instead of re-deriving asserts from prose.
"""

from __future__ import annotations

from src.motor.spec import MachineSpec, load_active_spec


def validate_parameters(params: dict, spec: MachineSpec | None = None,
                        spec_path: str = "") -> dict:
    """Validate a candidate parameter dict against the active spec.

    Returns {"ok": bool, "errors": [...], "warnings": [...]}.
    Errors: locked params touched, range/min/max/order violations.
    Warnings: unknown params (not in spec) — passed through, not rejected.
    """
    spec = spec or load_active_spec(spec_path)
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(params, dict) or not params:
        return {"ok": False, "errors": ["params must be a non-empty object"], "warnings": []}

    locked_set = set(spec.locked)
    for name, value in params.items():
        if name in locked_set:
            errors.append(f"'{name}' is LOCKED by the spec and must not vary")
            continue
        bounds = spec.params.get(name)
        if bounds is None:
            warnings.append(f"'{name}' is not in the spec; range unchecked")
            continue
        try:
            v = float(value)
        except (TypeError, ValueError):
            errors.append(f"'{name}' is not numeric: {value!r}")
            continue
        if v < bounds["min"] or v > bounds["max"]:
            errors.append(
                f"'{name}'={v} outside [{bounds['min']}, {bounds['max']}]"
                f"{' ' + bounds.get('unit', '') if bounds.get('unit') else ''}"
            )

    for rule in spec.minimums:
        name, minimum = rule.get("param"), rule.get("min")
        if name in params and name not in locked_set:
            try:
                if float(params[name]) < minimum:
                    errors.append(f"'{name}'={params[name]} below minimum {minimum} ({rule.get('reason', '')})".rstrip())
            except (TypeError, ValueError):
                pass

    for rule in spec.maximums:
        name, maximum = rule.get("param"), rule.get("max")
        if name in params and name not in locked_set:
            try:
                if float(params[name]) > maximum:
                    errors.append(f"'{name}'={params[name]} above maximum {maximum} ({rule.get('reason', '')})".rstrip())
            except (TypeError, ValueError):
                pass

    for chain in spec.order_chains:
        present = [p for p in chain if p in params]
        for lo, hi in zip(present, present[1:]):
            try:
                if not float(params[lo]) < float(params[hi]):
                    errors.append(f"ordering violated: '{lo}'={params[lo]} must be < '{hi}'={params[hi]}")
            except (TypeError, ValueError):
                pass

    return {"ok": not errors, "errors": errors, "warnings": warnings}


__all__ = ["validate_parameters"]
