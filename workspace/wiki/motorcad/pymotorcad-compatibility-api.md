---
type: motorcad_api
title: PyMotorCAD Compatibility API
source: ansys-motorcad-core documentation
tags: [motorcad, pymotorcad, compatibility,activex, legacy, snake-case]
aliases: [MotorCADCompatibility, legacy ActiveX scripts]
---

# PyMotorCAD Compatibility API

## Overview

The `MotorCADCompatibility()` class provides a bridge for **legacy ActiveX-based Motor-CAD scripts**. It maps old CamelCase method and property names to the modern snake_case API.

## Usage

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCADCompatibility()
```

This returns a compatibility wrapper that accepts legacy naming conventions.

## Naming Convention Migration

### CamelCase (legacy) to snake_case (modern)

| Legacy (ActiveX) | Modern (PyMotorCAD) |
|-------------------|---------------------|
| `LoadFromFile()` | `load_from_file()` |
| `SaveToFile()` | `save_to_file()` |
| `GetVariable()` | `get_variable()` |
| `SetVariable()` | `set_variable()` |
| `DoMagneticCalculation()` | `do_magnetic_calculation()` |
| `DoSteadyStateAnalysis()` | `do_steady_state_analysis()` |
| `ShowMagneticContext()` | `show_magnetic_context()` |
| `ShowThermalContext()` | `show_thermal_context()` |
| `SetVisible()` | `set_visible()` |
| `DisplayScreen()` | `display_screen()` |
| `Quit()` | `quit()` |

### Property-style access

| Legacy | Modern |
|--------|--------|
| `mcApp.VariableName` | `mc.get_variable("VariableName")` |
| `mcApp.VariableName = value` | `mc.set_variable("VariableName", value)` |

## Example: Legacy Script Migration

### Before (ActiveX-style)

```python
mcApp = MotorCADCompatibility()
mcApp.LoadFromFile("D:\\models\\SRM_1.mot")
mcApp.SetVariable("Shaft_Speed_[RPM]", 3000)
mcApp.DoMagneticCalculation()
torque = mcApp.GetVariable("ShaftTorque")
print("Torque:", torque)
mcApp.Quit()
```

### After (Modern PyMotorCAD)

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\SRM_1.mot")
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.do_magnetic_calculation()
torque = mc.get_variable("ShaftTorque")
print(f"Torque: {torque}")
mc.quit()
```

## When to Use Compatibility API

- Migrating existing ActiveX scripts incrementally
- Running legacy scripts without rewriting
- Testing old workflows before full migration

For new development, always use the modern `MotorCAD()` constructor directly.

## Cross-References

- [[pymotorcad-motorcad-api]] — Modern constructor and parameters
- [[pymotorcad-general-api]] — Full method reference
- [[pymotorcad-getting-started]] — Installation and first steps
- [[pymotorcad-setup]] — Registration and naming conventions

## Tags

#motorcad #pymotorcad #compatibility #activex #legacy #migration #snake-case
