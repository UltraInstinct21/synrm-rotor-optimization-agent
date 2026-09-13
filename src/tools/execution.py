"""Run Files & Execution Tools — allows Deep Agents to create and run Python scripts with PyMotorCAD.

Workflow contract (read before calling):
- Motor-CAD runs as a SINGLE shared instance: execution is MUTEX-guarded, so a
  second overlapping call fails fast with status "busy" — wait for the running
  call, then retry. NEVER issue execution calls in parallel in one turn.
- Every script is SAFETY-SCANNED before it runs. Banned in generated code:
  destructive filesystem ops (shutil.rmtree/remove, os.remove/unlink/rmdir/...),
  process spawning (subprocess, os.system/popen/...), network/exfiltration
  (socket, urllib, requests, http.client), dynamic code exec (eval/exec,
  __import__). File writes belong in the active project's scratch/ and
  models/ folders, workspace/experiments, or model (.mot) backup paths only.
  Deleting ANY file must go through the HITL-gated `delete_file` tool —
  never from generated code.
- SOLVE BUDGET: scripts calling mc.do_magnetic_calculation() consume the
  per-session solve budget ($MOTORCAD_MAX_SOLVES, default 200). N consecutive
  failures (any execution, default 8) trip the circuit breaker — fix the root
  cause, then `/budget reset`. Inspect via /budget.
- LEDGER: print one `CANDIDATE_RESULT: {"params": {...}, "results": {...}}`
  line per evaluated candidate; the wrapper auto-logs it to
  workspace/experiments/<project>/ledger.jsonl and auto-scores it.
- A full FEA solve (``mc.do_magnetic_calculation()``) takes ~45-90 s. Pass
  ``timeout_seconds>=600`` for any script that solves; use the 60 s floor only
  for inspection / parameter-read scripts that do NOT solve.
- Do NOT solve in exploratory scripts. If you only need to read parameter
  values or model properties, do not call ``do_magnetic_calculation()``.
- Generated scripts MUST define ``safe_get``/``safe_set`` wrappers, call
  ``mc.show_magnetic_context()`` before any EMag method, validate candidates
  with ``validate_motor_params`` BEFORE solving, score with
  ``score_motor_result`` AFTER solving, save a checkpoint before mutating
  geometry, and read ALL result variables immediately after the solve and
  BEFORE mutating geometry for the next candidate.
- Prefer the 1-turn shortcut ``execute_generated_motorcad_code`` for a single
  attempt. For multi-step sweeps, use named files: ``create_run_file`` once,
  then ``edit_file`` + ``execute_run_file`` to iterate without regenerating.
  Sweep sampling must use seeded `src.motor.sweep` helpers (latin_hypercube,
  neighbors, has_converged) — never improvised RNG.
"""

from __future__ import annotations

import io
import json
import os
import re
import subprocess
import sys
import threading
import time
import tokenize
import uuid
from pathlib import Path

from langchain_core.tools import tool

# Resolve scratch dir from the project layout instead of a hardcoded drive
# letter so checkouts at other paths keep working. Falls back to the legacy
# absolute path only if settings import fails (e.g. docs builds).
try:
    from src.config.settings import WORKSPACE_ROOT as _WORKSPACE_ROOT

    SCRATCH_DIR = _WORKSPACE_ROOT / "scratch"
except Exception:  # pragma: no cover - import-time fallback
    SCRATCH_DIR = Path("D:/SRM/Agent/workspace/scratch")


def _default_scratch_dir() -> Path:
    """Active project's scratch/ when a project is selected, else legacy scratch."""
    try:
        from src.config.projects import active_scratch_dir

        d = active_scratch_dir()
        if d is not None:
            return d
    except Exception:
        pass
    return SCRATCH_DIR


def _allowed_write_roots() -> list[Path]:
    """Roots generated scripts may write to (resolved, best-effort)."""
    roots: list[Path] = []
    try:
        from src.config.projects import active_project_dir

        d = active_project_dir()
        if d is not None:
            roots.append(d)
    except Exception:
        pass
    roots.append(SCRATCH_DIR)
    try:
        from src.config.settings import WORKSPACE_ROOT as _WS

        roots += [_WS / "experiments", _WS / "projects", _WS / "scratch"]
    except Exception:
        pass
    uniq: list[Path] = []
    for r in roots:
        try:
            rr = r.resolve()
        except Exception:
            continue
        if rr not in uniq:
            uniq.append(rr)
    return uniq

