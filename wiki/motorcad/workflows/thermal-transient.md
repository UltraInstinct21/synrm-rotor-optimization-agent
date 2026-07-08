---
type: motorcad_workflow
name: "Thermal Transient Analysis"
purpose: "Run transient thermal calculations with time-dependent cooling conditions"
prerequisites: ["Motor-CAD template loaded"]
source_files: ["Thermal transient — pymotorcad-core.md"]
confidence: Verified
---

# Thermal Transient Analysis

## Purpose

Run thermal transient calculations with the ability to modify cooling conditions at different time steps.

## Step-by-Step Procedure

### Internal Script Pattern

```python
class thermal_transient:
    def initial(self):
        mc.set_variable("MessageDisplayState", 2)
        mc.display_screen("Scripting")
        # Initialise cooling flow rates
        mc.set_variable("Wet_Rotor_Fluid_Volume_Flow_Rate", 0.1)
        mc.set_variable("WJ_Fluid_Volume_Flow_Rate", 0.1)

    def main(self):
        current_time = mc.get_variable("CurrentTime")
        if 1000 <= current_time < 1500:
            # Stop water jacket coolant flow
            mc.set_variable("WJ_Fluid_Volume_Flow_Rate", 0)
        else:
            # Stop rotor coolant flow
            mc.set_variable("Wet_Rotor_Fluid_Volume_Flow_Rate", 0)

    def final(self):
        print("Thermal Transient - Final")
        mc.set_variable("MessageDisplayState", 0)
```

## Variables to Set

| Variable | Purpose |
|----------|---------|
| `Wet_Rotor_Fluid_Volume_Flow_Rate` | Rotor coolant flow rate |
| `WJ_Fluid_Volume_Flow_Rate` | Water jacket flow rate |
| `CurrentTime` | Current simulation time (read-only) |

## Key Pattern

The `main()` method is called at each time step. Use `get_variable("CurrentTime")` to check the current time and modify conditions accordingly.

## Related Pages

- [[motorcad/workflows/thermal-steady-state]] — Steady-state variant
- [[motorcad/workflows/thermal-example-script]] — Full thermal analysis script
- [[motorcad/api/calculations-methods]] — `do_transient_analysis()`
