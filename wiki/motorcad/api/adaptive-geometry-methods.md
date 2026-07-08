---
type: motorcad_api
method_group: "Adaptive Geometry"
module: "ansys.motorcad.core"
source_files: ["Adaptive Geometry — pymotorcad-core.md"]
confidence: Verified
---

# Adaptive Geometry Methods

## Methods

| Method | Description |
|--------|-------------|
| `check_closed_region(region)` | Check region is closed using region detection |
| `check_collisions(region, regions_to_check)` | Check region does not collide with other regions |
| `delete_region(region, remove_children=False)` | Delete region from geometry engine |
| `get_adaptive_parameter_value(name)` | Get adaptive parameter value |
| `get_geometry_tree()` | Fetch GeometryTree object (v2026R1+) |
| `get_maxwell_udm_geometry_json()` | Fetch dict defining Maxwell UDM geometry |
| `get_region(name, get_linked=False)` | Get Motor-CAD geometry region |
| `get_region_dxf(name)` | Get Motor-CAD DXF geometry region |
| `load_adaptive_script(filepath)` | Load adaptive templates script file |
| `reset_adaptive_geometry()` | Reset geometry to default |
| `save_adaptive_script(filepath)` | Save adaptive templates script to file |
| `set_adaptive_parameter_default(name, value)` | Set default adaptive parameter if not exists |
| `set_adaptive_parameter_value(name, value)` | Set adaptive parameter (add if not exists) |
| `set_geometry_tree(tree)` | Set geometry using GeometryTree object |
| `set_region(region)` | Set Motor-CAD geometry region |
| `subtract_region(region, region_subtract)` | Subtract one region from another |
| `unite_regions(region, regions)` | Unite region with other regions |

## Related Pages

- [[motorcad/api/geometry-methods]] — Basic geometry methods
- [[motorcad/api/geometry-objects-functions]] — Region, Line, Arc objects
- [[motorcad/api/geometry-shapes]] — Predefined shapes (triangular_notch, etc.)
- [[motorcad/api/geometry-tree]] — GeometryTree API (v2026R1+)
- [[motorcad/workflows/adaptive-templates-scripting]] — Adaptive Templates workflow
