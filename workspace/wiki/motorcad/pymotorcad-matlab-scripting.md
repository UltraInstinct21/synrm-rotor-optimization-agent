---
type: motorcad_workflow
title: "Using PyMotorCAD from MATLAB"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - matlab
  - scripting
  - emag
  - integration
aliases:
  - "MotorCAD MATLAB integration"
  - "PyMotorCAD MATLAB"
---

# Using PyMotorCAD from MATLAB

## Overview

PyMotorCAD can be called directly from MATLAB via MATLAB's built-in Python interface. This allows motor design engineers to combine MATLAB's simulation, analysis, and visualization capabilities with Motor-CAD's electromagnetic and thermal solvers.

Use cases include:

- Parameter sweeps with MATLAB post-processing
- Custom optimization loops in MATLAB
- Automating Motor-CAD EMag/Thermal calculations from MATLAB scripts
- Generating plots and reports from Motor-CAD results in MATLAB
- Integrating Motor-CAD into larger MATLAB-based simulation architectures

---

## Prerequisites

- Motor-CAD installed with a valid license
- PyMotorCAD installed in a Python environment accessible to MATLAB
- MATLAB R2014b or later (Python interface support)
- Python 3.x registered with MATLAB (`pyenv` in MATLAB)

---

## Register Python Environment with MATLAB

Before using PyMotorCAD from MATLAB, ensure MATLAB can locate the correct Python interpreter:

```matlab
% Check which Python MATLAB is using
pyenv

% Set the Python executable if needed (e.g., a venv)
pyenv('Version', 'D:\SRM\Motor _CAD\.venv\Scripts\python.exe')
```

Verify PyMotorCAD is importable:

```matlab
py.importlib.import_module('ansys.motorcad.core');
disp('PyMotorCAD loaded successfully');
```

---

## Importing PyMotorCAD in MATLAB

The standard import pattern is:

```matlab
mc = py.ansys.motorcad.core.MotorCAD();
```

This is equivalent to the Python constructor:

```python
mc = ansys.motorcad.core.MotorCAD()
```

---

## Complete MATLAB EMag Example

The following script creates a Motor-CAD instance, configures geometry, material, and operating point, runs an electromagnetic calculation, and retrieves key results.

```matlab
%% PyMotorCAD EMag Example — MATLAB
% Ensure Python environment is configured
pe = pyenv;
if pe.Status ~= "Loaded"
    pyenv('Version', 'D:\SRM\Motor _CAD\.venv\Scripts\python.exe');
end

%% Create Motor-CAD instance
mc = py.ansys.motorcad.core.MotorCAD();
disp('Motor-CAD instance created');

%% Load an existing model
mc.load_from_file('D:\SRM\Motor _CAD\SRM_1.mot');
disp('Model loaded');

%% Switch to EMag context
mc.show_magnetic_context();

%% Set geometry parameters
mc.set_variable('Stator_Lam_Dia', 340);        % mm
mc.set_variable('Stator_bore', 215);           % mm
mc.set_variable('Airgap', 0.5);                % mm
mc.set_variable('Stator_Lam_Length', 180);     % mm
mc.set_variable('Pole_Number', 4);
mc.set_variable('Slot_Number', 48);
mc.set_variable('Shaft_Dia', 80);              % mm

%% Set rotor barrier geometry
mc.set_variable('L1_Diameter', 100);
mc.set_variable('L1_Bridge_Thickness', 4);
mc.set_variable('L1_Web_Thickness', 17);
mc.set_variable('L1_Outer_Angle_Offset', -10);
mc.set_variable('L1_Outer_Thickness', 4);
mc.set_variable('L1_Inner_Thickness', 5);
mc.set_variable('L2_Diameter', 130);
mc.set_variable('L2_Bridge_Thickness', 5);
mc.set_variable('L2_Web_Thickness', 50);
mc.set_variable('L3_Diameter', 160);
mc.set_variable('L3_Bridge_Thickness', 5);
mc.set_variable('L3_Web_Thickness', 82);

%% Set materials
mc.set_component_material('Stator Core', 'M19_29Ga');
mc.set_component_material('Rotor Core', 'M19_29Ga');
mc.set_component_material('Shaft', 'Steel');

%% Set winding parameters
mc.set_variable('WireDiameter', 1.715);        % mm
mc.set_variable('Copper_Slot_Fill', 0.4);

%% Set operating point
mc.set_variable('Shaft_Speed_[RPM]', 3000);
mc.set_variable('PhaseAdvance', 45);           % electrical degrees
mc.set_variable('TorquePointsPerCycle', 30);
mc.set_variable('TorqueNumberCycles', 1);

%% Run EMag calculation
mc.do_magnetic_calculation();
disp('EMag calculation complete');

%% Retrieve results
torque = mc.get_variable('ShaftTorque');
input_power = mc.get_variable('InputPower');
voltage = mc.get_variable('PeakLineLineVoltage');
stator_cu_loss = mc.get_variable('StatorCopperLossAC');
stator_fe_loss = mc.get_variable('StatorIronLoss_Total');
winding_temp = mc.get_variable('T_Winding_Average');

%% Display results
fprintf('Shaft Torque: %.2f Nm\n', double(torque));
fprintf('Input Power: %.2f W\n', double(input_power));
fprintf('Peak Line-Line Voltage: %.2f V\n', double(voltage));
fprintf('Stator Copper Loss (AC): %.2f W\n', double(stator_cu_loss));
fprintf('Stator Iron Loss (Total): %.2f W\n', double(stator_fe_loss));
fprintf('Winding Temperature: %.2f °C\n', double(winding_temp));

%% Calculate efficiency
shaft_power = double(torque) * 3000 * 2 * pi / 60;  % W
efficiency = shaft_power / double(input_power) * 100;
fprintf('Efficiency: %.2f%%\n', efficiency);

%% Save modified model
mc.save_to_file('D:\SRM\Motor _CAD\matlab_modified.mot');
disp('Model saved');

%% Disconnect
mc.quit();
disp('Motor-CAD closed');
```

