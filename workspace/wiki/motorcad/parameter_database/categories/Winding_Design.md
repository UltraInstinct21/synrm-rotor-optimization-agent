---
type: motorcad_parameter_category
category_name: Winding_Design
parameter_count: 118
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Winding_Design

## Overview
The **Winding_Design** category contains **118** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AWG_WireGaugeIndex|AWG_WireGaugeIndex]] | i/p | integer | N/A | AWG for the first wire type selection |
| [[motorcad/parameter_database/parameters/AWG_WireGaugeIndex_2|AWG_WireGaugeIndex_2]] | i/p | integer | N/A | AWG for the second wire type selection |
| [[motorcad/parameter_database/parameters/AWG_WireGaugeIndex_3|AWG_WireGaugeIndex_3]] | i/p | integer | N/A | AWG for the third wire type selection |
| [[motorcad/parameter_database/parameters/AWG_WireGaugeIndex_Aux|AWG_WireGaugeIndex_Aux]] | i/p | integer | N/A | The index for Aux AWG wire gauge selection |
| [[motorcad/parameter_database/parameters/AWG_WireGaugeIndex_Litz|AWG_WireGaugeIndex_Litz]] | i/p | integer | N/A | The index for the AWG Litz wire gauge selection |
| [[motorcad/parameter_database/parameters/AllowSingleColumnCentring|AllowSingleColumnCentring]] | setting | boolean | N/A | When enabled if slot width is insufficient for 2 columns of conductors then centre a single column |
| [[motorcad/parameter_database/parameters/Armature_CoilStyle|Armature_CoilStyle]] | i/p | integer | N/A | Armature coil style: Stranded or Hairpin |
| [[motorcad/parameter_database/parameters/Armature_WindingType|Armature_WindingType]] | i/p | integer | N/A | Overlapping or non-overlapping winding |
| [[motorcad/parameter_database/parameters/Armature_Winding_Definition|Armature_Winding_Definition]] | i/p | integer | N/A | The winding can be defined by the copper slot fill, wire size, or heavy build slot fill |
| [[motorcad/parameter_database/parameters/Armature_Winding_Definition_Hairpin|Armature_Winding_Definition_Hairpin]] | i/p | integer | N/A | The winding can be defined by the wire size or the seperation |
| [[motorcad/parameter_database/parameters/Coil_Divider_Width|Coil_Divider_Width]] | i/p | double | mm | Clearance between coils in same slot of Non-Overlapping windings |
| [[motorcad/parameter_database/parameters/ConductorCentre_L_x|ConductorCentre_L_x]] | i/p | double | mm | Array of Conductor centre x coordinates at left side of slot |
| [[motorcad/parameter_database/parameters/ConductorCentre_L_y|ConductorCentre_L_y]] | i/p | double | mm | Array of Conductor centre y coordinates at left side of slot |
| [[motorcad/parameter_database/parameters/ConductorCentre_R_x|ConductorCentre_R_x]] | i/p | double | mm | Array of Conductor centre x coordinates at right side of slot |
| [[motorcad/parameter_database/parameters/ConductorCentre_R_y|ConductorCentre_R_y]] | i/p | double | mm | Array of Conductor centre y coordinates at right side of slot |
| [[motorcad/parameter_database/parameters/ConductorHeightRatio|ConductorHeightRatio]] | i/p | double | N/A | The percentage of the total slot height taken up by a conductor |
| [[motorcad/parameter_database/parameters/ConductorHeightRatio_Array|ConductorHeightRatio_Array]] | i/p | double | N/A | The ratio of the height of a conductor against the available slot height |
| [[motorcad/parameter_database/parameters/ConductorHeight_Array|ConductorHeight_Array]] | i/p | double | mm | The height of each hairpin conductor |
| [[motorcad/parameter_database/parameters/ConductorSeparation|ConductorSeparation]] | setting | double | mm | This minimum separation distance between conductors |
| [[motorcad/parameter_database/parameters/ConductorWidth_Array|ConductorWidth_Array]] | i/p | double | mm | The width of each hairpin conductor |
| [[motorcad/parameter_database/parameters/ConductorsHorizontal|ConductorsHorizontal]] | setting | double | mm | This minimum separation distance between conductors in slot width direction |
| [[motorcad/parameter_database/parameters/ConductorsPerSlot|ConductorsPerSlot]] | i/p | integer | N/A | Number of conductors per slot |
| [[motorcad/parameter_database/parameters/ConductorsPerSlot_2|ConductorsPerSlot_2]] | i/p | integer | N/A | Number of wire 2 conductors per slot |
| [[motorcad/parameter_database/parameters/ConductorsPerSlot_3|ConductorsPerSlot_3]] | i/p | integer | N/A | Number of wire 3 conductors per slot |
| [[motorcad/parameter_database/parameters/ConductorsPerSlot_Total|ConductorsPerSlot_Total]] | o/p | integer | N/A | Total number of conductors per slot |
| [[motorcad/parameter_database/parameters/ConductorsSlotBase|ConductorsSlotBase]] | setting | double | mm | This minimum separation distance from conductors to the slot base |
| [[motorcad/parameter_database/parameters/ConductorsSlotTooth|ConductorsSlotTooth]] | setting | double | mm | This minimum separation distance from conductors to the tooth |
| [[motorcad/parameter_database/parameters/ConductorsVertical|ConductorsVertical]] | setting | double | mm | This minimum separation distance between conductors in slot depth direction |
| [[motorcad/parameter_database/parameters/Conductors_Slot_IM1PH|Conductors_Slot_IM1PH]] | o/p | integer | N/A | Total number of conductors (main + aux) in each IM1PH variable depth slot |
| [[motorcad/parameter_database/parameters/CopperLossFillRatio|CopperLossFillRatio]] | o/p | double | N/A | Ratio of total copper loss/fill factor in each IM1PH variable depth slot |
| [[motorcad/parameter_database/parameters/CopperLossPerSlot|CopperLossPerSlot]] | o/p | double | Watts | Total copper loss (Pcu) in each IM1PH variable depth slot |
| [[motorcad/parameter_database/parameters/Copper_Corner_Radius|Copper_Corner_Radius]] | i/p | double | mm | The corner radius of the rectangular copper |
| [[motorcad/parameter_database/parameters/Copper_Corner_Radius_2|Copper_Corner_Radius_2]] | i/p | double | mm | The corner radius of the second conductor |
| [[motorcad/parameter_database/parameters/Copper_Corner_Radius_3|Copper_Corner_Radius_3]] | i/p | double | mm | The corner radius of the third conductor |
| [[motorcad/parameter_database/parameters/Copper_Depth__%_|Copper_Depth_(%)]] | i/p | double | Percent | Percentage of windable slot depth full of copper [i.e. copper forced to slot bottom by wedge] |
| [[motorcad/parameter_database/parameters/Copper_Diameter|Copper_Diameter]] | i/p | double | mm | Uncovered wire (copper) diameter [from wire table or input directly] |
| [[motorcad/parameter_database/parameters/Copper_Diameter_2|Copper_Diameter_2]] | i/p | double | mm | Uncovered wire (copper) diameter of the second wire size |
| [[motorcad/parameter_database/parameters/Copper_Diameter_3|Copper_Diameter_3]] | i/p | double | mm | Uncovered wire (copper) diameter of the third wire size |
| [[motorcad/parameter_database/parameters/Copper_Diameter_Aux|Copper_Diameter_Aux]] | i/p | double | mm | Aux uncovered wire (copper) diameter [from wire table or input directly] |
| [[motorcad/parameter_database/parameters/Copper_Height|Copper_Height]] | i/p | double | mm | The height of the rectangular copper |
| [[motorcad/parameter_database/parameters/Copper_Height_2|Copper_Height_2]] | i/p | double | mm | The height of the second conductor |
| [[motorcad/parameter_database/parameters/Copper_Height_3|Copper_Height_3]] | i/p | double | mm | The height of the third conductor |
| [[motorcad/parameter_database/parameters/Copper_Width|Copper_Width]] | i/p | double | mm | The width of the rectangular copper |
| [[motorcad/parameter_database/parameters/Copper_Width_2|Copper_Width_2]] | i/p | double | mm | The width of the second conductor |
| [[motorcad/parameter_database/parameters/Copper_Width_3|Copper_Width_3]] | i/p | double | mm | The width of the third conductor |
| [[motorcad/parameter_database/parameters/EWdgLayerBendAngle|EWdgLayerBendAngle]] | o/p | double | MDeg | The end winding bend angle of each winding layer |
| [[motorcad/parameter_database/parameters/EWdgLayerLength_F|EWdgLayerLength_F]] | o/p | double | mm | The end winding length of each winding layer [Front] |
| [[motorcad/parameter_database/parameters/EWdgLayerLength_F_Adj|EWdgLayerLength_F_Adj]] | i/p | double | N/A | The end winding length adjusment factor of each winding layer [Front] |
| [[motorcad/parameter_database/parameters/EWdgLayerLength_F_Calc|EWdgLayerLength_F_Calc]] | o/p | double | mm | The calculated end winding length of each winding layer [Front] |
| [[motorcad/parameter_database/parameters/EWdgLayerLength_R|EWdgLayerLength_R]] | o/p | double | mm | The end winding length of each winding layer [Rear] |
| [[motorcad/parameter_database/parameters/EWdgLayerLength_R_Adj|EWdgLayerLength_R_Adj]] | i/p | double | N/A | The end winding length adjustment factor of each winding layer [Rear] |
| [[motorcad/parameter_database/parameters/EWdgLayerLength_R_Calc|EWdgLayerLength_R_Calc]] | o/p | double | mm | The calculated end winding length of each winding layer [Rear] |
| [[motorcad/parameter_database/parameters/EWdg_Fill|EWdg_Fill]] | i/p | double | N/A | Wire fill factor for armature end-winding, i.e. total wire volume/end-winding volume |
| [[motorcad/parameter_database/parameters/EWdg_MLT|EWdg_MLT]] | o/p | double | mm | Mean length per turn of armature conductor endwindings used in the calculation |
| [[motorcad/parameter_database/parameters/HairpinConductorCSA_Array|HairpinConductorCSA_Array]] | o/p | double | mm² | The cross sectional area of this armature conductor |
| [[motorcad/parameter_database/parameters/Imp_Goodness__Active_|Imp_Goodness_(Active)]] | i/p | double | N/A | Multiplier used to enhance/degrade the active impregnation thermal conductivity |
| [[motorcad/parameter_database/parameters/Imp_Goodness__EWdg_|Imp_Goodness_(EWdg)]] | i/p | double | N/A | Multiplier used to enhance/degrade the end-winding impregnation thermal conductivity |
| [[motorcad/parameter_database/parameters/Imp_Goodness__Liner-Lam_|Imp_Goodness_(Liner-Lam)]] | i/p | double | N/A | Multiplier used to enhance/degrade the liner-lamination thermal conductivity |
| [[motorcad/parameter_database/parameters/Imp_Goodness__Litz_|Imp_Goodness_(Litz)]] | i/p | double | N/A | Multiplier used to enhance/degrade the Litz impregnation thermal conductivity |
| [[motorcad/parameter_database/parameters/Ins_Slot_Base_Thickness|Ins_Slot_Base_Thickness]] | i/p | double | mm | Slot base insulation thickness |
| [[motorcad/parameter_database/parameters/Ins_Tooth_Side_Thickness|Ins_Tooth_Side_Thickness]] | i/p | double | mm | Tooth side insulation thickness |
| [[motorcad/parameter_database/parameters/Insulation_Thickness|Insulation_Thickness]] | i/p | double | mm | The insulation thickness of the rectangular coil |
| [[motorcad/parameter_database/parameters/Insulation_Thickness_2|Insulation_Thickness_2]] | i/p | double | mm | The insulation thickness of the second conductor |
| [[motorcad/parameter_database/parameters/Insulation_Thickness_3|Insulation_Thickness_3]] | i/p | double | mm | The insulation thickness of the third conductor |
| [[motorcad/parameter_database/parameters/Liner_-_Lam_Gap|Liner_-_Lam_Gap]] | i/p | double | mm | Gap between liner and lamination (can be air or impregnation - see Mat [Liner-Lam]) |
| [[motorcad/parameter_database/parameters/Liner_Layer_Conductivity|Liner_Layer_Conductivity]] | i/p | double | W/m/°C | Slot Liner Layer Thermal Conductivity |
| [[motorcad/parameter_database/parameters/Liner_Layer_Density|Liner_Layer_Density]] | i/p | double | kg/m³ | Slot Liner Layer Density |
| [[motorcad/parameter_database/parameters/Liner_Layer_Notes|Liner_Layer_Notes]] | i/p | OleStr | N/A | Notes Slot Liner Layer |
| [[motorcad/parameter_database/parameters/Liner_Layer_Specific_Heat|Liner_Layer_Specific_Heat]] | i/p | double | J/kg/°C | Slot Liner Layer Specific Heat Capacity |
| [[motorcad/parameter_database/parameters/Liner_Layer_Thickness|Liner_Layer_Thickness]] | i/p | double | mm | Slot Liner Layer Thickness |
| [[motorcad/parameter_database/parameters/Liner_Layers_Definition|Liner_Layers_Definition]] | i/p | integer | N/A | Model liner as a single layer or with multiple layers with different properties |
| [[motorcad/parameter_database/parameters/Liner_Thickness|Liner_Thickness]] | i/p | double | mm | Slot liner thickness |
| [[motorcad/parameter_database/parameters/Liner_Wire_Gap|Liner_Wire_Gap]] | i/p | double | mm | The distance between the conductor and the liner of the slot |
| [[motorcad/parameter_database/parameters/Liner_Wire_Gap_Array|Liner_Wire_Gap_Array]] | i/p | double | mm | The distances between the conductor and the liner of the slot |
| [[motorcad/parameter_database/parameters/LitzOverallBundleFill|LitzOverallBundleFill]] | o/p | double | N/A | The overall fill factor of a litz bundle |
| [[motorcad/parameter_database/parameters/LitzSubConductor_CopperDiameter|LitzSubConductor_CopperDiameter]] | i/p | double | mm | The uncovered wire (copper) diameter of each subconductor within the litz wire |
| [[motorcad/parameter_database/parameters/LitzSubConductor_WireDiameter|LitzSubConductor_WireDiameter]] | i/p | double | mm | The covered wire diameter of each subconductor within the litz wire (including insulation) |
| [[motorcad/parameter_database/parameters/LitzWireHeight|LitzWireHeight]] | i/p | double | mm | The height of the rectangular litz wire |
| [[motorcad/parameter_database/parameters/LitzWireInsulationThickness|LitzWireInsulationThickness]] | i/p | double | mm | The insulation thickness surrounding the litz wire |
| [[motorcad/parameter_database/parameters/LitzWireSubConductors|LitzWireSubConductors]] | i/p | integer | N/A | The number of subconductors within each litz wire |
| [[motorcad/parameter_database/parameters/LitzWireWidth|LitzWireWidth]] | i/p | double | mm | The width of the rectangular litz wire |
| [[motorcad/parameter_database/parameters/Mat__Liner-Lam_|Mat_(Liner-Lam)]] | i/p | integer | N/A | 0 = Air,     1 = Impregnation |
| [[motorcad/parameter_database/parameters/MaxConductorRows_L|MaxConductorRows_L]] | o/p | integer | N/A | Maximum Rows of Conductors Drawn (Left) |
| [[motorcad/parameter_database/parameters/MaxConductorRows_R|MaxConductorRows_R]] | o/p | integer | N/A | Maximum Rows of Conductors Drawn (Right) |
| [[motorcad/parameter_database/parameters/Metric_WireGaugeIndex|Metric_WireGaugeIndex]] | i/p | integer | N/A | Metric Wire Gauge for the first wire type selection |
| [[motorcad/parameter_database/parameters/Metric_WireGaugeIndex_2|Metric_WireGaugeIndex_2]] | i/p | integer | N/A | Metric Wire Gauge for the second wire type selection |
| [[motorcad/parameter_database/parameters/Metric_WireGaugeIndex_3|Metric_WireGaugeIndex_3]] | i/p | integer | N/A | Metric Wire Gauge for the third wire type selection |
| [[motorcad/parameter_database/parameters/Metric_WireGaugeIndex_Aux|Metric_WireGaugeIndex_Aux]] | i/p | integer | N/A | The index for Aux Metric wire gauge selection |
| [[motorcad/parameter_database/parameters/MinEWdgSeparation|MinEWdgSeparation]] | i/p | double | mm | The minimum separation distance between conductors in the hairpin endwinding |
| [[motorcad/parameter_database/parameters/NoMushConductorsDrawn|NoMushConductorsDrawn]] | o/p | double | N/A | This number of conductors drawn for mush winding (this may not be the number of conductors specified) |
| [[motorcad/parameter_database/parameters/NumberOfWireSizes|NumberOfWireSizes]] | i/p | integer | N/A | Number of wire sizes used to construct the winding |
| [[motorcad/parameter_database/parameters/Number_Liner_Layers|Number_Liner_Layers]] | i/p | integer | N/A | Number of liner layers in Multiple Layer Liner |
| [[motorcad/parameter_database/parameters/Potting_Goodness__EWdg_|Potting_Goodness_(EWdg)]] | i/p | double | N/A | Multiplier used to enhance/degrade the end-winding potting thermal conductivity, i.e. between coil and housing/endcap |
| [[motorcad/parameter_database/parameters/Rotor_Copper_Corner_Radius|Rotor_Copper_Corner_Radius]] | i/p | double | mm | The corner radius of the rectangular copper in rotor winding |
| [[motorcad/parameter_database/parameters/Rotor_Copper_Height|Rotor_Copper_Height]] | i/p | double | mm | The height of the rectangular copper in rotor winding |
| [[motorcad/parameter_database/parameters/Rotor_Copper_Width|Rotor_Copper_Width]] | i/p | double | mm | The width of the rectangular copper in rotor winding |
| [[motorcad/parameter_database/parameters/Rotor_Insulation_Thickness|Rotor_Insulation_Thickness]] | i/p | double | mm | The insulation thickness of the rectangular coil in rotor winding |
| [[motorcad/parameter_database/parameters/Rt_FormWoundCoilBackIron_Multiplier|Rt_FormWoundCoilBackIron_Multiplier]] | i/p | double | N/A | The multiplier for the form wound coil to back iron Resistance |
| [[motorcad/parameter_database/parameters/Rt_FormWoundInnerCoilTooth_Multiplier|Rt_FormWoundInnerCoilTooth_Multiplier]] | i/p | double | N/A | The multiplier for the form wound coil to inner tooth Resistance |
| [[motorcad/parameter_database/parameters/Rt_FormWoundOuterCoilTooth_Multiplier|Rt_FormWoundOuterCoilTooth_Multiplier]] | i/p | double | N/A | The multiplier for the form wound coil to outer tooth Resistance |
| [[motorcad/parameter_database/parameters/SWG_WireGaugeIndex|SWG_WireGaugeIndex]] | i/p | integer | N/A | SWG for the first wire type selection |
| [[motorcad/parameter_database/parameters/SWG_WireGaugeIndex_2|SWG_WireGaugeIndex_2]] | i/p | integer | N/A | SWG for the second wire type selection |
| [[motorcad/parameter_database/parameters/SWG_WireGaugeIndex_3|SWG_WireGaugeIndex_3]] | i/p | integer | N/A | SWG for the third wire type selection |
| [[motorcad/parameter_database/parameters/SlotDepthReduction|SlotDepthReduction]] | i/p | double | mm | reduction of slot depths for IM1PH |
| [[motorcad/parameter_database/parameters/Slot_Fill|Slot_Fill]] | i/p | double | N/A | No description |
| [[motorcad/parameter_database/parameters/StatorPottedEWdg|StatorPottedEWdg]] | i/p | integer | N/A | Is stator end-winding to endcap interface filled with potting material |
| [[motorcad/parameter_database/parameters/Wdg_Definition|Wdg_Definition]] | i/p | integer | N/A | 0 = Input_Slot_Fill, 1 = Input_Conductors_Slot |
| [[motorcad/parameter_database/parameters/Wedge_Model|Wedge_Model]] | i/p | integer | N/A | 0 = Non_Conductive, 1 = Wound_Space, 2 = Conductive, 3 = Air |
| [[motorcad/parameter_database/parameters/Winding_Type|Winding_Type]] | i/p | integer | N/A | 0 = Overlapping, 1 = Solid_Divider (Rectangular), 2 = Air_Divider (Rectangular), 3= Solid_TopBottom_Divider, 4=Air_TopBottom_Divider, 5 = V Solid Divider, 6 = V Air Divider |
| [[motorcad/parameter_database/parameters/Wire_Diameter|Wire_Diameter]] | i/p | double | mm | Covered wire diameter [from wire table or input directly] |
| [[motorcad/parameter_database/parameters/Wire_Diameter_2|Wire_Diameter_2]] | i/p | double | mm | Covered wire diameter of the second wire size |
| [[motorcad/parameter_database/parameters/Wire_Diameter_3|Wire_Diameter_3]] | i/p | double | mm | Covered wire diameter of the third wire size |
| [[motorcad/parameter_database/parameters/Wire_Diameter_Aux|Wire_Diameter_Aux]] | i/p | double | mm | Aux covered wire diameter [from wire table or input directly] |
| [[motorcad/parameter_database/parameters/Wire_Type_Aux|Wire_Type_Aux]] | i/p | integer | N/A | The wire type used in the Aux winding |
| [[motorcad/parameter_database/parameters/Wire_Type_Litz|Wire_Type_Litz]] | i/p | integer | N/A | The wire type used in the litz wire |
| [[motorcad/parameter_database/parameters/Wire_Type_Stator|Wire_Type_Stator]] | i/p | integer | N/A | The main wire type used in the armature winding |
| [[motorcad/parameter_database/parameters/Wire_Type_Stator_2|Wire_Type_Stator_2]] | i/p | integer | N/A | The second wire type used in the armature winding |
| [[motorcad/parameter_database/parameters/Wire_Type_Stator_3|Wire_Type_Stator_3]] | i/p | integer | N/A | The third wire type used in the armature winding |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
