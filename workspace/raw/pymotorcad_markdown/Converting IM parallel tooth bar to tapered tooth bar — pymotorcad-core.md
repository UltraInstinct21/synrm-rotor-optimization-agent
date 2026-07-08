![](_page_0_Picture_2.jpeg)

Note

Go to the end to download the full example code.

## Converting IM parallel tooth bar to tapered tooth bar

This script applies the adaptive templates functionality to change the points at the bottom of parallel tooth to create a tapered tooth bar geometry.

```
import math
import sys
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Coordinate, rt_to_xy, xy_to_rt
# Connect to Motor-CAD, using existing instance
# Alternatively, we could open a new instance and load a file with mc.load_from_file()
mc = pymotorcad.MotorCAD()
# Reset geometry to default
mc.reset_adaptive_geometry()
# Disable popup messages
mc.set_variable("MessageDisplayState", 2)
# function to return angle based on chord length
# Used for finding new point based on tooth width at bottom of bar
def chord_angle(cord_length, r):
    angle = 2 * math.asin(cord_length / (2 * r))
    return angle * 180 / math.pi
# Set IM motor type if not already
if not pymotorcad.is_running_in_internal_scripting():
    mc.load_template("i6a")
# Get the bar region
bar = mc.get_region("TopRotorBar")
# Get the points at the bottom corners of bar
# Point1 is away from x axis
point1 = bar.points[3]
point2 = bar.points[5]
# Get the top bar tooth width
# Define adaptive parameter for booth bar tooth width
tooth_width_top = mc.get_variable("Rotor_Tooth_Width_T")
mc.set_adaptive_parameter_default("Rotor Tooth Width Bottom", 4)
tooth_width_bottom = mc.get_adaptive_parameter_value("Rotor Tooth Width Bottom")
# Get the point 1 polar coordinates and modify
point1_r, point_1_t = xy_to_rt(point1.x, point1.y)
```

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Last updated on April 15, 2026