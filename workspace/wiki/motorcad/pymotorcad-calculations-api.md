---
type: pymotorcad_api
title: "PyMotorCAD Calculations API"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - calculations
  - emag
  - thermal
  - mechanical
  - api
aliases:
  - pymotorcad_calc
  - motorcad_calculations
related_pages:
  - "[[pymotorcad-emag-example]]"
  - "[[pymotorcad-thermal-example]]"
  - "[[pymotorcad-lab-api]]"
  - "[[pymotorcad-geometry-basic]]"
confidence: verified
---

# PyMotorCAD Calculations API

## Overview

The Calculations API contains all core simulation methods in PyMotorCAD. These methods trigger Motor-CAD's internal solvers for electromagnetic, thermal, mechanical, and multi-physics analyses. Each calculation method switches to the appropriate Motor-CAD context automatically before execution.

---

## Electromagnetic Calculations

### `do_magnetic_calculation()`

#### Purpose

Runs a steady-state electromagnetic (EMag) finite-element calculation for the current model geometry, materials, and operating point.

#### Signature

```python
do_magnetic_calculation() -> None
```

#### Description

This is the primary EMag solver call. It:

1. Switches to the Magnetic context (if not already there)
2. Meshes the geometry
3. Solves the nonlinear magnetic field problem
4. Computes torque, losses, flux densities, inductances, and voltage waveforms
5. Stores results accessible via `get_variable()`

#### Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Set operating point
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)
mc.set_variable("PeakCurrent", 100)

# Run EMag calculation
mc.do_magnetic_calculation()

# Read results
torque = mc.get_variable("ShaftTorque")
efficiency = mc.get_variable("Efficiency")
input_power = mc.get_variable("InputPower")

print(f"Torque: {torque:.2f} Nm")
print(f"Efficiency: {efficiency:.2f}%")
```

#### Prerequisites

- Model must be loaded with valid geometry
- Stator and rotor laminations must have material assigned
- Winding configuration must be defined
- Operating point (speed, current, angle) must be set

#### Key Output Variables

| Variable | Description | Units |
|---|---|---|
| `ShaftTorque` | Average electromagnetic torque | Nm |
| `Efficiency` | Overall efficiency | % |
| `InputPower` | Electrical input power | W |
| `StatorCopperLossAC` | AC copper loss in stator | W |
| `StatorIronLoss_Total` | Total stator iron loss | W |
| `PeakLineLineVoltage` | Peak line-line voltage | V |

#### Timing

Typical runtime: 60–120 seconds depending on geometry complexity and mesh density.

---

### `do_magnetic_thermal_calculation()`

#### Purpose

Runs a coupled electromagnetic + thermal calculation, solving the magnetic field and thermal problem iteratively until convergence.

#### Signature

```python
do_magnetic_thermal_calculation() -> None
```

#### Description

This method performs a one-way or bidirectional coupling between EMag and thermal solvers:

1. Runs `do_magnetic_calculation()` to get losses
2. Applies losses as heat sources in the thermal model
3. Solves the thermal problem to get temperatures
4. Optionally updates material properties with temperature-dependent values
5. Re-runs EMag with updated temperatures
6. Iterates until convergence

#### Example

```python
mc.do_magnetic_thermal_calculation()

# Results include both EMag and thermal outputs
torque = mc.get_variable("ShaftTorque")
winding_temp = mc.get_variable("T_[Winding_Average]")
rotor_temp = mc.get_variable("T_[Rotor]")
```

#### Use Cases

- Motors with significant thermal effects on performance
- High-current-density designs where winding resistance changes with temperature
- Optimizing cooling system effectiveness
- Validating thermal margins at rated and overload conditions

#### Key Thermal Output Variables

| Variable | Description | Units |
|---|---|---|
| `T_[Winding_Min]` | Minimum winding temperature | °C |
| `T_[Winding_Max]` | Maximum winding temperature | °C |
| `T_[Winding_Average]` | Average winding temperature | °C |
| `T_[Rotor]` | Rotor temperature | °C |
| `T_[Stator_Lam]` | Stator lamination temperature | °C |
| `T_[Magnet]` | Magnet temperature (PM motors) | °C |

---

### `calculate_torque_envelope()`

#### Purpose

Calculates the torque-speed envelope across a range of speeds, determining maximum torque capability at each operating point.

#### Signature

```python
calculate_torque_envelope() -> None
```

#### Description

This method performs multiple EMag calculations across the speed range to map out the full torque-speed characteristic. It accounts for voltage limits, current limits, and field-weakening behavior.

#### Example

```python
mc.set_variable("Speed_Min", 0)
mc.set_variable("Speed_Max", 6000)
mc.set_variable("Speed_Points", 20)

