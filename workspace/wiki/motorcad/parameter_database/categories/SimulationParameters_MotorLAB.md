---
type: motorcad_parameter_category
category_name: SimulationParameters_MotorLAB
parameter_count: 87
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: SimulationParameters_MotorLAB

## Overview
The **SimulationParameters_MotorLAB** category contains **87** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AlternateStart_Method_BPM_Lab|AlternateStart_Method_BPM_Lab]] | compatibility | integer | N/A | When trying to find a successful operating point, perform a final operating point with default Id/Iq guess if it has not already been tried. |
| [[motorcad/parameter_database/parameters/CalCalcComplete_MotorLAB|CalCalcComplete_MotorLAB]] | i/p | boolean | N/A | Whether the Lab calibration calculation has been completed |
| [[motorcad/parameter_database/parameters/CalCalcStatus_MotorLAB|CalCalcStatus_MotorLAB]] | i/p | OleStr | N/A | Status of the Lab calibration calculation |
| [[motorcad/parameter_database/parameters/CalcComplete_MotorLAB|CalcComplete_MotorLAB]] | i/p | boolean | N/A | Whether the Lab electromagnetic calculation has been completed |
| [[motorcad/parameter_database/parameters/CancelCalc_MotorLAB|CancelCalc_MotorLAB]] | i/p | boolean | N/A | No description |
| [[motorcad/parameter_database/parameters/ControlStrat_MotorLAB|ControlStrat_MotorLAB]] | i/p | integer | N/A | MTPA or ME control |
| [[motorcad/parameter_database/parameters/ControlStrat_PhaseAdvance_Lab|ControlStrat_PhaseAdvance_Lab]] | i/p | double | N/A | User-specified phase advance points for the Lab control strategy |
| [[motorcad/parameter_database/parameters/ControlStrat_Speed_Lab|ControlStrat_Speed_Lab]] | i/p | double | rpm | User-specified speed points for the Lab control strategy |
| [[motorcad/parameter_database/parameters/CurrentLimitedCheckMethod_Lab|CurrentLimitedCheckMethod_Lab]] | compatibility | integer | N/A | Enable additional checks for current limited cases |
| [[motorcad/parameter_database/parameters/CustomLossVariablesExternal_Lab|CustomLossVariablesExternal_Lab]] | i/p | OleStr | N/A | Variables available for use in external custom loss functions |
| [[motorcad/parameter_database/parameters/CustomLossVariablesInternal_Lab|CustomLossVariablesInternal_Lab]] | i/p | OleStr | N/A | Variables available for use in internal custom loss functions |
| [[motorcad/parameter_database/parameters/DCCurrentLimit_Lab|DCCurrentLimit_Lab]] | i/p | integer | N/A | Whether the DC current is limited in Lab electromagnetic calculations |
| [[motorcad/parameter_database/parameters/EMCalcStatus_MotorLAB|EMCalcStatus_MotorLAB]] | i/p | OleStr | N/A | Status of the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/EmagneticCalcType_Lab|EmagneticCalcType_Lab]] | i/p | integer | N/A | Lab electromagnetic calculation type |
| [[motorcad/parameter_database/parameters/EnforceTorqueDemandLimit_Lab|EnforceTorqueDemandLimit_Lab]] | compatibility | integer | N/A | Enforce an upper limit on torque to prevent points significantly exceeding the demand. |
| [[motorcad/parameter_database/parameters/ExceedingTorqueTolFactor_Lab|ExceedingTorqueTolFactor_Lab]] | setting | double | N/A | Factor of the torque tolerance to set an upper limit on the torque demand. |
| [[motorcad/parameter_database/parameters/FunctionCaching_Lab|FunctionCaching_Lab]] | i/p | integer | N/A | Use function caching for optimisation in Lab (0=no cache, 1=small cache, 2=large cache) |
| [[motorcad/parameter_database/parameters/IM_AlternativePointStrategy_Lab|IM_AlternativePointStrategy_Lab]] | compatibility | integer | N/A | Method used for induction machine alternative point strategy in Lab operating points |
| [[motorcad/parameter_database/parameters/IM_InitialSlip_MotorLAB|IM_InitialSlip_MotorLAB]] | i/p | double | N/A | Initial slip value for convergence |
| [[motorcad/parameter_database/parameters/IM_MaxAlternativePoints_Lab|IM_MaxAlternativePoints_Lab]] | i/p | integer | N/A | The maximum number of points to attempt when retrying Lab optimisation for induction machine |
| [[motorcad/parameter_database/parameters/IM_StatorCurrentLimit_Lab|IM_StatorCurrentLimit_Lab]] | compatibility | integer | N/A | Whether the stator current is limited to the max model build current in IM Lab calculations |
| [[motorcad/parameter_database/parameters/Iinc_MotorLAB|Iinc_MotorLAB]] | i/p | integer | N/A | The number of current increments used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/Imax_MotorLAB|Imax_MotorLAB]] | i/p | double | Amps | The maximum stator current (peak) used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/Imax_RMS_MotorLAB|Imax_RMS_MotorLAB]] | i/p | double | Amps | The maximum stator current (rms) used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/Imin_MotorLAB|Imin_MotorLAB]] | i/p | double | Amps | The minimum stator current (peak) used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/Imin_RMS_MotorLAB|Imin_RMS_MotorLAB]] | i/p | double | Amps | The minimum stator current (rms) used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/InitialCurrentMethod_Lab|InitialCurrentMethod_Lab]] | compatibility | integer | N/A | Method used for estimating initial current in Lab torque demand calculations |
| [[motorcad/parameter_database/parameters/LabMagneticCoupling|LabMagneticCoupling]] | i/p | integer | N/A | How data is transferred between the Lab Operating Point calculation and E-Magnetic model |
| [[motorcad/parameter_database/parameters/LabRunning|LabRunning]] | persistent | integer | N/A | Whether Lab is currently performing calculations |
| [[motorcad/parameter_database/parameters/LabThermalCoupling|LabThermalCoupling]] | i/p | integer | N/A | How data is transferred between the Lab Operating Point calculation and Thermal model |
| [[motorcad/parameter_database/parameters/LabThermalCoupling_DutyCycle|LabThermalCoupling_DutyCycle]] | i/p | integer | N/A | How data is transferred between the Lab Duty Cycle calculation and Thermal model |
| [[motorcad/parameter_database/parameters/MagnetLossBuildFactorMethod_Lab|MagnetLossBuildFactorMethod_Lab]] | compatibility | integer | N/A | Method for applying the magnet loss build factor to the interpolated losses when speed mapping is used. |
| [[motorcad/parameter_database/parameters/MaxDCCurrent_Lab|MaxDCCurrent_Lab]] | i/p | double | Amps | Maximum available DC current |
| [[motorcad/parameter_database/parameters/MaxNumAltStartPoints_Lab|MaxNumAltStartPoints_Lab]] | i/p | integer | N/A | Maximum number of alternate start points for Lab BPM operating point optimiser |
| [[motorcad/parameter_database/parameters/MaxRotorTemp_Lab|MaxRotorTemp_Lab]] | i/p | double | °C | Maximum rotor winding temperature used in thermal calculations |
| [[motorcad/parameter_database/parameters/MinTorque_MotorLAB|MinTorque_MotorLAB]] | i/p | double | Nm | Minimum torque |
| [[motorcad/parameter_database/parameters/NonSalient_MotorLAB|NonSalient_MotorLAB]] | i/p | boolean | N/A | Force gamma=0 before base speed |
| [[motorcad/parameter_database/parameters/NumControlStrategyPoints_Lab|NumControlStrategyPoints_Lab]] | i/p | integer | N/A | Number of points in the user specified Lab control strategy |
| [[motorcad/parameter_database/parameters/NumCustomLossVariablesExternal_Lab|NumCustomLossVariablesExternal_Lab]] | i/p | integer | N/A | Number of variables available for use in Lab external custom losses |
| [[motorcad/parameter_database/parameters/NumCustomLossVariablesInternal_Lab|NumCustomLossVariablesInternal_Lab]] | i/p | integer | N/A | Number of variables available for use in Lab internal custom losses |
| [[motorcad/parameter_database/parameters/NumOutputVariables_Lab|NumOutputVariables_Lab]] | o/p | integer | N/A | Number of output variables available from Lab calculation |
| [[motorcad/parameter_database/parameters/OpPointSpec_MotorLAB|OpPointSpec_MotorLAB]] | i/p | integer | N/A | Lab operating point definition |
| [[motorcad/parameter_database/parameters/OperatingMode_Lab|OperatingMode_Lab]] | i/p | integer | N/A | Operating mode (motor or generator) for Lab map and envelope calculations |
| [[motorcad/parameter_database/parameters/OutputVariables_Lab|OutputVariables_Lab]] | o/p | OleStr | N/A | Output variables available from Lab calculation |
| [[motorcad/parameter_database/parameters/PhaseAdvanceDemand_Lab|PhaseAdvanceDemand_Lab]] | i/p | double | EDeg | The requested phase advance in the Lab operating point |
| [[motorcad/parameter_database/parameters/PowerLimVal_MotorLAB|PowerLimVal_MotorLAB]] | i/p | double | Watts | The maximum power allowed in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/PowerLim_MotorLAB|PowerLim_MotorLAB]] | i/p | boolean | N/A | Limit electromagnetic performance calculation with maximum power |
| [[motorcad/parameter_database/parameters/PrevCalcIinc_MotorLAB|PrevCalcIinc_MotorLAB]] | i/p | integer | N/A | Current increment used in the last Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/PrevCalcImax_MotorLAB|PrevCalcImax_MotorLAB]] | i/p | double | Amps | Max current used in the last Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/PrevCalcImin_MotorLAB|PrevCalcImin_MotorLAB]] | i/p | double | Amps | Min current used in the last Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/ResistanceTurnsRef_MotorLAB|ResistanceTurnsRef_MotorLAB]] | i/p | double | N/A | No. of turns per coil used for winding resistance |
| [[motorcad/parameter_database/parameters/RotorCurrentDemand_Lab|RotorCurrentDemand_Lab]] | i/p | double | Amps | Operating point rotor current requested |
| [[motorcad/parameter_database/parameters/RotorCurrentEstimate_Lab|RotorCurrentEstimate_Lab]] | i/p | double | Amps | Initial rotor current estimate used in thermal calculations |
| [[motorcad/parameter_database/parameters/RotorTempDemand_Lab|RotorTempDemand_Lab]] | i/p | double | °C | The maximum allowed rotor temperature (Lab operating point) |
| [[motorcad/parameter_database/parameters/SlipDemand_Lab|SlipDemand_Lab]] | i/p | double | N/A | The requested slip in the Lab operating point |
| [[motorcad/parameter_database/parameters/SmoothMap_MotorLAB|SmoothMap_MotorLAB]] | i/p | boolean | N/A | Spaces data differently |
| [[motorcad/parameter_database/parameters/SpeedDemand_MotorLAB|SpeedDemand_MotorLAB]] | i/p | double | rpm | Shaft Speed (operating point) |
| [[motorcad/parameter_database/parameters/SpeedMax_MotorLAB|SpeedMax_MotorLAB]] | i/p | double | rpm | The maximum speed used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/SpeedMin_MotorLAB|SpeedMin_MotorLAB]] | i/p | double | rpm | The minimum speed used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/Speedinc_MotorLAB|Speedinc_MotorLAB]] | i/p | double | rpm | The speed increment used in the Lab electromagnetic calculation |
| [[motorcad/parameter_database/parameters/StatorCurrentDemand_Lab|StatorCurrentDemand_Lab]] | i/p | double | Amps | The maximum stator current (peak) in the Lab operating point |
| [[motorcad/parameter_database/parameters/StatorCurrentDemand_RMS_Lab|StatorCurrentDemand_RMS_Lab]] | i/p | double | Amps | The maximum stator current (rms) in the Lab operating point |
| [[motorcad/parameter_database/parameters/StatorCurrentLimit_Lab|StatorCurrentLimit_Lab]] | compatibility | integer | N/A | Whether the stator current is limited to the max model build current in BPM Lab calculations |
| [[motorcad/parameter_database/parameters/StatorTempDemand_Lab|StatorTempDemand_Lab]] | i/p | double | °C | The maximum allowed stator winding temperature (Lab operating point) |
| [[motorcad/parameter_database/parameters/Sync_ControlStrategy_Lab|Sync_ControlStrategy_Lab]] | i/p | integer | N/A | Control strategy used for Sync electromagnetic calculations |
| [[motorcad/parameter_database/parameters/Sync_ConvergenceMethod_Lab|Sync_ConvergenceMethod_Lab]] | compatibility | integer | N/A | Method used for the solver convergence in Lab Sync calculations |
| [[motorcad/parameter_database/parameters/Sync_ConvergenceTolerance_Lab|Sync_ConvergenceTolerance_Lab]] | i/p | double | Percent | Maximum error (%) tolerance allowed in convergence loop in Lab Sync calculations |
| [[motorcad/parameter_database/parameters/Sync_CurrentIncs_Lab|Sync_CurrentIncs_Lab]] | i/p | integer | N/A | Number of increments used in electromagnetic map calculation |
| [[motorcad/parameter_database/parameters/Sync_InitialGamma_Lab|Sync_InitialGamma_Lab]] | i/p | double | EDeg | Initial estimate for phase advance. Can be adjusted to aid convergence. |
| [[motorcad/parameter_database/parameters/Sync_IterationsBeforeAverage_Lab|Sync_IterationsBeforeAverage_Lab]] | i/p | integer | N/A | Number of iterations before averaging is used in convergence loop in Lab Sync calculations |
| [[motorcad/parameter_database/parameters/Sync_IterationsInAverage_Lab|Sync_IterationsInAverage_Lab]] | i/p | integer | N/A | Number of iteration steps over which the average is taken in convergence loop in Lab Sync calculations |
| [[motorcad/parameter_database/parameters/Sync_MaxIterations_Lab|Sync_MaxIterations_Lab]] | i/p | integer | N/A | Maximum number of iterations allowed in convergence loop in Lab Sync calculations |
| [[motorcad/parameter_database/parameters/Sync_MinTorqueLevel_Lab|Sync_MinTorqueLevel_Lab]] | i/p | double | N/A | Min torque level (% of max). Sets the minimum torque for the map calculation, used to improve the appearance of the efficiency map. |
| [[motorcad/parameter_database/parameters/Sync_OptAcceptTol_Lab|Sync_OptAcceptTol_Lab]] | i/p | double | N/A | Sync optimisation acceptance tolerance lab |
| [[motorcad/parameter_database/parameters/Sync_OptMaxIters_Lab|Sync_OptMaxIters_Lab]] | i/p | integer | N/A | Sync optimisation maximum iterations in lab |
| [[motorcad/parameter_database/parameters/Sync_OptimisationInitialSteps_Lab|Sync_OptimisationInitialSteps_Lab]] | i/p | integer | N/A | The number of rotor current steps in the initial sweep when using the improved iteration method |
| [[motorcad/parameter_database/parameters/Sync_OptimisationIterationMethod_Lab|Sync_OptimisationIterationMethod_Lab]] | i/p | integer | N/A | Optimise the sync operating point by iterating inductance (original) or rotor current (improved) method |
| [[motorcad/parameter_database/parameters/Sync_OptimisationRefineSteps_Lab|Sync_OptimisationRefineSteps_Lab]] | i/p | integer | N/A | The number of rotor current refinement steps after the initial sweep when using the improved iteration method |
| [[motorcad/parameter_database/parameters/Sync_OptimiserMethod_Lab|Sync_OptimiserMethod_Lab]] | compatibility | integer | N/A | Method used for optimiser  in Lab Sync calculations |
| [[motorcad/parameter_database/parameters/Sync_RotorCurrentMax_Lab|Sync_RotorCurrentMax_Lab]] | i/p | double | Amps | Maximum rotor current used in electromagnetic calculations |
| [[motorcad/parameter_database/parameters/Sync_SliceMethodForCurrentLimited_Lab|Sync_SliceMethodForCurrentLimited_Lab]] | i/p | boolean | N/A | Use the improved rotor slice optimisation for current limited cases as well as torque demand cases |
| [[motorcad/parameter_database/parameters/Sync_StatorCurrentMax_Lab|Sync_StatorCurrentMax_Lab]] | i/p | double | Amps | Maximum stator current used in electromagnetic calculations (peak) |
| [[motorcad/parameter_database/parameters/Sync_StatorCurrentMax_RMS_Lab|Sync_StatorCurrentMax_RMS_Lab]] | i/p | double | Amps | Maximum stator current used in electromagnetic calculations (rms) |
| [[motorcad/parameter_database/parameters/Sync_StatorRotorLossBiasRatio_Lab|Sync_StatorRotorLossBiasRatio_Lab]] | i/p | double | N/A | Bias ratio for stator:rotor copper losses used in Min Total Copper Loss control strategy in Lab Sync |
| [[motorcad/parameter_database/parameters/TorqueDemand_MotorLAB|TorqueDemand_MotorLAB]] | i/p | double | Nm | The requested torque in the Lab operating point |
| [[motorcad/parameter_database/parameters/TorqueInc_MotorLAB|TorqueInc_MotorLAB]] | i/p | integer | N/A | No. of torque increments |
| [[motorcad/parameter_database/parameters/TorqueMax_MotorLAB|TorqueMax_MotorLAB]] | i/p | double | Nm | Maximum torque |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
