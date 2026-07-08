![](_page_0_Picture_2.jpeg)

Note

Go to the end to download the full example code.

## Oblong stator ducts with thermal adjustment

This script applies the adaptive templates functionality to modify rectangular ducts into oblong ducts. Further, the thermal effect of modified duct is taken into account by modifying the area adjustment under housing water jacket in thermal module.

## Perform required imports

Import pymotorcad to access Motor-CAD. Import Arc , Line , Coordinate , rt\_to\_xy , xy\_to\_rt , math to define the adaptive template geometry. Import os , shutil , sys , and tempfile to open and save a temporary .mot file if none is open.

```
import math
import os
import shutil
import sys
import tempfile
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Arc, Coordinate, Line, rt_to_xy, xy_to_rt
```

# Connect to Motor-CAD

If this script is loaded into the Adaptive Templates file in Motor-CAD, the current Motor-CAD instance is used.

If the script is run externally, these actions occur: a new Motor-CAD instance is opened, the e9 IPM motor template is loaded and set up with rectangular stator ducts, and the file is saved to a temporary folder. To keep a new Motor-CAD instance open after executing the script, use the MotorCAD(keep\_instance\_open=True) option when opening the new instance. Alternatively, use the MotorCAD() method, which closes the Motor-CAD instance after the script is executed.

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
    mc.set_variable("StatorDuctType", 4) # selected rectangular ducts
    mc.set_variable("CircularDuctLayers", 1) # set number of duct layers
    mc.set_variable("CircularDuctL1RadialDiameter", 180) # set number of duct radial d
    mc.set_variable("CircularDuctL1ChannelWidth", 2) # set duct width
    mc.set_variable("CircularDuctL1ChannelHeight", 3) # set duct height
    mc.set_variable("CircularDuctL1Channels", 48) # set number of duct channels
    mc.set_variable("HousingType", 0) # set housing type to 'Round'
    # Open relevant file
    working_folder = os.path.join(tempfile.gettempdir(), "adaptive_library")
    try:
        shutil.rmtree(working_folder)
    except:
        pass
    os.mkdir(working_folder)
    mot_name = "Oblong_duct"
    mc.save_to_file(working_folder + "/" + mot_name + ".mot")
# Reset geometry to default
mc.reset_adaptive_geometry()
```

## Define necessary functions

#### Check line distance from origin

The rectangle consists of two lines of length equal to the rectangle width. Only the top and bottom lines requires modification. It is necessary to check whether the line is closest to the origin. As this will affect the center of arcs needs to convert the lines. Index i is the line under investigation. Index j is the adjacent line. If the radius of midpoint of line i is less than that of line j , line i is closer to the origin.

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

#### Generate arc associated with oblong duct

Two separate functions are needed depending on full duct or half duct (due to symmetry) is present under Geometry Editor

```
def get_arc_radius(entity_start, entity_end, height):
    # Generate arc radius and center based on
    # line and arc height
    start_point_xy = [entity_start.x, entity_start.y]
    end_point_xy = [entity_end.x, entity_end.y]
    x = math.dist(start_point_xy, end_point_xy) / 2 # chord length/2
    y = height
    # conversion to polar coordinates
    start_point_r, start_point_t = xy_to_rt(entity_start.x, entity_start.y)
    end_point_r, end_piont_t = xy_to_rt(entity_end.x, entity_end.y)
    r = (x**2 + y**2) / (2 * y) # radius
    return r
