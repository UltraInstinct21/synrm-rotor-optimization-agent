---
type: pymotorcad_example
title: "PyMotorCAD Bezier Rotor Pockets"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - bezier
  - rotor
  - pockets
  - ipm
  - adaptive-geometry
  - geometry
  - curved
aliases:
  - bezier_rotor_pockets
  - bezier_curves
motor_types: ["IPMSM", "PMaSynRM", "SynRM"]
confidence: verified
---

# PyMotorCAD Bezier Rotor Pockets

## Overview

This page documents how to create curved rotor pockets using **Bezier curves** for Interior Permanent Magnet (IPM) machines. Bezier curves enable smooth, continuously varying pocket boundaries that cannot be achieved with straight lines or simple arcs. The workflow uses 6 control points to define a Bezier curve, which is then evaluated to 256 points, fitted to arcs/lines, and placed via translate/rotate/mirror operations.

**Template:** e4a (IPM rotor with Bezier pocket geometry)

**Requirements:** MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+

---

## Adaptive Parameters

The following adaptive parameters control the Bezier pocket geometry:

| Parameter | Description | Units |
|---|---|---|
| L1 Bezier Curve Projection | Controls how far the Bezier curve deviates from the chord (projection distance) | mm |
| L1 Upper Convex | Curvature of the upper boundary of the pocket | mm (radius or offset) |
| L1 Lower Concave | Curvature of the lower boundary of the pocket | mm (radius or offset) |

These parameters are read from the adaptive template and fed into the Bezier control point calculation.

---

## Core Geometry API

### `get_bezier_points(control_points, num_points=256)`

Evaluates a Bezier curve through the given control points and returns a dense set of interpolated points.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `control_points` | `list[Coordinate]` | List of control points defining the Bezier curve (typically 6 points for rotor pockets) |
| `num_points` | `int` | Number of points to generate along the curve (default: 256) |

#### Returns

A list of `Coordinate` objects representing points along the Bezier curve.

#### Example

```python
from ansys.motorcad.core.geometry import Coordinate

# 6 control points for one pocket edge
control_points = [
    Coordinate(r=100.0, th=0.0),    # start
    Coordinate(r=105.0, th=5.0),    # control 1
    Coordinate(r=110.0, th=10.0),   # control 2
    Coordinate(r=108.0, th=15.0),   # control 3
    Coordinate(r=103.0, th=20.0),   # control 4
    Coordinate(r=100.0, th=25.0),   # end
]

bezier_points = mc.geometry.get_bezier_points(control_points, num_points=256)
```

### `return_entity_list(points)`

Converts a list of points into a list of geometry entities (lines and arcs) suitable for use in a `Region`.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `points` | `list[Coordinate]` | Dense point list (e.g. from `get_bezier_points`) |

#### Returns

An `EntityList` of `Line` and `Arc` entities that approximate the Bezier curve.

#### Example

```python
entities = mc.geometry.return_entity_list(bezier_points)
```

---

## Region Operations

Once the pocket boundary is defined as an entity list, the following operations place it correctly in the rotor geometry:

### `find_entity_from_coordinates(region, coordinate)`

Finds the entity index in a region that passes through (or closest to) a given coordinate.

```python
entity_index = mc.geometry.find_entity_from_coordinates(region, target_coord)
```

### `translate(region, dx, dy)`

Translates all entities in a region by `(dx, dy)` in Cartesian coordinates.

```python
mc.geometry.translate(region, dx=5.0, dy=0.0)
```

### `rotate(region, angle, centre)`

Rotates all entities in a region by `angle` degrees about `centre`.

```python
from ansys.motorcad.core.geometry import Coordinate

mc.geometry.rotate(region, angle=30.0, centre=Coordinate(r=0.0, th=0.0))
```

### `mirror(region, axis_angle)`

Mirrors all entities about a radial line at `axis_angle` degrees.

```python
mc.geometry.mirror(region, axis_angle=90.0)
```

### `replace(region, new_entities)`

Replaces the entity list of a region while preserving region properties (name, colour, material, duplications).

```python
mc.geometry.replace(region, entities)
```

---

