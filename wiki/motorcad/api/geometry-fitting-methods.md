---
type: motorcad_api
method_group: "Geometry Fitting"
module: "ansys.motorcad.core.geometry_fitting"
source_files: ["Geometry fitting — pymotorcad-core.md"]
confidence: Verified
---

# Geometry Fitting Methods

Functions to find line and arc entities to fit a list of coordinates within a defined tolerance. Used with Adaptive Templates.

## Functions

| Function | Description |
|----------|-------------|
| `return_entity_list(coordinates, line_tolerance, arc_tolerance)` | Get list of entities from coordinates |

## Importing

```python
from ansys.motorcad.core.geometry_fitting import return_entity_list
```

## Usage Example (from Bezier curve workflow)

```python
xylist = get_bezier_points(control_points, 256)
linetolerance = 0.01
arctolerance = 0.01
entities = return_entity_list(xylist, linetolerance, arctolerance)
```

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Line, Arc, Coordinate objects
- [[motorcad/workflows/bezier-curve-rotor-pockets]] — Bezier curve pocket example
