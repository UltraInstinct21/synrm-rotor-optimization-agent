---
type: pymotorcad_api
title: "PyMotorCAD Geometry Tree API"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - geometry
  - geometry-tree
  - adaptive-geometry
  - regions
  - magnets
  - api
aliases:
  - pymotorcad_geometry_tree
  - motorcad_geometry_tree
  - tree_region
related_pages:
  - "[[pymotorcad-adaptive-geometry]]"
  - "[[pymotorcad-geometry-objects]]"
  - "[[pymotorcad-geometry-basic]]"
  - "[[pymotorcad-calculations-api]]"
confidence: verified
---

# PyMotorCAD Geometry Tree API

## Overview

The Geometry Tree API provides a hierarchical, programmatic approach to motor geometry construction introduced in Motor-CAD v2026R1. Rather than setting individual geometric parameters, the Geometry Tree allows users to build, query, and manipulate motor geometry as a structured tree of regions — enabling more flexible, scriptable, and parametric geometry workflows.

This API is the foundation for adaptive geometry workflows where geometry is constructed programmatically rather than loaded from pre-defined parameter sets.

---

## Core Classes

### `GeometryTree(mc, create_root_node)`

#### Purpose

Creates a new Geometry Tree instance linked to a Motor-CAD model, providing the root container for all geometric regions.

#### Signature

```python
GeometryTree(mc: MotorCAD, create_root_node: bool = True)
```

#### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `mc` | `MotorCAD` | — | Motor-CAD instance to link the tree to |
| `create_root_node` | `bool` | `True` | Whether to create the root node automatically |

#### Description

The `GeometryTree` is the top-level container for all geometry regions. It represents the complete motor cross-section as a hierarchical tree where:

- The **root node** represents the full motor cross-section
- **Child nodes** represent major divisions (stator, rotor, airgap)
- **Grandchild nodes** represent sub-regions (slots, barriers, shafts)
- **Leaf nodes** represent individual geometric features

When `create_root_node=True`, the tree is automatically initialized with the standard motor structure (stator region, rotor region, airgap region, shaft region).

#### Example

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core import GeometryTree

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Create a geometry tree from the current model
tree = GeometryTree(mc, create_root_node=True)

# The tree now contains the full motor geometry as a hierarchy
print(f"Root node children: {tree.root.child_count()}")
```

#### Tree Structure

```
GeometryTree (root)
├── Stator
│   ├── Yoke
│   ├── Teeth (×48 for 48-slot)
│   └── Slots (×48)
├── Airgap
├── Rotor
│   ├── Lamination
│   ├── Barriers (×N_layers)
│   └── Shafts
└── Housing (optional)
```

#### Use Cases

- Programmatic motor geometry construction
- Parametric geometry modification
- Geometry optimization with direct tree manipulation
- Building geometry from scratch (not from parameter file)
- Querying geometric relationships between regions

---

### `TreeRegion(tree, region_type)`

#### Purpose

Creates a new geometric region within a Geometry Tree, defining a specific part of the motor cross-section.

#### Signature

```python
TreeRegion(tree: GeometryTree, region_type: str)
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `tree` | `GeometryTree` | The geometry tree to add the region to |
| `region_type` | `str` | Type of region to create |

#### Region Types

| `region_type` | Description |
|---|---|
| `"stator"` | Stator lamination region |
| `"rotor"` | Rotor lamination region |
| `"airgap"` | Airgap region between stator and rotor |
| `"shaft"` | Shaft region |
| `"magnet"` | Permanent magnet region (for PM motors) |
| `"barrier"` | Flux barrier region (for SynRM) |
| `"housing"` | Motor housing/frame |
| `"winding"` | Winding/copper region |
| `"insulation"` | Slot liner / insulation region |
| `"custom"` | User-defined custom region |

#### Example

```python
from ansys.motorcad.core import GeometryTree, TreeRegion

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

tree = GeometryTree(mc)

# Create region objects
stator_region = TreeRegion(tree, "stator")
rotor_region = TreeRegion(tree, "rotor")
airgap_region = TreeRegion(tree, "airgap")

# Regions can be configured with properties
stator_region.set_inner_diameter(215)  # mm
stator_region.set_outer_diameter(340)  # mm

rotor_region.set_outer_diameter(214)  # mm (stator bore - airgap)
rotor_region.set_inner_diameter(80)    # mm (shaft diameter)
```

#### Region Properties

Each region type supports specific properties:

| Region Type | Settable Properties |
|---|---|
| `stator` | `inner_diameter`, `outer_diameter`, `length`, `material` |
| `rotor` | `outer_diameter`, `inner_diameter`, `length`, `material` |
| `airgap` | `length`, `type` (radial/axial) |
| `shaft` | `diameter`, `length`, `material` |
| `magnet` | `inner_diameter`, `outer_diameter`, `arc`, `material`, `magnetization` |
| `barrier` | `inner_diameter`, `outer_diameter`, `arc_start`, `arc_span`, `material` |

