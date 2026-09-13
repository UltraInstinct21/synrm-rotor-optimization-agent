"""Tests for machine spec loading and resolution."""

from __future__ import annotations

import json

import pytest

from src.motor.spec import (
    MachineSpec,
    list_specs,
    load_active_spec,
    load_spec,
    resolve_active_spec_path,
)


def test_load_bundled_default():
    spec = load_active_spec()
    assert spec.slug == "synrm_45kw"
    assert spec.machine_type == "SynRM"
    assert len(spec.params) == 12
    assert len(spec.targets) == 4


def test_resolve_order_env_override(tmp_path, monkeypatch):
    from src.config import projects as projectsmod

    custom = {"project": "x", "slug": "x", "params": {"P": {"min": 0, "max": 1}},
              "targets": []}
    p = tmp_path / "custom.json"
    p.write_text(json.dumps(custom), encoding="utf-8")
    monkeypatch.setenv("MOTOR_SPEC", str(p))
    # No active project -> legacy $MOTOR_SPEC override applies.
    monkeypatch.setattr(projectsmod, "get_active_slug", lambda: None)
    monkeypatch.delenv("MOTOR_PROJECT", raising=False)
    assert resolve_active_spec_path() == p
    assert load_active_spec().slug == "x"


def test_resolve_order_project_beats_env(tmp_path, monkeypatch):
    from src.config import projects as projectsmod

    proj = {"project": "proj", "slug": "proj",
            "params": {"P": {"min": 0, "max": 1}}, "targets": []}
    p = tmp_path / "spec.json"
    p.write_text(json.dumps(proj), encoding="utf-8")
    monkeypatch.setattr(projectsmod, "active_spec_path", lambda: p)
    monkeypatch.setenv("MOTOR_SPEC", str(tmp_path / "other.json"))
    # Active project folder wins over $MOTOR_SPEC.
    assert resolve_active_spec_path() == p
    assert load_active_spec().slug == "proj"


def test_spec_use_active_json(tmp_path, monkeypatch):
    from src.config import projects as projectsmod
    from src.motor import spec as specmod

    monkeypatch.setattr(specmod, "specs_dir", lambda: tmp_path)
    monkeypatch.setattr(projectsmod, "get_active_slug", lambda: None)
    monkeypatch.delenv("MOTOR_PROJECT", raising=False)
    (tmp_path / "demo.json").write_text(json.dumps({
        "project": "demo", "slug": "demo",
        "params": {"P": {"min": 0, "max": 1}}, "targets": []}), encoding="utf-8")
    (tmp_path / "active.json").write_text(
        (tmp_path / "demo.json").read_text(encoding="utf-8"), encoding="utf-8")
    monkeypatch.delenv("MOTOR_SPEC", raising=False)
    assert load_active_spec().slug == "demo"


def test_invalid_spec_rejected():
    with pytest.raises(ValueError):
        MachineSpec.from_dict({"project": "bad", "params": {}})
    with pytest.raises(ValueError):
        MachineSpec.from_dict({"project": "bad",
                               "params": {"P": {"min": 5, "max": 5}}})
    with pytest.raises(ValueError):
        MachineSpec.from_dict({"project": "bad",
                               "params": {"P": {"min": 0, "max": 1}},
                               "targets": [{"key": "t"}]})


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_spec("/nonexistent/spec.json")


def test_list_specs_includes_default():
    names = {s["name"] for s in list_specs()}
    assert "synrm_45kw" in names
