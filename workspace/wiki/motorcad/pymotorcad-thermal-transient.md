---
type: motorcad_api
title: PyMotorCAD - Thermal Transient Analysis
source: PyMotorCAD Documentation
tags:
  - motorcad
  - pymotorcad
  - thermal
  - transient
  - time-dependent
  - hook
---

# PyMotorCAD - Thermal Transient Analysis

## Overview

Perform thermal transient analysis in Motor-CAD with time-dependent boundary conditions. The hook class mechanism allows dynamic changes to thermal parameters during the simulation.

## Hook Class: `thermal_transient`

The `thermal_transient` class provides three hook methods for time-dependent thermal analysis.

### Class Structure

```python
class thermal_transient:
    def initial(self, mc):
        """Called at the start of transient simulation."""
        pass
    
    def main(self, mc):
        """Called at each time step."""
        pass
    
    def final(self, mc):
        """Called when transient simulation completes."""
        pass
```

## Key Variables

| Variable | Description | Units |
|----------|-------------|-------|
| `CurrentTime` | Current simulation time | s |
| `WJ_Fluid_Volume_Flow_Rate` | Water jacket fluid flow rate | L/min |
| `Wet_Rotor_Fluid_Volume_Flow_Rate` | Wet rotor fluid flow rate | L/min |

## Time-Dependent Boundary Conditions

### Variable Update Pattern

```python
class thermal_transient:
    def initial(self, mc):
        """Set initial conditions."""
        mc.set_variable("WJ_Fluid_Volume_Flow_Rate", 10.0)
    
    def main(self, mc):
        """Update boundary conditions at each time step."""
        current_time = mc.get_variable("CurrentTime")
        
        # Example: flow rate varies with time
        if current_time < 100:
            flow_rate = 10.0
        elif current_time < 200:
            flow_rate = 5.0
        else:
            flow_rate = 2.0
        
        mc.set_variable("WJ_Fluid_Volume_Flow_Rate", flow_rate)
    
    def final(self, mc):
        """Read final results."""
        max_temp = mc.get_node_temperature("Winding_Max")
        print(f"Maximum winding temperature: {max_temp} °C")
```

## Complete Example

```python
import ansys.motorcad.core as pymotorcad

class thermal_transient:
    def initial(self, mc):
        """Initialize transient simulation."""
        print("Starting transient thermal analysis")
        mc.set_variable("WJ_Fluid_Volume_Flow_Rate", 10.0)
        mc.set_variable("Wet_Rotor_Fluid_Volume_Flow_Rate", 5.0)
    
    def main(self, mc):
        """Update conditions at each time step."""
        current_time = mc.get_variable("CurrentTime")
        
        # Cooling flow decreases over time
        wj_flow = max(2.0, 10.0 - (current_time * 0.01))
        mc.set_variable("WJ_Fluid_Volume_Flow_Rate", wj_flow)
        
        # Log progress
        if int(current_time) % 50 == 0:
            temp = mc.get_node_temperature("Winding_Average")
            print(f"t={current_time:.1f}s, T_winding={temp:.1f}°C")
    
    def final(self, mc):
        """Extract final thermal results."""
        results = {
            "winding_avg": mc.get_node_temperature("Winding_Average"),
            "winding_max": mc.get_node_temperature("Winding_Max"),
            "rotor": mc.get_node_temperature("Rotor"),
        }
        print(f"Final temperatures: {results}")

# Usage
mc = pymotorcad.MotorCAD()
mc.load_from_file("model.mot")
mc.show_thermal_context()

# Configure transient parameters
mc.set_variable("TotalTime", 300)  # 300 seconds simulation
mc.set_variable("TimeStep", 1.0)    # 1 second steps

# Run with hook class
hook = thermal_transient()
mc.do_transient_analysis(hook_class=hook)
```

## Related Pages

- [[pymotorcad-thermal-steady-state]] - Steady-state thermal analysis
- [[pymotorcad-thermal-example]] - More thermal examples

## Tags

#motorcad #pymotorcad #thermal #transient #time-dependent #hook #cooling