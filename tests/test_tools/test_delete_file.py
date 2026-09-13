"""Tests for the HITL-gated delete_file tool (no terminal required)."""

from __future__ import annotations

import json

from src.tools.files import delete_file, is_delete_approval_required


def _invoke(path: str) -> dict:
    return json.loads(delete_file.invoke({"path": path}))


def test_delete_real_temp_file_preapproved(tmp_path, monkeypatch):
    monkeypatch.setenv("DELETE_REQUIRE_APPROVAL", "0")
    assert is_delete_approval_required() is False
    target = tmp_path / "to_delete.txt"
    target.write_text("hello", encoding="utf-8")
    assert target.exists()
    res = _invoke(str(target))
    assert res["status"] == "success"
    assert res.get("deleted") is True
    assert not target.exists()


def test_non_empty_dir_refused(tmp_path, monkeypatch):
    monkeypatch.setenv("DELETE_REQUIRE_APPROVAL", "0")
    d = tmp_path / "full_dir"
    d.mkdir()
    (d / "child.txt").write_text("x", encoding="utf-8")
    res = _invoke(str(d))
    assert res["status"] == "error"
    assert "non-empty" in res["error"].lower()
    # Directory must survive the refusal.
    assert d.exists()
    assert (d / "child.txt").exists()


def test_missing_path_returns_error(tmp_path, monkeypatch):
    monkeypatch.setenv("DELETE_REQUIRE_APPROVAL", "0")
    missing = tmp_path / "does_not_exist.txt"
    res = _invoke(str(missing))
    assert res["status"] == "error"
    assert "not exist" in res["error"].lower() or "does not exist" in res["error"].lower()


def test_approval_declined_returns_rejected_and_file_survives(tmp_path, monkeypatch):
    monkeypatch.setenv("DELETE_REQUIRE_APPROVAL", "1")
    assert is_delete_approval_required() is True
    import apps.cli.display as display

    monkeypatch.setattr(display, "request_hitl_approval", lambda console, tool_name, details: False)
    target = tmp_path / "keep_me.txt"
    target.write_text("important", encoding="utf-8")
    res = _invoke(str(target))
    assert res["status"] == "rejected"
    assert target.exists()
    assert target.read_text(encoding="utf-8") == "important"
