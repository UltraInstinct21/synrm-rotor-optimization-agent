---
type: motorcad_workflow
name: "Motor-CAD Internal Scripting Tab"
purpose: "Creating, editing, and running Python scripts inside Motor-CAD"
prerequisites: ["Motor-CAD installed"]
source_files: ["Motor-CAD internal Scripting tab — pymotorcad-core.md"]
confidence: Verified
---

# Motor-CAD Internal Scripting Tab

## Purpose

The Scripting tab in Motor-CAD provides an embedded Python environment for automation scripts.

## Connecting from Internal Script

```python
import ansys.motorcad.core as pymotorcad
mcApp = pymotorcad.MotorCAD()
```

## Script Structure

### Main Function

Called when **Run** is pressed:

```python
def main():
    user_func = thermal_steady()
    user_func.initial()
```

### Calculation Classes

Five classes with `initial`, `final`, and optionally `main` hooks:

| Class | Purpose |
|-------|---------|
| `thermal_steady` | Steady-state thermal calculations |
| `thermal_transient` | Transient thermal calculations |
| `emagnetic` | E-magnetic calculations |
| `mechanical_stress` | Mechanical stress calculations |
| `mechanical_forces` | Mechanical force calculations |

- `initial()` — called before calculation
- `main()` — called before each time step (thermal only)
- `final()` — called after calculation

### Run During Analysis

Enable **Scripting → Settings → Script Control → Run During Analysis** to auto-run scripts during calculations.

## Example: Tooth Width Sweep

```python
def demo_func():
    array_tooth_widths = [1, 1.5, 2.0]
    mcApp.set_variable("MessageDisplayState", 2)
    for toothWidth in array_tooth_widths:
        mcApp.set_variable("Tooth_Width", toothWidth)
        mcApp.do_steady_state_analysis()
        temp = mcApp.get_variable("T_[WINDING_AVERAGE]")
    mcApp.set_variable("MessageDisplayState", 0)
```

## Related Pages

- [[motorcad/api/internal-scripting-methods]] — load_script, run_script, save_script
- [[motorcad/api/motorcad-api]] — MotorCAD constructor
- [[motorcad/troubleshooting/troubleshooting]] — Common issues