# Guardrails: keep subprocess payloads inside the agent context window and
# prevent runaway scripts from hanging the Motor-CAD licence seat.
_MAX_CODE_CHARS = 200_000
_MIN_TIMEOUT = 60
_MAX_TIMEOUT = 3600
_STDOUT_TAIL = 4000
_STDOUT_HEAD = 1000

# ── Mutual exclusion: Motor-CAD is a single shared instance ─────────────
# SAFE/SERIAL CONTRACT (P1 queued execution):
# - PARALLEL-SAFE tools (pure / read-only, no shared-instance mutation) may run
#   concurrently: TOOL_PARALLEL_SAFE.
# - SERIAL tools (mutate files or drive the single Motor-CAD instance) MUST run
#   one-at-a-time and MUST NEVER be parallelized in a single turn: TOOL_SERIAL.
# - execute_run_file / execute_generated_motorcad_code hold _EXEC_LOCK for the
#   whole subprocess solve, so the single-instance invariant always holds
#   (never two solves concurrently). Contended callers queue-wait (poll) then
#   get status "busy" with retry_after_s instead of fail-fast.
TOOL_PARALLEL_SAFE = frozenset({
    "validate_motor_params",
    "score_motor_result",
    "wiki_tool",
    "read_file",
    "glob",
    "grep",
    "research_subgraph",
})
TOOL_SERIAL = frozenset({
    "create_run_file",
    "execute_run_file",
    "execute_generated_motorcad_code",
    "edit_file",
    "delete_file",
})
_EXEC_LOCK = threading.Lock()

# ── Lightweight execution metrics (P1 measurement, process-local) ─────────
_TOOL_METRICS = {"calls": 0, "total_duration_ms": 0, "busy_count": 0}
_METRICS_LOCK = threading.Lock()
_EXEC_WAIT_TIMEOUT_S = 30
_EXEC_WAIT_POLL_S = 1
_BUSY_RETRY_AFTER_S = 5


def _metrics_record_call(duration_ms: int) -> None:
    """Record one completed subprocess execution (thread-safe)."""
    try:
        with _METRICS_LOCK:
            _TOOL_METRICS["calls"] += 1
            _TOOL_METRICS["total_duration_ms"] += int(duration_ms)
    except Exception:
        pass


def _metrics_record_busy() -> None:
    """Record one queued-wait exhaustion (still locked after wait)."""
    try:
        with _METRICS_LOCK:
            _TOOL_METRICS["busy_count"] += 1
    except Exception:
        pass


def get_execution_metrics() -> dict:
    """Return lightweight execution metrics (process-local).

    Returns:
        dict with keys: calls, total_duration_ms, avg_duration_ms, busy_count.
    """
    with _METRICS_LOCK:
        calls = int(_TOOL_METRICS.get("calls", 0))
        total = int(_TOOL_METRICS.get("total_duration_ms", 0))
        busy = int(_TOOL_METRICS.get("busy_count", 0))
    avg = (total / calls) if calls else 0
    return {
        "calls": calls,
        "total_duration_ms": total,
        "avg_duration_ms": avg,
        "busy_count": busy,
    }

# ── Solve budget / circuit breaker (per process) ────────────────────────
# RLock (re-entrant): reset paths hold the lock while reading status.
_BUDGET_LOCK = threading.RLock()
_solves_used = 0
_consecutive_failures = 0


def _max_solves() -> int:
    try:
        return max(1, int(os.getenv("MOTORCAD_MAX_SOLVES", "200")))
    except (TypeError, ValueError):
        return 200


def _max_consecutive_failures() -> int:
    try:
        return max(1, int(os.getenv("MOTORCAD_MAX_CONSECUTIVE_FAILURES", "8")))
    except (TypeError, ValueError):
        return 8


def _is_solve_code(code: str) -> bool:
    return "do_magnetic_calculation" in code


def get_budget_status() -> dict:
    """Return current solve budget / breaker state (used by /budget)."""
    with _BUDGET_LOCK:
        return {
            "solves_used": _solves_used,
            "solves_limit": _max_solves(),
            "solves_remaining": max(0, _max_solves() - _solves_used),
            "consecutive_failures": _consecutive_failures,
            "failure_limit": _max_consecutive_failures(),
        }


