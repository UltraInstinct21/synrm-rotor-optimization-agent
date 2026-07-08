![](_page_0_Picture_2.jpeg)

### Note

Go to the [end](#page-4-0) to download the full example code.

## Triangular Stator Notches

Adaptive Template script to create triangular stator notches to improve NVH performance.

![](_page_0_Picture_7.jpeg)

### Note

For more information on the use of Adaptive Templates in Motor-CAD, and how to create, modify and debug Adaptive Templates Scripts, see [Motor-CAD](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) adaptive templates [scripting](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) in the User [guide.](https://motorcad.docs.pyansys.com/version/stable/user_guide/index.html#ref-user-guide)

![](_page_0_Picture_10.jpeg)

### Note

Adaptive Templates in Motor-CAD require v2024.1.2 (Motor-CAD 2024 R1 Update) or later and PyMotorCAD v0.4.1. To update PyMotorCAD in Motor-CAD, go to Scripting -> Settings -> PyMotorCAD updates and select 'Update to Latest Release'.

This script is designed to be run from Motor-CAD template "e10". If no Motor-CAD file is open, the e10 template will be loaded.

This script uses the following adaptive parameters:

- Notch Sweep (2)
- Notch Depth (1)

If these parameters are not already set up in the Motor-CAD file, the parameters will be automatically set, with the default values shown in brackets.

To set an adaptive geometry for a Motor-CAD file, a script must be loaded in to the Adaptive Templates tab (Geometry -> Editor -> Adaptive Templates) in Motor-CAD and run. When the option 'Geometry Templates Type' is set to 'Adaptive', this script is automatically run repeatedly to keep the Adaptive Geometry set in Motor-CAD.

This Python script can also be executed externally. When executed externally, a Motor-CAD instance will be launched and a file based on the "e10" template will be saved to a temporary folder. This script will be loaded into the Adaptive Templates tab.

```
import math
import os
import shutil
import sys
import tempfile
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Arc, Coordinate, Line, Region, RegionType, rt_
```

### Perform Required imports

Import pymotorcad to access Motor-CAD. Import os, tempfile and shutil to open and save a temporary .mot file if none is open.

# Connect to Motor-CAD

If this script is loaded into the Adaptive Templates file in Motor-CAD, the current Motor-CAD instance is used.

If the script is run externally, these actions occur: a new Motor-CAD instance is opened, the e10 IPM motor template is loaded and the file is saved to a temporary folder. To keep a new Motor-CAD instance open after executing the script, use the MotorCAD(keep\_instance\_open=True) option when opening the new instance. Alternatively, use the MotorCAD() method, which closes the Motor-CAD instance after the script is executed.

```
if pymotorcad.is_running_in_internal_scripting():
    # Use existing Motor-CAD instance if possible
    mc = pymotorcad.MotorCAD(open_new_instance=False)
else:
    mc = pymotorcad.MotorCAD(keep_instance_open=True)
    # Disable popup messages
    mc.set_variable("MessageDisplayState", 2)
    mc.set_visible(True)
    mc.load_template("e10")
    # Open relevant file
    working_folder = os.path.join(tempfile.gettempdir(), "adaptive_library")
    try:
        shutil.rmtree(working_folder)
    except:
        pass
    os.mkdir(working_folder)
    mot_name = "BPMTriStatorNotches"
    mc.save_to_file(working_folder + "/" + mot_name + ".mot")
# Reset geometry to default
mc.reset_adaptive_geometry()
```

### Set Adaptive Parameters if required

Two Adaptive Parameters are required for this adaptive template. These are used to define the size of the stator notches to be added.

If the Adaptive Parameters have already been set in the current Motor-CAD file, their current values will be used. Otherwise, the Adaptive Parameters will be defined and set to default values.

Use the set\_adaptive\_parameter\_default method to set the required parameters if undefined.

```
mc.set_adaptive_parameter_default("Notch Sweep", 2)
mc.set_adaptive_parameter_default("Notch Depth", 1)
```

### Get required parameters and objects

Get the Adaptive Parameters specified in Motor-CAD, and their values

```
notch_angular_width = mc.get_adaptive_parameter_value("notch sweep")
notch_depth = mc.get_adaptive_parameter_value("notch depth")
```

Get the standard template stator region from Motor-CAD. Calculate the stator radius and define the stator centre coordinates.

```
stator_region = mc.get_region("Stator")
stator_radius = mc.get_variable("Stator_Bore") / 2
duplication_angle = 360 / stator_region.duplications
stator_centre = Coordinate(0, 0)
```

## Create the Adaptive Templates geometry

For each notch to be added:

- Calculate the angular position of the notch in mechanical degrees
- Create the notch Region and define the properties for the notch region
  - name
  - colour

- duplications
- material
- set the notch's parent to the stator region. This will allow Motor-CAD to treat the notch as a subregion of the stator and handle subtractions automatically.
- If the notch is closed, set the region in Motor-CAD.

```
notch_name = "Stator_Notch"
notch = Region(region_type=RegionType.stator)
notch.name = notch_name
notch.colour = (255, 255, 255)
notch.duplications = stator_region.duplications
notch.material = "Air"
notch.parent = stator_region
# generate coordinates for triangular notch using start/mid/end
# angles above converting from polar to cartesian
x1, y1 = rt_to_xy(stator_radius, 0)
x2, y2 = rt_to_xy(stator_radius, notch_angular_width / 2)
x3, y3 = rt_to_xy(stator_radius + notch_depth, 0)
p1 = Coordinate(x1, y1)
p2 = Coordinate(x2, y2)
p3 = Coordinate(x3, y3)
# using coordinate create entities making up notch region
airgap_arc = Arc(p1, p2, stator_centre, stator_radius * 1.0)
line_1 = Line(p2, p3)
line_2 = Line(p3, p1)
# add entities into notch region
notch.add_entity(airgap_arc)
notch.add_entity(line_1)
notch.add_entity(line_2)
if notch.is_closed():
    mc.set_region(notch)
# Generate other side by symmetry
symmetry_angle = (2 * math.pi) / stator_region.duplications / 2
symmetry_line = Line(
    stator_centre,
    Coordinate(stator_radius * math.cos(symmetry_angle), stator_radius * math.sin(symm
)
notch_mirror = notch.mirror(symmetry_line)
notch_mirror.name = "Stator_Notch_2"
if notch_mirror.is_closed():
    # set the notches parent to the stator region, this will allow Motor-CAD to treat
    # the notch as a sub-region of the stator and handle subtractions automatically
    notch_mirror.parent = stator_region
    mc.set_region(notch_mirror)
```

## Load in Adaptive Templates Script if required

When the script is run externally:

- Set Geometry type to "Adaptive"
- Load the script into the Adaptive Templates tab
- Go to the Geometry -> Radial tab to run the Adaptive Templates Script and display the new geometry

```
if not pymotorcad.is_running_in_internal_scripting():
    mc.set_variable("GeometryTemplateType", 1)
    mc.load_adaptive_script(sys.argv[0])
    mc.display_screen("Geometry;Radial")
```

![](_page_4_Picture_8.jpeg)

<span id="page-4-0"></span>Total running time of the script: (1 minutes 10.750 seconds)

Download Python source code: [BPMTriangularStatorNotches.py](https://motorcad.docs.pyansys.com/version/stable/_downloads/99ee6de35deea7ecde43ef7b2759e195/BPMTriangularStatorNotches.py)

Download zipped: [BPMTriangularStatorNotches.zip](https://motorcad.docs.pyansys.com/version/stable/_downloads/56b79df081648807e58159285e24d9f4/BPMTriangularStatorNotches.zip)

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.