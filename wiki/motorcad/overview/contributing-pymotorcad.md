---
type: motorcad_overview
title: "Contributing to PyMotorCAD"
description: "Installation modes, testing, documentation, and distribution"
confidence: Verified
source_files: ["Adding to external python and contributing — pymotorcad-core.md"]
---

# Contributing to PyMotorCAD

## Overview

PyMotorCAD uses a Python JSON-RPC interface to communicate with Motor-CAD locally or remotely via HTTP.

## User Installation

```bash
python -m pip install ansys-motorcad-core
```

## Developer Installation

```bash
git clone https://github.com/ansys/pymotorcad
cd pymotorcad
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate.bat on Windows
python -m pip install --editable .[tests,doc]
tox
```

## Testing (tox)

| Command | Purpose |
|---------|---------|
| `tox -e style` | Code style checks |
| `tox -e py` | Unit tests |
| `tox -e py-coverage` | Unit tests + coverage |
| `tox -e doc` | Documentation build |

## Documentation Build

```bash
tox -e doc
# or
make -C doc/ html
```

## Distribution

```bash
python -m build
python -m twine check dist/*
```

## Related Pages

- [[motorcad/overview/getting-started]] — User installation
