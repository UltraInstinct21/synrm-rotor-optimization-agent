---
type: pymotorcad_api
title: "PyMotorCAD Geometry Basic API"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - geometry
  - winding
  - coil
  - validation
  - api
aliases:
  - pymotorcad_geometry
  - motorcad_geometry_basic
related_pages:
  - "[[pymotorcad-geometry-objects]]"
  - "[[pymotorcad-geometry-tree]]"
  - "[[pymotorcad-adaptive-geometry]]"
  - "[[pymotorcad-calculations-api]]"
confidence: verified
---

# PyMotorCAD Geometry Basic API

## Overview

The Geometry Basic API provides fundamental methods for geometry validation and winding/coil data access in Motor-CAD. These methods handle geometry integrity checks and coil configuration — essential prerequisites before any electromagnetic calculation can run.

---

## Geometry Validation

### `check_if_geometry_is_valid()`

#### Purpose

Validates the current motor geometry for geometric consistency, detecting overlapping regions, invalid dimensions, or structural issues that would prevent a valid FEA mesh or magnetic solution.

#### Signature

```python
check_if_geometry_is_valid() -> bool
```

#### Returns

| Return | Type | Description |
|---|---|---|
| `bool` | `True` if geometry is valid, `False` if errors are detected |

#### Description

This method performs a comprehensive geometry validation including:

- **Dimensional consistency**: All geometric parameters produce a valid cross-section
- **Region overlap**: No two geometric regions overlap inappropriately
- **Bridge integrity**: Rotor bridges and ribs are within manufacturable limits
- **Airgap validity**: Airgap dimension is positive and reasonable
- **Shaft clearance**: Rotor interior geometry does not intersect the shaft
- **Slot geometry**: Slot dimensions are physically realizable
- **Barrier geometry**: Barrier shapes are valid (for SynRM/PMaSynRM)

#### Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Validate geometry before calculation
is_valid = mc.check_if_geometry_is_valid()

if is_valid:
    print("Geometry is valid — proceeding with calculation")
    mc.do_magnetic_calculation()
else:
    print("Geometry has errors — check parameters")
    # Common issues to investigate:
    # - Barriers too close to shaft or rotor OD
    # - Bridges thinner than minimum
    # - Slot dimensions conflicting
    # - Airgap too small
```

#### Validation Checks Detail

| Check | Description | Common Failure |
|---|---|---|
| Airgap positive | `Airgap > 0` | Airgap set to 0 or negative |
| Shaft clearance | Rotor bore > shaft diameter | Shaft too large for rotor |
| Barrier nesting | Inner barriers contained within outer | Barrier diameters incorrectly ordered |
| Bridge minimum | `Bridge_Thickness >= 1 mm` | Bridge too thin for manufacturing |
| Slot depth | `Slot_Depth > 0` | Slot parameters inconsistent |
| Stator bore < OD | `Stator_bore < Stator_Lam_Dia` | OD and bore swapped |
| Rotor OD < Stator bore | `Rotor_Diameter < Stator_bore` | Rotor intersects stator |

#### Defensive Pattern

```python
def validate_and_run(mc, max_retries=3):
    """Validate geometry and run calculation with retry logic."""
    for attempt in range(max_retries):
        if mc.check_if_geometry_is_valid():
            mc.do_magnetic_calculation()
            return True
        else:
            print(f"Geometry invalid on attempt {attempt + 1}")
            # Log or inspect parameters
    raise RuntimeError("Geometry validation failed after max retries")
```

---

## Winding and Coil Data

### `get_winding_coil()`

#### Purpose

Retrieves the coil data for a specified coil (phase group), including turns, conductors, coil span, and winding factor information.

#### Signature

```python
get_winding_coil(coil_index: int) -> dict
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `coil_index` | `int` | Index of the coil to retrieve (1-based) |

#### Returns

A dictionary containing coil data:

| Key | Type | Description |
|---|---|---|
| `turns` | `int` | Number of series turns per coil |
| `conductors` | `int` | Number of conductors per slot |
| `coil_pitch` | `int` | Coil span in slot pitches |
| `winding_factor` | `float` | Winding factor for this coil group |
| `parallel_paths` | `int` | Number of parallel current paths |
| `layer` | `int` | Winding layer (for double-layer windings) |

#### Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Get coil data for coil group 1
coil_1 = mc.get_winding_coil(1)
print(f"Turns: {coil_1['turns']}")
print(f"Conductors per slot: {coil_1['conductors']}")
print(f"Coil pitch: {coil_1['coil_pitch']} slots")
print(f"Winding factor: {coil_1['winding_factor']:.4f}")

# Iterate through all coils
num_coils = mc.get_variable("Coil_Groups")
for i in range(1, num_coils + 1):
    coil = mc.get_winding_coil(i)
    print(f"Coil {i}: {coil['turns']} turns, "
          f"pitch {coil['coil_pitch']}, "
          f"kW = {coil['winding_factor']:.4f}")
```

#### Use Cases

- Verifying winding configuration before EMag calculation
- Auditing conductor count for thermal limit compliance
- Checking winding factors for harmonic reduction
- Validating coil pitch for optimal torque production

---

### `set_winding_coil()`

#### Purpose

Sets the coil data for a specified coil (phase group), modifying turns, conductors, or coil span.

#### Signature

```python
set_winding_coil(coil_index: int, coil_data: dict) -> None
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `coil_index` | `int` | Index of the coil to modify (1-based) |
| `coil_data` | `dict` | Dictionary of coil parameters to set |

