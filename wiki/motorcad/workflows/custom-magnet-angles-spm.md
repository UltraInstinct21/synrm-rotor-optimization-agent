---
type: motorcad_workflow
name: "Custom Magnet Angles for SPM"
purpose: "Modify magnet angles in Halbach array SPM rotors"
prerequisites: ["Motor-CAD", "a1 SPM template or similar"]
source_files: ["Custom Magnet Angles for SPM — pymotorcad-core.md"]
confidence: Verified
---

# Custom Magnet Angles for SPM

## Purpose

Set custom magnet angles for Halbach array SPM rotors using adaptive parameters for symmetric angle offsets.

## Step-by-Step Procedure

### 1. Configure SPM Template

```python
mc.load_template("a1")
mc.set_variable("BPMRotor", 0)              # Surface Radial
mc.set_variable("Magnet_Arc_[ED]", 180)
mc.set_variable("CircumferentialSegments", 5)
mc.set_variable("Magnetization", 2)          # Halbach
mc.set_variable("HalbachMagnetization", 1)   # Sinusoidal Array
```

### 2. Set Adaptive Parameters

```python
magnet_segments = int(mc.get_variable("CircumferentialSegments"))
half_outer_segments = int((magnet_segments - 1) / 2)

magnet_angle_offset_values = []
for i in range(half_outer_segments):
    mc.set_adaptive_parameter_default(f"Magnet angle offset {i+1}", 10)
    magnet_angle_offset_values.append(
        mc.get_adaptive_parameter_value(f"Magnet angle offset {i+1}")
    )
```

### 3. Apply Angle Offsets

```python
magnets = []
for i in range(magnet_segments):
    magnets.append(mc.get_region(f"{i+1}Magnet1"))

for i in range(half_outer_segments):
    magnets[i].magnet_angle -= magnet_angle_offset_values[i]        # Right side
    magnets[-(i + 1)].magnet_angle += magnet_angle_offset_values[i]  # Left side
    mc.set_region(magnets[i])
    mc.set_region(magnets[-(i + 1)])
```

### 4. Visualize

```python
from ansys.motorcad.core.geometry_drawing import draw_objects

to_draw = [mc.get_region("Rotor"), mc.get_region("Banding"), mc.get_region("Shaft")]
to_draw.extend(magnets)
draw_objects(to_draw, label_regions=True, axes=False)
```

## Key Pattern

For 5 magnet segments (odd number):
- Central magnet (3Magnet1) — unchanged
- Outer pairs (1Magnet1 & 5Magnet1) — symmetric offset 1
- Inner pairs (2Magnet1 & 4Magnet1) — symmetric offset 2

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region, magnet_angle property
- [[motorcad/api/geometry-drawing-methods]] — draw_objects
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
