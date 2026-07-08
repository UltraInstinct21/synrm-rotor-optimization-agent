---
type: motorcad_api
title: "Mechanical Force & NVH Calculation Setup"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - mechanical
  - force
  - nvh
  - vibration
  - load-points
aliases:
  - mechanical_force
  - nvh_analysis
  - force_calculation
motor_types:
  - IPMSM
  - SPM
  - SynRM
  - PMaSynRM
  - SRM
  - IM
  - BLDC
topics:
  - force-calculation
  - nvh-analysis
  - vibration-analysis
  - load-point-setup
related_pages:
  - "[[pymotorcad-force-extraction]]"
  - "[[pymotorcad-calculations-api]]"
confidence: high
verification_status: verified
---

# Mechanical Force & NVH Calculation Setup

## Purpose

Set up force and NVH (Noise, Vibration, Harshness) calculations in Motor-CAD. This enables computation of electromagnetic forces on the stator/rotor, natural frequencies, and force spectral analysis for acoustic noise prediction.

## Concept

NVH analysis in Motor-CAD requires:

1. Defining **load points** (operating conditions) at which forces are calculated
2. Computing **electromagnetic forces** at each load point
3. Performing **FFT analysis** on force waveforms to extract spatial/temporal harmonics
4. Comparing force harmonics against **structural natural frequencies** to assess resonance risk

The load point definition varies by motor type:

| Motor Type | Load Point Definition |
|---|---|
| **BPM** (IPM/SPM) | Speed + Torque |
| **SRM** | Current + Turn-on angle + Turn-off angle |
| **IM** (Induction) | Current + Slip |

## API Methods

### Set Up Load Points

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Number of load points to evaluate
mc.set_variable("NumLoadPoints", 3)

# Load point arrays — define operating conditions
# For BPM motors: Speed (RPM) and Torque (Nm)
mc.set_variable("LoadPoint_Speed_Array", [1000, 3000, 6000])
mc.set_variable("LoadPoint_Torque_Array", [143, 143, 72])

# For SRM motors: Current (A), Turn-on angle (deg), Turn-off angle (deg)
# mc.set_variable("LoadPoint_Current_Array", [10, 20, 30])
# mc.set_variable("LoadPoint_OnAngle_Array", [0, 5, 10])
# mc.set_variable("LoadPoint_OffAngle_Array", [15, 20, 25])

# For IM motors: Current (A) and Slip
# mc.set_variable("LoadPoint_Current_Array", [10, 15, 20])
# mc.set_variable("LoadPoint_Slip_Array", [0.02, 0.04, 0.06])
```

### Run Force Calculation

```python
# Switch to electromagnetic context
mc.show_magnetic_context()

# Run the force calculation
mc.do_force_calculation()

# Read natural frequency result
natural_freq = mc.get_variable("NVH_NaturalFrequency")
print(f"First natural frequency: {natural_freq} Hz")
```

### Read Force Results

```python
# Read radial force density FFT amplitude
# N = stator tooth index, Th = harmonic order
radial_force = mc.get_variable("Fr_Density_Stator_FFT_Amplitude_OL_Th1")
print(f"Radial force density (1st harmonic): {radial_force} Pa")

# Read tangential force density
tangential_force = mc.get_variable("Ft_Density_Stator_FFT_Amplitude_OL_Th1")
print(f"Tangential force density (1st harmonic): {tangential_force} Pa")
```

### Multi-Speed NVH Sweep

```python
import csv

speeds = range(1000, 7001, 500)
results = []

for speed in speeds:
    mc.set_variable("NumLoadPoints", 1)
    mc.set_variable("LoadPoint_Speed_Array", [speed])
    mc.set_variable("LoadPoint_Torque_Array", [143])

    mc.do_force_calculation()

    nat_freq = mc.get_variable("NVH_NaturalFrequency")
    results.append({"speed_rpm": speed, "natural_freq_hz": nat_freq})

with open("nvh_sweep.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)
```

## Key Variables

### Input Variables

| Variable Name | Description | Units | Motor Type |
|---|---|---|---|
| `NumLoadPoints` | Number of operating points to evaluate | — | All |
| `LoadPoint_Speed_Array` | Array of speeds for each load point | RPM | BPM, IM |
| `LoadPoint_Torque_Array` | Array of torques for each load point | Nm | BPM |
| `LoadPoint_Current_Array` | Array of currents for each load point | A | SRM, IM |
| `LoadPoint_OnAngle_Array` | Turn-on angles | deg | SRM |
| `LoadPoint_OffAngle_Array` | Turn-off angles | deg | SRM |
| `LoadPoint_Slip_Array` | Slip values | — | IM |

### Result Variables

| Variable Name | Description | Units |
|---|---|---|
| `NVH_NaturalFrequency` | First natural frequency of stator | Hz |
| `Fr_Density_Stator_FFT_Amplitude_OL_ThN` | Radial force density FFT amplitude | Pa |
| `Ft_Density_Stator_FFT_Amplitude_OL_ThN` | Tangential force density FFT amplitude | Pa |

## Operating Point Configuration by Motor Type

### BPM (IPM/SPM)

```python
# BPM requires speed and torque at each load point
mc.set_variable("NumLoadPoints", 2)
mc.set_variable("LoadPoint_Speed_Array", [3000, 6000])
mc.set_variable("LoadPoint_Torque_Array", [143, 72])
```

### SRM

```python
# SRM requires current and switching angles
mc.set_variable("NumLoadPoints", 2)
mc.set_variable("LoadPoint_Current_Array", [15, 25])
mc.set_variable("LoadPoint_OnAngle_Array", [0, 5])
mc.set_variable("LoadPoint_OffAngle_Array", [15, 20])
```

### Induction Motor (IM)

```python
# IM requires current and slip
mc.set_variable("NumLoadPoints", 2)
mc.set_variable("LoadPoint_Current_Array", [12, 18])
mc.set_variable("LoadPoint_Slip_Array", [0.03, 0.05])
```

## NVH Assessment

### Resonance Risk

The NVH analysis compares electromagnetic force harmonics against structural natural frequencies. Resonance occurs when:

```
Force harmonic frequency ≈ Natural frequency ± tolerance
```

| Risk Level | Condition | Action |
|---|---|---|
| Low | Force harmonics far from natural freq | No action needed |
| Medium | Force harmonics near natural freq | Consider design modification |
| High | Force harmonic matches natural freq | Resonance — redesign required |

### Common NVH Mitigation Strategies

1. **Skew the rotor or stator** — reduces low-order force harmonics (see [[pymotorcad-force-extraction]])
2. **Modify slot/pole combination** — avoid problematic harmonics
3. **Increase stator stiffness** — raises natural frequency away from excitation
4. **Add damping** — through winding impregnation or structural modifications

## Common Pitfalls

1. **Wrong load point definition**: Ensure the load point arrays match the motor type
2. **Single speed check**: Always sweep across the full speed range
3. **Missing torque**: Force calculation requires both speed and torque for BPM motors
4. **Ignoring higher harmonics**: The 1st harmonic is not always the most critical

## Related Pages

- [[pymotorcad-force-extraction]] — Force extraction and FFT analysis details
- [[pymotorcad-calculations-api]] — All Motor-CAD calculation methods
- [[pymotorcad-mechanical-stress]] — Mechanical stress analysis
- [[pymotorcad-force-export-motion]] — Exporting forces to structural solvers
