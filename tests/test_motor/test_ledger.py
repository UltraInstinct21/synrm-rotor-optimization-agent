"""Tests for the append-only experiment ledger."""

from __future__ import annotations

from src.motor.ledger import best_by_objective, ledger_path, load_ledger, log_candidate


def test_log_and_load(tmp_path):
    p = log_candidate({"params": {"a": 1}, "objective": 5.0},
                      project_slug="proj", base_dir=tmp_path)
    assert p == ledger_path("proj", tmp_path)
    rows = load_ledger("proj", tmp_path)
    assert len(rows) == 1
    assert rows[0]["params"] == {"a": 1}
    assert "timestamp" in rows[0]


def test_best_by_objective(tmp_path):
    log_candidate({"objective": 9.0}, project_slug="p", base_dir=tmp_path)
    log_candidate({"objective": 2.0}, project_slug="p", base_dir=tmp_path)
    log_candidate({"no_score": True}, project_slug="p", base_dir=tmp_path)
    best = best_by_objective("p", tmp_path)
    assert best is not None and best["objective"] == 2.0


def test_best_none_when_unscored(tmp_path):
    assert best_by_objective("empty", tmp_path) is None


def test_corrupt_lines_skipped(tmp_path):
    p = ledger_path("c", tmp_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text('{"ok": 1}\nnot json\n{"ok": 2}\n', encoding="utf-8")
    assert len(load_ledger("c", tmp_path)) == 2
