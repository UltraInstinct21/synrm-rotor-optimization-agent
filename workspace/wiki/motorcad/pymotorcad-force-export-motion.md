---
type: motorcad_api
title: PyMotorCAD - Force Export to Ansys Motion
source: PyMotorCAD Documentation
tags:
  - motorcad
  - pymotorcad
  - force
  - ansys-motion
  - export
  - mechanical
---

# PyMotorCAD - Force Export to Ansys Motion

## Overview

Export electromagnetic forces from Motor-CAD to Ansys Motion for mechanical stress and vibration analysis. Forces are exported in standard formats compatible with Ansys Motion solvers.

## Functions

### `get_electrical_periods_per_revolution()`

Returns the number of electrical periods per mechanical revolution.

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
periods = mc.get_electrical_periods_per_revolution()
print(f"Electrical periods per revolution: {periods}")
```

**Returns:** Integer value representing electrical periods per revolution.

**Use case:** Determine force waveform repetition pattern for export length.

### `get_number_force_cycles()`

Returns the number of force cycles available for export.

```python
force_cycles = mc.get_number_force_cycles()
print(f"Available force cycles: {force_cycles}")
```

**Returns:** Integer count of force cycles.

### `get_num_duplications()`

Returns the number of mechanical duplications for force export.

```python
duplications = mc.get_num_duplications()
print(f"Number of duplications: {duplications}")
```

**Returns:** Integer count of duplications.

### `mechanical_node_positions()`

Returns the mechanical node positions for force mapping.

```python
node_positions = mc.mechanical_node_positions()
print(f"Node positions: {node_positions}")
```

**Returns:** Array of node position coordinates.

## Coordinate System Conversion

### Cylindrical to Cartesian

Motor-CAD calculates forces in cylindrical coordinates (radial and tangential components). Export to Ansys Motion requires Cartesian (X/Y) coordinates.

**Transformation equations:**

```
Fx = Fr * cos(θ) - Ft * sin(θ)
Fy = Fr * sin(θ) + Ft * cos(θ)
```

Where:
- `Fr` = Radial force component
- `Ft` = Tangential force component
- `θ` = Angular position of node

## Output Files

| File Format | Description | Contents |
|-------------|-------------|----------|
| `.unv` | Universal file (load points) | Node positions and force values |
| `.amesh` | Ansys mesh file | Mesh connectivity and geometry |
| `.anf` | Ansys neutral format | Force distribution data |

## Export Workflow

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file("model.mot")

# Switch to magnetic context
mc.show_magnetic_context()

# Run electromagnetic calculation
mc.do_magnetic_calculation()

# Get export parameters
periods = mc.get_electrical_periods_per_revolution()
cycles = mc.get_number_force_cycles()
dups = mc.get_num_duplications()

# Export forces (actual method name to be verified from docs)
# mc.export_forces_to_motion(output_path)
```

## Related Pages

- [[pymotorcad-force-extraction]] - Force extraction methods
- [[pymotorcad-mechanical-force]] - Mechanical force calculations

## Tags

#motorcad #pymotorcad #force #export #ansys-motion #mechanical #vibration