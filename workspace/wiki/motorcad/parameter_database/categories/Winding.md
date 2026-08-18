---
type: motorcad_parameter_category
category_name: Winding
parameter_count: 106
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Winding

## Overview
The **Winding** category contains **106** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/Area_Copper|Area_Copper]] | o/p | double | mm² | Area of wire conductor in the slot (not including insulation) |
| [[motorcad/parameter_database/parameters/Area_Copper_2|Area_Copper_2]] | o/p | double | mm² | Area of the second wire conductor in the slot (not including insulation) |
| [[motorcad/parameter_database/parameters/Area_Copper_3|Area_Copper_3]] | o/p | double | mm² | Area of the third wire conductor in the slot (not including insulation) |
| [[motorcad/parameter_database/parameters/Area_Copper_Total|Area_Copper_Total]] | o/p | double | mm² | Total area of conductor in the slot (not including insulation) |
| [[motorcad/parameter_database/parameters/Area_Covered_Wire|Area_Covered_Wire]] | o/p | double | mm² | Area of wire in the slot (includes wire insulation) |
| [[motorcad/parameter_database/parameters/Area_Covered_Wire_2|Area_Covered_Wire_2]] | o/p | double | mm² | Area of the second wire in the slot (includes wire insulation) |
| [[motorcad/parameter_database/parameters/Area_Covered_Wire_3|Area_Covered_Wire_3]] | o/p | double | mm² | Area of the third wire in the slot (includes wire insulation) |
| [[motorcad/parameter_database/parameters/Area_Covered_Wire_Total|Area_Covered_Wire_Total]] | o/p | double | mm² | Total area of wire in the slot (includes wire insulation) |
| [[motorcad/parameter_database/parameters/Area_Wire_Ins|Area_Wire_Ins]] | o/p | double | mm² | Area of wire insulation in the slot |
| [[motorcad/parameter_database/parameters/Area_Wire_Ins_2|Area_Wire_Ins_2]] | o/p | double | mm² | Area of the second wire insulation in the slot |
| [[motorcad/parameter_database/parameters/Area_Wire_Ins_3|Area_Wire_Ins_3]] | o/p | double | mm² | Area of the third wire insulation in the slot |
| [[motorcad/parameter_database/parameters/Area_Wire_Ins_Total|Area_Wire_Ins_Total]] | o/p | double | mm² | Total area of wire insulation in the slot |
| [[motorcad/parameter_database/parameters/ConductiveWedge|ConductiveWedge]] | recommended | integer | N/A | When enabled the wedge is thermally conductive |
| [[motorcad/parameter_database/parameters/Copper_Area|Copper_Area]] | o/p | double | mm² | No description |
| [[motorcad/parameter_database/parameters/Copper_Slot_Fill_(Wdg_Area)|Copper_Slot_Fill_(Wdg_Area)]] | o/p | double | N/A | No description |
| [[motorcad/parameter_database/parameters/Covered_Wire_Area|Covered_Wire_Area]] | o/p | double | mm² | No description |
| [[motorcad/parameter_database/parameters/CuboidPositionSetting|CuboidPositionSetting]] | compatibility | integer | N/A | Backwards compatiblity setting for slot depth used to position cuboids. |
| [[motorcad/parameter_database/parameters/Dt_WindingAv_Ambient|Dt_WindingAv_Ambient]] | o/p | double | °C | dT used in calculation of Rt[Winding(av)-Ambient] and TC[Winding] |
| [[motorcad/parameter_database/parameters/Dt_WindingAv_Housing|Dt_WindingAv_Housing]] | o/p | double | °C | dT used in calculation of Rt[Winding(av)-Housing] and TC[Winding] |
| [[motorcad/parameter_database/parameters/Dt_WindingMax_Ambient|Dt_WindingMax_Ambient]] | o/p | double | °C | dT used in calculation of Rt[Winding(max)-Ambient] |
| [[motorcad/parameter_database/parameters/Dt_WindingMax_Housing|Dt_WindingMax_Housing]] | o/p | double | °C | dT used in calculation of Rt[Winding(max)-Housing] |
| [[motorcad/parameter_database/parameters/EWdgEffectiveKCalc|EWdgEffectiveKCalc]] | compatibility | integer | N/A | Use of independent End Winding material properties and impreg goodness in the calculation of the End Winding effective k value |
| [[motorcad/parameter_database/parameters/EWdg_Layer_Cond_Mult|EWdg_Layer_Cond_Mult]] | o/p | double | N/A | No description |
| [[motorcad/parameter_database/parameters/FieldConductorPlacement|FieldConductorPlacement]] | setting | integer | N/A | The placement selection of the field winding conductors |
| [[motorcad/parameter_database/parameters/FieldConductorSeparation|FieldConductorSeparation]] | i/p | double | mm | The separation distance between the field winding conductors |
| [[motorcad/parameter_database/parameters/FieldConductorsHorizontal|FieldConductorsHorizontal]] | setting | double | mm | This minimum separation distance between field conductors in slot width direction |
| [[motorcad/parameter_database/parameters/FieldConductorsSlotBase|FieldConductorsSlotBase]] | setting | double | mm | This minimum separation distance from field conductors to the slot base |
| [[motorcad/parameter_database/parameters/FieldConductorsSlotTooth|FieldConductorsSlotTooth]] | setting | double | mm | This minimum separation distance from field conductors to the tooth |
| [[motorcad/parameter_database/parameters/FieldConductorsVertical|FieldConductorsVertical]] | setting | double | mm | This minimum separation distance between field conductors in slot depth direction |
| [[motorcad/parameter_database/parameters/FieldCopperSlotFill|FieldCopperSlotFill]] | o/p | double | N/A | The field copper slot fill factor (Slot Area). |
| [[motorcad/parameter_database/parameters/FieldWindingView|FieldWindingView]] | setting | integer | N/A | Field winding viewing options |
| [[motorcad/parameter_database/parameters/Field_Area_CoilDivider|Field_Area_CoilDivider]] | o/p | double | mm² | Coil divider area (used to separate coils in same slot of non-overlapping windings |
| [[motorcad/parameter_database/parameters/Field_Area_Copper|Field_Area_Copper]] | o/p | double | mm² | Copper area/slot (not including wire insulation) |
| [[motorcad/parameter_database/parameters/Field_Area_Covered_Wire|Field_Area_Covered_Wire]] | o/p | double | mm² | Wire area/slot (includes wire insulation) - calculation based on winding layer model |
| [[motorcad/parameter_database/parameters/Field_Area_Covered_Wire_Round_Conductors|Field_Area_Covered_Wire_Round_Conductors]] | o/p | double | mm² | covered wire area (cond) |
| [[motorcad/parameter_database/parameters/Field_Area_Impreg_No_Liner_Lam|Field_Area_Impreg_No_Liner_Lam]] | o/p | double | mm² | Impregnation area/slot - not including gap between liner and lamination |
| [[motorcad/parameter_database/parameters/Field_Area_Slot|Field_Area_Slot]] | o/p | double | mm² | slot area |
| [[motorcad/parameter_database/parameters/Field_Area_Slot_Wedge|Field_Area_Slot_Wedge]] | o/p | double | mm² | Slot wedge area/slot (includes slot area used to force conductors to base of slot) |
| [[motorcad/parameter_database/parameters/Field_Area_Winding_No_Liner|Field_Area_Winding_No_Liner]] | o/p | double | mm² | Slot area available for winding after liner insertion |
| [[motorcad/parameter_database/parameters/Field_Area_Winding_With_Liner|Field_Area_Winding_With_Liner]] | o/p | double | mm² | Slot area available for winding before liner insertion |
| [[motorcad/parameter_database/parameters/Field_Area_Wire_Ins|Field_Area_Wire_Ins]] | o/p | double | mm² | Wire insulation area/slot |
| [[motorcad/parameter_database/parameters/Field_Covered_Slot_Fill_Actual|Field_Covered_Slot_Fill_Actual]] | o/p | double | N/A | Actual slot fill (wire area/winding area) |
| [[motorcad/parameter_database/parameters/Field_Impreg_Thick|Field_Impreg_Thick]] | o/p | double | mm | Impregnation/airgap thickness between layers of copper in winding |
| [[motorcad/parameter_database/parameters/Field_Impreg_Thick_Layer1|Field_Impreg_Thick_Layer1]] | o/p | double | mm | Impregnation/airgap thickness between outer copper layer and slot liner |
| [[motorcad/parameter_database/parameters/Field_NumWindingLayers|Field_NumWindingLayers]] | o/p | integer | N/A | Number of field winding layers |
| [[motorcad/parameter_database/parameters/Field_Slot_Fill_Wire_Slot|Field_Slot_Fill_Wire_Slot]] | o/p | double | N/A | Slot fill calculated from copper area / slot area (including liner and wedge) |
| [[motorcad/parameter_database/parameters/Field_Uncovered_Slot_Fill_Actual|Field_Uncovered_Slot_Fill_Actual]] | o/p | double | N/A | Actual slot fill (copper area/winding area) |
| [[motorcad/parameter_database/parameters/Field_Wedge_Depth|Field_Wedge_Depth]] | o/p | double | mm | Winding wedge depth (including push back) |
| [[motorcad/parameter_database/parameters/Field_Winding_Depth_Copper|Field_Winding_Depth_Copper]] | o/p | double | mm | Radial depth of winding from slot-opening push-back to to slot-bottom (liner fitted) |
| [[motorcad/parameter_database/parameters/Field_WireIns_Thick|Field_WireIns_Thick]] | o/p | double | mm | Wire insulation thickness |
| [[motorcad/parameter_database/parameters/Field_Wire_Copper_Factor|Field_Wire_Copper_Factor]] | o/p | double | N/A | Field Wire Copper Factor |
| [[motorcad/parameter_database/parameters/FormWoundHorizontalGap|FormWoundHorizontalGap]] | i/p | double | mm | The horizontal separation distance between the conductors |
| [[motorcad/parameter_database/parameters/FormWoundVerticalGap|FormWoundVerticalGap]] | i/p | double | mm | The vertical separation distance between the conductors |
| [[motorcad/parameter_database/parameters/FormWoundWindingDefinitionCalc|FormWoundWindingDefinitionCalc]] | compatibility | integer | N/A | Form wound bar dimensions and their number of columns now automatically calculated |
| [[motorcad/parameter_database/parameters/GrossSlotFillFactor|GrossSlotFillFactor]] | o/p | double | N/A | The gross slot fill of copper in slot (copper area/slot area) |
| [[motorcad/parameter_database/parameters/GrossSlotFillFactorRotor|GrossSlotFillFactorRotor]] | o/p | double | N/A | The gross slot fill of copper in rotor slot (copper area/slot area) |
| [[motorcad/parameter_database/parameters/GrossSlotFillFactor_IM1PH|GrossSlotFillFactor_IM1PH]] | o/p | double | N/A | The gross slot fill of copper in slot (copper area/slot area) (IM1PH) |
| [[motorcad/parameter_database/parameters/Ins_Area_Slot|Ins_Area/Slot]] | o/p | double | mm² | No description |
| [[motorcad/parameter_database/parameters/Kt_LitzBundle_Axial|Kt_LitzBundle_Axial]] | i/p | double | W/m/°C | The axial thermal conductivity of a Litzbundle |
| [[motorcad/parameter_database/parameters/Kt_LitzBundle_Radial|Kt_LitzBundle_Radial]] | i/p | double | W/m/°C | The radial thermal conductivity of a Litzbundle |
| [[motorcad/parameter_database/parameters/Kt_LitzBundle_Tangential|Kt_LitzBundle_Tangential]] | i/p | double | W/m/°C | The tangential thermal conductivity of a Litzbundle |
| [[motorcad/parameter_database/parameters/LitzCopperFillFactor|LitzCopperFillFactor]] | o/p | double | N/A | The litz bundle copper fill (Submember Copper Area/Bundle Area) |
| [[motorcad/parameter_database/parameters/LitzFillFactor|LitzFillFactor]] | o/p | double | N/A | The litz bundle fill (Submember Area/Bundle Area) |
| [[motorcad/parameter_database/parameters/NetSlotFillFactor|NetSlotFillFactor]] | o/p | double | N/A | The net slot fill of wire in slot (Heavy build) |
| [[motorcad/parameter_database/parameters/NetSlotFillFactor_IM1PH|NetSlotFillFactor_IM1PH]] | o/p | double | N/A | The net slot fill of wire in slot (Heavy build) (IM1PH) |
| [[motorcad/parameter_database/parameters/NumRotorConductorsDrawn|NumRotorConductorsDrawn]] | o/p | integer | N/A | The number of turns drawn in field winding |
| [[motorcad/parameter_database/parameters/Periphery__Impreg_Outer_Layer_(Slot_Bottom)_|Periphery_(Impreg_Outer_Layer_(Slot_Bottom))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Impreg_Outer_Layer_(Tooth_Side)_|Periphery_(Impreg_Outer_Layer_(Tooth_Side))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Ins_Outer_Layer_(Slot_Bottom)_|Periphery_(Ins_Outer_Layer_(Slot_Bottom))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Ins_Outer_Layer_(Tooth_Side)_|Periphery_(Ins_Outer_Layer_(Tooth_Side))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Liner-Lam_Gap_|Periphery_(Liner-Lam_Gap)]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Liner-Lam_Gap_(Slot_Bottom)_|Periphery_(Liner-Lam_Gap_(Slot_Bottom))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Liner-Lam_Gap_(Tooth_Side)_|Periphery_(Liner-Lam_Gap_(Tooth_Side))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Liner_|Periphery_(Liner)]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Liner_(Slot_Bottom)_|Periphery_(Liner_(Slot_Bottom))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Periphery__Liner_(Tooth_Side)_|Periphery_(Liner_(Tooth_Side))]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/RequestedGrossSlotFillFactor|RequestedGrossSlotFillFactor]] | i/p | double | N/A | The required gross slot fill of copper in slot |
| [[motorcad/parameter_database/parameters/RequestedGrossSlotFillFactorField|RequestedGrossSlotFillFactorField]] | i/p | double | N/A | The required gross slot fill of copper in field winding slot |
| [[motorcad/parameter_database/parameters/RequestedLitzFillFactor|RequestedLitzFillFactor]] | i/p | double | N/A | The required bundle fill of litz subconductors within a bundle |
| [[motorcad/parameter_database/parameters/RequestedNetSlotFillFactor|RequestedNetSlotFillFactor]] | i/p | double | N/A | The required heavy build slot fill of wire in slot |
| [[motorcad/parameter_database/parameters/RotorInsSlotBaseThickness|RotorInsSlotBaseThickness]] | i/p | double | mm | Insulation thickness of the rotor slot base |
| [[motorcad/parameter_database/parameters/RotorInsToothSideThickness|RotorInsToothSideThickness]] | i/p | double | mm | Insulation thickness of the rotor tooth side |
| [[motorcad/parameter_database/parameters/Rt_RotorInsSlotBase|Rt_RotorInsSlotBase]] | o/p | double | °C/W | Thermal resistance of the slot base insulation |
| [[motorcad/parameter_database/parameters/Rt_RotorInsToothSide|Rt_RotorInsToothSide]] | o/p | double | °C/W | Thermal resistance of the tooth side insulation |
| [[motorcad/parameter_database/parameters/Rt_RotorLam_PoleTip|Rt_RotorLam_PoleTip]] | o/p | double | °C/W | Thermal resistance of the rotor lamination pole tip |
| [[motorcad/parameter_database/parameters/Rt_WindingAv_Ambient|Rt_WindingAv_Ambient]] | o/p | double | °C/W | Thermal resistance between winding average and ambient - [Twinding(average)-Tambient]/Loss(Copper) |
| [[motorcad/parameter_database/parameters/Rt_WindingAv_Ambient_TotalLoss|Rt_WindingAv_Ambient_TotalLoss]] | o/p | double | °C/W | Thermal resistance between winding average and ambient - [Twinding(average)-Tambient]/Total Losses |
| [[motorcad/parameter_database/parameters/Rt_WindingAv_Housing|Rt_WindingAv_Housing]] | o/p | double | °C/W | Thermal resistance between winding average and Housing - [Twinding(average)-THousing]/Loss(Copper) |
| [[motorcad/parameter_database/parameters/Rt_WindingMax_Ambient|Rt_WindingMax_Ambient]] | o/p | double | °C/W | Thermal resistance between winding hot spot and ambient - [Twinding(hot-spot)-Tambient]/Loss(Copper) |
| [[motorcad/parameter_database/parameters/Rt_WindingMax_Ambient_TotalLoss|Rt_WindingMax_Ambient_TotalLoss]] | o/p | double | °C/W | Thermal resistance between winding hot spot and ambient - [Twinding(hot-spot)-Tambient]/Total Losses |
| [[motorcad/parameter_database/parameters/Rt_WindingMax_Housing|Rt_WindingMax_Housing]] | o/p | double | °C/W | Thermal resistance between winding hot spot and Housing - [Twinding(hot-spot)-THousing]/Loss(Copper) |
| [[motorcad/parameter_database/parameters/Slot_Depth_(Windable)|Slot_Depth_(Windable)]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Slot_Fill_(Slot_Area)|Slot_Fill_(Slot_Area)]] | o/p | double | N/A | No description |
| [[motorcad/parameter_database/parameters/SyncRotorCuboid_X|SyncRotorCuboid_X]] | i/p | double | mm | Sync Rotor Cuboid Corner X position |
| [[motorcad/parameter_database/parameters/SyncRotorCuboid_Y|SyncRotorCuboid_Y]] | i/p | double | mm | Sync Rotor Cuboid Corner Y position |
| [[motorcad/parameter_database/parameters/Tw__Lower_|Tw_(Lower)]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Tw__Upper_|Tw_(Upper)]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/UsedCopperThickness|UsedCopperThickness]] | o/p | double | mm | Used Copper Thickness |
| [[motorcad/parameter_database/parameters/UsedWireInsThickness|UsedWireInsThickness]] | o/p | double | mm | Used Wire Ins Thickness |
| [[motorcad/parameter_database/parameters/Wedge_Depth|Wedge_Depth]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/WindingView|WindingView]] | setting | integer | N/A | Display the winding view |
| [[motorcad/parameter_database/parameters/Winding_Depth|Winding_Depth]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Winding_Iterations|Winding_Iterations]] | o/p | integer | N/A | Number of winding iterations required to converge winding layers |
| [[motorcad/parameter_database/parameters/Wire_Copper_Factor|Wire_Copper_Factor]] | o/p | double | N/A | Proportion of wire area that is copper rather than copper+insulation |
| [[motorcad/parameter_database/parameters/Wire_Ins_Thickness|Wire_Ins_Thickness]] | o/p | double | mm | No description |
| [[motorcad/parameter_database/parameters/Wire_Slot_Fill_(Wdg_Area)|Wire_Slot_Fill_(Wdg_Area)]] | o/p | double | N/A | No description |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
