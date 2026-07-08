![](_page_0_Picture_2.jpeg)

Note

Go to the end to download the full example code.

## Motor-CAD force extraction example script

This sets up the operating points and threading options for a force/NVH calculation, then displays some key force orders from a 2d FFT that may be important for NVH.

Import PyMotorCAD and launch Motor-CAD, turning off pop-up messages.

```
import ansys.motorcad.core as pymotorcad
mc = pymotorcad.MotorCAD()
mc.set_variable("MessageDisplayState", 2)
```

Load a baseline model - in this case a template. For users, this would normally be a baseline model.

```
mc.load_template("e9")
```

Set 90 torque points per cycle, which will give us information up to the 45th electrical order. If using an induction motor, use IMSingleLoadPointsPerCycle\_Rotating instead.

```
mc.set_variable("TorquePointsPerCycle", 90)
```

Enable multithreading for the force/NVH calculation

```
mc.set_variable("MultiForceThreading", 0) # 0 is multithreaded, 1 is single threaded.
```

Set operating points, in this case for speed and torque definition.

```
operating_points_speed = [250, 4000, 8000] # RPM
operating_points_torque = [250, 250, 100] # Nm
num_operating_points = len(operating_points_speed)
# Make sure the table is the correct length before setting value
mc.set_variable("NumLoadPoints", num_operating_points)
# Set the values:
for operating_point in range(num_operating_points):
    mc.set_array_variable(
        "LoadPoint_Speed_Array", operating_point, operating_points_speed[operating_poi
    )
    mc.set_array_variable(
        "LoadPoint_Torque_Array", operating_point, operating_points_torque[operating_po
    )
```

## Note

For other motor types or options, the following may be needed:

- All motor types and options: LoadPoint\_Speed\_Array
- BPM or similar for torque based definition: LoadPoint\_Torque\_Array
- BPM or similar for current/phase advance definition: LoadPoint\_Current\_Array,

and LoadPoint\_PhaseAdvance\_Array - SRM: LoadPoint\_Current\_Array, LoadPoint\_OnAngle\_Array, and LoadPoint\_OffAngle\_Array - IM: LoadPoint\_Current\_Array and LoadPoint\_Slip\_Array

Run the electromagnetic FEA calculation, which calculates the forces.

```
mc.do_multi_force_calculation()
```

Define the orders that we want to extract as space and time order pairs. In this case, these are some of the important orders for a 48 slot, 8 pole motor.

The orders are defined as pairs of [Space order (positive or negative), electrical time order (0 or positive)]:

```
required_orders = [[0, 12], [0, 24], [8, 2], [-8, 10], [8, 14]]
```

Get information about the results.

```
# Number of cycles. If using this for an induction motor, use
# `IMSingleLoadNumberCycles_Rotating` instead
electrical_cycles = mc.get_variable("TorqueNumberCycles")
# Maximum number of space orders in results
mech_force_space_order_max = mc.get_variable("ForceMaxOrder_Space_Stator_OL")
# Number of operating points. In this example we have set this earlier in the script
num_operating_points = mc.get_variable("NumLoadPoints")
# Find how many slices (for skew) are available.
if mc.get_variable("SkewType") == 2:
    # Stepped skew
    rotor_slices = mc.get_variable("RotorSkewSlices")
else:
    rotor_slices = 1
```

Find the force density for each slice, at the different operating points and slices:

```
for rotor_slice in range(rotor_slices):
    print("\nSlice " + str(rotor_slice + 1) + ":")
    for operating_point in range(num_operating_points):
        print("\nOperating point " + str(operating_point + 1) + ":")
        print(
            "Results as: Space order, "
            "Electrical order, "
            "Force density amplitude (N/m^2), "
            "Force density phase (deg):"
        )
        for required_order in required_orders:
            required_space_order = required_order[0]
            required_electrical_time_order = required_order[1]
            # Results stored with negative space orders at the end, so apply offset
            if required_space_order < 0:
                raw_space_order = required_space_order + 2 * mech_force_space_order_max
            else:
                raw_space_order = required_space_order
            # If more than one cycle used, scale between electrical orders and interna
            raw_time_order = required_electrical_time_order * electrical_cycles
            # Find the force density using GetMagnetic3DGraphPoint:
            # Note the use of _Th1 for the 1st operating point in the name.
            # Note also that rotor slice numbering starts at 1.
            _, force_density_amplitude = mc.get_magnetic_3d_graph_point(
                "Fr_Density_Stator_FFT_Amplitude_OL" + "_Th" + str(operating_point + 1
                rotor_slice + 1,
                raw_space_order,
                raw_time_order,
            )
            _, force_density_angle = mc.get_magnetic_3d_graph_point(
                "Fr_Density_Stator_FFT_Angle_OL" + "_Th" + str(operating_point + 1),
                rotor_slice + 1,
                ra space order
```

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Last updated on April 15, 2026