---
type: pymotorcad_guide
title: "Thermal Twin Builder Export"
source: "PyMotorCAD Documentation"
tags:
  - pymotorcad
  - thermal
  - twin-builder
  - export
  - ROM
  - LPTN
  - workflow
aliases: ["Thermal Twin Builder Export", "Thermal ROM Export"]
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM", "BLDC", "SRM"]
---

# Thermal Twin Builder Export

## Overview

Export thermal Lumped Parameter Thermal Network (LPTN) models from MotorCAD as Reduced Order Models (ROM) for Ansys Twin Builder. The export generates matrix files representing the thermal network nodes, resistances, capacitances, power sources, and temperature initial conditions.

---

## Output File Formats

The export produces five matrix files:

| Extension | File Type | Contents |
|---|---|---|
| `.nmf` | Node Matrix File | Node positions and identifiers |
| `.rmf` | Resistance Matrix File | Thermal resistances between nodes |
| `.cmf` | Capacitance Matrix File | Thermal capacitances at nodes |
| `.pmf` | Power Matrix File | Power source inputs at nodes |
| `.tmf` | Temperature Matrix File | Initial temperature conditions |

---

## Full Script

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD(open_new_instance=True)
mc.set_variable("MessageDisplayState", 2)

# --- Load Solved Thermal Model ---
mc.load_from_file(r"D:\SRM\Motor_CAD\SRM_1_thermal.mot")
mc.show_thermal_context()

# --- Generate Twin Builder Data ---
output_dir = r"D:\SRM\TwinBuilder\thermal"

# Step 1: Generate core thermal network data
mc.generateTwinData()

# Step 2: Get node data
node_data = mc.getNodeData()
print(f"Number of thermal nodes: {len(node_data)}")

# Step 3: Generate cooling system network
mc.generateCoolingSystemNetwork()

# Step 4: Generate samples for ROM
mc.generateSamples()

# Step 5: Generate loss distribution
mc.generateLossDistribution()

# Step 6: Export matrix files
mc.exportTwinBuilderData(output_dir)

