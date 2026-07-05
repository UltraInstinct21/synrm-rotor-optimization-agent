"""Execution layer — run scripts and capture structured results."""

from __future__ import annotations

import subprocess
import tempfile
import uuid
from pathlib import Path

from src.artifacts.experiment_report import ExperimentReport
from src.config import settings


def run_python_script(
    script_path: str | Path,
    args: list[str] | None = None,
    cwd: str | Path | None = None,
    timeout: int = 300,
) -> ExperimentReport:
    """Run a Python script and capture outputs.

    Parameters
    ----------
    script_path : str | Path
        Path to the .py file to execute.
    args : list[str], optional
        Command-line arguments to pass.
    cwd : str | Path, optional
        Working directory.  Defaults to the script's parent.
    timeout : int
        Kill after this many seconds (default 300).

    Returns
    -------
    ExperimentReport
        Structured result with logs, exit code, and output files.
    """
    script_path = Path(script_path)
    cwd = Path(cwd) if cwd else script_path.parent
    args = args or []

    experiment_id = f"run_{uuid.uuid4().hex[:8]}"
    log_file = settings.EXPERIMENTS_ROOT / f"{experiment_id}.log"
    settings.EXPERIMENTS_ROOT.mkdir(parents=True, exist_ok=True)

    cmd = ["python", str(script_path)] + args

    try:
        result = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        return ExperimentReport(
            experiment_id=experiment_id,
            workflow_name=script_path.name,
            result="failed",
            outputs={
                "files": [],
                "logs": [f"TIMEOUT after {timeout}s"],
                "stdout": e.stdout or "",
                "stderr": e.stderr or "",
            },
        )

    # Write log file.
    log_content = f"EXIT_CODE: {result.returncode}\n"
    log_content += f"STDOUT:\n{result.stdout}\n"
    log_content += f"STDERR:\n{result.stderr}\n"
    log_file.write_text(log_content, encoding="utf-8")

    return ExperimentReport(
        experiment_id=experiment_id,
        workflow_name=script_path.name,
        inputs={
            "parameters": {"args": args, "timeout": timeout},
            "config_files": [str(script_path)],
            "notes": "",
        },
        outputs={
            "files": [str(log_file)],
            "logs": [log_content],
        },
        result="success" if result.returncode == 0 else "failed",
        notes_for_wiki=[
            f"Experiment {experiment_id}: {script_path.name} "
            f"exited with code {result.returncode}"
        ],
    )
