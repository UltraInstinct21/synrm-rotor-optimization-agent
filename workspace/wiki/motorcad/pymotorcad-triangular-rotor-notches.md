---
type: pymotorcad_example
title: "PyMotorCAD Triangular Rotor Notches"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - triangular
  - notches
  - rotor
  - nvh
  - adaptive-geometry
  - noise
  - vibration
  - harshness
aliases:
  - triangular_rotor_notches
  - rotor_notches
motor_types: ["SynRM", "IPMSM", "SPM", "PMaSynRM"]
confidence: verified
---

# PyMotorCAD Triangular Rotor Notches

## Overview

This page documents how to create **triangular rotor notches** for NVH (Noise, Vibration, and Harshness) improvement. Triangular notches are wedge-shaped cutouts on the rotor surface that modify the airgap permeance distribution, reducing radial force harmonics that excite acoustic noise. The `triangular_notch()` function from `geometry_shapes` creates the notch geometry, which is then positioned and duplicated around the rotor.

**Template:** e9 (triangular notch template)

**Requirements:** MotorCAD v2024.1.2+ and PyMotorCAD v0.4.1+

---

## Adaptive Parameters

| Parameter | Description | Units |
|---|---|---|
| Notch Angle | Angular position of the notch centre on the rotor | mechanical degrees |
| Notch Sweep | Angular sweep (width) of the notch | mechanical degrees |
| Notch Depth | Radial depth of the notch into the rotor lamination | mm |
| Notches per Pole | Number of notch segments per pole | integer |

---

## Core Geometry Function

### `triangular_notch(radius, sweep, centre_angle, depth, region_type)`

Creates a triangular notch geometry — a wedge-shaped cut typically used for flux barrier entries or slot notch profiles.

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `radius` | `float` | Radial distance to the notch base (mm) |
| `sweep` | `float` | Angular sweep of the notch (degrees) |
| `centre_angle` | `float` | Angular centre of the notch (degrees) |
| `depth` | `float` | Radial depth of the notch (mm) |
| `region_type` | `RegionType` | Region classification |

#### Returns

A tuple of `(coordinates, entities)` representing the notch boundary.

#### Example

```python
from ansys.motorcad.core.geometry import RegionType

# Triangular notch at r=107 mm (rotor OD), 8 deg sweep, centred at 0 deg, 3 mm deep
coords, entities = mc.geometry.shapes.triangular_notch(
    radius=107.0,
    sweep=8.0,
    centre_angle=0.0,
    depth=3.0,
    region_type=RegionType.Region
)
```

---

## Region Properties

When creating a notch region, the following properties must be set:

| Property | Type | Description |
|---|---|---|
| `name` | `str` | Region name (e.g. `"Notch_Pole1_1"`) |
| `colour` | `tuple` | RGB colour tuple (0-255 per channel) |
| `duplications` | `int` | Number of symmetry duplications |
| `material` | `str` | Material name from MotorCAD library |
| `parent` | `str` | Parent region name (typically the rotor lamination) |

### Example

```python
from ansys.motorcad.core.geometry import Region, RegionType

notch = Region()
notch.name = "Notch_Pole1_1"
notch.colour = (100, 100, 255)
notch.material = "Steel_1008"
notch.duplications = 4       # 4 poles
notch.parent = "Rotor_Lam"
notch.entities = entities
```

---

## Boundary Checks

Triangular notches must satisfy geometric constraints to produce valid MotorCAD models:

### Must Not Cross Symmetry Boundary

The notch must not extend beyond the symmetry sector boundary. For a 4-pole motor with 90° symmetry:

```
notch_centre_angle + (notch_sweep / 2) < symmetry_sector_angle
notch_centre_angle - (notch_sweep / 2) > 0
```

### Must Not Overlap Other Features

The notch must not overlap with:
- Flux barriers
- Other notches on the same pole
- The shaft region
- The rotor outer diameter (notch must be within the lamination)

### Validation Check

```python
def validate_notch(radius, sweep, centre_angle, depth, rotor_od, shaft_dia, symmetry_angle):
    """Validate notch geometry constraints."""
    # Check notch doesn't exceed rotor OD
    assert radius <= rotor_od, f"Notch radius {radius} > rotor OD {rotor_od}"

    # Check notch doesn't go below shaft
    assert (radius - depth) >= shaft_dia, \
        f"Notch depth {depth} exceeds available radial space"

    # Check symmetry boundary
    half_sweep = sweep / 2
    assert (centre_angle - half_sweep) >= 0, \
        f"Notch crosses lower symmetry boundary at {centre_angle - half_sweep} deg"
    assert (centre_angle + half_sweep) <= symmetry_angle, \
        f"Notch crosses upper symmetry boundary at {centre_angle + half_sweep} deg"

    return True
```

