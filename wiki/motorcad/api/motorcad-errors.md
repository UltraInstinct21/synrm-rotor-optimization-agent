---
type: motorcad_api
method_name: "MotorCADError"
module: "ansys.motorcad.core"
source_files: ["Motor-CAD errors — pymotorcad-core.md"]
confidence: Verified
---

# MotorCADError

## Description

Exception raised when Motor-CAD reports an error during API calls. Replaces the old ActiveX success variable pattern.

## Usage

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core import MotorCADError

mc = pymotorcad.MotorCAD()

try:
    mc.do_magnetic_calculation()
except MotorCADError:
    print("Calculation failed")
```

## Related Pages

- [[motorcad/api/motorcad-api]] — MotorCAD constructor
- [[motorcad/overview/backwards-compatibility]] — Migration from success variable pattern
- [[motorcad/troubleshooting/troubleshooting]] — Common issues and solutions
