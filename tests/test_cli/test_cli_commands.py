"""Tests for CLI slash commands, session management, and visual components (No-Emoji)."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from apps.cli.app import MotorCLI
from apps.cli.commands import COMMANDS, dispatch
from apps.cli.session import Session, SessionStore
from apps.cli.theme import render_banner, render_user_query, get_tool_label


def test_session_lifecycle():
    with tempfile.TemporaryDirectory() as tmpdir:
        store = SessionStore(Path(tmpdir))
        session = store.new()
        assert len(session.id) == 12
        assert session.message_count == 0

        session.add("user", "What is SynRM motor efficiency?")
        session.add("assistant", "SynRM efficiency can exceed IE5 levels.")

        assert session.message_count == 2
        assert session.title == "What is SynRM motor efficiency?"

        # Test reload
        loaded = store.load_session(session.id)
        assert loaded is not None
        assert loaded.message_count == 2

        # Test markdown export
        export_file = Path(tmpdir) / "exported.md"
        session.export_markdown(export_file)
        assert export_file.exists()
        content = export_file.read_text(encoding="utf-8")
        assert "SynRM motor efficiency" in content


def test_slash_commands_registered():
    expected = ["help", "exit", "clear", "version", "expanded", "hitl", "todo", "model", "tools", "session", "history", "config", "system", "copy"]
    for cmd in expected:
        assert cmd in COMMANDS


def test_help_command():
    cli = MotorCLI()
    cli.console = MagicMock()
    res = dispatch(cli, "/help")
    assert res is None
    cli.console.print.assert_called()


def test_config_command():
    cli = MotorCLI()
    cli.console = MagicMock()
    cli.tools = [MagicMock(name="mock_tool")]
    res = dispatch(cli, "/config")
    assert res is None


def test_system_command():
    cli = MotorCLI()
    cli.console = MagicMock()
    res = dispatch(cli, "/system")
    assert res is None


def test_session_subcommands():
    cli = MotorCLI()
    cli.console = MagicMock()

    # /session list
    dispatch(cli, "/session list")

    # /session new
    dispatch(cli, "/session new")
    old_id = cli.current_session.id

    # /session load
    dispatch(cli, f"/session load {old_id}")
    assert cli.current_session.id == old_id


def test_hitl_toggle():
    cli = MotorCLI()
    cli.console = MagicMock()

    dispatch(cli, "/hitl off")
    from src.tools.search import get_hitl_enabled
    assert get_hitl_enabled() is False

    dispatch(cli, "/hitl on")
    assert get_hitl_enabled() is True


def test_tool_labels():
    assert get_tool_label("execute_generated_motorcad_code") == "[MOTORCAD]"
    assert get_tool_label("tavily_search") == "[SEARCH]"
    assert get_tool_label("research_subgraph") == "[RESEARCH]"
    assert get_tool_label("wiki_tool") == "[WIKI]"
    assert get_tool_label("create_run_file") == "[MOTORCAD]"
    assert get_tool_label("file_creator") == "[FILE]"


def test_todo_command():
    cli = MotorCLI()
    cli.console = MagicMock()

    dispatch(cli, "/todo add Run EMag calculation")
    todos = cli.current_session.get_todos()
    assert len(todos) == 1
    assert todos[0]["task"] == "Run EMag calculation"
    assert todos[0]["status"] == "pending"

    dispatch(cli, f"/todo done {todos[0]['id']}")
    todos = cli.current_session.get_todos()
    assert todos[0]["status"] == "completed"

    dispatch(cli, "/todo clear")
    assert len(cli.current_session.get_todos()) == 0


def test_hitl_approval_prompt():
    from apps.cli.display import request_hitl_approval
    console = MagicMock()

    with patch("builtins.input", return_value="y"):
        approved = request_hitl_approval(console, "tavily_search", {"query": "SynRM efficiency"})
        assert approved is True

    with patch("builtins.input", return_value="n"):
        approved = request_hitl_approval(console, "tavily_search", {"query": "SynRM efficiency"})
        assert approved is False


def test_render_bottom_input_bar_with_todos():
    from apps.cli.streaming import render_bottom_input_bar
    from apps.cli.session import Session

    session = Session(id="test1234")
    session.add_todo("Run EMag calculation", status="in_progress")
    session.add_todo("Optimize rotor flux barriers", status="pending")

    # Ensure render_bottom_input_bar renders without MarkupError crash
    grid = render_bottom_input_bar(
        session=session,
        model_name="test_model",
        expanded=True,
        active_tool="execute_generated_motorcad_code",
        width=80,
    )
    assert grid is not None