def reset_execution_budget() -> dict:
    """Reset solve + failure counters (used by `/budget reset`)."""
    global _solves_used, _consecutive_failures
    with _BUDGET_LOCK:
        _solves_used = 0
        _consecutive_failures = 0
        return get_budget_status()


def _budget_consume(is_solve: bool) -> str | None:
    """Check limits and consume one solve. Returns an error string or None."""
    global _solves_used
    with _BUDGET_LOCK:
        if _consecutive_failures >= _max_consecutive_failures():
            return (
                f"Circuit breaker tripped after {_consecutive_failures} consecutive failures "
                f"(limit {_max_consecutive_failures()}). Fix the root cause (read the last "
                f"stderr), then run `/budget reset` to continue."
            )
        if is_solve:
            if _solves_used >= _max_solves():
                return (
                    f"Solve budget exhausted ({_solves_used}/{_max_solves()}). "
                    f"Review the ledger best-so-far, then raise $MOTORCAD_MAX_SOLVES "
                    f"or run `/budget reset` to continue."
                )
            _solves_used += 1
    return None


def _budget_record_outcome(success: bool) -> None:
    global _consecutive_failures
    with _BUDGET_LOCK:
        _consecutive_failures = 0 if success else _consecutive_failures + 1


# ── Safety scan: static denylist over code (strings/comments stripped) ──
_SAFETY_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\bshutil\s*\.\s*(rmtree|remove|move|chown)\b"),
     "destructive filesystem op via shutil"),
    (re.compile(r"\bimport\s+shutil\b"), "importing shutil"),
    (re.compile(r"\bfrom\s+shutil\s+import\b"), "importing from shutil"),
    (re.compile(r"\bos\s*\.\s*(remove|unlink|rmdir|removedirs|rename|replace|system|popen|execl\w*|execv\w*|spawnl\w*|spawnv\w*|startfile|kill)\b"),
     "destructive/shell op via os"),
    (re.compile(r"\bsubprocess\b"), "process spawning via subprocess"),
    (re.compile(r"\bfrom\s+subprocess\s+import\b"), "importing from subprocess"),
    (re.compile(r"\bsocket\b"), "network access via socket"),
    (re.compile(r"\burllib\b"), "network access via urllib"),
    (re.compile(r"\brequests\b"), "network access via requests"),
    (re.compile(r"\bhttp\s*\.\s*client\b"), "network access via http.client"),
    (re.compile(r"\bftplib\b"), "network access via ftplib"),
    (re.compile(r"\beval\s*\("), "dynamic code exec via eval"),
    (re.compile(r"\bexec\s*\("), "dynamic code exec via exec"),
    (re.compile(r"__import__\s*\("), "dynamic import via __import__"),
]


def _strip_strings_and_comments(code: str) -> str:
    """Remove string literals and comments so the scan can't be fooled by them
    (and legit text mentioning banned words isn't flagged). Falls back to raw
    code when tokenization fails."""
    try:
        out: list[str] = []
        prev_end = (1, 0)
        tokens = tokenize.generate_tokens(io.StringIO(code).readline)
        for tok in tokens:
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            (srow, scol) = tok.start
            (prow, pcol) = prev_end
            if srow > prow:
                out.append("\n" * (srow - prow))
                out.append(" " * scol)
            else:
                out.append(" " * max(0, scol - pcol))
            out.append(tok.string)
            prev_end = tok.end
        return "".join(out)
    except (tokenize.TokenError, SyntaxError, IndentationError):
        return code


def scan_code_safety(code: str) -> list[str]:
    """Return a list of safety findings (empty = clean). Never raises."""
    try:
        stripped = _strip_strings_and_comments(code or "")
    except Exception:
        stripped = code or ""
    return [reason for pattern, reason in _SAFETY_PATTERNS if pattern.search(stripped)]


def _safety_error(findings: list[str]) -> str:
    return (
        "Execution BLOCKED by safety scan: "
        + "; ".join(findings)
        + ". Motor-CAD scripts may only compute, drive Motor-CAD, and write to "
        + "the active project's scratch/ and models/ folders, workspace/experiments, or model (.mot) backup paths. "
        + "Remove the flagged calls and retry."
    )


