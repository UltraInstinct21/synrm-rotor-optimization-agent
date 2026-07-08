---
type: motorcad_overview
title: "PyMotorCAD Scripting in MATLAB"
description: "Using PyMotorCAD from MATLAB scripts"
confidence: Verified
source_files: ["PyMotorCAD scripting in MATLAB — pymotorcad-core.md"]
---

# PyMotorCAD Scripting in MATLAB

PyMotorCAD can be called from MATLAB as long as Python is installed on the system with `ansys.motorcad.core` installed.

## Check Python Version in MATLAB

```matlab
pe = pyenv;
pe.Version
```

## Import PyMotorCAD

```matlab
pymotorcad = py.importlib.import_module('ansys.motorcad.core');
mcApp = pymotorcad.MotorCAD();
```

## Example: E-Magnetic Scripting

```matlab
pymotorcad = py.importlib.import_module('ansys.motorcad.core');
mcApp = pymotorcad.MotorCAD();
mcApp.set_variable('MessageDisplayState', 2)
mcApp.show_magnetic_context()
mcApp.display_screen('scripting')
% Geometry changes
mcApp.set_variable('Slot_Number', 24)
mcApp.set_variable('Tooth_Width', 6)
% ... calculation settings ...
mcApp.do_magnetic_calculation()
ShaftTorque = mcApp.get_variable('ShaftTorque');
```

## Related Pages

- [[motorcad/overview/getting-started]] — Python installation
- [[motorcad/api/motorcad-api]] — MotorCAD constructor
