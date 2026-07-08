![](_page_0_Picture_2.jpeg)

Note

Go to the [end](#page-2-0) to download the full example code.

## Mechanical force

This example demonstrates internal scripting mechanical force functionality This will compute the operating conditions for some requested torque values and display the natural frequencies for the 0th and 8th modes.

Perform required imports

**import ansys.motorcad.core as pymotorcad**

Launch Motor-CAD

mc = pymotorcad.MotorCAD()

Create internal script. This could also be saved in a separate file

```
import numpy as np
# This function is called when "Run" is pressed
def main():
    pass
class mechanical_forces:
    def initial(self):
        # %%
        # Disable pop-up messages
        mc.set_variable("MessageDisplayState", 2)
        # Called before calculation
        # For each operating point, set requested torque and speed
        # (using this mode requires that a Lab model has been built)
        # Note that if a lab model isn't available, MultiForceLoadPointDefinition
        # can be set to 1 (Current and Phase), and
        # LoadPoint_Current_Array and LoadPoint_PhaseAdvance_Array set
        # IM operating points are set with speed, current, and LoadPoint_Slip_Array
        NVH_Duty_Speed = np.concatenate((250, 6000, 9000), axis=None)
        NVH_Duty_Torque = np.concatenate((40, 20, 10), axis=None)
        mc.set_variable("NumLoadPoints", len(NVH_Duty_Speed))
        for i in range(len(NVH_Duty_Speed)):
            mc.set_array_variable("LoadPoint_Speed_Array", i, float(NVH_Duty_Speed[i])
            mc.set_array_variable("LoadPoint_Torque_Array", i, float(NVH_Duty_Torque[i
        # Set number of steps per cycle - for speed just use 30 in this example. 90 wou
        # a more usual minimum
        # If calculating for an induction machine (IM), use IMSingleLoadPointsPerCycle
        mc.set_variable("TorquePointsPerCycle", 30)
    def final(self):
        # Called after calculation
        # Example modal results
        o_Natural_Freq_Mode_0 = mc.get_magnetic_graph_point("NVH_NaturalFrequency", 0)
        o_Natural_Freq_Mode_8 = mc.get_magnetic_graph_point("NVH_NaturalFrequency", 8)
        mc.show_message(" Natural_Freq_Mode_0 " + str(o_Natural_Freq_Mode_0))
        mc.show_message(" Natural_Freq_Mode_8 " + str(o_Natural_Freq_Mode_8))
        mc.set_variable("MessageDisplayState", 0)
```

## Note

For further details, please see the E-NVH tutorial.

## PyMotorCAD Documentation Example

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

<span id="page-2-0"></span>Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026