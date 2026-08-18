---
type: motorcad_parameter_category
category_name: Dimensions
parameter_count: 510
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Dimensions

## Overview
The **Dimensions** category contains **510** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AFM_Banding_Depth|AFM_Banding_Depth]] | i/p | double | mm | Axial Flux Banding Depth |
| [[motorcad/parameter_database/parameters/AFM_D_Rotor|AFM_D_Rotor]] | i/p | double | mm | Axial Flux Rotor Outer Diameter |
| [[motorcad/parameter_database/parameters/AFM_D_Shaft|AFM_D_Shaft]] | i/p | double | mm | The shaft outer diameter of Axial Flux machine |
| [[motorcad/parameter_database/parameters/AFM_D_Stator|AFM_D_Stator]] | i/p | double | mm | The stator diameter for axial flux machines |
| [[motorcad/parameter_database/parameters/AFM_D_Stator_Bore|AFM_D_Stator_Bore]] | i/p | double | mm | The stator bore diameter for axial flux machines |
| [[motorcad/parameter_database/parameters/AFM_Magnet_Depth|AFM_Magnet_Depth]] | i/p | double | mm | Axial Flux Magnet Depth |
| [[motorcad/parameter_database/parameters/AFM_Magnet_Embed_Depth|AFM_Magnet_Embed_Depth]] | i/p | double | mm | The embed depth of magnet from rotor outer surface |
| [[motorcad/parameter_database/parameters/AFM_Magnet_Length|AFM_Magnet_Length]] | i/p | double | mm | Axial Flux Magnet Axial Length |
| [[motorcad/parameter_database/parameters/AFM_Rotor_Length|AFM_Rotor_Length]] | i/p | double | mm | Axial Flux Rotor Lamination Length |
| [[motorcad/parameter_database/parameters/AFM_Rotor_Web_Thickness|AFM_Rotor_Web_Thickness]] | i/p | double | mm | The rotor web thickness between poles |
| [[motorcad/parameter_database/parameters/AFM_Stator_Length|AFM_Stator_Length]] | i/p | double | mm | The axial length of each stator region for Axial Flux machines |
| [[motorcad/parameter_database/parameters/AFM_TopologyType|AFM_TopologyType]] | i/p | integer | N/A | Axial flux machine topology type |
| [[motorcad/parameter_database/parameters/ActiveLength|ActiveLength]] | o/p | double | mm | The length of the active part of the machine (stator lam, rotor lam and magnets). Used for the optiSLang export. |
| [[motorcad/parameter_database/parameters/Airgap|Airgap]] | i/p | double | mm | Airgap - including any stator bore sleeve or magnet retainment banding |
| [[motorcad/parameter_database/parameters/Area_CoilDivider|Area_CoilDivider]] | o/p | double | mm² | Coil divider area (used to separate coils in same slot of non-overlapping windings |
| [[motorcad/parameter_database/parameters/Area_Covered_Wire_Round_Conductors|Area_Covered_Wire_Round_Conductors]] | o/p | double | mm² | Round conductor wire area/slot (includes wire insulation) - calc based on actual conductors |
| [[motorcad/parameter_database/parameters/Area_Gap_Liner_Lam|Area_Gap_Liner_Lam]] | o/p | double | mm² | Gap area/slot between liner & lamination |
| [[motorcad/parameter_database/parameters/Area_Impreg_Liner_Lam|Area_Impreg_Liner_Lam]] | o/p | double | mm² | Impregnation area/slot between liner & lamination |
| [[motorcad/parameter_database/parameters/Area_Impreg_No_Liner_Lam|Area_Impreg_No_Liner_Lam]] | o/p | double | mm² | Impregnation area/slot - not including gap between liner and lamination |
| [[motorcad/parameter_database/parameters/Area_Liner|Area_Liner]] | o/p | double | mm² | Liner area/slot - not including gap between liner and lamination |
| [[motorcad/parameter_database/parameters/Area_Slot|Area_Slot]] | o/p | double | mm² | Slot area - including liner and wedge but not slot opening |
| [[motorcad/parameter_database/parameters/Area_SlotOpening|Area_SlotOpening]] | o/p | double | mm² | Slot opening area/slot |
| [[motorcad/parameter_database/parameters/Area_SlotWedge|Area_SlotWedge]] | o/p | double | mm² | Slot wedge area/slot (includes slot area used to force conductors to base of slot) |
| [[motorcad/parameter_database/parameters/Area_Slot_NoWedge|Area_Slot_NoWedge]] | o/p | double | mm² | Slot area - including liner but not slot opening or wedge |
| [[motorcad/parameter_database/parameters/Area_Winding_No_Liner|Area_Winding_No_Liner]] | o/p | double | mm² | Slot area available for winding after liner insertion |
| [[motorcad/parameter_database/parameters/Area_Winding_With_Liner|Area_Winding_With_Liner]] | o/p | double | mm² | Slot area available for winding before liner insertion |
| [[motorcad/parameter_database/parameters/Armature_Diameter|Armature_Diameter]] | i/p | double | mm | BPMOR/PMDC/WFC armature diameter |
| [[motorcad/parameter_database/parameters/AxialSegments|AxialSegments]] | i/p | integer | N/A | The number of axial segments that each magnet is split into |
| [[motorcad/parameter_database/parameters/AxialWJFinNumberCalc|AxialWJFinNumberCalc]] | compatibility | integer | N/A | Calculation of fin number for machines with Axial Covered Fins |
| [[motorcad/parameter_database/parameters/AxleOHang_F|AxleOHang_F]] | i/p | double | mm | The overhang of active section of axle over front of stator lamination |
| [[motorcad/parameter_database/parameters/AxleOHang_R|AxleOHang_R]] | i/p | double | mm | The overhang of active section of axle over rear of stator lamination |
| [[motorcad/parameter_database/parameters/Axle_Dia|Axle_Dia]] | i/p | double | mm | Axle diameter [active section of motor] |
| [[motorcad/parameter_database/parameters/Axle_Dia__F_|Axle_Dia_(F)]] | i/p | double | mm | Axle diameter [front of motor] |
| [[motorcad/parameter_database/parameters/Axle_Dia__R_|Axle_Dia_(R)]] | i/p | double | mm | Axle diameter [rear of motor] |
| [[motorcad/parameter_database/parameters/Axle_Extension__F_|Axle_Extension_(F)]] | i/p | double | mm | Amount by which Axle extends beyond housing at front of motor |
| [[motorcad/parameter_database/parameters/Axle_Extension__R_|Axle_Extension_(R)]] | i/p | double | mm | Amount by which Axle extends beyond housing at rear of motor |
| [[motorcad/parameter_database/parameters/Axle_Plate_Height__F_|Axle_Plate_Height_(F)]] | i/p | double | mm | Axle Plate Height [F] |
| [[motorcad/parameter_database/parameters/Axle_Plate_Height__R_|Axle_Plate_Height_(R)]] | i/p | double | mm | Axle Plate Height [R] |
| [[motorcad/parameter_database/parameters/Axle_Plate_Thickness__F_|Axle_Plate_Thickness_(F)]] | i/p | double | mm | BPMOR axle mounted cooling plate axial thickness |
| [[motorcad/parameter_database/parameters/Axle_Plate_Thickness__R|Axle_Plate_Thickness_(R]] | i/p | double | mm | BPMOR axle mounted cooling plate axial thickness |
| [[motorcad/parameter_database/parameters/Axle_Plate_Width__F_|Axle_Plate_Width_(F)]] | i/p | double | mm | Axle Plate Width Front |
| [[motorcad/parameter_database/parameters/Axle_Plate_Width__R_|Axle_Plate_Width_(R)]] | i/p | double | mm | Axle Plate Width [R] |
| [[motorcad/parameter_database/parameters/BackIronShape_WFC|BackIronShape_WFC]] | i/p | integer | N/A | The shape of the outer back iron for WFC machines |
| [[motorcad/parameter_database/parameters/BackIronThickness_Outer|BackIronThickness_Outer]] | i/p | double | mm | The thickness of the outer lamination back iron |
| [[motorcad/parameter_database/parameters/Back_Iron_Thickness|Back_Iron_Thickness]] | i/p | double | mm | BPMOR/PMDC back iron thickness (back of magnets) |
| [[motorcad/parameter_database/parameters/BandingAxialSegments|BandingAxialSegments]] | i/p | integer | N/A | The number of axial segments that banding is split into |
| [[motorcad/parameter_database/parameters/Banding_Thickness|Banding_Thickness]] | i/p | double | mm | Rotor retaining sleeve/banding radial thickness |
| [[motorcad/parameter_database/parameters/Bar Corner Radius_T_|Bar Corner Radius(T)]] | i/p | double | mm | The top bar corner radius |
| [[motorcad/parameter_database/parameters/Bar Depth _B_|Bar Depth (B)]] | i/p | double | mm | The bottom bar depth |
| [[motorcad/parameter_database/parameters/Bar Depth _T_|Bar Depth (T)]] | i/p | double | mm | The top bar depth |
| [[motorcad/parameter_database/parameters/Bar Opening Depth _B_|Bar Opening Depth (B)]] | i/p | double | mm | The bottom bar opening depth |
| [[motorcad/parameter_database/parameters/Bar Opening Depth _T_|Bar Opening Depth (T)]] | i/p | double | mm | The top bar opening depth |
| [[motorcad/parameter_database/parameters/Bar Opening _B_|Bar Opening (B)]] | i/p | double | mm | The bottom bar opening width |
| [[motorcad/parameter_database/parameters/Bar Opening _T_|Bar Opening (T)]] | i/p | double | mm | The top bar opening width |
| [[motorcad/parameter_database/parameters/Bar Tip Angle _T_|Bar Tip Angle (T)]] | i/p | double | MDeg | The top bar tip angle |
| [[motorcad/parameter_database/parameters/Bar Width _B_|Bar Width (B)]] | i/p | double | mm | The bottom bar width |
| [[motorcad/parameter_database/parameters/Bar Width _T_|Bar Width (T)]] | i/p | double | mm | The top bar width |
| [[motorcad/parameter_database/parameters/BarB_Corner_Radius|BarB_Corner_Radius]] | i/p | double | mm | The bottom bar corner radius |
| [[motorcad/parameter_database/parameters/BarB_Opening_Radius|BarB_Opening_Radius]] | i/p | double | mm | The bottom bar opening corner radius |
| [[motorcad/parameter_database/parameters/BarB_Tip_Angle|BarB_Tip_Angle]] | i/p | double | MDeg | The bottom bar tip angle |
| [[motorcad/parameter_database/parameters/BarT_Opening_Radius|BarT_Opening_Radius]] | i/p | double | mm | The top bar opening corner radius |
| [[motorcad/parameter_database/parameters/Base_Length|Base_Length]] | i/p | double | mm | Foot mounted base axial length |
| [[motorcad/parameter_database/parameters/Base_Thickness|Base_Thickness]] | i/p | double | mm | Foot mounted base thickness |
| [[motorcad/parameter_database/parameters/Base_Width|Base_Width]] | i/p | double | mm | Foot mounted base width |
| [[motorcad/parameter_database/parameters/BearingInner_Diameter|BearingInner_Diameter]] | i/p | double | mm | The bearing inner diameter for single bearing model |
| [[motorcad/parameter_database/parameters/BearingMount_Gap|BearingMount_Gap]] | i/p | double | mm | The gap between bearing mount and endcap for single bearing model |
| [[motorcad/parameter_database/parameters/BearingMount_Length|BearingMount_Length]] | i/p | double | mm | The bearing mount length for single bearing model |
| [[motorcad/parameter_database/parameters/BearingMount_Thickness|BearingMount_Thickness]] | i/p | double | mm | The bearing mount thickness for single bearing model |
| [[motorcad/parameter_database/parameters/Bearing_Dia__F_|Bearing_Dia_(F)]] | i/p | double | mm | Bearing diameter [front of motor] |
| [[motorcad/parameter_database/parameters/Bearing_Dia__R_|Bearing_Dia_(R)]] | i/p | double | mm | Bearing diameter [rear of motor] |
| [[motorcad/parameter_database/parameters/Bearing_Offset__F_|Bearing_Offset_(F)]] | i/p | double | mm | Bearing axial offset [front of motor], +ve moves within motor |
| [[motorcad/parameter_database/parameters/Bearing_Offset__R_|Bearing_Offset_(R)]] | i/p | double | mm | Bearing axial offset [rear of motor], +ve moves within motor |
| [[motorcad/parameter_database/parameters/Bearing_Width__F_|Bearing_Width_(F)]] | i/p | double | mm | Bearing width [front of motor] |
| [[motorcad/parameter_database/parameters/Bearing_Width__R_|Bearing_Width_(R)]] | i/p | double | mm | Bearing width [rear of motor] |
| [[motorcad/parameter_database/parameters/Br_Holder_Comm_Gap|Br_Holder_Comm_Gap]] | i/p | double | mm | gap between Brush Holder and Commutator surface |
| [[motorcad/parameter_database/parameters/Br_Holder_Height|Br_Holder_Height]] | i/p | double | mm | Brush Holder Height - metalic section hieght |
| [[motorcad/parameter_database/parameters/Br_Holder_Ins_Thick|Br_Holder_Ins_Thick]] | i/p | double | mm | Brush Holder Insulation Radial Thickness |
| [[motorcad/parameter_database/parameters/Br_Holder_Outer_Dia|Br_Holder_Outer_Dia]] | i/p | double | mm | Brush Holder Outer Diameter |
| [[motorcad/parameter_database/parameters/BridgeThickness_Array|BridgeThickness_Array]] | i/p | double | mm | The bridge thickness for the interior V-Shape magnet layer |
| [[motorcad/parameter_database/parameters/Bridge_Thickness|Bridge_Thickness]] | i/p | double | mm | The magnet bridge thickness for the interior Flat, V-Shape and U-Shape magnets |
| [[motorcad/parameter_database/parameters/Brush_Height|Brush_Height]] | i/p | double | mm | brush height |
| [[motorcad/parameter_database/parameters/Brush_Holder_Inner_Dia|Brush_Holder_Inner_Dia]] | o/p | double | mm | Brush holder insulation inner diameter |
| [[motorcad/parameter_database/parameters/Brush_Holder_Ins_Height|Brush_Holder_Ins_Height]] | o/p | double | mm | Brush holder insulation height |
| [[motorcad/parameter_database/parameters/Brush_Holder_Thickness_AXS|Brush_Holder_Thickness_AXS]] | o/p | double | mm | Brush holder thickness (metalic section) - axial cross section |
| [[motorcad/parameter_database/parameters/Brush_Holder_Thickness_RXS|Brush_Holder_Thickness_RXS]] | o/p | double | mm | Brush holder thickness (metalic section) - radial cross section |
| [[motorcad/parameter_database/parameters/Brush_Length|Brush_Length]] | i/p | double | mm | brush axial length |
| [[motorcad/parameter_database/parameters/Brush_Number|Brush_Number]] | i/p | integer | N/A | brush number |
| [[motorcad/parameter_database/parameters/Brush_Width|Brush_Width]] | i/p | double | mm | brush width |
| [[motorcad/parameter_database/parameters/CalculateInputWJFlowChannels|CalculateInputWJFlowChannels]] | i/p | integer | N/A | Calculate input water jacket channel number (need not be integer) |
| [[motorcad/parameter_database/parameters/CircumferentialSegments|CircumferentialSegments]] | i/p | integer | N/A | The number of radial segments that each magnet is split into |
| [[motorcad/parameter_database/parameters/Claw_Back_Iron|Claw_Back_Iron]] | i/p | double | mm | Claw pole motor back iron thickness |
| [[motorcad/parameter_database/parameters/Claw_Coil_Depth|Claw_Coil_Depth]] | i/p | double | mm | Claw pole motor radial coil depth |
| [[motorcad/parameter_database/parameters/Claw_Coil_Length|Claw_Coil_Length]] | i/p | double | mm | Claw pole motor axial coil length |
| [[motorcad/parameter_database/parameters/Claw_Liner_Base|Claw_Liner_Base]] | i/p | double | mm | Claw pole motor liner thickness at base of coil |
| [[motorcad/parameter_database/parameters/Claw_Liner_Side|Claw_Liner_Side]] | i/p | double | mm | Claw pole motor liner thickness ar side of coil |
| [[motorcad/parameter_database/parameters/Claw_Pole_Angle|Claw_Pole_Angle]] | o/p | double | MDeg | claw pole taper angle |
| [[motorcad/parameter_database/parameters/Claw_Pole_Depth|Claw_Pole_Depth]] | i/p | double | mm | Claw pole motor radial pole depth |
| [[motorcad/parameter_database/parameters/Claw_Pole_Length|Claw_Pole_Length]] | i/p | double | mm | Claw pole motor axial pole length |
| [[motorcad/parameter_database/parameters/Claw_Pole_Pairs|Claw_Pole_Pairs]] | i/p | integer | N/A | Claw pole motor pole pairs |
| [[motorcad/parameter_database/parameters/Claw_Pole_Spacing|Claw_Pole_Spacing]] | i/p | double | mm | Claw pole motor pole spacing |
| [[motorcad/parameter_database/parameters/Claw_Pole_Thickness|Claw_Pole_Thickness]] | o/p | double | mm | main rotor pole axial length |
| [[motorcad/parameter_database/parameters/Claw_Pole_Tip_Angle_Upper|Claw_Pole_Tip_Angle_Upper]] | o/p | double | MDeg | claw pole tip angle |
| [[motorcad/parameter_database/parameters/Claw_Pole_Tip_Width_Upper|Claw_Pole_Tip_Width_Upper]] | o/p | double | mm | claw pole tip width |
| [[motorcad/parameter_database/parameters/Claw_Pole_Width_Base|Claw_Pole_Width_Base]] | o/p | double | mm | claw pole width base |
| [[motorcad/parameter_database/parameters/Claw_Pole_Width_Top|Claw_Pole_Width_Top]] | o/p | double | mm | claw pole width top |
| [[motorcad/parameter_database/parameters/Claw_Tooth_Depth|Claw_Tooth_Depth]] | i/p | double | mm | Claw pole motor tooth tip depth |
| [[motorcad/parameter_database/parameters/Claw_Tooth_Width|Claw_Tooth_Width]] | i/p | double | mm | Claw pole tooth tip width |
| [[motorcad/parameter_database/parameters/CoilDividerOffset|CoilDividerOffset]] | i/p | double | mm | Offset of coil divider from middle of slot |
| [[motorcad/parameter_database/parameters/CoilDividerWidth_Outer|CoilDividerWidth_Outer]] | i/p | double | mm | The width of the outer coil dividers |
| [[motorcad/parameter_database/parameters/CoilDivider_DepthReduction_Rotor|CoilDivider_DepthReduction_Rotor]] | i/p | double | mm | The depth reduction of the Rotor Coil Divider |
| [[motorcad/parameter_database/parameters/CoilDivider_DepthReduction_Stator|CoilDivider_DepthReduction_Stator]] | i/p | double | mm | The depth reduction of the Stator Coil Divider |
| [[motorcad/parameter_database/parameters/CoilInsArea|CoilInsArea]] | o/p | double | mm² | The area of the coil insulation |
| [[motorcad/parameter_database/parameters/ColumnsConductorsCalc|ColumnsConductorsCalc]] | o/p | integer | N/A | The calculated number of conductors across each form wound slot |
| [[motorcad/parameter_database/parameters/Comm_Connection_Lmult|Comm_Connection_Lmult]] | i/p | double | N/A | connection length multiplier [winding to commutator wires] |
| [[motorcad/parameter_database/parameters/Comm_Connections|Comm_Connections]] | i/p | integer | N/A | number of connections (wires) between winding and commutator |
| [[motorcad/parameter_database/parameters/Comm_Cu_Thickness|Comm_Cu_Thickness]] | i/p | double | mm | Commutator copper radial thickness |
| [[motorcad/parameter_database/parameters/Comm_Dia|Comm_Dia]] | i/p | double | mm | Commutator diameter |
| [[motorcad/parameter_database/parameters/Comm_Length|Comm_Length]] | i/p | double | mm | Commutator axial length |
| [[motorcad/parameter_database/parameters/ConductorHeightCalc|ConductorHeightCalc]] | o/p | double | mm | The calculated height of each conductor bar |
| [[motorcad/parameter_database/parameters/ConductorWidthCalc|ConductorWidthCalc]] | o/p | double | mm | The calculated width of each conductor bar |
| [[motorcad/parameter_database/parameters/CornerRoundingRadius_Magnets|CornerRoundingRadius_Magnets]] | i/p | double | mm | The single value radius for all corner rounding on magnets. |
| [[motorcad/parameter_database/parameters/CornerRoundingRadius_Rotor|CornerRoundingRadius_Rotor]] | i/p | double | mm | The single value radius for corner rounding on any rotor lamination corners. |
| [[motorcad/parameter_database/parameters/Corner_Cutout_Add|Corner_Cutout_Add]] | i/p | double | mm | Housing corner cutout inner diameter material thickness addition |
| [[motorcad/parameter_database/parameters/Corner_Cutout__%_|Corner_Cutout_(%)]] | i/p | double | Percent | Housing corner cutout for inserting Flange mounted bolts [% of Housing Dia. (SQ) or 1/4 periphery (RND)] |
| [[motorcad/parameter_database/parameters/Cover_Ins_Length|Cover_Ins_Length]] | i/p | double | mm | Outer cover isnsulation axial length |
| [[motorcad/parameter_database/parameters/Cover_Ins_Thickness|Cover_Ins_Thickness]] | i/p | double | mm | Outer cover insulation thickness |
| [[motorcad/parameter_database/parameters/CoveredWireArea|CoveredWireArea]] | o/p | double | mm² | The area of the wire (copper + insulation) |
| [[motorcad/parameter_database/parameters/Cup_Axial_Length|Cup_Axial_Length]] | i/p | double | mm | BPMOR rotor cup axial length |
| [[motorcad/parameter_database/parameters/Cup_Axial_Thickness|Cup_Axial_Thickness]] | i/p | double | mm | BPMOR rotor cup axial thickess |
| [[motorcad/parameter_database/parameters/Cup_Radial_Thickness|Cup_Radial_Thickness]] | i/p | double | mm | BPMOR rotor cup radial thickess |
| [[motorcad/parameter_database/parameters/DamperBar_Depth|DamperBar_Depth]] | i/p | double | mm | This is the depth of the Damper Bars from the airgap |
| [[motorcad/parameter_database/parameters/DamperBar_Diameter|DamperBar_Diameter]] | i/p | double | mm | This is the diameter of each Damper Bar |
| [[motorcad/parameter_database/parameters/DamperBar_Number|DamperBar_Number]] | i/p | integer | N/A | This is the number of Damper Bars in each rotor pole |
| [[motorcad/parameter_database/parameters/DamperBar_Opening|DamperBar_Opening]] | i/p | double | mm | This is the opening width of the Damper Bars |
| [[motorcad/parameter_database/parameters/DamperBar_Pitch|DamperBar_Pitch]] | i/p | double | EDeg | This is the overall Damper Bar pitch per rotor pole |
| [[motorcad/parameter_database/parameters/Damper_Extension_F|Damper_Extension_F]] | i/p | double | mm | Extension of front Damper Bars from rotor lam before meeting end ring |
| [[motorcad/parameter_database/parameters/Damper_Extension_R|Damper_Extension_R]] | i/p | double | mm | Extension of rear Damper Bars from rotor lam before meeting end ring |
| [[motorcad/parameter_database/parameters/Damper_Inner_Add_F|Damper_Inner_Add_F]] | i/p | double | mm | Material added to front Damper End Ring inner radius |
| [[motorcad/parameter_database/parameters/Damper_Inner_Add_R|Damper_Inner_Add_R]] | i/p | double | mm | Material added to rear Damper End Ring inner radius |
| [[motorcad/parameter_database/parameters/Damper_Outer_Add_F|Damper_Outer_Add_F]] | i/p | double | mm | Material added to front Damper End Ring outer radius |
| [[motorcad/parameter_database/parameters/Damper_Outer_Add_R|Damper_Outer_Add_R]] | i/p | double | mm | Material added to rear Damper End Ring outer radius |
| [[motorcad/parameter_database/parameters/Damper_Thickness_F|Damper_Thickness_F]] | i/p | double | mm | Thickness of front Damper End Ring |
| [[motorcad/parameter_database/parameters/Damper_Thickness_R|Damper_Thickness_R]] | i/p | double | mm | Thickness of rear Damper End Ring |
| [[motorcad/parameter_database/parameters/EWdg-Bore__F_|EWdg-Bore_(F)]] | i/p | double | mm | Gap between end winding and bore [front of motor] |
| [[motorcad/parameter_database/parameters/EWdg-Bore__R_|EWdg-Bore_(R)]] | i/p | double | mm | Gap between end winding and bore [rear of motor] |
| [[motorcad/parameter_database/parameters/EWdg-Endcap__F_|EWdg-Endcap_(F)]] | i/p | double | mm | Gap between end winding and endcap [front of motor] |
| [[motorcad/parameter_database/parameters/EWdg-Endcap__R_|EWdg-Endcap_(R)]] | i/p | double | mm | Gap between end winding and endcap [rear of motor] |
| [[motorcad/parameter_database/parameters/EWdg-Housing__F_|EWdg-Housing_(F)]] | i/p | double | mm | Gap between end winding and housing [front of motor] |
| [[motorcad/parameter_database/parameters/EWdg-Housing__R_|EWdg-Housing_(R)]] | i/p | double | mm | Gap between end winding and housing [rear of motor] |
| [[motorcad/parameter_database/parameters/EWdg_Insulation__F_|EWdg_Insulation_(F)]] | i/p | double | mm | End Winding Insulation Thickness - around the outer surface of the end winding |
| [[motorcad/parameter_database/parameters/EWdg_Insulation__R_|EWdg_Insulation_(R)]] | i/p | double | mm | End Winding Insulation Thickness - around the outer surface of the end winding |
| [[motorcad/parameter_database/parameters/EWdg_Overhang_Mult__F_|EWdg_Overhang_Mult_(F)]] | i/p | double | N/A | Multiplier for the front end winding overhang |
| [[motorcad/parameter_database/parameters/EWdg_Overhang_Mult__R_|EWdg_Overhang_Mult_(R)]] | i/p | double | N/A | Multiplier for the rear end winding overhang |
| [[motorcad/parameter_database/parameters/EWdg_Overhang__F_|EWdg_Overhang_(F)]] | i/p | double | mm | End winding axial overhang [front of motor] |
| [[motorcad/parameter_database/parameters/EWdg_Overhang__F__Used|EWdg_Overhang_(F)_Used]] | o/p | double | mm | End winding axial overhang [front of motor] |
| [[motorcad/parameter_database/parameters/EWdg_Overhang__R_|EWdg_Overhang_(R)]] | i/p | double | mm | End winding axial overhang [rear of motor] |
| [[motorcad/parameter_database/parameters/EWdg_Overhang__R__Used|EWdg_Overhang_(R)_Used]] | o/p | double | mm | End winding axial overhang including multiplier [rear of motor] |
| [[motorcad/parameter_database/parameters/Enc_Axial_Gap|Enc_Axial_Gap]] | i/p | double | mm | Gap between encoder and encoder case in axial direction |
| [[motorcad/parameter_database/parameters/Enc_Barrier_Length|Enc_Barrier_Length]] | i/p | double | mm | Axial length of thermal barrier between motor shaft and encoder shaft |
| [[motorcad/parameter_database/parameters/Enc_Case_Dia|Enc_Case_Dia]] | i/p | double | mm | Encoder case outer diameter |
| [[motorcad/parameter_database/parameters/Enc_Case_Length|Enc_Case_Length]] | i/p | double | mm | Encoder case axial length |
| [[motorcad/parameter_database/parameters/Enc_Case_Thick|Enc_Case_Thick]] | i/p | double | mm | Encoder case material thickness |
| [[motorcad/parameter_database/parameters/Enc_Length|Enc_Length]] | i/p | double | mm | Encoder axial length |
| [[motorcad/parameter_database/parameters/Enc_Radial_Gap|Enc_Radial_Gap]] | i/p | double | mm | Gap between encoder and encoder case in radial direction |
| [[motorcad/parameter_database/parameters/Enc_Shaft_Dia|Enc_Shaft_Dia]] | i/p | double | mm | Encoder shaft diameter - also diameter of barrier between motor shaft and encoder shaft |
| [[motorcad/parameter_database/parameters/EndRing_Depth_F|EndRing_Depth_F]] | o/p | double | mm | Depth of front end ring |
| [[motorcad/parameter_database/parameters/EndRing_Depth_R|EndRing_Depth_R]] | o/p | double | mm | Depth of rear end ring |
| [[motorcad/parameter_database/parameters/EndRing_Extension_F|EndRing_Extension_F]] | i/p | double | mm | Extension of rotor bars from rotor lam before meet the front rotor end ring |
| [[motorcad/parameter_database/parameters/EndRing_Extension_R|EndRing_Extension_R]] | i/p | double | mm | Extension of rotor bars from rotor lam before meet the front rotor end ring |
| [[motorcad/parameter_database/parameters/EndRing_Inner_Add_F|EndRing_Inner_Add_F]] | i/p | double | mm | Material added to front end ring inner radius |
| [[motorcad/parameter_database/parameters/EndRing_Inner_Add_R|EndRing_Inner_Add_R]] | i/p | double | mm | Material added to front end ring inner radius |
| [[motorcad/parameter_database/parameters/EndRing_Inner_Diameter_F|EndRing_Inner_Diameter_F]] | o/p | double | mm | Inner Diameter of front end ring |
| [[motorcad/parameter_database/parameters/EndRing_Inner_Diameter_R|EndRing_Inner_Diameter_R]] | o/p | double | mm | Inner Diameter of rear end ring |
| [[motorcad/parameter_database/parameters/EndRing_Outer_Add_F|EndRing_Outer_Add_F]] | i/p | double | mm | Material added to front end ring outer radius |
| [[motorcad/parameter_database/parameters/EndRing_Outer_Add_R|EndRing_Outer_Add_R]] | i/p | double | mm | Material added to front end ring outer radius |
| [[motorcad/parameter_database/parameters/EndRing_Thickness_F|EndRing_Thickness_F]] | i/p | double | mm | Thickness of front rotor end ring |
| [[motorcad/parameter_database/parameters/EndRing_Thickness_R|EndRing_Thickness_R]] | i/p | double | mm | Thickness of front rotor end ring |
| [[motorcad/parameter_database/parameters/Endcap_Length__F_|Endcap_Length_(F)]] | i/p | double | mm | End cap axial length [front of motor] |
| [[motorcad/parameter_database/parameters/Endcap_Length__R_|Endcap_Length_(R)]] | i/p | double | mm | End cap axial length [rear of motor] |
| [[motorcad/parameter_database/parameters/Endcap_Thickness__F_|Endcap_Thickness_(F)]] | i/p | double | mm | Endcap Material Thickness [Drive End] |
| [[motorcad/parameter_database/parameters/Endcap_Thickness__R_|Endcap_Thickness_(R)]] | i/p | double | mm | Endcap Material Thickness [Non-Drive End] |
| [[motorcad/parameter_database/parameters/Fan_AxialPosition|Fan_AxialPosition]] | i/p | double | mm | This is the axial position of the shaft mounted fan. |
| [[motorcad/parameter_database/parameters/Fan_BackPlate_Dia|Fan_BackPlate_Dia]] | i/p | double | mm | This is the diameter of the shaft mounted fan back plate. |
| [[motorcad/parameter_database/parameters/Fan_BackPlate_Width|Fan_BackPlate_Width]] | i/p | double | mm | This is the axial width of the shaft mounted fan back plate. |
| [[motorcad/parameter_database/parameters/Fan_Blade_Axial_Offset|Fan_Blade_Axial_Offset]] | i/p | double | mm | This is the axial offset the fan blades. |
| [[motorcad/parameter_database/parameters/Fan_Blade_Thickness|Fan_Blade_Thickness]] | i/p | double | mm | This is the thickness of the fan blades. |
| [[motorcad/parameter_database/parameters/Fan_Blade_Width|Fan_Blade_Width]] | i/p | double | mm | This is the width the shaft mounted fan blades. |
| [[motorcad/parameter_database/parameters/Fan_Diameter|Fan_Diameter]] | i/p | double | mm | This is the diameter of the shaft mounted fan. |
| [[motorcad/parameter_database/parameters/Fan_Hub_Dia|Fan_Hub_Dia]] | i/p | double | mm | This is the diameter of the shaft mounted fan hub. |
| [[motorcad/parameter_database/parameters/Fan_Hub_Extension|Fan_Hub_Extension]] | i/p | double | mm | This is the axial extension of the shaft mounted fan hub. |
| [[motorcad/parameter_database/parameters/Feet_Length|Feet_Length]] | i/p | double | mm | Feet axial length |
| [[motorcad/parameter_database/parameters/Feet_Width__Base_|Feet_Width_(Base)]] | i/p | double | mm | Feet width at junction with base [assuming 2 feet] |
| [[motorcad/parameter_database/parameters/Feet_Width__Motor_|Feet_Width_(Motor)]] | i/p | double | mm | Feet width at junction with motor [assuming 2 feet] |
| [[motorcad/parameter_database/parameters/Fin_Base_Thickness|Fin_Base_Thickness]] | i/p | double | mm | Fin Base Thickness - Covered Round Axial Fin Housing |
| [[motorcad/parameter_database/parameters/Fin_Cover_Thickness|Fin_Cover_Thickness]] | i/p | double | mm | Fin Cover Thickness - Covered Round Axial Fin Housing |
| [[motorcad/parameter_database/parameters/Fin_Extension|Fin_Extension]] | i/p | double | mm | Fin extension beyond Housing Dia. |
| [[motorcad/parameter_database/parameters/Fin_Number__Quadrant_|Fin_Number_(Quadrant)]] | i/p | integer | N/A | Fin number per quarter housing (full length of machine in a radial finned housing) |
| [[motorcad/parameter_database/parameters/Fin_Number__Total_|Fin_Number_(Total)]] | i/p | integer | N/A | Fin Number [Total] |
| [[motorcad/parameter_database/parameters/Fin_Pitch|Fin_Pitch]] | o/p | double | mm | Fin pitch (calculated from fin thickness & fin pitch to thickness ratio) |
| [[motorcad/parameter_database/parameters/Fin_Pitch_Thick|Fin_Pitch/Thick]] | i/p | double | N/A | Fin pitch/thickness ratio |
| [[motorcad/parameter_database/parameters/Fin_Spacing__Fin_Base_|Fin_Spacing_(Fin_Base)]] | i/p | double | N/A | Fin spacing at base of fin channel |
| [[motorcad/parameter_database/parameters/Fin_Thickness|Fin_Thickness]] | i/p | double | mm | Fin thickness [use average thickness if fins are tapered] |
| [[motorcad/parameter_database/parameters/Flange_Depth|Flange_Depth]] | i/p | double | mm | Amount that Flange extends axially beyond housing, i.e. Flange mounting interface |
| [[motorcad/parameter_database/parameters/Flange_Dia|Flange_Dia]] | i/p | double | mm | Flange diameter - section that locates on flange mounted plate |
| [[motorcad/parameter_database/parameters/Flange_Extension|Flange_Extension]] | i/p | double | mm | Amount that Flange extends beyond Housing Dia. in a radial direction |
| [[motorcad/parameter_database/parameters/FlatMagnetSegments|FlatMagnetSegments]] | i/p | integer | N/A | The number of radial segments that each flat magnet is split into |
| [[motorcad/parameter_database/parameters/FormWoundCopperArea|FormWoundCopperArea]] | o/p | double | mm² | The area of the copper |
| [[motorcad/parameter_database/parameters/FormWound_WedgeDepth|FormWound_WedgeDepth]] | i/p | double | mm | The distance from stator bore to wedge for form wound machines |
| [[motorcad/parameter_database/parameters/Gap_H-Cup__Axial_|Gap_H-Cup_(Axial)]] | i/p | double | mm | Gap between housing and rotor cup (axial direction) |
| [[motorcad/parameter_database/parameters/Gap_H-Cup__Radial_|Gap_H-Cup_(Radial)]] | i/p | double | mm | Gap between housing and rotor cup (radial direction) |
| [[motorcad/parameter_database/parameters/Gap_Potting-Axle__F_|Gap_Potting-Axle_(F)]] | i/p | double | mm | Gap between potting and axle (front of motor) |
| [[motorcad/parameter_database/parameters/Gap_Potting-Axle__R_|Gap_Potting-Axle_(R)]] | i/p | double | mm | Gap between potting and axle (rear of motor) |
| [[motorcad/parameter_database/parameters/Gap_Shaft-Axle|Gap_Shaft-Axle]] | i/p | double | mm | Housed BPMOR - gap between rotating shaft and static axle (active section) |
| [[motorcad/parameter_database/parameters/Gap_Shaft-Axle__F_|Gap_Shaft-Axle_(F)]] | i/p | double | mm | Housed BPMOR - gap between rotating shaft and static axle (front section) |
| [[motorcad/parameter_database/parameters/Gap_Shaft-Axle__R_|Gap_Shaft-Axle_(R)]] | i/p | double | mm | Housed BPMOR - gap between rotating shaft and static axle (rear section) |
| [[motorcad/parameter_database/parameters/Gap_StatorPlateMount_F|Gap_StatorPlateMount_F]] | i/p | double | mm | The radial gap between the front stator plate and bearing mount for single bearing model |
| [[motorcad/parameter_database/parameters/Gap_StatorPlateMount_R|Gap_StatorPlateMount_R]] | i/p | double | mm | The radial gap between rear stator plate and bearing mount for single bearing model |
| [[motorcad/parameter_database/parameters/Gap__Comm-Winding_|Gap_(Comm-Winding)]] | i/p | double | mm | Gap between commutator and winding |
| [[motorcad/parameter_database/parameters/Gap__Endcap-Comm_|Gap_(Endcap-Comm)]] | i/p | double | mm | Gap between endcap and commutator |
| [[motorcad/parameter_database/parameters/Housing_Dia|Housing_Dia]] | i/p | double | mm | Housing outer diameter |
| [[motorcad/parameter_database/parameters/Housing_Thickness|Housing_Thickness]] | i/p | double | mm | BPMOR/PMDC housing thickness (back of magnets) |
| [[motorcad/parameter_database/parameters/IM_Pole_Number|IM_Pole_Number]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/ImpregArea|ImpregArea]] | o/p | double | mm² | The area of the impregnation |
| [[motorcad/parameter_database/parameters/Insulation Tooth Width|Insulation Tooth Width]] | i/p | double | mm | Thickness of non conducting barrier (Slotless) |
| [[motorcad/parameter_database/parameters/L_Breadloaf_Magnet|L_Breadloaf_Magnet]] | o/p | double | mm | Breadloaf Magnet Length |
| [[motorcad/parameter_database/parameters/LinerLamImpArea|LinerLamImpArea]] | o/p | double | mm² | The slot area between the slot liner and the lamination |
| [[motorcad/parameter_database/parameters/Liner_Coil_Base|Liner_Coil_Base]] | i/p | double | mm | rotor coil liner thickness [coil base] |
| [[motorcad/parameter_database/parameters/Liner_Pole_Side|Liner_Pole_Side]] | i/p | double | mm | rotor pole liner thickness [pole side] |
| [[motorcad/parameter_database/parameters/Liner_Pole_Tip|Liner_Pole_Tip]] | i/p | double | mm | rotor pole liner thickness [pole tips] |
| [[motorcad/parameter_database/parameters/Liner_Rotor_EWdg|Liner_Rotor_EWdg]] | i/p | double | mm | Liner thickness between rotor end winding and rotor pole |
| [[motorcad/parameter_database/parameters/MagnetBarWidth_Array|MagnetBarWidth_Array]] | i/p | double | mm | The bar width for the interior V-Shape magnet layer |
| [[motorcad/parameter_database/parameters/MagnetCentralArc_HalbachRing|MagnetCentralArc_HalbachRing]] | i/p | double | EDeg | The angle of the pole central magnet in Halbach Continuous Ring arrays in electrical degrees |
| [[motorcad/parameter_database/parameters/MagnetClearance|MagnetClearance]] | i/p | double | mm | The clearance for the embedded magnet |
| [[motorcad/parameter_database/parameters/MagnetDepth|MagnetDepth]] | i/p | double | mm | Spoke magnet depth |
| [[motorcad/parameter_database/parameters/MagnetInset|MagnetInset]] | i/p | double | mm | Spoke magnet inset distance from rotor surface |
| [[motorcad/parameter_database/parameters/MagnetOpening|MagnetOpening]] | i/p | double | mm | Spoke magnet opening distance |
| [[motorcad/parameter_database/parameters/MagnetReduction|MagnetReduction]] | i/p | double | mm | The thickness reduction of Surface Magnets |
| [[motorcad/parameter_database/parameters/MagnetSeparation_Array|MagnetSeparation_Array]] | i/p | double | mm | The magnet separation for the interior V-Shape magnet layer |
| [[motorcad/parameter_database/parameters/MagnetThickness_Array|MagnetThickness_Array]] | i/p | double | mm | The magnet radial thickness for the interior V-Shape magnet layer |
| [[motorcad/parameter_database/parameters/Magnet_Arc__ED_|Magnet_Arc_(ED)]] | i/p | double | EDeg | Magnet arc [electrical degrees] |
| [[motorcad/parameter_database/parameters/Magnet_Axial_Offset|Magnet_Axial_Offset]] | i/p | double | mm | Amount that axial center of magnet is offset from stator stack axial center [+ve towards front of motor] |
| [[motorcad/parameter_database/parameters/Magnet_Embed_Depth|Magnet_Embed_Depth]] | i/p | double | mm | How far magnet is inset into the rotor lamination in an IPM motor |
| [[motorcad/parameter_database/parameters/Magnet_Layers|Magnet_Layers]] | i/p | integer | N/A | The number of layers of U-Shape magnets |
| [[motorcad/parameter_database/parameters/Magnet_Length|Magnet_Length]] | i/p | double | mm | Magnet axial length |
| [[motorcad/parameter_database/parameters/Magnet_Post|Magnet_Post]] | i/p | double | mm | The thickness of the magnet post |
| [[motorcad/parameter_database/parameters/Magnet_Separation|Magnet_Separation]] | i/p | double | mm | The gap between the two pole magnets for interior V-Shape magnets |
| [[motorcad/parameter_database/parameters/Magnet_Thickness|Magnet_Thickness]] | i/p | double | mm | Magnet radial thickness |
| [[motorcad/parameter_database/parameters/Magnet_Width|Magnet_Width]] | i/p | double | mm | The width of each flat magnet block |
| [[motorcad/parameter_database/parameters/Magnet_Width_Reduction|Magnet_Width_Reduction]] | i/p | double | mm | The magnet width reduction for the interior Flat and V-Shape magnets |
| [[motorcad/parameter_database/parameters/MinBackIronThickness|MinBackIronThickness]] | i/p | double | mm | Minimum allowable thickness of stator back iron |
| [[motorcad/parameter_database/parameters/MinBottomRotorBarOpening|MinBottomRotorBarOpening]] | i/p | double | mm | Minimum allowable width of bottom rotor bar opening |
| [[motorcad/parameter_database/parameters/MinMagnetSeparation|MinMagnetSeparation]] | i/p | double | mm | Minimum allowable distance between interior magnet poles |
| [[motorcad/parameter_database/parameters/MinRotorBarSeparation|MinRotorBarSeparation]] | i/p | double | mm | Minimum allowable distance between rotor bars |
| [[motorcad/parameter_database/parameters/MinRotorBarWidth|MinRotorBarWidth]] | i/p | double | mm | Minimum allowable width of rotor bar |
| [[motorcad/parameter_database/parameters/MinShaftSeparation|MinShaftSeparation]] | i/p | double | mm | Minimum allowable distance between interior magnets and shaft |
| [[motorcad/parameter_database/parameters/MinUMagnetAspectRatio_Inner|MinUMagnetAspectRatio_Inner]] | i/p | double | N/A | Minimum allowable aspect ratio of inner U magnets |
| [[motorcad/parameter_database/parameters/MinUMagnetAspectRatio_Outer|MinUMagnetAspectRatio_Outer]] | i/p | double | N/A | Minimum allowable aspect ratio of outer U magnets |
| [[motorcad/parameter_database/parameters/MinVMagnetAspectRatio|MinVMagnetAspectRatio]] | i/p | double | N/A | Minimum allowable aspect ratio of interior V magnets |
| [[motorcad/parameter_database/parameters/Motor_Length|Motor_Length]] | i/p | double | mm | Motor axial length [including end-cap thickness] |
| [[motorcad/parameter_database/parameters/NumStatorVarSlotDepths|NumStatorVarSlotDepths]] | i/p | integer | N/A | Number of Stator Variable Slot Depths |
| [[motorcad/parameter_database/parameters/Periphery_Gap_Liner_Lam_Slot_Bottom|Periphery_Gap_Liner_Lam_Slot_Bottom]] | o/p | double | mm | Periphery Gap Liner Lam Slot Bottom |
| [[motorcad/parameter_database/parameters/Periphery_Gap_Liner_Lam_Tooth_Side|Periphery_Gap_Liner_Lam_Tooth_Side]] | o/p | double | mm | Average Periphery of Gap between liner and stator lamination [one whole slot] (Tooth Side) |
| [[motorcad/parameter_database/parameters/Periphery_Liner_Slot_Bottom|Periphery_Liner_Slot_Bottom]] | o/p | double | mm | Average Periphery of slot liner [one whole slot] (Slot Bottom) |
| [[motorcad/parameter_database/parameters/Periphery_Liner_Tooth_Side|Periphery_Liner_Tooth_Side]] | o/p | double | mm | Average Periphery of slot liner [one whole slot] (Tooth Side) |
| [[motorcad/parameter_database/parameters/Periphery_Rotor_Bars|Periphery_Rotor_Bars]] | o/p | double | mm | Periphery of total rotor cage slots |
| [[motorcad/parameter_database/parameters/PhaseSeparatorArea|PhaseSeparatorArea]] | o/p | double | mm² | The area of the phase separator |
| [[motorcad/parameter_database/parameters/Plate_Height|Plate_Height]] | i/p | double | mm | Flange mounted cooling plate height |
| [[motorcad/parameter_database/parameters/Plate_Thickness|Plate_Thickness]] | i/p | double | mm | Flange mounted cooling plate axial thickness |
| [[motorcad/parameter_database/parameters/Plate_Width|Plate_Width]] | i/p | double | mm | Flange mounted cooling plate width |
| [[motorcad/parameter_database/parameters/PoleArc_Array|PoleArc_Array]] | i/p | double | EDeg | The pole arc for the interior V-Shape layer in electrical degrees |
| [[motorcad/parameter_database/parameters/PoleNotchArc_Inner|PoleNotchArc_Inner]] | i/p | double | mm | The inner arc of the rotor lam inter pole notch |
| [[motorcad/parameter_database/parameters/PoleNotchArc_Outer|PoleNotchArc_Outer]] | i/p | double | EDeg | The outer arc of the rotor lam inter pole notch |
| [[motorcad/parameter_database/parameters/PoleNotchDepth|PoleNotchDepth]] | i/p | double | mm | The radial depth of the rotor lam inter pole notch |
| [[motorcad/parameter_database/parameters/PoleNumber_Outer|PoleNumber_Outer]] | i/p | integer | mm | The number of outer poles |
| [[motorcad/parameter_database/parameters/PoleSideAngle|PoleSideAngle]] | i/p | double | MDeg | The angle of the pole side in the Parallel Tooth Rotor |
| [[motorcad/parameter_database/parameters/PoleTipAngle|PoleTipAngle]] | i/p | double | MDeg | The angle of the pole tip in the Parallel Slot rotor |
| [[motorcad/parameter_database/parameters/PoleTipRadialDepth|PoleTipRadialDepth]] | i/p | double | mm | The radial depth of the pole tip in the Parallel Tooth and Parallel Slot rotors |
| [[motorcad/parameter_database/parameters/PoleVAngle_Array|PoleVAngle_Array]] | i/p | double | MDeg | The pole V angle for the interior V-Shape layer in mechanical degrees |
| [[motorcad/parameter_database/parameters/Pole_Arc|Pole_Arc]] | i/p | double | EDeg | The pole arc for the interior V-Shape layer in electrical degrees |
| [[motorcad/parameter_database/parameters/Pole_Base_Radius|Pole_Base_Radius]] | i/p | double | mm | Radius of curvature for corner of slot at base of pole |
| [[motorcad/parameter_database/parameters/Pole_Depth|Pole_Depth]] | i/p | double | mm | Pole depth (not including tip) |
| [[motorcad/parameter_database/parameters/Pole_Number|Pole_Number]] | i/p | integer | N/A | Pole number |
| [[motorcad/parameter_database/parameters/Pole_Surface_Offset|Pole_Surface_Offset]] | i/p | double | mm | Pole surface radius centre offset |
| [[motorcad/parameter_database/parameters/Pole_Surface_Radius|Pole_Surface_Radius]] | i/p | double | mm | Pole surface radius |
| [[motorcad/parameter_database/parameters/Pole_Tip_Depth|Pole_Tip_Depth]] | i/p | double | mm | Pole tip depth |
| [[motorcad/parameter_database/parameters/Pole_Tip_Radius|Pole_Tip_Radius]] | i/p | double | mm | Radius of curvature for corner of slot at tip of pole |
| [[motorcad/parameter_database/parameters/Pole_Tip_Width|Pole_Tip_Width]] | i/p | double | mm | Pole tip width |
| [[motorcad/parameter_database/parameters/Pole_V_Angle|Pole_V_Angle]] | i/p | double | MDeg | The angle between the pole magnets for the interior V-Shape magnets [degrees] |
| [[motorcad/parameter_database/parameters/Pole_Width|Pole_Width]] | i/p | double | mm | Pole width (not including tip) |
| [[motorcad/parameter_database/parameters/Potting-Endcap__F_|Potting-Endcap_(F)]] | i/p | double | mm | Gap between potting and endcap (front of motor) |
| [[motorcad/parameter_database/parameters/Potting-Endcap__R_|Potting-Endcap_(R)]] | i/p | double | mm | Gap between potting and endcap (rear of motor) |
| [[motorcad/parameter_database/parameters/Potting-Housing__F_|Potting-Housing_(F)]] | i/p | double | mm | Gap between potting and housing (front of motor) |
| [[motorcad/parameter_database/parameters/Potting-Housing__R_|Potting-Housing_(R)]] | i/p | double | mm | Gap between potting and housing (rear of motor) |
| [[motorcad/parameter_database/parameters/RadialDuctType|RadialDuctType]] | i/p | integer | N/A | The type of radial ducts in the machine |
| [[motorcad/parameter_database/parameters/RotorDiameter|RotorDiameter]] | i/p | double | mm | The rotor diameter not including banding |
| [[motorcad/parameter_database/parameters/RotorGridDepth|RotorGridDepth]] | i/p | double | mm | The depth of each of the Rotor grids |
| [[motorcad/parameter_database/parameters/RotorGridHeight|RotorGridHeight]] | i/p | double | mm | The height of the Rotor grids |
| [[motorcad/parameter_database/parameters/RotorGridNumber|RotorGridNumber]] | i/p | integer | N/A | The number of Rotor grids in each radial duct |
| [[motorcad/parameter_database/parameters/RotorGridOuterDiameter|RotorGridOuterDiameter]] | i/p | double | mm | The outer diameter of the Rotor grids |
| [[motorcad/parameter_database/parameters/RotorLaminationInset|RotorLaminationInset]] | i/p | double | mm | The inset distance of the rotor pole lamination |
| [[motorcad/parameter_database/parameters/RotorOuterDiameter|RotorOuterDiameter]] | i/p | double | mm | The rotor outer diameter not including housing |
| [[motorcad/parameter_database/parameters/RotorPlate_Thickness_F|RotorPlate_Thickness_F]] | i/p | double | mm | Thickness of front rotor clamp plate |
| [[motorcad/parameter_database/parameters/RotorPlate_Thickness_R|RotorPlate_Thickness_R]] | i/p | double | mm | Thickness of rear rotor clamp plate |
| [[motorcad/parameter_database/parameters/RotorPoleTaper|RotorPoleTaper]] | i/p | double | MDeg | The taper angle of the rotor pole sides |
| [[motorcad/parameter_database/parameters/RotorRadialDuct_Number|RotorRadialDuct_Number]] | i/p | integer | N/A | Number of rotor radial ducts |
| [[motorcad/parameter_database/parameters/RotorRadialDuct_Width|RotorRadialDuct_Width]] | i/p | double | mm | Width of rotor radial duct |
| [[motorcad/parameter_database/parameters/RotorSlotFilletRadius|RotorSlotFilletRadius]] | i/p | double | mm | The radius of the rotor slot fillets |
| [[motorcad/parameter_database/parameters/RotorSlots|RotorSlots]] | i/p | integer | N/A | Number of Rotor Slots |
| [[motorcad/parameter_database/parameters/RotorYokeThickness|RotorYokeThickness]] | o/p | double | mm | The thickness of the rotor yoke in sync machine |
| [[motorcad/parameter_database/parameters/Rotor_Axial_Offset|Rotor_Axial_Offset]] | i/p | double | mm | Amount that axial center of rotor stack is offset from stator stack axial center [+ve towards front of motor] |
| [[motorcad/parameter_database/parameters/Rotor_Bars|Rotor_Bars]] | i/p | integer | N/A | Induction Motor Rotor Slots/Bars |
| [[motorcad/parameter_database/parameters/Rotor_Coil_Depth|Rotor_Coil_Depth]] | i/p | double | mm | rotor pole coil depth (without liner) |
| [[motorcad/parameter_database/parameters/Rotor_Coil_Width|Rotor_Coil_Width]] | i/p | double | mm | rotor pole coil width (without liner) |
| [[motorcad/parameter_database/parameters/Rotor_EWdg_Ohang|Rotor_EWdg_Ohang]] | i/p | double | mm | Rotor end winding overhang |
| [[motorcad/parameter_database/parameters/Rotor_Lam_Length|Rotor_Lam_Length]] | i/p | double | mm | Rotor lamination stack axial length |
| [[motorcad/parameter_database/parameters/Rotor_Pole_Angle|Rotor_Pole_Angle]] | i/p | double | MDeg | SRM Rotor Pole Angle at Rotor Surface |
| [[motorcad/parameter_database/parameters/Rotor_Pole_Arc|Rotor_Pole_Arc]] | i/p | double | EDeg | Angle of the rotor pole arc |
| [[motorcad/parameter_database/parameters/Rotor_Pole_Tip_Side|Rotor_Pole_Tip_Side]] | i/p | double | mm | Length of the flat side of the pole tip |
| [[motorcad/parameter_database/parameters/Rotor_Pole_Width|Rotor_Pole_Width]] | o/p | double | mm | SRM Rotor Pole Width |
| [[motorcad/parameter_database/parameters/Rotor_Slot_Depth|Rotor_Slot_Depth]] | i/p | double | mm | SRM Rotor Pole Depth |
| [[motorcad/parameter_database/parameters/Rotor_Tooth_Width_B|Rotor_Tooth_Width_B]] | i/p | double | mm | The bottom bar rotor lamination tooth width |
| [[motorcad/parameter_database/parameters/Rotor_Tooth_Width_T|Rotor_Tooth_Width_T]] | i/p | double | mm | The top bar rotor lamination tooth width |
| [[motorcad/parameter_database/parameters/Rotor_WJ_Duct_Diameter|Rotor_WJ_Duct_Diameter]] | i/p | double | mm | Rotor Water Jacket Duct Diameter |
| [[motorcad/parameter_database/parameters/RoundStatorDiameter_WFC_Outer|RoundStatorDiameter_WFC_Outer]] | i/p | double | mm | The diameter of round WFC stator laminations |
| [[motorcad/parameter_database/parameters/ShaftType|ShaftType]] | i/p | integer | N/A | The type of shaft in machine (0=solid or 1=spider). |
| [[motorcad/parameter_database/parameters/Shaft_Dia|Shaft_Dia]] | i/p | double | mm | Shaft diameter [active section of motor] |
| [[motorcad/parameter_database/parameters/Shaft_Dia__F_|Shaft_Dia_(F)]] | i/p | double | mm | Shaft diameter [front of motor] |
| [[motorcad/parameter_database/parameters/Shaft_Dia__R_|Shaft_Dia_(R)]] | i/p | double | mm | Shaft diameter [rear of motor] |
| [[motorcad/parameter_database/parameters/Shaft_Extension__F_|Shaft_Extension_(F)]] | i/p | double | mm | Amount by which shaft extends beyond housing at front of motor |
| [[motorcad/parameter_database/parameters/Shaft_Extension__R_|Shaft_Extension_(R)]] | i/p | double | mm | Amount by which shaft extends beyond housing at rear of motor |
| [[motorcad/parameter_database/parameters/Shaft_Groove_Height|Shaft_Groove_Height]] | i/p | double | mm | Shaft spiral groove channel height |
| [[motorcad/parameter_database/parameters/Shaft_Groove_Spacing|Shaft_Groove_Spacing]] | i/p | double | mm | Shaft spiral groove channel spacing |
| [[motorcad/parameter_database/parameters/Shaft_Groove_Wall|Shaft_Groove_Wall]] | i/p | double | mm | Spacing between shaft spiral groove channel and lamination |
| [[motorcad/parameter_database/parameters/Shaft_Groove_Width|Shaft_Groove_Width]] | i/p | double | mm | Shaft spiral groove channel width |
| [[motorcad/parameter_database/parameters/Shaft_Height|Shaft_Height]] | i/p | double | mm | Height of shaft above Foot mounted base |
| [[motorcad/parameter_database/parameters/Shaft_To_Pole_Min|Shaft_To_Pole_Min]] | i/p | double | mm | Minimum distance between shaft and pole |
| [[motorcad/parameter_database/parameters/SleeveAxialSegments|SleeveAxialSegments]] | i/p | integer | N/A | The number of axial segments that sleeve is split into |
| [[motorcad/parameter_database/parameters/Sleeve_Thickness|Sleeve_Thickness]] | i/p | double | mm | Stator bore sleeve radial thickness |
| [[motorcad/parameter_database/parameters/SlotDepth_Outer|SlotDepth_Outer]] | i/p | double | mm | The depth of the outer slots |
| [[motorcad/parameter_database/parameters/Slot_Corner_Radius|Slot_Corner_Radius]] | i/p | double | mm | Radius of corner at slot base |
| [[motorcad/parameter_database/parameters/Slot_Depth|Slot_Depth]] | i/p | double | mm | Slot depth - bore to slot bottom |
| [[motorcad/parameter_database/parameters/Slot_Number|Slot_Number]] | i/p | integer | N/A | Slot number |
| [[motorcad/parameter_database/parameters/Slot_Opening|Slot_Opening]] | i/p | double | mm | Slot opening |
| [[motorcad/parameter_database/parameters/Slot_WJ_Duct_Height|Slot_WJ_Duct_Height]] | i/p | double | mm | slot water jacket duct height |
| [[motorcad/parameter_database/parameters/Slot_WJ_Duct_Parallel_Paths|Slot_WJ_Duct_Parallel_Paths]] | i/p | integer | N/A | number of slot water jacket parallel flow paths |
| [[motorcad/parameter_database/parameters/Slot_WJ_Duct_Width|Slot_WJ_Duct_Width]] | i/p | double | mm | slot water jacket duct width |
| [[motorcad/parameter_database/parameters/Slot_WJ_Insulation_Thickness|Slot_WJ_Insulation_Thickness]] | i/p | double | mm | slot water jacket insulation thickness - between duct and winding |
| [[motorcad/parameter_database/parameters/Slot_WJ_Wall_Thickness|Slot_WJ_Wall_Thickness]] | i/p | double | mm | slot water jacket duct wall thickness (tube thickness) |
| [[motorcad/parameter_database/parameters/Slot_Width|Slot_Width]] | i/p | double | mm | Slot width (parallel slots) |
| [[motorcad/parameter_database/parameters/Slot_Width_Bottom|Slot_Width_Bottom]] | i/p | double | mm | Width of slot at slot bottom |
| [[motorcad/parameter_database/parameters/Slot_Width_Top|Slot_Width_Top]] | i/p | double | mm | Width of slot at slot top |
| [[motorcad/parameter_database/parameters/SpiderArmLength|SpiderArmLength]] | i/p | double | mm | The length of the shaft spider arm |
| [[motorcad/parameter_database/parameters/SpiderArmWidth|SpiderArmWidth]] | i/p | double | mm | The width of the spider arm |
| [[motorcad/parameter_database/parameters/SpiderRadialThickness|SpiderRadialThickness]] | i/p | double | mm | The radial thickness of the spider arm |
| [[motorcad/parameter_database/parameters/SpokeMagnetSegments|SpokeMagnetSegments]] | i/p | integer | N/A | The number of radial segments that each spoke magnet block is split into |
| [[motorcad/parameter_database/parameters/SquareStatorLam_CornerRadius|SquareStatorLam_CornerRadius]] | i/p | double | mm | The radius of the corners of square WFC stator laminations |
| [[motorcad/parameter_database/parameters/SquareStatorLam_Height|SquareStatorLam_Height]] | i/p | double | mm | The height of square laminations |
| [[motorcad/parameter_database/parameters/SquareStatorLam_Width|SquareStatorLam_Width]] | i/p | double | mm | The width of square laminations |
| [[motorcad/parameter_database/parameters/StatorClampPlateThickness_F|StatorClampPlateThickness_F]] | i/p | double | mm | The thickness of the front stator clamping plate |
| [[motorcad/parameter_database/parameters/StatorClampPlateThickness_R|StatorClampPlateThickness_R]] | i/p | double | mm | The thickness of the rear stator clamping plate |
| [[motorcad/parameter_database/parameters/StatorGridDepth|StatorGridDepth]] | i/p | double | mm | The depth of each of the stator grids |
| [[motorcad/parameter_database/parameters/StatorGridHeight|StatorGridHeight]] | i/p | double | mm | The height of the stator grids |
| [[motorcad/parameter_database/parameters/StatorGridInnerDiameter|StatorGridInnerDiameter]] | i/p | double | mm | The inner diameter of the stator grids |
| [[motorcad/parameter_database/parameters/StatorGridNumber|StatorGridNumber]] | i/p | integer | N/A | The number of stator grids in each radial duct |
| [[motorcad/parameter_database/parameters/StatorMidSlotTooth_Depth|StatorMidSlotTooth_Depth]] | i/p | double | Percent | The depth of the mid slot tooth as a proportion of available copper depth. |
| [[motorcad/parameter_database/parameters/StatorMidSlotTooth_Width_Base|StatorMidSlotTooth_Width_Base]] | i/p | double | mm | The width of the mid slot tooth at the slot bottom. |
| [[motorcad/parameter_database/parameters/StatorMidSlotTooth_Width_Top|StatorMidSlotTooth_Width_Top]] | i/p | double | mm | The width of the mid slot tooth at the slot opening. |
| [[motorcad/parameter_database/parameters/StatorPlateChannelHeight_F|StatorPlateChannelHeight_F]] | i/p | double | mm | The channel height of front stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannelHeight_R|StatorPlateChannelHeight_R]] | i/p | double | mm | The channel height of rear stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannelSpacing_F|StatorPlateChannelSpacing_F]] | i/p | double | mm | The channel spacing of front stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannelSpacing_R|StatorPlateChannelSpacing_R]] | i/p | double | mm | The channel spacing of rear stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannelWall_F|StatorPlateChannelWall_F]] | i/p | double | mm | The channel wall width of front stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannelWall_R|StatorPlateChannelWall_R]] | i/p | double | mm | The channel wall width of rear stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannelWidth_F|StatorPlateChannelWidth_F]] | i/p | double | mm | The channel width of front stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannelWidth_R|StatorPlateChannelWidth_R]] | i/p | double | mm | The channel width of rear stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannels_F|StatorPlateChannels_F]] | i/p | double | N/A | The number of channels in front stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateChannels_R|StatorPlateChannels_R]] | i/p | double | N/A | The number of channels in rear stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateOffset_F|StatorPlateOffset_F]] | i/p | double | mm | The offset of the front stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateOffset_R|StatorPlateOffset_R]] | i/p | double | mm | The offset of the rear stator plate for single bearing model from |
| [[motorcad/parameter_database/parameters/StatorPlateThickness_F|StatorPlateThickness_F]] | i/p | double | mm | The thickness of the front stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPlateThickness_R|StatorPlateThickness_R]] | i/p | double | mm | The thickness of the rear stator plate for single bearing model |
| [[motorcad/parameter_database/parameters/StatorPole_TaperAngle|StatorPole_TaperAngle]] | i/p | double | MDeg | The taper angle of the SRM Stator Pole tooth |
| [[motorcad/parameter_database/parameters/StatorRadialDuct_Number|StatorRadialDuct_Number]] | i/p | integer | N/A | Number of stator radial ducts |
| [[motorcad/parameter_database/parameters/StatorRadialDuct_Width|StatorRadialDuct_Width]] | i/p | double | mm | Width of stator radial duct |
| [[motorcad/parameter_database/parameters/Stator_Axial_Offset|Stator_Axial_Offset]] | i/p | double | mm | Amount that axial center of stator stack is offset from housing axial center [+ve towards front of motor] |
| [[motorcad/parameter_database/parameters/Stator_Bore|Stator_Bore]] | i/p | double | mm | Stator bore diameter |
| [[motorcad/parameter_database/parameters/Stator_Lam_Dia|Stator_Lam_Dia]] | i/p | double | mm | Stator lamination outer diameter |
| [[motorcad/parameter_database/parameters/Stator_Lam_Length|Stator_Lam_Length]] | i/p | double | mm | Stator lamination stack axial length |
| [[motorcad/parameter_database/parameters/Stator_Pole_Angle|Stator_Pole_Angle]] | i/p | double | MDeg | SRM Stator Pole Angle at Stator Bore |
| [[motorcad/parameter_database/parameters/Stator_Pole_Depth|Stator_Pole_Depth]] | i/p | double | mm | SRM Stator Pole Depth |
| [[motorcad/parameter_database/parameters/Stator_Pole_Radius|Stator_Pole_Radius]] | i/p | double | mm | SRM Stator Pole Corner Radius |
| [[motorcad/parameter_database/parameters/Stator_Pole_Width|Stator_Pole_Width]] | o/p | double | mm | SRM Stator Pole Width |
| [[motorcad/parameter_database/parameters/StepHouseInner_F|StepHouseInner_F]] | i/p | double | mm | The inner step change in housing thickness of the front of the motor |
| [[motorcad/parameter_database/parameters/StepHouseInner_R|StepHouseInner_R]] | i/p | double | mm | The inner step change in housing thickness of the rear of the motor |
| [[motorcad/parameter_database/parameters/StepHouseOuter_F|StepHouseOuter_F]] | i/p | double | mm | The outer step change in housing thickness of the front of the motor |
| [[motorcad/parameter_database/parameters/StepHouseOuter_R|StepHouseOuter_R]] | i/p | double | mm | The outer step change in housing thickness of the rear of the motor |
| [[motorcad/parameter_database/parameters/SyncPoleArc|SyncPoleArc]] | i/p | double | EDeg | This is the central arc of the Rotor Pole [EDeg] |
| [[motorcad/parameter_database/parameters/SyncRotorSlot_Depth|SyncRotorSlot_Depth]] | i/p | double | mm | The depth of the Sync rotor slot from the rotor surface |
| [[motorcad/parameter_database/parameters/SyncRotorSlot_Width|SyncRotorSlot_Width]] | i/p | double | mm | The width of the Sync rotor slot |
| [[motorcad/parameter_database/parameters/Sync_L_Separator_Embed|Sync_L_Separator_Embed]] | i/p | double | mm | The distance that the seperator is embedded into the rotor lamination |
| [[motorcad/parameter_database/parameters/Sync_L_Separator_Radius|Sync_L_Separator_Radius]] | i/p | double | mm | Inner Radius for L-shaped Wdg Separator |
| [[motorcad/parameter_database/parameters/Sync_L_Separator_Width|Sync_L_Separator_Width]] | i/p | double | mm | Separator width |
| [[motorcad/parameter_database/parameters/ToothArc_Outer|ToothArc_Outer]] | i/p | double | N/A | The outer tooth arc in degrees |
| [[motorcad/parameter_database/parameters/ToothTipAngle_Outer|ToothTipAngle_Outer]] | i/p | double | N/A | The angle of the outer tooth tip |
| [[motorcad/parameter_database/parameters/ToothTipDepth_Outer|ToothTipDepth_Outer]] | i/p | double | mm | The depth of the outer tooth tip |
| [[motorcad/parameter_database/parameters/ToothWidth_Outer|ToothWidth_Outer]] | i/p | double | mm | The width of the outer tooth |
| [[motorcad/parameter_database/parameters/Tooth_Tip_Angle|Tooth_Tip_Angle]] | i/p | double | MDeg | Tooth-tip angle |
| [[motorcad/parameter_database/parameters/Tooth_Tip_Depth|Tooth_Tip_Depth]] | i/p | double | mm | Tooth-tip depth, i.e. depth of slot opening from bore to tooth taper region |
| [[motorcad/parameter_database/parameters/Tooth_Width|Tooth_Width]] | i/p | double | mm | Tooth width (parallel teeth) |
| [[motorcad/parameter_database/parameters/Tooth_Width_Bottom|Tooth_Width_Bottom]] | o/p | double | mm | Width of tooth at tooth bottom (only used for tapered slot) |
| [[motorcad/parameter_database/parameters/Tooth_Width_Top|Tooth_Width_Top]] | o/p | double | mm | Width of tooth at tooth top (only used for tapered slot) |
| [[motorcad/parameter_database/parameters/Tw_Lower|Tw_Lower]] | o/p | double | mm | tooth width (lower section of parallel slot tooth) |
| [[motorcad/parameter_database/parameters/Tw_Upper|Tw_Upper]] | o/p | double | mm | tooth width (upper section of parallel slot tooth) |
| [[motorcad/parameter_database/parameters/UMagnetInner_ClearanceI_Array|UMagnetInner_ClearanceI_Array]] | i/p | double | mm | The clearance of the U-Layer Inner magnet away from the magnet pole |
| [[motorcad/parameter_database/parameters/UMagnetInner_ClearanceO_Array|UMagnetInner_ClearanceO_Array]] | i/p | double | mm | The clearance of the U-Layer Inner magnet towards the magnet pole |
| [[motorcad/parameter_database/parameters/UMagnetOuter_ClearanceI_Array|UMagnetOuter_ClearanceI_Array]] | i/p | double | mm | The clearance of the U-Layer Outer magnet away from the magnet pole |
| [[motorcad/parameter_database/parameters/UMagnetOuter_ClearanceO_Array|UMagnetOuter_ClearanceO_Array]] | i/p | double | mm | The clearance of the U-Layer Outer magnet towards the magnet pole |
| [[motorcad/parameter_database/parameters/UMagnet_Length_Inner_Array|UMagnet_Length_Inner_Array]] | i/p | double | mm | The length of the U Layer Inner magnet |
| [[motorcad/parameter_database/parameters/UMagnet_Length_Outer_Array|UMagnet_Length_Outer_Array]] | i/p | double | mm | The length of the U Layer Outer magnet |
| [[motorcad/parameter_database/parameters/UMagnet_Offset_Inner_Array|UMagnet_Offset_Inner_Array]] | i/p | double | mm | The offset of the U Layer Inner magnet |
| [[motorcad/parameter_database/parameters/UMagnet_Offset_Outer_Array|UMagnet_Offset_Outer_Array]] | i/p | double | mm | The offset of the U Layer Outer magnet |
| [[motorcad/parameter_database/parameters/UShape_BridgeThickness_Array|UShape_BridgeThickness_Array]] | i/p | double | mm | The bridge thickness of the U layer |
| [[motorcad/parameter_database/parameters/UShape_CentrePost_Array|UShape_CentrePost_Array]] | i/p | double | mm | The thickness of the U Layer centre post |
| [[motorcad/parameter_database/parameters/UShape_InnerDiameter_Array|UShape_InnerDiameter_Array]] | i/p | double | mm | The inner diameter of the U layer |
| [[motorcad/parameter_database/parameters/UShape_MagnetSegments_Inner_Array|UShape_MagnetSegments_Inner_Array]] | i/p | integer | N/A | The number of inner magnet segments |
| [[motorcad/parameter_database/parameters/UShape_MagnetSegments_Outer_Array|UShape_MagnetSegments_Outer_Array]] | i/p | integer | N/A | The number of outer magnet segments |
| [[motorcad/parameter_database/parameters/UShape_MaxLength_Inner_Array|UShape_MaxLength_Inner_Array]] | o/p | double | mm | Maxiumum length available within the inner U layer section for the specified layer |
| [[motorcad/parameter_database/parameters/UShape_MaxLength_Outer_Array|UShape_MaxLength_Outer_Array]] | o/p | double | mm | Maxiumum length available within the outer U layer section for the specified layer |
| [[motorcad/parameter_database/parameters/UShape_OuterAngleOffset_Array|UShape_OuterAngleOffset_Array]] | i/p | double | MDeg | The offset angle of the outer U Layer |
| [[motorcad/parameter_database/parameters/UShape_Post_Inner_Array|UShape_Post_Inner_Array]] | i/p | double | mm | Thickness of the inner post |
| [[motorcad/parameter_database/parameters/UShape_Post_Inner_Offset|UShape_Post_Inner_Offset]] | i/p | double | mm | The offset distance of the inner post from the layer bend. |
| [[motorcad/parameter_database/parameters/UShape_Post_Outer_Array|UShape_Post_Outer_Array]] | i/p | double | mm | Thickness of the outer post |
| [[motorcad/parameter_database/parameters/UShape_Post_Outer_Offset|UShape_Post_Outer_Offset]] | i/p | double | mm | The offset distance of the outer post from the layer bend. |
| [[motorcad/parameter_database/parameters/UShape_Thickness_Inner_Array|UShape_Thickness_Inner_Array]] | i/p | double | mm | The inner thickness of the U Layer |
| [[motorcad/parameter_database/parameters/UShape_Thickness_Outer_Array|UShape_Thickness_Outer_Array]] | i/p | double | mm | The outer thickness of the U Layer |
| [[motorcad/parameter_database/parameters/UShape_WebThickness_Array|UShape_WebThickness_Array]] | i/p | double | mm | The web thickness of the U layer |
| [[motorcad/parameter_database/parameters/VMagnet_Layers|VMagnet_Layers]] | i/p | integer | N/A | The number of layers of V-Shape magnets |
| [[motorcad/parameter_database/parameters/VShapeMagnetPost_Array|VShapeMagnetPost_Array]] | i/p | double | mm | The post thickness for the interior V web magnet layer |
| [[motorcad/parameter_database/parameters/VShapeMagnetSegments_Array|VShapeMagnetSegments_Array]] | i/p | integer | N/A | The number of segments for each v-shape magnet in this layer |
| [[motorcad/parameter_database/parameters/VShape_Magnet_ClearanceInner|VShape_Magnet_ClearanceInner]] | i/p | double | mm | The inner clearance for each v-shape magnet in this layer |
| [[motorcad/parameter_database/parameters/VShape_Magnet_ClearanceOuter|VShape_Magnet_ClearanceOuter]] | i/p | double | mm | The outer clearance for each v-shape magnet in this layer |
| [[motorcad/parameter_database/parameters/VSimpleEndRegion_Inner_Array|VSimpleEndRegion_Inner_Array]] | i/p | double | mm | The distance the inner end region arc extends the airspace |
| [[motorcad/parameter_database/parameters/VSimpleEndRegion_Outer_Array|VSimpleEndRegion_Outer_Array]] | i/p | double | mm | The distance the inner end region arc extends the airspace |
| [[motorcad/parameter_database/parameters/VSimpleMagShift_Array|VSimpleMagShift_Array]] | i/p | double | mm | The offset for the interior V-Simple magnet layer |
| [[motorcad/parameter_database/parameters/VSimpleMagnetPost_Array|VSimpleMagnetPost_Array]] | i/p | double | mm | The post thickness for the interior V simple magnet layer |
| [[motorcad/parameter_database/parameters/VSimpleOffsetT_Array|VSimpleOffsetT_Array]] | i/p | double | MDeg | The angular offset of this magnet layer |
| [[motorcad/parameter_database/parameters/VSimpleWidth_Array|VSimpleWidth_Array]] | i/p | double | mm | The width for the interior V-Simple layer |
| [[motorcad/parameter_database/parameters/Volume_EW_Front_No_Ext|Volume_EW_Front_No_Ext]] | o/p | double | mm³ | Volume EW Front No Ext |
| [[motorcad/parameter_database/parameters/Volume_EW_Rear_No_Ext|Volume_EW_Rear_No_Ext]] | o/p | double | mm³ | Volume EW Rear No Ext |
| [[motorcad/parameter_database/parameters/WJ_Channel-Lam|WJ_Channel-Lam]] | i/p | double | mm | Spacing between housing water jacket spiral groove and stator lamination |
| [[motorcad/parameter_database/parameters/WJ_Channel_Height|WJ_Channel_Height]] | i/p | double | mm | Housing water jacket spiral groove channel height |
| [[motorcad/parameter_database/parameters/WJ_Channel_Number|WJ_Channel_Number]] | i/p | double | N/A | Number of water jacket channels in active, front, and rear flow components (before parallel paths applied) |
| [[motorcad/parameter_database/parameters/WJ_Channel_Spacing|WJ_Channel_Spacing]] | i/p | double | mm | Housing water jacket spiral groove channel spacing |
| [[motorcad/parameter_database/parameters/WJ_Channel_Width|WJ_Channel_Width]] | i/p | double | mm | Housing water jacket spiral groove channel width |
| [[motorcad/parameter_database/parameters/WJ_Parallel_Paths|WJ_Parallel_Paths]] | i/p | integer | N/A | Number of parallel paths (channels) available for fluid to flow down |
| [[motorcad/parameter_database/parameters/Wafter_Depth_Reduct_F|Wafter_Depth_Reduct_F]] | i/p | double | mm | Wafter radial depth reduction (compared to the end ring depth) [front] |
| [[motorcad/parameter_database/parameters/Wafter_Depth_Reduct_R|Wafter_Depth_Reduct_R]] | i/p | double | mm | Wafter radial depth reduction (compared to the end ring depth) [rear] |
| [[motorcad/parameter_database/parameters/Wafter_Inner_Add_F|Wafter_Inner_Add_F]] | i/p | double | mm | Material added to front wafter inner radius |
| [[motorcad/parameter_database/parameters/Wafter_Inner_Add_R|Wafter_Inner_Add_R]] | i/p | double | mm | Material added to rear wafter inner radius |
| [[motorcad/parameter_database/parameters/Wafter_Length_F|Wafter_Length_F]] | i/p | double | mm | Length of rotor wafters [front] |
| [[motorcad/parameter_database/parameters/Wafter_Length_R|Wafter_Length_R]] | i/p | double | mm | Length of rotor wafters [rear] |
| [[motorcad/parameter_database/parameters/Wafter_Number_F|Wafter_Number_F]] | i/p | integer | N/A | Number of rotor wafters [front] |
| [[motorcad/parameter_database/parameters/Wafter_Number_R|Wafter_Number_R]] | i/p | integer | N/A | Number of rotor wafters [front] |
| [[motorcad/parameter_database/parameters/Wafter_Outer_Add_F|Wafter_Outer_Add_F]] | i/p | double | mm | Material added to front wafter outer radius |
| [[motorcad/parameter_database/parameters/Wafter_Outer_Add_R|Wafter_Outer_Add_R]] | i/p | double | mm | Material added to rear wafter outer radius |
| [[motorcad/parameter_database/parameters/Wafter_Thickness_F|Wafter_Thickness_F]] | i/p | double | mm | Wafter circumferential thickness [front] |
| [[motorcad/parameter_database/parameters/Wafter_Thickness_R|Wafter_Thickness_R]] | i/p | double | mm | Wafter circumferential thickness [rear] |
| [[motorcad/parameter_database/parameters/Wdg_Add__Inner_F_|Wdg_Add_(Inner_F)]] | i/p | double | mm | Inner expansion of End Winding [front of motor] |
| [[motorcad/parameter_database/parameters/Wdg_Add__Inner_R_|Wdg_Add_(Inner_R)]] | i/p | double | mm | Inner expansion of End Winding [rear of motor] |
| [[motorcad/parameter_database/parameters/Wdg_Add__Outer_F_|Wdg_Add_(Outer_F)]] | i/p | double | mm | Outer expansion of End Winding [front of motor] |
| [[motorcad/parameter_database/parameters/Wdg_Add__Outer_R_|Wdg_Add_(Outer_R)]] | i/p | double | mm | Outer expansion of End Winding [rear of motor] |
| [[motorcad/parameter_database/parameters/Wdg_Extension_Inner|Wdg_Extension_Inner]] | i/p | double | mm | Amount that winding extends beyond inner stator radius before bending. |
| [[motorcad/parameter_database/parameters/Wdg_Extension_Outer|Wdg_Extension_Outer]] | i/p | double | mm | Amount that winding extends beyond outer stator radius before bending. |
| [[motorcad/parameter_database/parameters/Wdg_Extension__F_|Wdg_Extension_(F)]] | i/p | double | mm | Amount that winding extends beyond stator lamination before bending into end winding [front of motor] |
| [[motorcad/parameter_database/parameters/Wdg_Extension__R_|Wdg_Extension_(R)]] | i/p | double | mm | Amount that winding extends beyond stator lamination before bending into end winding [rear of motor] |
| [[motorcad/parameter_database/parameters/Wdg_Separator_Length|Wdg_Separator_Length]] | i/p | double | mm | Wdg Separator Length |
| [[motorcad/parameter_database/parameters/Wdg_Separator_Low__%_|Wdg_Separator_Low_(%)]] | i/p | double | Percent | winding separator (insulation) between coil sides (lower limit percent of coil depth) |
| [[motorcad/parameter_database/parameters/Wdg_Separator_Total__%_|Wdg_Separator_Total_(%)]] | i/p | double | Percent | winding separator between coil sides (percentage of separator depth) |
| [[motorcad/parameter_database/parameters/Wdg_Separator_Up__%_|Wdg_Separator_Up_(%)]] | i/p | double | Percent | winding separator (insulation) between coil sides (upper limit percent of coil depth) |
| [[motorcad/parameter_database/parameters/WebAngle|WebAngle]] | i/p | double | MDeg | The angle of the web in mechanical degrees for the interior flat magnets |
| [[motorcad/parameter_database/parameters/WebLength_Array|WebLength_Array]] | i/p | double | mm | The magnet web length for the interior V-Shape magnets |
| [[motorcad/parameter_database/parameters/WebThickness_Array|WebThickness_Array]] | i/p | double | mm | The web thickness for the interior V-Shape magnet layer |
| [[motorcad/parameter_database/parameters/Web_Length|Web_Length]] | i/p | double | mm | The magnet web length for the interior V-Shape magnets |
| [[motorcad/parameter_database/parameters/Web_Thickness|Web_Thickness]] | i/p | double | mm | The magnet web thickness for the interior Flat, V-Shape and U-Shape magnets |
| [[motorcad/parameter_database/parameters/Wedge_Inset|Wedge_Inset]] | i/p | double | mm | The depth of wedge from slot side |
| [[motorcad/parameter_database/parameters/Wedge_Thickness|Wedge_Thickness]] | i/p | double | mm | The thickness of wedge |
| [[motorcad/parameter_database/parameters/WindingArea|WindingArea]] | o/p | double | mm² | The slot area left for winding after liner insertion and top and bottom spacers |
| [[motorcad/parameter_database/parameters/WindingFill_Outer|WindingFill_Outer]] | i/p | double | N/A | The outer winding fill factor of the available space |
| [[motorcad/parameter_database/parameters/Winding_Separators|Winding_Separators]] | i/p | integer | N/A | Winding Separators |
| [[motorcad/parameter_database/parameters/coilHeight|coilHeight]] | i/p | double | mm | The height of the coil including the coil insulation |
| [[motorcad/parameter_database/parameters/coilWidth|coilWidth]] | i/p | double | mm | The width of the coil including the coil insulation |
| [[motorcad/parameter_database/parameters/columnsConductors|columnsConductors]] | i/p | integer | N/A | The number of conductors across each slot |
| [[motorcad/parameter_database/parameters/conductorHeight|conductorHeight]] | i/p | double | mm | The height of each conductor bar |
| [[motorcad/parameter_database/parameters/conductorWidth|conductorWidth]] | i/p | double | mm | The width of each conductor bar |
| [[motorcad/parameter_database/parameters/gapLinerSlotWall|gapLinerSlotWall]] | i/p | double | mm | The gap between the liner and the slot wall |
| [[motorcad/parameter_database/parameters/gapSlotBaseSpacerSlotBase|gapSlotBaseSpacerSlotBase]] | i/p | double | mm | The gap between the slot base spacer and the slot bottom |
| [[motorcad/parameter_database/parameters/gapSlotTopSpacerSlotTop|gapSlotTopSpacerSlotTop]] | i/p | double | mm | The gap between the slot top spacer and the slot wedge |
| [[motorcad/parameter_database/parameters/innerImpregHeight|innerImpregHeight]] | o/p | double | mm | Height of inner impregnation layer for form wound |
| [[motorcad/parameter_database/parameters/innerImpregWidth|innerImpregWidth]] | o/p | double | mm | Width of inner impregnation layer for form wound |
| [[motorcad/parameter_database/parameters/linerArea|linerArea]] | o/p | double | mm² | The area of the outer liner |
| [[motorcad/parameter_database/parameters/outerImpregHeight|outerImpregHeight]] | o/p | double | mm | Height of outer impregnation layer for form wound |
| [[motorcad/parameter_database/parameters/outerImpregWidth|outerImpregWidth]] | o/p | double | mm | Width of outer impregnation layer for form wound |
| [[motorcad/parameter_database/parameters/rowsConductors|rowsConductors]] | i/p | integer | N/A | The number of conductors down the slot in each phase group |
| [[motorcad/parameter_database/parameters/spacerArea|spacerArea]] | o/p | double | mm² | The area of the spacers |
| [[motorcad/parameter_database/parameters/thicknessCoilInsulation|thicknessCoilInsulation]] | i/p | double | mm | The thickness of the coil insulation |
| [[motorcad/parameter_database/parameters/thicknessCopperInsulation|thicknessCopperInsulation]] | i/p | double | mm | The thickness of the copper bar insulation |
| [[motorcad/parameter_database/parameters/thicknessPhaseSeparator|thicknessPhaseSeparator]] | i/p | double | mm | The thickness of the phase separator |
| [[motorcad/parameter_database/parameters/thicknessSlotBaseSpacer|thicknessSlotBaseSpacer]] | i/p | double | mm | The thickness of the spacer at the slot base |
| [[motorcad/parameter_database/parameters/thicknessSlotLinerOuterLayer|thicknessSlotLinerOuterLayer]] | i/p | double | mm | The thickness of the slot liner |
| [[motorcad/parameter_database/parameters/thicknessSlotTopSpacer|thicknessSlotTopSpacer]] | i/p | double | mm | The thickness of the spacer at the slot top |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
