"""Motor-design tools — validate candidates BEFORE solves, score AFTER solves.

Both tools resolve the active project spec ($MOTOR_PROJECT >
projects/active.json > legacy specs/active.json > example template).
They are machine-agnostic: new projects only need a new project folder
(workspace/projects/<slug>/spec.json), no code changes.
"""

from __future__ import annotations

import json

from langchain_core.tools import tool


@tool
def validate_motor_params(params_json: str, spec_path: str = "") -> str:
    """Validate a candidate geometry dict against the active machine spec.

    Call this BEFORE every Motor-CAD solve — it is cheaper than a 90 s FEA
    run on rejected geometry. Single source of truth for ranges, ordering
    (e.g. L1<L2<L3), minima, and locked params; never re-derive asserts.

    Args:
        params_json: JSON object of {param_name: value}, e.g.
            '{"L1_Diameter": 100, "L2_Diameter": 130, "L3_Diameter": 160}'.
        spec_path: Optional explicit spec file. Empty = active spec.

    Returns:
        JSON {status ok|error, errors[], warnings[], spec}.
    """
    from src.motor.spec import load_active_spec
    from src.motor.validate import validate_parameters

    try:
        params = json.loads(params_json) if isinstance(params_json, str) else params_json
    except (json.JSONDecodeError, TypeError) as e:
        return json.dumps({"status": "error", "error": f"params_json is not valid JSON: {e}"}, indent=2)
    try:
        spec = load_active_spec(spec_path)
    except Exception as e:
        return json.dumps({"status": "error", "error": f"Cannot load machine spec: {e}"}, indent=2)
    result = validate_parameters(params if isinstance(params, dict) else {}, spec)
    result["status"] = "ok" if result["ok"] else "error"
    result["spec"] = spec.project
    return json.dumps(result, indent=2)


@tool
def score_motor_result(results_json: str, spec_path: str = "") -> str:
    """Score solve results against spec targets (computed pass/fail).

    Call this AFTER every solve instead of eyeballing numbers. Derives shaft
    power/efficiency from torque + input power + speed when possible.

    Args:
        results_json: JSON object, e.g. '{"torque": 143.2,
            "input_power_w": 46800, "speed_rpm": 3000, "power_factor": 0.87}'.
            Missing targets are reported missing/failed.
        spec_path: Optional explicit spec file. Empty = active spec.

    Returns:
        JSON {objective (lower better), checks[{key,label,value,target,min,
        passed}], all_passed, spec}.
    """
    from src.motor.scoring import score_candidate
    from src.motor.spec import load_active_spec

    try:
        results = json.loads(results_json) if isinstance(results_json, str) else results_json
    except (json.JSONDecodeError, TypeError) as e:
        return json.dumps({"status": "error", "error": f"results_json is not valid JSON: {e}"}, indent=2)
    try:
        spec = load_active_spec(spec_path)
    except Exception as e:
        return json.dumps({"status": "error", "error": f"Cannot load machine spec: {e}"}, indent=2)
    out = score_candidate(results if isinstance(results, dict) else {}, spec)
    out["spec"] = spec.project
    return json.dumps(out, indent=2)


__all__ = ["score_motor_result", "validate_motor_params"]
