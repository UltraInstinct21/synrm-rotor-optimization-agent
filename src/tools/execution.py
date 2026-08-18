"""Run Files & Execution Tools — allows Deep Agents to create and run Python scripts with PyMotorCAD."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import uuid
from pathlib import Path

from langchain_core.tools import tool

SCRATCH_DIR = Path("D:/SRM/Agent/workspace/scratch")

def _resolve_safe_path(filename: str) -> Path:
    """Resolve script path safely, ensuring it is within SCRATCH_DIR."""
    clean_path = Path(filename.strip())
    if clean_path.is_absolute():
        # Allow absolute paths only if they resolve within SCRATCH_DIR
        target = clean_path.resolve()
    else:
        target = (SCRATCH_DIR / clean_path).resolve()
    scratch_resolved = SCRATCH_DIR.resolve()
    if scratch_resolved not in target.parents and target != scratch_resolved:
        raise ValueError(f"Path must stay within {SCRATCH_DIR}. Got: {target}")
    return target


def _diagnose_execution_error(stderr: str) -> str:
    """Extract helpful diagnostic hints from subprocess stderr."""
    hints = []
    if "ModuleNotFoundError" in stderr and "ansys.motorcad" in stderr:
        hints.append("PyMotorCAD package is missing. Ensure ansys-motorcad-core is installed.")
    if "SyntaxError" in stderr:
        hints.append("Python script contains a syntax error.")
    if "MotorCAD" in stderr and ("Licence" in stderr or "license" in stderr.lower()):
        hints.append("Motor-CAD license unavailable or license seats exhausted.")
    if "FileNotFoundError" in stderr:
        hints.append("Referenced .mot model or file not found.")

    return (" Hints: " + " ".join(hints)) if hints else ""


def _sanitize_code_content(code: str) -> str:
    """Sanitize generated Python code to fix common Windows string escaping syntax errors."""
    import re
    pattern = r'r(["\'])([^"\']*?\\)\1'
    def fix_raw_string(match: re.Match) -> str:
        quote = match.group(1)
        content = match.group(2)
        if content.endswith('\\'):
            content = content[:-1] + '/'
        return f'r{quote}{content}{quote}'

    return re.sub(pattern, fix_raw_string, code)


@tool
def create_run_file(
    filename: str,
    code_content: str,
) -> str:
    """Create or overwrite a Python run file with PyMotorCAD simulation script code.

    Args:
        filename: Name or relative path for the script (e.g. 'run_sim.py' or 'sweeps/sweep_l1.py').
        code_content: Complete Python source code using PyMotorCAD (ansys.motorcad.core) to run simulations.

    Returns:
        JSON string indicating status, created script path, and code line count.
    """
    if not filename or not filename.strip():
        return json.dumps({"status": "error", "error": "Filename parameter cannot be empty."})

    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    target_path = _resolve_safe_path(filename)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    project_root = str(Path(__file__).resolve().parents[2])

    code_content = _sanitize_code_content(code_content)

    # Prepend project root to sys.path if not already present
    header = f"""# Auto-generated Run File ({target_path.name})
import sys
import os
if r"{project_root}" not in sys.path:
    sys.path.insert(0, r"{project_root}")

"""
    full_code = header + code_content if "sys.path" not in code_content else code_content

    try:
        target_path.write_text(full_code, encoding="utf-8")
        line_count = len(full_code.splitlines())
        return json.dumps({
            "status": "success",
            "message": f"Run file created successfully at {target_path}",
            "script_path": str(target_path),
            "line_count": line_count,
        }, indent=2)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Failed to write run file: {e}",
            "script_path": str(target_path),
        }, indent=2)


@tool
def execute_run_file(
    filename: str,
    timeout_seconds: int = 300,
) -> str:
    """Execute a Python run file in a sandboxed subprocess and return stdout/stderr results.

    Args:
        filename: Name or path of the Python script to execute.
        timeout_seconds: Maximum execution time in seconds (default 300).

    Returns:
        JSON string with execution outcome (status, exit_code, stdout, stderr, script_path).
    """
    if not filename or not filename.strip():
        return json.dumps({"status": "error", "error": "Filename parameter cannot be empty."})

    target_path = _resolve_safe_path(filename)

    if not target_path.exists():
        return json.dumps({
            "status": "error",
            "error": f"Run file not found at {target_path}",
            "script_path": str(target_path),
        }, indent=2)

    timeout_seconds = max(1, min(int(timeout_seconds), 3600))
    cmd = [sys.executable, str(target_path)]
    env = os.environ.copy()

    try:
        process = subprocess.run(
            cmd,
            cwd=str(target_path.parent),
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            env=env,
        )

        stdout = process.stdout or ""
        stderr = process.stderr or ""
        success = process.returncode == 0
        diag = _diagnose_execution_error(stderr) if not success else ""

        return json.dumps({
            "status": "success" if success else "failed",
            "exit_code": process.returncode,
            "stdout": stdout[-3000:] if len(stdout) > 3000 else stdout,
            "stderr": (stderr[-3000:] if len(stderr) > 3000 else stderr) + diag,
            "script_path": str(target_path),
        }, indent=2)
    except subprocess.TimeoutExpired:
        return json.dumps({
            "status": "timeout",
            "error": f"Execution timed out after {timeout_seconds} seconds.",
            "script_path": str(target_path),
        }, indent=2)
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Subprocess execution failed: {e}",
            "script_path": str(target_path),
        }, indent=2)


@tool
def execute_generated_motorcad_code(
    code_content: str,
    timeout_seconds: int = 300,
) -> str:
    """Create and execute LLM-generated Python simulation code in an isolated subprocess sandbox.

    Args:
        code_content: The complete Python source code string to execute.
        timeout_seconds: Maximum runtime allowed before timing out (default 300s).

    Returns:
        JSON string with execution outcome (status, exit_code, stdout, stderr, script_path).
    """
    if not code_content or not code_content.strip():
        return json.dumps({
            "status": "error",
            "error": "code_content parameter cannot be empty.",
        }, indent=2)

    try:
        run_id = f"sim_{uuid.uuid4().hex[:8]}"
        create_res = create_run_file.invoke({"filename": f"{run_id}.py", "code_content": code_content})
        create_data = json.loads(create_res)
        if create_data.get("status") == "error":
            return create_res

        script_path = create_data["script_path"]
        try:
            return execute_run_file.invoke({"filename": script_path, "timeout_seconds": timeout_seconds})
        finally:
            try:
                Path(script_path).unlink(missing_ok=True)
            except Exception:
                pass
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Failed to execute generated Motor-CAD code: {e}",
        }, indent=2)


__all__ = [
    "create_run_file",
    "execute_run_file",
    "execute_generated_motorcad_code",
]
