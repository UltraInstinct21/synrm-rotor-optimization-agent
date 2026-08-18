"""Tests for DeepAgent sandbox backend, filesystem tool mounting, code sanitization, and thread session recovery."""

from __future__ import annotations

import json
import threading
from concurrent.futures import ThreadPoolExecutor
from apps.cli.session import Session
from src.tools.todo_tools import set_active_session, write_todos, update_todo_status
from src.tools.execution import _sanitize_code_content, create_run_file
from src.agent.factory import build_tools


def test_todo_tools_thread_safety():
    """Verify write_todos and update_todo_status work across worker threads."""
    s = Session()
    set_active_session(s)

    def worker():
        res = write_todos.invoke({"tasks": ["1. Task A", "2. Task B"]})
        data = json.loads(res)
        assert data["status"] == "success"
        
        res_upd = update_todo_status.invoke({"todo_id": "1", "status": "completed"})
        data_upd = json.loads(res_upd)
        assert data_upd["status"] == "success"

    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(worker)
        future.result()

    todos = s.get_todos()
    assert len(todos) == 2
    assert todos[0]["status"] == "completed"


def test_code_sanitization():
    """Verify raw string trailing backslash sanitization in Python code."""
    bad_code = 'path = r"D:\\SRM\\Agent\\"\nprint(path)'
    clean = _sanitize_code_content(bad_code)
    assert 'r"D:\\SRM\\Agent/"' in clean or 'r"D:\\SRM\\Agent/"' in clean


def test_build_tools_includes_wiki_tool():
    """Verify build_tools contains wiki_tool."""
    tools = build_tools()
    tool_names = {t.name for t in tools}
    assert "wiki_tool" in tool_names


def test_robust_filesystem_backend_path_normalization():
    """Verify RobustFilesystemBackend normalizes Windows absolute paths cleanly without errors."""
    from pathlib import Path
    from src.agent.factory import RobustFilesystemBackend
    from src.config import settings

    backend_virt = RobustFilesystemBackend(root_dir=settings.PROJECT_ROOT, virtual_mode=True)
    win_abs_path = str(settings.PROJECT_ROOT / "workspace" / "wiki")
    
    res_virt = backend_virt._resolve_path(win_abs_path)
    assert res_virt.resolve() == (settings.PROJECT_ROOT / "workspace" / "wiki").resolve()

    backend_nonvirt = RobustFilesystemBackend(root_dir=settings.PROJECT_ROOT, virtual_mode=False)
    res_nonvirt = backend_nonvirt._resolve_path(win_abs_path)
    assert res_nonvirt.resolve() == (settings.PROJECT_ROOT / "workspace" / "wiki").resolve()

