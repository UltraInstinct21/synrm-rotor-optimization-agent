---
type: motorcad_api
title: "Force Extraction for NVH Analysis"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - force
  - extraction
  - nvh
  - fft
  - skew
  - spatial-harmonics
aliases:
  - force_extraction
  - nvh_force
  - spatial_fft
motor_types:
  - IPMSM
  - SPM
  - SynRM
  - PMaSynRM
  - BLDC
topics:
  - force-extraction
  - fft-analysis
  - spatial-harmonics
  - skew-modeling
  - nvh-analysis
related_pages:
  - "[[pymotorcad-mechanical-force]]"
  - "[[pymotorcad-force-export-motion]]"
confidence: high
verification_status: verified
---

# Force Extraction for NVH Analysis

## Purpose

Extract electromagnetic forces from Motor-CAD's electromagnetic solver for NVH (Noise, Vibration, Harshness) analysis. This includes radial and tangential force densities, spatial/temporal FFT decomposition, 3D force maps, and skew handling.

## Concept

Electromagnetic forces on the stator teeth cause vibration and acoustic noise. Motor-CAD extracts these forces and decomposes them into spatial and temporal harmonics using FFT. The key outputs are:

- **Radial force density** (`Fr`) — the primary source of noise
- **Tangential force density** (`Ft`) — contributes to torque ripple
- **Spatial order** — number of force wave cycles around the airgap per mechanical revolution
- **Temporal order** — frequency of force oscillation relative to shaft speed

## API Methods

### Basic Force Extraction Setup

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Switch to electromagnetic context
mc.show_magnetic_context()

# Set number of torque calculation points per electrical cycle
mc.set_variable("TorquePointsPerCycle", 360)

# Enable multi-force threading for faster computation
mc.set_variable("MultiForceThreading", 1)

# Set number of load points
mc.set_variable("NumLoadPoints", 1)
mc.set_variable("LoadPoint_Speed_Array", [3000])
mc.set_variable("LoadPoint_Torque_Array", [143])

# Run force calculation
mc.do_force_calculation()

# Read radial force density FFT amplitude for spatial order 1
fr_th1 = mc.get_variable("Fr_Density_Stator_FFT_Amplitude_OL_Th1")
print(f"Radial force density (order 1): {fr_th1} Pa")
```

### Key Input Variables

| Variable Name | Description | Units | Default |
|---|---|---|---|
| `TorquePointsPerCycle` | Sample points per electrical cycle | — | 360 |
| `MultiForceThreading` | Enable multi-threaded force calculation | 0/1 | 0 |
| `NumLoadPoints` | Number of operating points | — | 1 |
| `LoadPoint_Speed_Array` | Speed at each load point | RPM | — |
| `LoadPoint_Torque_Array` | Torque at each load point | Nm | — |

### Force Result Variables

| Variable Name | Description | Units |
|---|---|---|
| `Fr_Density_Stator_FFT_Amplitude_OL_ThN` | Radial force density FFT amplitude (order N) | Pa |
| `Ft_Density_Stator_FFT_Amplitude_OL_ThN` | Tangential force density FFT amplitude (order N) | Pa |
| `NVH_NaturalFrequency` | First natural frequency of stator | Hz |

**Note**: Replace `N` with the spatial order number (1, 2, 3, ...).

### 3D Force Map (Space × Time Orders)

```python
# Get 3D force graph: spatial order vs time order vs amplitude
# This provides a complete picture of force harmonics
force_3d = mc.get_magnetic_3d_graph(
    "Fr_Density_Stator_FFT",  # Variable name
    "SpatialOrder",            # X-axis: spatial order
    "TimeOrder",               # Y-axis: time order
    "Amplitude"                # Z-axis: force amplitude
)

# The 3D graph contains:
# - X-axis: spatial orders (0, 1, 2, ..., N/2)
# - Y-axis: time orders (0, 1, 2, ..., M)
# - Z-axis: force density amplitude (Pa)
```

### Read Force at Specific Tooth

```python
# Read force at a specific stator tooth
# N = tooth index, Th = spatial order
fr_tooth_1 = mc.get_variable("Fr_Density_Stator_FFT_Amplitude_T1_Th1")
fr_tooth_5 = mc.get_variable("Fr_Density_Stator_FFT_Amplitude_T5_Th1")
print(f"Tooth 1, order 1: {fr_tooth_1} Pa")
print(f"Tooth 5, order 1: {fr_tooth_5} Pa")
```

## Skew Handling

### Skew Configuration

Skewing the rotor or stator reduces low-order force harmonics. Motor-CAD models skew by dividing the motor into slices and averaging the forces.

```python
# Set skew type
# 0 = no skew
# 1 = continuous skew
# 2 = stepped skew
mc.set_variable("SkewType", 1)  # Continuous skew

