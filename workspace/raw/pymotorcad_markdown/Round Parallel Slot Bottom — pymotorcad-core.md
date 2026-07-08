![](_page_0_Picture_2.jpeg)

Note

Go to the [end](#page-5-0) to download the full example code.

## Round Parallel Slot Bottom

This script applies the adaptive templates functionality to modify parallel slot bottoms from having square corners to round corners.

#### Perform required imports

Import pymotorcad to access Motor-CAD. Import draw\_objects\_debug to plot figures of geometry objects. Import os , shutil , sys , and tempfile to open and save a temporary .mot file if none is open.

```
import os
import shutil
import sys
import tempfile
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry_drawing import draw_objects_debug
```

# Connect to Motor-CAD

If this script is loaded into the Adaptive Templates file in Motor-CAD, the current Motor-CAD instance is used.

If the script is run externally, these actions occur: a new Motor-CAD instance is opened, the e3 WFSM motor template is loaded, the Slot Type is set to Parallel Slot and the file is saved to a temporary folder. To keep a new Motor-CAD instance open after executing the script, use the MotorCAD(keep\_instance\_open=True) option when opening the new instance. Alternatively, use the MotorCAD() method, which closes the Motor-CAD instance after the script is executed.

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
    mc.load_template("e3")
    mc.set_variable("SlotType", 2)
    # Open relevant file
    working_folder = os.path.join(tempfile.gettempdir(), "adaptive_library")
    try:
        shutil.rmtree(working_folder)
    except:
        pass
    os.mkdir(working_folder)
    mot_name = "e3_WFSM_Round_Parallel_Slot"
    mc.save_to_file(working_folder + "/" + mot_name + ".mot")
# Reset geometry to default
mc.reset_adaptive_geometry()
```

#### Get required parameters and objects

From Motor-CAD, get the adaptive parameters and their values.

Use the set\_adaptive\_parameter\_default method to set the required Slot Bttm Corner Radius parameter if undefined.

```
mc.set_adaptive_parameter_default("Slot Bttm Corner Radius", 0.5)
```

Get the slot bottom corner radius adaptive parameter value.

```
radius = mc.get_adaptive_parameter_value("Slot Bttm Corner Radius")
```

Get the standard template regions with corners to be rounded. These can be drawn for debugging if required.

```
stator = mc.get_region("Stator")
winding_1 = mc.get_region("ArmatureSlotL1")
winding_2 = mc.get_region("ArmatureSlotR1")
stator_slot = mc.get_region("StatorSlot")
liner = mc.get_region("Liner")
impreg = mc.get_region("Impreg")
```

Get the slot corner coordinates to be rounded. Plot the corner coordinates and the stator region using the draw\_objects\_debug function to ensure you have selected the correct points.

```
corners = [stator.entities[5].end, stator.entities[7].end]
draw_objects_debug([stator, corners[0], corners[1]])
```

![](_page_2_Figure_4.jpeg)

Define the impregration corner coordinates to be rounded. Draw the impregnation region and corner coordinates using the draw\_objects\_debug function.

```
impreg_corners = [impreg.entities[1].end, impreg.entities[3].end]
draw_objects_debug([stator, impreg, impreg_corners[0], impreg_corners[1]])
```

![](_page_3_Figure_2.jpeg)

### Create the Adaptive Templates geometry

Round the slot bottom corners for all regions that share these corner coordinates using the Region.round\_corners method. Armature winding regions only have 1 of the two corners, so use the Region.round\_corner method for these regions.

```
stator.round_corners(corners, radius)
stator_slot.round_corners(corners, radius)
liner.round_corners(corners, radius)
winding_1.round_corner(corners[1], radius)
winding_2.round_corner(corners[0], radius)
```

Round the impregnation corners for the liner and impregnation regions using the Region.round\_corners method.

```
liner.round_corners(impreg_corners, radius)
impreg.round_corners(impreg_corners, radius)
```

Set the edited regions in Motor-CAD.

```
mc.set_region(stator)
mc.set_region(stator_slot)
mc.set_region(winding_1)
mc.set_region(winding_2)
mc.set_region(liner)
mc.set_region(impreg)
```

![](_page_4_Picture_7.jpeg)

### Load in Adaptive Templates script if required

When this script is run externally, the script executes the following:

- Set Geometry type to Adaptive.
- Load the script into the Adaptive Templates tab.
- Go to the Geometry -> Radial tab to run the Adaptive Templates script and display the new geometry.

![](_page_5_Picture_7.jpeg)

#### Note

When running in a Jupyter Notebook, you must provide the path for the Adaptive Templates script (PY file) instead of sys.argv[0] when using the load\_adaptive\_script() method.

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026

<span id="page-5-0"></span>Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.