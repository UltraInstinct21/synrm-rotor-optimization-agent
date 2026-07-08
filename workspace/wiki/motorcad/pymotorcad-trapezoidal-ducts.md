---
type: pymotorcad_example
title: Trapezoidal Rotor Ducts from Rectangular Geometry
source: PyMotorCAD Official Documentation — Adaptive Geometry Example e10
tags:
  - pymotorcad
  - adaptive-geometry
  - rotor
  - ducts
  - trapezoidal
  - ventilation
  - geometry
---

# Trapezoidal Rotor Ducts from Rectangular Geometry

Adaptive geometry example demonstrating how to convert rectangular rotor ventilation ducts into trapezoidal profiles for improved cooling performance and mechanical integrity.

---

## Template Reference

- **Motor-CAD Template:** `e10`
- **Example Type:** Adaptive geometry modification — rotor duct geometry
- **Use Case:** Rotor ventilation duct shape optimisation

---

## Overview

Rectangular rotor ducts are the default ventilation geometry in many Motor-CAD templates. Trapezoidal ducts can improve coolant flow distribution across the rotor radial depth and reduce stress concentrations at duct corners. This example modifies the duct geometry using adaptive region editing.

---

## Key Variables

| Variable | Motor-CAD Name | Description |
|---|---|---|
| Rotor Duct Type | `RotorDuctType` | Set to `4` for trapezoidal duct geometry |
| Channel Width | `RotorCircularDuctLayer_ChannelWidth` | Width of each duct channel (mm) |
| Trapezoid Base Ratio | `Trapezoid_base_ratio` | Ratio of bottom width to top width (defines taper) |

### Setting the Duct Type

```python
mc.set_variable("RotorDuctType", 4)
```

`RotorDuctType = 4` activates trapezoidal duct geometry in Motor-CAD's internal model. The `Trapezoid_base_ratio` parameter then controls the taper angle.

---

## Coordinate Comparison with `xy_to_rt()`

When modifying duct geometry, you often need to compare positions defined in Cartesian coordinates `(x, y)` against polar positions `(r, th)`. The `xy_to_rt()` function converts between these systems.

```python
# Convert Cartesian duct corner to polar for comparison
r, th = mc.geometry.xy_to_rt(x_cart, y_cart)
```

This is essential when:
- Reading existing duct geometry points (often in Cartesian)
- Comparing against polar-defined stator/rotor boundaries
- Validating that modified duct geometry remains within the rotor lamination

---

## Geometry Modification with `edit_point()`

The `edit_point()` method modifies individual vertices of an existing adaptive geometry region without rebuilding the entire region.

```python
# Edit a specific point in the duct region
mc.geometry.edit_point(region, point_index, new_coordinate)
```

### Workflow for Trapezoidal Conversion

1. **Read existing duct geometry** — retrieve current rectangular region coordinates
2. **Identify corner points** — determine which vertices define the duct width at top and bottom
3. **Apply taper** — use `edit_point()` to shift the bottom corners inward or outward based on `Trapezoid_base_ratio`
4. **Validate geometry** — ensure modified region is closed and does not overlap adjacent ducts
5. **Set region** — write modified geometry back to Motor-CAD

---

## Code Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate, Line, Arc, EntityList

mc = pymotorcad.MotorCAD()

# Set trapezoidal duct type
mc.set_variable("RotorDuctType", 4)

# Get duct parameters
channel_width = mc.get_variable("RotorCircularDuctLayer_ChannelWidth")
base_ratio = mc.get_variable("Trapezoid_base_ratio")

# Example: modify a single duct region
# Get existing region points
region = mc.geometry.get_region()  # current duct region

# Calculate taper offset
top_width = channel_width
bottom_width = channel_width * base_ratio
taper_offset = (top_width - bottom_width) / 2.0

# Edit corner points to create trapezoidal profile
# Point 0 and 1: top corners (unchanged)
# Point 2 and 3: bottom corners (shifted inward)
for point_idx in [2, 3]:
    current_point = region.points[point_idx]
    r, th = mc.geometry.xy_to_rt(current_point.x, current_point.y)

    # Shift radial position to create taper
    if point_idx == 2:
        new_r = r - taper_offset
    else:
        new_r = r + taper_offset

    new_coord = Coordinate(r=new_r, th=th)
    mc.geometry.edit_point(region, point_idx, new_coord)

# Write back to Motor-CAD
mc.geometry.set_region(region)
```

---

## Trapezoid Base Ratio Effect

| Base Ratio | Shape | Cooling Impact |
|---|---|---|
| 1.0 | Rectangular (no taper) | Baseline — uniform flow |
| 0.8 | Slight taper (narrower bottom) | Slightly reduced flow at inner radius |
| 0.6 | Moderate taper |显著 reduced inner-radius flow |
| 0.4 | Aggressive taper | Minimal flow near shaft |

The base ratio should be chosen based on the thermal gradient across the rotor. A ratio < 1.0 narrows the duct toward the shaft, reducing flow resistance at the outer radius where heat generation is typically higher.

---

## Design Considerations

### Thermal Performance
- Trapezoidal ducts can reduce hot spots by redistributing coolant flow
- Optimal base ratio depends on rotor loss distribution and cooling method (forced air, water jacket, etc.)

### Mechanical Integrity
- Tapered corners reduce stress concentration factors compared to rectangular ducts
- Must ensure minimum duct width at the narrow end is sufficient for coolant passage

### Manufacturing
- Trapezoidal ducts may require modified punching tools
- Consider whether the thermal benefit justifies tooling changes

---

## Cross-References

- [[pymotorcad-adaptive-geometry]] — region management and adaptive geometry pipeline
- [[pymotorcad-geometry-objects]] — Coordinate, xy_to_rt(), edit_point() definitions
- [[pymotorcad-oblong-stator-ducts]] — similar duct shape modification for stator
- [[pymotorcad-adaptive-templates-guide]] — template reference for adaptive geometry examples

---

## Tags

#pymotorcad #adaptive-geometry #rotor #ducts #trapezoidal #ventilation #cooling #geometry #edit-point
