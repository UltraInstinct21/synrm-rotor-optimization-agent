---
type: motorcad_parameter_category
category_name: ThermalParameters_MotorLAB
parameter_count: 42
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: ThermalParameters_MotorLAB

## Overview
The **ThermalParameters_MotorLAB** category contains **42** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/BrTempCoeff_MotorLAB|BrTempCoeff_MotorLAB]] | i/p | double | %/°C | Change of magnet flux with temperature |
| [[motorcad/parameter_database/parameters/CustomThermalLimitName_Lab|CustomThermalLimitName_Lab]] | i/p | OleStr | N/A | Name of the custom thermal limit |
| [[motorcad/parameter_database/parameters/CustomThermalLimitNode_Lab|CustomThermalLimitNode_Lab]] | i/p | integer | N/A | Node of the custom thermal limit |
| [[motorcad/parameter_database/parameters/CustomThermalLimitTemperature_Lab|CustomThermalLimitTemperature_Lab]] | i/p | double | °C | Temperature of the custom thermal limit |
| [[motorcad/parameter_database/parameters/CustomThermalLimit_Lab|CustomThermalLimit_Lab]] | i/p | boolean | N/A | Whether to include the custom thermal limit |
| [[motorcad/parameter_database/parameters/IM_SllRotorSplit_MotorLAB|IM_SllRotorSplit_MotorLAB]] | i/p | double | N/A | Stray load loss proportion in rotor |
| [[motorcad/parameter_database/parameters/IM_SllStatorSplit_MotorLAB|IM_SllStatorSplit_MotorLAB]] | i/p | double | N/A | Stray load loss proportion in stator |
| [[motorcad/parameter_database/parameters/Iest_MotorLAB|Iest_MotorLAB]] | i/p | double | Amps | Initial stator current estimate (peak) |
| [[motorcad/parameter_database/parameters/Iest_RMS_MotorLAB|Iest_RMS_MotorLAB]] | i/p | double | Amps | Initial stator current estimate(rms) |
| [[motorcad/parameter_database/parameters/LossProp_RotorBackIron_Lab|LossProp_RotorBackIron_Lab]] | i/p | double | N/A | Proportion of the rotor iron losses that are in the back iron in Lab calculations |
| [[motorcad/parameter_database/parameters/LossProp_RotorPole_Lab|LossProp_RotorPole_Lab]] | i/p | double | N/A | Proportion of the rotor iron losses that are in the magnet pole in Lab calculations |
| [[motorcad/parameter_database/parameters/LossProp_Rotor_Lab|LossProp_Rotor_Lab]] | i/p | double | N/A | Proportion of the iron losses that are in the rotor in Lab calculations |
| [[motorcad/parameter_database/parameters/LossProp_StatorBackIron_Lab|LossProp_StatorBackIron_Lab]] | i/p | double | N/A | Proportion of the stator iron losses that are in the back iron in Lab calculations |
| [[motorcad/parameter_database/parameters/LossProp_StatorTooth_Lab|LossProp_StatorTooth_Lab]] | i/p | double | N/A | Proportion of the stator iron losses that are in the tooth in Lab calculations |
| [[motorcad/parameter_database/parameters/LossProp_Stator_Lab|LossProp_Stator_Lab]] | i/p | double | N/A | Proportion of the iron losses that are in the stator in Lab calculations |
| [[motorcad/parameter_database/parameters/MaxMagnet_MotorLAB|MaxMagnet_MotorLAB]] | i/p | double | °C | Maximum magnet temperature |
| [[motorcad/parameter_database/parameters/MaxSpeedTherm_MotorLAB|MaxSpeedTherm_MotorLAB]] | i/p | double | rpm | The maximum speed in the Lab thermal envelope calculation |
| [[motorcad/parameter_database/parameters/MaxTemperatureTransferMethod_Lab|MaxTemperatureTransferMethod_Lab]] | compatibility | integer | N/A | Method used to transfer temperatures from Lab Max Temperature operating point to thermal for IM and Sync machines |
| [[motorcad/parameter_database/parameters/MaxWindTemp_MotorLAB|MaxWindTemp_MotorLAB]] | i/p | double | °C | The maximum winding temperature allowed in the Lab thermal envelope calculation |
| [[motorcad/parameter_database/parameters/MaxWindingSpec_MotorLAB|MaxWindingSpec_MotorLAB]] | i/p | integer | N/A | Limit performance on maximum or peak winding temperature |
| [[motorcad/parameter_database/parameters/MinSpeedTherm_Lab|MinSpeedTherm_Lab]] | i/p | double | rpm | The minimum speed in the Lab thermal envelope calculation |
| [[motorcad/parameter_database/parameters/NumCustomThermalLimits_Lab|NumCustomThermalLimits_Lab]] | i/p | integer | N/A | Number of Custom Thermal Limits |
| [[motorcad/parameter_database/parameters/RotorTemperatureIterationsBeforeAverage_Lab|RotorTemperatureIterationsBeforeAverage_Lab]] | i/p | integer | N/A | Number of iterations before averaging is used in rotor temperature convergence loop in Lab thermal calculations |
| [[motorcad/parameter_database/parameters/RotorTemperatureIterationsInAverage_Lab|RotorTemperatureIterationsInAverage_Lab]] | i/p | integer | N/A | Number of iteration steps over which the average is taken in rotor temperature convergence loop in Lab thermal calculations |
| [[motorcad/parameter_database/parameters/RotorTemperatureMaxDivergingSteps_Lab|RotorTemperatureMaxDivergingSteps_Lab]] | i/p | integer | N/A | Maximum number of diverging steps allowed  in rotor temperature convergence loop in Lab thermal calculations |
| [[motorcad/parameter_database/parameters/RotorTemperatureMaxIterations_Lab|RotorTemperatureMaxIterations_Lab]] | i/p | integer | N/A | Maximum number of iterations allowed in rotor temperature convergence loop in Lab thermal calculations |
| [[motorcad/parameter_database/parameters/RotorTemperatureTolerance_Lab|RotorTemperatureTolerance_Lab]] | i/p | double | Percent | Maximum error (%) tolerance allowed in rotor temperature convergence loop in Lab thermal calculations |
| [[motorcad/parameter_database/parameters/SpeedStepTherm_MotorLAB|SpeedStepTherm_MotorLAB]] | i/p | double | rpm | The speed step used in the Lab thermal envelope calculation |
| [[motorcad/parameter_database/parameters/TempLimit_MotorLAB|TempLimit_MotorLAB]] | i/p | integer | N/A | How the thermal envelope is limited (stator only orr stator and rotor temperatures) |
| [[motorcad/parameter_database/parameters/ThermCalcType_MotorLAB|ThermCalcType_MotorLAB]] | i/p | integer | N/A | Transient or steady state thermal calculation |
| [[motorcad/parameter_database/parameters/ThermEnvBuilt_MotorLAB|ThermEnvBuilt_MotorLAB]] | i/p | boolean | N/A | Whether the Lab thermal envelope calculation has been completed |
| [[motorcad/parameter_database/parameters/ThermMapBuilt_MotorLAB|ThermMapBuilt_MotorLAB]] | i/p | boolean | N/A | Whether the Lab thermal map calculation has been completed |
| [[motorcad/parameter_database/parameters/ThermMaxCurrentLim_MotorLAB|ThermMaxCurrentLim_MotorLAB]] | i/p | boolean | N/A | Limit thermal envelope on maximum current |
| [[motorcad/parameter_database/parameters/ThermalCalcStatus_MotorLAB|ThermalCalcStatus_MotorLAB]] | i/p | OleStr | N/A | Status of the Lab thermal calculation |
| [[motorcad/parameter_database/parameters/ThermalConvergenceMethod_Lab|ThermalConvergenceMethod_Lab]] | compatibility | integer | N/A | Method used for convergence in Lab thermal calculations |
| [[motorcad/parameter_database/parameters/ThermalEnvelopeSensitivity_Lab|ThermalEnvelopeSensitivity_Lab]] | i/p | double | N/A | Sensitivity of the Lab thermal envelope & max temperature operating point. If the thermal model temperatures are more sensitive to changing losses then this factor should be increased to aid convergence. |
| [[motorcad/parameter_database/parameters/ThermalMapType_Lab|ThermalMapType_Lab]] | i/p | integer | N/A | Type of thermal map calculation (Envelope or Full Map) |
| [[motorcad/parameter_database/parameters/ThermalStatorWindingTemperatureMethod_Lab|ThermalStatorWindingTemperatureMethod_Lab]] | compatibility | integer | N/A | Stator winding temperature used for calculating machine performance in Lab thermal calculations |
| [[motorcad/parameter_database/parameters/Thermal_TemperaturesForEMag_Lab|Thermal_TemperaturesForEMag_Lab]] | recommended | integer | N/A | Temperatures used to calculate the e-magnetic performance in Lab thermal calculations for IM and Sync machines |
| [[motorcad/parameter_database/parameters/Tmag_MotorLAB|Tmag_MotorLAB]] | i/p | double | °C | Reference magnet temperature for inductances and saturation model |
| [[motorcad/parameter_database/parameters/Twdg_MotorLAB|Twdg_MotorLAB]] | i/p | double | °C | Reference winding temperature for resistance value |
| [[motorcad/parameter_database/parameters/WindingTemp_ACLoss_Ref_Lab|WindingTemp_ACLoss_Ref_Lab]] | i/p | double | °C | Reference winding temperature for Lab AC winding loss FEA map model |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
