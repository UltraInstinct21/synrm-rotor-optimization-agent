---
type: pymotorcad_api
title: PyMotorCAD Geometry Drawing and Visualisation
source: PyMotorCAD Official Documentation
tags:
  - pymotorcad
  - geometry
  - drawing
  - visualisation
  - debug
  - plotting
---

# PyMotorCAD Geometry Drawing and Visualisation

Functions for visualising adaptive geometry objects. Essential for debugging geometry construction, verifying region boundaries, and inspecting entity connectivity before committing geometry to MotorCAD.

---

## `draw_objects(objects, label_regions, ...)`

Renders a visual representation of geometry objects (regions, entities, coordinates) in MotorCAD's geometry display or a matplotlib window.

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `objects` | `list` | — | Geometry objects to draw (Region, EntityList, Coordinate lists) |
| `label_regions` | `bool` | `True` | Annotate regions with their names/types |
| `show_coords` | `bool` | `False` | Display coordinate labels at entity endpoints |
| `show_entities` | `bool` | `True` | Draw entity boundaries |
| `fill_regions` | `bool` | `False` | Fill closed regions with colour |

### Returns

None (display only).

### Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Region, Coordinate, Line, EntityList

mc = pymotorcad.MotorCAD()

# Build a simple region
start = Coordinate(r=50.0, th=0.0)
end = Coordinate(r=50.0, th=90.0)
line = Line(start, end)

entity_list = EntityList()
entity_list.add(line)

region = Region()
region.entities = entity_list

# Visualise
mc.geometry.draw_objects(
    objects=[region],
    label_regions=True,
    show_coords=True,
    fill_regions=True
)
```

### Use Cases

- **Barrier design:** verify barrier boundaries before running EMag analysis
- **Slot geometry:** confirm slot opening width and tooth tip angles
- **Magnet placement:** inspect magnet region positions in IPM rotors
- **Debugging:** identify open regions, overlapping entities, or misaligned coordinates

---

## `draw_objects_debug(objects)`

Enhanced debug visualisation that adds额外 diagnostic information:

- Entity connectivity arrows (direction of traversal)
- Coordinate values at every vertex
- Region closure status indicators
- Entity type labels (Line vs Arc vs Bezier)

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `objects` | `list` | Geometry objects to debug-draw |

### Returns

None (display only).

### Example

```python
# Debug visualisation of complex barrier geometry
mc.geometry.draw_objects_debug([barrier_region, magnet_region])
```

### Debug Output Indicators

| Indicator | Meaning |
|---|---|
| Green filled region | Closed, valid region |
| Red outline | Open or invalid region |
| Blue arrows | Entity traversal direction |
| Coordinate labels | `(r, th)` at each vertex |

---

## Drawing Workflow

A recommended workflow for verifying geometry before committing to MotorCAD:

```
1. Construct coordinates   →  Coordinate objects
2. Build entities          →  Line / Arc / Bezier entities
3. Assemble entity list    →  EntityList
4. Validate closure        →  get_entities_have_common_coordinate()
5. Visualise               →  draw_objects()
6. Debug if needed         →  draw_objects_debug()
7. Commit to MotorCAD      →  set_region() via adaptive geometry
```

### Example Workflow

```python
from ansys.motorcad.core.geometry import Coordinate, Line, Arc, EntityList, Region

# Step 1-3: Build geometry
p1 = Coordinate(r=50.0, th=0.0)
p2 = Coordinate(r=80.0, th=0.0)
p3 = Coordinate(r=80.0, th=30.0)
p4 = Coordinate(r=50.0, th=30.0)

e1 = Line(p1, p2)
e2 = Arc(p2, p3, radius=30.0)
e3 = Line(p3, p4)
e4 = Arc(p4, p1, radius=30.0)

entities = EntityList()
for e in [e1, e2, e3, e4]:
    entities.add(e)

# Step 4: Validate
assert mc.geometry.get_entities_have_common_coordinate(entities)

# Step 5-6: Visualise
region = Region()
region.entities = entities
mc.geometry.draw_objects([region], label_regions=True, fill_regions=True)
mc.geometry.draw_objects_debug([region])

# Step 7: Commit (see pymotorcad-adaptive-geometry)
mc.geometry.set_region("barrier_1", region)
```

---

## Common Drawing Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Region not displayed | Open entity list | Check endpoint connectivity with `get_entities_have_common_coordinate()` |
| Region appears hollow | `fill_regions=False` | Set `fill_regions=True` |
| Overlapping regions | Duplicate coordinates | Adjust coordinates or use [[pymotorcad-adaptive-geometry]] `check_collisions()` |
| Arc renders as straight line | Insufficient `num_points` | Increase interpolation points in Bezier/arc generation |
| Coordinates out of view | Radial values outside display range | Adjust MotorCAD viewport zoom |

---

## Related Pages

- [[pymotorcad-geometry-objects]] — core object types (Region, Entity, Coordinate, Line, Arc)
- [[pymotorcad-geometry-basic]] — fundamental geometry operations
- [[pymotorcad-geometry-shapes]] — pre-built shape constructors
- [[pymotorcad-adaptive-geometry]] — region management and committing geometry
- [[pymotorcad-geometry-fitting]] — fitting entities to coordinate sets

---

## Tags

#pymotorcad #geometry #drawing #visualisation #debug #plotting #region-display