---

## Key MATLAB-Python Mapping

| Python | MATLAB Equivalent |
|---|---|
| `import ansys.motorcad.core` | `py.ansys.motorcd.core` |
| `mc = MotorCAD()` | `mc = py.ansys.motorcd.core.MotorCAD()` |
| `mc.set_variable('name', value)` | `mc.set_variable('name', value)` |
| `mc.get_variable('name')` | `double(mc.get_variable('name'))` |
| `mc.do_magnetic_calculation()` | `mc.do_magnetic_calculation()` |
| `mc.load_from_file(path)` | `mc.load_from_file(path)` |
| `mc.save_to_file(path)` | `mc.save_to_file(path)` |

> **Note:** MATLAB returns Python numeric types. Use `double()` to convert to MATLAB native doubles for arithmetic and display.

---

## Retrieving String Variables

Some Motor-CAD variables return Python strings. In MATLAB:

```matlab
rotor_type = char(mc.get_variable('RotorType_Str'));
disp(rotor_type);
```

---

## Error Handling in MATLAB

Wrap Motor-CAD calls in try-catch blocks:

```matlab
try
    mc.do_magnetic_calculation();
catch ME
    fprintf('Motor-CAD error: %s\n', char(ME.message));
end
```

---

## Common Pitfalls

### Python version mismatch
MATLAB must use the same Python version where PyMotorCAD is installed. Use `pyenv` to verify and configure.

### Numeric type conversion
Motor-CAD API calls return Python floats. Always wrap results with `double()` before MATLAB arithmetic.

### Motor-CAD instance lifecycle
Each `py.ansys.motorcd.core.MotorCAD()` call launches a new Motor-CAD process. Always call `mc.quit()` when finished, or use persistent variables in scripts that run multiple calculations.

### Model file paths
Use absolute paths for `load_from_file` and `save_to_file`. Relative paths resolve against Motor-CAD's working directory, not MATLAB's.

---

## Related Pages

- [[pymotorcad-emag-example]] — Python EMag workflow example
- [[pymotorcad-getting-started]] — First steps with PyMotorCAD
- [[pymotorcad-virtual-environment]] — Configure custom Python venv for Motor-CAD
- [[motorcad_api/do_magnetic_calculation]] — EMag calculation API
- [[motorcad_api/set_variable]] — Setting Motor-CAD variables
- [[motorcad_api/get_variable]] — Reading Motor-CAD variables
