---
type: motorcad_api
method_name: "MotorCADCompatibility()"
module: "ansys.motorcad.core"
source_files: ["MotorCADCompatibility API — pymotorcad-core.md", "Backwards compatibility with old scripts — pymotorcad-core.md"]
confidence: Verified
---

# MotorCADCompatibility API

## Signature

```python
MotorCADCompatibility(port=-1, ...)
```

## Description

Creates a MotorCAD object that behaves the same as old ActiveX methods. Used for backwards compatibility when converting old scripts.

## Usage

```python
import ansys.motorcad.core as pymotorcad
mcApp = pymotorcad.MotorCADCompatibility()
```

Some new PyMotorCAD features are disabled to ensure compatibility with older scripts.

## Related Pages

- [[motorcad/api/motorcad-api]] — Full MotorCAD constructor with all options
- [[motorcad/overview/backwards-compatibility]] — Migration guide from ActiveX
