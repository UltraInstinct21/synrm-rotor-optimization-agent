---
type: motorcad_api
title: PyMotorCAD Getting Started
source: ansys-motorcad-core documentation
tags: [motorcad, pymotorcad, setup, python, getting-started]
aliases: [pymotorcad installation, ansys motorcad python]
---

# PyMotorCAD Getting Started

## Overview

**PyMotorCAD** is the official Python API for Ansys Motor-CAD, enabling scriptable access to motor design, electromagnetic, thermal, and mechanical simulations.

- **Package**: `ansys.motorcad.core`
- **Python versions**: 3.9 – 3.14 (Windows only)
- **Motor-CAD requirement**: v2023R1 or later

## Installation

```bash
pip install ansys-motorcad-core
```

## Verification

```python
import ansys.motorcad.core as pymotorcad

mcApp = pymotorcad.MotorCAD()
```

This launches a Motor-CAD instance and returns a connection object.

## Next Steps

- [[pymotorcad-setup]] — Register for automation, find parameter names, understand naming conventions
- [[pymotorcad-motorcad-api]] — Constructor parameters and connection options
- [[pymotorcad-general-api]] — File I/O, results, geometry, and export methods
- [[pymotorcad-internal-scripting]] — Internal Python scripting environment and hooks

## Tags

#motorcad #pymotorcad #python #getting-started #setup