---

### `TreeRegionMagnet(tree, motorcad_instance)`

#### Purpose

Creates a magnet region specifically for permanent magnet motor topologies, with magnet-specific properties and magnetization configuration.

#### Signature

```python
TreeRegionMagnet(tree: GeometryTree, motorcad_instance: MotorCAD)
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `tree` | `GeometryTree` | The geometry tree to add the magnet region to |
| `motorcad_instance` | `MotorCAD` | Motor-CAD instance for material and magnetization data |

#### Description

This is a specialized region class for permanent magnets in IPM, SPM, and PMaSynRM topologies. It extends `TreeRegion` with magnet-specific attributes:

- Magnetization direction (radial, parallel, Halbach)
- Remanent flux density (Br)
- Coercivity (Hc)
- Magnet grade and material
- Temperature coefficient of Br

#### Example

```python
from ansys.motorcad.core import GeometryTree, TreeRegionMagnet

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\ipmsm_45kw.mot")

tree = GeometryTree(mc)

# Create magnet region for IPM rotor
magnet = TreeRegionMagnet(tree, mc)

# Configure magnet properties
magnet.set_inner_diameter(100)   # mm
magnet.set_outer_diameter(130)   # mm
magnet.set_arc_span(40)          # degrees
magnet.set_magnetization("parallel")
magnet.set_material("N42SH")

# Apply to tree
magnet.add_to_tree()
```

#### Magnet Materials Reference

| Material | Br (T) | Hc (kA/m) | Max Temp (°C) |
|---|---|---|---|
| N42SH | 1.28 | 955 | 150 |
| N38EH | 1.22 | 935 | 180 |
| N35UH | 1.17 | 876 | 180 |
| Ferrite_8 | 0.42 | 240 | 250 |

---

## Geometry Tree API Methods

### `get_geometry_tree()`

#### Purpose

Retrieves the current geometry tree from a Motor-CAD model, providing programmatic access to all geometric regions.

#### Signature

```python
get_geometry_tree() -> GeometryTree
```

#### Returns

| Return | Type | Description |
|---|---|---|
| `GeometryTree` | Tree object containing all geometry regions |

#### Description

This method extracts the current geometry from Motor-CAD's internal representation and returns it as a `GeometryTree` object. The tree can then be inspected, modified, and written back.

#### Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Get the geometry tree
tree = mc.get_geometry_tree()

# Inspect the tree
print(f"Root has {tree.root.child_count()} children")

# Traverse the tree
for child in tree.root.children():
    print(f"  Region: {child.region_type}, "
          f"OD: {child.outer_diameter:.1f} mm, "
          f"ID: {child.inner_diameter:.1f} mm")
```

#### Tree Traversal

```python
tree = mc.get_geometry_tree()

def print_tree(node, indent=0):
    """Recursively print the geometry tree."""
    prefix = "  " * indent
    print(f"{prefix}{node.region_type}: "
          f"ID={node.inner_diameter:.1f}, OD={node.outer_diameter:.1f}")
    for child in node.children():
        print_tree(child, indent + 1)

print_tree(tree.root)
```

#### Output Example

```
rotor: ID=80.0, OD=214.0
  lamination: ID=80.0, OD=214.0
    barrier: ID=100.0, OD=130.0
    barrier: ID=130.0, OD=160.0
    barrier: ID=160.0, OD=195.0
airgap: ID=214.0, OD=215.0
stator: ID=215.0, OD=340.0
  yoke: ID=290.0, OD=340.0
  teeth: ID=215.0, OD=290.0
    slot: ID=215.0, OD=290.0
    slot: ID=215.0, OD=290.0
    ...
```

---

### `set_geometry_tree(tree)`

#### Purpose

Writes a modified geometry tree back to Motor-CAD, updating the model's internal geometry representation.

#### Signature

```python
set_geometry_tree(tree: GeometryTree) -> None
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `tree` | `GeometryTree` | Modified geometry tree to apply |

#### Description

After modifying a geometry tree (changing dimensions, adding/removing regions, modifying barriers), this method writes the changes back to Motor-CAD. The model's parameter set is updated to reflect the tree structure.

#### Example

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Get current tree
tree = mc.get_geometry_tree()

# Modify a barrier
for child in tree.root.children():
    if child.region_type == "rotor":
        for barrier in child.children():
            if barrier.region_type == "barrier":
                # Increase barrier arc span by 5 degrees
                barrier.set_arc_span(barrier.arc_span + 5)

# Write back to Motor-CAD
mc.set_geometry_tree(tree)

# Verify changes took effect
print(f"Barrier arc span updated: {barrier.arc_span:.1f} degrees")

# Run calculation with modified geometry
mc.do_magnetic_calculation()
```

#### Validation

After `set_geometry_tree()`, it is recommended to validate:

