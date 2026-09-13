"""Tests for the execution safety scan, mutex, budget breaker, and ledger hook."""

from __future__ import annotations

import json

import pytest

from src.tools import execution as ex


@pytest.fixture(autouse=True)
def _reset_budget():
    ex.reset_execution_budget()
    yield
    ex.reset_execution_budget()


CLEAN = '''
import ansys.motorcad.core as pymotorcad
mc = pymotorcad.MotorCAD()
mc.show_magnetic_context()
mc.set_variable("Shaft_Speed_[RPM]", 3000)
print("torque:", mc.get_variable("ShaftTorque"))
import os
os.environ.setdefault("MOTORCAD_INSTALL_DIR", "x")
print("subprocess")  # word in a string is fine
'''


def test_clean_script_passes_scan():
    assert ex.scan_code_safety(CLEAN) == []


def test_destructive_ops_blocked():
    assert ex.scan_code_safety("import shutil\nshutil.rmtree('/')")
    assert ex.scan_code_safety("import os\nos.remove('a')")
    assert ex.scan_code_safety("import os\nos.system('dir')")
    assert ex.scan_code_safety("x = os.popen('ls').read()")


def test_process_network_exec_blocked():
    assert ex.scan_code_safety("import subprocess\nsubprocess.run(['x'])")
    assert ex.scan_code_safety("from subprocess import Popen")
    assert ex.scan_code_safety("import socket\nsocket.create_connection(('h', 80))")
    assert ex.scan_code_safety("import urllib.request")
    assert ex.scan_code_safety("import requests\nrequests.get('http://x')")
    assert ex.scan_code_safety("y = eval(user_input)")
    assert ex.scan_code_safety("exec(code)")
    assert ex.scan_code_safety("f = __import__('os')")


def test_create_run_file_blocks_unsafe():
    res = json.loads(ex.create_run_file.invoke(
        {"filename": "evil_test.py", "code_content": "import shutil\nshutil.rmtree('.')"}))
    assert res["status"] == "error"
    assert "BLOCKED" in res["error"]


def test_execute_blocks_edited_unsafe_file():
    res = json.loads(ex.create_run_file.invoke(
        {"filename": "edit_me_test.py", "code_content": "print('ok')"}))
    assert res["status"] == "success"
    path = res["script_path"]
    try:
        from pathlib import Path

        Path(path).write_text("import os\nos.remove('x')\n", encoding="utf-8")
        out = json.loads(ex.execute_run_file.invoke({"filename": path}))
        assert out["status"] == "error"
        assert "BLOCKED" in out["error"]
    finally:
        from pathlib import Path

        Path(path).unlink(missing_ok=True)


def test_mutex_busy():
    res = json.loads(ex.create_run_file.invoke(
        {"filename": "busy_test.py", "code_content": "print('hi')"}))
    path = res["script_path"]
    try:
        assert ex._EXEC_LOCK.acquire(blocking=False)
        try:
            out = json.loads(ex.execute_run_file.invoke({"filename": path}))
            assert out["status"] == "busy"
        finally:
            ex._EXEC_LOCK.release()
    finally:
        from pathlib import Path

        Path(path).unlink(missing_ok=True)


def test_solve_budget_exhaustion(monkeypatch):
    monkeypatch.setenv("MOTORCAD_MAX_SOLVES", "1")
    assert ex._budget_consume(True) is None
    blocked = ex._budget_consume(True)
    assert blocked and "budget exhausted" in blocked


def test_circuit_breaker_trips(monkeypatch):
    monkeypatch.setenv("MOTORCAD_MAX_CONSECUTIVE_FAILURES", "2")
    ex._budget_record_outcome(False)
    ex._budget_record_outcome(False)
    blocked = ex._budget_consume(False)
    assert blocked and "Circuit breaker" in blocked
    ex.reset_execution_budget()
    assert ex._budget_consume(False) is None


def test_budget_status_shape():
    s = ex.get_budget_status()
    assert {"solves_used", "solves_limit", "solves_remaining",
            "consecutive_failures", "failure_limit"} <= set(s)


def test_ledger_hook_on_candidate_result(tmp_path, monkeypatch):
    monkeypatch.setenv("MOTOR_LEDGER_DIR", str(tmp_path))
    code = ('print(\'CANDIDATE_RESULT: {"params": {"L1_Diameter": 100}, '
            '"results": {"torque": 143.0, "input_power_w": 46500, '
            '"speed_rpm": 3000, "power_factor": 0.87, '
            '"output_power_kw": 44.9}}\')\n')
    res = json.loads(ex.create_run_file.invoke(
        {"filename": "ledger_test.py", "code_content": code}))
    out = json.loads(ex.execute_run_file.invoke({"filename": res["script_path"]}))
    assert out["status"] == "success"
    assert out.get("ledger", {}).get("logged") == 1
    assert out["ledger"].get("best_objective_this_run") is not None
    from src.motor.ledger import load_ledger

    rows = load_ledger("synrm_45kw", tmp_path)
    assert len(rows) == 1
    assert rows[0]["params"] == {"L1_Diameter": 100}
