---
type: motorcad_api
title: "Stress Sampling — Rotor Bridge Stress with Plastic Corrections"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - stress
  - sampling
  - rotor
  - bridges
  - plastic-correction
  - neuber
  - glinka
aliases:
  - stress_sampling
  - bridge_stress
  - rotor_stress_sampling
motor_types:
  - IPMSM
  - SynRM
  - PMaSynRM
  - SPM
topics:
  - stress-sampling
  - plastic-correction
  - rotor-bridges
  - structural-analysis
related_pages:
  - "[[pymotorcad-mechanical-stress]]"
  - "[[pymotorcad-stress-postprocessing]]"
confidence: high
verification_status: verified
---

# Stress Sampling — Rotor Bridge Stress with Plastic Corrections

## Purpose

Sample stresses at specific locations in rotor bridges and webs, then apply plastic corrections (Neuber or Glinka) to estimate actual stress accounting for local plastic deformation at stress concentrations.

## Concept

In rotor laminations, the **bridges** (thin sections between barriers and rotor OD) and **webs** (sections between adjacent barriers) are the most mechanically critical regions. Motor-CAD provides a dedicated stress sampling feature that:

1. Places **15 hardcoded sample points** per bridge/web location
2. Reads the local stress state (Sx, Sy, Txy, principal stresses, Von Mises)
3. Applies **plastic corrections** to account for stress concentrations

### Supported Rotor Types

| Rotor Type | Code | Variable Arrays |
|---|---|---|
| V-web | `rotor_type = 11` | `BridgeThickness_Array`, `WebThickness_Array`, `PoleArc_Array` |
| U-shape | `rotor_type = 13` | `UShape_BridgeThickness_Array`, `UShape_WebThickness_Array` |

## API Methods

### Run Stress Sampling

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Set rotor speed for the stress calculation
mc.set_variable("Shaft_Speed_[RPM]", 6000)

# Run stress sampling
mc.do_stress_sampling()

# Read sampled stress data
# 15 sample points per bridge location
sampled_stresses = mc.get_variable("StressSamplingResults")
print(f"Sampled stresses: {sampled_stresses}")
```

### V-web Rotor Geometry Setup (rotor_type=11)

```python
# V-web rotor geometry parameters
# Bridge thicknesses (mm) — thin sections at barrier ends
mc.set_variable("BridgeThickness_Array", [3.0, 4.0, 5.0])

# Web thicknesses (mm) — sections between barriers
mc.set_variable("WebThickness_Array", [20.0, 30.0, 40.0])

# Pole arc angles (deg) — angular extent of each barrier layer
mc.set_variable("PoleArc_Array", [30.0, 25.0, 20.0])

# Run stress sampling
mc.do_stress_sampling()
```

### U-shape Rotor Geometry Setup (rotor_type=13)

```python
# U-shape rotor geometry parameters
# Bridge thicknesses (mm)
mc.set_variable("UShape_BridgeThickness_Array", [3.5, 4.5])

# Web thicknesses (mm)
mc.set_variable("UShape_WebThickness_Array", [25.0, 35.0])

# Run stress sampling
mc.do_stress_sampling()
```

### Apply Plastic Corrections

```python
# Apply Neuber correction for local plasticity
# This accounts for stress concentration at notch roots
mc.apply_neuber_correction()

# Or apply Glinka correction (energy-based)
mc.apply_glinka_correction()

# Read corrected stress values
corrected_stress = mc.get_variable("StressSamplingResults_Corrected")
print(f"Corrected stresses: {corrected_stress}")
```

## Sample Point Layout

Each bridge/web location has **15 hardcoded sample points** distributed across the cross-section:

```
Bridge Cross-Section (15 points)
┌─────────────────────────────┐
│  ○  ○  ○  ○  ○  │  ← Surface (5 points)
│  ○  ○  ○  ○  ○  │  ← Mid-section (5 points)
│  ○  ○  ○  ○  ○  │  ← Interior (5 points)
└─────────────────────────────┘
```

The sample points capture:

- **Surface stresses** — highest stress concentration
- **Mid-section stresses** — average stress state
- **Interior stresses** — baseline stress level

## Plastic Correction Methods

### Neuber Correction

The Neuber rule relates nominal stress to actual stress accounting for local plasticity:

```
ε_actual × σ_actual = ε_nominal × σ_nominal
```

**When to use**: Notch-root plasticity, sharp stress concentrations

**Assumptions**:
- Uniaxial stress state
- Monotonic loading
- Neuber's constant is material-dependent

### Glinka Correction

The Glinka (energy-based) correction accounts for plastic strain energy:

```
σ_actual = σ_nominal × √(1 + (σ_nominal / σ_yield)² × Kt²)
```

**When to use**: Multiaxial stress states, gradual stress concentrations

**Assumptions**:
- Plane stress or plane strain
- Isotropic hardening
- Small-scale yielding

### When to Use Which

| Condition | Recommended Method |
|---|---|
| Sharp notch (high Kt) | Neuber |
| Gradual stress concentration | Glinka |
| Unknown | Try both, compare results |
| Conservative estimate | Neuber (typically more conservative) |

## Key Variables

### Geometry Variables (V-web)

| Variable Name | Description | Units |
|---|---|---|
| `BridgeThickness_Array` | Bridge thickness per layer | mm |
| `WebThickness_Array` | Web thickness per layer | mm |
| `PoleArc_Array` | Pole arc angle per layer | deg |

### Geometry Variables (U-shape)

| Variable Name | Description | Units |
|---|---|---|
| `UShape_BridgeThickness_Array` | U-shape bridge thickness per layer | mm |
| `UShape_WebThickness_Array` | U-shape web thickness per layer | mm |

### Operating Variables

| Variable Name | Description | Units |
|---|---|---|
| `Shaft_Speed_[RPM]` | Rotor speed | RPM |
| `YieldStress_RotorLam` | Yield strength of rotor lamination | MPa |

## Design Implications

### Bridge Thickness Tradeoffs

| Thicker Bridges | Thinner Bridges |
|---|---|
| Lower stress | Higher stress |
| Lower saliency | Higher saliency |
| Less torque ripple | More torque ripple |
| More mechanical robustness | Risk of yielding |

### Web Thickness Tradeoffs

| Thicker Webs | Thinner Webs |
|---|---|
| Higher stiffness | Lower stiffness |
| Higher stress in bridges | Stress distributed differently |
| More rotor mass | Less rotor mass |

## Common Pitfalls

1. **Wrong rotor type**: Ensure `rotor_type` matches the geometry (11 for V-web, 13 for U-shape)
2. **Missing plastic correction**: Without correction, stresses may be underestimated at stress concentrations
3. **Wrong sample location**: The 15 points are hardcoded; they may not capture the true maximum stress in all geometries
4. **Single speed check**: Always evaluate at maximum operating speed

## Related Pages

- [[pymotorcad-mechanical-stress]] — General mechanical stress analysis
- [[pymotorcad-stress-postprocessing]] — Post-processing with Element/StressRegion classes
- [[pymotorcad-material-mesh]] — Material mesh and lamination settings
- [[pymotorcad-mechanical-force]] — Force and NVH calculations
