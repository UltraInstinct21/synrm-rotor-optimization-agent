---
type: pymotorcad_example
title: Triangular Stator Notches for NVH Improvement
source: PyMotorCAD Official Documentation — Adaptive Geometry Example e10
tags:
  - pymotorcad
  - adaptive-geometry
  - stator
  - notches
  - NVH
  - triangular-notch
  - geometry
---

# Triangular Stator Notches for NVH Improvement

Adaptive geometry example demonstrating how to add triangular notches to the stator bore surface to reduce electromagnetic noise, vibration, and harshness (NVH) in electric motor designs.

---

## Template Reference

- **Motor-CAD Template:** `e10`
- **Example Type:** Adaptive geometry modification — stator notch geometry
- **Use Case:** NVH mitigation via stator bore surface profiling

---

## Overview

Triangular notches cut into the stator bore surface alter the effective airgap permeance distribution, reducing force harmonics that excite structural resonance. This technique is commonly applied in high-performance permanent magnet and synchronous reluctance motors where acoustic noise is a design constraint.

### Design Parameters

| Parameter | Motor-CAD Variable | Description |
|---|---|---|
| Notch Sweep | `Notch_Sweep` | Angular sweep of each notch (degrees) |
| Notch Depth | `Notch_Depth` | Radial depth of the notch into the stator (mm) |

The notch sweep and depth control the notch profile. Deeper, wider notches produce stronger NVH reduction but reduce effective airgap flux and may impact torque and power factor.

---

## Geometry Construction Approach

This example uses **manual geometry construction** with PyMotorCAD's geometry primitives rather than pre-built shapes. Each notch is constructed from:

- **`Arc`** — curved boundary at the stator bore radius
- **`Line`** — radial edges forming the notch sides
- **`Coordinate`** — polar or Cartesian points defining the geometry vertices

### Key API Methods

| Method | Purpose |
|---|---|
| `add_entity()` | Adds a Line or Arc entity to the region boundary |
| `is_closed()` | Validates that entity list forms a closed region |
| `set_region()` | Writes the completed region into Motor-CAD |

---

## Entity Order Rule

**Entities must be added in anticlockwise order.** This is a fundamental requirement of Motor-CAD's adaptive geometry system. Adding entities in clockwise order will produce an inverted or invalid region.

```
Anticlockwise:  Arc → Line → Line → Arc → Line → Line → ...
```

Verify the winding order by checking coordinate progression around the notch boundary before calling `set_region()`.

---

## Code Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate, Line, Arc, EntityList

mc = pymotorcad.MotorCAD()

# Parameters
stator_bore = mc.get_variable("Stator_bore")      # mm
notch_sweep = 10.0                                  # degrees
notch_depth = 2.0                                   # mm
notch_centre_angle = 0.0                            # degrees
num_notches = 48                                    # one per slot or custom

for i in range(num_notches):
    centre_angle = notch_centre_angle + i * (360.0 / num_notches)

    # Inner arc (stator bore surface)
    arc_start_angle = centre_angle - notch_sweep / 2.0
    arc_end_angle = centre_angle + notch_sweep / 2.0

    # Calculate notch vertices
    r_inner = stator_bore / 2.0
    r_outer = r_inner - notch_depth

    start_coord = Coordinate(r=r_inner, th=arc_start_angle)
    end_coord = Coordinate(r=r_inner, th=arc_end_angle)
    outer_start = Coordinate(r=r_outer, th=arc_start_angle)
    outer_end = Coordinate(r=r_outer, th=arc_end_angle)

    # Build entity list (anticlockwise order)
    entities = EntityList()
    entities.add(Arc(start_coord, end_coord, radius=r_inner))    # bore arc
    entities.add(Line(end_coord, outer_end))                      # radial line out
    entities.add(Arc(outer_end, outer_start, radius=r_outer))    # outer arc
    entities.add(Line(outer_start, start_coord))                  # radial line back

    # Verify closure
    if mc.geometry.get_entities_have_common_coordinate(entities):
        mc.geometry.set_region(entities)
    else:
        print(f"Warning: notch {i} region not closed — check geometry")
```

---

## Workflow Steps

1. **Set up stator geometry** — ensure `Stator_bore` and slot parameters are defined
2. **Calculate notch positions** — distribute notches around the bore (e.g., one per slot pitch)
3. **Build geometry primitives** — construct Arc and Line entities for each notch
4. **Enforce anticlockwise order** — add entities in the correct winding sequence
5. **Validate closure** — call `is_closed()` / `get_entities_have_common_coordinate()` before proceeding
6. **Write to Motor-CAD** — call `set_region()` to inject the geometry
7. **Run EMag calculation** — `do_magnetic_calculation()` to evaluate impact on torque, PF, and NVH metrics

---

## Design Considerations

### NVH Impact
- Notches reduce permeance harmonics at slot-pole interaction frequencies
- Optimal notch depth is typically 1–5 mm depending on airgap length
- Notch sweep should be less than the slot opening angle to avoid slot geometry conflicts

### Electromagnetic Trade-offs
- Deeper notches reduce effective airgap flux density → lower torque
- Notches increase airgap reluctance → may reduce power factor
- Must balance NVH improvement against torque and efficiency degradation

### Manufacturing
- Triangular notches are not standard in laminated stators — may require custom tooling
- Consider whether the NVH benefit justifies manufacturing complexity

---

## Cross-References

- [[pymotorcad-adaptive-geometry]] — region management and adaptive geometry pipeline
- [[pymotorcad-geometry-objects]] — Coordinate, Line, Arc, EntityList definitions
- [[pymotorcad-geometry-shapes]] — pre-built shape constructors including `triangular_notch()`
- [[pymotorcad-adaptive-templates-guide]] — template reference for adaptive geometry examples

---

## Tags

#pymotorcad #adaptive-geometry #stator #notches #NVH #triangular-notch #geometry #anticlockwise #set-region
