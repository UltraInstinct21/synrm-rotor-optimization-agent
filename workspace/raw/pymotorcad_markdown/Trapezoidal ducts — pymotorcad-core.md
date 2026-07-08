![](_page_0_Picture_2.jpeg)

Note

Go to the [end](#page-5-0) to download the full example code.

## Trapezoidal ducts

This script applies the adaptive templates functionality to modify rectangular ducts into trapezoidal ducts.

## Perform required imports

Import pymotorcad to access Motor-CAD. Import Coordinate , rt\_to\_xy , xy\_to\_rt to define the adaptive template geometry. Import os , shutil , sys , and tempfile to open and save a temporary .mot file if none is open.

```
import os
import shutil
import sys
import tempfile
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import xy_to_rt
```

# Connect to Motor-CAD

If this script is loaded into the Adaptive Templates file in Motor-CAD, the current Motor-CAD instance is used.

If the script is run externally, these actions occur: a new Motor-CAD instance is opened, the e10 IPM motor template is loaded and set up with four rectangular rotor ducts, and the file is saved to a temporary folder. To keep a new Motor-CAD instance open after executing the script, use the``MotorCAD(keep\_instance\_open=True)`` option when opening the new instance. Alternatively, use the MotorCAD() method, which closes the Motor-CAD instance after the script is executed.

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
    mc.load_template("e10")
    mc.set_variable("RotorDuctType", 4) # select rectangular ducts
    mc.set_array_variable("RotorCircularDuctLayer_ChannelWidth", 0, 4) # set duct wid
    # Open relevant file
    working_folder = os.path.join(tempfile.gettempdir(), "adaptive_library")
    try:
        shutil.rmtree(working_folder)
    except:
        pass
    os.mkdir(working_folder)
    mot_name = "Trapezoidal_duct"
    mc.save_to_file(working_folder + "/" + mot_name + ".mot")
# Reset geometry to default
mc.reset_adaptive_geometry()
```

## Define necessary functions

### Check line distance from origin

The rectangle consists of two lines of length equal to the rectangle width. Only the top line requires modification. It is necessary to check whether the line is closest to the origin. Index i is the line under investigation. Index j is the adjacent line. If the radius of midpoint of line i is less than that of line j , line i is closer to the origin.

```
def check_line_origin_distance(i, duct_region):
    if i == 0: # first index of rectangle duct
        j = 1
    else:
        j = i - 1
    rad_start_i, _ = xy_to_rt(duct_region.entities[i].start.x, duct_region.entities[i]
    rad_end_i, _ = xy_to_rt(duct_region.entities[i].end.x, duct_region.entities[i].end
    rad_mid_i = (rad_start_i + rad_end_i) / 2
    rad_start_j, _ = xy_to_rt(duct_region.entities[j].start.x, duct_region.entities[j]
    rad_end_j, _ = xy_to_rt(duct_region.entities[j].end.x, duct_region.entities[j].end
    rad_mid_j = (rad_start_j + rad_end_j) / 2
    if rad_mid_i < rad_mid_j:
        return True
    else:
        return False
```

## Get required parameters and objects

From Motor-CAD, get the adaptive parameters and their values.

Use the set\_adaptive\_parameter\_default() method to set the required Trapezoid\_base\_ratio parameter if undefined.

```
mc.set_adaptive_parameter_default("Trapezoid_base_ratio", 0.7)
```

Set required parameters for the trapezoid: ratio of top width / base width ( Trapezoid\_base\_ratio ), trapezoid width and trapezoid height.

```
Trap_ratio = mc.get_adaptive_parameter_value("Trapezoid_base_ratio")
Trap_W = mc.get_array_variable(
    "RotorCircularDuctLayer_ChannelWidth",
    0,
)
Trap_H = mc.get_array_variable(
    "RotorCircularDuctLayer_ChannelHeight",
    0,
)
```

Get the standard template rotor region. This can be drawn for debugging if required.

```
rt_region = mc.get_region("Rotor") # get the rotor region
```

## Create the Adaptive Templates geometry

For each child region of the rotor region:

- Check whether the region is a rotor duct.
- Find the top line that makes up the duct.
- Modify the start and end points of the line using the get\_coordinate\_from\_distance() method.
- Set the region in Motor-CAD.

The script accounts for whether ducts are full ducts or half ducts (the case when a duct spans the rotor pole boundary)

```
duct_area = Trap_H * Trap_W
for child_name in rt_region.child_names:
    if "RotorDuctFluidRegion" in child_name:
        duct_region = mc.get_region(child_name)
        if round(duct_region.area / duct_area, 2) == 1: # check if a full duct is draw
            for i, entity in enumerate(duct_region.entities):
                if (
                    round(entity.length / Trap_W, 2) == 1
                ): # check if the line length is the same as the duct width
                    # additional check in case the duct width = height
                    r_start_point, angle_start_point = xy_to_rt(entity.start.x, entity
                    r_end_point, angle_end_point = xy_to_rt(entity.end.x, entity.end.y
                    if abs(angle_end_point - angle_start_point) > 0.05: # 0.05 degree
                        # check if the line is located at top or bottom
                        Line_origin = check_line_origin_distance(i, duct_region)
                        if not Line_origin:
                            distance = entity.length * (1 - Trap_ratio)
                            new_start_point = entity.get_coordinate_from_distance(
                                entity.start, fraction=(1 - Trap_ratio) / 2
                            )
                            new_end_point = entity.get_coordinate_from_distance(
                                entity.end, fraction=(1 - Trap_ratio) / 2
                            )
                            duct_region.edit_point(entity.start, new_start_point)
                            duct_region.edit_point(entity.end, new_end_point)
                            mc.set_region(duct_region)
        elif (
            round(duct_region.area / duct_area, 2) == 0.5
        ): # account for the case where we have half ducts
            Symm_angle = 360 / duct_region.duplications # angle of symmetry
            for i, entity in enumerate(duct_region.entities):
                if (
                    round(entity.length / Trap_W, 2) == 0.5
                ): # check if the line length is the same as the duct width
                    # additional check in case the duct width = height
                    r_start_point, angle_start_point = xy_to_rt(entity.start.x, entity
                    r_end_point, angle_end_point = xy_to_rt(entity.end.x, entity.end.y
                    if abs(angle_end_point - angle_start_point) > 0.05: # 0.05 degree
                        Line_origin = check_line_origin_distance(i, duct_region)
                        if not Line_origin:
                            distance = entity.length * (1 - Trap_ratio)
                            if (
                                angle_start_point - 0 < 1e-10
                                or angle_start_point == 0
                                or round(angle_start_point / Symm_angle, 2) == 1
                            ): # on symmetry plane
                                new_end_point = entity.get_coordinate_from_distance(
                                    entity.end, fraction=(1 - Trap_ratio) / 2
                                )
                                duct_region.edit_point(entity.end, new_end_point)
                            elif (
                                angle_end_point - 0 < 1e-10
                                or round(angle_end_point / Symm_angle, 2) == 1
                            ): # symmetry plane
                                new_start_point = entity.get_coordinate_from_distance(
                                    entity.start, fraction=(1 - Trap_ratio) / 2
                                )
                                duct_region.edit_point(entity.start, new_start_point)
                            mc.set_region(duct_region)
```

![](_page_4_Picture_2.jpeg)

## Load in Adaptive Templates script if required

When this script is run externally, the script executes the following:

- Set Geometry type to Adaptive.
- Load the script into the Adaptive Templates tab.
- Go to the Geometry -> Radial tab to run the Adaptive Templates script and display the new geometry.

![](_page_4_Picture_8.jpeg)

#### Note

When running in a Jupyter Notebook, you must provide the path for the Adaptive Templates script (PY file) instead of sys.argv[0] when using the load\_adaptive\_script() method.

```
if not pymotorcad.is_running_in_internal_scripting():
    mc.set_variable("GeometryTemplateType", 1)
    mc.load_adaptive_script(sys.argv[0])
    mc.display_screen("Geometry;Radial")
```

<span id="page-5-0"></span>Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3. Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

Last updated on April 15, 2026