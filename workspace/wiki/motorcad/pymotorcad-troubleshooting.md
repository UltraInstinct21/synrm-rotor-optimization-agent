---
type: motorcad_guide
title: PyMotorCAD - Troubleshooting
source: PyMotorCAD Documentation
tags:
  - motorcad
  - pymotorcad
  - troubleshooting
  - errors
  - debugging
---

# PyMotorCAD - Troubleshooting

## Overview

Common issues encountered when using PyMotorCAD and their solutions.

## Issue 1: UI Not Updated After Variable Changes

### Symptom
Motor-CAD GUI does not reflect variable changes made through PyMotorCAD.

### Solution
Call `display_screen("scripting")` before making variable changes to force UI refresh.

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Show scripting tab to force UI update
mc.display_screen("scripting")

# Now set variables
mc.set_variable("Shaft_Speed_[RPM]", 3000)
```

**Why this works:** Motor-CAD UI updates are tied to screen display calls. The scripting tab must be active for Python-driven changes to be reflected.

## Issue 2: Popup Dialogs Blocking Automation

### Symptom
Motor-CAD displays popup dialogs that block script execution.

### Solution
Set `MessageDisplayState` to suppress popups.

```python
mc.set_variable("MessageDisplayState", 2)  # Suppress all popups
```

**MessageDisplayState values:**
| Value | Behavior |
|-------|----------|
| 0 | Show all messages (default) |
| 1 | Show errors only |
| 2 | Suppress all messages |

## Issue 3: Retrieving Motor-CAD Messages

### Symptom
Need to check Motor-CAD status or error messages after operations.

### Solution
Use `get_messages()` to retrieve recent messages.

```python
messages = mc.get_messages(num_messages=10)
for msg in messages:
    print(msg)
```

**Parameters:**
- `num_messages`: Number of recent messages to retrieve

**Returns:** List of message strings from Motor-CAD.

## Issue 4: Wrong Motor-CAD Version

### Symptom
Registration errors or feature incompatibility.

### Solution
Verify Motor-CAD version through registration form or:

```python
# Check Motor-CAD version (method may vary)
version = mc.get_variable("Version")
print(f"Motor-CAD version: {version}")
```

**Common version issues:**
- API methods may differ between versions
- Some features require specific Motor-CAD editions
- License compatibility must be verified

## Issue 5: Model File Not Found

### Symptom
`load_from_file()` fails with file not found error.

### Solution
Verify file path and use raw strings for Windows paths.

```python
# Correct path handling
model_path = r"D:\SRM\Motor _CAD\SRM_1.mot"
mc.load_from_file(model_path)
```

## Issue 6: Variable Name Errors

### Symptom
`set_variable()` or `get_variable()` fails with invalid variable name.

### Solution
Use `discover_variables()` to find correct variable names.

```python
def discover_variables(mc, keyword):
    all_vars = mc.get_variable_names()
    matches = [v for v in all_vars if keyword.lower() in v.lower()]
    print(f"Matches for '{keyword}': {matches}")
    return matches

# Find torque-related variables
discover_variables(mc, "torque")
```

## Issue 7: Calculation Not Producing Results

### Symptom
After `do_magnetic_calculation()`, result variables are empty or zero.

### Solution
Verify context and prerequisites.

```python
# Ensure correct context
mc.show_magnetic_context()

# Set required variables
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)

# Run calculation
mc.do_magnetic_calculation()

# Read results immediately
torque = mc.get_variable("ShaftTorque")
```

## Issue 8: PyMotorCAD Import Error

### Symptom
`ImportError: No module named 'ansys.motorcad.core'`

### Solution
Install PyMotorCAD properly.

```bash
pip install ansys-motorcad-core
```

Verify installation:

```python
import ansys.motorcad.core as pymotorcad
print("PyMotorCAD imported successfully")
```

## Related Pages

- [[pymotorcad-errors]] - MotorCADError exception handling
- [[pymotorcad-getting-started]] - Initial setup guide

## Tags

#motorcad #pymotorcad #troubleshooting #debugging #errors #common-issues