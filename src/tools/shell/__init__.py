"""Shell execution tool for the agent — sandboxed inside project root."""

from __future__ import annotations

import subprocess
from pathlib import Path

from agents import function_tool, RunContextWrapper

from src.config import settings


@function_tool
async def run_shell(
    ctx: RunContextWrapper,
    command: str,
    timeout: int = 30,
    workdir: str = "",
) -> str:
    """Execute a shell command inside the project root.

    Use for running scripts, git commands, and build tools.
    Only allows commands that don't escape the project root.

    Args:
        command: Shell command to run.
        timeout: Max execution time in seconds (default 30, max 120).
        workdir: Relative work directory inside the project (default: project root).

    Returns:
        stdout and stderr of the command.
    """
    cwd = Path(settings.PROJECT_ROOT)
    if workdir:
        cwd = (cwd / workdir).resolve()
        if not str(cwd).startswith(str(settings.PROJECT_ROOT.resolve())):
            return "Error: workdir escapes project root."

    safe_timeout = min(max(timeout, 1), 120)

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=str(cwd),
            timeout=safe_timeout,
        )
    except subprocess.TimeoutExpired:
        return f"Command timed out after {safe_timeout}s."
    except Exception as exc:
        return f"Command error: {exc}"

    output = result.stdout or ""
    if result.stderr:
        output += f"\n(stderr)\n{result.stderr}"
    if not output.strip():
        output = f"Exit code: {result.returncode} (no output)"
    return output.strip()[:5000]
