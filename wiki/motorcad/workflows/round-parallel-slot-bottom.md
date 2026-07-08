---
type: motorcad_workflow
name: "Round Parallel Slot Bottom"
purpose: "Add round corners to parallel slot bottoms in stator geometry"
prerequisites: ["Motor-CAD", "e3 WFSM template with Parallel Slot type"]
source_files: ["Round Parallel Slot Bottom — pymotorcad-core.md"]
confidence: Verified
---

# Round Parallel Slot Bottom

## Purpose

Modify stator parallel slot bottoms from square corners to round corners using Adaptive Templates.

## Step-by-Step Procedure

### 1. Setup Template

```python
mc.load_template("e3")
mc.set_variable("SlotType", 2)  # Parallel Slot
```

### 2. Set Adaptive Parameter

```python
mc.set_adaptive_parameter_default("Slot Bttm Corner Radius", 0.5)
radius = mc.get_adaptive_parameter_value("Slot Bttm Corner Radius")
```

### 3. Get Regions and Identify Corners

```python
stator = mc.get_region("Stator")
winding_1 = mc.get_region("ArmatureSlotL1")
winding_2 = mc.get_region("ArmatureSlotR1")
stator_slot = mc.get_region("StatorSlot")
liner = mc.get_region("Liner")
impreg = mc.get_region("Impreg")

# Slot bottom corners
corners = [stator.entities[5].end, stator.entities[7].end]

# Impregnation corners
impreg_corners = [impreg.entities[1].end, impreg.entities[3].end]
```

### 4. Round Corners

```python
# Round slot bottom corners (both corners)
stator.round_corners(corners, radius)
stator_slot.round_corners(corners, radius)
liner.round_corners(corners, radius)

# Windings only have one corner each
winding_1.round_corner(corners[1], radius)
winding_2.round_corner(corners[0], radius)

# Round impregnation corners
liner.round_corners(impreg_corners, radius)
impreg.round_corners(impreg_corners, radius)

# Set all modified regions
mc.set_region(stator)
mc.set_region(stator_slot)
mc.set_region(winding_1)
mc.set_region(winding_2)
mc.set_region(liner)
mc.set_region(impreg)
```

## Key Methods

| Method | Description |
|--------|-------------|
| `region.round_corners(corners, radius)` | Round multiple corners at once |
| `region.round_corner(corner, radius)` | Round a single corner |
| `draw_objects_debug()` | Visualize geometry for debugging |

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region.round_corners, Region.round_corner
- [[motorcad/api/geometry-drawing-methods]] — draw_objects_debug
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
