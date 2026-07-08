---
type: motorcad_api
title: PyMotorCAD - Error Handling
source: PyMotorCAD Documentation
tags:
  - motorcad
  - pymotorcad
  - errors
  - exceptions
  - error-handling
---

# PyMotorCAD - Error Handling

## Overview

PyMotorCAD provides the `MotorCADError` exception class for handling errors from Motor-CAD operations.

## MotorCADError Exception

### Import

```python
from ansys.motorcad.core.rpc_client_core import MotorCADError
```

### Basic Usage

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.rpc_client_core import MotorCADError

mc = pymotorcad.MotorCAD()

try:
    mc.load_from_file("nonexistent.mot")
except MotorCADError as e:
    print(f"Motor-CAD error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Common Error Scenarios

### File Operations

```python
try:
    mc.load_from_file(r"D:\models\missing.mot")
except MotorCADError as e:
    print(f"Failed to load model: {e}")
    # Handle missing file or invalid format
```

### Variable Operations

```python
try:
    mc.set_variable("InvalidVariableName", 100)
except MotorCADError as e:
    print(f"Variable error: {e}")
    # Use discover_variables() to find correct name
```

### Calculation Failures

```python
try:
    mc.do_magnetic_calculation()
except MotorCADError as e:
    print(f"Calculation failed: {e}")
    # Check prerequisites and model validity
```

## Comprehensive Error Handling Pattern

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.rpc_client_core import MotorCADError

def safe_motorcad_operation():
    mc = None
    try:
        # Connect to Motor-CAD
        mc = pymotorcad.MotorCAD()
        mc.set_variable("MessageDisplayState", 2)
        
        # Load model
        mc.load_from_file(r"D:\SRM\Motor _CAD\SRM_1.mot")
        
        # Set parameters
        mc.show_magnetic_context()
        mc.set_variable("Shaft_Speed_[RPM]", 3000)
        
        # Run calculation
        mc.do_magnetic_calculation()
        
        # Read results
        torque = mc.get_variable("ShaftTorque")
        print(f"Torque: {torque} Nm")
        
    except MotorCADError as e:
        print(f"Motor-CAD specific error: {e}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if mc:
            try:
                mc.quit()
            except:
                pass

safe_motorcad_operation()
```

## Error Information

MotorCADError exceptions typically contain:
- Error message from Motor-CAD
- Operation that failed
- Motor-CAD state at time of error

## Best Practices

1. **Always wrap Motor-CAD calls in try/except blocks**
2. **Use MotorCADError for Motor-CAD specific failures**
3. **Log error details for debugging**
4. **Clean up Motor-CAD instances in finally blocks**
5. **Check variable names before setting/getting**

## Related Pages

- [[pymotorcad-troubleshooting]] - Common issues and solutions
- [[pymotorcad-backwards-compatibility]] - Migration from ActiveX

## Tags

#motorcad #pymotorcad #errors #exceptions #error-handling #try-except