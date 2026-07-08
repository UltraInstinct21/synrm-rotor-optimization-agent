---
type: pymotorcad_example
title: "Thermal Analysis Example Script"
source: "PyMotorCAD Documentation"
tags:
  - pymotorcad
  - thermal
  - example
  - workflow
  - steady-state
  - transient
  - cooling
aliases: ["Thermal Example", "Thermal Analysis"]
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM", "BLDC", "SRM"]
---

# Thermal Analysis Example Script

## Overview

Complete thermal analysis workflow using PyMotorCAD. This example demonstrates setting loss inputs, configuring cooling systems, running steady-state and transient thermal simulations, and reading temperature results.

---

## Full Script

```python
import ansys.motorcad.core as pymotorcad
import matplotlib.pyplot as plt
import numpy as np

# --- Connection ---
mc = pymotorcad.MotorCAD(open_new_instance=True)
mc.set_variable("MessageDisplayState", 2)

# --- Load Template ---
mc.load_from_file(r"D:\SRM\Motor_CAD\SRM_1.mot")

# --- Switch to Thermal Context ---
mc.show_thermal_context()

# --- Set Loss Inputs (from EMag or Lab) ---
mc.set_variable("StatorCopperLossAC", 850)      # W
mc.set_variable("StatorIronLoss_Total", 320)    # W
mc.set_variable("RotorIronLoss", 50)            # W
mc.set_variable("MagnetLoss", 0)                # W (SynRM = 0)
mc.set_variable("MechanicalLoss", 45)           # W
mc.set_variable("StrayLoadLoss", 25)            # W

# --- Configure Housing Geometry ---
mc.set_variable("Housing_Dia", 350)             # mm
mc.set_variable("Housing_Length", 200)          # mm

# --- Configure Water Jacket ---
mc.set_variable("WJ_Fluid_Volume_Flow_Rate", 10)   # L/min
mc.set_variable("WJ_Fluid_Inlet_Temperature", 65)   # °C
mc.set_variable("WJ_Type", 1)                        # 1 = Housing jacket
mc.set_variable("WJ_Flow_Path", 0)                   # 0 = Axial

# --- Configure End Space Cooling ---
mc.set_variable("EndSpace_Coefficient", 50)     # W/m²K (air convection)
mc.set_variable("EndSpace_Air_Velocity", 5)     # m/s

# --- Configure Shaft Cooling ---
mc.set_variable("Shaft_Cooling", 0)             # 0 = No shaft cooling

# --- Ambient Temperature ---
mc.set_variable("AmbientTemperature", 40)       # °C

# --- Run Steady-State Thermal Analysis ---
mc.do_steady_state_analysis()

# --- Read Temperature Results ---
t_winding_min = mc.get_variable("T_[Winding_Min]")
t_winding_max = mc.get_variable("T_[Winding_Max]")
t_winding_avg = mc.get_variable("T_[Winding_Average]")
t_stator_core = mc.get_variable("T_[Stator_Core]")
t_magnet = mc.get_variable("T_[Magnet]")
t_shaft = mc.get_variable("T_[Shaft]")
t_housing = mc.get_variable("T_[Housing]")

print(f"=== Steady-State Thermal Results ===")
print(f"Winding Min:     {t_winding_min:.1f} °C")
print(f"Winding Max:     {t_winding_max:.1f} °C")
print(f"Winding Avg:     {t_winding_avg:.1f} °C")
print(f"Stator Core:     {t_stator_core:.1f} °C")
print(f"Magnet:          {t_magnet:.1f} °C")
print(f"Shaft:           {t_shaft:.1f} °C")
print(f"Housing:         {t_housing:.1f} °C")

# --- Transient Thermal Analysis ---
mc.set_variable("TransientCalculation", True)
mc.set_variable("TransientTime_Total", 600)     # seconds (10 min)
mc.set_variable("TransientTime_Step", 10)       # seconds

mc.do_transient_analysis()

# --- Read Transient Results ---
time_data = mc.get_graph_variable("Temperature Transient", "x")
winding_temp = mc.get_graph_variable("Temperature Transient", "y")

plt.figure(figsize=(10, 6))
plt.plot(time_data, winding_temp)
plt.xlabel("Time (s)")
plt.ylabel("Winding Temperature (°C)")
plt.title("Transient Thermal Response - Winding")
plt.grid(True)
plt.savefig(r"D:\SRM\Results\thermal_transient.png", dpi=150)
plt.show()

# --- Export Results ---
mc.save_to_file(r"D:\SRM\Motor_CAD\SRM_1_thermal.mot")
```

---

## Key Variables Reference

