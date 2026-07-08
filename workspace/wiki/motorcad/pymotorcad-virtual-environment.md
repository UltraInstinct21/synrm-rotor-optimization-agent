---
type: motorcad_setup
title: "PyMotorCAD Virtual Environment Configuration"
source: "PyMotorCAD Documentation"
tags:
  - motorcad
  - pymotorcad
  - setup
  - python
  - venv
  - configuration
aliases:
  - "MotorCAD Python venv"
  - "MotorCAD virtual environment"
---

# PyMotorCAD Virtual Environment Configuration

## Overview

Motor-CAD can be configured to use a **custom Python virtual environment** instead of its bundled Python interpreter. This is essential when your motor design workflows require third-party packages beyond those pre-installed in Motor-CAD's default environment.

Custom venvs are useful for:

- Project-specific package versions (NumPy, SciPy, Matplotlib, etc.)
- Reproducible environments across workstations
- Isolating conflicting package versions
- Including proprietary or internal packages
- Ensuring dependency consistency across team members

---

## Prerequisites

- Motor-CAD installed and licensed
- Python 3.x installed on the system (3.9+ recommended)
- PyMotorCAD package (`ansys-motorcad-core`)

---

## Step 1 — Create the Virtual Environment

Open a terminal (PowerShell or Command Prompt) and navigate to your working directory.

```powershell
cd D:\SRM\Motor _CAD
python -m venv .venv
```

This creates a `.venv` folder containing an isolated Python interpreter and `pip`.

---

## Step 2 — Activate the Virtual Environment

**PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Command Prompt:**

```cmd
.\.venv\Scripts\activate.bat
```

After activation, the terminal prompt will show the active environment name.

---

## Step 3 — Install Required Packages

With the venv active, install PyMotorCAD and any additional packages your workflow requires:

```powershell
pip install ansys-motorcad-core
pip install numpy scipy matplotlib pandas
```

Verify installation:

```powershell
pip list
```

Confirm `ansys-motorcad-core` appears in the output.

---

## Step 4 — Locate the Python Executable

The full path to the Python executable inside the venv is:

```
D:\SRM\Motor _CAD\.venv\Scripts\python.exe
```

This is the path you will enter into Motor-CAD.

---

## Step 5 — Configure Motor-CAD to Use the Custom Python Executable

1. Open Motor-CAD
2. Navigate to **Defaults** → **Default File Locations**
3. Locate the **Python exe** field
4. Paste the full path to the venv Python executable:

```
D:\SRM\Motor _CAD\.venv\Scripts\python.exe
```

5. Click **OK** or **Apply**
6. Restart Motor-CAD for the change to take effect

---

## Step 6 — Verify the Configuration

In Motor-CAD, open the **Scripting** tab and run a minimal test:

```python
import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)
import ansys.motorcad.core
print("PyMotorCAD version:", ansys.motorcad.core.__version__)
```

The output should confirm the custom venv path and the installed PyMotorCAD version.

---

## Package Management

With the venv configured, all `pip install` operations target the isolated environment. To freeze the environment for reproducibility:

```powershell
pip freeze > requirements.txt
```

To recreate the environment on another machine:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Troubleshooting

### Motor-CAD still uses its bundled Python

- Verify the path in **Defaults** → **Default File Locations** → **Python exe**
- Confirm the path points to `python.exe` inside the `.venv`, not the system Python
- Restart Motor-CAD after changing the setting

### Packages not found at runtime

- Ensure packages were installed into the venv, not the global Python
- Verify `pip list` inside the activated venv shows the expected packages
- Check `sys.executable` output in the Motor-CAD scripting tab to confirm the correct interpreter is active

### Import errors for ansys.motorcad.core

- Confirm `ansys-motorcad-core` is installed in the target venv
- Check that the Motor-CAD executable version matches the PyMotorCAD version
- Review the Motor-CAD scripting console for full traceback details

---

## Related Pages

- [[pymotorcad-getting-started]] — First steps with PyMotorCAD
- [[pymotorcad-setup]] — General PyMotorCAD setup and installation
- [[pymotorcad-contributing]] — Contributing to the PyMotorCAD project
- [[motorcad_api/index]] — PyMotorCAD API reference
