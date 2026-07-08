---
type: motorcad_workflow
name: "Stress Post-Processing with Neuber and Glinka"
purpose: "Post-process rotor stress results with non-linear plastic corrections"
prerequisites: ["Motor-CAD", "Stress calculation completed", "numpy"]
source_files: ["Motor-CAD Stress post-processing example script — pymotorcad-core.md"]
confidence: Verified
---

# Stress Post-Processing with Neuber and Glinka

## Purpose

Load Motor-CAD linear stress results and apply Neuber and Glinka corrections to estimate non-linear stress/strain including plastic deformation.

## Step-by-Step Procedure

### 1. Run Stress Calculation

```python
mc = pymotorcad.MotorCAD()
mc.load_template("e9")
mc.set_variable("ShaftSpeed", 15000)
mc.do_mechanical_calculation()
```

### 2. Load Stress Data

```python
stress_regions = get_stress_data(mc)
```

Uses `mc.save_fea_data()` to export element/node/region data to a temporary file, then parses it into `StressRegion` objects containing per-element stress components.

### 3. Apply Non-Linear Corrections

```python
non_linear_strain = np.array([0, 0.0002, 0.0004, ...])
non_linear_stress = np.array([0, 37, 74, ...])

for region in stress_regions:
    region.apply_corrections(non_linear_strain, non_linear_stress)
```

### 4. Key Classes

| Class | Purpose |
|-------|---------|
| `Element` | Per-element stress data with Neuber/Glinka corrections |
| `StressRegion` | Collection of elements with material properties |
| `StressRegions` | Multiple regions container |

### 5. Neuber Correction

Matches elastic stress×strain product to non-linear curve:

```python
elastic_stress_strain_product = elastic_stress * elastic_strain
equivalent_strain = np.interp(
    elastic_stress_strain_product, non_linear_stress_strain_product, non_linear_strain
)
```

### 6. Glinka Correction

Matches elastic stress-strain energy integral to non-linear curve using trapezium integration.

## Related Pages

- [[motorcad/workflows/stress-sampling-example]] — Bridge stress sampling
- [[motorcad/api/calculations-methods]] — do_mechanical_calculation
- [[motorcad/workflows/mechanical-stress-example]] — Internal scripting stress
