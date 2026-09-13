"""Experiment ledger — append-only JSONL record of every evaluated candidate.

The execution wrapper auto-logs any script that prints a
`CANDIDATE_RESULT: {...}` line. Generated scripts may also import this module
(project root is on sys.path) and call log_candidate() directly.

Record schema: {timestamp, project, iteration?, params, results, objective?,
all_passed?, script_path?, status?}. Ledger location resolution:
$MOTOR_LEDGER_DIR override > active project folder (workspace/projects/<slug>/
ledger.jsonl) > legacy workspace/experiments/<slug>/ (tests use the override).
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any


def ledger_base_dir() -> Path:
    override = os.getenv("MOTOR_LEDGER_DIR", "").strip()
    if override:
        return Path(override)
    from src.config.settings import WORKSPACE_ROOT

    return WORKSPACE_ROOT / "experiments"


def ledger_path(project_slug: str, base_dir: str | Path | None = None) -> Path:
    if base_dir is not None:
        return Path(base_dir) / project_slug / "ledger.jsonl"
    override = os.getenv("MOTOR_LEDGER_DIR", "").strip()
    if override:
        return Path(override) / project_slug / "ledger.jsonl"
    # Prefer the active project folder when it matches the slug (or when the
    # slug's project folder exists at all) so each project keeps its own log.
    try:
        from src.config.projects import ledger_path as _project_ledger_path
        from src.config.projects import get_active_slug, project_dir

        slug = (project_slug or "").strip()
        if slug and project_dir(slug).exists():
            return _project_ledger_path(slug)
        active = get_active_slug()
        if active and slug in ("", active, "default"):
            return _project_ledger_path(active)
    except Exception:
        pass
    base = ledger_base_dir()
    return base / project_slug / "ledger.jsonl"


def log_candidate(record: dict[str, Any], project_slug: str = "",
                  base_dir: str | Path | None = None) -> Path:
    """Append one candidate record; returns the ledger path."""
    if not isinstance(record, dict):
        raise ValueError("record must be an object")
    if not project_slug:
        project_slug = str(record.get("project_slug", "") or "default")
    path = ledger_path(project_slug, base_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    entry = {"timestamp": time.time(), **record}
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, default=str) + "\n")
    return path


def load_ledger(project_slug: str, base_dir: str | Path | None = None) -> list[dict]:
    path = ledger_path(project_slug, base_dir)
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def best_by_objective(project_slug: str, base_dir: str | Path | None = None) -> dict | None:
    """Return the logged record with the lowest objective (None if unscored)."""
    scored = [r for r in load_ledger(project_slug, base_dir)
              if isinstance(r.get("objective"), (int, float))]
    if not scored:
        return None
    return min(scored, key=lambda r: r["objective"])


__all__ = ["best_by_objective", "ledger_base_dir", "ledger_path", "load_ledger", "log_candidate"]