def get_arc_radius_halfduct(entity_start, entity_end, height, Line_origin, Symm_angle):
    # Generate arc radius, center, start and end point based on for half duct
    # line and arc height
    start_point_xy = [entity_start.x, entity_start.y]
    end_point_xy = [entity_end.x, entity_end.y]
    x = math.dist(start_point_xy, end_point_xy) # chord length
    y = height
    start_point_r, start_point_t = xy_to_rt(entity_start.x, entity_start.y)
    end_point_r, end_piont_t = xy_to_rt(entity_end.x, entity_end.y)
    r = (x**2 + y**2) / (2 * y) # radius
    if Line_origin == True:
        # line is closer to origin
        if start_point_t == 0 or round(start_point_t / Symm_angle, 2) == 1:
            # start point is on symmetry boundary of geometry
            new_start_x, new_start_y = rt_to_xy(start_point_r - height, start_point_t)
            new_end_x, new_end_y = entity_end.x, entity_end.y
        elif end_piont_t == 0 or round(end_piont_t / Symm_angle, 2) == 1:
            # end point is on symmetry boundary of geometry
            new_start_x, new_start_y = entity_start.x, entity_start.y
            new_end_x, new_end_y = rt_to_xy(end_point_r - height, end_piont_t)
    else:
        # Line is far from origin
        if start_point_t == 0 or round(start_point_t / Symm_angle, 2) == 1:
            # start point is on symmetry boundary of geometry
            new_start_x, new_start_y = rt_to_xy(start_point_r + height, start_point_t)
            new_end_x, new_end_y = entity_end.x, entity_end.y
        elif end_piont_t == 0 or round(end_piont_t / Symm_angle, 2) == 1:
            # end point is on symmetry boundary of geometry
            new_start_x, new_start_y = entity_start.x, entity_start.y
            new_end_x, new_end_y = rt_to_xy(end_point_r + height, end_piont_t)
    new_start_point = Coordinate(new_start_x, new_start_y)
    new_end_point = Coordinate(new_end_x, new_end_y)
    return r, new_start_point, new_end_point
