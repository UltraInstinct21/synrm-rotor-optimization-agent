---
type: pymotorcad_api
title: PyMotorCAD Adaptive Geometry System
source: PyMotorCAD Official Documentation
tags:
  - pymotorcad
  - adaptive-geometry
  - regions
  - geometry-tree
  - script-management
  - validation
  - barrier-design
---

# PyMotorCAD Adaptive Geometry System

The adaptive geometry system is MotorCAD's programme geometry layer — it allows Python scripts to construct, modify, validate, and commit 2D geometry (regions, barriers, magnets, slots) directly into the MotorCAD model. This is the primary mechanism for script-driven rotor/stator geometry definition.

---

## Region Management

### `get_region(name)`

Retrieves a named region from the current adaptive geometry.

| Parameter | Type | Description |
|---|---|---|
| `name` | `str` | Region name |

**Returns:** `Region` object with its entity list.

```python
barrier = mc.geometry.get_region("barrier_1")
```

### `set_region(name, region)`

Creates or replaces a named region in the adaptive geometry.

| Parameter | Type | Description |
|---|---|---|
| `name` | `str` | Region name (must be unique within the model) |
| `region` | `Region` | Region object with closed entity list |

```python
from ansys.motorcad.core.geometry import Region, Coordinate, Line, EntityList, RegionType

# Build a barrier region
p1 = Coordinate(r=50.0, th=0.0)
p2 = Coordinate(r=80.0, th=0.0)
p3 = Coordinate(r=80.0, th=30.0)
p4 = Coordinate(r=50.0, th=30.0)

entities = EntityList()
entities.add(Line(p1, p2))
entities.add(Line(p2, p3))
entities.add(Line(p3, p4))
entities.add(Line(p4, p1))

region = Region()
region.entities = entities
region.region_type = RegionType.Region

mc.geometry.set_region("barrier_1", region)
```

### `delete_region(name)`

Removes a named region from the adaptive geometry.

```python
mc.geometry.delete_region("barrier_1")
```

### `subtract_region(target, tool)`

Subtracts one region from another (Boolean difference operation).

| Parameter | Type | Description |
|---|---|---|
| `target` | `str` | Name of the region to subtract from |
| `tool` | `str` | Name of the region to subtract |

```python
# Subtract barrier from rotor lamination
mc.geometry.subtract_region("rotor_lam", "barrier_1")
```

### `unite_regions(region_list)`

Unions multiple regions into a single region.

| Parameter | Type | Description |
|---|---|---|
| `region_list` | `list[str]` | List of region names to unite |

```python
# Combine multiple barrier regions
mc.geometry.unite_regions(["barrier_1", "barrier_2", "barrier_3"])
```

---

## Validation

### `check_closed_region(name)`

Validates that a named region forms a closed loop (all entity endpoints connect).

| Parameter | Type | Description |
|---|---|---|
| `name` | `str` | Region name to validate |

**Returns:** `True` if closed, raises error or returns `False` if open.

```python
if not mc.geometry.check_closed_region("barrier_1"):
    print("Region is not closed — check entity connectivity")
```

### `check_collisions()`

Checks for overlapping or colliding regions in the current adaptive geometry.

**Returns:** List of collision pairs or `True`/`False`.

```python
collisions = mc.geometry.check_collisions()
if collisions:
    print(f"Found {len(collisions)} region collisions")
    for c in collisions:
        print(f"  {c}")
```

### Validation Workflow

```python
# Always validate before committing geometry
for name in ["barrier_1", "barrier_2", "barrier_3"]:
    assert mc.geometry.check_closed_region(name), f"{name} is not closed"

collisions = mc.geometry.check_collisions()
assert not collisions, "Region collisions detected"
```

---

## Adaptive Parameters

Adaptive parameters are named numeric values that can be linked to geometry dimensions, enabling parametric design.

### `get_adaptive_parameter_value(name)`

Returns the current value of a named adaptive parameter.

```python
barrier_width = mc.geometry.get_adaptive_parameter_value("barrier_1_width")
```

### `set_adaptive_parameter_value(name, value)`

Sets the value of a named adaptive parameter.

```python
mc.geometry.set_adaptive_parameter_value("barrier_1_width", 8.5)
```

### `set_adaptive_parameter_default(name, value)`

Sets the default (initial) value for an adaptive parameter.

```python
mc.geometry.set_adaptive_parameter_default("barrier_1_width", 10.0)
```

### Parametric Design Example

