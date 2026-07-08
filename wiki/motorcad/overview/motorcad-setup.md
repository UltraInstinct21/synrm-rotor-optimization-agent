---
type: motorcad_overview
title: "Motor-CAD Setup for Automation"
description: "Registering Motor-CAD, finding parameter names, GUI in automation, and units"
confidence: Verified
source_files: ["Motor-CAD setup — pymotorcad-core.md"]
---

# Motor-CAD Setup for Automation

## Registering Motor-CAD

Before scripting, verify registration: **Defaults → Automation → Update to current version**.

PyMotorCAD creates and runs from a new instance unless `open_new_instance=False` is specified.

## Finding Automation Parameter Names

- **Help → Automation Parameter Names** for full list
- Hover over any UI control to see its automation name in the status bar
- Press **F2** with a control focused to search for its name
- Press **Ctrl+F2** to copy the automation name of the selected control
- Naming convention: UI names with spaces → underscores (e.g., `Pole_Number`)

## GUI in Automation

By default, the GUI is hidden when Motor-CAD is launched by a script. To show it:

```python
mc.set_visible(True)
```

Best practice — show the Scripting tab before changing parameters:

```python
mc.display_screen("scripting")
```

> ⚠️ Never change a parameter displayed on the currently visible tab during automation.

## Units

Variables are always in Motor-CAD default units, regardless of the UI unit setting. See **Help → Automation Parameter Names** for default units.

## Related Pages

- [[motorcad/overview/getting-started]] — Installation and first steps
- [[motorcad/api/motorcad-api]] — MotorCAD() constructor
- [[motorcad/troubleshooting/ui-not-updated]] — UI not updating issue