## Complete Workflow

The full workflow for creating Bezier rotor pockets:

```
6 control points
    → get_bezier_points() → 256 Bezier points
    → return_entity_list() → fit to arcs/lines
    → translate() → position pocket
    → rotate() → orient to correct pole
    → mirror() → create symmetric pocket
```

### Step-by-Step

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate, Region

mc = pymotorcad.MotorCAD()
mc.show_magnetic_context()
mc.reset_adaptive_geometry()

# 1. Get existing rotor region
rotor_region = mc.get_region("Rotor Lam")

# 2. Define 6 Bezier control points for one pocket edge
upper_control = [
    Coordinate(r=100.0, th=0.0),
    Coordinate(r=105.0, th=5.0),
    Coordinate(r=110.0, th=10.0),
    Coordinate(r=108.0, th=15.0),
    Coordinate(r=103.0, th=20.0),
    Coordinate(r=100.0, th=25.0),
]

# 3. Evaluate Bezier curve
upper_points = mc.geometry.get_bezier_points(upper_control, num_points=256)

# 4. Convert to entities (arcs + lines)
upper_entities = mc.geometry.return_entity_list(upper_points)

# 5. Create pocket region
pocket = Region()
pocket.name = "PM_Pocket_1"
pocket.colour = (0, 255, 0)
pocket.entities = upper_entities

# 6. Translate to correct radial position
mc.geometry.translate(pocket, dx=2.0, dy=0.0)

# 7. Rotate to correct angular position
mc.geometry.rotate(pocket, angle=15.0, centre=Coordinate(r=0.0, th=0.0))

# 8. Mirror for symmetric pole
mc.geometry.mirror(pocket, axis_angle=90.0)

# 9. Set region back
mc.set_region(pocket)
```

---

## Control Point Geometry

The 6 control points define a quintic (order 5) Bezier curve:

| Point | Role | Typical Location |
|---|---|---|
| P0 | Start point | Inner radius of pocket |
| P1 | Control 1 | Pulls curve outward-upward |
| P2 | Control 2 | Pulls curve outward-upward |
| P3 | Control 3 | Pulls curve inward-downward |
| P4 | Control 4 | Pulls curve inward-downward |
| P5 | End point | Outer radius of pocket |

The `L1 Bezier Curve Projection` parameter controls the perpendicular distance from the chord P0→P5 to the curve apex. Higher values create deeper curvature.

---

## Design Considerations

- **Smooth boundaries** reduce flux concentration at sharp corners, improving saturation behaviour and reducing torque ripple.
- **Bezier curves** allow continuous variation of pocket shape without discrete arc segments, which is important for optimisation routines that vary geometry parameters.
- The **projection parameter** must be tuned to avoid pocket boundaries crossing into the shaft region or crossing the rotor outer diameter.
- **Mirror operations** ensure magnetic symmetry, which is required for correct EMag calculation with symmetry boundary conditions.

---

## Common Pitfalls

1. **Insufficient control points** — Fewer than 6 points may not capture the desired curvature. More points are possible but increase complexity.
2. **Bezier curve self-intersection** — Extreme control point placements can cause the curve to loop. Visualise before running EMag.
3. **Region not closed** — The entity list must form a closed loop. The first and last points should coincide or be connected.
4. **Missing `reset_adaptive_geometry()`** — Must be called before modifying regions to clear previous adaptive geometry state.

---

## Related Pages

- [[pymotorcad-adaptive-geometry]] — Full adaptive template API and region management
- [[pymotorcad-geometry-objects]] — Region, Coordinate, Line, Arc, EntityList types
- [[pymotorcad-geometry-shapes]] — Shape primitives (square, triangle, notch)
- [[pymotorcad-curved-flux-barriers]] — Curved flux barriers for SYNCREL (related curvature concept)
- [[pymotorcad-custom-dxf-geometry]] — Alternative: import pocket geometry from DXF
- [[pymotorcad-adaptive-templates-guide]] — Adaptive templates user guide

---

## Tags

#pymotorcad #motorcad #bezier #rotor #pockets #ipm #adaptive-geometry #geometry #curved #ipmsm
