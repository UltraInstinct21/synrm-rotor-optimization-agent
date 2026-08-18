"""Tests for sandboxed code execution tool."""

import json
from src.tools.execution import execute_generated_motorcad_code


def test_execute_generated_code_success():
    code = 'print("Hello from Sandboxed Execution!")\n'
    res_raw = execute_generated_motorcad_code.invoke({"code_content": code})
    res = json.loads(res_raw)
    assert res["status"] == "success"
    assert res["exit_code"] == 0
    assert "Hello from Sandboxed Execution!" in res["stdout"]


def test_execute_generated_code_error():
    code = 'raise ValueError("Simulated Motor-CAD error")\n'
    res_raw = execute_generated_motorcad_code.invoke({"code_content": code})
    res = json.loads(res_raw)
    assert res["status"] == "failed"
    assert res["exit_code"] != 0
    assert "ValueError: Simulated Motor-CAD error" in res["stderr"]
