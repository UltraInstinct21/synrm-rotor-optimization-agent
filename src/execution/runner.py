"""Experiment runner — high-level wrapper combining script execution, logging, and summarization."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from src.artifacts import ExperimentReport
from src.execution.experiment_logger import log_experiment_to_wiki
from src.execution.result_summarizer import report_to_summary, summarize_log


def _run_python_script(
    script_path: str | Path,
    args: list[str] | None = None,
    cwd: str | Path | None = None,
) -> ExperimentReport:
    """Execute a Python script and return an ExperimentReport."""
    cmd = [sys.executable, str(script_path)] + (args or [])
    try:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, timeout=300
        )
        report = ExperimentReport(
            experiment_id=f"run-{Path(script_path).stem}",
            workflow_name=str(script_path),
            result="success" if result.returncode == 0 else "failed",
            outputs={"files": [], "logs": [], "stdout": result.stdout, "stderr": result.stderr},
            metadata={"exit_code": result.returncode, "cwd": str(cwd)},
        )
        return report
    except subprocess.TimeoutExpired:
        return ExperimentReport(
            experiment_id=f"run-{Path(script_path).stem}",
            workflow_name=str(script_path),
            result="failed",
            metadata={"error": "timeout"},
        )
    except Exception as e:
        return ExperimentReport(
            experiment_id=f"run-{Path(script_path).stem}",
            workflow_name=str(script_path),
            result="failed",
            metadata={"error": str(e)},
        )


async def run_experiment(
    script_path: str | Path,
    args: list[str] | None = None,
    cwd: str | Path | None = None,
    log_to_wiki: bool = True,
) -> ExperimentReport:
    """Run a script, collect results, and optionally log to wiki.

    Parameters
    ----------
    script_path : str | Path
        Path to the script to execute.
    args : list[str], optional
        Command-line arguments.
    cwd : str | Path, optional
        Working directory.
    log_to_wiki : bool
        If True, write an experiment log page to workspace/wiki/motorcad/experiments/.

    Returns
    -------
    ExperimentReport
        Structured result with outputs, metrics, and wiki path if logged.
    """
    import asyncio

    report = await asyncio.get_event_loop().run_in_executor(
        None,
        lambda: _run_python_script(script_path, args=args, cwd=cwd),
    )

    # Parse metrics from logs.
    if report.outputs and report.outputs.get("files"):
        for log_file in report.outputs["files"]:
            metrics = summarize_log(log_file)
            if "exit_code" in metrics:
                exit_code = metrics.pop("exit_code")
                if exit_code != 0 and report.result == "success":
                    report.result = "failed"
            for k, v in metrics.items():
                if isinstance(v, (int, float)) and k in ("torque", "efficiency", "power_factor"):
                    report.key_metrics[k] = v

    # Log to wiki.
    if log_to_wiki:
        page_path = log_experiment_to_wiki(report)
        report.notes_for_wiki.append(f"Experiment logged: {page_path}")

    return report
