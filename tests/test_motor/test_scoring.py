"""Tests for spec compliance scoring."""

from __future__ import annotations

import json

from src.motor.scoring import derive_metrics, score_candidate
from src.motor.spec import load_active_spec
from src.tools.motor import score_motor_result


def _perfect():
    # 143 Nm @ 3000 RPM, 96.5% eff, PF 0.87
    shaft_kw = 143.0 * 3000 * 2 * 3.1415926535 / 60 / 1000
    return {"torque": 143.0, "input_power_w": shaft_kw * 1000 / 0.965,
            "speed_rpm": 3000, "power_factor": 0.87}


def test_perfect_candidate_passes():
    out = score_candidate(_perfect(), load_active_spec())
    assert out["all_passed"], out["checks"]
    assert out["objective"] < 5.0


def test_torque_miss_fails_and_scores_worse():
    good = score_candidate(_perfect(), load_active_spec())
    bad = score_candidate({**_perfect(), "torque": 120.0}, load_active_spec())
    assert not bad["all_passed"]
    assert bad["objective"] > good["objective"]
    torque_check = next(c for c in bad["checks"] if c["key"] == "torque")
    assert torque_check["passed"] is False


def test_efficiency_below_min_fails():
    out = score_candidate({**_perfect(), "input_power_w": 60000.0}, load_active_spec())
    eff = next(c for c in out["checks"] if c["key"] == "efficiency_pct")
    assert eff["passed"] is False


def test_missing_target_penalized():
    out = score_candidate({"torque": 143.0}, load_active_spec())
    assert not out["all_passed"]
    missing = [c for c in out["checks"] if c.get("reason") == "not reported"]
    assert missing


def test_derive_metrics_math():
    m = derive_metrics({"torque": 143.0, "input_power_w": 46500.0}, 3000)
    assert abs(m["output_power_kw"] - 44.93) < 0.05
    assert abs(m["efficiency_pct"] - 44.93 / 46.5 * 100) < 0.05


def test_tool_wrapper():
    out = json.loads(score_motor_result.invoke({"results_json": json.dumps(_perfect())}))
    assert out["all_passed"]
    assert "objective" in out
