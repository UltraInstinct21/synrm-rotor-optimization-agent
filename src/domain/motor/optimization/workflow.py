"""Optimization workflow — sweep, compare, and select candidate motor designs.

Provides:
- ``run_sweep()`` — run a parameter sweep across a design space.
- ``compare_designs()`` — compare multiple candidate designs.
"""

from __future__ import annotations

import csv
import math
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from src.artifacts import ExperimentReport
from src.domain.motor.geometry_models import MotorDesign
from src.domain.motor.parameter_mapping import design_to_motorcad_params
from src.domain.motor.result_models import ComparisonResult, ElectromagneticResult


@dataclass
class SweepConfig:
    """Configuration for a parameter sweep."""

    parameter_ranges: dict[str, tuple[float, float]] = field(default_factory=dict)
    """Parameter name → (min, max)."""

    fixed_params: dict[str, float] = field(default_factory=dict)
    """Parameters held constant across all candidates."""

    num_candidates: int = 10
    """Number of candidate points (for LHS-like sampling)."""


def _lhs_sample(ranges: dict[str, tuple[float, float]], n: int) -> list[dict[str, float]]:
    """Latin Hypercube Sampling — simple 1D stratification per parameter."""
    samples = []
    param_names = list(ranges.keys())

    for _ in range(n):
        point = {}
        for name in param_names:
            lo, hi = ranges[name]
            # Simple random sample within bounds.
            point[name] = random.uniform(lo, hi)
        samples.append(point)

    return samples


def _compute_metrics(params: dict[str, float], fixed: dict[str, float]) -> ElectromagneticResult:
    """Compute approximate electromagnetic metrics from geometry parameters.

    For Phase 4 this is a simplified analytical model.  In production,
    this would call PyMotorCAD FEA via ``run_motorcad.run_and_extract()``.
    """
    stack = params.get("stack_length_mm", fixed.get("stack_length_mm", 200))
    turns = params.get("turns_per_coil", fixed.get("turns_per_coil", 8))
    speed = fixed.get("speed_rpm", 3000)
    voltage = fixed.get("voltage_v", 400)

    # Simplified scaling model — placeholder until real FEA is integrated.
    # These are not physically accurate; they demonstrate the pipeline.
    torque_base = 143.0
    torque = torque_base * (stack / 200.0) * (turns / 8.0) * voltage / 400.0

    efficiency = 95.0 - random.uniform(0, 3)
    power_factor = 0.75 + random.uniform(0, 0.15)
    saliency = 5.0 + random.uniform(0, 3)
    ld = 15.0 + random.uniform(-2, 2)
    lq = ld * saliency

    omega = speed * (2 * math.pi / 60)
    power = torque * omega / 1000

    return ElectromagneticResult(
        torque_nm=round(torque, 1),
        efficiency_pct=round(efficiency, 1),
        power_factor=round(power_factor, 3),
        speed_rpm=speed,
        output_power_kw=round(power, 2),
        ld_mh=round(ld, 2),
        lq_mh=round(lq, 2),
        saliency=round(saliency, 2),
        copper_loss_w=round(random.uniform(500, 1500), 0),
        iron_loss_w=round(random.uniform(200, 600), 0),
    )


def run_sweep(
    config: SweepConfig,
    base_design: MotorDesign | None = None,
    log_dir: str | Path | None = None,
) -> ExperimentReport:
    """Run a parameter sweep and return results.

    In Phase 4 this dispatches to PyMotorCAD.  Currently uses analytical
    placeholder models to demonstrate the pipeline.
    """
    import uuid
    from datetime import datetime

    sweep_id = f"sweep_{uuid.uuid4().hex[:8]}"
    samples = _lhs_sample(config.parameter_ranges, config.num_candidates)

    results: list[dict[str, Any]] = []
    best_torque = -1.0
    best_params = {}

    for i, sample in enumerate(samples):
        all_params = {**config.fixed_params, **sample}
        metrics = _compute_metrics(sample, config.fixed_params)

        if metrics.torque_nm and metrics.torque_nm > best_torque:
            best_torque = metrics.torque_nm
            best_params = all_params

        results.append({
            "candidate": i + 1,
            "params": all_params,
            "metrics": metrics,
        })

    # Write CSV log.
    log_dir = Path(log_dir) if log_dir else Path.cwd() / "workspace" / "experiments"
    log_dir.mkdir(parents=True, exist_ok=True)
    csv_path = log_dir / f"{sweep_id}.csv"

    with open(csv_path, "w", newline="") as f:
        if results:
            param_keys = list(results[0]["params"].keys())
            metric_keys = [
                "torque_nm",
                "efficiency_pct",
                "power_factor",
                "saliency",
            ]
            writer = csv.writer(f)
            writer.writerow(param_keys + metric_keys)
            for r in results:
                row = [r["params"].get(k, "") for k in param_keys]
                for mk in metric_keys:
                    row.append(getattr(r["metrics"], mk, ""))
                writer.writerow(row)

    return ExperimentReport(
        experiment_id=sweep_id,
        workflow_name="parameter_sweep",
        inputs={
            "parameters": {
                "ranges": str(config.parameter_ranges),
                "fixed": str(config.fixed_params),
                "num_candidates": config.num_candidates,
            },
            "config_files": [],
            "notes": f"Sweep of {config.num_candidates} candidates",
        },
        outputs={
            "files": [str(csv_path)],
            "logs": [],
        },
        key_metrics={
            "torque": best_torque,
            "efficiency": max(
                (getattr(r["metrics"], "efficiency_pct", 0) or 0) for r in results
            ),
        },
        result="success",
        notes_for_wiki=[
            f"Sweep {sweep_id}: {config.num_candidates} candidates, "
            f"best torque = {best_torque:.1f} Nm"
        ],
    )


def compare_designs(designs: dict[str, ElectromagneticResult]) -> ComparisonResult:
    """Compare multiple candidate designs and return the comparison."""
    return ComparisonResult(designs=designs)
