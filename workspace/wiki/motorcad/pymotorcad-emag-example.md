---
type: pymotorcad_example
title: "EMag Example Script"
source: "PyMotorCAD Documentation"
tags:
  - pymotorcad
  - emag
  - example
  - workflow
  - magnetic-analysis
  - calculations
aliases: ["EMag Example", "Electromagnetic Analysis Example"]
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM", "BLDC", "SRM"]
---

# EMag Example Script

## Overview

Complete electromagnetic analysis workflow using PyMotorCAD. This example demonstrates loading a template, setting variables, configuring materials, running calculations, reading results, and generating graphs.

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

# --- Switch to EMag Context ---
mc.show_magnetic_context()

# --- Set Stator Variables ---
mc.set_variable("Slot_Number", 48)
mc.set_variable("Tooth_Width", 7.5)
mc.set_variable("Stator_Lam_Dia", 340)
mc.set_variable("Stator_bore", 215)
mc.set_variable("Slot_Depth", 29)

# --- Set Winding Variables ---
mc.set_variable("WireDiameter", 1.715)
mc.set_variable("Copper_Slot_Fill", 0.40)
mc.set_variable("Coil_Span", 10)  # Slot span

# --- Set Rotor Variables ---
mc.set_variable("Pole_Number", 4)
mc.set_variable("Airgap", 0.5)
mc.set_variable("Shaft_Dia", 80)

# --- Set Material ---
mc.set_component_material("Stator Lam", "50C250")
mc.set_component_material("Rotor Lam", "50C250")
mc.set_component_material("Magnet", "N42SH")

# --- Set Operating Point ---
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PeakCurrent", 100)
mc.set_variable("DCBusVoltage", 540)
mc.set_variable("PhaseAdvance", 45)  # Electrical angle (degrees)

# --- Configure Calculation ---
mc.set_variable("TorquePointsPerCycle", 60)
mc.set_variable("TorqueNumberCycles", 1)
mc.set_variable("TorqueCalculation", True)

# --- Run EMag Calculation ---
mc.do_magnetic_calculation()

# --- Read Results ---
shaft_torque = mc.get_variable("ShaftTorque")
peak_voltage = mc.get_variable("PeakLineLineVoltage")
input_power = mc.get_variable("InputPower")
stator_cu_loss = mc.get_variable("StatorCopperLossAC")
stator_iron_loss = mc.get_variable("StatorIronLoss_Total")

# --- Calculate Efficiency ---
shaft_power = shaft_torque * 3000 * 2 * 3.14159 / 60  # Convert Nm·RPM to W
efficiency = (shaft_power / input_power) * 100 if input_power > 0 else 0

print(f"=== EMag Results ===")
print(f"Shaft Torque:        {shaft_torque:.2f} Nm")
print(f"Peak L-L Voltage:    {peak_voltage:.2f} V")
print(f"Input Power:         {input_power/1000:.2f} kW")
print(f"Shaft Power:         {shaft_power/1000:.2f} kW")
print(f"Efficiency:          {efficiency:.2f}%")
print(f"Stator Cu Loss:      {stator_cu_loss:.2f} W")
print(f"Stator Iron Loss:    {stator_iron_loss:.2f} W")

# --- Generate Torque vs Waveform Graph ---
mc.graph_use("TorqueVW")
mc.graph_clear()

torque_data = mc.get_graph_variable("TorqueVW", "x")
torque_y = mc.get_graph_variable("TorqueVW", "y")

plt.figure(figsize=(10, 6))
plt.plot(torque_data, torque_y)
plt.xlabel("Electrical Angle (deg)")
plt.ylabel("Torque (Nm)")
plt.title("Torque Waveform - Full Load")
plt.grid(True)
plt.savefig(r"D:\SRM\Results\torque_waveform.png", dpi=150)
plt.show()

# --- Generate Airgap Flux Density Graph ---
mc.graph_use("B Gap (on load)")
mc.graph_clear()

