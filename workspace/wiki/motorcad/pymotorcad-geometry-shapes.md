---
type: pymotorcad_api
title: PyMotorCAD Geometry Shapes
source: PyMotorCAD Official Documentation
tags:
  - pymotorcad
  - geometry
  - shapes
  - squares
  - triangles
  - notches
  - adaptive-geometry
---

# PyMotorCAD Geometry Shapes

Pre-built shape constructors for creating primitive geometry objects within PyMotorCAD's adaptive geometry system. These functions generate coordinate lists and entity lists that can be composed into complex rotor/stator geometries.

---

## `square(width, r_O, th_O, region_type)`

Creates a square geometry centred at polar coordinates `(r_O, th_O)` with the given `width`.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `width` | `float` | Side length of the square (mm) |
| `r_O` | `float` | Radial centre of the square (mm) |
| `th_O` | `float` | Angular centre of the square (degrees) |
| `region_type` | `RegionType` | Region classification (e.g. `RegionType.Region`, `RegionType.RegionMagnet`) |

### Returns

A tuple of `(coordinates, entities)` representing the square boundary.

### Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import RegionType

mc = pymotorcad.MotorCAD()

# Create a 10 mm square centred at r=50 mm, th=0 deg
coords, entities = mc.geometry.shapes.square(
    width=10.0,
    r_O=50.0,
    th_O=0.0,
    region_type=RegionType.Region
)
```

### Notes

- The square is oriented with sides parallel/perpendicular to the radial direction at `th_O`.
- Useful for creating slot openings, ventilation ducts, or simplified barrier approximations.
- The returned coordinates can be passed to [[pymotorcad-adaptive-geometry]] region functions.

---

## `eq_triangle_h(height, r_O, th_O)`

Creates an equilateral triangle defined by its **height**, centred at polar coordinates `(r_O, th_O)`.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `height` | `float` | Height of the equilateral triangle (mm) |
| `r_O` | `float` | Radial centre of the triangle (mm) |
| `th_O` | `float` | Angular centre of the triangle (degrees) |

### Returns

A tuple of `(coordinates, entities)` representing the triangle boundary.

### Example

```python
# Equilateral triangle with height 12 mm at r=60 mm, th=45 deg
coords, entities = mc.geometry.shapes.eq_triangle_h(
    height=12.0,
    r_O=60.0,
    th_O=45.0
)
```

### Notes

- Side length is derived from height: `width = 2 * height / sqrt(3)`.
- The triangle apex points outward (away from shaft).
- No `region_type` parameter — use [[pymotorcad-geometry-objects]] `Region` to assign type after creation.

---

## `eq_triangle_w(width, r_O, th_O)`

Creates an equilateral triangle defined by its **width** (side length), centred at polar coordinates `(r_O, th_O)`.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `width` | `float` | Side length of the equilateral triangle (mm) |
| `r_O` | `float` | Radial centre of the triangle (mm) |
| `th_O` | `float` | Angular centre of the triangle (degrees) |

### Returns

A tuple of `(coordinates, entities)` representing the triangle boundary.

### Example

```python
# Equilateral triangle with side 15 mm at r=70 mm, th=90 deg
coords, entities = mc.geometry.shapes.eq_triangle_w(
    width=15.0,
    r_O=70.0,
    th_O=90.0
)
```

### Notes

- Height is derived from width: `height = width * sqrt(3) / 2`.
- Functionally equivalent to `eq_triangle_h` but parameterised by side length.
- Useful for barrier geometry approximations in SynRM rotor design.

---

## `triangular_notch(radius, sweep, centre_angle, depth, region_type)`

Creates a triangular notch geometry — a wedge-shaped cut typically used for flux barrier entries or slot notch profiles.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `radius` | `float` | Radial distance to the notch base (mm) |
| `sweep` | `float` | Angular sweep of the notch (degrees) |
| `centre_angle` | `float` | Angular centre of the notch (degrees) |
| `depth` | `float` | Radial depth of the notch (mm) |
| `region_type` | `RegionType` | Region classification |

### Returns

A tuple of `(coordinates, entities)` representing the notch boundary.

### Example

```python
from ansys.motorcad.core.geometry import RegionType

# Triangular notch at r=80 mm, 10 deg sweep, centred at 30 deg, 5 mm deep
coords, entities = mc.geometry.shapes.triangular_notch(
    radius=80.0,
    sweep=10.0,
    centre_angle=30.0,
    depth=5.0,
    region_type=RegionType.Region
)
```

### Notes

- The notch opens outward (toward larger radius).
- `depth` is measured radially inward from `radius`.
- Commonly used for flux barrier entry geometry in [[pymotorcad-bezier-rotor-pockets]].

---

## Related Pages

- [[pymotorcad-geometry-objects]] — core geometry object types and coordinate conversion functions
- [[pymotorcad-adaptive-geometry]] — region management and adaptive geometry pipeline
- [[pymotorcad-geometry-basic]] — fundamental geometry operations
- [[pymotorcad-geometry-tree]] — tree-based geometry management
- [[pymotorcad-bezier-rotor-pockets]] — Bezier-curve rotor pocket definitions

---

## Tags

#pymotorcad #geometry #shapes #squares #triangles #notches #adaptive-geometry #rotor-design
