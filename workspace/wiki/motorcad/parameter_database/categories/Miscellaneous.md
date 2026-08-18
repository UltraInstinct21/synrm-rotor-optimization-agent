---
type: motorcad_parameter_category
category_name: Miscellaneous
parameter_count: 58
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Miscellaneous

## Overview
The **Miscellaneous** category contains **58** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/Air_Property_Temperature|Air_Property_Temperature]] | i/p | double | °C | Temperature at which air properties are calculated |
| [[motorcad/parameter_database/parameters/AirgapConvectiveHTCMultiplier|AirgapConvectiveHTCMultiplier]] | i/p | double | N/A | Multiplier for the airgap convective heat transfer coefficient calculation |
| [[motorcad/parameter_database/parameters/Altitude|Altitude]] | i/p | double | m | Altitude - used together with US Standard Atmosphere Tables to set Air Pressure & Density |
| [[motorcad/parameter_database/parameters/AmbientTemperatureConvection|AmbientTemperatureConvection]] | o/p | double | °C | The final ambient temperature (convection) for a steady state or transient calculation. |
| [[motorcad/parameter_database/parameters/AmbientTemperatureRadiation|AmbientTemperatureRadiation]] | o/p | double | °C | The final ambient temperature (radiation) for a steady state or transient calculation. |
| [[motorcad/parameter_database/parameters/Axle_F_Temperature|Axle_F_Temperature]] | i/p | double | °C | Fixed Axle extension [F] temperature |
| [[motorcad/parameter_database/parameters/Axle_R_Temperature|Axle_R_Temperature]] | i/p | double | °C | Fixed Axle extension [R] temperature |
| [[motorcad/parameter_database/parameters/Base_Temperature|Base_Temperature]] | i/p | double | °C | Fixed base plate temperature |
| [[motorcad/parameter_database/parameters/Copper_Loss_Active_No_Stall|Copper_Loss_Active_No_Stall]] | o/p | double | Watts | Pcu[Active] including fact that one phase may have more copper loss than others (as if all phases have maximum current} |
| [[motorcad/parameter_database/parameters/Copper_Loss_Active_With_Uneven|Copper_Loss_Active_With_Uneven]] | o/p | double | Watts | Copper Loss Active With Uneven |
| [[motorcad/parameter_database/parameters/Copper_Loss_End_No_Stall_F|Copper_Loss_End_No_Stall_F]] | o/p | double | Watts | Pcu[End] including fact that one phase may have more copper loss than others (as if all phases have maximum current} |
| [[motorcad/parameter_database/parameters/Copper_Loss_End_No_Stall_R|Copper_Loss_End_No_Stall_R]] | o/p | double | Watts | Pcu[End] including fact that one phase may have more copper loss than others (as if all phases have maximum current} |
| [[motorcad/parameter_database/parameters/Copper_Loss_End_With_Uneven_F|Copper_Loss_End_With_Uneven_F]] | o/p | double | Watts | Copper Loss End With Uneven [Front] |
| [[motorcad/parameter_database/parameters/Copper_Loss_End_With_Uneven_R|Copper_Loss_End_With_Uneven_R]] | o/p | double | Watts | Copper Loss End With Uneven [Rear] |
| [[motorcad/parameter_database/parameters/EncGapConductivityMultiplier|EncGapConductivityMultiplier]] | i/p | double | N/A | Multiplier for encoder to encoder case airgap thermal conductivity |
| [[motorcad/parameter_database/parameters/Endcap_F_Temperature|Endcap_F_Temperature]] | i/p | double | °C | Fixed endcap [F] temperature |
| [[motorcad/parameter_database/parameters/Endcap_R_Temperature|Endcap_R_Temperature]] | i/p | double | °C | Fixed endcap [R] temperature |
| [[motorcad/parameter_database/parameters/Fault_Copper_Loss_Multiplier|Fault_Copper_Loss_Multiplier]] | o/p | double | N/A | Pcu multiplier used in estimation of fault condition |
| [[motorcad/parameter_database/parameters/FinSideBaseNatConvWeighting|FinSideBaseNatConvWeighting]] | i/p | double | N/A | Weighting of natural convection from fin side vs fin base used in axially-finned horizontally mounted machines |
| [[motorcad/parameter_database/parameters/MaxSlotOpeningParallelTooth|MaxSlotOpeningParallelTooth]] | compatibility | integer | N/A | Calculating the maximum slot opening for a parallel tooth machine in ratio mode |
| [[motorcad/parameter_database/parameters/Pcu_1ph_Dist_Schematic_Addition|Pcu_1ph_Dist_Schematic_Addition]] | o/p | double | Watts | Single phase IM Pcu difference between 1-ph dist model and average Pcu/slot model |
| [[motorcad/parameter_database/parameters/Pcu_1ph_average_per_slot|Pcu_1ph_average_per_slot]] | o/p | double | Watts | Single phase IM copper loss per slot if all slots the same |
| [[motorcad/parameter_database/parameters/Pcu_1ph_chosen_slot|Pcu_1ph_chosen_slot]] | o/p | double | Watts | Single phase IM copper loss in chosen slot |
| [[motorcad/parameter_database/parameters/Pcu_Active_1ph_Dist_Schematic_Addition|Pcu_Active_1ph_Dist_Schematic_Addition]] | o/p | double | Watts | Single phase IM Pcu[Active] difference between 1-ph dist model and average Pcu/slot model |
| [[motorcad/parameter_database/parameters/Pcu_Active_No_1ph_Dist|Pcu_Active_No_1ph_Dist]] | o/p | double | Watts | Single phase IM copper loss [Active] if all slots at chosen slot |
| [[motorcad/parameter_database/parameters/Pcu_Active_With_1ph_Dist|Pcu_Active_With_1ph_Dist]] | o/p | double | Watts | Single phase IM copper loss if all slots at chosen slot |
| [[motorcad/parameter_database/parameters/Pcu_End_1ph_Dist_Schematic_Addition|Pcu_End_1ph_Dist_Schematic_Addition]] | o/p | double | Watts | Single phase IM Pcu[End] difference between 1-ph dist model and average Pcu/slot model |
| [[motorcad/parameter_database/parameters/Pcu_End_No_1ph_Dist|Pcu_End_No_1ph_Dist]] | o/p | double | Watts | Single phase IM copper loss if all slots at average Pcu/slot |
| [[motorcad/parameter_database/parameters/Pcu_End_With_1ph_Dist_F|Pcu_End_With_1ph_Dist_F]] | o/p | double | Watts | Single phase IM copper loss [EWdg](Front) if all slots at chosen slot |
| [[motorcad/parameter_database/parameters/Pcu_End_With_1ph_Dist_R|Pcu_End_With_1ph_Dist_R]] | o/p | double | Watts | Single phase IM copper loss [EWdg](Rear) if all slots at chosen slot |
| [[motorcad/parameter_database/parameters/Pcu_No_1ph_Dist|Pcu_No_1ph_Dist]] | o/p | double | Watts | Single phase IM copper loss [Active] if all slots at average Pcu/slot |
| [[motorcad/parameter_database/parameters/Pcu_With_1ph_Dist|Pcu_With_1ph_Dist]] | o/p | double | Watts | Single phase IM copper loss [End] if all slots at average Pcu/slot |
| [[motorcad/parameter_database/parameters/PersisentInstanceHandle_Lab|PersisentInstanceHandle_Lab]] | persistent | integer | N/A | Handle for the Lab persistent instance |
| [[motorcad/parameter_database/parameters/Pfe_Back_Iron_1ph_Dist_Schematic_Addition|Pfe_Back_Iron_1ph_Dist_Schematic_Addition]] | o/p | double | Watts | Single phase IM Pfe added to back iron node to give correct power balance in 1-ph IM |
| [[motorcad/parameter_database/parameters/Pfe_Tooth_1ph_Dist_Schematic_Addition|Pfe_Tooth_1ph_Dist_Schematic_Addition]] | o/p | double | Watts | Single phase IM Pfe added to tooth node to give correct power balance in 1-ph IM |
| [[motorcad/parameter_database/parameters/Pfe_Tooth_Tip_1ph_Dist_Schematic_Addition|Pfe_Tooth_Tip_1ph_Dist_Schematic_Addition]] | o/p | double | Watts | Single phase IM Pfe added to tooth tip node to give correct power balance in 1-ph IM |
| [[motorcad/parameter_database/parameters/Plate_Temperature|Plate_Temperature]] | i/p | double | °C | Fixed flange mounted plate temperature |
| [[motorcad/parameter_database/parameters/Power_Copper_Loss_Active_Uneven_Schematic_Addition|Power_Copper_Loss_Active_Uneven_Schematic_Addition]] | o/p | double | Watts | Power Copper Loss Active Uneven Schematic Addition |
| [[motorcad/parameter_database/parameters/Power_Copper_Loss_End_Uneven_Schematic_Addition_F|Power_Copper_Loss_End_Uneven_Schematic_Addition_F]] | o/p | double | Watts | Power Copper Loss End Uneven Schematic Addition [Front] |
| [[motorcad/parameter_database/parameters/Power_Copper_Loss_End_Uneven_Schematic_Addition_R|Power_Copper_Loss_End_Uneven_Schematic_Addition_R]] | o/p | double | Watts | Power Copper Loss End Uneven Schematic Addition [Rear] |
| [[motorcad/parameter_database/parameters/Power_Copper_Loss_Uneven_Schematic_Addition|Power_Copper_Loss_Uneven_Schematic_Addition]] | o/p | double | Watts | Power Copper Loss Uneven Schematic Addition |
| [[motorcad/parameter_database/parameters/Power_Stator_Iron_Loss_Back_Iron_Uneven_Schematic_Addition|Power_Stator_Iron_Loss_Back_Iron_Uneven_Schematic_Addition]] | o/p | double | Watts | Losses added to back iron node to give correct power balance with uneven loss distribution |
| [[motorcad/parameter_database/parameters/ProximityLossModel|ProximityLossModel]] | i/p | integer | N/A | The AC winding loss model selection |
| [[motorcad/parameter_database/parameters/ProximityLossModel_FullFEA_CurrentPlacement|ProximityLossModel_FullFEA_CurrentPlacement]] | compatibility | integer | N/A | Positioning of currents in conductors for Full FEA AC Loss calculation |
| [[motorcad/parameter_database/parameters/ProximityLosses_ShowDetail|ProximityLosses_ShowDetail]] | i/p | boolean | N/A | When this is true then the AC winding loss detail for left and right hand sides of slot are shown in the output sheets |
| [[motorcad/parameter_database/parameters/Rt__Shaft_-_Amb_(Front)_|Rt_(Shaft_-_Amb_(Front))]] | i/p | double | °C/W | No description |
| [[motorcad/parameter_database/parameters/Rt__Shaft_-_Amb_(Rear)_|Rt_(Shaft_-_Amb_(Rear))]] | i/p | double | °C/W | No description |
| [[motorcad/parameter_database/parameters/ShaftSpeed|ShaftSpeed]] | i/p | double | rpm | Requested shaft speed |
| [[motorcad/parameter_database/parameters/Shaft_F_Temperature|Shaft_F_Temperature]] | i/p | double | °C | Fixed Shaft extension [F] temperature |
| [[motorcad/parameter_database/parameters/Shaft_R_Temperature|Shaft_R_Temperature]] | i/p | double | °C | Fixed Shaft extension [R] temperature |
| [[motorcad/parameter_database/parameters/Shaft_Speed_Ref|Shaft_Speed_Ref]] | i/p | double | rpm | Reference shaft speed used for all losses |
| [[motorcad/parameter_database/parameters/Single_Phase_Copper_Loss_Multiplier|Single_Phase_Copper_Loss_Multiplier]] | o/p | double | N/A | Pcu multiplier used in estimation of single phase IM performance |
| [[motorcad/parameter_database/parameters/Stacking_Factor_Rotor|Stacking_Factor_Rotor]] | i/p | double | N/A | Rotor lamination axial stacking factor |
| [[motorcad/parameter_database/parameters/Stacking_Factor_Stator|Stacking_Factor_Stator]] | i/p | double | N/A | Stator lamination axial stacking factor |
| [[motorcad/parameter_database/parameters/Stall_Copper_Loss_Multiplier|Stall_Copper_Loss_Multiplier]] | o/p | double | N/A | Pcu multiplier used in estimation of stall condition |
| [[motorcad/parameter_database/parameters/T_Ambient|T_Ambient]] | i/p | double | °C | Ambient temperature for convection |
| [[motorcad/parameter_database/parameters/T_Ambient_Radiation|T_Ambient_Radiation]] | i/p | double | °C | Ambient temperature for radiation |
| [[motorcad/parameter_database/parameters/Uneven_Copper_Loss_Multiplier|Uneven_Copper_Loss_Multiplier]] | o/p | double | N/A | Pcu multiplier used in estimation of uneven distribution condition |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
