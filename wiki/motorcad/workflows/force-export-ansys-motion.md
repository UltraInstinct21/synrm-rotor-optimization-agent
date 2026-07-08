---
type: motorcad_workflow
name: "Force Export for Ansys Motion"
purpose: "Export electromagnetic forces for Ansys Motion multibody analysis"
prerequisites: ["Motor-CAD", "Force calculation completed"]
source_files: ["Force export for Ansys Motion — pymotorcad-core.md"]
confidence: Verified
---

# Force Export for Ansys Motion

## Purpose

Export electromagnetic forces from Motor-CAD in UNV/ANF format for use in Ansys Motion multibody structural analysis.

## Prerequisites

- Force calculation must be completed in Motor-CAD before running this script
- Script runs from the Scripting tab

## Output Files

| File | Format | Content |
|------|--------|---------|
| `Output.unv` | UNV metadata | Load point definitions, speed, symmetry |
| `Output.amesh` | UNV 2411/2412 | Nodal positions and element connectivity |
| `Output.anf` | UNV 2414 | Transient nodal forces per timestep |

## Step-by-Step Procedure

### 1. Set Export Parameters

```python
unv_filename = "Output.unv"
amesh_filename = "Output.amesh"
anf_filename = "Output.anf"

offset_angle_degrees = 0    # Position of stator tooth centre relative to X axis
slice_centre_x = 0
slice_centre_y = 0
slice_centre_z = 0
```

### 2. Run Export Function

```python
export_to_motion_unv(
    mc, unv_filename, amesh_filename, anf_filename,
    offset_angle_degrees, slice_centre_x, slice_centre_y, slice_centre_z
)
```

### 3. Key Internal Logic

The export handles:

- **Force duplication** — duplicates electrical cycles to fill a full mechanical cycle
- **Node positioning** — calculates 3D positions from 2D polar coordinates
- **Force transformation** — converts radial/tangential forces to X/Y components
- **Time stepping** — generates transient force data with correct delta times

## Force Data Retrieved

```python
forces_stator_tangential = mc.get_magnetic_3d_graph("Ft_Stator_OL_Lumped_Th1", 1)
forces_stator_radial = mc.get_magnetic_3d_graph("Fr_Stator_OL_Lumped_Th1", 1)
forces_rotor_tangential = mc.get_magnetic_3d_graph("Ft_Rotor_OL_Lumped_Th1", 1)
forces_rotor_radial = mc.get_magnetic_3d_graph("Fr_Rotor_OL_Lumped_Th1", 1)
```

## Key Functions

| Function | Purpose |
|----------|---------|
| `get_electrical_periods_per_revolution()` | Poles/2 for BPM, poles for SRM |
| `get_num_duplications()` | Calculate mechanical cycle duplication factor |
| `duplicate_magnetic_3d_data()` | Tile force data for full mechanical cycle |
| `mechanical_node_positions()` | Convert 2D bore positions to 3D coordinates |

## Related Pages

- [[motorcad/workflows/force-extraction-example]] — Force/NVH calculation
- [[motorcad/api/graphs-methods]] — get_magnetic_3d_graph
- [[motorcad/api/calculations-methods]] — do_force_calculation
