---
type: motorcad_overview
title: "Getting Started with PyMotorCAD"
description: "Installation, requirements, and first steps with PyMotorCAD"
confidence: Verified
source_files: ["Getting started — pymotorcad-core.md"]
---

# Getting Started with PyMotorCAD

## Overview

PyMotorCAD provides Python access to Ansys Motor-CAD. Requires a licensed copy of Motor-CAD v2023R1 or later installed locally.

## Installation

### From PyPI (recommended)
```bash
pip install ansys-motorcad-core
```

### From GitHub (latest development)
```bash
pip install git+https://github.com/ansys/pymotorcad.git
```

### Local development
```bash
git clone https://github.com/ansys/pymotorcad.git
cd pymotorcad
pip install -e .
```

## Requirements

- Python 3.9 through 3.14 (Windows only)
- Ansys Motor-CAD v2023R1 or later

## Verify Installation

```python
import ansys.motorcad.core as pymotorcad
mcApp = pymotorcad.MotorCAD()
```

A Motor-CAD instance should appear on the taskbar.

## Related Pages

- [[motorcad/overview/motorcad-setup]] — Motor-CAD UI setup and registration
- [[motorcad/api/motorcad-api]] — MotorCAD() constructor reference
- [[motorcad/overview/backwards-compatibility]] — Converting old ActiveX scripts
- [[motorcad/overview/python-virtual-environment]] — Using virtual environments
