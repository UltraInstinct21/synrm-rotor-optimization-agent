---
type: motorcad_parameter_category
category_name: Discovery
parameter_count: 12
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Discovery

## Overview
The **Discovery** category contains **12** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/Discovery_APIVersion|Discovery_APIVersion]] | setting | OleStr | N/A | Sets the API version string in the Discovery geometry export script header |
| [[motorcad/parameter_database/parameters/Discovery_ConvertToSolids|Discovery_ConvertToSolids]] | setting | boolean | N/A | This selects if exported geometry outlines are converted to solid components. |
| [[motorcad/parameter_database/parameters/Discovery_FileName|Discovery_FileName]] | i/p | OleStr | N/A | The Discovery Python file being generated |
| [[motorcad/parameter_database/parameters/Discovery_GroupComponents|Discovery_GroupComponents]] | setting | boolean | N/A | This selects if exported components are organised into group nodes. |
| [[motorcad/parameter_database/parameters/Discovery_Housing|Discovery_Housing]] | setting | boolean | N/A | This selects if the housing components are included in the export. |
| [[motorcad/parameter_database/parameters/Discovery_MinArcDistance|Discovery_MinArcDistance]] | setting | double | mm | The minimum distance over which an arc can be defined, below which a line is used. |
| [[motorcad/parameter_database/parameters/Discovery_ModelType|Discovery_ModelType]] | setting | integer | N/A | This sets whether a 3D or 2D model is exported to Discovery/SpaceClaim |
| [[motorcad/parameter_database/parameters/Discovery_Rotor|Discovery_Rotor]] | setting | boolean | N/A | This selects if the rotor components are included in the export. |
| [[motorcad/parameter_database/parameters/Discovery_SetColours|Discovery_SetColours]] | setting | boolean | N/A | This selects if exported components use the Motor-CAD model colours. |
| [[motorcad/parameter_database/parameters/Discovery_SmallUnits|Discovery_SmallUnits]] | setting | boolean | N/A | Use of Small Units in the Discovery geometry export script, which may aid in drawing small features |
| [[motorcad/parameter_database/parameters/Discovery_Stator|Discovery_Stator]] | setting | boolean | N/A | This selects if the stator components are included in the export. |
| [[motorcad/parameter_database/parameters/Discovery_SymmetryOption|Discovery_SymmetryOption]] | setting | integer | N/A | This selects if symmetry based geometry is multiplied to a full machine and if so in which software. |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
