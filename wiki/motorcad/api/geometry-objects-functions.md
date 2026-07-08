---
type: motorcad_api
method_group: "Geometry Objects and Functions"
module: "ansys.motorcad.core.geometry"
source_files: ["Geometry objects and functions — pymotorcad-core.md"]
confidence: Verified
---

# Geometry Objects and Functions

## Geometry Objects

| Object | Description |
|--------|-------------|
| `Region(region_type, motorcad_instance)` | Create geometry region |
| `RegionMagnet(motorcad_instance)` | Create magnet geometry region |
| `RegionType` | Enumeration for Motor-CAD region types |
| `Coordinate(x, y)` | 2D coordinate |
| `Entity(start, end)` | Generic geometric entity |
| `EntityList([iterable])` | List of entities |
| `Line(start, end)` | Line entity |
| `Arc(start, end, centre=None, radius=None)` | Arc entity |

## RegionType Values

- `RegionType.rotor` — Rotor region
- `RegionType.rotor_air` — Rotor air region
- `RegionType.rotor_pocket` — Rotor pocket
- `RegionType.stator` — Stator region
- `RegionType.adaptive` — Adaptive region

## Geometry Functions

| Function | Description |
|----------|-------------|
| `get_entities_have_common_coordinate()` | Check if entities create a closed region |
| `xy_to_rt(x, y)` | Cartesian to polar (degrees) |
| `rt_to_xy(radius, theta)` | Polar (degrees) to Cartesian |
| `get_bezier_points(control_points, ...)` | Points along a Bezier curve |

## Importing

```python
from ansys.motorcad.core.geometry import (
    Arc, Coordinate, EntityList, Line, Region, RegionType, rt_to_xy, xy_to_rt
)
```

## Related Pages

- [[motorcad/api/adaptive-geometry-methods]] — get_region, set_region methods
- [[motorcad/api/geometry-shapes]] — Predefined shape functions
- [[motorcad/api/geometry-drawing-methods]] — draw_objects for visualization
- [[motorcad/api/geometry-fitting-methods]] — return_entity_list for curve fitting
- [[motorcad/workflows/adaptive-templates-scripting]] — Workflow guide