mc.calculate_torque_envelope()

# Access envelope data
max_torque = mc.get_variable("MaxTorqueEnvelope")
base_speed = mc.get_variable("BaseSpeed")
```

#### Use Cases

- Validating motor performance across the full operating range
- Determining constant-torque and field-weakening regions
- Sizing the motor for specific drive cycles
- Creating efficiency maps

---

### `calculate_saturation_map()`

#### Purpose

Generates electromagnetic saturation and loss data across a range of current levels and angles for use in control system mapping and loss estimation.

#### Signature

```python
calculate_saturation_map() -> None
```

#### Description

Performs a parametric sweep of current magnitude and angle, recording flux linkage, inductance, and loss data at each operating point. The resulting map is used for:

- Ld/Lq inductance mapping
- Flux linkage mapping
- Core loss characterization
- Control algorithm calibration

#### Example

```python
mc.set_variable("Current_Max", 150)
mc.set_variable("Current_Points", 10)
mc.set_variable("Angle_Points", 19)

mc.calculate_saturation_map()

# Retrieve map data
ld_map = mc.get_variable("Ld_Map")
lq_map = mc.get_variable("Lq_Map")
```

---

## Thermal Calculations

### `do_steady_state_analysis()`

#### Purpose

Runs a thermal steady-state analysis, solving for equilibrium temperatures under given loss inputs and cooling conditions.

#### Signature

```python
do_steady_state_analysis() -> None
```

#### Description

The steady-state thermal solver finds the temperature distribution where heat generation equals heat dissipation. It uses the thermal network model with nodes representing motor components.

#### Example

```python
mc.show_thermal_context()

# Set coolant conditions
mc.set_variable("Coolant_Temperature", 65)
mc.set_variable("Flow_Rate", 10)

# Set ambient conditions
mc.set_variable("Ambient_Temperature", 40)

# Run steady-state
mc.do_steady_state_analysis()

# Read temperatures
winding_temp = mc.get_variable("T_[Winding_Average]")
magnet_temp = mc.get_variable("T_[Magnet]")
```

#### Use Cases

- Verifying thermal limits are not exceeded at rated operation
- Sizing cooling systems
- Comparing thermal performance of different cooling configurations
- Validating thermal margin for IE5 efficiency compliance

---

### `do_transient_analysis()`

#### Purpose

Runs a thermal transient analysis, computing the time-varying temperature response to time-varying loss inputs.

#### Signature

```python
do_transient_analysis() -> None
```

#### Description

Unlike steady-state analysis, transient analysis captures thermal dynamics — how temperatures evolve over time. This is critical for:

- Duty cycle evaluation
- Overload capability assessment
- Start-up thermal behavior
- Intermittent operation characterization

#### Example

```python
mc.set_variable("Time_Final", 3600)  # 1 hour simulation
mc.set_variable("Time_Step", 10)     # 10-second steps

mc.do_transient_analysis()

# Read temperature at final time step
final_winding_temp = mc.get_variable("T_[Winding_Average]")
```

---

## Mechanical Calculations

### `do_mechanical_calculation()`

#### Purpose

Runs a mechanical stress analysis on the rotor, evaluating centrifugal stresses at the operating speed.

#### Signature

```python
do_mechanical_calculation() -> None
```

#### Description

At high speeds, centrifugal forces on the rotor can exceed material yield strength, particularly at thin bridges and ribs in SynRM rotors. This calculation evaluates mechanical integrity.

#### Example

```python
mc.set_variable("Shaft_Speed_[RPM]", 6000)  # Max speed

mc.do_mechanical_calculation()

# Check stress results
max_stress = mc.get_variable("Max_Stress")
safety_factor = mc.get_variable("Safety_Factor")
```

#### Use Cases

- Validating rotor mechanical integrity at max speed
- Optimizing bridge and rib thickness for mechanical strength
- Ensuring manufacturing feasibility
- High-speed motor design validation

---

## Multi-Physics Calculations

### `do_multi_force_calculation()`

#### Purpose

Calculates force harmonics at a specified operating point, useful for NVH (Noise, Vibration, Harshness) analysis.

#### Signature

```python
do_multi_force_calculation() -> None
```

#### Description

This method computes the spatial and temporal force harmonics acting on the stator teeth, which are the primary source of electromagnetic noise and vibration.

#### Example

```python
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)

