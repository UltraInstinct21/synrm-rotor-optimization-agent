## Adaptive Geometry

| check_closed_region (region)                 | Check region is closed using region detection.                                           |
|----------------------------------------------|------------------------------------------------------------------------------------------|
| check_collisions (region, regions_to_check)  | Check region does not collide with other<br>geometry regions.                            |
| delete_region (region[, remove_children])    | Delete region from Motor-CAD geometry<br>engine.                                         |
| get_adaptive_parameter_value (name)          | Get adaptive parameter.                                                                  |
| get_geometry_tree ()                         | Fetch a GeometryTree object containing all the<br>defining geometry of the loaded motor. |
| get_maxwell_udm_geometry_json ()             | Fetch a dict defining Maxwell UDM geometry.                                              |
| get_region (name[, get_linked])              | Get Motor-CAD geometry region.                                                           |
| get_region_dxf (name)                        | Get Motor-CAD dxf geometry region.                                                       |
| load_adaptive_script (filepath)              | Load adaptive templates script file to Motor<br>CAD.                                     |
| reset_adaptive_geometry ()                   | Reset geometry to default.                                                               |
| save_adaptive_script (filepath)              | Save adaptive templates script from Motor-CAD<br>to file.                                |
| set_adaptive_parameter_default (name, value) | Set default value for an adaptive parameter, if<br>the parameter does not already exist. |
| set_adaptive_parameter_value (name, value)   | Set adaptive parameter, if parameter does not<br>exist then add it.                      |
| set_geometry_tree (tree)                     | Use a GeometryTree object to set the defining<br>geometry of the loaded motor.           |
| set_region (region)                          | Set Motor-CAD geometry region.                                                           |
| subtract_region (region, region_subtract)    | Subtract Motor-CAD region (region_subtract)<br>from another Motor-CAD region (region).   |
| unite_regions (region, regions)              | Unite region with two or more other regions.                                             |

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026