### Loss Inputs
| Variable | Unit | Description |
|---|---|---|
| `StatorCopperLossAC` | W | AC copper loss in stator windings |
| `StatorIronLoss_Total` | W | Total iron loss in stator |
| `RotorIronLoss` | W | Iron loss in rotor lamination |
| `MagnetLoss` | W | Magnet eddy current loss |
| `MechanicalLoss` | W | Friction and windage loss |
| `StrayLoadLoss` | W | Stray load loss |

### Housing Geometry
| Variable | Unit | Description |
|---|---|---|
| `Housing_Dia` | mm | Outer diameter of motor housing |
| `Housing_Length` | mm | Axial length of motor housing |

### Water Jacket Configuration
| Variable | Unit | Description |
|---|---|---|
| `WJ_Fluid_Volume_Flow_Rate` | L/min | Coolant flow rate |
| `WJ_Fluid_Inlet_Temperature` | °C | Coolant inlet temperature |
| `WJ_Type` | — | 0=None, 1=Housing, 2=End winding, 3=Both |
| `WJ_Flow_Path` | — | 0=Axial, 1=Helical |

### End Space Cooling
| Variable | Unit | Description |
|---|---|---|
| `EndSpace_Coefficient` | W/m²K | Air convection coefficient |
| `EndSpace_Air_Velocity` | m/s | Air velocity in end space |

### Transient Settings
| Variable | Unit | Description |
|---|---|---|
| `TransientCalculation` | bool | Enable transient analysis |
| `TransientTime_Total` | s | Total simulation time |
| `TransientTime_Step` | s | Time step resolution |

### Temperature Outputs
| Variable | Unit | Description |
|---|---|---|
| `T_[Winding_Min]` | °C | Minimum winding temperature |
| `T_[Winding_Max]` | °C | Maximum winding temperature |
| `T_[Winding_Average]` | °C | Average winding temperature |
| `T_[Stator_Core]` | °C | Stator core temperature |
| `T_[Magnet]` | °C | Magnet temperature |
| `T_[Shaft]` | °C | Shaft temperature |
| `T_[Housing]` | °C | Housing temperature |

---

## Heat Transfer Correlation

The water jacket heat transfer coefficient can be estimated using the Dittus-Boelter correlation:

```
h = 0.005 × k × ρ × u / μ
```

Where:
- `h` = heat transfer coefficient (W/m²K)
- `k` = thermal conductivity of coolant (W/m·K)
- `ρ` = density of coolant (kg/m³)
- `u` = flow velocity (m/s)
- `μ` = dynamic viscosity (Pa·s)

For water at 65°C:
- k ≈ 0.66 W/m·K
- ρ ≈ 980 kg/m³
- μ ≈ 4.2×10⁻⁴ Pa·s

---

## Cooling System Types

| Type | Variable Value | Description |
|---|---|---|
| None | 0 | No active cooling |
| Housing Water Jacket | 1 | Coolant channels in motor housing |
| End Winding Spray | 2 | Direct spray on end windings |
| Both | 3 | Housing jacket + end winding spray |
| Shaft Spiral | 4 | Spiral channel in shaft |
| Ventilated | 5 | Forced air ventilation |

---

## Workflow Summary

### Steady-State Analysis
```
1. connect_motorcad()
2. load_from_file()
3. show_thermal_context()
4. set loss inputs (from EMag/Lab)
5. configure housing geometry
6. configure cooling system
7. set ambient temperature
8. do_steady_state_analysis()
9. read temperature results
```

### Transient Analysis
```
1. Complete steady-state setup
2. enable transient calculation
3. set total time and time step
4. do_transient_analysis()
5. read time-domain results
6. plot temperature vs time
```

---

## Thermal Limit Checks

| Component | Typical Limit | Consequence of Exceeding |
|---|---|---|
| Winding (Class F) | 155 °C | Insulation degradation |
| Winding (Class H) | 180 °C | Insulation failure |
| Magnet (N42SH) | 150 °C | Demagnetization |
| Bearing | 120 °C | Lubricant failure |
| Shaft seal | 100 °C | Seal degradation |

---

## Tips

- Always run EMag or Lab calculations first to obtain accurate loss values
- Verify water jacket flow rate is sufficient for the loss level
- Check winding hotspot temperature, not just average
- For transient analysis, use small time steps during initial warm-up period
- Compare steady-state result with transient at t → ∞ for validation

---

## Related Pages

- [[pymotorcad-thermal-steady-state]] — Steady-state thermal API
- [[pymotorcad-thermal-transient]] — Transient thermal API
- [[pymotorcad-calculations-api]] — Calculation methods reference
- [[pymotorcad-emag-example]] — EMag analysis (provides loss inputs)
- [[pymotorcad-lab-model-example]] — Lab analysis (provides loss inputs)
- [[pymotorcad-set-variable]] — Variable setting API
- [[pymotorcad-get-variable]] — Variable reading API
- [[pymotorcad-thermal-twin-builder]] — Thermal model Twin Builder export
