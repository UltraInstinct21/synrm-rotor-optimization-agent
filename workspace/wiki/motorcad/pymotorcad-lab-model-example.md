---
type: pymotorcad_example
title: "Lab Model Example Script"
source: "PyMotorCAD Documentation"
tags:
  - pymotorcad
  - lab
  - example
  - workflow
  - motor-lab
  - calculations
aliases: ["Lab Model Example", "Motor-CAD Lab Example"]
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM", "BLDC", "SRM"]
---

# Lab Model Example Script

## Overview

Complete Motor-CAD Lab model workflow using PyMotorCAD. The Lab module provides fast analytical motor calculations using pre-computed saturation models. This example demonstrates setting parameters, building the saturation model, running calculations, and reading results.

---

## Full Script

```python
import ansys.motorcad.core as pymotorcad
import numpy as np

# --- Connection ---
mc = pymotorcad.MotorCAD(open_new_instance=True)
mc.set_variable("MessageDisplayState", 2)

# --- Load Template ---
mc.load_from_file(r"D:\SRM\Motor_CAD\SRM_1.mot")

# --- Switch to Lab Context ---
mc.show_lab_context()

# --- Configure Lab Model ---
mc.set_variable("ModelType_MotorLAB", 1)  # 1 = Standard model
mc.set_variable("SatModelPoints_MotorLAB", 50)  # Saturation model resolution
mc.set_variable("BuildSatModel_MotorLAB", True)  # Build on calculation

# --- Set Operating Conditions ---
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PeakCurrent", 100)
mc.set_variable("DCBusVoltage", 540)
mc.set_variable("PhaseAdvance", 45)

# --- Run Lab Calculation ---
mc.do_lab_calculation()

# --- Read Lab Results ---
shaft_torque = mc.get_variable("LabOpPoint_ShaftTorque")
efficiency = mc.get_variable("LabOpPoint_Efficiency")
input_power = mc.get_variable("LabOpPoint_InputPower")
shaft_power = mc.get_variable("LabOpPoint_ShaftPower")
power_factor = mc.get_variable("LabOpPoint_PowerFactor")

stator_cu_loss = mc.get_variable("LabOpPoint_StatorCopperLoss")
rotor_cu_loss = mc.get_variable("LabOpPoint_RotorCopperLoss")
iron_loss = mc.get_variable("LabOpPoint_IronLoss")
mechanical_loss = mc.get_variable("LabOpPoint_MechanicalLoss")
stray_loss = mc.get_variable("LabOpPoint_StrayLoss")

winding_temp = mc.get_variable("T_[Winding_Average"])

print(f"=== Lab Results ===")
print(f"Shaft Torque:      {shaft_torque:.2f} Nm")
print(f"Input Power:       {input_power/1000:.2f} kW")
print(f"Shaft Power:       {shaft_power/1000:.2f} kW")
print(f"Efficiency:        {efficiency:.2f}%")
print(f"Power Factor:      {power_factor:.3f}")
print(f"Stator Cu Loss:    {stator_cu_loss:.1f} W")
print(f"Rotor Cu Loss:     {rotor_cu_loss:.1f} W")
print(f"Iron Loss:         {iron_loss:.1f} W")
print(f"Mechanical Loss:   {mechanical_loss:.1f} W")
print(f"Stray Loss:        {stray_loss:.1f} W")
print(f"Winding Temp:      {winding_temp:.1f} °C")

# --- Export Results to .mat ---
mc.export_lab_results_mat(r"D:\SRM\Results\lab_results.mat")
print("Results exported to .mat file")
```

---

## Key Variables Reference

### Lab Model Configuration
| Variable | Unit | Description |
|---|---|---|
| `ModelType_MotorLAB` | — | 0=Fast, 1=Standard, 2=Detailed |
| `SatModelPoints_MotorLAB` | — | Saturation curve resolution (10-100) |
| `BuildSatModel_MotorLAB` | bool | Auto-build saturation model on run |

### Operating Point
| Variable | Unit | Description |
|---|---|---|
| `Shaft_Speed_[RPM]` | RPM | Rotor speed |
| `PeakCurrent` | A | Peak phase current |
| `DCBusVoltage` | V | DC bus voltage |
| `PhaseAdvance` | deg | Electrical control angle |

### Lab Output Results
| Variable | Unit | Description |
|---|---|---|
| `LabOpPoint_ShaftTorque` | Nm | Average shaft torque |
| `LabOpPoint_Efficiency` | % | Overall motor efficiency |
| `LabOpPoint_InputPower` | W | Electrical input power |
| `LabOpPoint_ShaftPower` | W | Mechanical output power |
| `LabOpPoint_PowerFactor` | — | Power factor |

### Lab Loss Components
| Variable | Unit | Description |
|---|---|---|
| `LabOpPoint_StatorCopperLoss` | W | Stator copper loss |
| `LabOpPoint_RotorCopperLoss` | W | Rotor copper loss (induction) |
| `LabOpPoint_IronLoss` | W | Core/iron loss |
| `LabOpPoint_MechanicalLoss` | W | Friction and windage |
| `LabOpPoint_StrayLoss` | W | Stray load loss |

### Thermal Results (from Lab)
| Variable | Unit | Description |
|---|---|---|
| `T_[Winding_Min]` | °C | Minimum winding temperature |
| `T_[Winding_Max]` | °C | Maximum winding temperature |
| `T_[Winding_Average]` | °C | Average winding temperature |

---

## Model Types

| Type | Value | Description |
|---|---|---|
| Fast | 0 | Simplified calculation, fastest |
| Standard | 1 | Balanced speed/accuracy |
| Detailed | 2 | Full saturation model, most accurate |

---

## Output Format

### .mat File Contents
The exported `.mat` file contains MATLAB-compatible variables:
- Operating point results (torque, efficiency, power)
- Loss breakdown (copper, iron, mechanical, stray)
- Temperature results
- Inductance characteristics (Ld, Lq)
- Saturation data if model was built

---

## Workflow Summary

```
1. connect_motorcad()
2. load_from_file()
3. show_lab_context()
4. configure Lab model parameters
5. set operating point
6. do_lab_calculation()
7. read results
8. export to .mat (optional)
```

---

## When to Use Lab vs EMag

| Aspect | Lab | EMag |
|---|---|---|
| Speed | Fast (<1 sec) | Slow (60-90 sec) |
| Accuracy | Good for steady-state | High (FEA-based) |
| Use case | Parametric sweeps, optimization | Final validation, detailed analysis |
| Saturation | Pre-computed model | Full FEA solution |
| Waveforms | Not available | Available (torque, flux) |

---

## Related Pages

- [[pymotorcad-lab-api]] — Lab module API methods
- [[pymotorcad-emag-example]] — EMag analysis workflow
- [[pymotorcad-calculations-api]] — Calculation methods reference
- [[pymotorcad-set-variable]] — Variable setting API
- [[pymotorcad-get-variable]] — Variable reading API
- [[pymotorcad-thermal-example]] — Thermal analysis workflow
