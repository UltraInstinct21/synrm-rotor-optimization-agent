---
type: motorcad_overview
title: "Using a Python Virtual Environment in Motor-CAD"
description: "Setting up and using a Python virtual environment with Motor-CAD"
confidence: Verified
source_files: ["Using a Python virtual environment in Motor-CAD — pymotorcad-core.md"]
---

# Using a Python Virtual Environment in Motor-CAD

Motor-CAD defaults to the Python bundled with its installation. A virtual environment can be used instead.

## Create Virtual Environment

```bash
python -m venv virtual_environment_folder_location
```

### Activate

**PowerShell:**
```powershell
.\virtual_environment_folder_location\Scripts\activate.ps1
```

**Command Prompt:**
```cmd
.\virtual_environment_folder_location\Scripts\activate.bat
```

### Install packages

```bash
pip install ansys.motorcad.core numpy bezier
```

## Configure Motor-CAD

Go to **Defaults → Default File Locations** and set the Python executable path to `pythonw.exe` in the virtual environment's `Scripts` folder.

## Related Pages

- [[motorcad/overview/getting-started]] — Basic installation
- [[motorcad/overview/motorcad-setup]] — Motor-CAD UI configuration
