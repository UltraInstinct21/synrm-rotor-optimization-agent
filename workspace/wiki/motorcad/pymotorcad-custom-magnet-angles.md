---
type: pymotorcad_example
title: "PyMotorCAD Custom Magnet Angles"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - magnet
  - angles
  - halbach
  - spm
  - adaptive-geometry
  - magnetization
  - custom
aliases:
  - custom_magnet_angles
  - halbach_magnetization
motor_types: ["SPM", "BLDC", "IPMSM"]
confidence: verified
---

# PyMotorCAD Custom Magnet Angles

## Overview

This page documents how to define **custom magnet angles** for a Surface-mounted Permanent Magnet (SPM) machine using a Halbach array magnetisation pattern. Standard SPM machines use radial or parallel magnetisation, but a Halbach array arranges magnet segments with rotating magnetisation directions to concentrate flux on one side (airgap side) while cancelling it on the other (back-iron side). This improves airgap flux density, reduces back-iron thickness, and can increase torque density.

**Template:** a1 (SPM rotor)

**Requirements:** MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+

---

## Key Variables

| Variable | MotorCAD Name | Description | Value/Units |
|---|---|---|---|
| Circumferential Segments | `CircumferentialSegments` | Number of magnet segments per pole | integer |
| Magnetisation Type | `Magnetization` | Magnetisation method selector | 2 = Halbach |
| Halbach Magnetisation | `HalbachMagnetization` | Halbach variant selector | 1 = standard Halbach |

---

## Adaptive Parameters

| Parameter | Description |
|---|---|
| Magnet angle offset N | Angular offset applied to the Nth magnet segment to define its magnetisation direction |

Each magnet segment has an independently controllable magnetisation angle. The adaptive parameter allows per-segment angle offsets that deviate from the default radial/parallel pattern.

---

## Halbach Array Theory

A Halbach array arranges magnet segments so that the magnetisation vector rotates progressively around the rotor circumference:

```
Segment 1:  0°   (radial outward)
Segment 2:  45°  (tangential)
Segment 3:  90°  (radial inward)
Segment 4:  135° (tangential)
...
```

For a 4-segment Halbach with `CircumferentialSegments=4` and `Magnetization=2`:

| Segment | Angle Offset | Magnetisation Direction |
|---|---|---|
| 1 | 0° | Radial outward |
| 2 | 90° | Tangential (clockwise) |
| 3 | 180° | Radial inward |
| 4 | 270° | Tangential (counter-clockwise) |

The net effect: flux is **added** on the airgap side and **cancelled** on the back-iron side.

---

## Geometry Logic

### Symmetric Segments

For a pole-pair with `N` circumferential segments, the angular span of each segment is:

```
segment_span = pole_arc / N
```

The segments are symmetric about the pole centre. For even `N`, segments are paired left/right of the pole axis.

### Offset Application

The `Magnet angle offset N` parameter applies an angular offset to the magnetisation direction of each segment:

- **Left magnets** (segments on the leading side of the pole): offset applied relative to the local radial direction
- **Right magnets** (segments on the trailing side of the pole): offset applied symmetrically

This allows fine-tuning of the Halbach pattern without changing the segment geometry.

---

## Complete Workflow

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"path\to\spm_model.mot")
mc.show_magnetic_context()

# Set Halbach configuration
mc.set_variable("CircumferentialSegments", 4)
mc.set_variable("Magnetization", 2)            # Halbach
mc.set_variable("HalbachMagnetization", 1)     # Standard Halbach

# Reset adaptive geometry
mc.reset_adaptive_geometry()

# Get magnet regions and apply custom angle offsets
# (Specific region names depend on template a1 geometry)
for seg in range(4):
    region_name = f"Magnet_Seg_{seg + 1}"
    region = mc.get_region(region_name)

    # Apply angle offset via adaptive parameters
    # The exact parameter names depend on the template
    mc.set_adaptive_parameter(f"Magnet_angle_offset_{seg + 1}", seg * 90.0)

    mc.set_region(region)

# Run EMag calculation
mc.do_magnetic_calculation()

# Compare results
torque = mc.get_variable("ShaftTorque")
flux_density = mc.get_variable("AirgapFluxDensity")
print(f"Halbach torque: {torque:.2f} Nm")
print(f"Airgap B: {flux_density:.4f} T")
```

---

## Comparison: Radial vs Halbach

| Property | Radial Magnetisation | Halbach Array |
|---|---|---|
| Airgap flux density | Base | ~1.4× higher (theoretical √2×) |
| Back-iron thickness | Full | Can be reduced significantly |
| Cogging torque | Standard | Can be reduced with proper segmentation |
| Manufacturing complexity | Simple | Higher (multiple magnetisation directions) |
| Cost | Lower | Higher (more segments, complex magnetisation) |
| Applications | General purpose | High-performance, weight-constrained |

---

## Design Considerations

- **Number of segments** — More segments approximate a continuous Halbach rotation more closely but increase manufacturing cost. 3–4 segments per pole is typical.
- **Segment arc** — Each segment spans `pole_arc / N`. The segment arc affects the flux concentration ratio.
- **Airgap flux shape** — A perfect Halbach produces a near-sinusoidal airgap flux distribution, reducing harmonics and torque ripple.
- **Back-iron reduction** — The cancelled back-iron flux allows thinner yoke, reducing motor diameter and weight.
- **Material** — NdFeB is typical for Halbach arrays due to high remanence. Ferrite Halbach arrays are possible but offer less benefit.

---

## Common Pitfalls

1. **Wrong `Magnetization` value** — Must be set to `2` for Halbach. Value `1` is radial, `0` is parallel.
2. **Segment count mismatch** — `CircumferentialSegments` must match the actual number of magnet regions in the model.
3. **Angle offset units** — Offsets are in **electrical degrees**, not mechanical. For a 4-pole machine, 1 mechanical degree = 2 electrical degrees.
4. **Symmetry breaking** — Incorrect Halbach angle offsets can break the magnetic symmetry required for EMag boundary conditions.
5. **Region naming** — Magnet region names are template-dependent. Use `mc.get_variable_names()` or inspect the model to find exact names.

---

## Related Pages

- [[pymotorcad-adaptive-geometry]] — Full adaptive template API
- [[pymotorcad-geometry-shapes]] — Shape primitives for magnet segments
- [[pymotorcad-geometry-objects]] — Region, RegionMagnet, Coordinate types
- [[pymotorcad-adaptive-templates-guide]] — Adaptive templates user guide
- [[pymotorcad-bezier-rotor-pockets]] — Bezier curves for rotor geometry
- [[pymotorcad-custom-dxf-geometry]] — DXF import for custom magnet shapes

---

## Tags

#pymotorcad #motorcad #magnet #angles #halbach #spm #adaptive-geometry #magnetization #custom #bldc
