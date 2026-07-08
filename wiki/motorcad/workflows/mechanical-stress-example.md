---
type: motorcad_workflow
name: "Mechanical Stress Internal Scripting"
purpose: "Internal scripting example for mechanical stress calculation"
prerequisites: ["Motor-CAD"]
source_files: ["Mechanical stress — pymotorcad-core.md"]
confidence: Verified
---

# Mechanical Stress Internal Scripting

## Purpose

Demonstrate internal scripting for rotor mechanical stress calculation using the `mechanical_stress` class.

## Internal Script Pattern

```python
class mechanical_stress:
    def initial(self):
        mc.set_variable("MessageDisplayState", 2)
        mc.set_variable("ShaftSpeed", 1500)

    def final(self):
        yield_stress = mc.get_variable("YieldStress_RotorLam")
        max_stress = mc.get_variable("MaxStress_RotorLam")
        print("Max Stress: " + str(max_stress))
        safety_factor = yield_stress / max_stress
        print("Safety factor is: " + str(round(safety_factor, 3)))
        mc.set_variable("MessageDisplayState", 0)
```

## Key Variables

| Variable | Purpose |
|----------|---------|
| `ShaftSpeed` | Rotor speed (RPM) |
| `YieldStress_RotorLam` | Material yield stress |
| `MaxStress_RotorLam` | Calculated maximum stress |

## Related Pages

- [[motorcad/api/calculations-methods]] — do_mechanical_calculation
- [[motorcad/workflows/stress-post-processing]] — Advanced post-processing
- [[motorcad/workflows/stress-sampling-example]] — Bridge stress sampling
