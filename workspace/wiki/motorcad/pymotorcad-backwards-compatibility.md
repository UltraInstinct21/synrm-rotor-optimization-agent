---
type: motorcad_guide
title: PyMotorCAD - Backwards Compatibility (ActiveX Migration)
source: PyMotorCAD Documentation
tags:
  - motorcad
  - pymotorcad
  - backwards-compatibility
  - activex
  - migration
  - win32com
---

# PyMotorCAD - Backwards Compatibility

## Overview

PyMotorCAD provides compatibility with legacy ActiveX (win32com) code for migration purposes.

## Old Approach: ActiveX (win32com)

### Import and Connection

```python
import win32com.client

mc = win32com.client.Dispatch("MotorCAD.AppAutomation")
```

### Example Operations (Legacy)

```python
import win32com.client

mc = win32com.client.Dispatch("MotorCAD.AppAutomation")

# Set variable (CamelCase)
mc.SetVariable("Shaft_Speed_[RPM]", 3000)

# Get variable
torque = mc.GetVariable("ShaftTorque")

# Run calculation
mc.DoMagneticCalculation()
```

## New Approach: PyMotorCAD

### Import and Connection

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
```

### Example Operations (PyMotorCAD)

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Set variable (snake_case)
mc.set_variable("Shaft_Speed_[RPM]", 3000)

# Get variable
torque = mc.get_variable("ShaftTorque")

# Run calculation
mc.do_magnetic_calculation()
```

## Compatibility Layer

### MotorCADCompatibility Class

For existing ActiveX code, use the compatibility class:

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCADCompatibility()

# ActiveX-style method calls still work
mc.SetVariable("Shaft_Speed_[RPM]", 3000)
torque = mc.GetVariable("ShaftTorque")
```

## Key Changes

### Method Naming Convention

| ActiveX (CamelCase) | PyMotorCAD (snake_case) |
|---------------------|------------------------|
| `SetVariable()` | `set_variable()` |
| `GetVariable()` | `get_variable()` |
| `DoMagneticCalculation()` | `do_magnetic_calculation()` |
| `LoadFromFile()` | `load_from_file()` |
| `SaveToFile()` | `save_to_file()` |
| `ShowMagneticContext()` | `show_magnetic_context()` |
| `ShowThermalContext()` | `show_thermal_context()` |
| `DisplayScreen()` | `display_screen()` |

### Error Handling

**ActiveX:**
```python
try:
    mc.SetVariable("Invalid", 100)
except Exception as e:
    print(f"Error: {e}")
```

**PyMotorCAD:**
```python
from ansys.motorcad.core.rpc_client_core import MotorCADError

try:
    mc.set_variable("Invalid", 100)
except MotorCADError as e:
    print(f"Motor-CAD error: {e}")
```

### Communication Protocol

| Aspect | ActiveX | PyMotorCAD |
|--------|---------|------------|
| Protocol | COM/ActiveX | JSON-RPC |
| Platform | Windows only | Cross-platform |
| Error handling | Generic exceptions | MotorCADError |
| Method naming | CamelCase | snake_case |

## Migration Checklist

1. **Update imports**
   ```python
   # Old
   import win32com.client
   mc = win32com.client.Dispatch("MotorCAD.AppAutomation")
   
   # New
   import ansys.motorcad.core as pymotorcad
   mc = pymotorcad.MotorCAD()
   ```

2. **Convert method names to snake_case**

3. **Replace generic exceptions with MotorCADError**

4. **Test all variable names** (should remain unchanged)

5. **Update path handling** (use raw strings for Windows paths)

## Related Pages

- [[pymotorcad-compatibility-api]] - Compatibility API reference
- [[pymotorcad-errors]] - MotorCADError exception handling

## Tags

#motorcad #pymotorcad #backwards-compatibility #activex #migration #win32com #compatibility