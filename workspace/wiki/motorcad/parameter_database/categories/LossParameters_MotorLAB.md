---
type: motorcad_parameter_category
category_name: LossParameters_MotorLAB
parameter_count: 62
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: LossParameters_MotorLAB

## Overview
The **LossParameters_MotorLAB** category contains **62** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/ACConductorLossProportion_Lab|ACConductorLossProportion_Lab]] | i/p | double | N/A | This is the proportion of AC winding losses in each cuboid for the Lab AC loss model |
| [[motorcad/parameter_database/parameters/ACConductorLossSplit_Lab|ACConductorLossSplit_Lab]] | recommended | integer | N/A | How the AC winding losses are distributed between cuboids when Lab is coupled to the Thermal model |
| [[motorcad/parameter_database/parameters/ACLossGeneratorMethod_Lab|ACLossGeneratorMethod_Lab]] | compatibility | integer | N/A | How the AC winding losses are calculated for generating points in the Lab model |
| [[motorcad/parameter_database/parameters/ACLossMap_FullFEA_ExtrapMethod_Lab|ACLossMap_FullFEA_ExtrapMethod_Lab]] | compatibility | integer | N/A | Method for extrapolating losses from Full FEA AC loss map outside Lab model build speed range. |
| [[motorcad/parameter_database/parameters/ACLossMethod_Lab|ACLossMethod_Lab]] | i/p | integer | N/A | Method used to calculate AC losses in Lab model build |
| [[motorcad/parameter_database/parameters/ACLossSpeedScalingMethod_Lab|ACLossSpeedScalingMethod_Lab]] | compatibility | integer | N/A | How the AC winding losses are scaled with speed in the Lab model |
| [[motorcad/parameter_database/parameters/AcLossFreq_MotorLAB|AcLossFreq_MotorLAB]] | i/p | double | N/A | Scaling of Rac/Rdc with frequency |
| [[motorcad/parameter_database/parameters/Ae_MotorLAB|Ae_MotorLAB]] | i/p | double | N/A | Eddy open circuit loss coefficient |
| [[motorcad/parameter_database/parameters/Ah_MotorLAB|Ah_MotorLAB]] | i/p | double | N/A | Hysteresis open circuit loss coefficient |
| [[motorcad/parameter_database/parameters/Be_MotorLAB|Be_MotorLAB]] | i/p | double | N/A | Eddy short circuit loss coefficient |
| [[motorcad/parameter_database/parameters/Bh_MotorLAB|Bh_MotorLAB]] | i/p | double | N/A | Hysteresis short circuit loss coefficient |
| [[motorcad/parameter_database/parameters/BuildLossModel_MotorLAB|BuildLossModel_MotorLAB]] | i/p | boolean | N/A | When true, the Lab Loss Model will be built |
| [[motorcad/parameter_database/parameters/CalcTypeCuLoss_MotorLAB|CalcTypeCuLoss_MotorLAB]] | i/p | integer | N/A | Copper loss model type used in Lab calculations |
| [[motorcad/parameter_database/parameters/ElectricalCustomLoss_Method_Lab|ElectricalCustomLoss_Method_Lab]] | compatibility | integer | N/A | Improved method separates custom electrical losses into internal and external, and display system and motor parameters for Efficiency, Terminal Power, and Losses |
| [[motorcad/parameter_database/parameters/FeEddyLossArray_MotorLAB|FeEddyLossArray_MotorLAB]] | i/p | double | Watts | Total Eddy Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeEddyLossArray_Rotor_Lab|FeEddyLossArray_Rotor_Lab]] | i/p | double | Watts | Total Eddy Loss in the Rotor (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeEddyLossArray_Stator_Lab|FeEddyLossArray_Stator_Lab]] | i/p | double | Watts | Total Eddy Loss in the Stator (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeHysLossArray_MotorLAB|FeHysLossArray_MotorLAB]] | i/p | double | Watts | Total Hysteresis Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeHysLossArray_Rotor_Lab|FeHysLossArray_Rotor_Lab]] | i/p | double | Watts | Total Hysteresis Loss in the Rotor (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeHysLossArray_Stator_Lab|FeHysLossArray_Stator_Lab]] | i/p | double | Watts | Total Hysteresis Loss in the Stator (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossBackIronEd_MotorLAB|FeLossBackIronEd_MotorLAB]] | i/p | double | Watts | Stator Back Iron Eddy Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossBackIronHy_MotorLAB|FeLossBackIronHy_MotorLAB]] | i/p | double | Watts | Stator Back Iron Hysteresis Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossRotorEd_MotorLAB|FeLossRotorEd_MotorLAB]] | i/p | double | Watts | Rotor Back Iron Eddy Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossRotorHy_MotorLAB|FeLossRotorHy_MotorLAB]] | i/p | double | Watts | Rotor Back Iron Hysteresis Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossRotorPoleEd_MotorLAB|FeLossRotorPoleEd_MotorLAB]] | i/p | double | Watts | Embedded Magnet Pole Eddy Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossRotorPoleHy_MotorLAB|FeLossRotorPoleHy_MotorLAB]] | i/p | double | Watts | Embedded Magnet Pole Hysteresis Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossToothEd_MotorLAB|FeLossToothEd_MotorLAB]] | i/p | double | Watts | Stator Tooth Eddy Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/FeLossToothHy_MotorLAB|FeLossToothHy_MotorLAB]] | i/p | double | Watts | Stator Tooth Hysteresis Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/IM_FeEddyLossArray_MotorLAB|IM_FeEddyLossArray_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeHysLossArray_MotorLAB|IM_FeHysLossArray_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_RotorBackIronEddy_MotorLAB|IM_FeLoss_RotorBackIronEddy_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_RotorBackIronHys_MotorLAB|IM_FeLoss_RotorBackIronHys_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_RotorToothEddy_MotorLAB|IM_FeLoss_RotorToothEddy_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_RotorToothHys_MotorLAB|IM_FeLoss_RotorToothHys_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_StatorBackIronEddy_MotorLAB|IM_FeLoss_StatorBackIronEddy_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_StatorBackIronHys_MotorLAB|IM_FeLoss_StatorBackIronHys_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_StatorToothEddy_MotorLAB|IM_FeLoss_StatorToothEddy_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_FeLoss_StatorToothHys_MotorLAB|IM_FeLoss_StatorToothHys_MotorLAB]] | i/p | double | Watts | No description |
| [[motorcad/parameter_database/parameters/IM_IronLossCalc_MotorLAB|IM_IronLossCalc_MotorLAB]] | i/p | integer | N/A | Iron loss model type |
| [[motorcad/parameter_database/parameters/IM_LmArray_MotorLAB|IM_LmArray_MotorLAB]] | i/p | double | Henry | No description |
| [[motorcad/parameter_database/parameters/Imag_MotorLAB|Imag_MotorLAB]] | i/p | double | Amps | Current at which on-load magnet loss is derived (peak) |
| [[motorcad/parameter_database/parameters/IronLossCalc_Lab|IronLossCalc_Lab]] | i/p | integer | N/A | Iron loss model type used in Lab calculations |
| [[motorcad/parameter_database/parameters/LossModel_Lab|LossModel_Lab]] | i/p | integer | N/A | Lab loss model type |
| [[motorcad/parameter_database/parameters/MagLossArray_MotorLAB|MagLossArray_MotorLAB]] | i/p | double | Watts | Magnet Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/MagLossCoeff_MotorLAB|MagLossCoeff_MotorLAB]] | i/p | double | N/A | Scaling of magnet losses with speed |
| [[motorcad/parameter_database/parameters/MagnetLossCalc_Lab|MagnetLossCalc_Lab]] | i/p | integer | N/A | Magnet loss model type used in Lab calculations |
| [[motorcad/parameter_database/parameters/Nmag_MotorLAB|Nmag_MotorLAB]] | i/p | double | rpm | Speed at which on-load magnet loss is derived |
| [[motorcad/parameter_database/parameters/RacRdc_MotorLAB|RacRdc_MotorLAB]] | i/p | double | N/A | Ratio of AC to DC copper Loss |
| [[motorcad/parameter_database/parameters/Resistance_MotorLAB|Resistance_MotorLAB]] | i/p | double | Ohms | Winding resistance per phase |
| [[motorcad/parameter_database/parameters/RotorIronEddyLossExponent_Lab|RotorIronEddyLossExponent_Lab]] | i/p | double | N/A | The exponent value used for scaling of solid rotor eddy current losses with frequency in Lab |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_RotorBackIronEddy_Lab|Sync_FeLoss_RotorBackIronEddy_Lab]] | i/p | double | Watts | Lab Sync rotor back iron eddy current losses |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_RotorBackIronHys_Lab|Sync_FeLoss_RotorBackIronHys_Lab]] | i/p | double | Watts | Lab Sync rotor back iron hysteresis losses |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_RotorToothEddy_Lab|Sync_FeLoss_RotorToothEddy_Lab]] | i/p | double | Watts | Lab Sync rotor tooth eddy current losses |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_RotorToothHys_Lab|Sync_FeLoss_RotorToothHys_Lab]] | i/p | double | Watts | Lab Sync rotor tooth hysteresis losses |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_StatorBackIronEddy_Lab|Sync_FeLoss_StatorBackIronEddy_Lab]] | i/p | double | Watts | Lab Sync stator back iron eddy current losses |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_StatorBackIronHys_Lab|Sync_FeLoss_StatorBackIronHys_Lab]] | i/p | double | Watts | Lab Sync stator back iron hysteresis losses |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_StatorToothEddy_Lab|Sync_FeLoss_StatorToothEddy_Lab]] | i/p | double | Watts | Lab Sync stator tooth eddy current losses |
| [[motorcad/parameter_database/parameters/Sync_FeLoss_StatorToothHys_Lab|Sync_FeLoss_StatorToothHys_Lab]] | i/p | double | Watts | Lab Sync stator tooth hysteresis losses |
| [[motorcad/parameter_database/parameters/Sync_IronLossCalc_Lab|Sync_IronLossCalc_Lab]] | i/p | integer | N/A | Iron loss model type |
| [[motorcad/parameter_database/parameters/WmagOC_MotorLAB|WmagOC_MotorLAB]] | i/p | double | Watts | Reference open circuit loss for magnet loss model |
| [[motorcad/parameter_database/parameters/Wmag_MotorLAB|Wmag_MotorLAB]] | i/p | double | Watts | Reference on-load loss for magnet loss model |
| [[motorcad/parameter_database/parameters/n2ac_MotorLAB|n2ac_MotorLAB]] | i/p | double | rpm | Speed at which the Lab AC loss model is defined |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
