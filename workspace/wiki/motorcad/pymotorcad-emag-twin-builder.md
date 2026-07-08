---
type: pymotorcad_guide
title: "EMag Twin Builder Export"
source: "PyMotorCAD Documentation"
tags:
  - pymotorcad
  - emag
  - twin-builder
  - export
  - ECE
  - workflow
aliases: ["Twin Builder Export", "ECE Model Export"]
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM"]
---

# EMag Twin Builder Export

## Overview

Export electromagnetic equivalent circuit (ECE) models from MotorCAD for use in Ansys Twin Builder. The exported model includes saturation maps, inductance characteristics, and operating point data for system-level simulation.

---

## Full Script

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD(open_new_instance=True)
mc.set_variable("MessageDisplayState", 2)

# --- Load Solved EMag Model ---
mc.load_from_file(r"D:\SRM\Motor_CAD\SRM_1_solved.mot")
mc.show_magnetic_context()

# --- Set Operating Point for Saturation Map ---
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PeakCurrent", 100)
mc.set_variable("DCBusVoltage", 540)
mc.set_variable("PhaseAdvance", 45)

# --- Run Back EMF Calculation ---
mc.set_variable("BackEMFCalculation", True)
mc.do_magnetic_calculation()

# --- Configure Saturation Map ---
mc.set_variable("SaturationMap_InputDefinition", 1)  # 1 = Current + Angle
mc.set_variable("SaturationMap_CalculationMethod", 1)  # 1 = MotorCAD method
mc.set_variable("SaturationMap_Current_D_Max", 150)  # Max d-axis current (A)
mc.set_variable("SaturationMap_Current_Q_Max", 150)  # Max q-axis current (A)
mc.set_variable("SaturationMap_Current_Points", 10)  # Grid points per axis
mc.set_variable("SaturationMap_Angle_Points", 12)  # Angle resolution

# --- Calculate Saturation Map ---
mc.do_magnetic_calculation()

# --- Export for Twin Builder ---
output_dir = r"D:\SRM\TwinBuilder"

# Generate ECE model files
mc.twin_builder_export(output_dir)

print(f"Exported ECE model to: {output_dir}")
print("Files generated:")
print("  - *.txt  (model parameters)")
print("  - *.sml  (schematic model)")
```

---

## Saturation Map Variables

### Input Configuration
| Variable | Type | Description |
|---|---|---|
| `SaturationMap_InputDefinition` | int | Input type: 0=Id,Iq, 1=Current+Angle |
| `SaturationMap_CalculationMethod` | int | 0=Manual, 1=MotorCAD auto |
| `SaturationMap_Current_D_Max` | A | Maximum d-axis current |
| `SaturationMap_Current_Q_Max` | A | Maximum q-axis current |
| `SaturationMap_Current_Points` | — | Number of current grid points |
| `SaturationMap_Angle_Points` | — | Number of angle steps |

### Calculation Settings
| Variable | Type | Description |
|---|---|---|
| `BackEMFCalculation` | bool | Enable back-EMF calculation |
| `SaturationMap_Calculation` | bool | Enable saturation map generation |

---

## Output Files

### TXT Files
Contain numerical data for saturation characteristics:
- Inductance maps (Ld, Lq) vs current
- Flux linkage maps vs current
- Torque maps vs current and angle
- Back-EMF waveforms

### SML Files
MotorCAD schematic model file for Twin Builder import:
- Equivalent circuit topology
- Parameterized component values
- Look-up tables from saturation maps
- Operating point definitions

---

## Twin Builder Import Workflow

1. Open Twin Builder in Ansys Electronics Desktop
2. Create new schematic
3. Use **File → Import → MotorCAD ECE Model**
4. Select the `.sml` file from export directory
5. Connect to drive inverter and mechanical load models
6. Run transient simulation

---

## Complete Workflow: EMag → Twin Builder

```
1. Load solved MotorCAD model
2. Set operating point (speed, current, voltage)
3. Run back EMF calculation
4. Configure saturation map parameters
5. Calculate saturation map
6. Export ECE model (TXT + SML)
7. Import SML into Twin Builder
8. Connect to system simulation
```

---

## Tips and Best Practices

- **Grid resolution:** Higher `Current_Points` and `Angle_Points` improve accuracy but increase calculation time
- **Operating range:** Ensure `Current_D_Max` and `Current_Q_Max` cover the full operating envelope
- **Speed dependency:** Export multiple speed points if the drive operates across a wide speed range
- **Validation:** Compare MotorCAD results with Twin Builder simulation to verify export accuracy

---

## Related Pages

- [[pymotorcad-emag-example]] — Complete EMag analysis workflow
- [[pymotorcad-calculations-api]] — EMag calculation methods
- [[pymotorcad-set-variable]] — Variable setting API
- [[pymotorcad-get-variable]] — Variable reading API
- [[pymotorcad-thermal-twin-builder]] — Thermal model Twin Builder export
