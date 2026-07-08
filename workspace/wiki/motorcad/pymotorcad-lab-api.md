---
type: pymotorcad_api
title: "PyMotorCAD Lab API"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - lab
  - system-level
  - duty-cycle
  - efficiency-map
  - api
aliases:
  - pymotorcad_lab
  - motorcad_lab
related_pages:
  - "[[pymotorcad-lab-model-example]]"
  - "[[pymotorcad-calculations-api]]"
  - "[[pymotorcad-emag-example]]"
  - "[[pymotorcad-motorcad-api]]"
confidence: verified
---

# PyMotorCAD Lab API

## Overview

The Lab API provides system-level simulation capabilities in Motor-CAD. Unlike the component-level EMag and thermal solvers, Lab operates at the **motor-drive system level**, combining motor electromagnetic models with inverter models, control strategies, duty cycles, and thermal models to evaluate real-world performance.

Lab is essential for:

- Efficiency map generation
- Drive cycle evaluation
- EV powertrain sizing
- Thermal performance under variable loading
- Loss breakdown across operating regions

---

## Model Building

### `build_model_lab()`

#### Purpose

Constructs the Lab system-level model by linking the electromagnetic motor model, inverter model, control parameters, and thermal model into a unified simulation framework.

#### Signature

```python
build_model_lab() -> None
```

#### Description

This method assembles the complete Lab model from the component definitions already configured in Motor-CAD. It:

1. Reads the EMag motor model (geometry, materials, winding)
2. Configures the inverter model (switching frequency, losses, voltage limits)
3. Links the control strategy (FOC, DTC, etc.)
4. Attaches the thermal model for loss-temperature feedback
5. Prepares the model for operating point, duty cycle, or efficiency map calculations

#### Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Configure inverter parameters
mc.set_variable("DC_bus_voltage", 400)
mc.set_variable("Switching_Frequency", 10000)
mc.set_variable("Inverter_Efficiency", 98)

# Build the Lab model
mc.build_model_lab()
```

#### Prerequisites

- A valid motor model must be loaded
- EMag geometry and materials must be defined
- Inverter parameters must be set
- Control parameters must be configured

#### Inverter Parameters

| Variable | Description | Typical Units |
|---|---|---|
| `DC_bus_voltage` | DC link voltage | V |
| `Switching_Frequency` | PWM switching frequency | Hz |
| `Inverter_Efficiency` | Average inverter efficiency | % |
| `Current_ripple` | Allowable current ripple | % |

---

## Magnetic Lab Calculations

### `calculate_magnetic_lab()`

#### Purpose

Runs an electromagnetic calculation within the Lab framework at a specified operating point, incorporating inverter effects and control constraints.

#### Signature

```python
calculate_magnetic_lab() -> None
```

#### Description

Unlike `do_magnetic_calculation()` which operates at the component level, this method runs within the Lab context and includes:

- Inverter voltage and current limits
- Field-weakening control constraints
- PWM harmonics effects
- Temperature-dependent resistance feedback

#### Example

```python
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("ShaftTorque", 143)

mc.calculate_magnetic_lab()

# Read Lab-specific results
efficiency = mc.get_variable("Efficiency")
input_power = mc.get_variable("InputPower")
stator_loss = mc.get_variable("StatorCopperLossAC")
iron_loss = mc.get_variable("StatorIronLoss_Total")
```

---

## Thermal Lab Calculations

### `calculate_thermal_lab()`

#### Purpose

Runs a thermal calculation within the Lab context, using the loss distribution from a Lab magnetic calculation as the thermal load.

#### Signature

```python
calculate_thermal_lab() -> None
```

#### Description

This method applies Lab-computed losses to the thermal network and solves for temperatures. It is typically called after `calculate_magnetic_lab()` to get the thermal state at a specific operating point.

#### Example

```python
mc.calculate_magnetic_lab()
mc.calculate_thermal_lab()

