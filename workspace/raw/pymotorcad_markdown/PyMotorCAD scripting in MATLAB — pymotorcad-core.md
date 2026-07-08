## PyMotorCAD scripting in MATLAB

PyMotorCAD is available to use in MATLAB in the same way as other Python modules. If the ansys.motorcad.core package is installed for a version of Python, this version of Python can be used in MATLAB and the PyMotorCAD API can be called. This means that MATLAB scripts can make use of PyMotorCAD for controlling Motor-CAD and automation.

## <span id="page-0-0"></span>Using Python modules in MATLAB [#](#page-0-0)

Python modules can be called in MATLAB as long as Python is installed on the system.

Please refer to the Mathworks website for detailed information on [configuring](https://uk.mathworks.com/help/matlab/matlab_external/install-supported-python-implementation.html) your system to use [Python](https://uk.mathworks.com/help/matlab/matlab_external/install-supported-python-implementation.html) and [accessing](https://uk.mathworks.com/help/matlab/matlab_external/create-object-from-python-class.html) Python Modules from MATLAB.

By default, MATLAB selects the version of Python based on the system path. To view the system path in MATLAB, use the getenv('path') command. To see which version of Python MATLAB is using, call the pyenv function in MATLAB.

```
pe = pyenv;
pe.Version
```

For example, if version Python version 3.10 is installed and added to path, MATLAB outputs:

```
ans =
"3.10"
```

## Using PyMotorCAD in MATLAB

If the Python version that MATLAB is using has the ansys.motorcad.core package installed, PyMotorCAD is available to use in MATLAB. See [Getting](https://motorcad.docs.pyansys.com/version/stable/getting_started/index.html#ref-getting-started) started for details on installing ansys.motorcad.core .

To import the ansys.motorcad.core module as pymotorcad for use in scripts, use:

```
pymotorcad = py.importlib.import_module('ansys.motorcad.core');
```

Then [MotorCAD](https://motorcad.docs.pyansys.com/version/stable/methods/MotorCAD_object.html#ref-motorcad-object) API commands can be used in MATLAB in the same way as in Python. To start and connect to a Motor-CAD instance, access the MotorCAD() object:

```
mcApp = pymotorcad.MotorCAD();
```

## Example: Motor-CAD E-magnetic scripting in MATLAB

An example of a MATLAB script using PyMotorCAD to change the motor geometry and materials, run magnetic calculations and extract results for further analysis is presented. This example is also included in the Automation tutorial supplied with Motor-CAD.

```
% Use pymotorcad as an alias to access functionality in ansys.motorcad.core
pymotorcad = py.importlib.import_module('ansys.motorcad.core');
% Launch an instance of Motor-CAD
mcApp = pymotorcad.MotorCAD();
% Turn off popups
mcApp.set_variable('MessageDisplayState', 2)
% Change tab to scripting so that there are no conflicts when changing
% variables
mcApp.show_magnetic_context()
mcApp.display_screen('scripting')
% change to default BPM motor
mcApp.set_variable('Motor_Type', 0)
% Geometry changes
mcApp.set_variable('Slot_Number', 24)
mcApp.set_variable('Tooth_Width', 6)
mcApp.set_variable('Magnet_Thickness', 4.5)
% Coil changes
mcApp.set_variable('MagPhases',3);
mcApp.set_variable('ParallelPaths',1);
mcApp.set_variable('WindingLayers',2);
mcApp.set_variable('MagWindingType',1);
mcApp.set_variable('MagPathType',1);
mcApp.set_winding_coil(int64(2), int64(1), int64(3), int64(4), 'b', int64(18), 'a', in
% Material changes
mcApp.set_component_material('Stator Lam (Back Iron)', 'M250-35A')
mcApp.set_component_material('Rotor Lam (Back Iron)', 'M250-35A')
% Set calculation preferences
PointsPerCycle = 30;
NumberCycles = 1;
mcApp.set_variable('TorquePointsPerCycle', PointsPerCycle);
mcApp.set_variable('TorqueNumberCycles', NumberCycles);
% Turn off performance tests
mcApp.set_variable('BackEMFCalculation', false);
mcApp.set_variable('CoggingTorqueCalculation', false);
mcApp.set_variable('ElectromagneticForcesCalc_OC', false);
mcApp.set_variable('TorqueSpeedCalculation', false);
mcApp.set_variable('DemagnetizationCalc', false);
mcApp.set_variable('ElectromagneticForcesCalc_Load', false);
mcApp.set_variable('InductanceCalc', false);
mcApp.set_variable('BPMShortCircuitCalc', false);
% Enable transient torque
mcApp.set_variable('TorqueCalculation', true);
% Emangetic calculation settings
mcApp.set_variable('Shaft_Speed_[RPM]', 1000);
mcApp.set_variable('CurrentDefinition', 0);
mcApp.set_variable('PeakCurrent', 3);
mcApp.set_variable('DCBusVoltage', 350);
mcApp.set_variable('PhaseAdvance', 45);
% Save file and calculate
mcApp.save_to_file('C:\ANSYS_Motor-CAD\2023_1_1\Motor-CAD Data\MATLAB_Tutorial\automat
mcApp.do_magnetic_calculation()
% data retrieval and export
mcApp.export_results('EMagnetic','C:\ANSYS_Motor-CAD\2023_1_1\Motor-CAD Data\MATLAB_Tut
ShaftTorque = mcApp.get_variable('ShaftTorque');
LineVoltage = mcApp.get_variable('PeakLineLineVoltage');
NumTorquePoints = (PointsPerCycle * NumberCycles) + 1;
for loop = 0:NumTorquePoints-1
```

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026