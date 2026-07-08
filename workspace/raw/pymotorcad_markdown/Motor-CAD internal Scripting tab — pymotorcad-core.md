# Motor-CAD internal Scripting tab

The Scripting tab in Motor-CAD facilitates creating, editing, loading, and saving internal Python scripts within Motor-CAD.

![](_page_0_Picture_4.jpeg)

Scripting -> Settings tab in Ansys Motor-CAD 2023 R1

From the Scripting tab in Motor-CAD, you can connect from an internal script by accessing the MotorCAD() object with this code:

```
import ansys.motorcad.core as pymotorcad
mcApp = pymotorcad.MotorCAD()
```

With the [MotorCAD](https://motorcad.docs.pyansys.com/version/stable/methods/MotorCAD_object.html#ref-motorcad-object) API, you can use PyMotorCAD methods to send commands to the current Motor-CAD instance. For example, you can set and get values before, during, and after calculations. You can also create a script for Motor-CAD automation.

In the following image, the Scripting tab shows the demo script. You can use this default script as a starting point for scripting internally in Motor-CAD. However, you can also add and run any Python script from this tab.

Scripting -> Python Scripting tab in Ansys Motor-CAD 2023 R1

# Demo script example

The demo script is shown by default on the Scripting tab in Moto-CAD to providing examples of how you use PyMotorCAD methods and Motor-CAD automation parameters.

For more information, see the Motor-CAD Automation tutorial (section 2.iii), provided with the Motor-CAD installation.

#### Setup

Import pymotorcad to access Motor-CAD.

```
import ansys.motorcad.core as pymotorcad
```

Connect to Motor-CAD.

```
mcApp = pymotorcad.MotorCAD()
```

# Main function

The main function is called when Run is pressed in the Motor-CAD GUI. You can use the main function to test other functions before running a calculation. For example, you can use it to run the thermal\_steady() and initial() functions. You can also use it to run calculations within another defined function, such as the demo\_func function.

```
def main():
    user_func = thermal_steady()
    user_func.initial()
    demo_func()
```

## Demo function

The defined demo\_func function sets the tooth\_width function and runs thermal calculations.

All messages are set to display in a separate window using this PyMotorCAD method:

mcApp.set\_variable("MessageDisplayState", 2)

![](_page_2_Picture_10.jpeg)

Note

This PyMotorCAD method disables crucial popups, including prompts to save files and overwrite data. Ensure that this is the desired behavior.

The demo\_func function defines a range of values for the tooth\_width function, runs a steady state thermal calculation, and gets the average winding temperature for each. Results are shown in the message window. The last line of the function resets the message window.

```
def demo_func():
    array_tooth_widths = [1, 1.5, 2.0]
    mcApp.set_variable("MessageDisplayState", 2)
    for toothWidth in array_tooth_widths:
        mcApp.show_message("Tooth width = " + str(toothWidth))
        mcApp.set_variable("Tooth_Width", toothWidth)
        mcApp.do_steady_state_analysis()
        temperature = mcApp.get_variable(
            "T_[WINDING_AVERAGE]",
        )
        mcApp.show_message("Winding temperature = " + str(temperature))
    mcApp.set_variable("MessageDisplayState", 0)
```

## Functions run during calculations

The previously described functions run only when the Run During Analysis option is selected from the Scripting -> Settings tab in Motor-CAD. (This option appears under the Script Control heading.)

![](_page_3_Picture_5.jpeg)

Scripting -> Settings tab in Ansys Motor-CAD 2023 R1

If the Run During Analysis option is selected, the script is imported. This means that anything other than setting up the MotorCAD object should be moved to a function or class to avoid unexpected behavior.

Five classes are defined: thermal\_steady , thermal\_transient , emagnetic , mechanical\_stress and mechanical\_forces . Each of these classes contains the initial and final functions. The thermal classes also contain the main function.

- initial is called before the calculation.
- final is called after the calculation.
- main is called before each time step in a calculation.

The thermal\_steady class contains functions for steady-state thermal calculations:

```
class thermal_steady:
    def initial(self):
        self.step = 0
        print("Thermal Steady State - Initial")
    def main(self):
        self.step = self.step + 1
        print("Step: " + str(self.step) + ". Thermal Steady State - Main")
    def final(self):
        print("Thermal Steady State - Final")
```

The thermal\_transient class contains functions for transient thermal calculations:

```
class thermal_transient:
    def initial(self):
        self.step = 0
        print("Thermal Transient - Initial")
    def main(self):
        self.step = self.step + 1
        print("Step: " + str(self.step) + ". Thermal Transient State - Main")
    def final(self):
        print("Thermal Transient - Final")
```

The emagnetic class contains functions for E-Magnetic calculations:

```
class emagnetic:
    def initial(self):
        print("E-Magnetic - Initial")
    def final(self):
        print("E-Magnetic - Final")
```

The mechanical\_stress class contains functions for Mechanical stress calculations:

```
class mechanical_stress:
   def initial(self):
         i t("M h St I iti l")
```

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Last updated on April 15, 2026