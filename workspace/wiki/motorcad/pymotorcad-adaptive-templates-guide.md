---
type: pymotorcad_guide
title: "Adaptive Templates Guide"
source: "PyMotorCAD Documentation"
tags:
  - pymotorcad
  - adaptive-templates
  - geometry
  - API
  - region
  - workflow
aliases: ["Adaptive Templates", "Adaptive Geometry"]
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM", "BLDC", "SRM"]
---

# Adaptive Templates Guide

## Overview

Adaptive Templates allow programmatic creation and modification of motor geometry using the PyMotorCAD API. This guide covers the complete workflow for defining rotor and stator geometries from scratch or by modifying existing templates.

**Requirements:** MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+

---

## Core API Pattern

The fundamental workflow for adaptive geometry operations:

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# 1. Reset adaptive geometry
mc.reset_adaptive_geometry()

# 2. Get existing region
region = mc.get_region("RegionName")

# 3. Modify region entities
# ... add arcs, lines, etc.

# 4. Set the region back
mc.set_region(region)
```

---

## Geometry Library

The `ansys.motorcad.core.geometry` module provides primitives for defining regions.

### Region

The top-level container for geometry entities.

```python
from ansys.motorcad.core.geometry import Region, RegionType, Coordinate, Line, Arc

region = Region()
region.name = "Rotor Lam"
region.colour = (255, 0, 0)  # RGB tuple
region.material = "Steel_1008"
region.duplications = 4  # Number of pole duplications
```

**Properties:**
| Property | Type | Description |
|---|---|---|
| `name` | str | Region name displayed in MotorCAD |
| `colour` | tuple | RGB colour (0-255 per channel) |
| `material` | str | Material name from MotorCAD library |
| `duplications` | int | Number of symmetry duplications |
| `parent` | str | Parent region name |
| `entities` | list | Geometry entities (lines, arcs) |

### RegionType

Enum defining region type classifications.

```python
from ansys.motorcad.core.geometry import RegionType

# Available types
RegionType.STATOR_ROTOR_LAM  # Lamination region
RegionType.MAGNET            # Magnet region
RegionType.SHAFT             # Shaft region
RegionType.SLOT_LINER        # Slot liner
RegionType.WINDING           # Winding region
RegionType.AIR               # Air region
RegionType.FRAME             # Frame
```

### Coordinate

Represents a point in 2D space.

```python
from ansys.motorcad.core.geometry import Coordinate

# Cartesian coordinates
coord = Coordinate(x=10.0, y=5.0)

# From polar coordinates using rt_to_xy
coord = rt_to_xy(r=50.0, theta=45.0)
```

### Line

A straight line segment between two coordinates.

```python
from ansys.motorcad.core.geometry import Line, Coordinate

start = Coordinate(x=0, y=0)
end = Coordinate(x=10, y=0)
line = Line(start, end)
```

### Arc

A circular arc defined by start point, end point, and either centre point or radius.

```python
from ansys.motorcad.core.geometry import Arc, Coordinate

start = Coordinate(x=10, y=0)
end = Coordinate(x=0, y=10)
centre = Coordinate(x=0, y=0)

# Method 1: arc from centre
arc = Arc(start, end, centre)

# Method 2: arc from radius
arc = Arc(start, end, radius=14.14)
```

### rt_to_xy / xy_to_rt

Coordinate conversion utilities between polar and Cartesian.

```python
from ansys.motorcad.core.geometry import rt_to_xy, xy_to_rt

# Polar to Cartesian
x, y = rt_to_xy(r=50.0, theta=45.0)

# Cartesian to polar
r, theta = xy_to_rt(x=35.36, y=35.36)
```

---

## Geometry Shapes

The `ansys.motorcad.core.geometry.shapes` module provides pre-built shapes.

### triangular_notch

Creates a triangular notch (barrier) shape commonly used in SynRM rotors.

```python
from ansys.motorcad.core.geometry.shapes import triangular_notch

# Parameters
centre = (100.0, 0.0)  # Centre of notch (x, y)
width = 15.0           # Notch width in mm
height = 20.0          # Notch height in mm

notch = triangular_notch(centre, width, height)
# Returns list of Line/Arc entities forming the closed notch
```

---

## Region Workflow (Step by Step)

### 1. Create Region

```python
from ansys.motorcad.core.geometry import Region, RegionType, Coordinate, Line, Arc

mc.reset_adaptive_geometry()

# Create a new region
rotor_lam = Region()
rotor_lam.name = "Rotor_Lam"
rotor_lam.colour = (0, 128, 255)
rotor_lam.material = "50C250"
rotor_lam.duplications = 4
```

### 2. Add Entities (Anticlockwise)

All entities must be added in **anticlockwise order** to form a valid closed region.

```python
# Define key coordinates
r_shaft = 40.0
r_rotor_outer = 107.0
theta_start = 0.0
theta_end = 90.0  # Quarter pole (4-pole motor)

# Convert polar to Cartesian
start_shaft = rt_to_xy(r_shaft, theta_start)
end_shaft = rt_to_xy(r_shaft, theta_end)
start_outer = rt_to_xy(r_rotor_outer, theta_start)
end_outer = rt_to_xy(r_rotor_outer, theta_end)