gap_angle = mc.get_graph_variable("B Gap (on load)", "x")
gap_flux = mc.get_graph_variable("B Gap (on load)", "y")

plt.figure(figsize=(10, 6))
plt.plot(gap_angle, gap_flux)
plt.xlabel("Mechanical Angle (deg)")
plt.ylabel("Flux Density (T)")
plt.title("Airgap Flux Density (On Load)")
plt.grid(True)
plt.savefig(r"D:\SRM\Results\airgap_flux.png", dpi=150)
plt.show()

# --- Save Results ---
mc.save_to_file(r"D:\SRM\Motor_CAD\SRM_1_solved.mot")
```

---

## Key Variables Reference

### Stator Geometry
| Variable | Unit | Description |
|---|---|---|
| `Slot_Number` | — | Number of stator slots |
| `Tooth_Width` | mm | Stator tooth width |
| `Stator_Lam_Dia` | mm | Stator lamination outer diameter |
| `Stator_bore` | mm | Stator bore (inner) diameter |
| `Slot_Depth` | mm | Total slot depth |
| `Slot_Corner_Radius` | mm | Slot bottom corner radius |
| `Slot_Opening` | mm | Slot opening width |

### Winding
| Variable | Unit | Description |
|---|---|---|
| `WireDiameter` | mm | Conductor wire diameter |
| `Copper_Slot_Fill` | — | Copper fill factor (0-1) |
| `Coil_Span` | slots | Coil throw (slot span) |

### Rotor
| Variable | Unit | Description |
|---|---|---|
| `Pole_Number` | — | Number of rotor poles |
| `Airgap` | mm | Mechanical airgap |
| `Shaft_Dia` | mm | Shaft diameter |

### Operating Point
| Variable | Unit | Description |
|---|---|---|
| `Shaft_Speed_[RPM]` | RPM | Rotor mechanical speed |
| `PeakCurrent` | A | Peak phase current |
| `DCBusVoltage` | V | DC bus voltage |
| `PhaseAdvance` | deg | Electrical control angle |

### Calculation Settings
| Variable | Unit | Description |
|---|---|---|
| `TorquePointsPerCycle` | — | Samples per electrical cycle |
| `TorqueNumberCycles` | — | Number of cycles to simulate |
| `TorqueCalculation` | bool | Enable torque calculation |

---

## Result Variables

| Variable | Unit | Description |
|---|---|---|
| `ShaftTorque` | Nm | Average shaft torque |
| `PeakLineLineVoltage` | V | Peak line-to-line voltage |
| `InputPower` | W | Total electrical input power |
| `StatorCopperLossAC` | W | AC copper loss in stator |
| `StatorIronLoss_Total` | W | Total iron loss in stator |

---

## Available Graphs

| Graph Name | Description |
|---|---|
| `TorqueVW` | Torque vs electrical angle |
| `B Gap (on load)` | Airgap flux density (loaded) |
| `B Gap (no load)` | Airgap flux density (no load) |
| `Flux Linkage` | Phase flux linkage vs angle |
| `Inductance` | Ld/Lq vs current angle |

---

## Workflow Summary

```
1. connect_motorcad()
2. load_from_file()
3. show_magnetic_context()
4. set stator variables
5. set winding variables
6. set rotor variables
7. set materials
8. set operating point
9. configure calculation parameters
10. do_magnetic_calculation()
11. read results
12. generate graphs
13. save model
```

---

## Related Pages

- [[pymotorcad-calculations-api]] — Calculation methods reference
- [[pymotorcad-graphs-api]] — Graph generation API
- [[pymotorcad-set-variable]] — Setting MotorCAD variables
- [[pymotorcad-get-variable]] — Reading MotorCAD variables
- [[pymotorcad-thermal-example]] — Thermal analysis workflow
- [[pymotorcad-adaptive-templates-guide]] — Geometry creation guide
- [[pymotorcad-emag-twin-builder]] — Twin Builder export