winding_temp = mc.get_variable("T_[Winding_Average]")
rotor_temp = mc.get_variable("T_[Rotor]")
```

---

## Operating Point Calculation

### `calculate_operating_point_lab()`

#### Purpose

Evaluates motor performance at a single specified operating point (speed + torque) within the Lab framework, including all loss components and thermal effects.

#### Signature

```python
calculate_operating_point_lab() -> None
```

#### Description

This is the workhorse method for point evaluations. It combines:

1. Electromagnetic calculation at the specified speed/torque
2. Loss computation (copper, iron, mechanical, stray)
3. Thermal calculation (optional)
4. Efficiency computation
5. Voltage and current limit checking

#### Example

```python
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("ShaftTorque", 143)

mc.calculate_operating_point_lab()

# Comprehensive results
results = {
    "torque": mc.get_variable("ShaftTorque"),
    "speed": mc.get_variable("Shaft_Speed_[RPM]"),
    "input_power": mc.get_variable("InputPower"),
    "efficiency": mc.get_variable("Efficiency"),
    "cu_loss": mc.get_variable("StatorCopperLossAC"),
    "iron_loss": mc.get_variable("StatorIronLoss_Total"),
    "winding_temp": mc.get_variable("T_[Winding_Average]"),
    "voltage": mc.get_variable("PeakLineLineVoltage"),
    "current": mc.get_variable("PeakCurrent"),
}
```

---

## Duty Cycle Calculation

### `calculate_duty_cycle_lab()`

#### Purpose

Runs a complete duty cycle simulation, evaluating motor performance across a time-varying load profile.

#### Signature

```python
calculate_duty_cycle_lab() -> None
```

#### Description

This method simulates the motor over a prescribed duty cycle — a sequence of speed/torque points with specified durations. It tracks:

- Energy consumption per segment
- Loss accumulation over the cycle
- Temperature evolution throughout the cycle
- Average and peak efficiency
- Thermal limits compliance

#### Example

```python
# Define duty cycle (speed_torque_pairs: [speed_rpm, torque_Nm, duration_s])
mc.set_variable("Duty_Cycle_Points", 5)

# Point 1: cruise
mc.set_variable("Duty_Cycle_Speed_1", 3000)
mc.set_variable("Duty_Cycle_Torque_1", 80)
mc.set_variable("Duty_Cycle_Duration_1", 600)

# Point 2: acceleration
mc.set_variable("Duty_Cycle_Speed_2", 4500)
mc.set_variable("Duty_Cycle_Torque_2", 143)
mc.set_variable("Duty_Cycle_Duration_2", 30)

# ... more points

mc.calculate_duty_cycle_lab()

# Results
avg_efficiency = mc.get_variable("Avg_Efficiency")
peak_winding_temp = mc.get_variable("T_[Winding_Max]")
energy_consumed = mc.get_variable("Total_Energy")
```

#### Use Cases

- WLTP / FTP-75 drive cycle evaluation
- Industrial duty cycle compliance
- Thermal sizing for intermittent operation
- Energy consumption estimation

---

## Efficiency Map Export

### `export_concept_ev_model()`

#### Purpose

Exports the motor model and efficiency map data in a format suitable for EV powertrain simulation tools (e.g., AVL Cruise, GT-SUITE, Simulink).

#### Signature

```python
export_concept_ev_model(file_path: str) -> None
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `file_path` | `str` | Output file path for the exported model |

#### Description

This method generates a complete efficiency map across the speed-torque plane and exports it in a standardized format. The export includes:

- Efficiency at each (speed, torque) point
- Loss breakdown (copper, iron, mechanical)
- Voltage and current limits
- Thermal limits
- Maximum torque envelope

#### Example

```python
# Generate efficiency map
mc.build_model_lab()

# Set map resolution
mc.set_variable("Speed_Points_Map", 50)
mc.set_variable("Torque_Points_Map", 50)

mc.export_concept_ev_model(r"D:\exports\synrm_efficiency_map.csv")
```

#### Output Format

The exported file typically contains:

| Column | Description |
|---|---|
| Speed [RPM] | Operating speed |
| Torque [Nm] | Output torque |
| Efficiency [%] | Overall efficiency |
| Input Power [W] | Electrical input |
| Copper Loss [W] | Stator copper loss |
| Iron Loss [W] | Core loss |
| Voltage [V] | Required voltage |
| Current [A] | Phase current |

