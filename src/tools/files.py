"""HITL-gated file-deletion tool.

This module is the ONLY sanctioned way to delete a file or empty directory
in this repo. Generated Motor-CAD scripts must never delete anything:
the execution safety scan bans destructive primitives (shutil, os.remove /
os.unlink / os.rmdir, subprocess, eval/exec, network) in generated code,
so agent-side deletion must go through the `delete_file` tool below, which
requires explicit human approval on every call.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from langchain_core.tools import tool


def is_delete_approval_required() -> bool:
    """Return True unless headless pre-approval is explicitly enabled.

    Reads env var ``DELETE_REQUIRE_APPROVAL`` (default "1"). When set to
    "0" or "false" (case-insensitive), approval prompting is skipped for
    pre-approved headless runs (the skip is still logged). Any other value
    — including unset — means approval is required.
    """
    return os.getenv("DELETE_REQUIRE_APPROVAL", "1").lower() not in ("0", "false")


@tool
def delete_file(path: str) -> str:
    """Delete a regular file or an EMPTY directory, with human approval.

    This is the ONLY sanctioned way to delete a file in this repo.
    Generated Motor-CAD scripts must never delete (safety scan bans it).

    Scope: regular files (and symlinks) via Path.unlink(), empty
    directories via Path.rmdir(). Refuses with status "error": empty
    path, filesystem root/anchor, non-existent path, non-empty
    directories. Full filesystem access is allowed — any absolute path
    outside the repo is fine as long as it is not a root anchor and not
    a non-empty directory.

    EVERY call requires human approval via request_hitl_approval unless
    DELETE_REQUIRE_APPROVAL is "0"/"false" (pre-approved headless run,
    still logged). When the approval UI raises (no terminal) and the env
    gate is not disabled, the call is rejected (no deletion).

    Args:
        path: Path of the file or empty directory to delete.

    Returns:
        JSON string with status "success" | "error" | "rejected".
    """
    if not path or not str(path).strip():
        return json.dumps(
            {"status": "error", "path": path, "error": "path parameter cannot be empty."},
            indent=2,
        )

    raw = str(path).strip()
    try:
        resolved = Path(raw).expanduser().resolve()
    except Exception:
        resolved = Path(raw).expanduser().absolute()
    resolved_str = str(resolved)

    # Refuse filesystem root/anchor (e.g. "/" or "C:\\").
    try:
        anchor = resolved.anchor
    except Exception:
        anchor = ""
    if (anchor and resolved_str == anchor) or resolved.parent == resolved:
        return json.dumps(
            {"status": "error", "path": resolved_str, "error": "refusing to delete filesystem root."},
            indent=2,
        )

    # Refuse non-existent paths (lexists so broken symlinks are deletable).
    if not os.path.lexists(resolved_str):
        return json.dumps(
            {"status": "error", "path": resolved_str, "error": "path does not exist."},
            indent=2,
        )

    # Human-In-The-Loop Approval Check (mirrors tavily_search: decoupled
    # from CLI so headless runtimes — run.py, tests, langgraph server —
    # don't import prompt_toolkit at module scope and don't crash).
    if is_delete_approval_required():
        approved: bool | None = None
        try:
            from apps.cli.display import request_hitl_approval
            from apps.cli.theme import get_console

            console = get_console()
            approved = request_hitl_approval(
                console=console,
                tool_name="delete_file",
                details={"path": resolved_str},
            )
        except Exception:
            # No interactive console (server/test/headless): fail closed.
            return json.dumps(
                {
                    "status": "rejected",
                    "path": resolved_str,
                    "reason": (
                        "No interactive terminal for HITL approval. "
                        "Set DELETE_REQUIRE_APPROVAL=0 for pre-approved headless runs."
                    ),
                },
                indent=2,
            )
        if not approved:
            return json.dumps(
                {
                    "status": "rejected",
                    "path": resolved_str,
                    "reason": "File deletion request was declined by the human user in HITL approval check.",
                },
                indent=2,
            )
    else:
        # Pre-approved headless run: skip the prompt but still log.
        print(f"[delete_file] pre-approved headless run (DELETE_REQUIRE_APPROVAL=0): {resolved_str}")

    # Scope enforcement + deletion. Never shutil / subprocess / os.system.
    try:
        target = Path(resolved_str)
        if target.is_dir() and not target.is_symlink():
            try:
                next(target.iterdir())
            except StopIteration:
                pass
            else:
                return json.dumps(
                    {
                        "status": "error",
                        "path": resolved_str,
                        "error": "refusing to delete non-empty directory.",
                    },
                    indent=2,
                )
            target.rmdir()
            return json.dumps(
                {"status": "success", "path": resolved_str, "deleted": True, "type": "directory"},
                indent=2,
            )
        if target.is_file() or target.is_symlink():
            target.unlink()
            return json.dumps(
                {"status": "success", "path": resolved_str, "deleted": True, "type": "file"},
                indent=2,
            )
        return json.dumps(
            {
                "status": "error",
                "path": resolved_str,
                "error": "not a regular file or empty directory; refusing to delete.",
            },
            indent=2,
        )
    except Exception as e:
        return json.dumps(
            {"status": "error", "path": resolved_str, "error": f"delete failed: {e}"},
            indent=2,
        )


__all__ = ["delete_file", "is_delete_approval_required"]
