---
type: pymotorcad_example
title: Tapered Rotor Tooth Bar for Induction Motor
source: PyMotorCAD Official Documentation — Adaptive Geometry Example i6a
tags:
  - pymotorcad
  - adaptive-geometry
  - rotor
  - induction-motor
  - tooth-bar
  - tapered
  - geometry
---

# Tapered Rotor Tooth Bar for Induction Motor

Adaptive geometry example demonstrating how to convert an induction motor rotor bar from parallel-sided to tapered geometry by modifying the rotor tooth width at the bottom.

---

## Template Reference

- **Motor-CAD Template:** `i6a`
- **Example Type:** Adaptive geometry modification — rotor tooth bar taper
- **Use Case:** Induction motor rotor bar geometry optimisation

---

## Overview

In induction motor (IM) rotors, the rotor bars sit in slots cut into the rotor lamination. The default geometry often uses parallel-sided bars (constant slot width). Tapering the bar — making it wider at the bottom (靠近 shaft) and narrower at the top (靠近 airgap) — can:

- **Improve starting torque** by increasing bar cross-section at the high-current region
- **Reduce rotor losses** by optimising current distribution
- **Improve thermal performance** by increasing copper volume near the rotor core

This example modifies the rotor tooth bar geometry using Motor-CAD's adaptive geometry system.

---

## Key Variables

| Variable | Motor-CAD Name | Description |
|---|---|---|
| Rotor Tooth Width (Top) | `Rotor_Tooth_Width` | Width of the tooth at the airgap side (mm) |
| Rotor Tooth Width (Bottom) | `Rotor_Tooth_Width_T` | Width of the tooth at the shaft side (mm) |

The taper is defined by the difference between `Rotor_Tooth_Width` (top) and `Rotor_Tooth_Width_T` (bottom).

---

## Adaptive Parameter

| Parameter | Description |
|---|---|
| Rotor Tooth Width Bottom | Controls the bottom width of the tooth bar, defining the taper angle |

```python
mc.set_variable("Rotor_Tooth_Width_T", 8.0)  # bottom width in mm
```

When `Rotor_Tooth_Width_T` differs from `Rotor_Tooth_Width`, the bar has a trapezoidal cross-section.

---

## Helper Function: `chord_angle()`

The `chord_angle()` function calculates the angular span required to accommodate a chord of a given length at a specified radius.

```python
import math

def chord_angle(cord_length, r):
    """Calculate the angular span for a chord of given length at radius r.

    Parameters
    ----------
    cord_length : float
        Chord length (mm)
    r : float
        Radius at which the chord is measured (mm)

    Returns
    -------
    float
        Angular span in degrees
    """
    return 2.0 * math.degrees(math.asin(cord_length / (2.0 * r)))
```

### Usage

This function is used to convert linear tooth widths into angular spans at different radial positions:

```python
# Angular span of tooth at top (airgap radius)
r_top = 107.0  # mm (airgap radius)
width_top = 6.0  # mm
angle_top = chord_angle(width_top, r_top)

# Angular span of tooth at bottom (near shaft)
r_bottom = 50.0  # mm
width_bottom = 8.0  # mm
angle_bottom = chord_angle(width_bottom, r_bottom)
```

The difference between `angle_top` and `angle_bottom` defines the taper angle of the bar.

---

## Code Example

```python
import math
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate, Line, Arc, EntityList

mc = pymotorcad.MotorCAD()

def chord_angle(cord_length, r):
    """Angular span (degrees) for a chord of given length at radius r."""
    return 2.0 * math.degrees(math.asin(cord_length / (2.0 * r)))

# Parameters
airgap_radius = mc.get_variable("Stator_bore") / 2.0  # mm
shaft_radius = mc.get_variable("Shaft_Dia") / 2.0     # mm
bar_slot_depth = airgap_radius - shaft_radius           # mm

# Tooth widths
width_top = 6.0     # mm at airgap side
width_bottom = 8.0  # mm at shaft side (tapered)

# Calculate angular spans
angle_top = chord_angle(width_top, airgap_radius)
angle_bottom = chord_angle(width_bottom, shaft_radius)

# Build tapered bar region (anticlockwise)
entities = EntityList()

# Top left corner (airgap side)
tl = Coordinate(r=airgap_radius, th=-angle_top / 2.0)
tr = Coordinate(r=airgap_radius, th=angle_top / 2.0)

# Bottom corners (shaft side)
bl = Coordinate(r=shaft_radius, th=-angle_bottom / 2.0)
br = Coordinate(r=shaft_radius, th=angle_bottom / 2.0)

# Add entities in anticlockwise order
entities.add(Line(tl, tr))          # top (airgap side)
entities.add(Line(tr, br))          # right flank (tapered)
entities.add(Line(br, bl))          # bottom (shaft side)
entities.add(Line(bl, tl))          # left flank (tapered)

# Validate and set region
if mc.geometry.get_entities_have_common_coordinate(entities):
    mc.geometry.set_region(entities)
    print("Tapered bar region set successfully")
else:
    print("Warning: region not closed")
```

---

## Workflow Steps

1. **Read rotor dimensions** — get `Stator_bore` and `Shaft_Dia` to compute radii
2. **Define tooth widths** — set top (airgap) and bottom (shaft) widths
3. **Calculate angular spans** — use `chord_angle()` to convert linear widths to angles at each radius
4. **Build region geometry** — construct Lines connecting the four corners
5. **Enforce anticlockwise order** — ensure entities are added in the correct winding sequence
6. **Validate closure** — check that the region is closed before setting
7. **Write to Motor-CAD** — `set_region()` to inject the tapered bar geometry
8. **Run calculation** — `do_magnetic_calculation()` to evaluate electromagnetic performance

---

## Taper Angle Calculation

The taper angle `α` of the bar is:

```
α = atan((width_bottom - width_top) / (2 × bar_slot_depth))
```

| Taper | Width Bottom | Width Top | Taper Angle |
|---|---|---|---|
| Parallel | 6.0 mm | 6.0 mm | 0° |
| Mild taper | 7.0 mm | 6.0 mm | ~1.5° |
| Moderate taper | 8.0 mm | 6.0 mm | ~3.0° |
| Aggressive taper | 10.0 mm | 6.0 mm | ~6.0° |

---

## Design Considerations

### Electromagnetic
- Tapered bars increase copper cross-section at the bottom → lower resistance → higher starting torque
- May increase rotor leakage inductance slightly
- Optimal taper depends on operating frequency and slip characteristics

### Thermal
- More copper near the shaft improves heat conduction to the rotor core
- Reduces hot-spot temperature in the bar during starting

### Mechanical
- Tapered bars are more securely seated in slots (self-locking effect)
- Reduces bar vibration and potential for bar loosening

### Manufacturing
- Tapered slots require modified punching tools
- Die cost increase is typically 15–30% over parallel slots
- Bar insertion may require press-fit or gravity-fed methods

---

## Cross-References

- [[pymotorcad-adaptive-geometry]] — region management and adaptive geometry pipeline
- [[pymotorcad-geometry-objects]] — Coordinate, Line, Arc, EntityList definitions
- [[pymotorcad-geometry-shapes]] — pre-built shape constructors
- [[pymotorcad-adaptive-templates-guide]] — template reference for adaptive geometry examples

---

## Tags

#pymotorcad #adaptive-geometry #rotor #induction-motor #tooth-bar #tapered #geometry #chord-angle #starting-torque
