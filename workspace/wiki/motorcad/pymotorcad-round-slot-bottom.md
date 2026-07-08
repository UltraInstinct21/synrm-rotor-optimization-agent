---
type: pymotorcad_example
title: Round Slot Bottom Corners for Parallel Stator Slots
source: PyMotorCAD Official Documentation — Adaptive Geometry Example e3
tags:
  - pymotorcad
  - adaptive-geometry
  - stator
  - slots
  - round-corners
  - slot-bottom
  - geometry
---

# Round Slot Bottom Corners for Parallel Stator Slots

Adaptive geometry example demonstrating how to round the square corners at the bottom of parallel stator slots using Motor-CAD's corner-rounding API methods.

---

## Template Reference

- **Motor-CAD Template:** `e3`
- **Example Type:** Adaptive geometry modification — slot corner rounding
- **Use Case:** Slot bottom corner radius for manufacturing, insulation, and thermal performance

---

## Overview

Parallel stator slots (parallel tooth or parallel slot type) have square corners at the slot bottom by default. These sharp corners create:

- **Manufacturing issues** — stress concentration in lamination punching
- **Insulation problems** — winding insulation damage at sharp corners
- **Thermal hot spots** — poor copper packing and air pockets at corners

Rounding these corners with a defined radius improves all three concerns.

---

## Adaptive Parameter

| Parameter | Motor-CAD Name | Description |
|---|---|---|
| Slot Bttm Corner Radius | `Slot_Corner_Radius` | Radius of the rounded corner at the slot bottom (mm) |

This parameter is exposed as an **adaptive parameter**, meaning it can be swept or optimised within Motor-CAD's adaptive geometry framework.

```python
mc.set_variable("Slot_Corner_Radius", 4.7)  # 4.7 mm corner radius
```

---

## Affected Regions

Rounding the slot bottom corner affects multiple nested regions in Motor-CAD's geometry hierarchy. All of the following regions must be updated when the corner radius changes:

| Region | Description |
|---|---|
| **Stator** | Outer stator lamination boundary |
| **StatorSlot** | Slot opening and body geometry |
| **ArmatureSlotL1** | Left side of the slot (tooth flank) |
| **ArmatureSlotR1** | Right side of the slot (tooth flank) |
| **Liner** | Slot liner (insulation) geometry |
| **Impreg** | Impregnation region within the slot |

Each of these regions contains corner vertices that must be repositioned according to the new radius.

---

## API Methods

### `region.round_corners()`

Rounds all applicable corners in a region by the specified radius. This is the batch method for applying a uniform corner radius.

```python
from ansys.motorcad.core.geometry import Region

region = mc.geometry.get_region("ArmatureSlotL1")
region.round_corners(radius=4.7)
mc.geometry.set_region(region, "ArmatureSlotL1")
```

### `region.round_corner()`

Rounds a specific corner identified by index or position. Use this when only certain corners need rounding.

```python
region = mc.geometry.get_region("ArmatureSlotR1")
region.round_corner(corner_index=2, radius=4.7)
mc.geometry.set_region(region, "ArmatureSlotR1")
```

---

## Code Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Set the slot bottom corner radius
corner_radius = 4.7  # mm
mc.set_variable("Slot_Corner_Radius", corner_radius)

# Regions affected by corner rounding
affected_regions = [
    "Stator",
    "StatorSlot",
    "ArmatureSlotL1",
    "ArmatureSlotR1",
    "Liner",
    "Impreg",
]

# Apply corner rounding to each affected region
for region_name in affected_regions:
    try:
        region = mc.geometry.get_region(region_name)
        region.round_corners(radius=corner_radius)
        mc.geometry.set_region(region, region_name)
        print(f"  Rounded corners in {region_name}")
    except Exception as e:
        print(f"  Failed to round {region_name}: {e}")

# Verify geometry
print("Corner rounding complete. Running geometry check...")
mc.do_magnetic_calculation()
```

---

## Workflow Steps

1. **Set corner radius** — define `Slot_Corner_Radius` value
2. **Identify affected regions** — Stator, StatorSlot, ArmatureSlotL1, ArmatureSlotR1, Liner, Impreg
3. **Read each region** — `get_region()` to retrieve current geometry
4. **Apply rounding** — `round_corners()` or `round_corner()` on each region
5. **Write regions back** — `set_region()` for each modified region
6. **Validate** — run `do_magnetic_calculation()` to ensure geometry is accepted

---

## Design Considerations

### Manufacturing
- Typical corner radii: 2–6 mm for medium-sized motors
- Radii < 1 mm provide minimal benefit; radii > 8 mm may reduce slot area significantly
- Must match punching tool radius in production

### Insulation
- Minimum radius should accommodate slot liner thickness (typically 0.2–0.5 mm)
- Sharp corners (< 1 mm) risk liner tearing during winding insertion

### Electromagnetic
- Larger corner radii slightly reduce effective slot area → lower copper cross-section
- May marginally increase slot leakage inductance
- Impact on torque is typically < 1% for radii < 6 mm

### Thermal
- Rounded corners improve copper packing factor at slot bottom
- Reduces air pockets that act as thermal insulators
- Can reduce winding hot-spot temperature by 2–5°C

---

## Cross-References

- [[pymotorcad-adaptive-geometry]] — region management and adaptive geometry pipeline
- [[pymotorcad-geometry-objects]] — Region, round_corners(), round_corner() definitions
- [[pymotorcad-geometry-shapes]] — pre-built shape constructors
- [[pymotorcad-adaptive-templates-guide]] — template reference for adaptive geometry examples

---

## Tags

#pymotorcad #adaptive-geometry #stator #slots #round-corners #slot-bottom #geometry #insulation #manufacturing
