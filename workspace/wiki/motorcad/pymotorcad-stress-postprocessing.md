---
type: motorcad_api
title: "Stress Post-Processing — FEA Data Export & Plastic Corrections"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - stress
  - postprocessing
  - fea
  - plastic-correction
  - neuber
  - glinka
  - element
  - stress-region
aliases:
  - stress_postprocessing
  - fea_data_export
  - stress_element
motor_types:
  - IPMSM
  - SynRM
  - PMaSynRM
  - SPM
topics:
  - stress-postprocessing
  - fea-data
  - plastic-correction
  - element-stress
related_pages:
  - "[[pymotorcad-stress-sampling]]"
  - "[[pymotorcad-mechanical-stress]]"
confidence: high
verification_status: verified
---

# Stress Post-Processing — FEA Data Export & Plastic Corrections

## Purpose

Post-process rotor stress results from Motor-CAD's FEA solver. Export raw FEA stress data, organize it into structured objects (Element, StressRegion), and apply plastic corrections (Neuber, Glinka) to account for local material yielding at stress concentrations.

## Concept

Motor-CAD's stress post-processing workflow:

1. **Export FEA data** — extract raw stress results from the electromagnetic FEA mesh
2. **Organize into elements** — each FEA element has position (X, Y) and stress components
3. **Group into regions** — elements are grouped by structural region (bridge, web, rib)
4. **Apply corrections** — plastic corrections modify raw stress to account for local yielding

### FEA Data Fields

The exported FEA data includes the following fields per element:

| Field | Description | Units |
|---|---|---|
| `RegCode` | Region code identifying the structural region | — |
| `X` | X-coordinate of element centroid | mm |
| `Y` | Y-coordinate of element centroid | mm |
| `Sx` | Normal stress in X-direction | MPa |
| `Sy` | Normal stress in Y-direction | MPa |
| `Txy` | Shear stress in XY-plane | MPa |
| `Sp1` | Principal stress 1 (maximum) | MPa |
| `Sp2` | Principal stress 2 (minimum) | MPa |
| `SVM` | Von Mises stress | MPa |
| `Ux` | Displacement in X-direction | mm |
| `Uy` | Displacement in Y-direction | mm |

## API Methods

### Save FEA Data

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Run stress calculation first
mc.set_variable("Shaft_Speed_[RPM]", 6000)
mc.do_mechanical_calculation()

# Export FEA data to file
mc.save_fea_data(r"D:\SRM\Motor_CAD\ScriptFiles\fea_stress_data.csv")

# The exported CSV contains columns:
# RegCode, X, Y, Sx, Sy, Txy, Sp1, Sp2, SVM, Ux, Uy
```

### Read FEA Data Programmatically

```python
import csv

def read_fea_data(filepath):
    """Read exported FEA stress data."""
    elements = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            element = Element(
                reg_code=int(row["RegCode"]),
                x=float(row["X"]),
                y=float(row["Y"]),
                sx=float(row["Sx"]),
                sy=float(row["Sy"]),
                txy=float(row["Txy"]),
                sp1=float(row["Sp1"]),
                sp2=float(row["Sp2"]),
                svm=float(row["SVM"]),
                ux=float(row["Ux"]),
                uy=float(row["Uy"])
            )
            elements.append(element)
    return elements

elements = read_fea_data(r"D:\SRM\Motor_CAD\ScriptFiles\fea_stress_data.csv")
```

### Element Class

```python
class Element:
    """Represents a single FEA element with stress data and corrections."""

    def __init__(self, reg_code, x, y, sx, sy, txy, sp1, sp2, svm, ux, uy):
        self.reg_code = reg_code
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.txy = txy
        self.sp1 = sp1
        self.sp2 = sp2
        self.svm = svm
        self.ux = ux
        self.uy = uy

        # Corrected stress values (populated after correction)
        self.svm_corrected = None
        self.sp1_corrected = None
        self.sp2_corrected = None

    def apply_neuber_correction(self, yield_stress, kt=1.0):
        """Apply Neuber plastic correction to this element."""
        if self.svm < yield_stress:
            self.svm_corrected = self.svm
            return

        # Neuber hyperbola: σ_actual × ε_actual = σ_nom × ε_nom
        sigma_nom = self.svm
        sigma_yield = yield_stress
        self.svm_corrected = sigma_yield * (
            (sigma_nom / sigma_yield) ** 0.5
        ) * kt

    def apply_glinka_correction(self, yield_stress, kt=1.0):
        """Apply Glinka energy-based plastic correction."""
        sigma_nom = self.svm
        sigma_yield = yield_stress

        if sigma_nom <= sigma_yield:
            self.svm_corrected = sigma_nom
            return

        # Glinka correction factor
        ratio = sigma_nom / sigma_yield
        self.svm_corrected = sigma_nom * (1 + ratio**2 * kt**2)**0.5
