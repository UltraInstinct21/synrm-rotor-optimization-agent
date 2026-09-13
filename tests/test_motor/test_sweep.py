"""Tests for deterministic sweep primitives."""

from __future__ import annotations

import pytest

from src.motor.sweep import clamp, has_converged, latin_hypercube, neighbors

BOUNDS = {"a": (0.0, 10.0), "b": (-5.0, 5.0)}


def test_lhs_count_and_bounds():
    pts = latin_hypercube(BOUNDS, 20, seed=42)
    assert len(pts) == 20
    for p in pts:
        assert 0.0 <= p["a"] <= 10.0
        assert -5.0 <= p["b"] <= 5.0


def test_lhs_deterministic():
    assert latin_hypercube(BOUNDS, 10, seed=7) == latin_hypercube(BOUNDS, 10, seed=7)
    assert latin_hypercube(BOUNDS, 10, seed=7) != latin_hypercube(BOUNDS, 10, seed=8)


def test_lhs_stratified_coverage():
    # Each of the n strata per dim should hold exactly one sample.
    pts = latin_hypercube({"a": (0.0, 10.0)}, 10, seed=3)
    strata = sorted(int(p["a"] // 1) for p in pts)
    assert strata == list(range(10))


def test_lhs_rejects_bad_bounds():
    with pytest.raises(ValueError):
        latin_hypercube({"a": (5.0, 5.0)}, 4, seed=1)
    with pytest.raises(ValueError):
        latin_hypercube(BOUNDS, 0, seed=1)


def test_clamp():
    assert clamp({"a": 99, "b": -99}, BOUNDS) == {"a": 10.0, "b": -5.0}


def test_neighbors():
    n = neighbors({"a": 5.0, "b": 0.0}, {"a": 1.0, "b": 0.5})
    assert len(n) == 4
    assert {"a": 4.0, "b": 0.0} in n and {"a": 6.0, "b": 0.0} in n
    assert {"a": 5.0, "b": -0.5} in n and {"a": 5.0, "b": 0.5} in n


def test_has_converged():
    assert has_converged([140.0, 140.3], tol=0.5)
    assert not has_converged([140.0, 141.0], tol=0.5)
    assert not has_converged([140.0], tol=0.5)