def _execution_approval_enabled() -> bool:
    return os.getenv("MOTORCAD_REQUIRE_APPROVAL", "").lower() in ("1", "true", "yes", "on")


def _request_execution_approval(script_path: str, is_solve: bool) -> bool | None:
    """Ask for HITL approval. True/False, or None when no console exists."""
    try:
        from apps.cli.theme import get_console
        from apps.cli.display import request_hitl_approval

        return request_hitl_approval(
            console=get_console(),
            tool_name="execute_run_file",
            details={"script": script_path, "solve": str(is_solve)},
        )
    except Exception:
        return None


_CANDIDATE_RE = re.compile(r"^CANDIDATE_RESULT:\s*(\{.*\})\s*$", re.M)


def _ledger_hook(stdout: str, script_path: str, status: str) -> dict | None:
    """Auto-log CANDIDATE_RESULT lines to the experiment ledger (best-effort).

    Returns a ledger summary dict when markers were present, else None. Never
    raises — ledger failures must not fail the execution result.
    """
    try:
        matches = _CANDIDATE_RE.findall(stdout or "")
        if not matches:
            return None
        from src.motor.ledger import log_candidate
        from src.motor.scoring import score_candidate
        from src.motor.spec import load_active_spec

        try:
            spec = load_active_spec()
            project = spec.project
            slug = spec.slug
        except Exception:
            spec, project, slug = None, "unknown", "default"
        logged = 0
        objectives: list[float] = []
        last_path = ""
        for raw in matches:
            try:
                entry = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if not isinstance(entry, dict):
                continue
            entry.setdefault("script_path", script_path)
            entry.setdefault("status", status)
            params, results = entry.get("params"), entry.get("results")
            if spec is not None and isinstance(params, dict) and isinstance(results, dict):
                try:
                    scored = score_candidate(results, spec)
                    entry["objective"] = scored["objective"]
                    entry["all_passed"] = scored["all_passed"]
                    objectives.append(scored["objective"])
                except Exception:
                    pass
            try:
                last_path = str(log_candidate(entry, project_slug=slug))
                logged += 1
            except Exception:
                continue
        if not logged:
            return {"logged": 0, "reason": "no parseable CANDIDATE_RESULT payloads"}
        summary: dict = {"logged": logged, "project": project, "ledger_path": last_path}
        if objectives:
            summary["best_objective_this_run"] = min(objectives)
        return summary
    except Exception as e:
        return {"logged": 0, "reason": f"ledger hook failed: {e}"}

def _resolve_safe_path(filename: str) -> Path:
    """Resolve a script path safely inside the allowed write roots.

    Relative names resolve against the ACTIVE PROJECT's scratch/
    (fallback legacy workspace/scratch). Absolute paths are accepted when
    they resolve inside any of `_allowed_write_roots()`, or — for model
    (.mot) backups — anywhere inside the workspace root. Anything else
    raises ValueError naming the allowed roots.
    """
    clean_path = Path(filename.strip())
    if clean_path.is_absolute():
        target = clean_path.resolve()
    else:
        target = (_default_scratch_dir() / clean_path).resolve()
    allowed = _allowed_write_roots()
    for root in allowed:
        try:
            root_resolved = root.resolve()
        except Exception:
            continue
        if target == root_resolved or root_resolved in target.parents:
            return target
    # Model (.mot) backups may live anywhere under the workspace root
    # (e.g. the active project's models/ folder).
    if target.suffix.lower() == ".mot":
        try:
            from src.config.settings import WORKSPACE_ROOT as _WS

            ws_resolved = _WS.resolve()
            if target == ws_resolved or ws_resolved in target.parents:
                return target
        except Exception:
            pass
    raise ValueError(
        f"Path must stay within one of {[str(r) for r in allowed]} "
        f"(or a .mot model backup inside the workspace root). Got: {target}"
    )


