## FEA Geometry

| add_arc_boundary_rt (direction, rc, tc, th1,) | Add a boundary condition arc using r, t<br>coordinates for the center.                      |
|-----------------------------------------------|---------------------------------------------------------------------------------------------|
| add_arc_boundary_xy (direction, xc, yc, th1,) | Add a boundary condition arc using x, y<br>coordinates for the center.                      |
| add_arc_centre_start_end_rt (radius_centre,)  | Add an arc to the Motor-CAD axial geometry<br>with an r, t (polar) coordinate system.       |
| add_arc_centre_start_end_xy (x_centre,)       | Add an arc to the Motor-CAD axial geometry<br>with an r, t (polar) coordinate system.       |
| add_arc_rt (radius_center, theta_centre,)     | Add an arc to the Motor-CAD axial geometry<br>with an r, t (polar) coordinate system.       |
| add_arc_xy (x_centre, y_centre, theta_start,) | Add an arc to the Motor-CAD axial geometry<br>with an x, y coordinate system.               |
| add_line_boundary_rt (rs, ts, re, t_e,)       | Add a boundary condition line using r, t<br>coordinates for the start and end points.       |
| add_line_boundary_xy (xs, ys, xe, ye,)        | Add a boundary condition line using x, y<br>coordinates for the start and end points.       |
| add_line_rt (radius_start, theta_start,)      | Add a line to the Motor-CAD axial geometry<br>with an r, t (polar) coordinate system.       |
| add_line_xy (x_start, y_start, x_end, y_end)  | Add a line to the Motor-CAD axial geometry<br>with an x, y coordinate system.               |
| add_magnet_region_rt (radius, theta,)         | Add a magnet region to the Motor-CAD<br>geometry with an r, t (polar) coordinate<br>system. |
| add_magnet_region_xy (x, y, region_name,)     | Add a magnet region to the Motor-CAD<br>geometry with an x, y coordinate system.            |
| add_point_custom_material_rt (radius, theta,) | Add a region to the geometry and specify<br>the material.                                   |
| add_point_custom_material_xy (x, y,)          | Add a region to the geometry and specify<br>the material.                                   |
| add_region_rt (radius, theta, region_name)    | Add a region to the Motor-CAD geometry<br>with an r, t (polar) coordinate system.           |
| add_region_xy (x, y, region_name)             | Add a region to the Motor-CAD geometry<br>with an x, y coordinate system.                   |

| clear_all_data ()                              | Clear data and initialize the FEA.                                                       |
|------------------------------------------------|------------------------------------------------------------------------------------------|
| create_optimised_mesh ()                       | Create the FEA geometry and an optimized<br>mesh.                                        |
| delete_regions (region_name)                   | Delete a comma-separated list of named<br>regions or all regions.                        |
| do_slot_finite_element ()                      | Run slot FEA.                                                                            |
| edit_magnet_region (region_name,)              | Edit a magnet region.                                                                    |
| get_point_value (parameter, x, y)              | Get a point value from the Motor-CAD FEA.                                                |
| get_region_loss (expression, region_name,)     | Calculate the loss value for an expression of<br>a region.                               |
| get_region_value (expression, region_name)     | Calculate the integral value for an<br>expression of a region.                           |
| initiate_geometry_from_script ()               | Initiate the geometry from scripting so<br>Motor-CAD knows how to use it.                |
| reset_regions ()                               | Reset custom FEA regions to standard<br>regions from the Motor-CAD template<br>geometry. |
| save_fea_data (file, first_step, final_step,)  | Save raw data for the current FEA solution.                                              |
| set_fea_path_arc (path_name, path_location,)   | Add or edit an arc in the path editor.                                                   |
| set_fea_path_line (path_name, path_location,)  | Add or edit a line in the path editor.                                                   |
| set_fea_path_point (path_name, path_location,) | Add or edit a point in the path editor.                                                  |
|                                                |                                                                                          |

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026