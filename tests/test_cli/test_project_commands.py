"""Tests for /spec, /budget, /preflight commands (read-only paths)."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from src.config import settings


def _make_cli():
    from apps.cli.app import MotorCLI

    cli = MotorCLI()
    cli.console = MagicMock()
    return cli


def test_slash_commands_registered():
    from apps.cli.commands import COMMANDS

    for cmd in ("spec", "budget", "preflight"):
        assert cmd in COMMANDS


def test_spec_list():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    dispatch(cli, "/spec list")
    cli.console.print.assert_called()


def test_spec_show_active():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    dispatch(cli, "/spec show")
    cli.console.print.assert_called()


def test_spec_use_missing():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    dispatch(cli, "/spec use does-not-exist-zzz")
    printed = " ".join(str(c) for c in cli.console.print.call_args_list)
    assert "not found" in printed


def test_budget_show_and_reset():
    from apps.cli.commands import dispatch
    from src.tools import execution as ex

    ex.reset_execution_budget()
    cli = _make_cli()
    dispatch(cli, "/budget")
    cli.console.print.assert_called()
    dispatch(cli, "/budget reset")
    printed = " ".join(str(c) for c in cli.console.print.call_args_list)
    assert "reset" in printed.lower()


def test_preflight_command():
    from apps.cli.commands import dispatch

    cli = _make_cli()
    with patch("src.config.preflight.run_preflight",
               return_value=[{"check": "x", "level": "ok", "message": "y"}]):
        dispatch(cli, "/preflight")
    cli.console.print.assert_called()
