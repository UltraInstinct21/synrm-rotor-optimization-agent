---
type: motorcad_workflow
name: "Thermal Steady-State Analysis"
purpose: "Run steady-state thermal calculations with custom resistances"
prerequisites: ["Motor-CAD template loaded"]
source_files: ["Thermal steady-state — pymotorcad-core.md"]
confidence: Verified
---

# Thermal Steady-State Analysis

## Purpose

Run thermal steady-state calculations with the ability to modify resistances between nodes during the iterative solve.

## Step-by-Step Procedure

### Internal Script Pattern

```python
class thermal_steady:
    housing_node = 1
    ambient_node = 0

    def initial(self):
        mc.set_variable("MessageDisplayState", 2)
        mc.display_screen("Scripting")
        mc.set_variable("Armature_Copper_Loss_@Ref_Speed", 200)

    def main(self):
        # Called each iteration
        ambient_temp = mc.get_variable("T_Ambient")
        resistance = (ambient_temp * 0.01) + 1
        mc.set_resistance_value(
            "Custom Resistance", self.ambient_node, self.housing_node, resistance, ""
        )

    def final(self):
        housing_temp = mc.get_node_temperature(self.housing_node)
        print("Housing Temperature: " + str(round(housing_temp, 1)))
        mc.set_variable("MessageDisplayState", 0)
```

### External Script

```python
mc.do_steady_state_analysis()
```

## Variables to Set

| Variable | Purpose |
|----------|---------|
| `Armature_Copper_Loss_@Ref_Speed` | Copper loss at reference speed |
| `T_Ambient` | Ambient temperature |

## Outputs to Capture

- Node temperatures via `get_node_temperature(node_number)`
- Winding temperatures via `get_variable("T_[Winding_Average]")`

## Related Pages

- [[motorcad/api/calculations-methods]] — `do_steady_state_analysis()`
- [[motorcad/workflows/thermal-example-script]] — Full thermal example
- [[motorcad/workflows/thermal-transient]] — Transient variant
