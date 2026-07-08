---
type: motorcad_api
title: PyMotorCAD Setup and Configuration
source: ansys-motorcad-core documentation
tags: [motorcad, pymotorcad, setup, automation, configuration]
aliases: [pymotorcad registration, automation parameters]
---

# PyMotorCAD Setup and Configuration

## Registering for Automation

Before using PyMotorCAD, register Motor-CAD for automation access:

1. Open Motor-CAD
2. Go to **Defaults** → **Automation**
3. Click **Update to current version**

This enables the automation interface and allows external scripts to connect.

## Finding Parameter Names

Motor-CAD exposes internal variable names for scripting. To find them:

| Method | Description |
|--------|-------------|
| **Help → Automation Parameter Names** | Opens the full parameter reference |
| **F2** | Show parameter name for the active GUI field |
| **Ctrl+F2** | Copy the parameter name to clipboard |

Use these names with `get_variable()` and `set_variable()`.

## Naming Convention

Motor-CAD GUI labels contain spaces, but parameter names use **underscores**:

| GUI Label | Parameter Name |
|-----------|----------------|
| Stator Lam Dia | `Stator_Lam_Dia` |
| Shaft Dia | `Shaft_Dia` |
| Copper Slot Fill | `Copper_Slot_Fill` |
| Slot Corner Radius | `Slot_Corner_Radius` |

## GUI in Automation

You can show or hide the Motor-CAD GUI during scripting:

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()

# Show the GUI
mc.set_visible(True)

# Navigate to the scripting tab
mc.display_screen("scripting")

# Hide the GUI (runs headless)
mc.set_visible(False)
```

## Units

Always use **Motor-CAD default units** when setting variables:

| Quantity | Default Unit |
|----------|--------------|
| Length | mm |
| Angle | degrees |
| Current | A |
| Voltage | V |
| Speed | RPM |
| Torque | Nm |
| Power | W |
| Temperature | °C |

PyMotorCAD does **not** perform unit conversion. If you set `Airgap = 0.5`, Motor-CAD interprets it as 0.5 mm.

## Cross-References

- [[pymotorcad-getting-started]] — Installation and first connection
- [[pymotorcad-general-api]] — File I/O, results, and export methods
- [[pymotorcad-motorcad-api]] — Constructor parameters
- [[pymotorcad-internal-scripting]] — Internal scripting environment

## Tags

#motorcad #pymotorcad #setup #automation #units #naming-convention