```python
# Define parametric barrier geometry
mc.geometry.set_adaptive_parameter_default("barrier_1_r_inner", 50.0)
mc.geometry.set_adaptive_parameter_default("barrier_1_r_outer", 80.0)
mc.geometry.set_adaptive_parameter_default("barrier_1_th_start", 0.0)
mc.geometry.set_adaptive_parameter_default("barrier_1_th_end", 30.0)

# Build region using parameters
r_in = mc.geometry.get_adaptive_parameter_value("barrier_1_r_inner")
r_out = mc.geometry.get_adaptive_parameter_value("barrier_1_r_outer")
# ... construct coordinates from these values ...

# Update parametrically
mc.geometry.set_adaptive_parameter_value("barrier_1_r_outer", 85.0)
# Region will rebuild with updated geometry
```

---

## Script Management

### `load_adaptive_script(filepath)`

Loads a previously saved adaptive geometry script and executes it.

| Parameter | Type | Description |
|---|---|---|
| `filepath` | `str` | Path to the adaptive geometry script file |

```python
mc.geometry.load_adaptive_script(r"D:\SRM\scripts\barrier_geometry.py")
```

### `save_adaptive_script(filepath)`

Saves the current adaptive geometry construction as a reusable Python script.

| Parameter | Type | Description |
|---|---|---|
| `filepath` | `str` | Output path for the script |

```python
mc.geometry.save_adaptive_script(r"D:\SRM\scripts\barrier_geometry.py")
```

### `reset_adaptive_geometry()`

Clears all adaptive geometry data, returning to the base MotorCAD geometry.

```python
mc.geometry.reset_adaptive_geometry()
```

---

## Tree-Based Geometry Management

### `get_geometry_tree()`

Returns the hierarchical geometry tree showing all regions, their types, and parent-child relationships.

```python
tree = mc.geometry.get_geometry_tree()
print(tree)
```

### `set_geometry_tree(tree)`

Sets the geometry tree from a previously retrieved or constructed tree structure.

```python
tree = mc.geometry.get_geometry_tree()
# Modify tree as needed
mc.geometry.set_geometry_tree(tree)
```

---

## Complete Workflow Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import (
    Region, Coordinate, Line, Arc, EntityList, RegionType
)

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\SRM\Motor _CAD\SRM_1.mot")
mc.show_magnetic_context()

# 1. Define adaptive parameters
mc.geometry.set_adaptive_parameter_default("b1_r_in", 50.0)
mc.geometry.set_adaptive_parameter_default("b1_r_out", 80.0)
mc.geometry.set_adaptive_parameter_default("b1_th_span", 30.0)

# 2. Build barrier geometry
r_in = mc.geometry.get_adaptive_parameter_value("b1_r_in")
r_out = mc.geometry.get_adaptive_parameter_value("b1_r_out")
span = mc.geometry.get_adaptive_parameter_value("b1_th_span")

p1 = Coordinate(r=r_in, th=-span/2)
p2 = Coordinate(r=r_out, th=-span/2)
p3 = Coordinate(r=r_out, th=span/2)
p4 = Coordinate(r=r_in, th=span/2)

entities = EntityList()
entities.add(Line(p1, p2))
entities.add(Arc(p2, p3, radius=r_out))
entities.add(Line(p3, p4))
entities.add(Arc(p4, p1, radius=r_in))

barrier = Region()
barrier.entities = entities
barrier.region_type = RegionType.Region

# 3. Validate
assert mc.geometry.get_entities_have_common_coordinate(entities)

# 4. Commit
mc.geometry.set_region("barrier_1", barrier)

# 5. Check
assert mc.geometry.check_closed_region("barrier_1")
collisions = mc.geometry.check_collisions()
assert not collisions

# 6. Save
mc.geometry.save_adaptive_script(r"D:\SRM\scripts\barrier_1.py")
mc.save_to_file(r"D:\SRM\Motor _CAD\adaptive_test.mot")
```

---

## Related Pages

- [[pymotorcad-geometry-objects]] — Region, Entity, Coordinate, Line, Arc types
- [[pymotorcad-geometry-shapes]] — pre-built shape constructors
- [[pymotorcad-geometry-drawing]] — visualisation and debug
- [[pymotorcad-geometry-fitting]] — fitting entities to coordinates
- [[pymotorcad-geometry-tree]] — tree-based geometry management
- [[pymotorcad-adaptive-templates-guide]] — adaptive geometry templates
- [[pymotorcad-fea-geometry]] — FEA geometry construction

---

## Tags

#pymotorcad #adaptive-geometry #regions #geometry-tree #validation #parametric-design #barrier-design #script-management
