---
type: motorcad_api
method_group: "E-magnetic"
module: "ansys.motorcad.core"
source_files: ["E-magnetic — pymotorcad-core.md"]
confidence: Verified
---

# E-Magnetic Methods (Example)

This page documents the E-magnetic internal scripting example from the PyMotorCAD docs.

## Internal Script Pattern

```python
import ansys.motorcad.core as pymotorcad
mc = pymotorcad.MotorCAD()
mc.set_variable("MessageDisplayState", 2)

def main():
    pass

class emagnetic:
    def initial(self):
        mc.display_screen("Scripting")
        shaft_speed = mc.get_variable("ShaftSpeed")
        if shaft_speed > 1000:
            mc.set_variable("ShaftSpeed", 500)
    def final(self):
        loss_total = mc.get_variable("loss_total")
        print("total loss is: " + str(round(loss_total, 2)))
        mc.display_screen("Calculation")
```

## Key Variables Used

- `ShaftSpeed` — Shaft speed in RPM
- `loss_total` — Total loss output
- `MessageDisplayState` — Popup message control (2 = suppress)

## Related Pages

- [[motorcad/api/calculations-methods]] — `do_magnetic_calculation()`
- [[motorcad/api/general-methods]] — General methods
- [[motorcad/workflows/e-magnetic-calculation]] — E-magnetic workflow
