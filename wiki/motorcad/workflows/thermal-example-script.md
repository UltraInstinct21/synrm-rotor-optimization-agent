---
type: motorcad_workflow
name: "Thermal Analysis Example Script"
purpose: "Complete thermal analysis workflow: setup, steady-state, transient, and plotting"
prerequisites: ["Motor-CAD", "e8 template"]
source_files: ["Motor-CAD thermal example script — pymotorcad-core.md"]
confidence: Verified
---

# Thermal Analysis Example Script

## Purpose

End-to-end thermal analysis: configure housing/cooling, run steady-state and transient calculations, extract and plot temperatures.

## Step-by-Step Procedure

### 1. Setup

```python
mcad = pymotorcad.MotorCAD()
mcad.set_variable("MessageDisplayState", 2)
mcad.load_template("e8")
```

### 2. Configure Thermal Parameters

```python
mcad.show_thermal_context()
mcad.set_variable("Housing_Dia", 250)
mcad.set_variable("WJ_Fluid_Volume_Flow_Rate", 0.002)
mcad.set_variable("WJ_Fluid_Inlet_Temperature", 25)
mcad.set_fluid("HousingWJFluid", "Dynalene HF-LO")
```

### 3. Set Heat Transfer Correlation

```python
mcad.set_variable("Calc/Input_h[WJ]_Rear_Housing", 1)
wj_fluid_k = mcad.get_variable("WJ_Fluid_Thermal_Conductivity")
wj_fluid_rho = mcad.get_variable("WJ_Fluid_Density")
wj_fluid_mu = mcad.get_variable("WJ_Fluid_Dynamic_Viscosity")
wj_fluid_u_a = mcad.get_array_variable("HousingWJ_Velocity_A", 0)
h_A = 0.005 * wj_fluid_k * wj_fluid_rho * wj_fluid_u_a / wj_fluid_mu
mcad.set_array_variable("HousingWJ_InputH_A", 0, h_A)
```

### 4. Steady-State Calculation

```python
mcad.do_steady_state_analysis()

# Get results
node_temperature = mcad.get_node_temperature(13)
winding_temp_min = mcad.get_variable("T_[Winding_Min]")
winding_temp_max = mcad.get_variable("T_[Winding_Max]")
winding_temp_avg = mcad.get_variable("T_[Winding_Average]")
```

### 5. Transient Calculation

```python
mcad.set_variable("Transient_Calc_Type", 0)
mcad.set_variable("Transient_Time_Period", 60)
mcad.do_transient_analysis()

# Get transient results
num_time_steps = 51
for timeStep in range(num_time_steps):
    (x, y) = mcad.get_temperature_graph_point("Winding (Avg)", timeStep)
```

## Key Variables

| Variable | Purpose |
|----------|---------|
| `Housing_Dia` | Housing diameter |
| `WJ_Fluid_Volume_Flow_Rate` | Water jacket flow rate |
| `WJ_Fluid_Inlet_Temperature` | Coolant inlet temperature |
| `T_[Winding_Min/Max/Average]` | Winding temperatures |

## Related Pages

- [[motorcad/api/calculations-methods]] — do_steady_state_analysis, do_transient_analysis
- [[motorcad/api/general-methods]] — get_variable, set_variable
- [[motorcad/workflows/thermal-steady-state]] — Internal scripting thermal
- [[motorcad/workflows/thermal-transient]] — Internal scripting transient
