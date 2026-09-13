"""Tests for geometry validation against the spec."""

from __future__ import annotations

import json

from src.motor.spec import load_active_spec
from src.motor.validate import validate_parameters
from src.tools.motor import validate_motor_params


def _spec():
    return load_active_spec()


def test_valid_candidate_passes():
    r = validate_parameters(
        {"L1_Diameter": 100, "L2_Diameter": 130, "L3_Diameter": 160,
         "L1_Bridge_Thickness": 4}, _spec())
    assert r["ok"] and not r["errors"]


def test_range_violation():
    r = validate_parameters({"L1_Diameter": 200}, _spec())
    assert not r["ok"]
    assert any("L1_Diameter" in e for e in r["errors"])


def test_ordering_violation():
    r = validate_parameters({"L1_Diameter": 140, "L2_Diameter": 130}, _spec())
    assert not r["ok"]
    assert any("ordering" in e for e in r["errors"])


def test_bridge_minimum():
    r = validate_parameters({"L1_Bridge_Thickness": 0.5}, _spec())
    assert not r["ok"]


def test_rotor_od_maximum():
    r = validate_parameters({"L3_Diameter": 220}, _spec())
    assert not r["ok"]


def test_locked_param_rejected():
    r = validate_parameters({"Slot_Number": 48}, _spec())
    assert not r["ok"]
    assert any("LOCKED" in e for e in r["errors"])


def test_unknown_param_warns_only():
    r = validate_parameters({"SomeFuture_Param": 1.5}, _spec())
    assert r["ok"]
    assert r["warnings"]


def test_empty_params():
    assert not validate_parameters({}, _spec())["ok"]


def test_tool_wrapper_ok():
    import json as j

    out = j.loads(validate_motor_params.invoke({
        "params_json": j.dumps({"L1_Diameter": 100, "L2_Diameter": 130})}))
    assert out["status"] == "ok"
    assert out["spec"] == "45kW SynRM rotor optimization"


def test_tool_wrapper_bad_json():
    import json as j

    out = j.loads(validate_motor_params.invoke({"params_json": "{bad"}))
    assert out["status"] == "error"


def test_tool_wrapper_violation():
    import json as j

    out = j.loads(validate_motor_params.invoke({
        "params_json": j.dumps({"L1_Diameter": 140, "L2_Diameter": 130})}))
    assert out["status"] == "error"
    assert out["errors"]
