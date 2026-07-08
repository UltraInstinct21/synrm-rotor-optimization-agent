---
type: motorcad_api
title: "Mechanical Stress Analysis — Rotor Structural Analysis"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - mechanical
  - stress
  - structural
  - safety-factor
  - rotor
aliases:
  - mechanical_stress
  - stress_analysis
  - structural_analysis
motor_types:
  - IPMSM
  - SynRM
  - PMaSynRM
  - SPM
  - BLDC
topics:
  - mechanical-analysis
  - structural-integrity
  - safety-factor
  - rotor-lamination
related_pages:
  - "[[pymotorcad-mechanical-force]]"
  - "[[pymotorcad-calculations-api]]"
confidence: high
verification_status: verified
---

# Mechanical Stress Analysis — Rotor Structural Analysis

## Purpose

Perform mechanical stress analysis on rotor laminations due to centrifugal forces at high speed. This analysis is critical for ensuring the rotor structure (bridges, webs, ribs) can withstand the mechanical loads at maximum operating speed.

## Concept

At high rotational speeds, the rotor lamination experiences centrifugal stress. The mechanical stress analysis in Motor-CAD computes:

- **Maximum Von Mises stress** in the rotor lamination
- **Stress distribution** across the rotor geometry
- **Safety factor** = Yield Stress / Maximum Stress

The safety factor must be greater than 1.0 (typically > 1.5 for production motors) to ensure structural integrity.

## API Methods

### Run Mechanical Stress Calculation

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Switch to mechanical context
mc.show_mechanical_context()

# Set rotor speed (RPM)
mc.set_variable("Shaft_Speed_[RPM]", 6000)  # Maximum speed

# Run the stress calculation
mc.do_mechanical_calculation()

# Read results
max_stress = mc.get_variable("MaxStress_RotorLam")
yield_stress = mc.get_variable("YieldStress_RotorLam")

# Calculate safety factor
safety_factor = yield_stress / max_stress
print(f"Max stress: {max_stress} MPa")
print(f"Yield stress: {yield_stress} MPa")
print(f"Safety factor: {safety_factor:.2f}")
```

### Set Material Properties

```python
# Set rotor lamination yield stress (MPa)
mc.set_variable("YieldStress_RotorLam", 450.0)

# Set material density (kg/m³) — needed for centrifugal force calculation
mc.set_variable("Density_RotorLam", 7650.0)

# Set Young's modulus (GPa)
mc.set_variable("YoungsModulus_RotorLam", 200.0)
```

### Batch Stress Evaluation at Multiple Speeds

```python
import csv

speeds = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
results = []

for speed in speeds:
    mc.set_variable("Shaft_Speed_[RPM]", speed)
    mc.do_mechanical_calculation()

    max_stress = mc.get_variable("MaxStress_RotorLam")
    yield_stress = mc.get_variable("YieldStress_RotorLam")
    safety_factor = yield_stress / max_stress

    results.append({
        "speed_rpm": speed,
        "max_stress_mpa": max_stress,
        "yield_stress_mpa": yield_stress,
        "safety_factor": safety_factor
    })

# Save results
with open("stress_analysis.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)
```

## Key Variables

| Variable Name | Description | Units | Typical Range |
|---|---|---|---|
| `Shaft_Speed_[RPM]` | Rotor rotational speed | RPM | 0–20000 |
| `YieldStress_RotorLam` | Yield strength of rotor lamination | MPa | 300–600 |
| `MaxStress_RotorLam` | Maximum computed Von Mises stress | MPa | varies |
| `Density_RotorLam` | Rotor lamination density | kg/m³ | 7600–7800 |
| `YoungsModulus_RotorLam` | Young's modulus of rotor lamination | GPa | 180–210 |

## Safety Factor Calculation

```
Safety Factor = YieldStress_RotorLam / MaxStress_RotorLam
```

| Safety Factor | Status | Action |
|---|---|---|
| > 2.0 | Excellent | Design is robust |
| 1.5–2.0 | Good | Acceptable for production |
| 1.0–1.5 | Marginal | Consider increasing bridge thickness |
| < 1.0 | FAIL | Rotor will yield at this speed |

## Critical Locations for Stress

The maximum stress typically occurs at:

1. **Bridge regions** — thin sections connecting barrier segments to the rotor OD
2. **Web regions** — sections between adjacent barriers
3. **Rib regions** — thin material between barrier tips
4. **Shaft interface** — where the rotor meets the shaft

See [[pymotorcad-stress-sampling]] for detailed stress sampling at specific locations.

## Design Implications

### How Geometry Affects Stress

| Geometry Change | Effect on Stress |
|---|---|
| Thicker bridges | Lower stress, lower saliency |
| Thinner bridges | Higher stress, higher saliency |
| More barriers | More bridges to stress, complex tradeoff |
| Larger rotor OD | Higher peripheral speed → higher stress |
| Higher shaft speed | Stress scales with speed² |

### Material Selection

| Material | Yield Stress (MPa) | Density (kg/m³) | Notes |
|---|---|---|---|
| 50C250 | 450 | 7650 | Common motor lamination |
| M19 | 380 | 7650 | Standard electrical steel |
| M27 | 350 | 7650 | Higher silicon, lower loss |
| Maraging steel | 1800 | 8000 | Premium high-speed rotors |

## Common Pitfalls

1. **Speed too high**: Always run stress at maximum operating speed, not rated speed
2. **Wrong material yield stress**: Ensure the yield stress matches the actual lamination grade
3. **Missing density**: Centrifugal force depends on density; omitting it gives zero stress
4. **Single-point check**: Always sweep across the full speed range, not just rated speed

## Related Pages

- [[pymotorcad-mechanical-force]] — Force and NVH calculations
- [[pymotorcad-calculations-api]] — All calculation methods in Motor-CAD
- [[pymotorcad-stress-sampling]] — Detailed stress sampling at specific bridge locations
- [[pymotorcad-stress-postprocessing]] — Post-processing with plastic corrections
- [[pymotorcad-material-mesh]] — Material mesh and lamination settings
