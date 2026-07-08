## Geometry tree

The geometry tree object and its methods are used to define and modify the Motor-CAD Adaptive Templates geometry using PyMotorCAD. Geometry trees were introduced in Motor-CAD v2026R1 and are not compatible with earlier versions of Motor-CAD. In earlier versions of Motor-CAD, you should use the geometry objects and functions under [Geometry](https://motorcad.docs.pyansys.com/version/stable/methods/geometry_functions.html#ref-geometry-functions) objects and functions.

More information on Adaptive Templates is available in the User [guide](https://motorcad.docs.pyansys.com/version/stable/user_guide/index.html#ref-user-guide) under [Motor-CAD](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) adaptive [templates](https://motorcad.docs.pyansys.com/version/stable/user_guide/adaptive_templates.html#ref-adaptive-templates-ug) scripting.

API reference for the Motor-CAD methods used for getting and setting the geometry tree is available under Adaptive [Geometry](https://motorcad.docs.pyansys.com/version/stable/methods/_autogen_Adaptive%20Geometry.html#ref-adaptive-geometry-api).

## Geometry tree objects

| GeometryTree ([mc, create_root_node])        | Class used to build geometry trees.                     |
|----------------------------------------------|---------------------------------------------------------|
| TreeRegion (tree, region_type[,])            | Subclass of Region used for entries in<br>GeometryTree. |
| TreeRegionMagnet (tree[, motorcad_instance]) | Class for magnets in tree.                              |