---
type: motorcad_workflow
name: "Bezier Curve Rotor Pockets"
purpose: "Create custom curved rotor pocket geometry using Bezier functions"
prerequisites: ["Motor-CAD v2024 R2+", "e4a template or similar IPM"]
source_files: ["Bezier curve rotor pockets — pymotorcad-core.md"]
confidence: Verified
---

# Bezier Curve Rotor Pockets

## Purpose

Modify IPM rotor pockets with custom curves defined using Bezier functions for optimized flux barriers.

## Prerequisites

Motor-CAD v2024 R2 or later. Script designed for e4a template (48 slot, 8 pole IPM).

## Step-by-Step Procedure

### 1. Set Adaptive Parameters

```python
mc.set_adaptive_parameter_default("L1 Bezier Curve Projection", 6)
mc.set_adaptive_parameter_default("L1 Upper Convex", 0.5)
mc.set_adaptive_parameter_default("L1 Lower Concave", -0.3)
```

Parameters control:
- **Bezier Curve Projection** — pocket extension beyond magnet edge (mm)
- **Upper Convex** — convex curvature beyond magnet edge
- **Lower Concave** — concave curvature beyond magnet edge

### 2. Get Magnet Edge Properties

```python
rotor_region = mc.get_region("Rotor")
# Find magnet edge shared with first rotor pocket
for j in Magnet_regions:
    for i in j.entities:
        MagnetFaceLine = Rotor_Pocket_regions[0].find_entity_from_coordinates(i.start, ...)
        if MagnetFaceLine is not None:
            break

LineLength = MagnetFaceLine.length
StartCoordinate = MagnetFaceLine.start
```

### 3. Define Bezier Control Points

```python
control_points = [
    Coordinate(0.0, 0),
    Coordinate(totalprojection * -0.2, (1 - lowerconcave) * LineLength),
    Coordinate(totalprojection * -0.5, -0.5 * LineLength),
    Coordinate(-1 * totalprojection, 0.5 * LineLength),
    Coordinate(totalprojection * -0.5, (1 + upperconvex) * LineLength),
    Coordinate(0.0, 1 * LineLength),
]

num_pts = 256
xylist = get_bezier_points(control_points, num_pts)
```

### 4. Convert to Entities

```python
bez_curve_entities = return_entity_list(xylist, linetolerance=0.01, arctolerance=0.01)

for ent in bez_curve_entities:
    Rotor_Pocket_regions[0].add_entity(ent)
```

### 5. Position and Set Region

```python
Rotor_Pocket_regions[0].translate(StartCoordinate.x, StartCoordinate.y)
Rotor_Pocket_regions[0].rotate(StartCoordinate, -(90 - MagnetFaceLine.angle))
Rotor_Pocket_regions[0].add_entity(MagnetFaceLine)

if Rotor_Pocket_regions[0].is_closed():
    mc.set_region(Rotor_Pocket_regions[0])
```

### 6. Mirror to Second Pocket

```python
mirrorLine = Line(Coordinate(0, 0), Coordinate(mirrorlinex, mirrorliney))
mirroredRegion = Rotor_Pocket_regions[0].mirror(mirrorLine)
Rotor_Pocket_regions[1].replace(mirroredRegion)

if Rotor_Pocket_regions[1].is_closed():
    mc.set_region(Rotor_Pocket_regions[1])
```

## Key Functions Used

| Function | Source | Purpose |
|----------|--------|---------|
| `get_bezier_points()` | `ansys.motorcad.core.geometry` | Generate points along Bezier curve |
| `return_entity_list()` | `ansys.motorcad.core.geometry_fitting` | Convert points to Line/Arc entities |
| `region.mirror()` | Region method | Mirror geometry across a line |
| `region.replace()` | Region method | Replace entities keeping properties |

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region, Line, Arc, Coordinate
- [[motorcad/api/geometry-fitting-methods]] — return_entity_list
- [[motorcad/api/geometry-shapes]] — Other shape utilities
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
- [[motorcad/workflows/triangular-rotor-notches-ipm]] — Another IPM geometry example