#### Supported Dictionary Keys

| Key | Type | Description |
|---|---|---|
| `turns` | `int` | Number of series turns |
| `conductors` | `int` | Number of conductors per slot |
| `coil_pitch` | `int` | Coil span in slot pitches |
| `parallel_paths` | `int` | Number of parallel paths |

#### Example

```python
# Modify coil 1: increase turns from 22 to 26
mc.set_winding_coil(1, {"turns": 26})

# Modify coil pitch for coil group 1
mc.set_winding_coil(1, {"coil_pitch": 10})

# Set multiple parameters at once
mc.set_winding_coil(1, {
    "turns": 24,
    "conductors": 48,
    "coil_pitch": 11,
    "parallel_paths": 2
})

# After modifying, regenerate winding pattern
mc.create_winding_pattern()
```

#### Prerequisites

- Model must be loaded
- Coil index must be valid (within the number of coil groups defined)
- Winding type must support the modification (e.g., distributed vs. concentrated)

#### Validation After Modification

```python
# Modify winding
mc.set_winding_coil(1, {"turns": 26})
mc.create_winding_pattern()

# Validate geometry (winding changes can affect slot fill)
is_valid = mc.check_if_geometry_is_valid()
if not is_valid:
    print("Winding modification caused geometry error — reverting")
    mc.set_winding_coil(1, {"turns": 22})
    mc.create_winding_pattern()
```

---

## Winding Configuration Overview

Motor-CAD supports several winding types. Understanding the coil data structure depends on the winding configuration:

### Distributed Windings

- Multiple coils per phase per pole
- Coil pitch typically接近 but not equal to pole pitch
- Used in: standard AC motors, SynRM, IPMSM

### Concentrated (Tooth-Coil) Windings

- One coil per tooth
- Coil pitch = 1 slot
- Used in: some BLDC, PMSM, high-slot-fill designs

### Fractional-Slot Windings

- Slot count not an integer multiple of pole count
- Produces sub-harmonics and higher harmonics
- Used in: PMSM for torque ripple reduction

---

## Coil Data and EMag Calculation

The coil data directly affects:

| Parameter | Effect of Coil Changes |
|---|---|
| **Turns** | Linearly affects flux linkage and inductance |
| **Conductors** | Affects slot fill factor and copper loss |
| **Coil pitch** | Affects winding factor and harmonic spectrum |
| **Parallel paths** | Affects current per path and resistance |

### Relationship to Key Outputs

```
Flux Linkage ∝ Turns × Winding Factor × Flux per pole
Torque ∝ Turns × Current × Winding Factor × Flux
Copper Loss ∝ (Turns × Current)² × Resistance
Slot Fill = (Turns × Conductor Area) / Slot Area
```

---

## Common Winding Parameters

| Parameter | MotorCAD Variable | Description |
|---|---|---|
| Series turns | `Series_Turns` | Total series turns per phase |
| Coil pitch | `Coil_Pitch` | Coil span in slot pitches |
| Slot number | `Slot_Number` | Total number of stator slots |
| Pole number | `Pole_Number` | Number of magnetic poles |
| Parallel paths | `Parallel_Paths` | Number of parallel current paths |
| Coil groups | `Coil_Groups` | Number of coil groups per phase |
| Winding factor | `Winding_Factor` | Fundamental winding factor |
| Slot fill factor | `Copper_Slot_Fill` | Copper-to-slot area ratio |
| Wire diameter | `WireDiameter` | Conductor wire diameter |

---

## Complete Workflow: Winding Setup and Validation

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# 1. Check current winding configuration
num_coils = mc.get_variable("Coil_Groups")
print(f"Number of coil groups: {num_coils}")

for i in range(1, num_coils + 1):
    coil = mc.get_winding_coil(i)
    print(f"Coil {i}: turns={coil['turns']}, "
          f"pitch={coil['coil_pitch']}, "
          f"kW={coil['winding_factor']:.4f}")

# 2. Modify winding (example: increase turns for higher torque)
mc.set_winding_coil(1, {"turns": 26})
mc.create_winding_pattern()

# 3. Validate geometry
if not mc.check_if_geometry_is_valid():
    print("ERROR: Winding modification invalid — reverting")
    mc.set_winding_coil(1, {"turns": 22})
    mc.create_winding_pattern()

# 4. Run EMag with modified winding
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)

mc.do_magnetic_calculation()

torque = mc.get_variable("ShaftTorque")
print(f"Torque with modified winding: {torque:.2f} Nm")
```

---

## Cross-References

- [[pymotorcad-geometry-objects]] — Advanced geometry object manipulation
- [[pymotorcad-geometry-tree]] — Tree-based geometry construction (v2026R1+)
- [[pymotorcad-adaptive-geometry]] — Adaptive mesh and geometry refinement
- [[pymotorcad-calculations-api]] — Calculation methods that depend on geometry
- [[pymotorcad-emag-example]] — Complete EMag workflow including winding setup

---

## Tags

#pymotorcad #motorcad #api #geometry #winding #coil #validation #distributed-winding #concentrated-winding #slot-fill