print(f"Thermal ROM exported to: {output_dir}")
print("Files generated:")
print("  - nodes.nmf")
print("  - resistance.rmf")
print("  - capacitance.cmf")
print("  - power.pmf")
print("  - temperature.tmf")
```

---

## API Methods

### generateTwinData()

Generates the core thermal network data from the MotorCAD thermal model.

```python
mc.generateTwinData()
```

**Returns:** None  
**Side effects:** Creates internal thermal network representation

---

### getNodeData()

Retrieves thermal node information from the generated network.

```python
node_data = mc.getNodeData()
```

**Returns:** List of node data dictionaries  
**Node properties:**
| Property | Type | Description |
|---|---|---|
| `id` | int | Unique node identifier |
| `name` | str | Human-readable node name |
| `type` | str | Node type (winding, core, housing, etc.) |
| `position` | tuple | (x, y, z) coordinates |

---

### generateCoolingSystemNetwork()

Generates the thermal network for cooling system components.

```python
mc.generateCoolingSystemNetwork()
```

**Supported cooling systems:**
- End Space convection
- Ventilated cooling
- Housing Water Jacket
- Shaft Spiral cooling
- Wet Rotor cooling
- Spray Cooling

---

### generateSamples()

Generates sampling points for ROM construction.

```python
mc.generateSamples()
```

---

### generateLossDistribution()

Generates the loss distribution matrix mapping power sources to thermal nodes.

```python
mc.generateLossDistribution()
```

---

### exportTwinBuilderData()

Exports all matrix files to the specified directory.

```python
mc.exportTwinBuilderData(output_dir)
```

**Parameters:**
| Parameter | Type | Description |
|---|---|---|
| `output_dir` | str | Output directory path |

---

## Loss Types (25 Categories)

The thermal model supports 25 distinct loss types:

### Copper Losses
| Loss Type | Description |
|---|---|
| Stator Copper Loss (AC) | AC resistance copper loss in stator windings |
| Stator Copper Loss (DC) | DC resistance copper loss |
| Rotor Copper Loss | Rotor winding loss (IM/WRM) |

### Iron Losses
| Loss Type | Description |
|---|---|
| Stator Iron Loss (Hysteresis) | Hysteresis component |
| Stator Iron Loss (Eddy) | Eddy current component |
| Stator Iron Loss (Excess) | Excess loss component |
| Rotor Iron Loss (Hysteresis) | Rotor hysteresis loss |
| Rotor Iron Loss (Eddy) | Rotor eddy current loss |
| Rotor Iron Loss (Excess) | Rotor excess loss |

### Magnet Losses
| Loss Type | Description |
|---|---|
| Magnet Eddy Current Loss | Eddy current loss in permanent magnets |
| Magnet Hysteresis Loss | Magnet hysteresis loss |

### Mechanical Losses
| Loss Type | Description |
|---|---|
| Bearing Friction Loss | Bearing friction |
| Windage Loss | Air resistance on rotor |
| Brush Friction Loss | Brush friction (if applicable) |

### Stray Losses
| Loss Type | Description |
|---|---|
| Stator Stray Load Loss | Stator stray load loss |
| Rotor Stray Load Loss | Rotor stray load loss |

### Other Losses
| Loss Type | Description |
|---|---|
| Slot Liner Loss | Dielectric loss in slot liners |
| Wedge Loss | Loss in slot wedges |
| Frame Loss | Loss in motor frame |
| End Cap Loss | Loss in end caps |
| Terminal Box Loss | Loss in terminal box |
| Encoder Loss | Loss in encoder (if present) |
| Resolver Loss | Loss in resolver (if present) |

---

## Cooling System Types

### End Space
Air-filled end space with natural or forced convection.

```python
mc.set_variable("EndSpace_Coefficient", 50)    # W/m²K
mc.set_variable("EndSpace_Air_Velocity", 5)    # m/s
```

### Ventilated
Forced air ventilation through motor.

```python
mc.set_variable("Ventilation_Flow_Rate", 0.05)  # m³/s
mc.set_variable("Ventilation_Air_Temp", 40)     # °C
```

### Housing Water Jacket
Coolant channels in motor housing.

```python
mc.set_variable("WJ_Fluid_Volume_Flow_Rate", 10)  # L/min
mc.set_variable("WJ_Fluid_Inlet_Temperature", 65)  # °C
mc.set_variable("WJ_Type", 1)                       # 1=Housing
```

### Shaft Spiral
Helical channel in shaft for coolant flow.

```python
mc.set_variable("ShaftSpiral_Flow_Rate", 5)      # L/min
mc.set_variable("ShaftSpiral_Inlet_Temp", 65)    # °C
```

### Wet Rotor
Direct coolant contact with rotor surface.

```python
mc.set_variable("WetRotor_Flow_Rate", 8)         # L/min
mc.set_variable("WetRotor_Coolant_Temp", 60)     # °C
```

### Spray Cooling
Direct spray on end windings.

```python
mc.set_variable("SprayCooling_Flow_Rate", 3)     # L/min
mc.set_variable("SprayCooling_Droplet_Size", 100) # μm
mc.set_variable("SprayCooling_Velocity", 10)      # m/s
```

---

## Twin Builder Import Workflow

1. Open Twin Builder in Ansys Electronics Desktop
2. Create new schematic
3. Use **File → Import → MotorCAD Thermal ROM**
4. Select any of the `.nmf`, `.rmf`, `.cmf`, `.pmf`, or `.tmf` files
5. The ROM component is automatically created with all thermal nodes
6. Connect to drive electronics and mechanical load models
7. Run coupled electro-thermal simulation

---

## Matrix File Structure

### Node Matrix File (.nmf)
```
NodeID, Name, Type, X, Y, Z
1, Winding_Avg, Winding, 0.0, 0.0, 0.1
2, Stator_Core, Core, 0.0, 0.0, 0.05
3, Housing, Housing, 0.175, 0.0, 0.0
...
```

### Resistance Matrix File (.rmf)
```
Node1, Node2, Resistance
1, 2, 0.05
2, 3, 0.12
...
```

### Capacitance Matrix File (.cmf)
```
NodeID, Capacitance
1, 50.0
2, 120.0
...
```

### Power Matrix File (.pmf)
```
NodeID, Power_Source
1, 850.0
2, 320.0
...
```

### Temperature Matrix File (.tmf)
```
NodeID, Initial_Temperature
1, 40.0
2, 45.0
...
```

---

## Complete Workflow

```
1. Run EMag or Lab to get loss values
2. Run steady-state thermal analysis in MotorCAD
3. Verify thermal results are reasonable
4. Call generateTwinData()
5. Call getNodeData() to inspect network
6. Call generateCoolingSystemNetwork()
7. Call generateSamples()
8. Call generateLossDistribution()
9. Call exportTwinBuilderData() to disk
10. Import .nmf/.rmf/.cmf/.pmf/.tmf into Twin Builder
11. Connect ROM to system simulation
```

---

## Tips and Best Practices

- **Loss accuracy:** Ensure EMag/Lab loss values are accurate before export
- **Cooling configuration:** Set up all cooling systems before generating ROM
- **Node resolution:** Higher `SatModelPoints_MotorLAB` improves thermal node resolution
- **Validation:** Compare MotorCAD thermal results with Twin Builder simulation
- **Speed dependency:** Export multiple operating points if motor operates across wide speed range
- **File management:** Keep all five matrix files together in the same directory

---

## Related Pages

- [[pymotorcad-thermal-example]] — Thermal analysis workflow
- [[pymotorcad-thermal-steady-state]] — Steady-state thermal API
- [[pymotorcad-thermal-transient]] — Transient thermal API
- [[pymotorcad-emag-twin-builder]] — EMag model Twin Builder export
- [[pymotorcad-calculations-api]] — Calculation methods reference
- [[pymotorcad-set-variable]] — Variable setting API
- [[pymotorcad-get-variable]] — Variable reading API
