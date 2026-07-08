![](_page_0_Picture_2.jpeg)

Note

Go to the [end](#page-4-0) to download the full example code.

# Motor-CAD Lab model example script

This example provides a Motor-CAD Lab model script.

#### Set up example

Setting up this example consists of performing imports, launching Motor-CAD, disabling all popup messages from Motor-CAD, and opening the file for the lab model.

Perform required imports

```
import os
import matplotlib.pyplot as plt
from scipy import io
import ansys.motorcad.core as pymotorcad
if "QT_API" in os.environ:
    os.environ["QT_API"] = "pyqt"
```

### Launch Motor-CAD

```
print("Starting initialization.")
mcad = pymotorcad.MotorCAD()
```

Out:

Starting initialization.

#### Disable popup messages

```
mcad.set_variable("MessageDisplayState", 2)
```

#### Open relevant file

Specify the working directory and open the relevant file for the lab model.

```
working_folder = os.getcwd()
mcad.load_template("e8")
mcad_name = "e8_mobility"
mcad.save_to_file(os.path.join(working_folder, mcad_name + ".mot"))
print("Initialization completed.")
```

Out:

Initialization completed.

### Build model

Set build options for the lab model.

```
mcad.set_variable("ModelType_MotorLAB", 1)
mcad.set_variable("SatModelPoints_MotorLAB", 0)
mcad.set_variable("LossModel_Lab", 0)
mcad.set_variable("ModelBuildSpeed_MotorLAB", 10000)
mcad.set_variable("MaxModelCurrent_MotorLAB", 480)
mcad.set_variable("BuildSatModel_MotorLAB", True)
```

Show the lab context.

```
mcad.set_motorlab_context()
```

Build the model.

```
mcad.clear_model_build_lab()
mcad.build_model_lab()
```

Change operating modes.

```
mcad.set_variable("OperatingMode_Lab", 0)
```

# Calculate e-magnetic performance

Set e-magnetic calculation options.

```
mcad.set_variable("EmagneticCalcType_Lab", 0)
mcad.set_variable("SpeedMax_MotorLAB", 10000)
mcad.set_variable("Speedinc_MotorLAB", 250)
mcad.set_variable("SpeedMin_MotorLAB", 500)
mcad.set_variable("Imax_MotorLAB", 480)
```

Calculate e-magnetic performance.

```
try:
    mcad.calculate_magnetic_lab()
    print("Magnetic calculation successfully completed.")
except pymotorcad.MotorCADError:
    print("Magnetic calculation failed.")
```

Out:

Magnetic calculation successfully completed.

Retrieve results.

```
data = io.loadmat(os.path.join(working_folder, mcad_name, "Lab", "MotorLAB_elecdata.ma
speed = data["Speed"]
shaft_torque = data["Shaft_Torque"]
shaft_power = data["Shaft_Power"]
```

### Plot results

Plot torque/speed curve results.

```
plt.figure(1)
plt.subplot(211)
plt.plot(speed, shaft_torque)
plt.xlabel("Speed")
plt.ylabel("Shaft Torque")
plt.subplot(212)
plt.plot(speed, shaft_power)
plt.xlabel("Speed")
plt.ylabel("Shaft Power")
plt.show(block=False)
plt.savefig(os.path.join(working_folder, "../Maximum Torque VS Speed Curve.png"))
```

![](_page_3_Figure_3.jpeg)

### Calculate operating point

Set operating point calculation options.

```
mcad.set_variable("OpPointSpec_MotorLAB", 1)
mcad.set_variable("StatorCurrentDemand_Lab", 480)
mcad.set_variable("SpeedDemand_MotorLAB", 4000)
mcad.set_variable("LabThermalCoupling", 0)
mcad.set_variable("LabMagneticCoupling", 0)
```

# Calculate operating point.

mcad.calculate\_operating\_point\_lab()

Retrieve results.

```
op_point_shaft_torque = mcad.get_variable("LabOpPoint_ShaftTorque")
op_point_efficiency = mcad.get_variable("LabOpPoint_Efficiency")
print("Operating Point Shaft Torque = ", op_point_shaft_torque)
print("Operating Point Efficiency = ", op_point_efficiency)
```

Out:

```
Operating Point Shaft Torque = 292.729198137905
Operating Point Efficiency = 96.9311076958813
```

# Exit Motor-CAD

Exit Motor-CAD.

```
mcad.quit()
print("Simulation completed.")
```

Out:

Simulation completed.

<span id="page-4-0"></span>© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026