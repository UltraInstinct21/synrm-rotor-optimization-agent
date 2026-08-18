"""Integration tests for run file creation and execution."""

import json
from src.tools.execution import create_run_file, execute_run_file, execute_generated_motorcad_code


def test_create_and_run_simulation_script():
    script_content = """
import sys

print("Initializing simulation run file...")
params = {"L1_Diameter": 105.0, "L2_Diameter": 130.0}
print(f"Set parameters: {params}")
print("Simulation run file execution completed successfully.")
"""
    create_res = create_run_file.invoke({
        "filename": "sim_test.py",
        "code_content": script_content,
    })
    c_data = json.loads(create_res)
    assert c_data["status"] == "success"

    exec_res = execute_run_file.invoke({"filename": "sim_test.py"})
    e_data = json.loads(exec_res)
    assert e_data["status"] == "success"
    assert "Simulation run file execution completed successfully." in e_data["stdout"]


def test_execute_generated_code_shortcut():
    code = 'print("Executing generated code shortcut")\n'
    res_raw = execute_generated_motorcad_code.invoke({"code_content": code})
    res = json.loads(res_raw)
    assert res["status"] == "success"
    assert "Executing generated code shortcut" in res["stdout"]
