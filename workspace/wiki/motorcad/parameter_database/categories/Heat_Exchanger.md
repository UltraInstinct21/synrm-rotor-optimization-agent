---
type: motorcad_parameter_category
category_name: Heat_Exchanger
parameter_count: 90
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Heat_Exchanger

## Overview
The **Heat_Exchanger** category contains **90** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/Area_Dissipation_HeatEx_inner|Area_Dissipation_HeatEx_inner]] | o/p | double | mm² | The Heat Exchanger dissipation area from the duct inner surface |
| [[motorcad/parameter_database/parameters/Area_Dissipation_HeatEx_outer|Area_Dissipation_HeatEx_outer]] | o/p | double | mm² | The Heat Exchanger dissipation area from the duct outer surface |
| [[motorcad/parameter_database/parameters/Calc_Input_h_HeatEx_inner|Calc_Input_h_HeatEx_inner]] | i/p | integer | N/A | The Heat Exchanger calculated or input set value for htc from flow over the inner Surface (0=Calc h, 1=Input h) |
| [[motorcad/parameter_database/parameters/Calc_Input_h_HeatEx_outer|Calc_Input_h_HeatEx_outer]] | i/p | integer | N/A | The Heat Exchanger calculated or input set value for htc from flow over the outer Surface (0=Calc h, 1=Input h) |
| [[motorcad/parameter_database/parameters/HeatExFlowOption|HeatExFlowOption]] | i/p | integer | N/A | The option for selecting the duct type of the Heat Exchanger |
| [[motorcad/parameter_database/parameters/HeatExOutletCoupling|HeatExOutletCoupling]] | i/p | integer | N/A | The cooling system supplied by the Heat Exchanger |
| [[motorcad/parameter_database/parameters/HeatExPowerFlowMethod|HeatExPowerFlowMethod]] | compatibility | integer | N/A | Method used to determine how much power to reinject into HeatEx_Fluid to account for cooling system dissipation |
| [[motorcad/parameter_database/parameters/HeatEx_Channel_Correlation_inner|HeatEx_Channel_Correlation_inner]] | o/p | integer | N/A | The correlation for the Heat Exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Channel_Correlation_outer|HeatEx_Channel_Correlation_outer]] | o/p | integer | N/A | The correlation for the Heat Exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Channel_Flow_Area_Inner|HeatEx_Channel_Flow_Area_Inner]] | o/p | double | mm² | This is the Heat Exchanger channel flow area |
| [[motorcad/parameter_database/parameters/HeatEx_Channel_Flow_Area_Outer|HeatEx_Channel_Flow_Area_Outer]] | i/p | double | mm² | This is the Heat Exchanger flow area of main volume |
| [[motorcad/parameter_database/parameters/HeatEx_Channel_Perimeter|HeatEx_Channel_Perimeter]] | o/p | double | mm | This is the Heat Exchanger channel perimeter |
| [[motorcad/parameter_database/parameters/HeatEx_Coolant_Inlet_Temp|HeatEx_Coolant_Inlet_Temp]] | i/p | double | °C | The Heat Exchanger coolant inlet temperature |
| [[motorcad/parameter_database/parameters/HeatEx_Coolant_Outlet_Temp|HeatEx_Coolant_Outlet_Temp]] | o/p | double | °C | The Heat Exchanger coolant outlet temperature |
| [[motorcad/parameter_database/parameters/HeatEx_Dissipation|HeatEx_Dissipation]] | o/p | double | Watts | The Heat Exchanger dissipation between the fluids |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_Diameter|HeatEx_Duct_Diameter]] | i/p | double | mm | The Heat Exchanger duct diameter |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_FlowResistance|HeatEx_Duct_FlowResistance]] | o/p | double | kg/m⁷ | The flow resistance of the HeatEx ducts |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_FrictionFactor|HeatEx_Duct_FrictionFactor]] | o/p | double | N/A | This is wall friction factor value for the Heat Exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_Friction_k_Adjustment|HeatEx_Duct_Friction_k_Adjustment]] | i/p | double | N/A | This is friction k Adjustment factor for the Heat Exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_Length|HeatEx_Duct_Length]] | i/p | double | mm | The total Heat Exchanger duct length (includes all parallel paths) |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_Parallel_Paths|HeatEx_Duct_Parallel_Paths]] | i/p | integer | N/A | The Heat Exchanger number of parallel duct paths |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_Wall_Notes|HeatEx_Duct_Wall_Notes]] | i/p | OleStr | N/A | The notes of the heat exchanger ducts |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_Wall_Roughness|HeatEx_Duct_Wall_Roughness]] | i/p | double | mm | The roughness of the heat exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Duct_k_Wall_Friction|HeatEx_Duct_k_Wall_Friction]] | o/p | double | N/A | This is wall friction k value for the Heat Exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Fluid_Conductivity|HeatEx_Fluid_Conductivity]] | i/p | double | W/m/°C | The Heat Exchanger coolant thermal conductivity |
| [[motorcad/parameter_database/parameters/HeatEx_Fluid_Cp|HeatEx_Fluid_Cp]] | i/p | double | J/kg/°C | The Heat Exchanger coolant specific heat capacity |
| [[motorcad/parameter_database/parameters/HeatEx_Fluid_Density|HeatEx_Fluid_Density]] | i/p | double | kg/m³ | The Heat Exchanger coolant density |
| [[motorcad/parameter_database/parameters/HeatEx_Fluid_Dynamic_Viscosity|HeatEx_Fluid_Dynamic_Viscosity]] | o/p | double | kg/m/s | The Heat Exchanger coolant dynamic viscosity |
| [[motorcad/parameter_database/parameters/HeatEx_Fluid_Kinematic_Viscosity|HeatEx_Fluid_Kinematic_Viscosity]] | i/p | double | m²/s | The Heat Exchanger coolant kinematic viscosity |
| [[motorcad/parameter_database/parameters/HeatEx_Fluid_Pr|HeatEx_Fluid_Pr]] | o/p | double | N/A | The Heat Exchanger coolant Prandtl number |
| [[motorcad/parameter_database/parameters/HeatEx_Fluid_Temp|HeatEx_Fluid_Temp]] | o/p | double | °C | The temperature of fluid being cooled in the Heat Exchanger |
| [[motorcad/parameter_database/parameters/HeatEx_HydraulicDiameter_Inner_mm|HeatEx_HydraulicDiameter_Inner_mm]] | o/p | double | N/A | This is hydraulic diameter for the Heat Exchanger |
| [[motorcad/parameter_database/parameters/HeatEx_HydraulicDiameter_Outer_mm|HeatEx_HydraulicDiameter_Outer_mm]] | o/p | double | N/A | This is hydraulic diameter for the Heat Exchanger |
| [[motorcad/parameter_database/parameters/HeatEx_InletFluid_Velocity|HeatEx_InletFluid_Velocity]] | o/p | double | m/s | The fluid velocity before entering the HeatEx ducts |
| [[motorcad/parameter_database/parameters/HeatEx_Inlet_ContExp_Notes|HeatEx_Inlet_ContExp_Notes]] | i/p | OleStr | N/A | The notes of the HeatEx ContExp |
| [[motorcad/parameter_database/parameters/HeatEx_Inlet_FlowArea|HeatEx_Inlet_FlowArea]] | o/p | double | mm² | The inlet flow area of the heat exchanger ducts |
| [[motorcad/parameter_database/parameters/HeatEx_Inlet_k_ContExp|HeatEx_Inlet_k_ContExp]] | o/p | double | N/A | This is k value for the Heat Exchanger ContExp |
| [[motorcad/parameter_database/parameters/HeatEx_Inlet_k_ContExp_Adjustment|HeatEx_Inlet_k_ContExp_Adjustment]] | i/p | double | N/A | This is ContExp k Adjustment factor for the Heat Exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Insulation_Thickness|HeatEx_Insulation_Thickness]] | i/p | double | mm | The Heat Exchanger duct insulation thickness |
| [[motorcad/parameter_database/parameters/HeatEx_OutletFluid_Velocity|HeatEx_OutletFluid_Velocity]] | o/p | double | m/s | The fluid velocity before entering the HeatEx ducts |
| [[motorcad/parameter_database/parameters/HeatEx_Outlet_ContExp_FlowResistance|HeatEx_Outlet_ContExp_FlowResistance]] | o/p | double | kg/m⁷ | The flow resistance of the ContExp |
| [[motorcad/parameter_database/parameters/HeatEx_Outlet_ContExp_Notes|HeatEx_Outlet_ContExp_Notes]] | i/p | OleStr | N/A | The notes of the HeatEx ContExp |
| [[motorcad/parameter_database/parameters/HeatEx_Outlet_FlowArea|HeatEx_Outlet_FlowArea]] | o/p | double | mm² | The outlet flow area of the heat exchanger ducts |
| [[motorcad/parameter_database/parameters/HeatEx_Outlet_k_ContExp|HeatEx_Outlet_k_ContExp]] | o/p | double | N/A | This is k value for the Heat Exchanger ContExp |
| [[motorcad/parameter_database/parameters/HeatEx_Outlet_k_ContExp_Adjustment|HeatEx_Outlet_k_ContExp_Adjustment]] | i/p | double | N/A | This is ContExp k Adjustment factor for the Heat Exchanger duct |
| [[motorcad/parameter_database/parameters/HeatEx_Volume_Flow_Rate|HeatEx_Volume_Flow_Rate]] | i/p | double | m³/s | The Heat Exchanger coolant volume flow rate |
| [[motorcad/parameter_database/parameters/HeatEx_Volume_Flow_Rate_Inner|HeatEx_Volume_Flow_Rate_Inner]] | o/p | double | m³/s | The Heat Exchanger volume flow rate inside the ducts |
| [[motorcad/parameter_database/parameters/HeatEx_Volume_Flow_Rate_Outer|HeatEx_Volume_Flow_Rate_Outer]] | o/p | double | m³/s | The Heat Exchanger volume flow rate outside the duct |
| [[motorcad/parameter_database/parameters/HeatEx_Wall_Thickness|HeatEx_Wall_Thickness]] | i/p | double | mm | The Heat Exchanger duct wall thickness |
| [[motorcad/parameter_database/parameters/HeatEx_inlet_ContExp_FlowResistance|HeatEx_inlet_ContExp_FlowResistance]] | o/p | double | kg/m⁷ | The flow resistance of the ContExp |
| [[motorcad/parameter_database/parameters/HeatEx_inner_FilmTemp|HeatEx_inner_FilmTemp]] | o/p | double | °C | The Heat Exchanger film temperature of the duct inner |
| [[motorcad/parameter_database/parameters/HeatEx_inner_WallTemp|HeatEx_inner_WallTemp]] | o/p | double | °C | The Heat Exchanger wall temperature of the duct inner surface |
| [[motorcad/parameter_database/parameters/HeatEx_outer_FilmTemp|HeatEx_outer_FilmTemp]] | o/p | double | °C | The Heat Exchanger film temperature for natural convection on the duct outer |
| [[motorcad/parameter_database/parameters/HeatEx_outer_Gr|HeatEx_outer_Gr]] | o/p | double | N/A | The Heat Exchanger Grashof number for natural convection on the duct outer |
| [[motorcad/parameter_database/parameters/HeatEx_outer_Pr|HeatEx_outer_Pr]] | o/p | double | N/A | The Heat Exchanger Prandtl number for natural convection on the duct outer |
| [[motorcad/parameter_database/parameters/HeatEx_outer_Ra|HeatEx_outer_Ra]] | o/p | double | N/A | The Heat Exchanger Rayleigh number for natural convection on the duct outer |
| [[motorcad/parameter_database/parameters/HeatEx_outer_WallTemp|HeatEx_outer_WallTemp]] | o/p | double | °C | The Heat Exchanger wall temperature for natural convection on the duct outer |
| [[motorcad/parameter_database/parameters/HeatExchanger|HeatExchanger]] | i/p | boolean | N/A | When selected the Heat Exchanger can be connected to the cooling system. |
| [[motorcad/parameter_database/parameters/IncludeHeatExDuctWallFriction|IncludeHeatExDuctWallFriction]] | recommended | boolean | N/A | When enabled the duct wall friction is taken into account in the Heat Exchanger flow |
| [[motorcad/parameter_database/parameters/Notes_HeatEx_inner|Notes_HeatEx_inner]] | i/p | OleStr | N/A | The Heat Exchanger notes for the inner Surface |
| [[motorcad/parameter_database/parameters/Notes_HeatEx_outer|Notes_HeatEx_outer]] | i/p | OleStr | N/A | The Heat Exchanger notes for the outer Surface |
| [[motorcad/parameter_database/parameters/Nu_HeatEx_inner|Nu_HeatEx_inner]] | o/p | double | N/A | The Heat Exchanger nusselt number in the duct inner |
| [[motorcad/parameter_database/parameters/Nu_HeatEx_outer_forConv|Nu_HeatEx_outer_forConv]] | o/p | double | N/A | The Heat Exchanger nusselt number on the duct outer (forced convection) |
| [[motorcad/parameter_database/parameters/Nu_HeatEx_outer_natConv|Nu_HeatEx_outer_natConv]] | o/p | double | N/A | The Heat Exchanger nusselt number on the duct outer (natural convection) |
| [[motorcad/parameter_database/parameters/Re_Critical_HeatEx_inner|Re_Critical_HeatEx_inner]] | o/p | double | N/A | The Heat Exchanger critical reynolds number for flow over the inner Surface |
| [[motorcad/parameter_database/parameters/Re_Critical_HeatEx_outer|Re_Critical_HeatEx_outer]] | o/p | double | N/A | The Heat Exchanger critical reynolds number for flow over the outer Surface |
| [[motorcad/parameter_database/parameters/Re_HeatEx_inner|Re_HeatEx_inner]] | o/p | double | N/A | The Heat Exchanger reynolds number for flow over the inner Surface |
| [[motorcad/parameter_database/parameters/Re_HeatEx_outer|Re_HeatEx_outer]] | o/p | double | N/A | The Heat Exchanger reynolds number for flow over the outer Surface |
| [[motorcad/parameter_database/parameters/Rt_HeatExFluid_Coolant|Rt_HeatExFluid_Coolant]] | o/p | double | °C/W | This is the thermal resistance from the internal fluid to the heat exchanger fluid |
| [[motorcad/parameter_database/parameters/Rt_HeatExFluid_DuctWall|Rt_HeatExFluid_DuctWall]] | o/p | double | °C/W | This is the thermal resistance from the internal fluid to the exterior of duct wall |
| [[motorcad/parameter_database/parameters/Rt_HeatEx_DuctWall|Rt_HeatEx_DuctWall]] | o/p | double | °C/W | This is the Heat Exchanger duct wall thermal resistance |
| [[motorcad/parameter_database/parameters/Rt_HeatEx_Insulation|Rt_HeatEx_Insulation]] | o/p | double | °C/W | This is the Heat Exchanger duct insulation thermal resistance |
| [[motorcad/parameter_database/parameters/Rt_HeatEx_inner|Rt_HeatEx_inner]] | o/p | double | °C/W | The Heat Exchanger thermal resistance from the duct inner surface to the fluid |
| [[motorcad/parameter_database/parameters/Rt_HeatEx_outer|Rt_HeatEx_outer]] | o/p | double | °C/W | The Heat Exchanger thermal resistance from the duct outer surface to the fluid |
| [[motorcad/parameter_database/parameters/Vel_HeatEx_inner|Vel_HeatEx_inner]] | o/p | double | m/s | The Heat Exchanger velocity in the duct |
| [[motorcad/parameter_database/parameters/Vel_HeatEx_inner_Calc|Vel_HeatEx_inner_Calc]] | o/p | double | m/s | The Heat Exchanger velocity in the duct |
| [[motorcad/parameter_database/parameters/Vel_HeatEx_outer|Vel_HeatEx_outer]] | o/p | double | m/s | The Heat Exchanger velocity outside the duct |
| [[motorcad/parameter_database/parameters/Vel_HeatEx_outer_Calc|Vel_HeatEx_outer_Calc]] | o/p | double | m/s | The Heat Exchanger velocity outside the duct |
| [[motorcad/parameter_database/parameters/Vel_Mult_HeatEx_inner|Vel_Mult_HeatEx_inner]] | i/p | double | N/A | The Heat Exchanger velocity multiplier over the inner Surface |
| [[motorcad/parameter_database/parameters/Vel_Mult_HeatEx_outer|Vel_Mult_HeatEx_outer]] | i/p | double | N/A | The Heat Exchanger velocity multiplier over the outer Surface |
| [[motorcad/parameter_database/parameters/h_Adjust_HeatEx_inner|h_Adjust_HeatEx_inner]] | i/p | double | N/A | The Heat Exchanger flow heat transfer coefficient adjustment (user input) over the inner Surface |
| [[motorcad/parameter_database/parameters/h_Adjust_HeatEx_outer|h_Adjust_HeatEx_outer]] | i/p | double | N/A | The Heat Exchanger flow heat transfer coefficient adjustment (user input) over the outer Surface |
| [[motorcad/parameter_database/parameters/h_HeatEx_inner|h_HeatEx_inner]] | o/p | double | W/m²/°C | The Heat Exchanger heat transfer coefficient over the inner Surface |
| [[motorcad/parameter_database/parameters/h_HeatEx_inner_forconv|h_HeatEx_inner_forconv]] | o/p | double | W/m²/°C | The Heat Exchanger forced convection heat transfer coefficient over the inner Surface |
| [[motorcad/parameter_database/parameters/h_HeatEx_inner_mixed|h_HeatEx_inner_mixed]] | o/p | double | W/m²/°C | The Heat Exchanger mixed heat transfer coefficient over the inner Surface |
| [[motorcad/parameter_database/parameters/h_HeatEx_outer_forconv|h_HeatEx_outer_forconv]] | o/p | double | W/m²/°C | The Heat Exchanger forced convection heat transfer coefficient over the outer Surface |
| [[motorcad/parameter_database/parameters/h_HeatEx_outer_mixed|h_HeatEx_outer_mixed]] | o/p | double | W/m²/°C | The Heat Exchanger mixed heat transfer coefficient over the outer Surface |
| [[motorcad/parameter_database/parameters/h_HeatEx_outer_natconv|h_HeatEx_outer_natconv]] | o/p | double | W/m²/°C | The Heat Exchanger natural convection heat transfer coefficient over the outer Surface |
| [[motorcad/parameter_database/parameters/h_Input_HeatEx_inner|h_Input_HeatEx_inner]] | i/p | double | W/m²/°C | The Heat Exchanger flow heat transfer coefficient (user input) over the inner Surface |
| [[motorcad/parameter_database/parameters/h_Input_HeatEx_outer|h_Input_HeatEx_outer]] | i/p | double | W/m²/°C | The Heat Exchanger flow heat transfer coefficient (user input) over the outer Surface |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
