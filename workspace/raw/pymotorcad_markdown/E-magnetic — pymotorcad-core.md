![](_page_0_Picture_2.jpeg)

Note

Go to the [end](#page-1-0) to download the full example code.

## <sup>E</sup>-magnetic

This example demonstrates internal scripting E-Mag functionality

```
import ansys.motorcad.core as pymotorcad
mc = pymotorcad.MotorCAD()
```

Disable pop-up messages

```
mc.set_variable("MessageDisplayState", 2)
# This function is called when "Run" is pressed
def main():
    pass
class emagnetic:
    def initial(self):
        mc.display_screen("Scripting")
        shaft_speed = mc.get_variable("ShaftSpeed")
        if shaft_speed > 1000:
            print("Shaft speed is too high. Resetting to 500")
            mc.set_variable("ShaftSpeed", 500)
    def final(self):
        loss_total = mc.get_variable("loss_total")
        # display total loss rounded to 2dp if available
        print("total loss is: " + str(round(loss_total, 2)))
        mc.display_screen("Calculation")
```

## PyMotorCAD Documentation Example

(Used for the PyMotorCAD Documentation Examples only)

```
try:
    from setup_scripts.setup_script import run_emag_demo
except ImportError:
    pass
else:
    run_emag_demo(mc)
mc.set_variable("MessageDisplayState", 0)
```

Out:

```
1:32:47 PM : Warning: Licences for different machine types are checked out.
You may wish to review your licence configuration.
1:32:52 PM : Loaded script file: C:\actions_runner_docs\_work\pymotorcad\pymotorcad\exa
1:32:54 PM : Python script output: Shaft speed is too high. Resetting to 500
1:32:59 PM : FEA Calculation Time: 2 Seconds
1:32:59 PM : Warning: Operating point outside voltage limit. Check the DC bus voltage.
1:32:59 PM : Solving completed
1:32:59 PM : Python script output: total loss is: 137.91
Shaft speed:500
```

<span id="page-1-0"></span>Total running time of the script: (0 minutes 26.157 seconds)

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Last updated on April 15, 2026