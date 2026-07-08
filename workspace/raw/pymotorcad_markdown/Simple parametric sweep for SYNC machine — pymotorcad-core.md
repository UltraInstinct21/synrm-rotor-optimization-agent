![](_page_0_Picture_2.jpeg)

Note

Go to the [end](#page-2-0) to download the full example code.

## Simple parametric sweep for SYNC machine

This is a simple example showing a two-dimensional parametric sweep for a wound field synchronous motor varying continuous stator skew and field current.

## Out:

```
Running skew: 0 Field current: 5
Sound power level [dB], electrical time order, space order:
(68.7276863619575, 2.0, 8)
(65.5984814738516, 12.0, 0)
(61.9204366255285, 10.0, -8)
(53.5085651751754, 4.0, -8)
(52.1074232045378, 6.0, 0)
Running skew: 0 Field current: 10
Sound power level [dB], electrical time order, space order:
(72.333173447728, 2.0, 8)
(65.1847772191679, 12.0, 0)
(64.001889551303, 10.0, -8)
(57.9477621024528, 6.0, 0)
(53.6727826441799, 14.0, 8)
Running skew: 7.5 Field current: 5
Sound power level [dB], electrical time order, space order:
(68.0603698519479, 2.0, 8)
(52.3791765470274, 6.0, 0)
(51.3030010569811, 4.0, -8)
(49.8355349659019, 10.0, -8)
(49.3445496498124, 12.0, 0)
Running skew: 7.5 Field current: 10
Sound power level [dB], electrical time order, space order:
(71.7012705350929, 2.0, 8)
(55.0306134574719, 6.0, 0)
(52.1824725532868, 3.0, 8)
(50.4153803571902, 1.0, 0)
(50.3422557394932, 10.0, -8)
```

```
import math
import ansys.motorcad.core as pymotorcad
# Open connection to Motor-CAD, and open e3 template (Sync machine)
mc = pymotorcad.MotorCAD()
mc.set_variable("MessageDisplayState", 2)
mc.load_template("e3")
# Alternatively, use the following
# mc = pymotorcad.MotorCAD()
# mc.load_from_file('filename.mot')
# Ensure the transient calculation and force calculation are enabled
mc.set_variable("TorqueCalculation", True)
mc.set_variable("ElectromagneticForcesCalc_Load", True)
# Make sure continuous stator skew is enabled
mc.set_variable("SkewType", 1)
# Set up the sweep parameters, in this case for sync machine field current and skew ang
skew_angles = [0, 7.5]
field_currents = [5, 10]
# Run the sweep
for skew_angle in skew_angles:
    for field_current in field_currents:
        # Set the parameter(s) to sweep
        mc.set_variable("StatorSkew", skew_angle)
        mc.set_variable("DCFieldCurrent", field_current)
        # Tell the user what step we are on:
        print("Running skew: " + str(skew_angle) + " Field current: " + str(field_curr
        # Run the calculation
        mc.do_magnetic_calculation()
        # Find many steps have been run
        if mc.get_variable("MotorType_MotorLAB") == "IM":
            try:
                # Variable was renamed in 2024R1, try newer naming first
                numberOfCycles = mc.get_variable("IMSingleLoadNumberCycles_Rotating")
            except pymotorcad.MotorCADError:
                numberOfCycles = mc.get_variable("IMSingleLoadNumberCycles")
        else:
            numberOfCycles = mc.get_variable("TorqueNumberCycles")
        # Get the NVH data matrix
        nvh_data_raw = mc.get_magnetic_3d_graph("NVH_RadiatedPower_Level_OL", 1)
        # Find length of data available
        time_order_items = len(nvh_data_raw.y)
        space_order_items = len(nvh_data_raw.x)
        index_offset_space = math.floor(space_order_items / 2)
        # Iterate over data, storing as a list of tuples, so we can sort to find the bi
        nvh_list = []
        for raw_time_order in range(time_order_items):
            electrical_order = raw_time_order / numberOfCycles
            for raw_space_order in range(space_order_items):
                space_order = raw_space_order - index_offset_space
                # Store a tuple of sound power level, electrical time order, space orde
                nvh_list.append(
                    (
                        nvh_data_raw.data[raw_space_order][raw_time_order],
                        electrical_order,
```

```
space_order,
            )
        )
# Sort the list on NVH, from highest to lowest, and show top 5 orders
nvh_list.sort(reverse=True)
print("Sound power level [dB], electrical time order, space order:")
for i in range(min(5, len(nvh_list))):
    print(nvh list[i])
```

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

<span id="page-2-0"></span>Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Last updated on April 15, 2026