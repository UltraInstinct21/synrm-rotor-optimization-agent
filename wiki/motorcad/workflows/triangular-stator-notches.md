---
type: motorcad_workflow
name: "Triangular Stator Notches"
purpose: "Create triangular stator notches to improve NVH performance"
prerequisites: ["Motor-CAD v2024.1.2+", "e10 IPM template"]
source_files: ["Triangular Stator Notches — pymotorcad-core.md"]
confidence: Verified
---

# Triangular Stator Notches

## Purpose

Add triangular notches to the stator bore surface to improve NVH performance.

## Adaptive Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `Notch Sweep` | 2 | Angular width of notch (deg) |
| `Notch Depth` | 1 | Radial depth into stator (mm) |

## Step-by-Step Procedure

### 1. Set Parameters

```python
mc.set_adaptive_parameter_default("Notch Sweep", 2)
mc.set_adaptive_parameter_default("Notch Depth", 1)
```

### 2. Create Notch Geometry

```python
stator_region = mc.get_region("Stator")
stator_radius = mc.get_variable("Stator_Bore") / 2
stator_centre = Coordinate(0, 0)

# Create triangular notch
notch = Region(region_type=RegionType.stator)
notch.name = "Stator_Notch"
notch.colour = (255, 255, 255)
notch.duplications = stator_region.duplications
notch.material = "Air"
notch.parent = stator_region

# Generate coordinates
x1, y1 = rt_to_xy(stator_radius, 0)
x2, y2 = rt_to_xy(stator_radius, notch_angular_width / 2)
x3, y3 = rt_to_xy(stator_radius + notch_depth, 0)

p1, p2, p3 = Coordinate(x1, y1), Coordinate(x2, y2), Coordinate(x3, y3)

# Create entities (anticlockwise)
airgap_arc = Arc(p1, p2, stator_centre, stator_radius)
line_1 = Line(p2, p3)
line_2 = Line(p3, p1)

notch.add_entity(airgap_arc)
notch.add_entity(line_1)
notch.add_entity(line_2)

if notch.is_closed():
    mc.set_region(notch)
```

### 3. Mirror for Symmetry

```python
symmetry_angle = (2 * math.pi) / stator_region.duplications / 2
symmetry_line = Line(
    stator_centre,
    Coordinate(stator_radius * math.cos(symmetry_angle), stator_radius * math.sin(symmetry_angle))
)
notch_mirror = notch.mirror(symmetry_line)
notch_mirror.name = "Stator_Notch_2"
notch_mirror.parent = stator_region

if notch_mirror.is_closed():
    mc.set_region(notch_mirror)
```

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region, Arc, Line, Coordinate
- [[motorcad/workflows/triangular-rotor-notches-ipm]] — Rotor variant
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