def _diagnose_execution_error(stderr: str) -> str:
    """Extract helpful diagnostic hints from subprocess stderr."""
    hints = []
    if "ModuleNotFoundError" in stderr and "ansys.motorcad" in stderr:
        hints.append("PyMotorCAD package is missing. Ensure ansys-motorcad-core is installed (pip install -e \".[motorcad]\").")
    if "SyntaxError" in stderr:
        hints.append("Python script contains a syntax error. Prefer edit_file to patch the persisted script, then rerun via execute_run_file.")
    if "MotorCAD" in stderr and ("Licence" in stderr or "license" in stderr.lower()):
        hints.append("Motor-CAD license unavailable or license seats exhausted. Wait and retry; do not launch parallel solves.")
    if "FileNotFoundError" in stderr:
        hints.append("Referenced .mot model or file not found. Verify the active project's models/ path (/project show) before solving.")
    if "TimeoutExpired" in stderr or "timed out" in stderr.lower():
        hints.append("Solve exceeded timeout. Re-run with a larger timeout_seconds (up to 3600) for FEA solves.")
    if "get_variable" in stderr or "set_variable" in stderr:
        hints.append("Unknown Motor-CAD variable string. Search workspace/wiki/motorcad/parameter_database via wiki_tool before retrying — never guess names.")

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
    """Create or overwrite a NAMED persistent Python run file for multi-step Motor-CAD work.

    Use this (instead of the 1-turn shortcut) when you will iterate: sweeps,
    Phase-1/Phase-2 optimization, or any script you intend to patch with
    `edit_file` and rerun with `execute_run_file`.

    The script MUST follow the Motor-CAD contract: search
    `workspace/wiki/motorcad/parameter_database` for unverified variable names
    first, define safe_get/safe_set helpers, call
    `mc.show_magnetic_context()` before any EMag solve, save a checkpoint
    before mutating geometry, and read all results before the next mutation.

    Args:
        filename: Name or relative path inside the ACTIVE PROJECT's scratch/
            (fallback legacy workspace/scratch) (e.g. 'run_sim.py' or
            'sweeps/sweep_l1.py'). Absolute paths are accepted only if they
            resolve inside the allowed write roots.
        code_content: Complete Python source code using PyMotorCAD
            (ansys.motorcad.core). Max 200,000 chars.

    Returns:
        JSON string indicating status, created script path, and code line count.
    """
    if not filename or not filename.strip():
        return json.dumps({"status": "error", "error": "Filename parameter cannot be empty."})
    if not code_content or not code_content.strip():
        return json.dumps({"status": "error", "error": "code_content parameter cannot be empty."})
    if len(code_content) > _MAX_CODE_CHARS:
        return json.dumps({"status": "error", "error": f"code_content exceeds {_MAX_CODE_CHARS} chars. Split into smaller scripts."})

    findings = scan_code_safety(code_content)
    if findings:
        return json.dumps({"status": "error", "error": _safety_error(findings)}, indent=2)

    _default_scratch_dir().mkdir(parents=True, exist_ok=True)
    try:
        target_path = _resolve_safe_path(filename)
    except ValueError as e:
        return json.dumps({"status": "error", "error": str(e)}, indent=2)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    project_root = Path(__file__).resolve().parents[2].as_posix()

    code_content = _sanitize_code_content(code_content)

    # Prepend project root to sys.path if not already present.
    # as_posix() avoids Windows raw-string trailing-backslash syntax errors.
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
    """Execute a persisted Python run file (created by `create_run_file`) sequentially.

    Motor-CAD is single-instance and MUTEX-guarded: overlapping calls fail fast
    with status "busy" instead of corrupting the solve — wait, then retry. Call
    this tool ALONE in a turn, never in parallel. After a failure, patch the
    persisted script with `edit_file` and rerun with this tool.

    The file is safety-scanned again at execute time (it may have been patched
    via edit_file since creation). Solve scripts consume the solve budget and
    count toward the consecutive-failure breaker (see /budget).

    Timeout guidance: inspection-only scripts (no solve) finish in seconds —
    the 60 s floor is fine. Any script calling `mc.do_magnetic_calculation()`
    needs `timeout_seconds>=600` (FEA solve ~45-90 s plus Motor-CAD startup).

    Args:
        filename: Name or path of the Python script to execute (relative to
            the active project scratch/, fallback legacy workspace/scratch,
            or an absolute path inside the allowed write roots).
        timeout_seconds: Maximum execution time in seconds (clamped 60-3600;
            default 300; use >=600 for FEA solves).

    Returns:
        JSON string with execution outcome (status, exit_code, stdout, stderr,
        script_path, budget, ledger?). stdout/stderr are tail-truncated with
        head preserved and a truncation notice when over the cap.
    """
    if not filename or not filename.strip():
        return json.dumps({"status": "error", "error": "Filename parameter cannot be empty."})

    try:
        target_path = _resolve_safe_path(filename)
    except ValueError as e:
        return json.dumps({"status": "error", "error": str(e)}, indent=2)

    if not target_path.exists():
        return json.dumps({
            "status": "error",
            "error": f"Run file not found at {target_path}",
            "script_path": str(target_path),
        }, indent=2)

    try:
        timeout_seconds = max(_MIN_TIMEOUT, min(int(timeout_seconds), _MAX_TIMEOUT))
    except (TypeError, ValueError):
        return json.dumps({"status": "error", "error": "timeout_seconds must be an integer."}, indent=2)

    # Safety re-scan: the file may have been patched via edit_file since creation.
    try:
        file_code = target_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return json.dumps({"status": "error", "error": f"Cannot read run file: {e}",
                           "script_path": str(target_path)}, indent=2)
    findings = scan_code_safety(file_code)
    if findings:
        return json.dumps({"status": "error", "error": _safety_error(findings),
                           "script_path": str(target_path)}, indent=2)

    is_solve = _is_solve_code(file_code)

    # Opt-in HITL gate (default off; enable with MOTORCAD_REQUIRE_APPROVAL=1).
    if _execution_approval_enabled():
        decision = _request_execution_approval(str(target_path), is_solve)
        if decision is None:
            return json.dumps({
                "status": "rejected",
                "error": "MOTORCAD_REQUIRE_APPROVAL is set but no interactive terminal "
                         "exists for approval. Unset it or run via CLI.",
                "script_path": str(target_path),
            }, indent=2)
        if not decision:
            return json.dumps({
                "status": "rejected",
                "reason": "Execution declined by the human user.",
                "script_path": str(target_path),
            }, indent=2)

    blocked = _budget_consume(is_solve)
    if blocked:
        return json.dumps({"status": "error", "error": blocked,
                           "script_path": str(target_path),
                           "budget": get_budget_status()}, indent=2)

    if not _EXEC_LOCK.acquire(blocking=False):
        # Queued wait (P1): poll for the lock up to _EXEC_WAIT_TIMEOUT_S so a
        # second caller waits for the running solve instead of failing fast.
        # Single-instance invariant holds: we never run two solves concurrently.
        _acquired = False
        for _ in range(int(_EXEC_WAIT_TIMEOUT_S / _EXEC_WAIT_POLL_S)):
            time.sleep(_EXEC_WAIT_POLL_S)
            if _EXEC_LOCK.acquire(blocking=False):
                _acquired = True
                break
        if not _acquired:
            _metrics_record_busy()
            return json.dumps({
                "status": "busy",
                "code": "busy_retry",
                "retry_after_s": _BUSY_RETRY_AFTER_S,
                "hint": "wait then retry; do not parallelize execution tools",
                "error": "Another Motor-CAD execution is already running (single shared "
                         "instance). Wait then retry — do not parallelize.",
                "script_path": str(target_path),
            }, indent=2)

    cmd = [sys.executable, str(target_path)]
    env = os.environ.copy()

    _t0 = time.perf_counter()
    try:
        process = subprocess.run(
            cmd,
            cwd=str(target_path.parent),
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            env=env,
        )
        _metrics_record_call(int((time.perf_counter() - _t0) * 1000))

        stdout = process.stdout or ""
        stderr = process.stderr or ""
        success = process.returncode == 0
        _budget_record_outcome(success)
        diag = _diagnose_execution_error(stderr) if not success else ""

        result = {
            "status": "success" if success else "failed",
            "exit_code": process.returncode,
            # Keep the tail (traceback error is at the end) plus the head
            # (failing statement context) when output was truncated.
            "stdout": stdout[-_STDOUT_TAIL:] if len(stdout) > _STDOUT_TAIL else stdout,
            "stderr": (stderr[-_STDOUT_TAIL:] if len(stderr) > _STDOUT_TAIL else stderr) + diag,
            "script_path": str(target_path),
            "budget": get_budget_status(),
        }
        if len(stdout) > _STDOUT_TAIL:
            result["stdout_head"] = stdout[:_STDOUT_HEAD]
            result["stdout_truncated"] = True
        if len(stderr) > _STDOUT_TAIL:
            result["stderr_head"] = stderr[:_STDOUT_HEAD]
            result["stderr_truncated"] = True
        ledger = _ledger_hook(stdout, str(target_path), result["status"])
        if ledger is not None:
            result["ledger"] = ledger
        return json.dumps(result, indent=2)
    except subprocess.TimeoutExpired:
        _metrics_record_call(int((time.perf_counter() - _t0) * 1000))
        _budget_record_outcome(False)
        return json.dumps({
            "status": "timeout",
            "error": f"Execution timed out after {timeout_seconds} seconds. Retry with a larger timeout_seconds (FEA solves need >=600).",
            "script_path": str(target_path),
            "budget": get_budget_status(),
        }, indent=2)
    except Exception as e:
        _metrics_record_call(int((time.perf_counter() - _t0) * 1000))
        _budget_record_outcome(False)
        return json.dumps({
            "status": "error",
            "error": f"Subprocess execution failed: {e}",
            "script_path": str(target_path),
            "budget": get_budget_status(),
        }, indent=2)
    finally:
        _EXEC_LOCK.release()


