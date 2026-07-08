---
type: pymotorcad_api
title: PyMotorCAD FEA Geometry Construction
source: PyMotorCAD Official Documentation
tags:
  - pymotorcad
  - fea
  - geometry
  - finite-element
  - meshing
  - post-processing
  - boundary-conditions
  - regions
---

# PyMotorCAD FEA Geometry Construction

Low-level finite element analysis (FEA) geometry construction API for building custom 2D cross-sections, defining boundary conditions, assigning regions and materials, executing FEA solve, and extracting post-processing results. This is the lowest-level geometry API in MotorCAD — use [[pymotorcad-adaptive-geometry]] for higher-level parametric workflows.

---

## Geometry Construction — Lines

### `add_line_rt(r1, th1, r2, th2)`

Adds a straight line in polar coordinates.

| Parameter | Type | Description |
|---|---|---|
| `r1` | `float` | Start radius (mm) |
| `th1` | `float` | Start angle (degrees) |
| `r2` | `float` | End radius (mm) |
| `th2` | `float` | End angle (degrees) |

### `add_line_xy(x1, y1, x2, y2)`

Adds a straight line in Cartesian coordinates.

| Parameter | Type | Description |
|---|---|---|
| `x1` | `float` | Start X (mm) |
| `y1` | `float` | Start Y (mm) |
| `x2` | `float` | End X (mm) |
| `y2` | `float` | End Y (mm) |

```python
# Radial line from r=50 to r=80 at th=0
mc.add_line_rt(50.0, 0.0, 80.0, 0.0)

# Cartesian equivalent
mc.add_line_xy(50.0, 0.0, 80.0, 0.0)
```

---

## Geometry Construction — Arcs

### `add_arc_rt(r, th_start, th_end)`

Adds a circular arc at constant radius from `th_start` to `th_end`.

| Parameter | Type | Description |
|---|---|---|
| `r` | `float` | Arc radius (mm) |
| `th_start` | `float` | Start angle (degrees) |
| `th_end` | `float` | End angle (degrees) |

### `add_arc_xy(x1, y1, x2, y2)`

Adds an arc between two Cartesian points (MotorCAD infers the arc centre from context).

### `add_arc_centre_start_end_rt(r Centre, th_centre, r_start, th_start, r_end, th_end)`

Adds an arc with explicit centre point in polar coordinates.

| Parameter | Type | Description |
|---|---|---|
| `r_centre` | `float` | Centre radius (mm) |
| `th_centre` | `float` | Centre angle (degrees) |
| `r_start` | `float` | Start radius (mm) |
| `th_start` | `float` | Start angle (degrees) |
| `r_end` | `float` | End radius (mm) |
| `th_end` | `float` | End angle (degrees) |

### `add_arc_centre_start_end_xy(x_centre, y_centre, x_start, y_start, x_end, y_end)`

Same as above in Cartesian coordinates.

```python
# Arc at r=65 mm from 0 to 30 degrees
mc.add_arc_rt(65.0, 0.0, 30.0)

# Arc with explicit centre
mc.add_arc_centre_start_end_rt(
    r_centre=0.0, th_centre=0.0,
    r_start=50.0, th_start=0.0,
    r_end=50.0, th_end=30.0
)
```

---

## Boundary Conditions

### `add_line_boundary_rt(r1, th1, r2, th2)`

Adds a boundary-condition line (periodic, symmetric, or anti-symmetric).

```python
# Periodic boundary at th=0
mc.add_line_boundary_rt(50.0, 0.0, 80.0, 0.0)
```

### `add_line_boundary_xy(x1, y1, x2, y2)`

Cartesian version of boundary line.

### `add_arc_boundary_rt(r, th_start, th_end)`

Adds a boundary-condition arc.

### `add_arc_boundary_xy(x1, y1, x2, y2)`

Cartesian version of boundary arc.

---

## Region Assignment

### `add_region_rt(r1, th1, r2, th2)`

Defines a region by two corner points in polar coordinates (bounding box).

```python
# Define barrier region
mc.add_region_rt(50.0, 0.0, 80.0, 30.0)
```

### `add_region_xy(x1, y1, x2, y2)`

Cartesian version of region definition.

### `add_magnet_region_rt(r1, th1, r2, th2, mag_angle)`

Defines a magnet region with magnetisation direction.

| Parameter | Type | Description |
|---|---|---|
| `r1, th1, r2, th2` | `float` | Region bounding box (polar) |
| `mag_angle` | `float` | Magnetisation angle (degrees) |

### `add_magnet_region_xy(x1, y1, x2, y2, mag_angle)`

Cartesian version.

