---
type: pymotorcad_example
title: Material and Mesh Properties for Adaptive Geometry
source: PyMotorCAD Official Documentation — Adaptive Geometry Example
tags:
  - pymotorcad
  - adaptive-geometry
  - material
  - mesh
  - FEA
  - region-properties
  - lamination
---

# Material and Mesh Properties for Adaptive Geometry

Guide to assigning material, mesh, and lamination properties to adaptive geometry regions in Motor-CAD. Covers the region property workflow, property definitions, and practical examples.

---

## Overview

After creating adaptive geometry regions, each region must be assigned physical properties before Motor-CAD can run electromagnetic or thermal FEA. Properties include material assignment, mesh length control, lamination type, duplication count, and parent-child relationships between regions.

---

## Region Properties

Each adaptive geometry region can carry the following properties:

| Property | Description | Example Values |
|---|---|---|
| `material` | Material name assigned to the region | `"50C250"`, `"4340 Steel"`, `"Copper"` |
| `mesh_length` | Maximum mesh element length (mm) | `1.0`, `2.0`, `5.0` |
| `lamination_type` | Lamination classification | `"Lam"`, `"Solid"`, `"None"` |
| `duplications` | Number of angular duplications (for periodic geometry) | `1`, `4`, `12` |
| `parent` | Parent region for hierarchical geometry | `"Stator"`, `"Rotor"` |

---

## Workflow

The standard workflow for assigning properties to adaptive geometry regions:

```
reset_adaptive_geometry()
    ↓
get_region()       ← read existing region
    ↓
Set properties     ← assign material, mesh, lamination, etc.
    ↓
set_region()       ← write region back to Motor-CAD
```

### Step 1: Reset Adaptive Geometry

Clear any existing adaptive geometry to start fresh:

```python
mc.reset_adaptive_geometry()
```

### Step 2: Get Region

Read an existing region to modify its properties:

```python
region = mc.geometry.get_region("RotorBand")
```

### Step 3: Set Properties

Assign material, mesh length, and other properties to the region object:

```python
region.material = "4340 Steel"
region.mesh_length = 2.0
region.lamination_type = "Solid"
region.duplications = 1
region.parent = "Rotor"
```

### Step 4: Set Region

Write the modified region back to Motor-CAD:

```python
mc.geometry.set_region(region, "RotorBand")
```

---

## Code Example: Rotor Band with 4340 Steel

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Reset adaptive geometry
mc.reset_adaptive_geometry()

# Get the rotor band region
region = mc.geometry.get_region("RotorBand")

# Assign material and mesh properties
region.material = "4340 Steel"        # high-strength steel for rotor band
region.mesh_length = 2.0              # 2 mm max element size
region.lamination_type = "Solid"      # solid (non-laminated) construction
region.duplications = 1               # no angular duplication needed
region.parent = "Rotor"               # parent region

# Write back to Motor-CAD
mc.geometry.set_region(region, "RotorBand")

print("Rotor band material and mesh properties assigned")
```

---

## Lamination Type Options

| Type | Description | Use Case |
|---|---|---|
| `"Lam"` | Laminated steel | Stator and rotor cores |
| `"Solid"` | Solid (non-laminated) | Rotor bands, shafts, end rings |
| `"None"` | No lamination | Air regions, copper, magnets |

The lamination type affects how Motor-CAD computes eddy current losses:
- **Lam** — losses computed using lamination thickness and stacking factor
- **Solid** — full eddy current losses in solid conductor
- **None** — no eddy current losses (non-conductive regions)

---

## Mesh Length Control

The `mesh_length` property controls the maximum element size in the FEA mesh for that region. Smaller values produce finer meshes with higher accuracy but longer computation times.

### Guidelines

| Region Type | Recommended Mesh Length |
|---|---|
| Airgap | 0.5–1.0 mm |
| Rotor/stator teeth | 1.0–2.0 mm |
| Rotor/stator yoke | 2.0–5.0 mm |
| Bars / windings | 1.0–2.0 mm |
| Rotor band | 2.0–3.0 mm |
| magnets | 1.0–2.0 mm |

Fine mesh in the airgap is critical for accurate torque calculation. Coarser mesh in the yoke is acceptable where flux gradients are lower.

---

## Duplication Property

The `duplications` property specifies how many angular copies of the region exist in the full motor geometry. This is used for periodic symmetry exploitation.

```python
# 4-pole motor: 4 duplications of each rotor region
region.duplications = 4

# Fractional-slot winding: may need non-integer duplication handling
region.duplications = 12
```

Motor-CAD uses duplication count to:
- Reduce FEA model size by modelling only one pole/slot pitch
- Correctly apply periodic boundary conditions
- Account for angular offset between duplicated regions

---

## Parent-Child Relationships

The `parent` property establishes a hierarchical relationship between regions. Child regions are meshed within the boundary of their parent.

```python
# Rotor band is a child of the rotor
region.parent = "Rotor"

# Slot liner is a child of the stator slot
region.parent = "StatorSlot"
```

This hierarchy ensures:
- Correct mesh generation (child regions constrained within parent boundary)
- Proper material assignment cascade
- Logical grouping for post-processing

---

## Complete Example: Multi-Region Property Assignment

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Reset and rebuild adaptive geometry
mc.reset_adaptive_geometry()

# Define region properties
region_properties = {
    "RotorBand": {
        "material": "4340 Steel",
        "mesh_length": 2.0,
        "lamination_type": "Solid",
        "duplications": 1,
        "parent": "Rotor",
    },
    "RotorCore": {
        "material": "50C250",
        "mesh_length": 2.0,
        "lamination_type": "Lam",
        "duplications": 4,
        "parent": "Rotor",
    },
    "StatorCore": {
        "material": "50C250",
        "mesh_length": 2.0,
        "lamination_type": "Lam",
        "duplications": 1,
        "parent": "Stator",
    },
    "Airgap": {
        "material": "Air",
        "mesh_length": 0.5,
        "lamination_type": "None",
        "duplications": 4,
        "parent": None,
    },
}

# Apply properties to each region
for region_name, props in region_properties.items():
    try:
        region = mc.geometry.get_region(region_name)
        for key, value in props.items():
            setattr(region, key, value)
        mc.geometry.set_region(region, region_name)
        print(f"  Properties set for {region_name}")
    except Exception as e:
        print(f"  Failed to set properties for {region_name}: {e}")

print("All region properties assigned")
```

---

## Design Considerations

### Material Selection
- Use verified material names that exist in Motor-CAD's material database
- Custom materials must be added to the database before assignment
- Material properties (BH curve, conductivity, density) affect all subsequent calculations

### Mesh Quality
- Overly coarse mesh in critical regions (airgap, teeth) produces inaccurate results
- Overly fine mesh everywhere wastes computation time
- Adaptive mesh refinement can be used for initial studies

### Lamination Type Impact
- Incorrect lamination type can produce significantly wrong loss predictions
- Solid steel in the core → overestimates eddy current losses by 10–100×
- Laminated treatment on a solid band → underestimates eddy current losses

---

## Cross-References

- [[pymotorcad-adaptive-geometry]] — region management and adaptive geometry pipeline
- [[pymotorcad-fea-geometry]] — FEA geometry setup and mesh configuration
- [[pymotorcad-geometry-objects]] — Region object and property definitions
- [[pymotorcad-geometry-shapes]] — pre-built shape constructors

---

## Tags

#pymotorcad #adaptive-geometry #material #mesh #FEA #region-properties #lamination #solid #mesh-length #rotor-band
