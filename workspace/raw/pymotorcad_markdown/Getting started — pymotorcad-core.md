# Getting started

PyMotorCAD provides access to Ansys Motor-CAD via Python.

To run PyMotorCAD, there must be a licensed copy of Motor-CAD v2023R1 or later installed locally.

For more information on Motor-CAD, see the Ansys [Motor-CAD](https://www.ansys.com/products/electronics/ansys-motor-cad) page on the Ansys website.

PyMotorCAD is installed with Motor-CAD v2023R1 and later for internal Motor-CAD Scripting tab use. To install PyMotorCAD for use outside of Motor-CAD, it may be downloaded from GitHub. PyMotorCAD is available for install via pip in the near future.

## Installation

### Python module

The ansys.motorcad.core package currently supports Python 3.9 through Python 3.14 on Windows.

Install the latest release from [PyPi](https://pypi.org/project/ansys-motorcad-core/) with:

```
pip install ansys-motorcad-core
```

Alternatively, install the latest from [PyMotorCAD](https://github.com/ansys/pymotorcad) GitHub via:

```
pip install git+https://github.com/ansys/pymotorcad.git
```

For a local development version, install with:

```
git clone https://github.com/ansys/pymotorcad.git
cd pymotorcad
pip install -e .
```

This allows you to install the ansys-motorcad-core module, modify it locally and have the changes reflected in your setup after restarting the Python kernel.

## Ansys software requirements

For the latest features, you must have a copy of Ansys Motor-CAD v2023R1 installed locally.

For more information, see Install [Motor-CAD](https://motorcad.docs.pyansys.com/version/stable/getting_started/running_motorcad.html#install-motorcad).

#### Verify your installation

Check that Motor-CAD can be started from Python by running:

```
>>> import ansys.motorcad.core as pymotorcad
>>> mcApp = pymotorcad.MotorCAD()
```

If successful, a Motor-CAD instance is launched, appearing on the taskbar. You are now ready to start using Motor-CAD with PyMotorCAD. For more information on the PyMotorCAD interface, see the [User](https://motorcad.docs.pyansys.com/version/stable/user_guide/index.html#ref-user-guide) [guide.](https://motorcad.docs.pyansys.com/version/stable/user_guide/index.html#ref-user-guide)

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026