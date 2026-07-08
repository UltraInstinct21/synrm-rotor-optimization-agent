---
type: pymotorcad_example
title: "PyMotorCAD Parametric Sweep"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - parametric-sweep
  - sync-machine
  - skew
  - field-current
  - nvh
  - sweep
  - optimization
aliases:
  - parametric_sweep
  - sweep_example
motor_types: ["SYNC", "SynRM", "IPMSM"]
confidence: verified
---

# PyMotorCAD Parametric Sweep

## Overview

This page documents a complete parametric sweep workflow for a SYNC (synchronous) machine using PyMotorCAD. The example demonstrates a **2D sweep** across `skew_angles` and `field_currents`, recording NVH radiated power levels as the output metric. Parametric sweeps are fundamental to motor design optimization — they map the design space and identify sensitivities before committing to a single design point.

**Requirements:** MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+

---

## Key Variables

| Variable | MotorCAD Name | Description | Units |
|---|---|---|---|
| Skew Type | `SkewType` | Skew implementation method (e.g. continuous, step) | enum |
| Stator Skew | `StatorSkew` | Stator skew angle | mechanical degrees |
| DC Field Current | `DCFieldCurrent` | DC field winding current for SYNC excitation | A |

These variables are set via `mc.set_variable()` before each calculation iteration.

---

## Workflow

### 1. Initialise MotorCAD Connection

```python
import ansys.motorcad.core as pymotorcad
import numpy as np
import csv
import time

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"path\to\model.mot")
```

### 2. Define Sweep Grid

```python
skew_angles = np.linspace(0, 10, 11)       # 0 to 10 deg, 11 points
field_currents = np.linspace(0, 50, 11)     # 0 to 50 A, 11 points

results = []
```

### 3. Execute 2D Sweep

```python
mc.show_magnetic_context()

for skew in skew_angles:
    for field_cur in field_currents:
        # Set sweep variables
        mc.set_variable("SkewType", 1)              # continuous skew
        mc.set_variable("StatorSkew", skew)
        mc.set_variable("DCFieldCurrent", field_cur)

        # Run EMag calculation
        mc.do_magnetic_calculation()

        # Record results
        torque = mc.get_variable("ShaftTorque")
        efficiency = mc.get_variable("Efficiency")
        nvh_power = mc.get_variable("NVHRadiatedPower")

        results.append({
            "skew_angle": skew,
            "field_current": field_cur,
            "torque": torque,
            "efficiency": efficiency,
            "nvh_radiated_power": nvh_power,
        })

        print(f"skew={skew:.1f} deg, field={field_cur:.1f} A -> "
              f"torque={torque:.2f} Nm, NVH={nvh_power:.4f} W")
```

### 4. Log Results to CSV

```python
csv_path = r"D:\SRM\Motor_CAD\ScriptFiles\parametric_sweep_results.csv"
fieldnames = list(results[0].keys())

with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Results saved to {csv_path}")
```

### 5. Identify Optimal Design Point

```python
# Find minimum NVH radiated power
best = min(results, key=lambda r: r["nvh_radiated_power"])
print(f"\nBest design: skew={best['skew_angle']:.1f} deg, "
      f"field={best['field_current']:.1f} A -> "
      f"NVH={best['nvh_radiated_power']:.4f} W")
```

---

## Result Metrics

| Metric | Variable Name | Description |
|---|---|---|
| Shaft Torque | `ShaftTorque` | Output torque (Nm) |
| Efficiency | `Efficiency` | Overall efficiency (%) |
| NVH Radiated Power | `NVHRadiatedPower` | Acoustic radiated power (W) |

For any variable not listed, use `mc.get_variable_names()` to discover the exact name before use. See [[pymotorcad-general-api]] for variable discovery patterns.

---

## Design Considerations

- **Skew angle** reduces torque ripple and NVH but also reduces fundamental torque. There is an optimal non-zero skew angle.
- **Field current** in a SYNC machine controls flux level. Higher field current increases flux but also increases copper loss and may saturate the core.
- The interaction between skew and field current is non-linear — a 2D sweep captures this coupling.
- NVH radiated power is a key metric for automotive and industrial applications where acoustic noise is a constraint.

---

## Common Pitfalls

1. **Missing `show_magnetic_context()`** — EMag methods will fail if the magnetic context is not active.
2. **Reading results after modifying geometry** — Motor-CAD results refer to the last calculation. Always read all outputs before calling `set_variable()` for the next iteration.
3. **Variable name typos** — MotorCAD variable names are exact internal strings. Use `mc.get_variable_names()` to verify. See [[pymotorcad-general-api]].
4. **Skew type not set** — `SkewType` must be set before `StatorSkew` is meaningful.

---

## Related Pages

- [[pymotorcad-calculations-api]] — EMag calculation methods
- [[pymotorcad-graphs-api]] — Graph data retrieval for NVH and other post-processing outputs
- [[pymotorcad-general-api]] — Variable get/set, file I/O, result retrieval
- [[pymotorcad-emag-example]] — Basic EMag calculation example
- [[pymotorcad-adaptive-templates-guide]] — Adaptive geometry workflow
- [[pymotorcad-motorcad-api]] — MotorCAD class constructor and connection

---

## Tags

#pymotorcad #motorcad #parametric-sweep #sync-machine #skew #field-current #nvh #sweep #optimization #emag
