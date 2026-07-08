---
type: motorcad_api
method_group: "Geometry Tree"
module: "ansys.motorcad.core"
source_files: ["Geometry tree — pymotorcad-core.md"]
confidence: Verified
---

# Geometry Tree

> Introduced in Motor-CAD v2026R1. Not compatible with earlier versions.

## Objects

| Object | Description |
|--------|-------------|
| `GeometryTree(mc, create_root_node)` | Class to build geometry trees |
| `TreeRegion(tree, region_type, ...)` | Subclass of Region for GeometryTree entries |
| `TreeRegionMagnet(tree, motorcad_instance)` | Class for magnets in tree |

## Methods

| Method | Description |
|--------|-------------|
| `get_geometry_tree()` | Fetch GeometryTree from Motor-CAD |
| `set_geometry_tree(tree)` | Set geometry using GeometryTree |

## Importing

```python
from ansys.motorcad.core import GeometryTree, TreeRegion
```

## Related Pages

- [[motorcad/api/geometry-objects-functions]] — Region, Line, Arc (pre-v2026)
- [[motorcad/api/adaptive-geometry-methods]] — get_region, set_region
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates workflow
