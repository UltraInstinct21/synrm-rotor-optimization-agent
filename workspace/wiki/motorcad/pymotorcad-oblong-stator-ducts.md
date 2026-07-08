---
type: pymotorcad_example
title: Oblong Stator Ducts with Thermal Area Adjustment
source: PyMotorCAD Official Documentation — Adaptive Geometry Example e10
tags:
  - pymotorcad
  - adaptive-geometry
  - stator
  - ducts
  - oblong
  - rounded
  - thermal
  - water-jacket
  - cooling
---

# Oblong Stator Ducts with Thermal Area Adjustment

Adaptive geometry example demonstrating how to convert rectangular stator ventilation ducts into oblong (rounded) shapes and adjust the thermal cross-sectional area for water jacket cooling analysis.

---

## Template Reference

- **Motor-CAD Template:** `e10`
- **Example Type:** Adaptive geometry modification — stator duct geometry with thermal adjustment
- **Use Case:** Stator ventilation duct shape optimisation for water-jacket cooled motors

---

## Overview

Oblong (stadium-shaped) stator ducts replace sharp rectangular corners with semicircular arcs, improving coolant flow characteristics and reducing pressure drop. When used with water jacket cooling, the effective thermal cross-sectional area must be adjusted to reflect the true duct geometry.

---

## Key Variables

| Variable | Motor-CAD Name | Description |
|---|---|---|
| Stator Duct Type | `StatorDuctType` | Set to `4` for oblong duct geometry |
| Circular Duct Layers | `CircularDuctLayers` | Number of duct layers in the stator |
| Housing Type | `HousingType` | Set to `0` for water jacket cooling |
| Channel CSArea Adjustment | `HousingWJ_Channel_CSArea_L1_A_Adjustment` | Thermal area correction factor for oblong shape |

### Setting the Duct Type

```python
mc.set_variable("StatorDuctType", 4)       # oblong ducts
mc.set_variable("HousingType", 0)          # water jacket cooling
```

---

## Arc Radius Calculation

The oblong shape is formed by replacing rectangular corners with semicircular arcs. The arc radius `r` for a duct of width `x` and height `y` is:

```
r = (x² + y²) / (2y)
```

Where:
- `x` = half-width of the duct
- `y` = half-height of the duct (or the offset from centre to the arc midpoint)

This formula ensures the arc passes through the duct corner points while maintaining a smooth curvature.

### Derivation

Given a duct corner at `(x, y)` and the arc centre at `(0, r)`:

```
x² + (y - r)² = r²
x² + y² - 2yr + r² = r²
x² + y² = 2yr
r = (x² + y²) / (2y)
```

---

## Code Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate, Line, Arc, EntityList

mc = pymotorcad.MotorCAD()

# Set oblong duct type
mc.set_variable("StatorDuctType", 4)
mc.set_variable("HousingType", 0)

# Get duct parameters
duct_width = mc.get_variable("StatorDuct_Width")
duct_height = mc.get_variable("StatorDuct_Height")

# Calculate arc radius for oblong shape
half_w = duct_width / 2.0
half_h = duct_height / 2.0
arc_radius = (half_w**2 + half_h**2) / (2.0 * half_h)

# Build oblong duct region
# Rectangular body with semicircular ends
entities = EntityList()

# Bottom arc (semicircle at bottom of duct)
bottom_centre = Coordinate(x=0.0, y=-half_h + arc_radius)
bottom_start = Coordinate(x=-half_w, y=-half_h)
bottom_end = Coordinate(x=half_w, y=-half_h)

# Right line (vertical)
right_start = Coordinate(x=half_w, y=-half_h)
right_end = Coordinate(x=half_w, y=half_h)

# Top arc (semicircle at top of duct)
top_centre = Coordinate(x=0.0, y=half_h - arc_radius)
top_start = Coordinate(x=half_w, y=half_h)
top_end = Coordinate(x=-half_w, y=half_h)

# Left line (vertical)
left_start = Coordinate(x=-half_w, y=half_h)
left_end = Coordinate(x=-half_w, y=-half_h)

# Add entities in anticlockwise order
entities.add(Line(bottom_start, right_start))
entities.add(Arc(right_start, top_start, radius=arc_radius))
entities.add(Line(top_start, left_start))
entities.add(Arc(left_start, bottom_start, radius=arc_radius))

# Validate and set region
if mc.geometry.get_entities_have_common_coordinate(entities):
    mc.geometry.set_region(entities)
else:
    print("Warning: oblong duct region not closed")
```

---

## Thermal Area Adjustment

When `HousingType = 0` (water jacket cooling), Motor-CAD uses the duct cross-sectional area to calculate thermal resistance. Converting from rectangular to oblong ducts changes the effective area, requiring an adjustment.

### Adjustment Variable

```python
mc.set_variable("HousingWJ_Channel_CSArea_L1_A_Adjustment", adjustment_factor)
```

The adjustment factor is the ratio of the oblong area to the original rectangular area:

```
adjustment_factor = A_oblong / A_rectangular
```

### Area Calculation

| Shape | Area Formula |
|---|---|
| Rectangular | `A = width × height` |
| Oblong (stadium) | `A = width × height + π × r²` where `r` is the arc radius |

The adjustment ensures the thermal solver uses the correct duct geometry for water jacket heat transfer calculations.

---

## Workflow Steps

1. **Set duct type** — `StatorDuctType = 4` for oblong geometry
2. **Set housing type** — `HousingType = 0` for water jacket
3. **Read duct dimensions** — get width and height from Motor-CAD variables
4. **Calculate arc radius** — `r = (x² + y²) / (2y)`
5. **Build region geometry** — construct lines and arcs for the oblong shape
6. **Validate closure** — check that entities form a closed region
7. **Set region** — write geometry to Motor-CAD
8. **Calculate thermal adjustment** — compute area ratio and set adjustment variable
9. **Run thermal analysis** — `do_steady_state_analysis()` to evaluate cooling performance

---

## Design Considerations

### Thermal Performance
- Oblong ducts have ~10–20% larger cross-sectional area than equivalent rectangles
- Reduced pressure drop allows higher coolant flow rates
- Smoother corners reduce turbulence and improve heat transfer coefficient

### Mechanical
- Rounded corners reduce stress concentration in stator lamination
- Improved fatigue life under thermal cycling

### Manufacturing
- Oblong ducts require modified punching tools compared to rectangular
- Consider tooling cost vs. thermal benefit for production volumes

---

## Cross-References

- [[pymotorcad-adaptive-geometry]] — region management and adaptive geometry pipeline
- [[pymotorcad-geometry-objects]] — Coordinate, Line, Arc, EntityList definitions
- [[pymotorcad-trapezoidal-ducts]] — similar duct shape modification for rotor
- [[pymotorcad-adaptive-templates-guide]] — template reference for adaptive geometry examples

---

## Tags

#pymotorcad #adaptive-geometry #stator #ducts #oblong #rounded #thermal #water-jacket #cooling #geometry #arc-radius