```python
mc.set_geometry_tree(tree)

# Validate the modified geometry
is_valid = mc.check_if_geometry_is_valid()
if not is_valid:
    print("WARNING: Modified geometry is invalid")
    # Revert or fix
```

---

## Complete Workflow: Programmatic Geometry Construction

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core import GeometryTree, TreeRegion

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_base.mot")

# Create empty tree
tree = GeometryTree(mc, create_root_node=True)

# Build stator
stator = TreeRegion(tree, "stator")
stator.set_inner_diameter(215)
stator.set_outer_diameter(340)
stator.set_material("50C250")

# Build rotor
rotor = TreeRegion(tree, "rotor")
rotor.set_outer_diameter(214)
rotor.set_inner_diameter(80)

# Build airgap
airgap = TreeRegion(tree, "airgap")
airgap.set_length(0.5)

# Build flux barriers
barrier1 = TreeRegion(tree, "barrier")
barrier1.set_inner_diameter(100)
barrier1.set_outer_diameter(130)
barrier1.set_arc_span(35)

barrier2 = TreeRegion(tree, "barrier")
barrier2.set_inner_diameter(130)
barrier2.set_outer_diameter(160)
barrier2.set_arc_span(30)

barrier3 = TreeRegion(tree, "barrier")
barrier3.set_inner_diameter(160)
barrier3.set_outer_diameter(195)
barrier3.set_arc_span(25)

# Apply to Motor-CAD
mc.set_geometry_tree(tree)

# Validate
if mc.check_if_geometry_is_valid():
    print("Geometry construction successful")
    mc.do_magnetic_calculation()
else:
    print("Geometry construction failed validation")
```

---

## Parametric Geometry Optimization

The Geometry Tree enables direct parametric optimization without round-tripping through Motor-CAD parameters:

```python
import ansys.motorcad.core as pymotorcad
from ansys.motorcad.core import GeometryTree

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

def evaluate_geometry(barrier_arc_spans):
    """Evaluate torque for a given set of barrier arc spans."""
    tree = mc.get_geometry_tree()
    
    # Find and modify barriers
    barrier_idx = 0
    for child in tree.root.children():
        if child.region_type == "rotor":
            for grandchild in child.children():
                if grandchild.region_type == "barrier":
                    grandchild.set_arc_span(barrier_arc_spans[barrier_idx])
                    barrier_idx += 1
    
    mc.set_geometry_tree(tree)
    mc.do_magnetic_calculation()
    return mc.get_variable("ShaftTorque")

# Parametric sweep
results = []
for l1_arc in range(30, 45, 5):
    for l2_arc in range(25, 40, 5):
        torque = evaluate_geometry([l1_arc, l2_arc, 25])
        results.append((l1_arc, l2_arc, torque))
        print(f"L1={l1_arc}, L2={l2_arc}: Torque={torque:.2f} Nm")

# Find best
best = max(results, key=lambda x: x[2])
print(f"\nBest: L1={best[0]}, L2={best[1]}, Torque={best[2]:.2f} Nm")
```

---

## Tree Node Properties

Each node in the geometry tree exposes common properties:

| Property | Type | Description |
|---|---|---|
| `region_type` | `str` | Type of region (stator, rotor, barrier, etc.) |
| `inner_diameter` | `float` | Inner diameter in mm |
| `outer_diameter` | `float` | Outer diameter in mm |
| `arc_start` | `float` | Starting angle in degrees (for arc regions) |
| `arc_span` | `float` | Angular span in degrees (for arc regions) |
| `material` | `str` | Material name |
| `children()` | `list` | Child nodes |
| `child_count()` | `int` | Number of children |
| `parent()` | `node` | Parent node reference |

---

## Geometry Tree vs. Parameter-Based Geometry

| Aspect | Parameter-Based | Geometry Tree |
|---|---|---|
| **Modification** | `set_variable()` calls | Direct tree manipulation |
| **Querying** | `get_variable()` calls | Tree traversal |
| **Parametric** | Requires manual parameter management | Natural parametric loops |
| **Validation** | `check_if_geometry_is_valid()` | Same + tree structure validation |
| **Flexibility** | Limited to predefined parameters | Full structural control |
| **Version** | All versions | v2026R1+ |
| **Use case** | Simple parameter changes | Complex geometry construction |

---

## Cross-References

- [[pymotorcad-adaptive-geometry]] — Adaptive mesh refinement using geometry tree
- [[pymotorcad-geometry-objects]] — Lower-level geometry object manipulation
- [[pymotorcad-geometry-basic]] — Basic geometry validation and winding APIs
- [[pymotorcad-calculations-api]] — Calculation methods that consume geometry
- [[pymotorcad-emag-example]] — EMag workflow with geometry setup

---

## Tags

#pymotorcad #motorcad #api #geometry #geometry-tree #adaptive-geometry #regions #magnets #barriers #parametric #optimization #v2026R1