---

## Custom Losses

### `add_external_custom_loss()`

#### Purpose

Adds a user-defined external loss component to the Lab model, representing losses not computed by Motor-CAD's built-in solvers (e.g., inverter switching losses, mechanical friction, windage).

#### Signature

```python
add_external_custom_loss(loss_name: str, loss_value: float) -> None
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `loss_name` | `str` | Name identifier for the loss component |
| `loss_value` | `float` | Loss value in Watts |

#### Example

```python
# Add inverter switching losses (not computed by EMag)
mc.add_external_custom_loss("Inverter_Switching_Loss", 150)

# Add mechanical friction
mc.add_external_custom_loss("Bearing_Friction_Loss", 50)

# Add windage
mc.add_external_custom_loss("Windage_Loss", 30)

# These losses are included in total efficiency calculation
mc.calculate_operating_point_lab()
total_loss = mc.get_variable("Total_Loss")
```

---

### `add_internal_custom_loss()`

#### Purpose

Adds a user-defined internal loss distribution to the Lab model, allowing loss assignment to specific motor components.

#### Signature

```python
add_internal_custom_loss(loss_name: str, loss_value: float, component: str) -> None
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `loss_name` | `str` | Name identifier for the loss component |
| `loss_value` | `float` | Loss value in Watts |
| `component` | `str` | Motor component to which the loss is assigned (for thermal analysis) |

#### Example

```python
# Add stray load loss assigned to stator teeth
mc.add_internal_custom_loss("Stray_Load_Loss", 40, "Stator_Teeth")

# Add rotor surface loss
mc.add_internal_custom_loss("Rotor_Surface_Loss", 25, "Rotor")
```

#### Use Cases

- Including manufacturer-specific loss data
- Adding measured loss components from test data
- Modeling losses from external components (e.g., encoder, resolver)
- Calibrating the model to match test results

---

## Lab Workflow: Efficiency Map Generation

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Configure motor parameters
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)

# Configure inverter
mc.set_variable("DC_bus_voltage", 400)
mc.set_variable("Switching_Frequency", 10000)

# Build Lab model
mc.build_model_lab()

# Add custom losses
mc.add_external_custom_loss("Inverter_Loss", 200)
mc.add_external_custom_loss("Mechanical_Loss", 50)

# Set map resolution
mc.set_variable("Speed_Points_Map", 50)
mc.set_variable("Torque_Points_Map", 50)
mc.set_variable("Speed_Min_Map", 0)
mc.set_variable("Speed_Max_Map", 6000)
mc.set_variable("Torque_Min_Map", 0)
mc.set_variable("Torque_Max_Map", 200)

# Generate and export efficiency map
mc.export_concept_ev_model(r"D:\exports\synrm_45kw_effmap.csv")

print("Efficiency map exported successfully")
```

---

## Lab vs. EMag vs. Thermal: When to Use What

| Method | Context | Use When |
|---|---|---|
| `do_magnetic_calculation()` | EMag | Component-level EMag only |
| `do_steady_state_analysis()` | Thermal | Component-level thermal only |
| `do_magnetic_thermal_calculation()` | EMag+Thermal | Coupled EMag+thermal at one point |
| `calculate_operating_point_lab()` | Lab | System-level single point with inverter |
| `calculate_duty_cycle_lab()` | Lab | Time-varying load profile |
| `export_concept_ev_model()` | Lab | Efficiency map for EV tools |

---

## Cross-References

- [[pymotorcad-lab-model-example]] — Complete Lab model workflow example
- [[pymotorcad-calculations-api]] — Component-level calculation methods
- [[pymotorcad-emag-example]] — Electromagnetic calculation workflow
- [[pymotorcad-thermal-example]] — Thermal analysis workflow
- [[pymotorcad-motorcad-api]] — Full API reference

---

## Tags

#pymotorcad #motorcad #api #lab #system-level #efficiency-map #duty-cycle #inverter #ev #powertrain #losses
