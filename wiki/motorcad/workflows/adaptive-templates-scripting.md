---
type: motorcad_workflow
name: "Adaptive Templates Scripting"
purpose: "Custom geometric parameterisations beyond standard Motor-CAD templates"
prerequisites: ["Motor-CAD v2024.1.2+", "PyMotorCAD v0.4.1+"]
source_files: ["Motor-CAD adaptive templates scripting — pymotorcad-core.md"]
confidence: Verified
---

# Adaptive Templates Scripting

## Purpose

Create custom motor geometries that cannot be represented by standard templates. Scripts define geometry using Python, can be run internally or externally.

## Prerequisites

- Motor-CAD v2024.1.2 or later
- PyMotorCAD v0.4.1 or later

## Step-by-Step Procedure

### 1. Enable Adaptive Templates

**Geometry → Editor → Adaptive Templates → Geometry Templates Type → Adaptive**

### 2. Write the Script

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Arc, Coordinate, Line, Region, RegionType

mc = pymotorcad.MotorCAD(open_new_instance=False)

# CRITICAL: Reset geometry first
mc.reset_adaptive_geometry()

# Get existing region
rotor = mc.get_region("Rotor")

# Create new region
notch = Region(region_type=RegionType.rotor_air)
notch.name = "Rotor_Notch_1"
notch.material = "Air"
notch.colour = (255, 255, 255)
notch.duplications = rotor.duplications
notch.parent = rotor  # Motor-CAD handles subtraction

# Add entities (anticlockwise order!)
notch.add_entity(line_1)
notch.add_entity(line_2)
notch.add_entity(airgap_arc)

if notch.is_closed():
    mc.set_region(notch)
```

### 3. Adaptive Parameters

```python
# Set default if parameter doesn't exist
mc.set_adaptive_parameter_default("Notch Depth", 1)

# Read parameter value
depth = mc.get_adaptive_parameter_value("Notch Depth")

# Set parameter value
mc.set_adaptive_parameter_value("Notch Depth", 2)
```

Parameters appear in **Geometry → Editor → Adaptive Parameters** and **Geometry → Radial** tabs.

### 4. Working from External IDE

1. Set Geometry Templates Type to Adaptive
2. Save script to file
3. Tick "Use External IDE"
4. Open with default IDE or choose specific IDE
5. Use `open_new_instance=False` when connecting

### 5. Key Rules

- **Always call `mc.reset_adaptive_geometry()` before getting/setting geometry**
- Entities must be added in **anticlockwise order**
- Check `region.is_closed()` before `set_region()`
- Parent regions handle subtraction automatically

## Variables to Set

| Variable | Purpose |
|----------|---------|
| `GeometryTemplateType` | 1 = Adaptive, 0 = Standard |

## Outputs to Capture

- Modified geometry regions via `get_region()`
- Geometry drawing via `draw_objects()`

## Pitfalls

- Never change a parameter on the currently displayed tab
- Display Scripting tab before parameter changes: `mc.display_screen("scripting")`
- In Jupyter, pass explicit path to `load_adaptive_script()`, not `sys.argv[0]`
- Entities not in anticlockwise order → geometry issues, FEA failure

## Related Pages

- [[motorcad/api/adaptive-geometry-methods]] — All adaptive geometry API methods
- [[motorcad/api/geometry-objects-functions]] — Region, Line, Arc objects
- [[motorcad/api/geometry-shapes]] — triangular_notch, square, etc.
- [[motorcad/api/geometry-drawing-methods]] — draw_objects for debugging
- [[motorcad/workflows/triangular-rotor-notches-ipm]] — Example: rotor notches
- [[motorcad/workflows/bezier-curve-rotor-pockets]] — Example: Bezier pockets
- [[motorcad/workflows/curved-rotor-flux-barriers-syncrel]] — Example: curved barriers
