---
type: motorcad_parameter_category
category_name: Thermal
parameter_count: 36
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Thermal

## Overview
The **Thermal** category contains **36** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/CalculationRunning_Therm|CalculationRunning_Therm]] | o/p | boolean | N/A | When set true the Thermal calculation is running |
| [[motorcad/parameter_database/parameters/Conductivity_Air_Ambient|Conductivity_Air_Ambient]] | o/p | double | W/m/°C | Thermal conductivity of air at T[Ambient] |
| [[motorcad/parameter_database/parameters/Conductivity_Air_Tsupply|Conductivity_Air_Tsupply]] | o/p | double | W/m/°C | Thermal conductivity of air at T[supplied] |
| [[motorcad/parameter_database/parameters/Conductivity_RotorBar|Conductivity_RotorBar]] | o/p | double | W/m/°C | The equivalent thermal conductivity of the rotor bar taking into account all components |
| [[motorcad/parameter_database/parameters/Cp_Air_Ambient|Cp_Air_Ambient]] | o/p | double | J/kg/°C | Specific heat of air at T[Ambient] |
| [[motorcad/parameter_database/parameters/Cp_Air_Tsupply|Cp_Air_Tsupply]] | o/p | double | J/kg/°C | Specific heat of air at T[supplied] |
| [[motorcad/parameter_database/parameters/Cp_RotorBar|Cp_RotorBar]] | o/p | double | J/kg/°C | The equivalent specific heat capacity of the rotor bar taking into account all components |
| [[motorcad/parameter_database/parameters/Density_Air_Ambient|Density_Air_Ambient]] | o/p | double | kg/m³ | Density of air at T[Ambient] |
| [[motorcad/parameter_database/parameters/Density_Air_Tsupply|Density_Air_Tsupply]] | o/p | double | kg/m³ | Density of air at T[supplied] |
| [[motorcad/parameter_database/parameters/Density_RotorBar|Density_RotorBar]] | o/p | double | kg/m³ | The equivalent density of the rotor bar taking into account all components |
| [[motorcad/parameter_database/parameters/Density_US_Standard_Atmosphere|Density_US_Standard_Atmosphere]] | o/p | double | kg/m³ | Air Density at given Altitude - from US Standard Atmosphere Tables, 1976 |
| [[motorcad/parameter_database/parameters/Dynamic_Viscosity_Air_Ambient|Dynamic_Viscosity_Air_Ambient]] | o/p | double | kg/m/s | Dynamic viscosity of air at T[Ambient] |
| [[motorcad/parameter_database/parameters/Dynamic_Viscosity_Air_Tsupply|Dynamic_Viscosity_Air_Tsupply]] | o/p | double | kg/m/s | Dynamic viscosity of air at T[supplied] |
| [[motorcad/parameter_database/parameters/Flux_Ratio|Flux_Ratio]] | o/p | double | N/A | Proportion of magnet flux at actual magnet temperature compared to Tm given in loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/Iph|Iph]] | o/p | double | Amps | Phase current required to achive Shaft Torque at actual temperature |
| [[motorcad/parameter_database/parameters/Iph_at_Tw_and_Tm|Iph_at_Tw_and_Tm]] | o/p | double | Amps | Phase current required to achive Shaft Torque at Tw & Tm given iron & copper loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/Kinematic_Viscosity_Air_Ambient|Kinematic_Viscosity_Air_Ambient]] | o/p | double | m²/s | Kinematic viscosity of air at T[Ambient] |
| [[motorcad/parameter_database/parameters/Kinematic_Viscosity_Air_Tsupply|Kinematic_Viscosity_Air_Tsupply]] | o/p | double | m²/s | Kinematic viscosity of air at T[supplied] |
| [[motorcad/parameter_database/parameters/MaxNumSchematicNodes|MaxNumSchematicNodes]] | o/p | integer | N/A | Maximum number of thermal model nodes |
| [[motorcad/parameter_database/parameters/Power_Mech|Power_Mech]] | o/p | double | Watts | Mechanical loss at actual temperature |
| [[motorcad/parameter_database/parameters/Power_Mech_at_Tm|Power_Mech_at_Tm]] | o/p | double | Watts | Mechanical loss at Tm given iron loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/Pr_Air_Ambient|Pr_Air_Ambient]] | o/p | double | N/A | Prandtl number of air at T[Ambient] |
| [[motorcad/parameter_database/parameters/Pr_Air_Tsupply|Pr_Air_Tsupply]] | o/p | double | N/A | Prandtl number of air at T[supplied] |
| [[motorcad/parameter_database/parameters/Pressure_Air_Ambient|Pressure_Air_Ambient]] | o/p | double | Pa | Air Pressure at given Altitude and T[Ambient] - from US Standard Atmosphere Tables, 1976 |
| [[motorcad/parameter_database/parameters/Pressure_Air_Tsupply|Pressure_Air_Tsupply]] | o/p | double | Pa | Air Pressure at given Altitude and T[supplied] - from US Standard Atmosphere Tables, 1976 |
| [[motorcad/parameter_database/parameters/Pressure_US_Standard_Atmosphere|Pressure_US_Standard_Atmosphere]] | o/p | double | Pa | Air Pressure at given Altitude - from US Standard Atmosphere Tables, 1976 |
| [[motorcad/parameter_database/parameters/Proximity_Winding_Resistance_Multiplier|Proximity_Winding_Resistance_Multiplier]] | o/p | double | N/A | Winding active thermal resistances are multiplied by this factor to model concentration of copper loss at centre of slot due to AC Winding effects |
| [[motorcad/parameter_database/parameters/Rph|Rph]] | o/p | double | Ohms | Phase resistance at actual temperature |
| [[motorcad/parameter_database/parameters/Rph_20C|Rph_20C]] | o/p | double | Ohms | Phase resistance at 20C |
| [[motorcad/parameter_database/parameters/Temperature_US_Standard_Atmosphere|Temperature_US_Standard_Atmosphere]] | o/p | double | °C | Air Temperature at given Altitude - from US Standard Atmosphere Tables, 1976 |
| [[motorcad/parameter_database/parameters/Torque_EM|Torque_EM]] | o/p | double | Nm | Electro-magnetic Torque at actual temperature |
| [[motorcad/parameter_database/parameters/Torque_EM_at_Tm|Torque_EM_at_Tm]] | o/p | double | Nm | Electro-magnetic Torque at Tm given iron loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/Torque_Mech|Torque_Mech]] | o/p | double | Watts | Mechanical torque loss at actual temperature |
| [[motorcad/parameter_database/parameters/Torque_Mech_at_Tm|Torque_Mech_at_Tm]] | o/p | double | Watts | Mechanical torque loss at Tm given iron loss variation with temperature & load |
| [[motorcad/parameter_database/parameters/Torque_Shaft_Required|Torque_Shaft_Required]] | o/p | double | Nm | Required Shaft Torque |
| [[motorcad/parameter_database/parameters/VolumeFlowRateMultiplierCalculation|VolumeFlowRateMultiplierCalculation]] | compatibility | integer | N/A | Calculate the volume flow rate unit multiplier exactly or use old truncated values. |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