### `add_point_custom_material_rt(r, th, material_name)`

Places a custom material point at a specific polar location.

```python
# Assign custom material at specific point
mc.add_point_custom_material_rt(65.0, 15.0, "M270_35A")
```

### `add_point_custom_material_xy(x, y, material_name)`

Cartesian version.

---

## FEA Execution

### `clear_all_data()`

Clears all FEA geometry data, resetting to an empty cross-section.

```python
mc.clear_all_data()
```

### `create_optimised_mesh()`

Generates an optimised finite element mesh from the current geometry.

```python
mc.create_optimised_mesh()
```

### `initiate_geometry_from_script()`

Loads geometry from a script file and initialises the FEA model.

```python
mc.initiate_geometry_from_script()
```

### `do_slot_finite_element()`

Executes the slot-level finite element solve.

```python
mc.do_slot_finite_element()
```

### FEA Workflow

```python
# 1. Clear previous geometry
mc.clear_all_data()

# 2. Build geometry (lines, arcs, boundaries)
mc.add_line_rt(50.0, 0.0, 80.0, 0.0)
mc.add_arc_rt(80.0, 0.0, 30.0)
mc.add_line_rt(80.0, 30.0, 50.0, 30.0)
mc.add_arc_rt(50.0, 30.0, 0.0)

# 3. Define regions
mc.add_region_rt(50.0, 0.0, 80.0, 30.0)

# 4. Add boundary conditions
mc.add_line_boundary_rt(50.0, 0.0, 80.0, 0.0)
mc.add_line_boundary_rt(80.0, 30.0, 50.0, 30.0)

# 5. Mesh and solve
mc.create_optimised_mesh()
mc.do_slot_finite_element()
```

---

## Post-Processing

### `get_point_value(r, th, quantity)`

Extracts a field value at a specific point.

| Parameter | Type | Description |
|---|---|---|
| `r` | `float` | Radial position (mm) |
| `th` | `float` | Angular position (degrees) |
| `quantity` | `str` | Field quantity name (e.g. `"FluxDensity"`, `"FieldStrength"`) |

**Returns:** Field value at the specified point.

```python
B = mc.get_point_value(65.0, 15.0, "FluxDensity")
print(f"Flux density at (65, 15): {B} T")
```

### `get_region_value(region_name, quantity)`

Extracts an averaged or integrated value over a region.

```python
avg_B = mc.get_region_value("barrier_1", "FluxDensity")
```

### `get_region_loss(region_name)`

Returns iron or copper loss for a specific region.

```python
iron_loss = mc.get_region_loss("stator_lam")
```

### `save_fea_data(filepath)`

Exports all FEA results to a data file.

```python
mc.save_fea_data(r"D:\SRM\results\fea_results.dat")
```

---

## Path Editor

The path editor defines sampling paths for extracting field distributions along lines, arcs, or point sequences.

### `set_fea_path_arc(r, th_start, th_end, num_points)`

Defines an arc-shaped sampling path.

| Parameter | Type | Description |
|---|---|---|
| `r` | `float` | Path radius (mm) |
| `th_start` | `float` | Start angle (degrees) |
| `th_end` | `float` | End angle (degrees) |
| `num_points` | `int` | Number of sample points |

### `set_fea_path_line(r1, th1, r2, th2, num_points)`

Defines a straight-line sampling path.

### `set_fea_path_point(r, th)`

Defines a single-point sampling location.

```python
# Define airgap flux density path
mc.set_fea_path_arc(r=107.25, th_start=0.0, th_end=360.0, num_points=360)
```

---

## FEA Geometry vs Adaptive Geometry

| Feature | FEA Geometry (this page) | Adaptive Geometry |
|---|---|---|
| Abstraction level | Low-level lines/arcs | High-level regions |
| Parametric support | Manual | Built-in parameters |
| Validation | Manual | `check_closed_region()`, `check_collisions()` |
| Script saving | Manual | `save_adaptive_script()` |
| Use case | Custom FEA, single-shot | Parametric design, optimisation |
| Recommended for | One-off analysis | Iterative design workflows |

---

## Related Pages

- [[pymotorcad-adaptive-geometry]] — higher-level parametric geometry system
- [[pymotorcad-material-mesh]] — material assignment and meshing
- [[pymotorcad-geometry-objects]] — core geometry types
- [[pymotorcad-geometry-drawing]] — visualising FEA geometry
- [[pymotorcad-geometry-fitting]] — fitting entities to coordinates

---

## Tags

#pymotorcad #fea #geometry #finite-element #meshing #post-processing #boundary-conditions #regions #field-extraction
