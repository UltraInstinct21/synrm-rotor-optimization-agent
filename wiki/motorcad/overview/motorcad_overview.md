---
type: motorcad_overview
name: MotorCAD Overview
aliases: [Ansys Motor-CAD, Motor-CAD]
topics: [motorcad, software, overview]
source_files: ["raw/pymotorcad_markdown/Getting started — pymotorcad-core.md"]
confidence: Verified
---

# MotorCAD Overview

## What Is MotorCAD

Motor-CAD is a dedicated electric motor design software by Ansys that enables multi-physics analysis (electromagnetic, thermal, mechanical) within a single environment.

## Key Features

- **EMagnetic**: Electromagnetic FEA for torque, inductance, flux density
- **Thermal**: Steady-state and transient thermal analysis
- **Mechanical**: Stress analysis for rotating components
- **Lab**: System-level simulation and drive cycle analysis
- **Scripting**: PyMotorCAD for automation

## Workflow Fit

```
Specification → Analytical Design → MotorCAD Model → EM Analysis → Thermal Analysis → Optimization
```

## Modules

| Module | Purpose |
|--------|---------|
| EMagnetic | Electromagnetic analysis (torque, losses, flux) |
| Thermal | Temperature distribution, cooling analysis |
| Mechanical | Stress, deflection, vibration |
| Lab | Drive cycle, control system integration |
| Scripting | Python automation via PyMotorCAD |

## PyMotorCAD

Python interface for Motor-CAD automation:
- `pip install ansys-motorcad-core`
- Requires Motor-CAD v2023R1 or later
- Supports Python 3.9–3.14 on Windows

See [[motorcad/api/index]] for API reference.

## Related Pages

- [[motorcad/api/index]]
- [[motorcad/variables/index]]
- [[motorcad/workflows/index]]
- [[motorcad/outputs/index]]
- [[software/pymotorcad]]
