---
type: motorcad_workflow
name: "Oblong Stator Ducts with Thermal Adjustment"
purpose: "Convert rectangular ducts to oblong shape and adjust thermal model"
prerequisites: ["Motor-CAD v2024 R2+", "e9 IPM template or similar"]
source_files: ["Oblong stator ducts with thermal adjustment — pymotorcad-core.md"]
confidence: Verified
---

# Oblong Stator Ducts with Thermal Adjustment

## Purpose

Modify rectangular stator ducts into oblong (rounded) shapes and correct the thermal model for the changed cross-section area.

## Step-by-Step Procedure

### 1. Setup Template

```python
mc.load_template("e9")
mc.set_variable("StatorDuctType", 4)           # Rectangular ducts
mc.set_variable("CircularDuctLayers", 1)
mc.set_variable("CircularDuctL1RadialDiameter", 180)
mc.set_variable("CircularDuctL1ChannelWidth", 2)
mc.set_variable("CircularDuctL1ChannelHeight", 3)
mc.set_variable("CircularDuctL1Channels", 48)
mc.set_variable("HousingType", 0)              # Round housing
```

### 2. Set Adaptive Parameter

```python
mc.set_adaptive_parameter_default("Duct Arc Height", 0.7)
duct_arc_height = mc.get_adaptive_parameter_value("Duct Arc Height")
```

### 3. Replace Lines with Arcs

For each stator duct region, find the top/bottom lines and replace with arcs:

```python
for child_name in st_region.child_names:
    if "StatorDuctFluidRegion" in child_name:
        duct_region = mc.get_region(child_name)
        for i, entity in enumerate(duct_region.entities):
            if round(entity.length / duct_width, 2) == 1:
                radius = get_arc_radius(entity.start, entity.end, duct_arc_height)
                Duct_Arc = Arc(entity.start, entity.end, radius=radius)
                duct_region.entities[i] = Duct_Arc
        mc.set_region(duct_region)
```

### 4. Apply Thermal Area Correction

The oblong duct has larger area than rectangular. Correct the thermal model:

```python
oblong_duct_areas = []
for child_name in st_region.child_names:
    if "StatorDuctFluidRegion" in child_name:
        oblong_duct_areas.append(mc.get_region(child_name).area)

oblong_duct_area = sum(oblong_duct_areas) / ducts_per_slot
area_adjustment = oblong_duct_area - duct_area

mc.set_array_variable("HousingWJ_Channel_CSArea_L1_A_Adjustment", 0, area_adjustment)
```

## Key Functions

| Function | Purpose |
|----------|---------|
| `check_line_origin_distance()` | Determine if line is near/far from origin |
| `get_arc_radius()` | Calculate arc radius for full duct |
| `get_arc_radius_halfduct()` | Calculate arc for half-duct (symmetry boundary) |

## Pitfalls

- Half-ducts at symmetry boundaries need special handling
- Area correction in Thermal module is essential for accurate cooling predictions
- Duct area visible in Geometry → Editor → Geometry tab

## Related Pages

- [[motorcad/api/adaptive-geometry-methods]] — Adaptive geometry methods
- [[motorcad/api/geometry-objects-functions]] — Arc, Line, Coordinate
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates overview
- [[motorcad/workflows/trapezoidal-ducts]] — Another duct modification
