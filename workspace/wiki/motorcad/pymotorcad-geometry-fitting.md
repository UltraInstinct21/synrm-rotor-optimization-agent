---
type: pymotorcad_api
title: PyMotorCAD Geometry Fitting
source: PyMotorCAD Official Documentation
tags:
  - pymotorcad
  - geometry
  - fitting
  - line-fitting
  - arc-fitting
  - entity-fitting
  - coordinates
---

# PyMotorCAD Geometry Fitting

Functions for converting raw coordinate sets into optimised entity lists (lines and arcs). This is critical when importing geometry from external sources (CAD exports, CSV data, analytical curves) or when converting Bezier-generated points into MotorCAD-native entities.

---

## `return_entity_list(coordinates, tolerance)`

Fits a sequence of `Line` and `Arc` entities to a set of input coordinates, optimising for geometric accuracy within the specified tolerance.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `coordinates` | `list[Coordinate]` | Ordered list of points to fit |
| `tolerance` | `float` | Maximum allowable deviation between fitted entities and input coordinates (mm) |

### Returns

An `EntityList` containing the fitted `Line` and `Arc` entities.

### Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate

mc = pymotorcad.MotorCAD()

# Raw coordinates (e.g. from CSV import or Bezier interpolation)
raw_points = [
    Coordinate(r=50.0, th=0.0),
    Coordinate(r=55.0, th=5.0),
    Coordinate(r=65.0, th=10.0),
    Coordinate(r=80.0, th=15.0),
    # ... more points
]

# Fit lines and arcs within 0.01 mm tolerance
fitted_entities = mc.geometry.return_entity_list(
    coordinates=raw_points,
    tolerance=0.01
)

print(f"Fitted {len(fitted_entities)} entities to {len(raw_points)} points")
```

### How the Algorithm Works

1. **Segment detection:** identifies collinear point sequences (lines) vs curved sequences (arcs)
2. **Line fitting:** fits straight lines to collinear segments using least-squares
3. **Arc fitting:** fits circular arcs to curved segments, minimising radial deviation
4. **Tolerance enforcement:** splits entities where deviation exceeds `tolerance`
5. **Entity assembly:** builds a connected `EntityList` from fitted segments

### Tolerance Selection Guide

| Tolerance | Use Case | Entity Count | Accuracy |
|---|---|---|---|
| `0.001` mm | Precision FEA meshing | High | Maximum |
| `0.01` mm | General geometry fitting | Medium | High |
| `0.1` mm | Approximate shapes,快速原型 | Low | Moderate |
| `1.0` mm | Simplified geometry, visual only | Very low | Low |

### Notes

- Tighter tolerances produce more entities (smaller line/arc segments), increasing mesh complexity.
- For [[pymotorcad-bezier-rotor-pockets]] workflows, a tolerance of `0.01`–`0.05` mm is typically sufficient.
- The algorithm preserves the order and connectivity of input coordinates.
- The output `EntityList` can be directly assigned to a `Region` and committed via [[pymotorcad-adaptive-geometry]].

---

## Common Fitting Scenarios

### Scenario 1: Importing Bezier Curve Points

```python
# Generate Bezier points from control points
controls = [
    Coordinate(r=50.0, th=0.0),
    Coordinate(r=70.0, th=5.0),
    Coordinate(r=85.0, th=10.0),
    Coordinate(r=80.0, th=20.0),
]
bezier_points = mc.geometry.get_bezier_points(controls, num_points=50)

# Fit to entities
entities = mc.geometry.return_entity_list(bezier_points, tolerance=0.02)
```

### Scenario 2: CAD-Imported Profile

```python
import csv

# Read coordinates from CSV
coords = []
with open("rotor_profile.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        coords.append(Coordinate(r=float(row["r"]), th=float(row["th"])))

# Fit to MotorCAD entities
entities = mc.geometry.return_entity_list(coords, tolerance=0.05)
```

### Scenario 3: Analytical Curve Sampling

```python
import math

# Sample a sinusoidal barrier profile
coords = []
for i in range(100):
    th = i * 0.5  # 0 to 49.5 degrees
    r = 60 + 10 * math.sin(math.radians(th * 2))
    coords.append(Coordinate(r=r, th=th))

entities = mc.geometry.return_entity_list(coords, tolerance=0.01)
```

---

## Fitting Quality Checks

After fitting, verify the result:

```python
# Check entity count — unexpected spikes indicate fitting issues
print(f"Entities: {len(entities)}")

# Visualise the fit
mc.geometry.draw_objects([fitted_region], fill_regions=True, show_coords=True)

# Compare original coordinates to fitted entities
mc.geometry.draw_objects_debug([fitted_region])
```

### Quality Indicators

| Metric | Good | Investigate |
|---|---|---|
| Entity count | 5–30 per region | >50 suggests over-segmentation |
| Max deviation | < tolerance | Deviations > tolerance indicate algorithm issue |
| Visual smoothness | Curves appear smooth | Jagged edges suggest insufficient points or loose tolerance |

---

## Related Pages

- [[pymotorcad-geometry-objects]] — Entity, EntityList, Line, Arc, Coordinate types
- [[pymotorcad-geometry-shapes]] — pre-built shape constructors
- [[pymotorcad-bezier-rotor-pockets]] — Bezier-based rotor pocket definitions
- [[pymotorcad-geometry-drawing]] — visualising fitted geometry
- [[pymotorcad-adaptive-geometry]] — committing fitted regions to MotorCAD

---

## Tags

#pymotorcad #geometry #fitting #line-fitting #arc-fitting #entity-fitting #tolerance #coordinate-fitting
