# Adding to external python and contributing PyMotorCAD

![](_page_0_Figure_3.jpeg)

## Overview

Ansys Motor-CAD is a dedicated design and analysis tool for electric motors. It enables rapid and accurate multiphysics design and analysis of electric machines across the full-operating spectrum.

PyMotorCAD uses a Python JSON-RPC (remote procedure call) interface for Motor-CAD to launch or connect with a Motor-CAD instance, either locally or from a remote machine via HTTP. With PyMotorCAD, you can programmatically create, interact with, and control a Motor-CAD model, with or without using the Motor-CAD GUI.

# <span id="page-0-0"></span>Documentation and issues [#](#page-0-0)

Documentation for the latest stable release of PyMotorCAD is hosted at PyMotorCAD [documentation](https://motorcad.docs.pyansys.com/version/stable/).

In the upper right corner of the documentation's title bar, there is an option for switching from viewing the documentation for the latest stable release to viewing the documentation for the development version or previously released versions.

You can also [view](https://cheatsheets.docs.pyansys.com/pymotorcad_cheat_sheet.png) or [download](https://cheatsheets.docs.pyansys.com/pymotorcad_cheat_sheet.pdf) the PyMotorCAD cheat sheet. This one-page reference provides syntax rules and commands for using PyMotorCAD.

On the [PyMotorCAD](https://github.com/ansys/pymotorcad/issues) Issues page, you can create issues to report bugs and request new features. On the [Discussions](https://discuss.ansys.com/) page on the Ansys Developer portal, you can post questions, share ideas, and get community feedback.

To reach the project support team, email [pyansys.core@ansys.com.](mailto:pyansys.core%40ansys.com)

## Installation

PyMotorCAD has two installation modes: user and developer.

#### Install in user mode

Before installing PyMotorCAD in user mode, run this command to ensure that you have the latest version of [pip](https://pypi.org/project/pip/):

```
python -m pip install -U pip
```

Then, run this command to install PyMotorCAD:

```
python -m pip install ansys-motorcad-core
```

#### Install in developer mode

Installing PyMotorCAD in developer mode allows you to modify the source and enhance it.

Note: Before contributing to this project, ensure that you are familiar with all guidelines in the [PyAnsys](https://dev.docs.pyansys.com/) [Developer's](https://dev.docs.pyansys.com/) Guide.

To install in developer mode, complete these steps:

1. Clone the pymotorcad repository with this command:

```
git clone https://github.com/ansys/pymotorcad
cd pymotorcad
```

2. Create a fresh-clean Python environment and then activate it with these commands:

```
# Create a virtual environment
python -m venv .venv
# Activate it in a POSIX system
source .venv/bin/activate
# Activate it in Windows CMD environment
.venv\Scripts\activate.bat
# Activate it in Windows Powershell
.venv\Scripts\Activate.ps1
```

3. Ensure that you have the latest required build system and documentation, testing, and CI tools with this command:

```
python -m pip install -U pip tox
```

4. Install the project in editable mode with this command:

```
python -m pip install --editable .[tests,doc]
```

5. Verify your development installation with this command:

```
tox
```

## Testing

This project takes advantage of [tox.](https://tox.wiki/) This tool allows you to automate common development tasks (similar to Makefile), but it is oriented towards Python development.

While Makefile has rules, tox has environments. In fact, tox creates its own virtual environment to guarantee the project's integrity by isolating anything being tested.

![](_page_2_Picture_12.jpeg)

Here are commands for running various checks in the tox environment:

- tox -e style: Checks for coding style quality.
- tox -e py: Checks for unit tests.
- tox -e py-coverage: Checks for unit testing and code coverage.
- tox -e doc: Checks for the documentation-building process.

#### Raw testing

If required, you can call style commands, such as [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort), and [flake8,](https://flake8.pycqa.org/en/latest/) or unit testing commands, such as`pytest`\_, from the command line. However, using these commands does not guarantee that your project is being tested in an isolated environment, which is why tools like [tox](https://tox.wiki/) exist.

# Style checks

The style checks take advantage of [pre-commit](https://pre-commit.com/). Developers are not forced but encouraged to install this tool by running this command:

python -m pip install pre-commit && pre-commit install

## Documentation builds

To build documentation, you can run the usual rules provided in the [Sphinx](https://www.sphinx-doc.org/en/master/) Makefile with a command like this:

make -C doc/ html && your\_browser\_name doc/html/index.html

However, the recommended way of checking documentation integrity is to use a tox command like this:

tox -e doc && your\_browser\_name .tox/doc\_out/index.html

## Distribution

If you would like to create either source or wheel files, run the following commands to install the building requirements and execute the build module:

python -m pip install -U pip python -m build python -m twine check dist/\*

## License and acknowledgements

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026