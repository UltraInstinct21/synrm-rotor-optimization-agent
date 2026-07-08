---
type: motorcad_api
method_group: "Geometry Drawing"
module: "ansys.motorcad.core.geometry_drawing"
source_files: ["Geometry drawing — pymotorcad-core.md"]
confidence: Verified
---

# Geometry Drawing Methods

Functions to visualize Motor-CAD geometry objects.

## Functions

| Function | Description |
|----------|-------------|
| `draw_objects(objects, label_regions=False, ...)` | Draw geometry objects on a plot |
| `draw_objects_debug(objects)` | Draw regions if not running in Motor-CAD |

## Importing

```python
from ansys.motorcad.core.geometry_drawing import draw_objects
from ansys.motorcad.core.geometry_drawing import draw_objects_debug
```

## Usage

```python
# Draw regions with labels
draw_objects([rotor_region, stator_region], label_regions=True)

# Draw with points for debugging
draw_objects(pockets, label_regions=True, draw_points=True)

# Debug mode (only draws from external IDE)
draw_objects_debug([stator, corners[0], corners[1]])
```

## Options

- `label_regions=True` — Show region names
- `draw_points=True` — Show vertex points
- `draw_internal=True` — Draw from Motor-CAD scripting interface
- `axes=False` — Hide axes

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region objects
- [[motorcad/workflows/adaptive-templates-scripting]] — Using draw_objects in workflows
