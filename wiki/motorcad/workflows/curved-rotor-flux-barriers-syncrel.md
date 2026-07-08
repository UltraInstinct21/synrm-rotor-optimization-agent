---
type: motorcad_workflow
name: "Curved Rotor Flux Barriers for SYNCREL"
purpose: "Create curved flux barrier pockets for SYNCREL U-Shape rotor"
prerequisites: ["Motor-CAD v2024.1.2+", "PyMotorCAD v0.4.1+", "i3 template"]
source_files: ["Curved Rotor Flux Barriers for SYNCREL U-Shape — pymotorcad-core.md"]
confidence: Verified
---

# Curved Rotor Flux Barriers for SYNCREL U-Shape

## Purpose

Alter SYNCREL U-Shape rotor template to use curved rotor pockets instead of straight edges.

## Prerequisites

- Motor-CAD v2024.1.2 or later
- PyMotorCAD v0.4.1 or later
- Template "i3" (SYNCREL U-Shape)

**Limitations:** Does not support zero inner/outer layer thickness or inner/outer posts.

## Step-by-Step Procedure

### 1. Define Helper Functions

```python
def get_barrier_centre_and_radius(coordinate_1, coordinate_2, coordinate_3, arc_direction):
    """Calculate arc centre and radius from three coordinates."""
    # ... (circumcircle calculation)
    return radius, centre

def get_pockets_include_corner_rounding():
    """Check if corner rounding is enabled."""
    return (mc.get_variable("CornerRounding_Rotor") == 1) and (
        mc.get_variable("CornerRoundingRadius_Rotor") > 0
    )

def get_rotor_mirror_line():
    """Create mirror line through rotor from origin to airgap."""
    rotor_radius = mc.get_variable("RotorDiameter")
    number_poles = mc.get_variable("Pole_Number")
    airgap_centre_x, airgap_centre_y = rt_to_xy(rotor_radius, (360 / number_poles) / 2)
    return Line(Coordinate(0, 0), Coordinate(airgap_centre_x, airgap_centre_y))
```

### 2. Update Pocket Geometry

```python
def update_pocket_geometry(pocket, coordinates):
    """Replace straight edges with arcs using three coordinates per arc."""
    entities = []
    for element in range(0, len(coordinates), 3):
        arc_direction = -1 if (element + 1) % 2 == 0 else 1
        radius, centre = get_barrier_centre_and_radius(
            coordinates[element], coordinates[element + 1], coordinates[element + 2],
            arc_direction
        )
        entities.append(Arc(coordinates[element], coordinates[element + 1], centre, radius))
    # Remove old entities, insert new arcs
    # ...
```

### 3. Process Each Layer

```python
number_layers = mc.get_variable("Magnet_Layers")
for layer in range(number_layers):
    outer_thickness = mc.get_array_variable("UShape_Thickness_Outer_Array", layer)
    inner_thickness = mc.get_array_variable("UShape_Thickness_Inner_Array", layer)
    centre_post_width = mc.get_array_variable("UShape_CentrePost_Array", layer)

    pocket_left = mc.get_region(get_pocket_name(pocket_number))

    if centre_post_width == 0:
        new_coordinates = get_coordinates_no_centre_post(pocket_left)
    else:
        new_coordinates = get_coordinates_centre_post(pocket_left)

    update_pocket_geometry(pocket_left, new_coordinates)
    pocket_number += 1

    if pocket_left.is_closed():
        mc.set_region(pocket_left)

    if centre_post_width > 0:
        pocket_right = pocket_left.mirror(get_rotor_mirror_line(), unique_name=False)
        pocket_right.name = get_pocket_name(pocket_number)
        pocket_number += 1
        if pocket_right.is_closed():
            mc.set_region(pocket_right)
```

## Key Design Patterns

- **Helper functions** encapsulate repeated geometry calculations
- **Layer loop** processes each magnet layer identically
- **Mirror symmetry** used to create matching right-side pockets
- **Corner rounding** handled conditionally based on Motor-CAD settings

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region, Arc, Line, Coordinate
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
- [[motorcad/workflows/bezier-curve-rotor-pockets]] — Bezier pockets for IPM
- [[motorcad/workflows/triangular-rotor-notches-ipm]] — Notches for IPM
