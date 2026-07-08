---
type: motorcad_workflow
name: "Converting IM Parallel Tooth Bar to Tapered"
purpose: "Modify induction motor rotor bar geometry from parallel to tapered tooth"
prerequisites: ["Motor-CAD", "IM template (e.g. i6a)"]
source_files: ["Converting IM parallel tooth bar to tapered tooth bar — pymotorcad-core.md"]
confidence: Verified
---

# Converting IM Parallel Tooth Bar to Tapered

## Purpose

Change the points at the bottom of a parallel tooth bar to create a tapered tooth bar geometry for induction motors.

## Step-by-Step Procedure

### 1. Load IM Template

```python
mc = pymotorcad.MotorCAD()
mc.reset_adaptive_geometry()
mc.load_template("i6a")
```

### 2. Get Bar Region and Define Parameters

```python
bar = mc.get_region("TopRotorBar")

# Get bottom corner points
point1 = bar.points[3]  # Away from x axis
point2 = bar.points[5]

# Define adaptive parameter for bottom tooth width
tooth_width_top = mc.get_variable("Rotor_Tooth_Width_T")
mc.set_adaptive_parameter_default("Rotor Tooth Width Bottom", 4)
tooth_width_bottom = mc.get_adaptive_parameter_value("Rotor Tooth Width Bottom")
```

### 3. Modify Point Positions

```python
point1_r, point_1_t = xy_to_rt(point1.x, point1.y)
# Calculate new angle from chord length
def chord_angle(cord_length, r):
    angle = 2 * math.asin(cord_length / (2 * r))
    return angle * 180 / math.pi
```

### 4. Update Region

Modify the bar region points to create the taper, then set the region back.

## Key Concepts

- Uses `xy_to_rt()` and `rt_to_xy()` for coordinate conversion
- Adaptive parameter controls bottom tooth width
- `chord_angle()` helper calculates angular position from chord length

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Coordinate, rt_to_xy, xy_to_rt
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
- [[motorcad/api/adaptive-geometry-methods]] — Adaptive geometry API
