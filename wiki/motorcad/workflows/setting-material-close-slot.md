---
type: motorcad_workflow
name: "Setting Material Properties to Close Slot"
purpose: "Convert slot opening air region to steel for closed-slot modeling"
prerequisites: ["Motor-CAD", "Adaptive Templates"]
source_files: ["Setting material properties to close slot — pymotorcad-core.md"]
confidence: Verified
---

# Setting Material Properties to Close Slot

## Purpose

Change the air region in the slot opening to steel material to model a closed slot configuration.

## Step-by-Step Procedure

```python
import ansys.motorcad.core as pymotorcad
import ansys.motorcad.core.geometry as geo

mc = pymotorcad.MotorCAD()
mc.reset_adaptive_geometry()

# Get the air region in slot opening
stator_air = mc.get_region("StatorAir")
stator = mc.get_region("Stator")

# Copy material properties from stator
stator_air.material = stator.material
stator_air.colour = stator.colour

# Set to laminated region type
stator_air._region_type = geo.RegionType.adaptive
stator_air.lamination_type = "Laminated"

mc.set_region(stator_air)

# Load adaptive template script if running externally
if not pymotorcad.is_running_in_internal_scripting():
    mc.set_variable("GeometryTemplateType", 1)
    mc.load_adaptive_script(sys.argv[0])
```

## Key Pattern

- Copy material from existing region: `stator_air.material = stator.material`
- Force region type to adaptive: `region._region_type = geo.RegionType.adaptive`
- Set lamination type: `region.lamination_type = "Laminated"`

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region properties
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
- [[motorcad/workflows/material-mesh-properties]] — Material and mesh properties
