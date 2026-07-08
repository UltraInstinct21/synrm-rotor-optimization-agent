---
type: pymotorcad_example
title: "PyMotorCAD Curved Flux Barriers"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - curved
  - flux-barriers
  - syncrel
  - u-shape
  - adaptive-geometry
  - arcs
  - circular
aliases:
  - curved_flux_barriers
  - circular_barriers
motor_types: ["SynRM", "SYNCREL"]
confidence: verified
---

# PyMotorCAD Curved Flux Barriers

## Overview

This page documents how to create **curved flux barriers** for a SYNCREL (synchronous reluctance) machine with U-Shape rotor geometry. Straight flux barriers are the default in most SynRM designs, but curved barriers defined by circular arcs can improve flux引导, reduce torque ripple, and enhance saliency. The workflow uses a circle-through-3-points geometric construction to define arc segments that replace straight barrier edges.

**Template:** i3 (SYNCREL U-Shape)

**Requirements:** MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+

---

## Key Variables

| Variable | MotorCAD Name | Description | Units |
|---|---|---|---|
| Outer thickness array | `UShape_Thickness_Outer_Array` | Array of outer barrier thickness values per layer | mm |
| Outer post array | `UShape_Post_Outer_Array` | Array of outer post (bridge) positions per layer | mm |
| Inner thickness array | `UShape_Thickness_Inner_Array` | Array of inner barrier thickness values per layer | mm |

These arrays define the baseline straight barrier geometry. The curved barrier workflow replaces the straight edges with arcs while respecting these thickness constraints.

---

## Core Functions

### `get_barrier_centre_and_radius(p1, p2, p3)`

Computes the centre and radius of a circle passing through **3 points**. This is the fundamental geometric construction for defining a curved barrier edge as a circular arc.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `p1` | `Coordinate` | First point on the arc |
| `p2` | `Coordinate` | Second point on the arc (typically the midpoint) |
| `p3` | `Coordinate` | Third point on the arc |

#### Returns

A tuple of `(centre, radius)` where `centre` is a `Coordinate` and `radius` is a `float` (mm).

#### Mathematical Basis

Given three non-collinear points, the unique circle through them has:

```
centre = intersection of perpendicular bisectors of (p1,p2) and (p2,p3)
radius = distance(centre, p1) = distance(centre, p2) = distance(centre, p3)
```

#### Example

```python
from ansys.motorcad.core.geometry import Coordinate

p1 = Coordinate(r=100.0, th=10.0)
p2 = Coordinate(r=105.0, th=15.0)
p3 = Coordinate(r=100.0, th=20.0)

centre, radius = mc.geometry.get_barrier_centre_and_radius(p1, p2, p3)
print(f"Circle centre: r={centre.r:.2f}, th={centre.th:.2f}")
print(f"Circle radius: {radius:.2f} mm")
```

---

### `get_coordinates_no_centre_post(layer_index)`

Returns the pocket coordinates for a barrier layer **without** a centre post. The coordinates define the closed boundary of one flux barrier region.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `layer_index` | `int` | Index of the barrier layer (0-based) |

#### Returns

A list of `Coordinate` objects defining the barrier pocket boundary.

---

### `get_coordinates_centre_post(layer_index)`

Returns the pocket coordinates for a barrier layer **with** a centre post. The centre post is a structural bridge that splits the barrier into two halves.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `layer_index` | `int` | Index of the barrier layer (0-based) |

#### Returns

A list of `Coordinate` objects defining the barrier pocket boundary including the centre post geometry.

---

### `update_pocket_geometry(region, barrier_points, arc_points)`

Replaces the straight edges of a barrier region with circular arc segments. This is the operation that converts a straight barrier into a curved one.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `region` | `Region` | The barrier region to modify |
| `barrier_points` | `list[Coordinate]` | Points defining the barrier boundary |
| `arc_points` | `list[Coordinate]` | Points defining the arc curvature |

#### Returns

Modified `Region` with arc entities replacing line entities.

---

## Complete Workflow

