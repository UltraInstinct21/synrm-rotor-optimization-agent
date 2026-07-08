---
type: motorcad_api
title: PyMotorCAD - Thermal Steady-State Analysis
source: PyMotorCAD Documentation
tags:
  - motorcad
  - pymotorcad
  - thermal
  - steady-state
  - hook
  - temperature
---

# PyMotorCAD - Thermal Steady-State Analysis

## Overview

Perform thermal steady-state analysis in Motor-CAD using the hook class mechanism. Custom boundary conditions and resistance values can be applied through Python callbacks.

## Hook Class: `thermal_steady`

The `thermal_steady` class provides three hook methods that execute at different stages of the thermal calculation.

### Class Structure

```python
class thermal_steady:
    def initial(self, mc):
        """Called before thermal calculation starts."""
        pass
    
    def main(self, mc):
        """Called during thermal calculation."""
        pass
    
    def final(self, mc):
        """Called after thermal calculation completes."""
        pass
```

## Key Variables

| Variable | Description | Units |
|----------|-------------|-------|
| `T_Ambient` | Ambient temperature | °C |
| `Armature_Copper_Loss_@Ref_Speed` | Copper loss at reference speed | W |

## API Methods

### `set_resistance_value()`

Sets a custom thermal resistance value.

```python
mc.set_resistance_value(node1, node2, resistance)
```

**Parameters:**
- `node1`: First thermal node
- `node2`: Second thermal node  
- `resistance`: Thermal resistance value (K/W)

### `get_node_temperature()`

Retrieves temperature at a specific thermal node.

```python
temperature = mc.get_node_temperature(node)
print(f"Node temperature: {temperature} °C")
```

**Parameters:**
- `node`: Thermal node identifier

**Returns:** Temperature value in °C.

## Complete Example

```python
import ansys.motorcad.core as pymotorcad

class thermal_steady:
    def initial(self, mc):
        """Set initial conditions before thermal solve."""
        ambient = mc.get_variable("T_Ambient")
        print(f"Ambient temperature: {ambient} °C")
    
    def main(self, mc):
        """Modify resistance values during calculation."""
        ambient = mc.get_variable("T_Ambient")
        # Custom resistance calculation
        custom_resistance = (ambient * 0.01) + 1
        mc.set_resistance_value("WJ_Node1", "WJ_Node2", custom_resistance)
    
    def final(self, mc):
        """Read results after calculation completes."""
        winding_temp = mc.get_node_temperature("Winding_Average")
        print(f"Final winding temperature: {winding_temp} °C")

# Usage
mc = pymotorcad.MotorCAD()
mc.load_from_file("model.mot")
mc.show_thermal_context()

# Run with hook class
hook = thermal_steady()
mc.do_steady_state_analysis(hook_class=hook)
```

## Related Pages

- [[pymotorcad-thermal-example]] - More thermal examples
- [[pymotorcad-calculations-api]] - Calculations API reference

## Tags

#motorcad #pymotorcad #thermal #steady-state #hook #temperature #resistance