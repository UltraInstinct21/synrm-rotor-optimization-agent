---
type: motorcad_parameter_category
category_name: Rotor_Winding
parameter_count: 19
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Rotor_Winding

## Overview
The **Rotor_Winding** category contains **19** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AWG_WireGaugeIndex_Rotor|AWG_WireGaugeIndex_Rotor]] | i/p | integer | N/A | The index for AWG Rotor wire gauge selection |
| [[motorcad/parameter_database/parameters/FieldCoilDivider_Validation|FieldCoilDivider_Validation]] | compatibility | integer | N/A | Improved method checks extra criteria before using Field Coil Divider Width |
| [[motorcad/parameter_database/parameters/FieldConductorsPerSlot|FieldConductorsPerSlot]] | i/p | integer | N/A | The number of conductors per field winding slot |
| [[motorcad/parameter_database/parameters/Field_Coil_Divider|Field_Coil_Divider]] | i/p | double | N/A | Clearance between coils in same slot of Non-Overlapping windings |
| [[motorcad/parameter_database/parameters/Field_Copper_Depth_Perc|Field_Copper_Depth_Perc]] | i/p | double | N/A | Percentage of windable slot depth full of conductors [i.e. conductors forced to slot bottom by wedge] |
| [[motorcad/parameter_database/parameters/Field_Copper_Diameter|Field_Copper_Diameter]] | i/p | double | mm | Uncovered wire (copper) diameter [from wire table or input directly] |
| [[motorcad/parameter_database/parameters/Field_EWdg_Fill|Field_EWdg_Fill]] | i/p | double | N/A | Wire fill factor for field end-winding, i.e. total wire volume/end-winding volume |
| [[motorcad/parameter_database/parameters/Field_EWdg_MLT_Used|Field_EWdg_MLT_Used]] | o/p | double | mm | The field endwinding mean length per turn |
| [[motorcad/parameter_database/parameters/Field_Impreg_Goodness_Active|Field_Impreg_Goodness_Active]] | i/p | double | N/A | Multiplier used to enhance/degrade the active impregnation thermal conductivity |
| [[motorcad/parameter_database/parameters/Field_Impreg_Goodness_EWdg|Field_Impreg_Goodness_EWdg]] | i/p | double | N/A | Multiplier used to enhance/degrade the end-winding impregnation thermal conductivity |
| [[motorcad/parameter_database/parameters/Field_Impreg_Goodness_Liner_Lam|Field_Impreg_Goodness_Liner_Lam]] | i/p | double | N/A | Multiplier used to enhance/degrade the liner-lamination thermal conductivity |
| [[motorcad/parameter_database/parameters/Field_Liner_Thickness|Field_Liner_Thickness]] | i/p | double | mm | Field winding liner thickness |
| [[motorcad/parameter_database/parameters/Field_Slot_Fill|Field_Slot_Fill]] | i/p | double | N/A | Required slot fill - based on round covered conductors and slot area available for winding after liner insertion |
| [[motorcad/parameter_database/parameters/Field_WindingType|Field_WindingType]] | i/p | integer | N/A | Overlapping or non-overlapping winding |
| [[motorcad/parameter_database/parameters/Field_Winding_Definition|Field_Winding_Definition]] | i/p | integer | N/A | The winding can be defined by the copper slot fill or wire size |
| [[motorcad/parameter_database/parameters/Field_Wire_Diameter|Field_Wire_Diameter]] | i/p | double | mm | Covered wire diameter [from wire table or input directly] |
| [[motorcad/parameter_database/parameters/Metric_WireGaugeIndex_Rotor|Metric_WireGaugeIndex_Rotor]] | i/p | integer | N/A | The index for Metric Rotor wire gauge selection |
| [[motorcad/parameter_database/parameters/SWG_WireGaugeIndex_Rotor|SWG_WireGaugeIndex_Rotor]] | i/p | integer | N/A | The index for SWG Rotor wire gauge selection |
| [[motorcad/parameter_database/parameters/Wire_Type_Rotor|Wire_Type_Rotor]] | i/p | integer | N/A | The wire type used in the field winding |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
