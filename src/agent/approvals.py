"""Approval gates — permission boundaries between subsystems.

Each capability has a recommended permission level.  The orchestrator uses
these to decide whether to ask the user before delegating a sensitive task.
"""

from __future__ import annotations

from enum import Enum


class PermissionLevel(Enum):
    """How much autonomy a subsystem has."""

    # Proceed without asking — safe, well-scoped operations.
    AUTO = "auto"
    # Ask the user before acting — code writes, wiki edits, experiment runs.
    MANUAL = "manual"
    # Always present a detailed plan for user approval first.
    APPROVAL = "approval"


# ── Default permission map ────────────────────────────────────────────
# Subsystem → default permission level for its primary operation.
PERMISSIONS: dict[str, PermissionLevel] = {
    # Repo coding
    "read_code": PermissionLevel.AUTO,
    "edit_code": PermissionLevel.MANUAL,
    "run_tests": PermissionLevel.MANUAL,
    # Wiki
    "read_wiki": PermissionLevel.AUTO,
    "edit_wiki": PermissionLevel.MANUAL,
    "create_wiki_page": PermissionLevel.MANUAL,
    # Research
    "search_web": PermissionLevel.AUTO,
    "read_sources": PermissionLevel.AUTO,
    "synthesize": PermissionLevel.AUTO,
    # Execution
    "run_script": PermissionLevel.MANUAL,
    "read_output": PermissionLevel.AUTO,
}


def requires_approval(action: str) -> PermissionLevel:
    """Return the permission level for *action*.

    Falls back to MANUAL for unknown actions (safe default).
    """
    return PERMISSIONS.get(action, PermissionLevel.MANUAL)
