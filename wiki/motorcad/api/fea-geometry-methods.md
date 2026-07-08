---
type: motorcad_api
method_group: "FEA Geometry"
module: "ansys.motorcad.core"
source_files: ["FEA Geometry — pymotorcad-core.md"]
confidence: Verified
---

# FEA Geometry Methods

## Adding Geometry

| Method | Description |
|--------|-------------|
| `add_arc_boundary_rt(...)` / `add_arc_boundary_xy(...)` | Add boundary condition arc |
| `add_arc_centre_start_end_rt(...)` / `add_arc_centre_start_end_xy(...)` | Add arc with centre, start, end |
| `add_arc_rt(...)` / `add_arc_xy(...)` | Add arc using polar or Cartesian |
| `add_line_boundary_rt(...)` / `add_line_boundary_xy(...)` | Add boundary condition line |
| `add_line_rt(...)` / `add_line_xy(...)` | Add line using polar or Cartesian |
| `add_magnet_region_rt(...)` / `add_magnet_region_xy(...)` | Add magnet region |
| `add_point_custom_material_rt(...)` / `add_point_custom_material_xy(...)` | Add region with custom material |
| `add_region_rt(...)` / `add_region_xy(...)` | Add region using polar or Cartesian |

## FEA Operations

| Method | Description |
|--------|-------------|
| `clear_all_data()` | Clear data and initialize FEA |
| `create_optimised_mesh()` | Create FEA geometry and optimized mesh |
| `delete_regions(region_name)` | Delete named regions or all |
| `do_slot_finite_element()` | Run slot FEA |
| `edit_magnet_region(region_name, ...)` | Edit magnet region |
| `get_point_value(parameter, x, y)` | Get point value from FEA |
| `get_region_loss(expression, region_name, ...)` | Calculate loss for region expression |
| `get_region_value(expression, region_name)` | Calculate integral value for region |
| `initiate_geometry_from_script()` | Initiate geometry from scripting |
| `reset_regions()` | Reset custom FEA to template geometry |
| `save_fea_data(file, first_step, final_step, ...)` | Save raw FEA solution data |
| `set_fea_path_arc(path_name, path_location, ...)` | Add/edit arc in path editor |
| `set_fea_path_line(path_name, path_location, ...)` | Add/edit line in path editor |
| `set_fea_path_point(path_name, path_location, ...)` | Add/edit point in path editor |

## Related Pages

- [[motorcad/api/geometry-methods]] — Basic geometry methods
- [[motorcad/api/adaptive-geometry-methods]] — Adaptive geometry methods