```

### StressRegion Class

```python
class StressRegion:
    """Collection of elements belonging to a structural region."""

    def __init__(self, reg_code, name=""):
        self.reg_code = reg_code
        self.name = name
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    @property
    def max_svm(self):
        return max(e.svm for e in self.elements) if self.elements else 0

    @property
    def max_svm_corrected(self):
        corrected = [e.svm_corrected for e in self.elements if e.svm_corrected is not None]
        return max(corrected) if corrected else self.max_svm

    @property
    def average_svm(self):
        return sum(e.svm for e in self.elements) / len(self.elements) if self.elements else 0

    @property
    def max_displacement(self):
        import math
        return max(math.sqrt(e.ux**2 + e.uy**2) for e in self.elements) if self.elements else 0

    def apply_neuber_all(self, yield_stress, kt=1.0):
        for element in self.elements:
            element.apply_neuber_correction(yield_stress, kt)

    def apply_glinka_all(self, yield_stress, kt=1.0):
        for element in self.elements:
            element.apply_glinka_correction(yield_stress, kt)
```

### StressRegions Class

```python
class StressRegions:
    """Container for all stress regions in the model."""

    def __init__(self):
        self.regions = {}

    def add_element(self, element):
        code = element.reg_code
        if code not in self.regions:
            self.regions[code] = StressRegion(reg_code=code, name=f"Region_{code}")
        self.regions[code].add_element(element)

    def get_region(self, reg_code):
        return self.regions.get(reg_code)

    @property
    def global_max_svm(self):
        return max(r.max_svm for r in self.regions.values()) if self.regions else 0

    @property
    def global_max_svm_corrected(self):
        return max(r.max_svm_corrected for r in self.regions.values()) if self.regions else 0

    def apply_neuber_all(self, yield_stress, kt=1.0):
        for region in self.regions.values():
            region.apply_neuber_all(yield_stress, kt)

    def apply_glinka_all(self, yield_stress, kt=1.0):
        for region in self.regions.values():
            region.apply_glinka_all(yield_stress, kt)
```

## Complete Post-Processing Workflow

```python
import csv
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# 1. Run mechanical calculation
mc.set_variable("Shaft_Speed_[RPM]", 6000)
mc.do_mechanical_calculation()

# 2. Export FEA data
fea_path = r"D:\SRM\Motor_CAD\ScriptFiles\fea_stress.csv"
mc.save_fea_data(fea_path)

# 3. Load into StressRegions
regions = StressRegions()
with open(fea_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        element = Element(
            reg_code=int(row["RegCode"]),
            x=float(row["X"]), y=float(row["Y"]),
            sx=float(row["Sx"]), sy=float(row["Sy"]),
            txy=float(row["Txy"]),
            sp1=float(row["Sp1"]), sp2=float(row["Sp2"]),
            svm=float(row["SVM"]),
            ux=float(row["Ux"]), uy=float(row["Uy"])
        )
        regions.add_element(element)

# 4. Apply plastic corrections
yield_stress = mc.get_variable("YieldStress_RotorLam")
regions.apply_neuber_all(yield_stress)

# 5. Report results
print(f"Global max SVM (uncorrected): {regions.global_max_svm:.1f} MPa")
print(f"Global max SVM (Neuber corrected): {regions.global_max_svm_corrected:.1f} MPa")

for code, region in regions.regions.items():
    print(f"Region {code}: max={region.max_svm:.1f}, corrected={region.max_svm_corrected:.1f}")
```

## Common Pitfalls

1. **Forgetting yield stress**: Corrections require `YieldStress_RotorLam`; without it, corrections are meaningless
2. **Wrong Kt value**: The stress concentration factor `kt` should match the actual notch geometry
3. **Large deformations**: Plastic corrections assume small-scale yielding; large deformations require nonlinear FEA
4. **Cyclic loading**: Neuber/Glinka are for monotonic loading; fatigue requires additional corrections

## Related Pages

- [[pymotorcad-stress-sampling]] — Stress sampling at specific bridge locations
- [[pymotorcad-mechanical-stress]] — General mechanical stress analysis
- [[pymotorcad-material-mesh]] — Material mesh and lamination settings
- [[pymotorcad-calculations-api]] — All Motor-CAD calculation methods
