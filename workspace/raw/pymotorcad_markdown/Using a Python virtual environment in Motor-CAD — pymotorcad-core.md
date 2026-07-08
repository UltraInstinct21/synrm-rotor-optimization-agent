## Using a Python virtual environment in Motor-CAD

You can use a Python virtual environment with Motor-CAD. By default, Motor-CAD uses the Python version that comes with the Motor-CAD installation.

![](_page_0_Picture_4.jpeg)

## Create a local Python virtual environment

![](_page_1_Picture_3.jpeg)

## Note

If you are using a Python IDE, this often creates a virtual environment for you when you start a new project. In this case, you can skip the section below, which describes how to create a virtual environment from the command line.

If Python is already installed, you can check the version by running the following command in a terminal. (You can use the Windows terminal or any terminal integrated with an IDE such as Visual Studio Code or PyCharm.)

python --version

Based on the Python version, you create a virtual environment:

python -m venv virtual\_environment\_folder\_location

Activate the newly created virtual environment:

In case of Windows Powershell

.\virtual\_environment\_folder\_location\Scripts\activate.ps1

In case of Windows Command Prompt

.\virtual\_environment\_folder\_location\Scripts\activate.bat

Depending on the terminal specification, the virtual environment name might be highlighted. Use pip to install all required packages, such as ansys.motorcad.core , numpy or bezier .

pip install ansys.motorcad.core bezier numpy

In the terminal window, the preceding commands might look like this:

## Change the Python exe path in the Motor-CAD UI

Proceed to change the path for the Python exe in Defaults -> Default File Locations. This should point to the pythonw.exe file in the Scripts folder of the virtual environment:

![](_page_3_Figure_2.jpeg)

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Last updated on April 15, 2026