@tool
def execute_generated_motorcad_code(
    code_content: str,
    timeout_seconds: int = 300,
) -> str:
    """1-turn shortcut: persist LLM-generated PyMotorCAD code and run it sequentially.

    Use for single attempts (read a parameter, run one solve). For iterative
    sweeps use `create_run_file` + `edit_file` + `execute_run_file` so the
    script survives across turns.

    Same Motor-CAD contract as `create_run_file`: verify variable names in
    the parameter database first, validate candidates with
    `validate_motor_params` before solving, define safe_get/safe_set, call
    `mc.show_magnetic_context()` before solving, checkpoint before geometry
    mutation, read all results before the next mutation, and print a
    `CANDIDATE_RESULT: {...}` line per evaluated candidate for the ledger.
    Never call this tool in parallel with another execution tool (mutex
    enforced). FEA solves need `timeout_seconds>=600` and consume solve
    budget. Banned primitives (destructive fs, subprocess, network, eval)
    are blocked by the safety scan.

    The script is kept on disk (path returned as `script_path`) whether it
    succeeds or fails, so follow-ups can patch it with `edit_file` instead of
    regenerating from scratch.

    Args:
        code_content: The complete Python source code string to execute
            (max 200,000 chars).
        timeout_seconds: Maximum runtime allowed before timing out
            (clamped 60-3600; default 300; use >=600 for FEA solves).

    Returns:
        JSON string with execution outcome (status, exit_code, stdout, stderr, script_path).
    """
    if not code_content or not code_content.strip():
        return json.dumps({
            "status": "error",
            "error": "code_content parameter cannot be empty.",
        }, indent=2)
    if len(code_content) > _MAX_CODE_CHARS:
        return json.dumps({
            "status": "error",
            "error": f"code_content exceeds {_MAX_CODE_CHARS} chars. Use create_run_file with smaller chunks.",
        }, indent=2)

    try:
        try:
            timeout_seconds = max(_MIN_TIMEOUT, min(int(timeout_seconds), _MAX_TIMEOUT))
        except (TypeError, ValueError):
            return json.dumps({"status": "error", "error": "timeout_seconds must be an integer."}, indent=2)
        run_id = f"sim_{uuid.uuid4().hex[:8]}"
        create_res = create_run_file.invoke({"filename": f"{run_id}.py", "code_content": code_content})
        create_data = json.loads(create_res)
        if create_data.get("status") == "error":
            return create_res

        script_path = create_data["script_path"]
        # Keep every script (success or failure) for audit trail + patch-rerun.
        # Stale files are swept by the CLI after 7 days.
        return execute_run_file.invoke({"filename": script_path, "timeout_seconds": timeout_seconds})
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": f"Failed to execute generated Motor-CAD code: {e}",
        }, indent=2)


__all__ = [
    "create_run_file",
    "execute_run_file",
    "execute_generated_motorcad_code",
    "get_budget_status",
    "reset_execution_budget",
    "scan_code_safety",
    "get_execution_metrics",
    "TOOL_PARALLEL_SAFE",
    "TOOL_SERIAL",
]
