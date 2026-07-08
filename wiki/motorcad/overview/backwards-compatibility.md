---
type: motorcad_overview
title: "Backwards Compatibility with Old Scripts"
description: "Converting ActiveX scripts to PyMotorCAD"
confidence: Verified
source_files: ["Backwards compatibility with old scripts — pymotorcad-core.md"]
---

# Backwards Compatibility with Old Scripts

## Quick Migration

Replace the ActiveX connection:
```python
# Old (ActiveX)
import win32com.client
mcApp = win32com.client.Dispatch("MotorCAD.AppAutomation")

# New (PyMotorCAD)
import ansys.motorcad.core as pymotorcad
mcApp = pymotorcad.MotorCADCompatibility()
```

`MotorCADCompatibility()` turns off new PyMotorCAD features to ensure compatibility.

## Full Conversion

### Change function names to snake_case

```python
# Old
McApp.GetVariable()
# New
mcApp.get_variable()
```

### Remove success variable checking

```python
# Old (success returned as first tuple element)
success, VariableValue = mcApp.GetVariable("Not_A_Real_Var")

# New (raises MotorCADError on failure)
variable_value = mcApp.get_variable("Not_A_Real_Var")
```

### Use try/except for expected failures

```python
from ansys.motorcad.core import MotorCADError
try:
    x, y = mcApp.get_magnetic_graph_point("TorqueVW", i)
except MotorCADError:
    # End of graph reached
```

## Related Pages

- [[motorcad/api/motorcad-api]] — MotorCAD constructor
- [[motorcad/api/motorcad-compatibility-api]] — MotorCADCompatibility constructor
- [[motorcad/api/motorcad-errors]] — MotorCADError reference