mc.do_multi_force_calculation()

# Retrieve force harmonic data
force_harmonics = mc.get_variable("Force_Harmonics")
```

---

### `do_weight_calculation()`

#### Purpose

Calculates the weight of all motor components based on the current geometry and material assignments.

#### Signature

```python
do_weight_calculation() -> None
```

#### Description

Computes mass of each motor component (stator lamination, rotor lamination, copper, magnets, shaft, housing, etc.) and total motor weight.

#### Example

```python
mc.do_weight_calculation()

total_weight = mc.get_variable("Total_Mass")
stator_weight = mc.get_variable("Stator_Lam_Mass")
copper_weight = mc.get_variable("Copper_Mass")
rotor_weight = mc.get_variable("Rotor_Lam_Mass")
```

#### Use Cases

- Power density optimization
- Cost estimation
- Application-specific weight constraints
- Comparing topologies

---

## Force Harmonics

### `calculate_force_harmonics_spatial()`

#### Purpose

Calculates spatial force harmonics acting on the stator bore surface.

#### Signature

```python
calculate_force_harmonics_spatial() -> None
```

#### Description

Spatial force harmonics describe the radial force distribution around the stator bore as a function of angular position. They are decomposed into spatial orders (harmonic numbers).

---

### `calculate_force_harmonics_temporal()`

#### Purpose

Calculates temporal force harmonics — the time-varying component of electromagnetic forces.

#### Signature

```python
calculate_force_harmonics_temporal() -> None
```

#### Description

Temporal force harmonics describe how the radial force at each spatial location varies with time. Combined with spatial harmonics, they provide the complete force field for NVH prediction.

---

## Winding Pattern

### `create_winding_pattern()`

#### Purpose

Creates or modifies the winding pattern definition for the motor model.

#### Signature

```python
create_winding_pattern() -> None
```

#### Description

Defines the coil arrangement, number of turns, parallel paths, and winding factors. This must be configured before running any EMag calculation.

#### Example

```python
mc.set_variable("Coil_Pitch", 10)
mc.set_variable("Series_Turns", 44)
mc.set_variable("Parallel_Paths", 2)

mc.create_winding_pattern()
```

---

## Calculation Context Switching

Motor-CAD organizes calculations by context. The calculation methods handle context switching automatically, but understanding the contexts is important:

| Context | Methods | Purpose |
|---|---|---|
| Magnetic | `do_magnetic_calculation()`, `do_magnetic_thermal_calculation()` | Electromagnetic analysis |
| Thermal | `do_steady_state_analysis()`, `do_transient_analysis()` | Thermal analysis |
| Mechanical | `do_mechanical_calculation()` | Structural analysis |
| Lab | `calculate_magnetic_lab()`, etc. | System-level analysis |

---

## Complete Workflow Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Set operating point
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)
mc.set_variable("PeakCurrent", 100)

# 1. Run EMag
mc.do_magnetic_calculation()
torque = mc.get_variable("ShaftTorque")
print(f"Torque: {torque:.2f} Nm")

# 2. Run coupled EMag+Thermal
mc.do_magnetic_thermal_calculation()
winding_temp = mc.get_variable("T_[Winding_Average]")
print(f"Winding Temp: {winding_temp:.1f} C")

# 3. Check mechanical at max speed
mc.set_variable("Shaft_Speed_[RPM]", 6000)
mc.do_mechanical_calculation()
max_stress = mc.get_variable("Max_Stress")
print(f"Max Stress: {max_stress:.1f} MPa")

# 4. Calculate weight
mc.do_weight_calculation()
total_mass = mc.get_variable("Total_Mass")
print(f"Total Mass: {total_mass:.2f} kg")
```

---

## Cross-References

- [[pymotorcad-emag-example]] — Complete electromagnetic workflow example
- [[pymotorcad-thermal-example]] — Thermal analysis workflow
- [[pymotorcad-lab-api]] — Lab (system-level) calculations
- [[pymotorcad-geometry-basic]] — Geometry setup before calculations
- [[pymotorcad-graphs-api]] — Extracting results as graphs
- [[pymotorcad-motorcad-api]] — Full API reference

---

## Tags

#pymotorcad #motorcad #api #calculations #emag #thermal #mechanical #finite-element #simulation #torque #losses #temperature
