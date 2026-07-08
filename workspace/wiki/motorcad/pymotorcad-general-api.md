---
type: motorcad_api
title: PyMotorCAD General API Methods
source: ansys-motorcad-core documentation
tags: [motorcad, pymotorcad, api, file-io, results, geometry, export]
aliases: [pymotorcad file operations, pymotorcad export]
---

# PyMotorCAD General API Methods

## Overview

The general API provides methods for file I/O, template management, results handling, geometry export, winding patterns, duty cycles, and reporting.

All methods are called on a `MotorCAD` instance:

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
```

---

## File I/O

### load_from_file()

Loads an existing Motor-CAD model file.

```python
mc.load_from_file(r"D:\models\SRM_1.mot")
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `file_path` | str | Full path to `.mot` file |

### save_to_file()

Saves the current model to a specified path.

```python
mc.save_to_file(r"D:\models\SRM_1_backup.mot")
```

### download_mot_file()

Downloads the current model from the Motor-CAD instance to a local file.

```python
mc.download_mot_file(r"D:\local_copy.mot")
```

### upload_mot_file()

Uploads a local `.mot` file to the Motor-CAD instance.

```python
mc.upload_mot_file(r"D:\local_copy.mot")
```

---

## Templates

### load_template()

Loads a Motor-CAD template as the base for a new model.

```python
mc.load_template("SynRM")
```

### save_template()

Saves the current model configuration as a reusable template.

```python
mc.save_template("MySynRM_Template")
```

---

## Results

### load_results()

Loads previously saved calculation results.

```python
mc.load_results(r"D:\results\run_001.mot")
```

### save_results()

Saves current calculation results to a file.

```python
mc.save_results(r"D:\results\run_001_results.mot")
```

### export_results()

Exports results to an external format (CSV, etc.).

```python
mc.export_results(r"D:\results\run_001.csv")
```

---

## Geometry

### geometry_export()

Exports motor geometry to a file (DXF, SVG, etc.).

```python
mc.geometry_export(r"D:\geometry\motor_cross_section.dxf")
```

### load_dxf_file()

Imports a DXF geometry file into Motor-CAD.

```python
mc.load_dxf_file(r"D:\geometry\custom_rotor.dxf")
```

---

## Winding

### load_winding_pattern()

Loads a winding pattern from file.

```python
mc.load_winding_pattern(r"D:\winding\48slot_4pole.wnd")
```

### save_winding_pattern()

Saves the current winding pattern.

```python
mc.save_winding_pattern(r"D:\winding\my_pattern.wnd")
```

---

## Duty Cycle

### clear_duty_cycle()

Clears all duty cycle points.

```python
mc.clear_duty_cycle()
```

### load_duty_cycle()

Loads a duty cycle profile from file.

```python
mc.load_duty_cycle(r"D:\duty\drive_cycle.csv")
```

### save_duty_cycle()

Saves the current duty cycle profile.

```python
mc.save_duty_cycle(r"D:\duty\my_cycle.csv")
```

---

## Export

### create_report()

Generates a report from the current model and results.

```python
mc.create_report(r"D:\reports\design_report.pdf")
```

### export_to_ansys_discovery()

Exports the model to Ansys Discovery for 3D visualization.

```python
mc.export_to_ansys_discovery()
```

### export_to_ansys_electronics_desktop()

Exports the model to Ansys Electronics Desktop for FEA.

```python
mc.export_to_ansys_electronics_desktop()
```

---

## Messages

### get_messages()

Retrieves messages from the Motor-CAD message log.

```python
messages = mc.get_messages()
print(messages)
```

### clear_message_log()

Clears the message log.

```python
mc.clear_message_log()
```

---

## Control

### quit()

Closes the Motor-CAD instance.

```python
mc.quit()
```

### set_free()

Releases the Motor-CAD instance for manual GUI interaction.

```python
mc.set_free()
```

---

## Cross-References

- [[pymotorcad-motorcad-api]] — Constructor and connection parameters
- [[pymotorcad-setup]] — Registration, parameter names, units
- [[pymotorcad-compatibility-api]] — Legacy ActiveX compatibility
- [[pymotorcad-internal-scripting]] — Internal scripting and hooks

## Tags

#motorcad #pymotorcad #api #file-io #results #geometry #export #winding #duty-cycle
