---
type: motorcad_parameter_category
category_name: Mechanical
parameter_count: 77
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Mechanical

## Overview
The **Mechanical** category contains **77** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AnsysMechanicalExport_TangentialDirection|AnsysMechanicalExport_TangentialDirection]] | compatibility | integer | N/A | The improved method corrects the tangential force direction in the Ansys Mechanical force export |
| [[motorcad/parameter_database/parameters/AvDisplacement_RotorLam|AvDisplacement_RotorLam]] | o/p | double | mm | Average mechanical displacement on Rotor Lamination |
| [[motorcad/parameter_database/parameters/AvStressRadialLocation_Bridge|AvStressRadialLocation_Bridge]] | i/p | double | N/A | Controls the radial location of points used to calculate the average bridge stress. 0 = Inner bridge edge ; 1 = Outer bridge edge |
| [[motorcad/parameter_database/parameters/AvStressRadialLocation_Post|AvStressRadialLocation_Post]] | i/p | double | N/A | Controls the radial location of points used to calculate the average post stress. 0 = Inner post edge ; 1 = Outer post edge |
| [[motorcad/parameter_database/parameters/AvStress_MagnetBridge|AvStress_MagnetBridge]] | o/p | double | MPa | Average stress along an arc through the magnet bridge for each magnet layer |
| [[motorcad/parameter_database/parameters/AvStress_MagnetPost|AvStress_MagnetPost]] | o/p | double | MPa | Average stress across the magnet post for each V magnet layer |
| [[motorcad/parameter_database/parameters/AvStress_MagnetPost_Inner|AvStress_MagnetPost_Inner]] | o/p | double | MPa | Average stress across the inner magnet post for each U magnet layer |
| [[motorcad/parameter_database/parameters/AvStress_PostLocationMethod|AvStress_PostLocationMethod]] | compatibility | integer | N/A | Method for positioning the measurement points of the average stress post calculation. |
| [[motorcad/parameter_database/parameters/AvStress_RotorLam|AvStress_RotorLam]] | o/p | double | MPa | Average mechanical stress on Rotor Lamination |
| [[motorcad/parameter_database/parameters/AvStress_ViewPoints|AvStress_ViewPoints]] | setting | boolean | N/A | Plot the location of points used to calculate the average post / bridge stress |
| [[motorcad/parameter_database/parameters/DensityAdjustment_FieldWdg_EWdg|DensityAdjustment_FieldWdg_EWdg]] | o/p | double | N/A | The density adjustment factor for Field Winding to take into account of endwindings |
| [[motorcad/parameter_database/parameters/DensityAdjustment_FieldWdg_User|DensityAdjustment_FieldWdg_User]] | i/p | double | N/A | The user specified density adjustment factor for Field Winding |
| [[motorcad/parameter_database/parameters/EquivDensity_FieldWdg|EquivDensity_FieldWdg]] | o/p | double | kg/m³ | The equivalent density for Field Winding to take into account of endwindings in 2D mechancial FEA model |
| [[motorcad/parameter_database/parameters/EquivDensity_FieldWdg_Calc|EquivDensity_FieldWdg_Calc]] | o/p | double | kg/m³ | The calculated equivalent density for Field Winding to take into account different winding components |
| [[motorcad/parameter_database/parameters/HoopStressMethod_Spoke|HoopStressMethod_Spoke]] | compatibility | integer | N/A | Method used to calculate rotor lam hoop stress for spoke magnet machines |
| [[motorcad/parameter_database/parameters/HoopStress_RotorLam_Inner|HoopStress_RotorLam_Inner]] | o/p | double | MPa | The Hoop Stress at the inner radius of the rotor lamination (analytical calculation for rotating cylinders) |
| [[motorcad/parameter_database/parameters/HoopStress_RotorLam_Outer|HoopStress_RotorLam_Outer]] | o/p | double | MPa | The Hoop Stress at the outer radius of the rotor lamination (analytical calculation for rotating cylinders) |
| [[motorcad/parameter_database/parameters/MaxDisplacement_RotorLam|MaxDisplacement_RotorLam]] | o/p | double | mm | Maximum mechanical displacement on Rotor Lamination |
| [[motorcad/parameter_database/parameters/MaxStress_RotorLam|MaxStress_RotorLam]] | o/p | double | MPa | Maximum mechanical stress on Rotor Lamination |
| [[motorcad/parameter_database/parameters/PoissonsRatio_BottomBar|PoissonsRatio_BottomBar]] | i/p | double | N/A | Poissons Ratio value of the Bottom Bar |
| [[motorcad/parameter_database/parameters/PoissonsRatio_BottomBarOpening|PoissonsRatio_BottomBarOpening]] | i/p | double | N/A | Poissons Ratio value of the Bottom Bar Opening |
| [[motorcad/parameter_database/parameters/PoissonsRatio_Damper_Bars|PoissonsRatio_Damper_Bars]] | i/p | double | N/A | Poissons Ratio value of the Damper Bar material |
| [[motorcad/parameter_database/parameters/PoissonsRatio_Damper_End_F|PoissonsRatio_Damper_End_F]] | i/p | double | N/A | Poissons Ratio value of the front Damper End Ring material |
| [[motorcad/parameter_database/parameters/PoissonsRatio_Damper_End_R|PoissonsRatio_Damper_End_R]] | i/p | double | N/A | Poissons Ratio value of the rear Damper End Ring material |
| [[motorcad/parameter_database/parameters/PoissonsRatio_Damper_Opening|PoissonsRatio_Damper_Opening]] | i/p | double | N/A | Poissons Ratio value of the Damper Opening material |
| [[motorcad/parameter_database/parameters/PoissonsRatio_Embedded_Magnet_Pole|PoissonsRatio_Embedded_Magnet_Pole]] | i/p | double | N/A | Poissons Ratio value of the Embedded Magnet Pole |
| [[motorcad/parameter_database/parameters/PoissonsRatio_FieldDivider|PoissonsRatio_FieldDivider]] | i/p | double | N/A | Poissons Ratio value of the Field Divider |
| [[motorcad/parameter_database/parameters/PoissonsRatio_FieldLiner|PoissonsRatio_FieldLiner]] | i/p | double | N/A | Poissons Ratio value of the Field Liner |
| [[motorcad/parameter_database/parameters/PoissonsRatio_FieldSeparator|PoissonsRatio_FieldSeparator]] | i/p | double | N/A | Poissons Ratio value of the Field Separator |
| [[motorcad/parameter_database/parameters/PoissonsRatio_FieldWdg|PoissonsRatio_FieldWdg]] | i/p | double | N/A | Poissons Ratio value of the Field Winding (field copper) |
| [[motorcad/parameter_database/parameters/PoissonsRatio_Magnet|PoissonsRatio_Magnet]] | i/p | double | N/A | Poissons Ratio value of the Magnet |
| [[motorcad/parameter_database/parameters/PoissonsRatio_Pocket|PoissonsRatio_Pocket]] | i/p | double | N/A | Poissons Ratio value of the Pocket |
| [[motorcad/parameter_database/parameters/PoissonsRatio_RotorHub|PoissonsRatio_RotorHub]] | i/p | double | N/A | Poissons Ratio value of the Rotor Hub |
| [[motorcad/parameter_database/parameters/PoissonsRatio_RotorLam|PoissonsRatio_RotorLam]] | i/p | double | N/A | Poissons Ratio value of the Rotor Lamination |
| [[motorcad/parameter_database/parameters/PoissonsRatio_RotorWedge|PoissonsRatio_RotorWedge]] | i/p | double | N/A | Poissons Ratio value of the Rotor Wedge |
| [[motorcad/parameter_database/parameters/PoissonsRatio_TopBar|PoissonsRatio_TopBar]] | i/p | double | N/A | Poissons Ratio value of the Top Bar |
| [[motorcad/parameter_database/parameters/PoissonsRatio_TopBarOpening|PoissonsRatio_TopBarOpening]] | i/p | double | N/A | Poissons Ratio value of the Top Bar Opening |
| [[motorcad/parameter_database/parameters/SafetyFactor_RotorLam|SafetyFactor_RotorLam]] | o/p | double | N/A | Ratio of Material Yield Stress to Rotor Lamination Stress |
| [[motorcad/parameter_database/parameters/YieldStressRatio_RotorLam|YieldStressRatio_RotorLam]] | o/p | double | N/A | Ratio of Rotor Lamination Stress to Material Yield Stress |
| [[motorcad/parameter_database/parameters/YieldStress_BottomBar|YieldStress_BottomBar]] | i/p | double | MPa | The Yield Stress of the Bottom Bar material |
| [[motorcad/parameter_database/parameters/YieldStress_BottomBarOpening|YieldStress_BottomBarOpening]] | i/p | double | MPa | The Yield Stress of the Bottom Bar Opening material |
| [[motorcad/parameter_database/parameters/YieldStress_Damper_Bars|YieldStress_Damper_Bars]] | i/p | double | MPa | The Yield Stress of the Damper Bar material |
| [[motorcad/parameter_database/parameters/YieldStress_Damper_End_F|YieldStress_Damper_End_F]] | i/p | double | MPa | The Yield Stress of the front Damper End Ring material |
| [[motorcad/parameter_database/parameters/YieldStress_Damper_End_R|YieldStress_Damper_End_R]] | i/p | double | MPa | The Yield Stress of the rear Damper End Ring material |
| [[motorcad/parameter_database/parameters/YieldStress_Damper_Opening|YieldStress_Damper_Opening]] | i/p | double | MPa | The Yield Stress of the Damper Opening material |
| [[motorcad/parameter_database/parameters/YieldStress_Embedded_Magnet_Pole|YieldStress_Embedded_Magnet_Pole]] | i/p | double | MPa | The Yield Stress of the rotor embedded magnet pole material |
| [[motorcad/parameter_database/parameters/YieldStress_FieldDivider|YieldStress_FieldDivider]] | i/p | double | MPa | The Yield Stress of the Field Divider material |
| [[motorcad/parameter_database/parameters/YieldStress_FieldLiner|YieldStress_FieldLiner]] | i/p | double | MPa | The Yield Stress of the Field Liner |
| [[motorcad/parameter_database/parameters/YieldStress_FieldSeparator|YieldStress_FieldSeparator]] | i/p | double | MPa | The Yield Stress of the Field Separator material |
| [[motorcad/parameter_database/parameters/YieldStress_FieldWdg|YieldStress_FieldWdg]] | i/p | double | MPa | The Yield Stress of the Field Winding material (field copper) |
| [[motorcad/parameter_database/parameters/YieldStress_Magnet|YieldStress_Magnet]] | i/p | double | MPa | The Yield Stress of the Magnet material |
| [[motorcad/parameter_database/parameters/YieldStress_Pocket|YieldStress_Pocket]] | i/p | double | MPa | The Yield Stress of the Pocket material |
| [[motorcad/parameter_database/parameters/YieldStress_RotorHub|YieldStress_RotorHub]] | i/p | double | MPa | The Yield Stress of the Rotor Hub material |
| [[motorcad/parameter_database/parameters/YieldStress_RotorLam|YieldStress_RotorLam]] | i/p | double | MPa | The Yield Stress of the rotor lamination material |
| [[motorcad/parameter_database/parameters/YieldStress_RotorWedge|YieldStress_RotorWedge]] | i/p | double | MPa | The Yield Stress of the Rotor Wedge material |
| [[motorcad/parameter_database/parameters/YieldStress_TopBar|YieldStress_TopBar]] | i/p | double | MPa | The Yield Stress of the Top Bar material |
| [[motorcad/parameter_database/parameters/YieldStress_TopBarOpening|YieldStress_TopBarOpening]] | i/p | double | MPa | The Yield Stress of the Top Bar Opening material |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_BottomBar|YoungsCoefficient_BottomBar]] | i/p | double | MPa | Youngs Coefficient value of the Bottom Bar |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_BottomBarOpening|YoungsCoefficient_BottomBarOpening]] | i/p | double | MPa | Youngs Coefficient value of the Bottom Bar Opening |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Damper_Bars|YoungsCoefficient_Damper_Bars]] | i/p | double | N/A | Youngs Coefficient value of the Damper Bar material |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Damper_End_F|YoungsCoefficient_Damper_End_F]] | i/p | double | N/A | Youngs Coefficient value of the front Damper End Ring material |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Damper_End_R|YoungsCoefficient_Damper_End_R]] | i/p | double | N/A | Youngs Coefficient value of the rear Damper End Ring material |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Damper_Opening|YoungsCoefficient_Damper_Opening]] | i/p | double | N/A | Youngs Coefficient value of the Damper Opening material |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Embedded_Magnet_Pole|YoungsCoefficient_Embedded_Magnet_Pole]] | i/p | double | MPa | Youngs Coefficient value of the Embedded Magnet Pole |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_FieldDivider|YoungsCoefficient_FieldDivider]] | i/p | double | MPa | Youngs Coefficient value of the Field Divider |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_FieldLiner|YoungsCoefficient_FieldLiner]] | i/p | double | MPa | Youngs Coefficient value of the Field Liner |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_FieldSeparator|YoungsCoefficient_FieldSeparator]] | i/p | double | MPa | Youngs Coefficient value of the Field Separator |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_FieldWdg|YoungsCoefficient_FieldWdg]] | i/p | double | MPa | Youngs Coefficient value of the Field Winding (field copper) |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Housing_Active|YoungsCoefficient_Housing_Active]] | i/p | double | MPa | Youngs Coefficient value of the Housing [Active] |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Magnet|YoungsCoefficient_Magnet]] | i/p | double | MPa | Youngs Coefficient value of the Magnet |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Pocket|YoungsCoefficient_Pocket]] | i/p | double | MPa | Youngs Coefficient value of the Pocket |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_RotorHub|YoungsCoefficient_RotorHub]] | i/p | double | MPa | Youngs Coefficient value of the Rotor Hub |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_RotorLam|YoungsCoefficient_RotorLam]] | i/p | double | MPa | Youngs Coefficient value of the Rotor Lamination |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_RotorWedge|YoungsCoefficient_RotorWedge]] | i/p | double | MPa | Youngs Coefficient value of the Rotor Wedge |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_Stator_Lam_Back_Iron|YoungsCoefficient_Stator_Lam_Back_Iron]] | i/p | double | MPa | Youngs Coefficient value of the Stator Back Iron Lamination |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_TopBar|YoungsCoefficient_TopBar]] | i/p | double | MPa | Youngs Coefficient value of the Top Bar |
| [[motorcad/parameter_database/parameters/YoungsCoefficient_TopBarOpening|YoungsCoefficient_TopBarOpening]] | i/p | double | MPa | Youngs Coefficient value of the Top Bar Opening |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