---

## Complete Workflow

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core.geometry import Region, RegionType

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"path\to\model.mot")
mc.show_magnetic_context()
mc.reset_adaptive_geometry()

# Notch parameters
rotor_od = 214.0        # mm
notch_depth = 3.0       # mm
notch_sweep = 8.0       # deg
notches_per_pole = 2
pole_count = 4
symmetry_angle = 90.0   # deg (360 / pole_count)

# Calculate notch positions
notch_angles = []
for n in range(notches_per_pole):
    angle = (n + 1) * symmetry_angle / (notches_per_pole + 1)
    notch_angles.append(angle)

# Create notches for one pole
for i, angle in enumerate(notch_angles):
    # Create notch geometry
    coords, entities = mc.geometry.shapes.triangular_notch(
        radius=rotor_od,
        sweep=notch_sweep,
        centre_angle=angle,
        depth=notch_depth,
        region_type=RegionType.Region
    )

    # Create region
    notch_region = Region()
    notch_region.name = f"Notch_Pole1_{i + 1}"
    notch_region.colour = (100, 100, 255)
    notch_region.material = "Steel_1008"
    notch_region.duplications = pole_count
    notch_region.parent = "Rotor_Lam"
    notch_region.entities = entities

    # Set region
    mc.set_region(notch_region)

# Run EMag calculation
mc.do_magnetic_calculation()

# Compare NVH metrics
base_power = mc.get_variable("NVHRadiatedPower")
print(f"NVH radiated power with notches: {base_power:.6f} W")
```

---

## NVH Improvement Mechanism

Triangular notches improve NVH by modifying the **airgap permeance distribution**:

| Without Notches | With Notches |
|---|---|
| Uniform airgap permeance | Modulated permeance profile |
| Strong radial force harmonics | Reduced force harmonic amplitudes |
| Higher acoustic noise | Lower acoustic noise |
| Slightly reduced torque | Marginal torque reduction |

The notch creates a local increase in effective airgap, which modulates the permeance. This modulates the radial force density, reducing the specific harmonic orders that excite stator mode shapes.

---

## Design Considerations

- **Depth** — Deeper notches provide more NVH reduction but remove more iron, reducing torque and increasing flux density in remaining material.
- **Sweep** — Wider notches affect more harmonics but reduce the structural integrity of the rotor surface.
- **Number per pole** — Multiple notches per pole can target multiple force harmonic orders simultaneously.
- **Position** — Notch placement relative to the pole axis and flux barriers affects which harmonics are targeted.
- **Manufacturing** — Triangular notches are simple to stamp and add no manufacturing complexity.
- **Interaction with barriers** — Notches must not overlap with flux barrier entries. Check geometry constraints.

---

## Common Pitfalls

1. **Crossing symmetry boundary** — Notch extends beyond the symmetry sector. Reduce sweep or adjust centre angle.
2. **Overlapping barriers** — Notch intersects a flux barrier. Check radial and angular positions against barrier geometry.
3. **Exceeding rotor OD** — Notch radius is set beyond the rotor outer diameter. Use the actual rotor OD.
4. **Missing `duplications`** — If `duplications` is not set, the notch appears only in one pole instead of all poles.
5. **Wrong `parent`** — The parent must be the rotor lamination region for correct material and mesh assignment.
6. **Notch too close to shaft** — Deep notches at small radii may approach the shaft region, causing geometry errors.

---

## Related Pages

- [[pymotorcad-adaptive-geometry]] — Full adaptive template API
- [[pymotorcad-geometry-shapes]] — triangular_notch() and other shape primitives
- [[pymotorcad-geometry-objects]] — Region, RegionType, Coordinate types
- [[pymotorcad-adaptive-templates-guide]] — Adaptive templates user guide
- [[pymotorcad-mechanical-force]] — Force/NVH calculation methods
- [[pymotorcad-triangular-stator-notches]] — Triangular stator notches (related concept)
- [[torque-ripple]] — Torque ripple and reduction methods

---

## Tags

#pymotorcad #motorcad #triangular #notches #rotor #nvh #adaptive-geometry #noise #vibration #harshness #rotor-design
