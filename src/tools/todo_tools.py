"""Session TODO tracking tools — allow DeepAgent to plan and update task progress mid-session."""

from __future__ import annotations

import json
from typing import Any
from langchain_core.tools import tool
import threading

_thread_local = threading.local()
_global_session = None


def set_active_session(session: Any) -> None:
    """Register the active CLI session for TODO tools across thread contexts."""
    global _global_session
    _thread_local.session = session
    _global_session = session


def get_active_session() -> Any:
    """Retrieve the active CLI session safely across threads."""
    sess = getattr(_thread_local, 'session', None)
    if sess is not None:
        return sess
    return _global_session


@tool
def write_todos(tasks: list[str]) -> str:
    """Set or update the list of TODO items/tasks for the current session optimization or workflow.

    Args:
        tasks: List of task description strings (e.g. ["1. Check stator geometry", "2. Run EMag calculation", "3. Save model"]).

    Returns:
        JSON string confirming created TODO items.
    """
    session = get_active_session()
    if session is None:
        return json.dumps({"status": "error", "error": "No active session registered for TODOs."})

    session.clear_todos()
    created = []
    for task in tasks:
        item = session.add_todo(task, status="pending")
        created.append(item)

    return json.dumps({
        "status": "success",
        "message": f"Updated TODO list with {len(created)} tasks.",
        "todos": session.get_todos(),
    }, indent=2)


@tool
def update_todo_status(todo_id: str, status: str) -> str:
    """Update the status of a TODO task item as the agent executes steps mid-session.

    Args:
        todo_id: The task ID/number string (e.g. "1", "2").
        status: The new status string: 'pending', 'in_progress', or 'completed' (or 'done').

    Returns:
        JSON string confirming status update.
    """
    session = get_active_session()
    if session is None:
        return json.dumps({"status": "error", "error": "No active session registered for TODOs."})

    normalized = status.lower().strip()
    if normalized in ("done", "completed", "complete", "finished"):
        norm_status = "completed"
    elif normalized in ("in_progress", "running", "active", "doing"):
        norm_status = "in_progress"
    else:
        norm_status = "pending"

    success = session.update_todo(todo_id, norm_status)
    if success:
        return json.dumps({
            "status": "success",
            "todo_id": todo_id,
            "new_status": norm_status,
            "todos": session.get_todos(),
        }, indent=2)
    else:
        return json.dumps({
            "status": "error",
            "error": f"TODO item with ID '{todo_id}' not found.",
            "todos": session.get_todos(),
        }, indent=2)


__all__ = ["write_todos", "update_todo_status", "set_active_session", "get_active_session"]
