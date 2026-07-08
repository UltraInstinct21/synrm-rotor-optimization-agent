## MotorCAD API

*class* **MotorCAD(***port=-1***,** *open\_new\_instance=True***,** *enable\_exceptions=True***,** *enable\_success\_variable=False***,** *reuse\_parallel\_instances=False***,** *keep\_instance\_open=False***,** *url=''***,** *use\_blackbox\_licence=None***)**

<span id="page-0-0"></span>Connect to an existing Motor-CAD instance or open a new instance.

## Parameters:

port : [int](https://docs.python.org/dev/library/functions.html#int) , default: -1

Port to use for communication.

open\_new\_instance : Boolean , default: [True](https://docs.python.org/dev/library/constants.html#True)

Open a new instance or try to connect to an existing instance.

enable\_exceptions : Boolean , default: [True](https://docs.python.org/dev/library/constants.html#True)

Whether to show Motor-CAD communication errors as Python exceptions.

enable\_success\_variable : Boolean , default: [False](https://docs.python.org/dev/library/constants.html#False)

Whether Motor-CAD methods return a success variable (first object in tuple).

reuse\_parallel\_instances : Boolean , default: [False](https://docs.python.org/dev/library/constants.html#False)

Whether to reuse Motor-CAD instances when running in parallel. You must free instances after use.

keep\_instance\_open : Boolean , default: [False](https://docs.python.org/dev/library/constants.html#False)

Whether to keep the Motor-CAD instance open after the instance becomes free.

url: string, default = ""

Full url for Motor-CAD connection. Assumes we are connecting to existing instance.

use\_blackbox\_licence: Boolean, default: None

Ask Motor-CAD to consume blackbox licence. If set to None, existing Motor-CAD behaviour will be used.

## Returns:

[MotorCAD](#page-0-0) object.