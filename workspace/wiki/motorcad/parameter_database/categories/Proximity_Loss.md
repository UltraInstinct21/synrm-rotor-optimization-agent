---
type: motorcad_parameter_category
category_name: Proximity_Loss
parameter_count: 9
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Proximity_Loss

## Overview
The **Proximity_Loss** category contains **9** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/ACLossModel_FullFEA_AllSlots_MaxConductors|ACLossModel_FullFEA_AllSlots_MaxConductors]] | i/p | integer | N/A | Maximum number of conductors per slot for Full FEA AC Loss calculation with conductors in all slots. |
| [[motorcad/parameter_database/parameters/ACLoss_FEA_OC_Total|ACLoss_FEA_OC_Total]] | o/p | double | Watts | The total open circuit AC winding losses (full FEA) |
| [[motorcad/parameter_database/parameters/ACLoss_FEA_OnLoad_Total|ACLoss_FEA_OnLoad_Total]] | o/p | double | Watts | The total on load AC winding losses (full FEA) |
| [[motorcad/parameter_database/parameters/ACLoss_FEA_Turns|ACLoss_FEA_Turns]] | o/p | integer | N/A | The number of AC winding loss turns |
| [[motorcad/parameter_database/parameters/ArmatureCopperFreqCompLoss|ArmatureCopperFreqCompLoss]] | o/p | double | Watts | The AC winding losses in model |
| [[motorcad/parameter_database/parameters/HybridAdjustmentFactor_ACLosses|HybridAdjustmentFactor_ACLosses]] | i/p | double | N/A | The adjustment factor for the AC Losses calculated by the Hybrid FEA method. |
| [[motorcad/parameter_database/parameters/HybridModel_FEAFluxLinePoints|HybridModel_FEAFluxLinePoints]] | i/p | integer | N/A | The number of points taken along each line in the hybrid loss model |
| [[motorcad/parameter_database/parameters/HybridModel_PolynomialPower|HybridModel_PolynomialPower]] | i/p | double | N/A | Defines the skew distrubution of the lines in the hybrid loss model |
| [[motorcad/parameter_database/parameters/HybridModel_TotalLines|HybridModel_TotalLines]] | i/p | integer | N/A | The total number of lines used in the hybrid loss model |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
