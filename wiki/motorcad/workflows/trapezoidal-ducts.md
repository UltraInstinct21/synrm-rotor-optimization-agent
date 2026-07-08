---
type: motorcad_workflow
name: "Trapezoidal Rotor Ducts"
purpose: "Convert rectangular rotor ducts to trapezoidal shape"
prerequisites: ["Motor-CAD", "e10 IPM template or similar"]
source_files: ["Trapezoidal ducts — pymotorcad-core.md"]
confidence: Verified
---

# Trapezoidal Rotor Ducts

## Purpose

Modify rectangular rotor ducts into trapezoidal shapes by adjusting the top line width.

## Step-by-Step Procedure

### 1. Setup Template

```python
mc.load_template("e10")
mc.set_variable("RotorDuctType", 4)  # Rectangular ducts
mc.set_array_variable("RotorCircularDuctLayer_ChannelWidth", 0, 4)
```

### 2. Set Adaptive Parameter

```python
mc.set_adaptive_parameter_default("Trapezoid_base_ratio", 0.7)
Trap_ratio = mc.get_adaptive_parameter_value("Trapezoid_base_ratio")
```

### 3. Modify Duct Geometry

For each rotor duct, find the top line (furthest from origin) and narrow it:

```python
for child_name in rt_region.child_names:
    if "RotorDuctFluidRegion" in child_name:
        duct_region = mc.get_region(child_name)
        for i, entity in enumerate(duct_region.entities):
            if round(entity.length / Trap_W, 2) == 1:
                Line_origin = check_line_origin_distance(i, duct_region)
                if not Line_origin:  # Top line (far from origin)
                    new_start_point = entity.get_coordinate_from_distance(
                        entity.start, fraction=(1 - Trap_ratio) / 2
                    )
                    new_end_point = entity.get_coordinate_from_distance(
                        entity.end, fraction=(1 - Trap_ratio) / 2
                    )
                    duct_region.edit_point(entity.start, new_start_point)
                    duct_region.edit_point(entity.end, new_end_point)
                    mc.set_region(duct_region)
```

## Key Functions

| Function | Purpose |
|----------|---------|
| `check_line_origin_distance()` | Identify top vs bottom line |
| `entity.get_coordinate_from_distance()` | Calculate new point along line |
| `region.edit_point()` | Move a vertex to new position |

## Related Pages

- [[motorcad/api/adaptive-geometry-methods]] — Adaptive geometry methods
- [[motorcad/api/geometry-objects-functions]] — Region, Line, Coordinate
- [[motorcad/workflows/oblong-stator-ducts]] — Oblong duct modification