# Add entities anticlockwise
rotor_lam.add_entity(Line(start_shaft, end_shaft))      # Shaft arc approximation (line for simplicity)
rotor_lam.add_entity(Arc(end_shaft, start_outer, centre=Coordinate(0, 0)))  # Outer arc
rotor_lam.add_entity(Line(start_outer, end_outer))       # Radial line
rotor_lam.add_entity(Arc(end_outer, start_shaft, centre=Coordinate(0, 0))) # Inner arc
```

### 3. Set Parent Region (if applicable)

```python
rotor_lam.parent = "Rotor"  # Set parent region
```

### 4. Verify Closed Region

Before setting the region, verify the geometry forms a closed loop:

```python
# Check that start point of first entity equals end point of last entity
first_start = rotor_lam.entities[0].start
last_end = rotor_lam.entities[-1].end

if first_start != last_end:
    raise ValueError("Region is not closed!")
```

### 5. Set Region in MotorCAD

```python
mc.set_region(rotor_lam)
```

---

## Adaptive Parameters

Adaptive parameters allow parameterized geometry definitions.

### Setting Defaults

```python
mc.set_adaptive_parameter_default("barrier_width", 15.0)
mc.set_adaptive_parameter_default("barrier_depth", 20.0)
mc.set_adaptive_parameter_default("rib_thickness", 1.0)
```

### Getting and Setting Values

```python
# Get current value
width = mc.get_adaptive_parameter_value("barrier_width")

# Set new value
mc.set_adaptive_parameter_value("barrier_width", 18.0)
```

### Using Parameters in Geometry

```python
width = mc.get_adaptive_parameter_value("barrier_width")
depth = mc.get_adaptive_parameter_value("barrier_depth")

# Use in geometry definitions
centre = (100.0, 0.0)
notch = triangular_notch(centre, width, depth)
```

---

## DXF Import

Import regions from DXF files using the geometry library.

```python
from ansys.motorcad.core.geometry import Region

# Import region from DXF file
region = Region.from_dxf("path/to/geometry.dxf")

# Or use mc method
region = mc.get_region_dxf("dxf_layer_name")

# Modify imported region
region.name = "Modified_Region"
region.material = "New_Material"

# Replace region in model
mc.set_region(region)
```

### Region.replace()

Replace an existing region with a new one:

```python
# Get existing region
old_region = mc.get_region("Old_Region")

# Create new region (or modify existing)
new_region = Region()
new_region.name = "New_Region"
# ... add entities ...

# Replace
old_region.replace(new_region)
mc.set_region(old_region)
```

---

## Best Practices

### IDE Setup

- Use VS Code or PyCharm with MotorCAD IntelliSense
- Enable type hints for better code completion
- Install the MotorCAD extension for VS Code if available

### Debugging

```python
# Use open_new_instance=False for faster development
mc = pymotorcad.MotorCAD(open_new_instance=False)

# Set breakpoints in your IDE after reset_adaptive_geometry()
# Inspect region objects before calling set_region()

# Use MessageDisplayState for debugging output
mc.set_variable("MessageDisplayState", 2)
```

### Common Pitfalls

1. **Entities not anticlockwise** → MotorCAD rejects the region
2. **Non-closed region** → Always verify start/end points match
3. **Missing material** → Region will use default or error
4. **Wrong duplications** → Ensure pole count matches `duplications`
5. **Region name conflicts** → Use unique names per region

---

## Complete Example: SynRM Rotor Barrier

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import (
    Region, RegionType, Coordinate, Line, Arc, rt_to_xy
)
from ansys.motorcad.core.geometry.shapes import triangular_notch

mc = pymotorcad.MotorCAD()
mc.reset_adaptive_geometry()

# Define parameters
shaft_r = 40.0
rotor_od = 214.0
airgap = 0.5
rotor_r = rotor_od / 2 - airgap
pole_pitch = 360 / 4  # 4-pole motor

# Rotor lamination region
rotor = Region()
rotor.name = "Rotor_Lam"
rotor.material = "50C250"
rotor.duplications = 4

# Build geometry entities anticlockwise
theta = 0
p1 = rt_to_xy(shaft_r, theta)
p2 = rt_to_xy(rotor_r, theta)
p3 = rt_to_xy(rotor_r, pole_pitch)
p4 = rt_to_xy(shaft_r, pole_pitch)

rotor.add_entity(Arc(p1, p2, centre=Coordinate(0, 0)))
rotor.add_entity(Line(p2, p3))
rotor.add_entity(Arc(p3, p4, centre=Coordinate(0, 0)))
rotor.add_entity(Line(p4, p1))

mc.set_region(rotor)

# Add barrier notches
barrier_width = mc.get_adaptive_parameter_value("barrier_width")
barrier_depth = mc.get_adaptive_parameter_value("barrier_depth")
barrier_centre = rt_to_xy(rotor_r * 0.6, pole_pitch / 2)

barrier = Region()
barrier.name = "Barrier_1"
barrier.material = "Air"
barrier.parent = "Rotor_Lam"

notch_entities = triangular_notch(barrier_centre, barrier_width, barrier_depth)
for entity in notch_entities:
    barrier.add_entity(entity)

mc.set_region(barrier)

# Run calculation
mc.show_magnetic_context()
mc.do_magnetic_calculation()
```

---

## Related Pages

- [[pymotorcad-adaptive-geometry]] — Detailed geometry object reference
- [[pymotorcad-geometry-objects]] — Coordinate, Line, Arc, Region API reference
- [[pymotorcad-calculations-api]] — EMag calculation methods
- [[pymotorcad-set-variable]] — Variable setting API
- [[pymotorcad-get-variable]] — Variable reading API
- [[pymotorcad-emag-example]] — Complete EMag workflow example
