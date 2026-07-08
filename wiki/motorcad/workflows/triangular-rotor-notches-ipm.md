---
type: motorcad_workflow
name: "Triangular Rotor Notches for IPM"
purpose: "Create triangular rotor notches to improve NVH performance"
prerequisites: ["Motor-CAD v2024.1.2+", "e9 IPM template"]
source_files: ["Triangular Rotor Notches for IPM — pymotorcad-core.md"]
confidence: Verified
---

# Triangular Rotor Notches for IPM

## Purpose

Add triangular notches to the rotor surface of IPM motors to improve NVH (noise, vibration, harshness) performance.

## Prerequisites

- Motor-CAD v2024.1.2 or later
- PyMotorCAD v0.4.1 or later

## Adaptive Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `Notch Angle` | -4 | Angular offset of notches (deg) |
| `Notch Sweep` | 5 | Angular width of each notch (deg) |
| `Notch Depth` | 1 | Radial depth of notch (mm) |
| `Notches per Pole` | 2 | Number of notches per pole |

## Step-by-Step Procedure

### 1. Set Parameters

```python
mc.set_adaptive_parameter_default("Notch Angle", -4)
mc.set_adaptive_parameter_default("Notch Sweep", 5)
mc.set_adaptive_parameter_default("Notch Depth", 1)
mc.set_adaptive_parameter_default("Notches per Pole", 2)
```

### 2. Create Notches

```python
for notch_loop in range(number_notches):
    notch_name = "Rotor_Notch_" + str(notch_loop + 1)
    notch_centre_angle = ((2 * notch_loop) + 1) * (duplication_angle / (2 * number_notches))

    # Apply offset angle
    if notch_centre_angle < duplication_angle / 2:
        notch_centre_angle = notch_centre_angle - notch_angle
    if notch_centre_angle > duplication_angle / 2:
        notch_centre_angle = notch_centre_angle + notch_angle

    # Generate triangular notch using geometry_shapes helper
    notch = triangular_notch(
        rotor_radius, notch_angular_width, notch_centre_angle, notch_depth,
        region_type=RegionType.rotor_pocket,
    )
    notch.name = notch_name
    notch.colour = (255, 255, 255)
    notch.duplications = rotor_region.duplications
    notch.material = "Air"
    notch.parent = rotor_region  # Motor-CAD handles subtraction

    if notch.is_closed():
        mc.set_region(notch)
```

## Key Function

```python
from ansys.motorcad.core.geometry_shapes import triangular_notch
```

`triangular_notch(radius, angular_width, centre_angle, depth)` — creates a complete triangular notch region ready to set.

## Pitfalls

- Notch angle is clamped to prevent crossing symmetry boundaries
- Notch angle is clamped to prevent overlap at pole center
- Entities must be anticlockwise for correct geometry

## Related Pages

- [[motorcad/api/geometry-shapes]] — triangular_notch, square, eq_triangle
- [[motorcad/api/geometry-objects-functions]] — Region properties
- [[motorcad/workflows/triangular-stator-notches]] — Stator variant
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
