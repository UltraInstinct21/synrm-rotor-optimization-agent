---
name: motorcad-workflow
description: "How to run Motor-CAD workflows, extract results, and log experiments"
metadata:
  phase: future
---

# motorcad-workflow

## Purpose

Run Motor-CAD simulations, extract key metrics, and log results in the wiki.

## Prerequisites

- Ansys Motor-CAD 2025.1+ installed
- `ansys.motorcad.core` Python package available
- A valid `.mot` model file

## Workflow steps

1. **Load model** — open the `.mot` file via PyMotorCAD.
2. **Set parameters** — use `safe_set` wrappers for geometry/winding/rating changes.
3. **Save checkpoint** — `best_so_far.mot` before changing rotor params.
4. **Run analysis** — electromagnetic or thermal.
5. **Extract results** — torque, efficiency, power factor, Ld/Lq, saliency, losses.
6. **Log experiment** — write to `workspace/wiki/motorcad/experiments/<run>.md`.
7. **Return** `ExperimentReport` with key metrics.

## PyMotorCAD anti-hallucination rules

1. `mc.get_variable_names()` before any `set`/`get` call.
2. Use `safe_get`/`safe_set` wrappers — never raw property access.
3. `show_magnetic_context()` before electromagnetic analysis.
4. Save before changing rotor params.
5. Read all results before changing any parameter.

## Output fields

| Metric | Unit | Notes |
|--------|------|-------|
| Torque | Nm | Average electromagnetic torque |
| Efficiency | % | At rated operating point |
| Power factor | — | cos(φ) |
| Ld | H | d-axis inductance |
| Lq | H | q-axis inductance |
| Saliency | — | Lq/Ld ratio |
| Iron loss | W | Core losses |
| Copper loss | W | Winding losses |
