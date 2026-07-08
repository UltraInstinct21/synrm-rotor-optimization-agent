## Geometry objects and functions

Geometry functions are used to define and modify the Motor-CAD Adaptive Templates geometry using PyMotorCAD.

More information on Adaptive Templates is available in the User [guide](https://motorcad.docs.pyansys.com/version/stable/user_guide/index.html#ref-user-guide) under [Motor-CAD](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) adaptive [templates](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) scripting.

API reference for the Motor-CAD methods for getting and setting geometry regions is available under Adaptive [Geometry.](https://motorcad.docs.pyansys.com/version/stable/methods/_autogen_Adaptive%20Geometry.html#ref-adaptive-geometry-api)

## Geometry objects

| Region ([region_type, motorcad_instance])      | Create geometry region.                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------------------|
| RegionMagnet ([motorcad_instance])             | Create magnet geometry region.                                                                 |
| RegionType (value[, names, module, qualname,]) | Provides an enumeration for storing<br>Motor-CAD region types.                                 |
| Coordinate (x, y)                              | Provides the Python representation of a<br>coordinate in two-dimensional space.                |
| Entity (start, end)                            | Generic parent class for geometric<br>entities based upon a start and end<br>coordinate.       |
| EntityList ([iterable])                        | Generic class for list of Entities.                                                            |
| Line (start, end)                              | Python representation of Motor-CAD line<br>entity based upon start and end<br>coordinates.     |
| Arc (start, end[, centre, radius])             | Python representation of Motor-CAD arc<br>entity based upon start, end, (centre or<br>radius). |

## Geometry functions

| get_entities_have_common_coordinate () | Check whether region entities create a closed region.                       |
|----------------------------------------|-----------------------------------------------------------------------------|
| xy_to_rt (x, y)                        | Convert Motor-CAD Cartesian coordinates to polar<br>coordinates in degrees. |
| rt_to_xy (radius, theta)               | Convert Motor-CAD polar coordinates to Cartesian<br>coordinates in degrees. |
| get_bezier_points (control_points,)    | Find a list of coordinates along a Bezier curve.                            |

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026