```
UShape_Thickness/Post arrays
    → get_coordinates_no_centre_post() / get_coordinates_centre_post()
        → barrier boundary points
    → get_barrier_centre_and_radius()
        → circle centre and radius for each edge
    → update_pocket_geometry()
        → replace straight edges with arcs
    → mc.set_region()
        → apply curved barrier to model
```

### Step-by-Step Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate, Region, Arc

mc = pymotorcad.MotorCAD()
mc.show_magnetic_context()
mc.reset_adaptive_geometry()

# Read UShape variables (already set in model)
thickness_outer = mc.get_variable("UShape_Thickness_Outer_Array")
post_outer = mc.get_variable("UShape_Post_Outer_Array")
thickness_inner = mc.get_variable("UShape_Thickness_Inner_Array")

# Process each barrier layer
num_layers = len(thickness_outer)

for layer in range(num_layers):
    # Get barrier coordinates
    coords = mc.geometry.get_coordinates_no_centre_post(layer)

    # Define 3 points for arc fitting on each edge
    for i in range(0, len(coords) - 2, 3):
        p1 = coords[i]
        p2 = coords[i + 1]
        p3 = coords[i + 2]

        # Compute arc parameters
        centre, radius = mc.geometry.get_barrier_centre_and_radius(p1, p2, p3)

        # Create arc entity
        arc = Arc(start=p1, end=p3, centre=centre)

        # Replace straight edges with arc in region
        region = mc.get_region(f"Barrier_{layer}")
        mc.geometry.update_pocket_geometry(region, coords, [arc])
        mc.set_region(region)

print("Curved flux barriers applied successfully.")
```

---

## Geometric Interpretation

For a U-Shape barrier:

| Feature | Straight (Default) | Curved (Arc) |
|---|---|---|
| Barrier edges | Line segments | Circular arcs |
| Flux path | Angular corners | Smooth curvature |
| Stress concentration | High at corners | Reduced |
| Torque ripple | Higher | Lower |
| Manufacturing | Simpler stamping | More complex |

The curvature is defined by the **radius** of the circle through 3 points:
- Larger radius → flatter curve (closer to straight)
- Smaller radius → more pronounced curvature

---

## Design Considerations

- **Curvature direction** — Arcs can curve inward (concave) or outward (convex) relative to the shaft. The choice affects flux引导 paths.
- **Layer interaction** — Curved barriers in adjacent layers must not overlap. Check geometry constraints after applying arcs.
- **Centre post** — If present, the centre post divides the barrier into two symmetric halves. Each half can have independent curvature.
- **Thickness preservation** — The arc fitting must preserve the barrier thickness defined by `UShape_Thickness` arrays. Deviation from the target thickness degrades the magnetic design.
- **Symmetry** — Only one pole sector needs to be defined; MotorCAD handles duplication via the `duplications` property.

---

## Common Pitfalls

1. **Collinear points** — `get_barrier_centre_and_radius()` fails if the 3 points are collinear (infinite radius). Ensure points are not aligned.
2. **Arc direction ambiguity** — Through 3 points there is a unique circle, but the arc can go the "short way" or "long way". Ensure the correct arc segment is selected.
3. **Region not closed** — Arc entities must connect end-to-end to form a closed boundary.
4. **Version mismatch** — This workflow requires MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+. Earlier versions do not support the required geometry APIs.
5. **Missing `reset_adaptive_geometry()`** — Must be called before each modification cycle.

---

## Related Pages

- [[pymotorcad-adaptive-geometry]] — Full adaptive template API
- [[pymotorcad-geometry-objects]] — Region, Coordinate, Arc, Line types
- [[flux-barriers]] — Flux barrier design theory and guidelines
- [[pymotorcad-bezier-rotor-pockets]] — Bezier curves (alternative curvature method)
- [[pymotorcad-adaptive-templates-guide]] — Adaptive templates user guide
- [[pymotorcad-geometry-shapes]] — Shape primitives

---

## Tags

#pymotorcad #motorcad #curved #flux-barriers #syncrel #u-shape #adaptive-geometry #arcs #circular #rotor-design
