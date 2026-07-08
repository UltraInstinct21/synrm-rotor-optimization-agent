---
type: motorcad_workflow
name: "Custom DXF Geometry Import"
purpose: "Import rotor geometry from DXF files into Adaptive Templates"
prerequisites: ["Motor-CAD v2024 R2+", "DXF file prepared"]
source_files: ["Custom DXF Geometry — pymotorcad-core.md"]
confidence: Verified
---

# Custom DXF Geometry Import

## Purpose

Import custom rotor geometry from DXF files and use it to replace standard template regions in Adaptive Templates.

## Prerequisites

Motor-CAD v2024 R2 or later.

## Step-by-Step Procedure

### 1. Prepare the Template

Before running the script, adjust Standard Template geometry to match the imported DXF:

```python
mc.set_array_variable("VShape_Magnet_ClearanceInner", 0, 0)  # Layer 1
mc.set_array_variable("VShape_Magnet_ClearanceInner", 1, 0)  # Layer 2
mc.set_array_variable("WebThickness_Array", 1, 18)
mc.set_array_variable("PoleArc_Array", 1, 105)
mc.set_array_variable("RotorCircularDuctLayer_RadialDiameter", 1, 123.8)
mc.set_array_variable("RotorCircularDuctLayer_ChannelDiameter", 1, 4.94)
```

### 2. Get Standard Template Regions

```python
standard_regions = [
    mc.get_region("Rotor Pocket_1"),
    mc.get_region("Rotor Pocket_2"),
    mc.get_region("Rotor Pocket_4"),
    mc.get_region("Rotor Pocket_5"),
    mc.get_region("RotorDuctFluidRegion_1"),
    mc.get_region("RotorDuctFluidRegion_2"),
]
```

### 3. Get Imported DXF Regions

```python
replacement_regions = [
    mc.get_region_dxf("DXFRegion_Rotor_6"),
    mc.get_region_dxf("DXFRegion_Rotor_7"),
    mc.get_region_dxf("DXFRegion_Rotor_10"),
    mc.get_region_dxf("DXFRegion_Rotor_11"),
    mc.get_region_dxf("DXFRegion_Rotor_14"),
    mc.get_region_dxf("DXFRegion_Rotor_12"),
]
```

### 4. Replace Regions

Indices must match between standard and replacement lists:

```python
for index in range(len(standard_regions)):
    standard_regions[index].replace(replacement_regions[index])
    mc.set_region(standard_regions[index])
```

## Key Methods

| Method | Description |
|--------|-------------|
| `get_region_dxf(name)` | Get an imported DXF region by name |
| `region.replace(other_region)` | Replace entities while keeping region properties |

## Pitfalls

- DXF region names appear under **Import** in the Geometry Tree
- Indices in standard_regions and replacement_regions must correspond
- Region properties (name, material, colour) are retained from the original

## Related Pages

- [[motorcad/api/adaptive-geometry-methods]] — `get_region_dxf()`
- [[motorcad/api/geometry-objects-functions]] — Region.replace()
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
