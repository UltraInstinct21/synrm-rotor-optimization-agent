"""Deterministic sweep primitives — the agent invokes these, not improvisation.

Phase 1: latin_hypercube(bounds, n, seed) for the coarse sweep.
Phase 2: neighbors(candidate, steps) for coordinate descent from the best
candidate, stopping when has_converged(torque_history, tol) is true.
All functions are pure and seeded: same inputs always give same outputs.
Generated Motor-CAD scripts import them via `from src.motor.sweep import ...`
(project root is prepended to sys.path automatically).
"""

from __future__ import annotations

import random


def latin_hypercube(bounds: dict[str, tuple[float, float]], n: int, seed: int) -> list[dict]:
    """Seeded Latin Hypercube sample over {param: (lo, hi)}. Returns n dicts."""
    if n < 1:
        raise ValueError("n must be >= 1")
    rng = random.Random(seed)
    names = list(bounds.keys())
    strata: dict[str, list[float]] = {}
    for name in names:
        lo, hi = bounds[name]
        if lo >= hi:
            raise ValueError(f"bound '{name}' needs lo < hi")
        perm = rng.sample(range(n), n)
        strata[name] = [lo + (s + rng.random()) / n * (hi - lo) for s in perm]
    return [{name: strata[name][i] for name in names} for i in range(n)]


def clamp(candidate: dict, bounds: dict[str, tuple[float, float]]) -> dict:
    """Clamp every candidate value into its bounds."""
    out = dict(candidate)
    for name, (lo, hi) in bounds.items():
        if name in out:
            out[name] = min(hi, max(lo, float(out[name])))
    return out


def neighbors(candidate: dict, steps: dict[str, float]) -> list[dict]:
    """One coordinate-descent step: +/- step per param. Returns 2*len(steps) dicts."""
    out = []
    for name, step in steps.items():
        if name not in candidate:
            continue
        lo = dict(candidate)
        lo[name] = float(candidate[name]) - step
        hi = dict(candidate)
        hi[name] = float(candidate[name]) + step
        out.extend([lo, hi])
    return out


def has_converged(torque_history: list[float], tol: float = 0.5) -> bool:
    """Converged when the last two reported torques differ by less than tol."""
    if len(torque_history) < 2:
        return False
    return abs(float(torque_history[-1]) - float(torque_history[-2])) < tol


__all__ = ["clamp", "has_converged", "latin_hypercube", "neighbors"]
