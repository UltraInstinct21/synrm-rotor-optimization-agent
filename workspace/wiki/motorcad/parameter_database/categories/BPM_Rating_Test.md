---
type: motorcad_parameter_category
category_name: BPM_Rating_Test
parameter_count: 8
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: BPM_Rating_Test

## Overview
The **BPM_Rating_Test** category contains **8** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/Constant_Torque_or_Constant_Current|Constant_Torque_or_Constant_Current]] | i/p | integer | °C/W | 0 = Constant_Torque,    1 = Constant_Current |
| [[motorcad/parameter_database/parameters/Iron_loss_Flux_To_Power_Ratio|Iron_loss_Flux_To_Power_Ratio]] | i/p | double | N/A | Iron loss flux density raise to power coefficient - used in calculation of loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/Magnet_Temperature_Load_Vary|Magnet_Temperature_Load_Vary]] | i/p | double | °C | Magnet temperature at which Torque & Rph specified - used in  calculation of loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/PM_Losses_Vary_With_Temperature_and_Load|PM_Losses_Vary_With_Temperature_and_Load]] | i/p | boolean | N/A | PM Losses vary with temperature & load - to maintain a constant torque (rating test) |
| [[motorcad/parameter_database/parameters/Rph_at_Tw|Rph_at_Tw]] | i/p | double | Ohms | Phase resistance [@Tw] used in calculation of loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/Torque_Constant|Torque_Constant]] | o/p | double | N/A | Torque constant Nm/Arms [Arms is motor line current] |
| [[motorcad/parameter_database/parameters/Torque_Current_Multiplier|Torque_Current_Multiplier]] | i/p | double | Nm/A | Steady-State thermal calculation is carried out at this multiple of the Shaft Torque or Motor Current defined above |
| [[motorcad/parameter_database/parameters/Winding_Temperature_Load_Vary|Winding_Temperature_Load_Vary]] | i/p | double | °C | Winding temperature at which Torque & Rph specified - used in  calculation of loss variation with temperature & load |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
