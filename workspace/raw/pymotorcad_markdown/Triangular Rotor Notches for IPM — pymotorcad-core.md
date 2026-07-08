![](_page_0_Picture_2.jpeg)

Note

Go to the [end](#page-6-0) to download the full example code.

## Triangular Rotor Notches for IPM

This script applies the adaptive templates functionality to create triangular rotor notches to improve NVH performance.

![](_page_0_Picture_7.jpeg)

### Note

For more information on the use of Adaptive Templates in Motor-CAD, and how to create, modify and debug Adaptive Templates Scripts, see [Motor-CAD](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) adaptive templates [scripting](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) in the User [guide.](https://motorcad.docs.pyansys.com/version/stable/user_guide/index.html#ref-user-guide)

![](_page_0_Picture_10.jpeg)

### Note

Adaptive Templates in Motor-CAD require v2024.1.2 (Motor-CAD 2024 R1 Update) or later and PyMotorCAD v0.4.1. To update PyMotorCAD in Motor-CAD, go to Scripting -> Settings -> PyMotorCAD updates and select 'Update to Latest Release'.

This script is designed to be run from Motor-CAD template "e9". If no Motor-CAD file is open, the e9 template will be loaded.

This script uses the following adaptive parameters:

- Notch Angle (-4)
- Notch Sweep (5)
- Notch Depth (1)
- Notches per Pole (2)

If these parameters are not already set up in the Motor-CAD file, the parameters will be automatically set, with the default values shown in brackets.

To set an adaptive geometry for a Motor-CAD file, a script must be loaded in to the Adaptive Templates tab (Geometry -> Editor -> Adaptive Templates) in Motor-CAD and run. When the option 'Geometry

Templates Type' is set to 'Adaptive', this script is automatically run repeatedly to keep the Adaptive Geometry set in Motor-CAD.

![](_page_1_Figure_3.jpeg)

This Python script can also be executed externally. When executed externally, a Motor-CAD instance will be launched and a file based on the "e9" template will be saved to a temporary folder. This script will be loaded into the Adaptive Templates tab.

### Perform Required imports

Import the pymotorcad package to access Motor-CAD. Import the triangular\_notch function to create the notch geometry region with Adaptive Templates geometry. Import the os , shutil , sys , and tempfile packages to open and save a temporary MOT file if none is open.

```
import os
import shutil
import sys
import tempfile
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import RegionType
from ansys.motorcad.core.geometry_shapes import triangular_notch
```

# Connect to Motor-CAD

If this script is loaded into the Adaptive Templates file in Motor-CAD, the current Motor-CAD instance is used.

If the script is run externally, these actions occur: a new Motor-CAD instance is opened, the e9 IPM motor template is loaded, and the file is saved to a temporary folder. To keep a new Motor-CAD instance open after executing the script, use the MotorCAD(keep\_instance\_open=True) option when opening the new instance. Alternatively, use the MotorCAD() method, which closes the Motor-CAD instance after the script is executed.

```
if pymotorcad.is_running_in_internal_scripting():
    # Use existing Motor-CAD instance if possible
    mc = pymotorcad.MotorCAD(open_new_instance=False)
else:
    mc = pymotorcad.MotorCAD(keep_instance_open=True)
    # Disable popup messages
    mc.set_variable("MessageDisplayState", 2)
    if not "PYMOTORCAD_DOCS_BUILD" in os.environ:
        mc.set_visible(True)
    mc.load_template("e9")
    # Open relevant file
    working_folder = os.path.join(tempfile.gettempdir(), "adaptive_library")
    try:
        shutil.rmtree(working_folder)
    except:
        pass
    os.mkdir(working_folder)
    mot_name = "BPMTriRotorNotches"
    mc.save_to_file(working_folder + "/" + mot_name + ".mot")
# Reset geometry to default
mc.reset_adaptive_geometry()
```

### Set Adaptive Parameters if required

Four Adaptive Parameters are required for this adaptive template. These are used to define the number of rotor notches to be added, their position and size.

If the Adaptive Parameters have already been set in the current Motor-CAD file, their current values will be used. Otherwise, the Adaptive Parameters will be defined and set to default values.

Use the set\_adaptive\_parameter\_default method to set the required parameters if undefined.

```
mc.set_adaptive_parameter_default("Notch Angle", -4)
mc.set_adaptive_parameter_default("Notch Sweep", 5)
mc.set_adaptive_parameter_default("Notch Depth", 1)
mc.set_adaptive_parameter_default("Notches per Pole", 2)
```

### Get required parameters and objects

Get the Adaptive Parameters specified in Motor-CAD, and their values

```
notch_angle = mc.get_adaptive_parameter_value("notch angle")
notch_angular_width = mc.get_adaptive_parameter_value("notch sweep")
notch_depth = mc.get_adaptive_parameter_value("notch depth")
number_notches = int(mc.get_adaptive_parameter_value("notches per pole"))
```

Get the standard template rotor region from Motor-CAD. Calculate the rotor radius and define the rotor centre coordinates.

```
rotor_region = mc.get_region("Rotor")
rotor_radius = mc.get_variable("RotorDiameter") / 2
duplication_angle = 360 / rotor_region.duplications
```

Add an if statement to account for the case when a notch crosses the symmetry boundary. This resets notch\_angle to half the notch\_angular\_width away from the boundary.

```
if notch_angle > (duplication_angle / (2 * number_notches)) - (notch_angular_width / 2
    # Limit so notch does not cross the symmetry boundary
    notch_angle = (duplication_angle / (2 * number_notches)) - notch_angular_width / 2
    mc.show_message("Adaptive Parameter: 'notch angle' not valid, reset to " + str(not
    mc.set_adaptive_parameter_value("notch angle", notch_angle)
```

Add an if statement to account for the case when notches overlap at the centre of the pole. This resets notch\_angle to:

- Half the notch\_angular\_width away from the pole centre when there are an even number of notches
- The full notch\_angular\_width away from the pole centre when there are an odd number of notches

```
if number_notches % 2 == 0:
    x = -1
else:
    x = -2
if notch_angle < -((duplication_angle / (2 * number_notches)) - (notch_angular_width /
    # Limit so notches do not overlap at centre of pole
    notch_angle = x * ((duplication_angle / (2 * number_notches)) - notch_angular_widt
    mc.show_message("Adaptive Parameter: 'notch angle' not valid, reset to " + str(not
    mc.set_adaptive_parameter_value("notch angle", notch_angle)
```

### Create the Adaptive Templates geometry

For each notch to be added:

- Calculate the angular position of the notch in mechanical degrees
- Apply the offset angle. For notches on the left side of the pole, the position is shifted by + notch\_angle mechanical degrees. For notches on the right side of the pole, the position is shifted by - notch\_angle mechanical degrees.
- Create the notch Region using the triangular\_notch() function, imported from ansys.motorcad.core.geometry\_shapes . The arguments for the function are:
  - rotor\_radius
  - notch\_angular\_width
  - notch\_centre\_angle
  - notch\_depth
- Define the properties for the notch region
  - name
  - colour
  - duplication angle
  - material
- set the notch's parent to the rotor region. This will allow Motor-CAD to treat the notch as a subregion of the rotor and handle subtractions automatically.
- If the notch is closed, set the region in Motor-CAD.

```
for notch_loop in range(0, number_notches):
    notch_name = "Rotor_Notch_" + str(notch_loop + 1)
    # angular position of notch
    notch_centre_angle = ((2 * notch_loop) + 1) * (duplication_angle / (2 * number_not
    # Offset angle by notch_angle
    if notch_centre_angle < duplication_angle / 2:
        notch_centre_angle = notch_centre_angle - notch_angle
    if notch_centre_angle > duplication_angle / 2:
        notch_centre_angle = notch_centre_angle + notch_angle
    # generate a triangular notch region
    notch = triangular_notch(
        rotor_radius,
        notch_angular_width,
        notch_centre_angle,
        notch_depth,
        region_type=RegionType.rotor_pocket,
    )
    # notch properties
    notch.name = notch_name
    notch.colour = (255, 255, 255)
    notch.duplications = rotor_region.duplications
    notch.material = "Air"
    notch.parent = rotor_region
    if notch.is_closed():
        mc.set_region(notch)
```

![](_page_5_Picture_3.jpeg)

## Load in Adaptive Templates script if required

When this script is run externally, the script executes the following:

- Set Geometry type to Adaptive.
- Load the script into the Adaptive Templates tab.
- Go to the Geometry -> Radial tab to run the Adaptive Templates script and display the new geometry.

![](_page_6_Picture_7.jpeg)

Note

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

<span id="page-6-0"></span>Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026