```

### Get required parameters and objects

From Motor-CAD, get the adaptive parameters and their values.

Use the set\_adaptive\_parameter\_default() method to set the required Duct Arc Height parameter if undefined.

```
mc.set_adaptive_parameter_default("Duct Arc Height", 0.7)
```

Set required parameters for the oblong: height of arc Duct Arc Height , duct width and duct height.

```
duct_arc_height = mc.get_adaptive_parameter_value("Duct Arc Height")
duct_height = mc.get_variable("CircularDuctL1ChannelHeight")
duct_width = mc.get_variable("CircularDuctL1ChannelWidth")
duct_area = duct_height * duct_width
```

Get the standard template stator region. This can be drawn for debugging if required.

```
st_region = mc.get_region("stator") # get the stator region
```

## Create the Adaptive Templates geometry

For each child region of the stator region:

- Check whether the region is a stator duct.
- Find the top and bottom lines that makes up the duct.
- Modify the lines with respective arcs.
- Set the region in Motor-CAD.

The script accounts for whether ducts are full ducts or half ducts (the case when a duct spans the rotor pole boundary)

```
for child_name in st_region.child_names:
    if "StatorDuctFluidRegion" in child_name:
        duct_region = mc.get_region(child_name)
        if round(duct_region.area / duct_area, 2) == 1: # check if full duct is drawn
            for i, entity in enumerate(duct_region.entities):
                if round(entity.length / duct_width, 2) == 1: # check if the line is
                    # additional check in case width = height
                    _, angle_start_point_angle = xy_to_rt(entity.start.x, entity.start
                    _, angle_end_point_angle = xy_to_rt(entity.end.x, entity.end.y)
                    if (
                        abs(angle_end_point_angle - angle_start_point_angle) > 0.05
                    ): # 0.05 degree is tolerance
                        # get radius and center
                        # convert this line segment to Arc
                        Line_origin = check_line_origin_distance(
                            i, duct_region
                        ) # line near of far from origin
                        radius = get_arc_radius(entity.start, entity.end, duct_arc_heig
                        Duct_Arc = Arc(entity.start, entity.end, radius=radius)
                        duct_region.entities[i] = Duct_Arc
        elif round(duct_region.area / duct_area, 2) == 0.5: # if the half duct is draw
            Symm_angle = 360 / duct_region.duplications # angle of symmetry
            for i, entity in enumerate(duct_region.entities):
                if (
                    round(entity.length / duct_width, 2) == 0.5
                ): # check if the line is half duct width
                    # additional check in case width/2 = height
                    _, angle_start_point_angle = xy_to_rt(entity.start.x, entity.start
                    _, angle_end_point_angle = xy_to_rt(entity.end.x, entity.end.y)
                    if (
                        abs(angle_end_point_angle - angle_start_point_angle) > 0.05
                    ): # 0.05 degree is tolerance
                        # get radius and center
                        # convert this line segment to Arc
                        Line_origin = check_line_origin_distance(i, duct_region)
                        radius, start_point, end_point = get_arc_radius_halfduct(
                            entity.start, entity.end, duct_arc_height, Line_origin, Sym
                        )
                        Duct_Arc = Arc(start_point, end_point, radius=radius)
                        duct_region.entities[i] = Duct_Arc
                elif round(entity.length / duct_height, 2) == 1:
                    # modify the line on symmetry planes
                    rad_start_point, angle_start_point = xy_to_rt(entity.start.x, enti
                    rad_end_point, angle_end_point = xy_to_rt(entity.end.x, entity.end
                    if angle_start_point == 0 and angle_end_point == 0:
                        # line located at x=0
                        entity.start.x = entity.start.x - duct_arc_height
                        entity.end.x = entity.end.x + duct_arc_height
                    elif (
                        round(angle_start_point / Symm_angle, 2) == 1
                        and round(angle_end_point / Symm_angle, 2) == 1
                    ):
                        # line on symmetry plane
                        # start and end point follow anticlockwise naming convention
                        rad_start_point = rad_start_point + duct_arc_height
                        rad_end_point = rad_end_point - duct_arc_height
                        new_start_x, new_start_y = rt_to_xy(rad_start_point, angle_sta
                        new_end_x, new_end_y = rt_to_xy(rad_end_point, angle_end_point
                        start_point = Coordinate(new_start_x, new_start_y)
                        end_point = Coordinate(new_end_x, new_end_y)
                        duct_region.entities[i] = Line(start_point, end_point)
```

mc.set\_region(duct\_region)

![](_page_6_Picture_3.jpeg)

# Apply surface area correction in Motor-CAD Thermal

The oblong stator ducts can be used in the Motor-CAD Thermal model as channels for water jacket cooling. The Housing Water Jacket cooling model in Motor-CAD can be set up to use stator duct channels when a housing type without channels is selected in the Geometry tab.

As of Motor-CAD v2024R2, the Housing Water Jacket calculations will use duct areas from the Motor-CAD Standard Template geometry - not the custom Adaptive Templates geometry. For example, when the stator duct geometry has been updated from rectangular to oblong shapes, the duct area has increased. For this example, the area increases from 6 mm to 8.03852 . This can be seen in the Geometry -> Editor -> Geometry tab, or by using the area method for the duct region. 2 2

![](_page_7_Figure_2.jpeg)

![](_page_7_Figure_3.jpeg)

To account for this in the Housing Water Jacket cooling model, you can apply a cross section area adjustment. By default, this is set to 0. To see this in the Motor-CAD interface, go to the Input Data -> Housing Water Jacket -> Fluid FLow tab in the Thermal context.

![](_page_7_Picture_5.jpeg)

The appropriate area adjustment is calculated and applied within the Adaptive Templates script. To calculate the area adjustment, get the area of the stator duct regions using the area method. For the case where there are two half-ducts, it is necessary to get the area for all duct regions and to calculate the sum of the areas.

```
oblong_duct_areas = []
num_slots = mc.get_variable("Slot_Number")
num_ducts = mc.get_variable("CircularDuctL1Channels")
ducts_per_slot = num_ducts / num_slots
for child_name in st_region.child_names:
    if "StatorDuctFluidRegion" in child_name:
        oblong_duct_areas.append(mc.get_region(child_name).area)
oblong_duct_area = sum(oblong_duct_areas) / ducts_per_slot
```

The area of the original rectangular duct was already calculated earlier ( duct\_area ). The area adjustment is calculated by subtracting the rectangular duct area from the oblong duct area.

```
area_adjustment = oblong_duct_area - duct_area
```

Set the area adjustment value in Motor-CAD.

```
mc.set_array_variable("HousingWJ_Channel_CSArea_L1_A_Adjustment", 0, area_adjustment)
```

The area adjustment is applied by the Adaptive Templates script and is updated any time the geometry

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

Last updated on April 15, 2026