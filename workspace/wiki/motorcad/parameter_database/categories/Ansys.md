---
type: motorcad_parameter_category
category_name: Ansys
parameter_count: 18
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Ansys

## Overview
The **Ansys** category contains **18** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AnsysAirgapMesh|AnsysAirgapMesh]] | setting | integer | N/A | Whether airgap cylindrical mesh is used for Ansys export |
| [[motorcad/parameter_database/parameters/AnsysExportFormat|AnsysExportFormat]] | setting | integer | N/A | This determines the format of the Ansys Electronics Desktop model exported from Motor-CAD |
| [[motorcad/parameter_database/parameters/AnsysModelType|AnsysModelType]] | setting | integer | N/A | This sets whether 2D or 3D model is exported to Ansys Electronics Desktop model |
| [[motorcad/parameter_database/parameters/AnsysReplaceArcEntities|AnsysReplaceArcEntities]] | setting | boolean | N/A | Replace Arc entities with a sweep smaller than a given value with a line entity between the start and end coordinate of the original arc entity. |
| [[motorcad/parameter_database/parameters/AnsysReplaceArcEntities_MinimumSweep|AnsysReplaceArcEntities_MinimumSweep]] | setting | double | N/A | The arc sweep used to check whether to replace arc entity with line entity in degrees. |
| [[motorcad/parameter_database/parameters/AnsysSolve|AnsysSolve]] | setting | integer | N/A | This sets whether the model solves automatically when the script is run. |
| [[motorcad/parameter_database/parameters/Ansys_ArcType|Ansys_ArcType]] | setting | integer | N/A | The arc type used in Ansys Maxwell polyline objects |
| [[motorcad/parameter_database/parameters/Ansys_DemagCurve|Ansys_DemagCurve]] | setting | integer | N/A | Whether to export the intrinsic or normal demagnetisation curve. |
| [[motorcad/parameter_database/parameters/Ansys_DriveType|Ansys_DriveType]] | setting | integer | N/A | The drive type used for the model in Maxwell, either Current or Voltage driven. |
| [[motorcad/parameter_database/parameters/Ansys_MagnetThermalData|Ansys_MagnetThermalData]] | setting | integer | N/A | Whether magnet thermal data is included in the Maxwell export. |
| [[motorcad/parameter_database/parameters/Ansys_NonStandardRegions_Names|Ansys_NonStandardRegions_Names]] | setting | OleStr | N/A | The names of non-standard custom regions for Ansys Maxwell export |
| [[motorcad/parameter_database/parameters/Ansys_NonStandardRegions_Number|Ansys_NonStandardRegions_Number]] | setting | integer | N/A | The number of non-standard custom regions for Ansys Maxwell export |
| [[motorcad/parameter_database/parameters/Ansys_NonStandardRegions_Temperatures|Ansys_NonStandardRegions_Temperatures]] | setting | integer | N/A | The temperatures of non-standard custom regions for Ansys Maxwell export |
| [[motorcad/parameter_database/parameters/Ansys_NonStandardRegions_Types|Ansys_NonStandardRegions_Types]] | setting | OleStr | N/A | The type strings of non-standard custom regions for Ansys Maxwell export |
| [[motorcad/parameter_database/parameters/Ansys_ScriptFormat|Ansys_ScriptFormat]] | setting | integer | N/A | The script format used for Ansys Maxwell export, either Python or Visual Basic script. |
| [[motorcad/parameter_database/parameters/Ansys_WindingGroups|Ansys_WindingGroups]] | setting | integer | N/A | The winding group definition in Ansys Maxwell export |
| [[motorcad/parameter_database/parameters/Maxwell_PolylineCircles|Maxwell_PolylineCircles]] | compatibility | integer | N/A | Whether to use circles when creating Maxwell Export using polylines |
| [[motorcad/parameter_database/parameters/NoSkewSlices_Maxwell|NoSkewSlices_Maxwell]] | setting | integer | N/A | The number of skew slices used for Maxwell export |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
