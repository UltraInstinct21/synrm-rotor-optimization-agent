---
type: motorcad_workflow
name: "Stress Sampling for Rotor Bridges"
purpose: "Sample stresses at specific points in rotor bridges for fatigue analysis"
prerequisites: ["Motor-CAD", "V-web or U-shape rotor", "Stress calculation completed"]
source_files: ["Stress sampling example — pymotorcad-core.md"]
confidence: Verified
---

# Stress Sampling for Rotor Bridges

## Purpose

Sample stresses at specific radial locations within rotor bridges to calculate average bridge stress and apply non-linear plastic corrections.

## Supported Rotor Types

- **V-Web** (rotor type 11): Uses `VMagnet_Layers`
- **U-Shape** (rotor type 13): Uses `Magnet_Layers`

## Step-by-Step Procedure

### 1. Find Bridge Stress Sample Points

```python
def find_bridge_stress_sample_points(mc):
    sample_points = 15  # Hardcoded in Motor-CAD
    rotor_type = mc.get_variable("BPMRotor")

    if rotor_type == 11:  # V-Web
        layers = mc.get_variable("VMagnet_Layers")
    elif rotor_type == 13:  # U-Shape
        layers = mc.get_variable("Magnet_Layers")

    for layer in range(layers):
        # Calculate angular span of bridge
        # Sample 15 points along the bridge arc
        # Return x,y coordinates for each layer
```

### 2. Key Variables

| Variable | Purpose |
|----------|---------|
| `AvStressRadialLocation_Bridge` | Radial fraction for sampling |
| `BridgeThickness_Array` | Bridge thickness per layer |
| `WebThickness_Array` | Web thickness per layer |
| `PoleArc_Array` | Pole arc per layer |

### 3. Apply Corrections

Uses the same Neuber/Glinka corrections as [[motorcad/workflows/stress-post-processing]].

## Related Pages

- [[motorcad/workflows/stress-post-processing]] — Full stress post-processing
- [[motorcad/api/calculations-methods]] — do_mechanical_calculation
- [[motorcad/workflows/mechanical-stress-example]] — Internal scripting stress