# Set number of rotor skew slices
mc.set_variable("RotorSkewSlices", 8)

# Set skew angle (degrees mechanical)
mc.set_variable("RotorSkewAngle", 1.0)  # 1 degree skew

# Run force calculation with skew
mc.do_force_calculation()
```

### Skew Variables

| Variable Name | Description | Values |
|---|---|---|
| `SkewType` | Type of skew modeling | 0 = none, 1 = continuous, 2 = stepped |
| `RotorSkewSlices` | Number of slices for skew integration | 4–16 typical |
| `RotorSkewAngle` | Skew angle in mechanical degrees | 0–5 typical |

### Skew Effects on Force Harmonics

| Spatial Order | Effect of Skew |
|---|---|
| Order 0 | Unchanged (breathing mode) |
| Order 1 | Reduced proportionally to skew angle |
| Order 2 | Reduced, but less than order 1 |
| Order ≥ 3 | Minimal reduction |

**Key insight**: Skewing is most effective at reducing **low-order** spatial harmonics (orders 1–2). Higher-order harmonics are less affected.

## Spatial and Temporal Order Definitions

### Spatial Order

The number of force wave cycles around the airgap per mechanical revolution:

| Spatial Order | Description |
|---|---|
| 0 | Breathing mode (uniform expansion/contraction) |
| 1 | Elliptical deformation |
| 2 | Two-lobe deformation |
| N | N-lobe deformation |

### Temporal Order

The frequency of force oscillation relative to shaft speed:

| Temporal Order | Frequency (at 3000 RPM) |
|---|---|
| 0 | DC (static) |
| 1 | 50 Hz (shaft frequency) |
| 2 | 100 Hz |
| 6 | 300 Hz (6× shaft for 4-pole) |

## Complete NVH Workflow

```python
import ansys.motorcad.core as pymotorcad
import csv

mc = pymotorcad.MotorCAD()
mc.show_magnetic_context()

# Configuration
speeds = [1000, 2000, 3000, 4000, 5000, 6000]
results = []

for speed in speeds:
    mc.set_variable("NumLoadPoints", 1)
    mc.set_variable("LoadPoint_Speed_Array", [speed])
    mc.set_variable("LoadPoint_Torque_Array", [143])
    mc.set_variable("TorquePointsPerCycle", 360)
    mc.set_variable("MultiForceThreading", 1)

    mc.do_force_calculation()

    # Read key force harmonics
    fr_1 = mc.get_variable("Fr_Density_Stator_FFT_Amplitude_OL_Th1")
    fr_2 = mc.get_variable("Fr_Density_Stator_FFT_Amplitude_OL_Th2")
    nat_freq = mc.get_variable("NVH_NaturalFrequency")

    results.append({
        "speed_rpm": speed,
        "fr_order_1_pa": fr_1,
        "fr_order_2_pa": fr_2,
        "natural_freq_hz": nat_freq
    })

# Save results
with open("force_extraction_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)
```

## Key Output Interpretation

### Force Density Magnitude

| Force Density (Pa) | Assessment |
|---|---|
| < 1000 | Low noise risk |
| 1000–5000 | Moderate noise risk |
| 5000–20000 | High noise risk |
| > 20000 | Very high noise risk |

### Resonance Detection

Resonance occurs when a force harmonic frequency matches a structural natural frequency:

```
Force harmonic frequency = Spatial order × Shaft speed / (60 × Poles/2)
```

If this frequency is close to `NVH_NaturalFrequency`, resonance is likely.

## Common Pitfalls

1. **Insufficient sample points**: `TorquePointsPerCycle` too low causes aliasing in FFT
2. **Missing skew**: Always consider skew for production motors
3. **Ignoring order 0**: The breathing mode can be significant in some geometries
4. **Wrong load point**: Forces depend strongly on operating condition; evaluate at worst case

## Related Pages

- [[pymotorcad-mechanical-force]] — Force and NVH calculation setup
- [[pymotorcad-force-export-motion]] — Exporting forces to external structural solvers
- [[pymotorcad-calculations-api]] — All Motor-CAD calculation methods
- [[pymotorcad-stator-geometry]] — Stator geometry affecting force distribution
