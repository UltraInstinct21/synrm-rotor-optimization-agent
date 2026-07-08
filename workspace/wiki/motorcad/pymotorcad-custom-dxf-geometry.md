---
type: pymotorcad_example
title: "PyMotorCAD Custom DXF Geometry"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - dxf
  - import
  - geometry
  - custom
  - adaptive-geometry
  - rotor
  - region
aliases:
  - custom_dxf_geometry
  - dxf_import
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM", "BLDC", "SRM"]
confidence: verified
---

# PyMotorCAD Custom DXF Geometry

## Overview

This page documents how to **import custom rotor geometry from a DXF file** into MotorCAD using PyMotorCAD. DXF (Drawing Exchange Format) is a universal CAD interchange format, allowing geometry designed in external tools (AutoCAD, SolidWorks, Fusion 360, etc.) to be imported directly into MotorCAD's adaptive geometry system. The `replace()` method swaps existing geometry entities with the imported DXF region while preserving region properties.

**Template:** e8 (custom DXF import template)

**Requirements:** MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+

---

## Core API

### `get_region_dxf(dxf_region_name)`

Retrieves a region from a DXF file that has been loaded into MotorCAD. The DXF file must be imported into the model first (via MotorCAD GUI or file setup).

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `dxf_region_name` | `str` | Name of the region in the DXF file to retrieve |

#### Returns

A `Region` object containing the geometry entities from the DXF file.

#### Example

```python
# Retrieve a DXF region named "DXFRegion_Rotor_14"
dxf_region = mc.get_region_dxf("DXFRegion_Rotor_14")
```

---

### `Region.replace(new_entities)`

Replaces the entity list of a region with new entities while **preserving all region properties** (name, colour, material, duplications, parent).

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `new_entities` | `EntityList` | New geometry entities to replace the existing ones |

#### Returns

Modified `Region` with updated entities.

#### Example

```python
# Get existing region
rotor_region = mc.get_region("Rotor_Lam")

# Get DXF geometry
dxf_region = mc.get_region_dxf("DXFRegion_Rotor_14")

# Replace entities while preserving region properties
rotor_region.replace(dxf_region.entities)

# Set the modified region back
mc.set_region(rotor_region)
```

---

## What `replace()` Preserves

When `replace()` is called, the following region properties are **kept unchanged**:

| Property | Preserved? | Notes |
|---|---|---|
| `name` | Yes | Region name stays the same |
| `colour` | Yes | RGB colour is unchanged |
| `material` | Yes | Material assignment is unchanged |
| `duplications` | Yes | Symmetry duplication count is unchanged |
| `parent` | Yes | Parent region reference is unchanged |
| `entities` | **Replaced** | Old entities removed, new entities inserted |

This is critical — you can swap geometry without re-configuring material, colour, or symmetry settings.

---

## Complete Workflow

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"path\to\model_with_dxf.mot")
mc.show_magnetic_context()

# 1. Reset adaptive geometry
mc.reset_adaptive_geometry()

# 2. Retrieve the DXF region
#    The DXF file must already be imported into the model
dxf_region = mc.get_region_dxf("DXFRegion_Rotor_14")

# 3. Get the target region to replace
target_region = mc.get_region("Rotor_Lam")

# 4. Replace geometry entities
target_region.replace(dxf_region.entities)

# 5. Set the modified region back
mc.set_region(target_region)

# 6. Run EMag calculation
mc.do_magnetic_calculation()

# 7. Read results
torque = mc.get_variable("ShaftTorque")
print(f"Torque with DXF geometry: {torque:.2f} Nm")
```

---

## DXF File Preparation

### Requirements

| Requirement | Details |
|---|---|
| Format | DXF (R12 or R2000 compatible recommended) |
| Geometry type | 2D profile (closed polyline or line/arc entities) |
| Units | Must match MotorCAD model units (typically mm) |
| Coordinate system | Polar or Cartesian — MotorCAD converts as needed |
| Closed boundary | The DXF profile must form a closed loop |

### Recommended DXF Workflow

1. Design rotor profile in CAD tool (AutoCAD, SolidWorks, etc.)
2. Export as DXF (R12 or R2000 format for maximum compatibility)
3. Import DXF into MotorCAD via GUI (File → Import DXF)
4. Verify the imported region name (e.g. `DXFRegion_Rotor_14`)
5. Use PyMotorCAD `get_region_dxf()` to retrieve and `replace()` to apply

---

## Design Considerations

- **Geometry validation** — Always verify the imported DXF geometry visually in MotorCAD before running EMag calculations.
- **Region naming** — DXF region names are assigned by MotorCAD during import. The naming convention is `DXFRegion_<type>_<index>`. Use the MotorCAD GUI to confirm the exact name.
- **Entity types** — DXF files may contain lines, arcs, circles, and polylines. MotorCAD converts these to its internal entity format. Splines and 3D entities may not be supported.
- **Scaling** — Ensure the DXF units match the MotorCAD model. A 100 mm radius in DXF must correspond to 100 mm in MotorCAD.
- **Optimisation** — DXF import is useful for geometry that cannot be parameterised easily with standard adaptive templates (e.g. topology-optimised rotors, organic shapes).

---

## Common Pitfalls

1. **DXF not imported** — `get_region_dxf()` fails if the DXF file has not been imported into the model via the GUI first.
2. **Wrong region name** — The DXF region name is assigned by MotorCAD, not by the DXF file. Check the GUI for the exact name.
3. **Open boundary** — If the DXF profile is not closed, `replace()` may produce invalid geometry. Ensure the profile forms a closed loop.
4. **Unit mismatch** — A DXF designed in inches will be imported at the wrong scale if MotorCAD expects mm.
5. **Entity count mismatch** — The DXF may have significantly more or fewer entities than the original region. This is normal but may affect mesh density.
6. **Missing `reset_adaptive_geometry()`** — Must be called before modifying regions.

---

## Use Cases

| Application | Why DXF Import |
|---|---|
| Topology-optimised rotor | Organic shapes from optimisation algorithms |
| Research paper geometries | Import profiles from published designs |
| Third-party CAD models | Rotor profiles designed in external tools |
| Non-standard barrier shapes | Curves that cannot be parameterised with standard functions |
| Prototyping | Quick iteration on imported geometry |

---

## Related Pages

- [[pymotorcad-adaptive-geometry]] — Full adaptive template API
- [[pymotorcad-geometry-objects]] — Region, EntityList, Coordinate types
- [[pymotorcad-bezier-rotor-pockets]] — Bezier curves (alternative to DXF for curved geometry)
- [[pymotorcad-curved-flux-barriers]] — Circular arc barriers (another curvature method)
- [[pymotorcad-adaptive-templates-guide]] — Adaptive templates user guide
- [[pymotorcad-geometry-shapes]] — Shape primitives

---

## Tags

#pymotorcad #motorcad #dxf #import #geometry #custom #adaptive-geometry #rotor #region #cad
