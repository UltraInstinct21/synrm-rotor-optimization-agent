---
type: motorcad_api
title: PyMotorCAD Internal Scripting
source: ansys-motorcad-core documentation
tags: [motorcad, pymotorcad, scripting, hooks, internal]
aliases: [motorcad internal python, motorcad hooks]
---

# PyMotorCAD Internal Scripting

## Overview

Motor-CAD includes an **internal Python scripting environment** accessible from the GUI. Scripts written here execute within the Motor-CAD process itself, without requiring an external Python installation.

## main() Function

Internal scripts must define a `main()` function. Motor-CAD calls `main()` when you click **Run**:

```python
def main():
    # Your automation code here
    mc.set_variable("Shaft_Speed_[RPM]", 3000)
    mc.do_magnetic_calculation()
    torque = mc.get_variable("ShaftTorque")
    print(f"Shaft Torque: {torque} Nm")
```

## Disabling Popups

Set `MessageDisplayState` to suppress modal dialogs during automation:

```python
mc.set_variable("MessageDisplayState", 2)  # Disable all popups
```

| Value | Behavior |
|-------|----------|
| 0 | Show all messages (default) |
| 1 | Show errors only |
| 2 | Suppress all popups |

## Hook Classes

Motor-CAD provides hook classes that intercept specific calculation contexts. Define these classes to run custom code before, during, or after calculations.

### Available Hook Classes

| Hook Class | Context |
|------------|---------|
| `thermal_steady` | Thermal steady-state analysis |
| `thermal_transient` | Thermal transient analysis |
| `emagnetic` | Electromagnetic analysis |
| `mechanical_stress` | Mechanical stress analysis |
| `mechanical_forces` | Mechanical forces analysis |

### Lifecycle Methods

Each hook class supports three lifecycle methods:

```python
class emagnetic:
    def initial(self):
        """Called before the calculation starts."""
        pass

    def main(self):
        """Called during the calculation. Modify variables here."""
        mc.set_variable("PhaseAdvance", 45)

    def final(self):
        """Called after the calculation completes."""
        torque = mc.get_variable("ShaftTorque")
        print(f"Torque: {torque}")
```

| Method | Timing |
|--------|--------|
| `initial()` | Before calculation begins |
| `main()` | During calculation (can modify variables) |
| `final()` | After calculation completes |

### Example: EMag Hook

```python
class emagnetic:
    def initial(self):
        mc.set_variable("TorqueCalculation", True)
        mc.set_variable("TorquePointsPerCycle", 30)

    def main(self):
        pass  # Motor-CAD performs the EMag solve

    def final(self):
        torque = mc.get_variable("ShaftTorque")
        efficiency = mc.get_variable("Efficiency")
        print(f"Torque: {torque:.2f} Nm, Efficiency: {efficiency:.1f}%")
```

## Cross-References

- [[pymotorcad-getting-started]] — Installation and verification
- [[pymotorcad-setup]] — Registration and parameter names
- [[pymotorcad-emag-example]] — Electromagnetic analysis example
- [[pymotorcad-general-api]] — File I/O and export methods

## Tags

#motorcad #pymotorcad #scripting #hooks #internal #emagnetic #thermal
