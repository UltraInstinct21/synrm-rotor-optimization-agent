---
type: motorcad_api
title: "Close Slot — Air-to-Steel Region Conversion"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - material
  - close-slot
  - stator
  - lamination
  - adaptive-geometry
aliases:
  - close_slot
  - StatorAir
  - closed-slot
motor_types:
  - IPMSM
  - SPM
  - SynRM
  - BPM
  - BLDC
topics:
  - material-assignment
  - slot-geometry
  - lamination-type
related_pages:
  - "[[pymotorcad-material-mesh]]"
  - "[[pymotorcad-adaptive-geometry]]"
confidence: high
verification_status: verified
---

# Close Slot — Air-to-Steel Region Conversion

## Purpose

Convert the air region in the slot opening to a solid or laminated steel region, enabling closed-slot (semi-closed or closed) slot geometry modeling in Motor-CAD.

Closed slots are commonly used in:

- **IPMSM** and **SPM** designs to reduce cogging torque
- **BLDC** designs where magnets sit in slots
- High-inductance applications where slot leakage flux is beneficial

## Concept

In Motor-CAD's slot geometry model, the **slot opening** is represented as a separate region (StatorAir) that defaults to air. To model a closed or semi-closed slot:

1. Identify the air region in the slot opening (`StatorAir`)
2. Copy the **stator lamination material** into that region
3. Set the **lamination type** appropriately (laminated or solid)

The `Adaptive Templates` feature in Motor-CAD can convert an air region to solid or laminated material directly.

## API Methods

### Close a Slot (Set Material in Slot Opening)

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Switch to electromagnetic context
mc.show_magnetic_context()

# Access the slot opening region
# StatorAir is the default name for the air region in the slot opening
mc.set_component_material("StatorAir", "Steel_50C250")

# Set the lamination type (laminated = 1, solid = 0)
mc.set_variable("StatorAir_Lamination", 1)

# Alternatively, use Adaptive Templates to convert air to solid
# This is the recommended approach for complex geometries
mc.adaptive_template_close_slot()
```

### Using Adaptive Templates

```python
# Adaptive Templates automatically detect and convert air regions
# in slot openings to the correct material type

# Close all open slots
mc.adaptive_template_close_slot()

# Or close slots with specific material override
mc.set_component_material("StatorAir", "M19_29Ga")
mc.set_variable("StatorAir_Lamination", 1)
```

### Verify the Conversion

```python
# Read back the material assignment
material = mc.get_variable("StatorAir_Material")
lamination = mc.get_variable("StatorAir_Lamination")
print(f"Slot opening material: {material}")
print(f"Lamination type: {lamination}")  # 1 = laminated, 0 = solid
```

## Regions Involved

| Region Name | Default Material | After Close Slot |
|---|---|---|
| `StatorAir` | Air | Stator lamination (e.g., 50C250, M19) |
| Lamination type | N/A | 1 (laminated) or 0 (solid) |

## Lamination Type Settings

| Value | Meaning | Use Case |
|---|---|---|
| `0` | Solid steel | Non-laminated structures, bridges |
| `1` | Laminated steel | Standard stator/rotor laminations |

## Design Implications

### Benefits of Closed Slots

- **Reduced cogging torque**: The closed slot smooths the air-gap permeance variation
- **Lower noise**: Reduced slot harmonics
- **Increased inductance**: Slot leakage flux path is enhanced
- **Higher saliency ratio** (SynRM): More reluctance torque component

### Tradeoffs

- **Increased copper loss**: Slot leakage inductance increases copper loss at rated current
- **Reduced winding area**: The closed slot may require a narrower slot opening
- **Manufacturing complexity**: Closing the slot requires tighter tolerances
- **Reduced thermal conductance**: The closed slot may trap heat near the winding

### Typical Slot Opening Widths

| Motor Type | Typical Slot Opening | Closed Slot? |
|---|---|---|
| IPMSM | 1–4 mm | Often semi-closed |
| SPM | 2–5 mm | Usually open |
| SynRM | 2–5 mm | Depends on application |
| BLDC | 1–3 mm | Often closed |

## Common Pitfalls

1. **Material mismatch**: Ensure the closed slot uses the same lamination as the stator core
2. **Lamination type not set**: Forgetting to set lamination type causes incorrect loss calculations
3. **Airgap effects**: Closing the slot changes the effective airgap; verify [[pymotorcad-material-mesh]] settings
4. **Adaptive template failure**: If the geometry is too complex, Adaptive Templates may fail to close the slot; manual assignment may be needed

## Related Pages

- [[pymotorcad-material-mesh]] — Material mesh settings and verification
- [[pymotorcad-adaptive-geometry]] — Adaptive geometry templates and mesh adaptation
- [[pymotorcad-material-assignment]] — General material assignment workflows
- [[pymotorcad-stator-geometry]] — Stator geometry parameters
