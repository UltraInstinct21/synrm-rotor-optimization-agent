"""Unit tests for agent-wide error handling, loop safety, path traversal defense, and session recovery."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

from apps.cli.session import Session
from src.tools.execution import (
    create_run_file,
    execute_run_file,
    execute_generated_motorcad_code,
    _diagnose_execution_error,
)
from src.tools.wiki import wiki_tool
from src.tools.research.research_tool import research_subgraph


def test_wiki_path_traversal_prevention():
    """Verify that wiki_tool blocks path traversal attempts."""
    res = wiki_tool.invoke({"action": "read", "page_path": "../../../AGENTS.md"})
    data = json.loads(res)
    assert data.get("status") == "error"
    assert "Wiki page not found or path invalid" in data.get("error", "")

    res_write = wiki_tool.invoke({"action": "write", "page_path": "../../hacked.md", "content": "bad"})
    data_write = json.loads(res_write)
    assert data_write.get("status") == "error"
    assert "Invalid or prohibited wiki path" in data_write.get("error", "")


def test_execution_path_resolution_and_empty_inputs():
    """Verify input validation and empty parameter traps in execution tools."""
    res_empty_file = create_run_file.invoke({"filename": "", "code_content": "print('hello')"})
    data_empty_file = json.loads(res_empty_file)
    assert data_empty_file.get("status") == "error"

    res_empty_exec = execute_run_file.invoke({"filename": ""})
    data_empty_exec = json.loads(res_empty_exec)
    assert data_empty_exec.get("status") == "error"

    res_empty_gen = execute_generated_motorcad_code.invoke({"code_content": ""})
    data_empty_gen = json.loads(res_empty_gen)
    assert data_empty_gen.get("status") == "error"


def test_stderr_diagnostics_parser():
    """Verify stderr diagnostic hints parser."""
    hint1 = _diagnose_execution_error("ModuleNotFoundError: No module named 'ansys.motorcad.core'")
    assert "PyMotorCAD package is missing" in hint1

    hint2 = _diagnose_execution_error("SyntaxError: invalid syntax")
    assert "Python script contains a syntax error" in hint2


def test_corrupted_session_recovery():
    """Verify that corrupted session files are safely recovered without crashing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        corrupted_path = Path(tmpdir) / "bad_session.json"
        corrupted_path.write_text("{ invalid json structure", encoding="utf-8")

        recovered = Session.load(corrupted_path)
        assert recovered.id == "bad_session"
        assert len(recovered.messages) == 1
        assert "Recovered session" in recovered.messages[0]["content"]


def test_research_subgraph_empty_input():
    """Verify research subgraph empty input validation."""
    import asyncio
    res = asyncio.run(research_subgraph.ainvoke({"question": ""}))
    data = json.loads(res)
    assert data.get("status") == "error"
    assert "cannot be empty" in data.get("error", "")
