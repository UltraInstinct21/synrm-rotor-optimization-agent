---
type: software
name: PyMotorCAD
aliases: [ansys-motorcad-core]
topics: [motorcad, python, automation]
source_files: ["raw/pymotorcad_markdown/"]
confidence: Verified
---

# PyMotorCAD

## Overview

Python interface for Ansys Motor-CAD automation. Package: `ansys-motorcad-core`.

## Installation

```bash
pip install ansys-motorcad-core
```

Requires Motor-CAD v2023R1 or later installed locally.

## Basic Usage

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load("model.mot")
```

## Key Capabilities

- Open/close/save models
- Set/get variables
- Run electromagnetic calculations
- Run thermal analysis
- Extract results
- Parametric sweeps
- Optimization

## Related Pages

- [[motorcad/api/index]]
- [[motorcad/overview/motorcad_overview]]
