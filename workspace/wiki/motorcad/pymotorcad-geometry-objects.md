---
type: pymotorcad_api
title: PyMotorCAD Geometry Objects
source: PyMotorCAD Official Documentation
tags:
  - pymotorcad
  - geometry
  - objects
  - coordinates
  - entities
  - region
  - line
  - arc
  - bezier
---

# PyMotorCAD Geometry Objects

Core data structures and utility functions for representing 2D geometry in PyMotorCAD. These objects form the foundation of all adaptive geometry operations.

---

## Object Types

### `Region`

A closed geometric region defined by a list of entities (lines, arcs, Bezier curves). Regions are the primary building blocks for rotor barriers, stator slots, magnets, and other geometric features.

```python
from ansys.motorcad.core.geometry import Region

region = Region()
region.entities = entity_list  # EntityList of Line/Arc/Bezier
```

### `RegionMagnet`

A specialised region type representing a magnet. Inherits from `Region` but carries additional magnet-specific metadata (magnetisation direction, material assignment).

```python
from ansys.motorcad.core.geometry import RegionMagnet

magnet_region = RegionMagnet()
```

### `RegionType`

Enum-like classification for regions:

| Value | Meaning |
|---|---|
| `RegionType.Region` | General geometric region (barrier, slot, etc.) |
| `RegionType.RegionMagnet` | Magnet region |

### `Coordinate`

A 2D point in polar or Cartesian coordinates.

```python
from ansys.motorcad.core.geometry import Coordinate

# Polar coordinate
coord = Coordinate(r=50.0, th=45.0)

# Cartesian coordinate
coord = Coordinate(x=35.36, y=35.36)
```

### `Entity`

Base class for geometric entities (lines, arcs, Bezier curves). An entity connects two coordinates.

### `EntityList`

An ordered collection of `Entity` objects forming a continuous path. Used to define closed region boundaries.

```python
entity_list = EntityList()
entity_list.add(line1)
entity_list.add(arc1)
entity_list.add(line2)
```

### `Line`

A straight-line entity connecting two coordinates.

```python
from ansys.motorcad.core.geometry import Line, Coordinate

start = Coordinate(r=50.0, th=0.0)
end = Coordinate(r=50.0, th=10.0)
line = Line(start, end)
```

### `Arc`

A circular arc entity connecting two coordinates with a defined radius.

```python
from ansys.motorcad.core.geometry import Arc, Coordinate

start = Coordinate(r=50.0, th=0.0)
end = Coordinate(r=50.0, th=15.0)
arc = Arc(start, end, radius=10.0)
```

---

## Coordinate Conversion Functions

### `xy_to_rt(x, y)`

Converts Cartesian coordinates `(x, y)` to polar coordinates `(r, th)`.

| Parameter | Type | Description |
|---|---|---|
| `x` | `float` | X-coordinate (mm) |
| `y` | `float` | Y-coordinate (mm) |

**Returns:** `(r, th)` tuple where `r` is in mm and `th` is in degrees.

```python
r, th = mc.geometry.xy_to_rt(35.36, 35.36)
# r ≈ 50.0, th ≈ 45.0
```

### `rt_to_xy(r, th)`

Converts polar coordinates `(r, th)` to Cartesian coordinates `(x, y)`.

| Parameter | Type | Description |
|---|---|---|
| `r` | `float` | Radial distance (mm) |
| `th` | `float` | Angular position (degrees) |

**Returns:** `(x, y)` tuple in mm.

```python
x, y = mc.geometry.rt_to_xy(50.0, 45.0)
# x ≈ 35.36, y ≈ 35.36
```

### `get_bezier_points(control_points, num_points)`

Generates interpolated points along a Bezier curve defined by control points.

| Parameter | Type | Description |
|---|---|---|
| `control_points` | `list[Coordinate]` | Bezier control points |
| `num_points` | `int` | Number of interpolated points to generate |

**Returns:** List of `Coordinate` objects along the curve.

```python
from ansys.motorcad.core.geometry import Coordinate

controls = [
    Coordinate(r=50.0, th=0.0),
    Coordinate(r=70.0, th=5.0),
    Coordinate(r=80.0, th=10.0),
]
points = mc.geometry.get_bezier_points(controls, num_points=20)
```

---

## Region Validation

### `get_entities_have_common_coordinate(entity_list)`

Checks whether an entity list forms a closed region by verifying that the last entity's endpoint connects to the first entity's start point.

| Parameter | Type | Description |
|---|---|---|
| `entity_list` | `EntityList` | List of entities to validate |

**Returns:** `True` if the region is closed (entities share common coordinates at boundaries).

```python
is_closed = mc.geometry.get_entities_have_common_coordinate(entity_list)
if not is_closed:
    print("Warning: region is not closed — check entity connectivity")
```

### Notes

- This is a prerequisite check before passing entity lists to [[pymotorcad-adaptive-geometry]] `set_region()`.
- Open regions will cause MotorCAD to reject the geometry or produce incorrect FEA mesh.

---

## Related Pages

- [[pymotorcad-geometry-shapes]] — pre-built shape constructors (square, triangle, notch)
- [[pymotorcad-geometry-basic]] — fundamental geometry operations
- [[pymotorcad-geometry-drawing]] — visualisation and debug drawing
- [[pymotorcad-geometry-fitting]] — fitting lines/arcs to coordinate sets
- [[pymotorcad-adaptive-geometry]] — region management pipeline

---

## Tags

#pymotorcad #geometry #objects #coordinates #entities #region #line #arc #bezier #coordinate-conversion
