---
type: motorcad_workflow
name: "Material and Mesh Properties via Adaptive Templates"
purpose: "Set custom material types and mesh densities for adaptive geometry regions"
prerequisites: ["Motor-CAD v2025.1.1+", "Adaptive Templates enabled"]
source_files: ["Material and Mesh Properties — pymotorcad-core.md"]
confidence: Verified
---

# Material and Mesh Properties via Adaptive Templates

## Purpose

Modify material properties (including lamination type) and mesh density for custom regions created with Adaptive Templates.

## Prerequisites

Motor-CAD v2025.1.1 (2025 R1 Update) or later.

## Step-by-Step Procedure

### 1. Create Region with Custom Material

```python
rt_band = Region(region_type=RegionType.rotor)
rt_band.name = "rotor band"
rt_band.entities = EntityList([line_1, arc_mag, line_2, arc_rt])
rt_band.duplications = rt_region.duplications
rt_band.parent = rt_region

# Set material
rt_band.material = "4340 Steel"

# Set mesh density
rt_band.mesh_length = mc.get_adaptive_parameter_value("Rotor_band_mesh_length")

# Set lamination type (Solid vs Laminated)
rt_band.lamination_type = "Solid"

mc.set_region(rt_band)
```

### 2. Set Adaptive Parameters for Mesh Control

```python
mc.set_adaptive_parameter_default("Rotor_band_thickness", 0.225)
mc.set_adaptive_parameter_default("Rotor_band_mesh_length", 0.05)
```

### 3. Run EMag Calculation

After setting the region, run electromagnetic analysis to see flux density and eddy current losses in the custom region.

## Region Properties

| Property | Method | Description |
|----------|--------|-------------|
| Material | `region.material = "name"` | Set material from Motor-CAD library |
| Mesh length | `region.mesh_length = value` | Control mesh density |
| Lamination type | `region.lamination_type = "Solid"` or `"Laminated"` | Solid allows eddy currents |

## Outputs

- Eddy current losses in custom regions appear under **Output Data → Losses → Additional Custom Materials Loss**
- Flux density visible in EMag plots

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region properties
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
- [[motorcad/api/fea-geometry-methods]] — FEA geometry methods
