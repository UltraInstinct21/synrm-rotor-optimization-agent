---
type: motorcad_api
method_group: "Geometry Shapes"
module: "ansys.motorcad.core.geometry_shapes"
source_files: ["Geometry shapes — pymotorcad-core.md"]
confidence: Verified
---

# Geometry Shapes

Predefined functions to create common geometry regions.

## Functions

| Function | Description |
|----------|-------------|
| `square(width, r_O, th_O, region_type=None)` | Create square at given coordinates |
| `eq_triangle_h(height, r_O, th_O, ...)` | Create equilateral triangle by height |
| `eq_triangle_w(width, r_O, th_O, ...)` | Create equilateral triangle by width |
| `triangular_notch(radius, sweep, ...)` | Create triangular notch for rotor or stator |

## triangular_notch Parameters

| Parameter | Description |
|-----------|-------------|
| `radius` | Radial position of notch outer edge (rotor radius) |
| `sweep` | Sweep along airgap in degrees (defines width) |
| `centre_angle` | Angular position of notch centre |
| `depth` | Depth of the notch |

## Importing

```python
from ansys.motorcad.core.geometry_shapes import triangular_notch
```

## Usage Example

```python
notch = triangular_notch(rotor_radius, 5, 22.5, 1)
notch.name = "Rotor_Notch_1"
notch.material = "Air"
notch.parent = rotor_region
if notch.is_closed():
    mc.set_region(notch)
```

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region, Line, Arc primitives
- [[motorcad/workflows/triangular-rotor-notches-ipm]] — Example: rotor notches
- [[motorcad/workflows/triangular-stator-notches]] — Example: stator notches
