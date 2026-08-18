---
type: motorcad_parameter_category
category_name: ModelParameters_MotorLAB
parameter_count: 236
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: ModelParameters_MotorLAB

## Overview
The **ModelParameters_MotorLAB** category contains **236** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/ACLossMethod_Maxwell_Lab|ACLossMethod_Maxwell_Lab]] | i/p | integer | N/A | Method used to calculate AC losses in Maxwell when using Ansys Maxwell Lab link |
| [[motorcad/parameter_database/parameters/ACLossModelBuildPoints_Current_Lab|ACLossModelBuildPoints_Current_Lab]] | i/p | integer | N/A | Number of current points in Lab full FEA AC loss model build |
| [[motorcad/parameter_database/parameters/ACLossModelBuildPoints_Gamma_Lab|ACLossModelBuildPoints_Gamma_Lab]] | i/p | integer | N/A | Number of phase advance points in Lab full FEA AC loss model build |
| [[motorcad/parameter_database/parameters/ACLossModelBuildPoints_Lab|ACLossModelBuildPoints_Lab]] | i/p | integer | N/A | Number of points in Lab FEA map AC loss model build |
| [[motorcad/parameter_database/parameters/ACLossModelBuildPoints_Speed_Lab|ACLossModelBuildPoints_Speed_Lab]] | i/p | integer | N/A | Number of speed points in Lab full FEA AC loss model build |
| [[motorcad/parameter_database/parameters/ACLossModel_Gamma_Lab|ACLossModel_Gamma_Lab]] | i/p | double | EDeg | Lab phase advance (AC loss model) |
| [[motorcad/parameter_database/parameters/ACLossModel_Ir_Lab|ACLossModel_Ir_Lab]] | i/p | double | Amps | Lab rotor current (AC loss model) |
| [[motorcad/parameter_database/parameters/ACLossModel_Is_Lab|ACLossModel_Is_Lab]] | i/p | double | Amps | Lab stator current (AC loss model) |
| [[motorcad/parameter_database/parameters/ACLossModel_Speed_Lab|ACLossModel_Speed_Lab]] | i/p | double | rpm | Lab shaft speed (AC loss model) |
| [[motorcad/parameter_database/parameters/ACLosses_BundleHeight_Maxwell_Lab|ACLosses_BundleHeight_Maxwell_Lab]] | i/p | double | mm | Bundle Height used for AC loss calculation in the Maxwell lab model |
| [[motorcad/parameter_database/parameters/AEDTInstallPath_Lab|AEDTInstallPath_Lab]] | i/p | OleStr | N/A | The directory containing the AEDT exe. |
| [[motorcad/parameter_database/parameters/AEDTProjectLocation_Lab|AEDTProjectLocation_Lab]] | i/p | OleStr | N/A | The location of the AEDT project file. |
| [[motorcad/parameter_database/parameters/AutoShowResults_MotorLAB|AutoShowResults_MotorLAB]] | i/p | boolean | N/A | When true, the Lab results viewer will automatically be shown on completion of calculations |
| [[motorcad/parameter_database/parameters/BandingComponentNames_Maxwell_Lab|BandingComponentNames_Maxwell_Lab]] | i/p | OleStr | N/A | The names of the banding for the Maxwell lab model |
| [[motorcad/parameter_database/parameters/BandingLossCalc_Lab|BandingLossCalc_Lab]] | i/p | integer | N/A | Lab Banding loss calculation method |
| [[motorcad/parameter_database/parameters/BandingLossCoefficient_Lab|BandingLossCoefficient_Lab]] | i/p | double | N/A | Lab Banding loss speed scaling coefficient |
| [[motorcad/parameter_database/parameters/BuildSatModel_MotorLAB|BuildSatModel_MotorLAB]] | i/p | boolean | N/A | When true, the Lab Saturation Model will be built |
| [[motorcad/parameter_database/parameters/ComparisonPath_Lab|ComparisonPath_Lab]] | i/p | OleStr | N/A | Folder Path to the Comparison file used in Lab |
| [[motorcad/parameter_database/parameters/CorelossOnField_Maxwell_Lab|CorelossOnField_Maxwell_Lab]] | i/p | double | Watts | The core loss on the field in the Maxwell-Lab model |
| [[motorcad/parameter_database/parameters/CustomLoss_AllowedValues_Lab|CustomLoss_AllowedValues_Lab]] | recommended | integer | N/A | Whether negative loss or voltage values are allowed in the Lab custom losses. When negative values are not allowed, negative values will be replaced by 0. |
| [[motorcad/parameter_database/parameters/CustomLoss_Function_Internal_Lab|CustomLoss_Function_Internal_Lab]] | i/p | OleStr | N/A | Function for Lab internal custom losses |
| [[motorcad/parameter_database/parameters/CustomLoss_Name_External_Lab|CustomLoss_Name_External_Lab]] | i/p | OleStr | N/A | Name for Lab external custom losses |
| [[motorcad/parameter_database/parameters/CustomLoss_Name_Internal_Lab|CustomLoss_Name_Internal_Lab]] | i/p | OleStr | N/A | Name for Lab internal custom losses |
| [[motorcad/parameter_database/parameters/CustomLoss_PowerFunction_External_Lab|CustomLoss_PowerFunction_External_Lab]] | i/p | OleStr | N/A | Power function for Lab external custom losses |
| [[motorcad/parameter_database/parameters/CustomLoss_ThermalNode_Internal_Lab|CustomLoss_ThermalNode_Internal_Lab]] | i/p | integer | N/A | Node to which the internal custom loss is applied in thermal model |
| [[motorcad/parameter_database/parameters/CustomLoss_Type_Internal_Lab|CustomLoss_Type_Internal_Lab]] | i/p | OleStr | N/A | Type of custom loss (mechanical or electrical) |
| [[motorcad/parameter_database/parameters/CustomLoss_VoltageFunction_External_Lab|CustomLoss_VoltageFunction_External_Lab]] | i/p | OleStr | N/A | Function for voltage drop for lab external custom losses |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Array_CurrentPU_Lab|CustomModelPoints_Array_CurrentPU_Lab]] | i/p | double | N/A | Array of stator current (per unit) points for custom resolution of Lab model build |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Array_CurrentRMS_Lab|CustomModelPoints_Array_CurrentRMS_Lab]] | i/p | double | Amps | Array of stator current RMS points for custom resolution of Lab model build |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Array_Current_Lab|CustomModelPoints_Array_Current_Lab]] | i/p | double | Amps | Array of stator current peak points for custom resolution of Lab model build |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Array_Gamma_Lab|CustomModelPoints_Array_Gamma_Lab]] | i/p | double | EDeg | Array of phase advance points for custom resolution of Lab model build |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Array_RotorCurrentPU_Lab|CustomModelPoints_Array_RotorCurrentPU_Lab]] | i/p | double | N/A | Array of rotor current (per unit) points for custom resolution of Lab model build |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Array_RotorCurrent_Lab|CustomModelPoints_Array_RotorCurrent_Lab]] | i/p | double | Amps | Array of rotor current points for custom resolution of Lab model build |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Array_Speed_Lab|CustomModelPoints_Array_Speed_Lab]] | i/p | double | rpm | Array of speed points for custom resolution of Lab model build |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Current_Lab|CustomModelPoints_Current_Lab]] | i/p | integer | N/A | Number of current points in Lab saturation/loss model build custom resolution array. |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Gamma_Lab|CustomModelPoints_Gamma_Lab]] | i/p | integer | N/A | Number of phase advance points in Lab saturation/loss model build custom resolution array. |
| [[motorcad/parameter_database/parameters/CustomModelPoints_RotorCurrent_Lab|CustomModelPoints_RotorCurrent_Lab]] | i/p | integer | N/A | Number of rotor current points in Lab saturation/loss model build custom resolution array. |
| [[motorcad/parameter_database/parameters/CustomModelPoints_Speed_Lab|CustomModelPoints_Speed_Lab]] | i/p | integer | N/A | Number of speed points in Lab saturation/loss model build custom resolution array. |
| [[motorcad/parameter_database/parameters/CustomModelPoints_UnitDefinition_Lab|CustomModelPoints_UnitDefinition_Lab]] | i/p | integer | N/A | Define custom resolution points for the model build using Per Unit (PU) or absolute values |
| [[motorcad/parameter_database/parameters/DCCurrentLimitExternaLine_Method_Lab|DCCurrentLimitExternaLine_Method_Lab]] | compatibility | integer | N/A | Improved method includes losses due to external line resistance when calculating the Lab DC current limit |
| [[motorcad/parameter_database/parameters/DCCurrentLimitOptimisationMethod_Lab|DCCurrentLimitOptimisationMethod_Lab]] | compatibility | integer | N/A | Whether we optimise for torque (original) or copper losses (improved) when we have a DC current limit in generating mode |
| [[motorcad/parameter_database/parameters/EndWindingInductance_Lab|EndWindingInductance_Lab]] | i/p | double | Henry | End winding inductance (per phase) used in the Lab model |
| [[motorcad/parameter_database/parameters/EndWindingResistance_Field_Lab|EndWindingResistance_Field_Lab]] | i/p | double | Ohms | Field end winding resistance used in the Lab model |
| [[motorcad/parameter_database/parameters/EndWindingResistance_Lab|EndWindingResistance_Lab]] | i/p | double | Ohms | End winding resistance (per phase) used in the Lab model |
| [[motorcad/parameter_database/parameters/FEALossMap_RefSpeed_Lab|FEALossMap_RefSpeed_Lab]] | i/p | double | rpm | Speed at which Lab FEA map magnet, sleeve and banding loss models are built |
| [[motorcad/parameter_database/parameters/FastRotorSkewInterpMethod_Lab|FastRotorSkewInterpMethod_Lab]] | compatibility | integer | N/A | Method for limiting interpolated phase advance points to the model build range when using fast rotor skew. |
| [[motorcad/parameter_database/parameters/FastRotorSkew_Lab|FastRotorSkew_Lab]] | i/p | integer | N/A | Uses the saturation model to account for rotor skew slices. Incompatible with computing the torque ripple model |
| [[motorcad/parameter_database/parameters/Frequency_AnalyticalACLoss_Maxwell|Frequency_AnalyticalACLoss_Maxwell]] | i/p | double | Hz | The frequency values for analytical AC loss calculation in the Maxwell lab model. |
| [[motorcad/parameter_database/parameters/IMEndringCurrentMethod_Lab|IMEndringCurrentMethod_Lab]] | compatibility | integer | N/A | Method of calculating endring current in Lab |
| [[motorcad/parameter_database/parameters/IMFixedModelParametersMethod_Lab|IMFixedModelParametersMethod_Lab]] | compatibility | integer | N/A | Current and slip definition used to compute fixed equivalent circuit parameters for Lab |
| [[motorcad/parameter_database/parameters/IMMagnetizingInductanceFEAMethod_Lab|IMMagnetizingInductanceFEAMethod_Lab]] | compatibility | integer | N/A | Method of applying magnetizing inductance multiplier to IM machines with FEA model |
| [[motorcad/parameter_database/parameters/IMSlipLimitMethod_Lab|IMSlipLimitMethod_Lab]] | compatibility | integer | N/A | Limits for slip when optimising in Lab |
| [[motorcad/parameter_database/parameters/IMStatorLeakageInductanceFEALookupMethod|IMStatorLeakageInductanceFEALookupMethod]] | compatibility | integer | N/A | If fixed or variable stator leakage inductance is used in the Lab IM FEA saturation model |
| [[motorcad/parameter_database/parameters/IM_AirgapMeshPoints_AdvancedFEA_Lab|IM_AirgapMeshPoints_AdvancedFEA_Lab]] | i/p | double | N/A | The number of airgap mesh points used for advanced FEA Lab simulations |
| [[motorcad/parameter_database/parameters/IM_ConvergenceTolerance_AdvancedFEA_Lab|IM_ConvergenceTolerance_AdvancedFEA_Lab]] | i/p | integer | N/A | Convergence Tollerance for advanced FEA simulations |
| [[motorcad/parameter_database/parameters/IM_FeLossModelPoints_MotorLAB|IM_FeLossModelPoints_MotorLAB]] | i/p | integer | N/A | Number of points in Lab IM loss model |
| [[motorcad/parameter_database/parameters/IM_IphFeArray_MotorLAB|IM_IphFeArray_MotorLAB]] | i/p | double | Amps | No description |
| [[motorcad/parameter_database/parameters/IM_IphLmArray_MotorLAB|IM_IphLmArray_MotorLAB]] | i/p | double | Amps | No description |
| [[motorcad/parameter_database/parameters/IM_IronLoss_Points_Lab|IM_IronLoss_Points_Lab]] | i/p | integer | N/A | Number of points to define the iron loss model |
| [[motorcad/parameter_database/parameters/IM_L1_MotorLAB|IM_L1_MotorLAB]] | i/p | double | Henry | Stator leakage inductance (Lab model) |
| [[motorcad/parameter_database/parameters/IM_L2_MotorLAB|IM_L2_MotorLAB]] | i/p | double | Henry | Referred rotor leakage inductance (Lab model) |
| [[motorcad/parameter_database/parameters/IM_LmCurve_MotorLAB|IM_LmCurve_MotorLAB]] | i/p | boolean | N/A | Curve fit magnetizing inductance data: only use to help convergence |
| [[motorcad/parameter_database/parameters/IM_MagnetizingInductance_Points_Lab|IM_MagnetizingInductance_Points_Lab]] | i/p | integer | N/A | Number of points to define the magnetizing inductance saturation model. |
| [[motorcad/parameter_database/parameters/IM_NoPointsPerCycle_AdvancedFEA_Lab|IM_NoPointsPerCycle_AdvancedFEA_Lab]] | i/p | integer | N/A | Number of points per cycle for advanced FEA simulations |
| [[motorcad/parameter_database/parameters/IM_ParallelInductanceModel_Lab|IM_ParallelInductanceModel_Lab]] | i/p | double | Henry | Parallel inductance values Lab (IM rotor leakage inductance model) |
| [[motorcad/parameter_database/parameters/IM_ParallelResistanceModel_Lab|IM_ParallelResistanceModel_Lab]] | i/p | double | Ohms | Parallel resistance values Lab (IM rotor resistance model) |
| [[motorcad/parameter_database/parameters/IM_R1_MotorLAB|IM_R1_MotorLAB]] | i/p | double | Ohms | Phase resistance (Lab model) |
| [[motorcad/parameter_database/parameters/IM_R2_MotorLAB|IM_R2_MotorLAB]] | i/p | double | Ohms | Referred rotor resistance (Lab model) |
| [[motorcad/parameter_database/parameters/IM_RotorBarsMeshSize_AdvancedFEA_Lab|IM_RotorBarsMeshSize_AdvancedFEA_Lab]] | i/p | double | N/A | The rotor bars mesh size used for advanced FEA Lab simulations [mm] |
| [[motorcad/parameter_database/parameters/IM_RotorLeakageInductanceModel_Is_Lab|IM_RotorLeakageInductanceModel_Is_Lab]] | i/p | double | Amps | Stator currents Lab (IM rotor leakage inductance model) |
| [[motorcad/parameter_database/parameters/IM_RotorLeakage_Points_Lab|IM_RotorLeakage_Points_Lab]] | i/p | integer | N/A | Number of points to define the rotor leakage saturation model |
| [[motorcad/parameter_database/parameters/IM_RotorResistanceModelType_Lab|IM_RotorResistanceModelType_Lab]] | i/p | integer | N/A | Type of Model Used for IM Rotor Resistance Model in Advanced IM Lab |
| [[motorcad/parameter_database/parameters/IM_RotorResistanceModel_Fr_Lab|IM_RotorResistanceModel_Fr_Lab]] | i/p | double | Hz | Rotor frequencies Lab (IM rotor resistance model) |
| [[motorcad/parameter_database/parameters/IM_RotorResistance_Points_Lab|IM_RotorResistance_Points_Lab]] | i/p | integer | N/A | Number of points to define the rotor resistance frequency model |
| [[motorcad/parameter_database/parameters/IM_RtrBarC_MotorLAB|IM_RtrBarC_MotorLAB]] | i/p | double | N/A | Rotor bar conductivity (Lab model) |
| [[motorcad/parameter_database/parameters/IM_RtrBarH_MotorLAB|IM_RtrBarH_MotorLAB]] | i/p | double | mm | Rotor bar height (Lab model) |
| [[motorcad/parameter_database/parameters/IM_SaturationModelType_Lab|IM_SaturationModelType_Lab]] | i/p | integer | N/A | Type of model used for IM magnetizing inductance model |
| [[motorcad/parameter_database/parameters/IM_SlipFixedModelParameters_Lab|IM_SlipFixedModelParameters_Lab]] | i/p | double | N/A | Slip value to compute IM fixed equivalent circuit parameters in Lab |
| [[motorcad/parameter_database/parameters/IM_SlipRes_MotorLAB|IM_SlipRes_MotorLAB]] | i/p | double | N/A | No description |
| [[motorcad/parameter_database/parameters/InitialImport_MotorLAB|InitialImport_MotorLAB]] | i/p | boolean | N/A | Whether the initial model data has been imported into Lab module |
| [[motorcad/parameter_database/parameters/InitialPhaseAlignment_Maxwell_Lab|InitialPhaseAlignment_Maxwell_Lab]] | i/p | integer | N/A | Introduce an initial angle between the rotor d-axis and the stator phase? |
| [[motorcad/parameter_database/parameters/InitialPhaseoffsetAngle_Maxwell_Lab|InitialPhaseoffsetAngle_Maxwell_Lab]] | i/p | double | MDeg | The initial angle for phaseoffset between rotor d-axis and stator phase |
| [[motorcad/parameter_database/parameters/IronLossModelSplit_Lab|IronLossModelSplit_Lab]] | recommended | integer | N/A | Method for splitting the iron losses between the stator/rotor in Lab |
| [[motorcad/parameter_database/parameters/IronLossModelSplit_Rotor_Lab|IronLossModelSplit_Rotor_Lab]] | i/p | integer | N/A | Method for splitting the rotor iron losses between rotor components in Lab |
| [[motorcad/parameter_database/parameters/IronLossModelSplit_Stator_Lab|IronLossModelSplit_Stator_Lab]] | i/p | integer | N/A | Method for splitting the stator iron losses between stator components in Lab |
| [[motorcad/parameter_database/parameters/Isc_MotorLAB|Isc_MotorLAB]] | i/p | double | Amps | Short circuit current |
| [[motorcad/parameter_database/parameters/LEndWdg_MotorLAB|LEndWdg_MotorLAB]] | i/p | double | Henry | Additional end winding adjustment: useful with calibration calculation and short circuit test. |
| [[motorcad/parameter_database/parameters/LabModel_ACLoss_CalculationMethod|LabModel_ACLoss_CalculationMethod]] | i/p | integer | N/A | AC Loss Model Type for currently built Lab model |
| [[motorcad/parameter_database/parameters/LabModel_ACLoss_Date|LabModel_ACLoss_Date]] | i/p | OleStr | N/A | Lab saturation model build date |
| [[motorcad/parameter_database/parameters/LabModel_ACLoss_MaxSpeed|LabModel_ACLoss_MaxSpeed]] | i/p | double | rpm | Maximum speed for which full FEA AC Loss Lab Model is valid |
| [[motorcad/parameter_database/parameters/LabModel_ACLoss_Method|LabModel_ACLoss_Method]] | i/p | integer | N/A | Stator Copper Loss Calculation Type for currently built Lab model |
| [[motorcad/parameter_database/parameters/LabModel_ACLoss_RotorCurrent|LabModel_ACLoss_RotorCurrent]] | i/p | double | Amps | Maximum rotor current used in Lab AC loss model build |
| [[motorcad/parameter_database/parameters/LabModel_ACLoss_StatorCurrent_Peak|LabModel_ACLoss_StatorCurrent_Peak]] | i/p | double | Amps | Maximum stator current used in Lab AC loss model build (peak) |
| [[motorcad/parameter_database/parameters/LabModel_ACLoss_StatorCurrent_RMS|LabModel_ACLoss_StatorCurrent_RMS]] | i/p | double | Amps | Maximum stator current used in Lab AC loss model build (rms) |
| [[motorcad/parameter_database/parameters/LabModel_BandingLoss_Date|LabModel_BandingLoss_Date]] | i/p | OleStr | N/A | Lab banding loss model build date |
| [[motorcad/parameter_database/parameters/LabModel_BandingLoss_Method|LabModel_BandingLoss_Method]] | i/p | integer | N/A | Lab banding loss model build method |
| [[motorcad/parameter_database/parameters/LabModel_BandingLoss_RotorCurrent|LabModel_BandingLoss_RotorCurrent]] | i/p | double | Amps | Maximum rotor current used in Lab banding loss model build |
| [[motorcad/parameter_database/parameters/LabModel_BandingLoss_StatorCurrent_Peak|LabModel_BandingLoss_StatorCurrent_Peak]] | i/p | double | Amps | Maximum stator current used in Lab banding loss model build (peak) |
| [[motorcad/parameter_database/parameters/LabModel_BandingLoss_StatorCurrent_RMS|LabModel_BandingLoss_StatorCurrent_RMS]] | i/p | double | Amps | Maximum stator current used in Lab banding loss model build (rms) |
| [[motorcad/parameter_database/parameters/LabModel_IronLoss_Date|LabModel_IronLoss_Date]] | i/p | OleStr | N/A | Lab saturation model build date |
| [[motorcad/parameter_database/parameters/LabModel_IronLoss_Method|LabModel_IronLoss_Method]] | i/p | integer | N/A | Lab iron loss model build method |
| [[motorcad/parameter_database/parameters/LabModel_IronLoss_RotorCurrent|LabModel_IronLoss_RotorCurrent]] | i/p | double | Amps | Maximum rotor current used in Lab iron loss model build |
| [[motorcad/parameter_database/parameters/LabModel_IronLoss_StatorCurrent_Peak|LabModel_IronLoss_StatorCurrent_Peak]] | i/p | double | Amps | Maximum stator current used in Lab iron loss model build (peak) |
| [[motorcad/parameter_database/parameters/LabModel_IronLoss_StatorCurrent_RMS|LabModel_IronLoss_StatorCurrent_RMS]] | i/p | double | Amps | Maximum stator current used in Lab iron loss model build (rms) |
| [[motorcad/parameter_database/parameters/LabModel_MagnetLoss_Date|LabModel_MagnetLoss_Date]] | i/p | OleStr | N/A | Lab magnet loss model build date |
| [[motorcad/parameter_database/parameters/LabModel_MagnetLoss_Method|LabModel_MagnetLoss_Method]] | i/p | integer | N/A | Lab magnet loss model build method |
| [[motorcad/parameter_database/parameters/LabModel_MagnetLoss_RotorCurrent|LabModel_MagnetLoss_RotorCurrent]] | i/p | double | Amps | Maximum rotor current used in Lab magnet loss model build |
| [[motorcad/parameter_database/parameters/LabModel_MagnetLoss_StatorCurrent_Peak|LabModel_MagnetLoss_StatorCurrent_Peak]] | i/p | double | Amps | Maximum stator current used in Lab magnet loss model build (peak) |
| [[motorcad/parameter_database/parameters/LabModel_MagnetLoss_StatorCurrent_RMS|LabModel_MagnetLoss_StatorCurrent_RMS]] | i/p | double | Amps | Maximum stator current used in Lab magnet loss model build (rms) |
| [[motorcad/parameter_database/parameters/LabModel_Saturation_Date|LabModel_Saturation_Date]] | i/p | OleStr | N/A | Lab saturation model build date |
| [[motorcad/parameter_database/parameters/LabModel_Saturation_Method|LabModel_Saturation_Method]] | i/p | integer | N/A | Lab saturation model build method |
| [[motorcad/parameter_database/parameters/LabModel_Saturation_NumPoints|LabModel_Saturation_NumPoints]] | i/p | integer | N/A | Number of points in Lab saturation model build |
| [[motorcad/parameter_database/parameters/LabModel_Saturation_RotorCurrent|LabModel_Saturation_RotorCurrent]] | i/p | double | Amps | Maximum rotor current used in Lab saturation model build |
| [[motorcad/parameter_database/parameters/LabModel_Saturation_StatorCurrent_Peak|LabModel_Saturation_StatorCurrent_Peak]] | i/p | double | Amps | Maximum stator current used in Lab saturation model build (peak) |
| [[motorcad/parameter_database/parameters/LabModel_Saturation_StatorCurrent_RMS|LabModel_Saturation_StatorCurrent_RMS]] | i/p | double | Amps | Maximum stator current used in Lab saturation model build (rms) |
| [[motorcad/parameter_database/parameters/LabModel_SleeveLoss_Date|LabModel_SleeveLoss_Date]] | i/p | OleStr | N/A | Lab sleeve loss model build date |
| [[motorcad/parameter_database/parameters/LabModel_SleeveLoss_Method|LabModel_SleeveLoss_Method]] | i/p | integer | N/A | Lab sleeve loss model build method |
| [[motorcad/parameter_database/parameters/LabModel_SleeveLoss_RotorCurrent|LabModel_SleeveLoss_RotorCurrent]] | i/p | double | Amps | Maximum rotor current used in Lab sleeve loss model build |
| [[motorcad/parameter_database/parameters/LabModel_SleeveLoss_StatorCurrent_Peak|LabModel_SleeveLoss_StatorCurrent_Peak]] | i/p | double | Amps | Maximum stator current used in Lab sleeve loss model build (peak) |
| [[motorcad/parameter_database/parameters/LabModel_SleeveLoss_StatorCurrent_RMS|LabModel_SleeveLoss_StatorCurrent_RMS]] | i/p | double | Amps | Maximum stator current used in Lab sleeve loss model build (rms) |
| [[motorcad/parameter_database/parameters/LabOpPoint_CustomLoss_Internal|LabOpPoint_CustomLoss_Internal]] | o/p | double | Watts | Internal Custom Loss (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_CustomLoss_Power_External|LabOpPoint_CustomLoss_Power_External]] | o/p | double | Watts | External Custom Power Loss (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_CustomLoss_Total_Internal|LabOpPoint_CustomLoss_Total_Internal]] | o/p | double | Watts | Total Internal Custom Power Loss (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_CustomLoss_Total_Power_External|LabOpPoint_CustomLoss_Total_Power_External]] | o/p | double | Watts | Total External Custom Power Loss (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_CustomLoss_Total_Voltage_External|LabOpPoint_CustomLoss_Total_Voltage_External]] | o/p | double | Volts | Total External Custom Voltage Drop (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_CustomLoss_Voltage_External|LabOpPoint_CustomLoss_Voltage_External]] | o/p | double | Volts | External Custom Voltage Drop (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_CustomThermalLimitsTemperatures|LabOpPoint_CustomThermalLimitsTemperatures]] | o/p | double | °C | Custom Thermal Limits Temperatures (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_ExternalLineLoss|LabOpPoint_ExternalLineLoss]] | o/p | double | Watts | External line loss (operating point result) |
| [[motorcad/parameter_database/parameters/LabOpPoint_ShaftSpeed|LabOpPoint_ShaftSpeed]] | o/p | double | rpm | Shaft Speed (Operating Point Result) |
| [[motorcad/parameter_database/parameters/LabProgressBar_MaxMultithreadingPercentage|LabProgressBar_MaxMultithreadingPercentage]] | o/p | double | N/A | Maximum percentage that multithreading calculations should contribute during Lab model build calculations. |
| [[motorcad/parameter_database/parameters/LamM_MotorLAB|LamM_MotorLAB]] | i/p | double | Vs | PM Flux linkage |
| [[motorcad/parameter_database/parameters/Ld_MotorLAB|Ld_MotorLAB]] | i/p | double | Henry | D-Axis inductance |
| [[motorcad/parameter_database/parameters/Length_Calc_Lab|Length_Calc_Lab]] | i/p | double | mm | Active length used in Lab calculations |
| [[motorcad/parameter_database/parameters/Length_Ref_Lab|Length_Ref_Lab]] | i/p | double | mm | Active length used in Lab model build (longest of rotor lam/stator lam/magnet lengths) |
| [[motorcad/parameter_database/parameters/Length_Ref_Resistance_Lab|Length_Ref_Resistance_Lab]] | i/p | double | mm | Active length used as reference for Lab winding resistance |
| [[motorcad/parameter_database/parameters/LossModelBuildPoints_Lab|LossModelBuildPoints_Lab]] | i/p | integer | N/A | Number of points in Lab FEA map loss model build |
| [[motorcad/parameter_database/parameters/LossModel_AC_Lab|LossModel_AC_Lab]] | i/p | double | Watts | Lab AC Excitation Loss FEA map model |
| [[motorcad/parameter_database/parameters/LossModel_Banding_Lab|LossModel_Banding_Lab]] | i/p | double | Watts | Banding Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/LossModel_Gamma_Lab|LossModel_Gamma_Lab]] | i/p | double | EDeg | Lab phase advance (loss model) |
| [[motorcad/parameter_database/parameters/LossModel_Ir_Lab|LossModel_Ir_Lab]] | i/p | double | Amps | Lab Sync rotor current (loss model) |
| [[motorcad/parameter_database/parameters/LossModel_Is_Lab|LossModel_Is_Lab]] | i/p | double | Amps | Lab stator current (loss model) |
| [[motorcad/parameter_database/parameters/LossModel_Sleeve_Lab|LossModel_Sleeve_Lab]] | i/p | double | Watts | Sleeve Loss (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/LossModel_Speed_Lab|LossModel_Speed_Lab]] | i/p | double | rpm | Lab rotor speed (loss model) |
| [[motorcad/parameter_database/parameters/Lq_MotorLAB|Lq_MotorLAB]] | i/p | double | Henry | Q-Axis inductance |
| [[motorcad/parameter_database/parameters/MachineComponentType_Maxwell_BPM|MachineComponentType_Maxwell_BPM]] | i/p | integer | N/A | The type of the machine component shown in the machine component grid for BPM |
| [[motorcad/parameter_database/parameters/MachineComponentType_Maxwell_IM|MachineComponentType_Maxwell_IM]] | i/p | integer | N/A | The type of the machine component shown in the machine component grid for IM |
| [[motorcad/parameter_database/parameters/MachineComponentType_Maxwell_SYNC|MachineComponentType_Maxwell_SYNC]] | i/p | integer | N/A | The type of the machine component shown in the machine component grid for SYNC |
| [[motorcad/parameter_database/parameters/MagnetComponentNames_Maxwell_Lab|MagnetComponentNames_Maxwell_Lab]] | i/p | OleStr | N/A | The names of the magnet components for the Maxwell lab model |
| [[motorcad/parameter_database/parameters/MaxModelCurrent_MotorLAB|MaxModelCurrent_MotorLAB]] | i/p | double | Amps | Maximum stator current used in model build (peak) |
| [[motorcad/parameter_database/parameters/MaxModelCurrent_RMS_MotorLAB|MaxModelCurrent_RMS_MotorLAB]] | i/p | double | Amps | Maximum stator current used in model build (rms) |
| [[motorcad/parameter_database/parameters/MaxModelCurrent_Rotor_Lab|MaxModelCurrent_Rotor_Lab]] | i/p | double | Amps | Maximum rotor current used in model build |
| [[motorcad/parameter_database/parameters/MaxwellActiveDesignName_Lab|MaxwellActiveDesignName_Lab]] | i/p | OleStr | N/A | The design name of the copied Maxwell model which was created via the Maxwell-Lab link API. This is the design that will be analysed. |
| [[motorcad/parameter_database/parameters/MaxwellDesignName_Lab|MaxwellDesignName_Lab]] | i/p | OleStr | N/A | The design name of the Maxwell model used for Ansys Lab link |
| [[motorcad/parameter_database/parameters/MaxwellParameterDictionary_Lab|MaxwellParameterDictionary_Lab]] | i/p | OleStr | N/A | The parameter dictionary for the Maxwell-Lab link stored as a json string |
| [[motorcad/parameter_database/parameters/MaxwellToolkitLibPath_Lab|MaxwellToolkitLibPath_Lab]] | i/p | OleStr | N/A | The location of the Toolkit of Ansys Maxwell |
| [[motorcad/parameter_database/parameters/ModelBuildGammaDistribution_Lab|ModelBuildGammaDistribution_Lab]] | compatibility | integer | N/A | Method of distributing the phase advance values in Lab saturation/loss model build when using 30 points |
| [[motorcad/parameter_database/parameters/ModelBuildOption_Maxwell_Lab|ModelBuildOption_Maxwell_Lab]] | i/p | integer | N/A | Whether to build the full model or use the split analysis. |
| [[motorcad/parameter_database/parameters/ModelBuildPoints_Current_Lab|ModelBuildPoints_Current_Lab]] | i/p | integer | N/A | Number of current points in Lab saturation/loss model build |
| [[motorcad/parameter_database/parameters/ModelBuildPoints_Gamma_Lab|ModelBuildPoints_Gamma_Lab]] | i/p | integer | N/A | Number of phase advance points in Lab saturation/loss model build |
| [[motorcad/parameter_database/parameters/ModelBuildPoints_ResolutionType_Lab|ModelBuildPoints_ResolutionType_Lab]] | i/p | integer | N/A | Which method of spacing for model build points |
| [[motorcad/parameter_database/parameters/ModelBuildPoints_RotorCurrent_Lab|ModelBuildPoints_RotorCurrent_Lab]] | i/p | integer | N/A | Number of rotor current points in Lab saturation/loss model build |
| [[motorcad/parameter_database/parameters/ModelBuildPoints_Speed_Lab|ModelBuildPoints_Speed_Lab]] | i/p | integer | N/A | Number of speed points in Lab model build. |
| [[motorcad/parameter_database/parameters/ModelBuildSpeed_Min_Lab|ModelBuildSpeed_Min_Lab]] | i/p | double | rpm | Minimum speed used when building the Lab model with speed mapping. |
| [[motorcad/parameter_database/parameters/ModelBuildSpeed_MotorLAB|ModelBuildSpeed_MotorLAB]] | i/p | integer | rpm | Maximum speed used when building the Lab loss model, used with magnet, AC, sleeve and banding loss models |
| [[motorcad/parameter_database/parameters/ModelType_MotorLAB|ModelType_MotorLAB]] | i/p | integer | N/A | Saturation model type |
| [[motorcad/parameter_database/parameters/ModulationIndex_MotorLAB|ModulationIndex_MotorLAB]] | i/p | double | N/A | Utilisation of DC link voltage for peak line-line terminal voltage |
| [[motorcad/parameter_database/parameters/MotorCADexeName|MotorCADexeName]] | persistent | OleStr | N/A | File name of the Motor-CAD executable program |
| [[motorcad/parameter_database/parameters/MotorCADprocessID|MotorCADprocessID]] | persistent | OleStr | N/A | Process ID of this instance of Motor-CAD |
| [[motorcad/parameter_database/parameters/NoBandingComponents_Maxwell|NoBandingComponents_Maxwell]] | setting | integer | N/A | The number of banding components for the Maxwell lab model |
| [[motorcad/parameter_database/parameters/NoEntries_AnalyticalACLoss_Maxwell|NoEntries_AnalyticalACLoss_Maxwell]] | setting | integer | N/A | The number of entries in the look-up table for the analytical AC loss calculation in the Maxwell lab model. |
| [[motorcad/parameter_database/parameters/NoMagnetComponents_Maxwell|NoMagnetComponents_Maxwell]] | setting | integer | N/A | The number of magnet components for the Maxwell lab model |
| [[motorcad/parameter_database/parameters/NoOnLoadFrequencyPoints_Maxwell_Lab|NoOnLoadFrequencyPoints_Maxwell_Lab]] | i/p | integer | N/A | The number of frequency points for the on load resistance calculation with the Maxwell-Lab link. |
| [[motorcad/parameter_database/parameters/NoRotorCoreLossComponents_Maxwell_Lab|NoRotorCoreLossComponents_Maxwell_Lab]] | i/p | integer | N/A | The number of rotor core loss components in the Maxwell-Lab model |
| [[motorcad/parameter_database/parameters/NoSleeveComponents_Maxwell|NoSleeveComponents_Maxwell]] | setting | integer | N/A | The number of sleeve components for the Maxwell lab model |
| [[motorcad/parameter_database/parameters/NoStatorCoreLossComponents_Maxwell_Lab|NoStatorCoreLossComponents_Maxwell_Lab]] | i/p | integer | N/A | The number of stator core loss components in the Maxwell-Lab model |
| [[motorcad/parameter_database/parameters/NoStatorWindings_SYNC_Maxwell|NoStatorWindings_SYNC_Maxwell]] | i/p | integer | N/A | The number of stator windings for the Maxwell SYNC lab model. |
| [[motorcad/parameter_database/parameters/NoWindingGroups_FEAACLoss_Maxwell|NoWindingGroups_FEAACLoss_Maxwell]] | setting | integer | N/A | The number of winding groups used for the full FEA AC loss calculation in the Maxwell lab model. |
| [[motorcad/parameter_database/parameters/NumCustomLossesExternal_Lab|NumCustomLossesExternal_Lab]] | i/p | integer | N/A | Number of external custom losses defined in Lab |
| [[motorcad/parameter_database/parameters/NumCustomLossesInternal_Lab|NumCustomLossesInternal_Lab]] | i/p | integer | N/A | Number of internal custom losses defined in Lab |
| [[motorcad/parameter_database/parameters/NumElecCycles_Lab|NumElecCycles_Lab]] | i/p | integer | N/A | The number of electric cycles for the Maxwell model |
| [[motorcad/parameter_database/parameters/NumberOfCuboids_LossModel_Lab|NumberOfCuboids_LossModel_Lab]] | i/p | integer | N/A | Number of cuboids used in the Lab FEA map loss model build |
| [[motorcad/parameter_database/parameters/OnLoadFrequencyArray_Maxwell_Lab|OnLoadFrequencyArray_Maxwell_Lab]] | i/p | double | Hz | The frequency array for the on load rotor resistance calculation with the Maxwell-Lab link |
| [[motorcad/parameter_database/parameters/OnLoadFrequency_Maxwell_Lab|OnLoadFrequency_Maxwell_Lab]] | i/p | double | Hz | The frequency for the on load leakage inductance calculation with the Maxwell-Lab link |
| [[motorcad/parameter_database/parameters/PhaseOffset_Maxwell_Lab|PhaseOffset_Maxwell_Lab]] | i/p | double | N/A | The phase offset in the Maxwell-Lab model |
| [[motorcad/parameter_database/parameters/PhaseResistance_AnalyticalACLoss_Maxwell|PhaseResistance_AnalyticalACLoss_Maxwell]] | i/p | double | Ohms | The phase resistance values for the analytical AC loss calculation in the Maxwell lab model. |
| [[motorcad/parameter_database/parameters/PhaseResistance_Maxwell_Lab|PhaseResistance_Maxwell_Lab]] | i/p | double | Ohms | The phase resistance of the stator windings in the Maxwell-Lab model. |
| [[motorcad/parameter_database/parameters/PointsPerElecCycle_Lab|PointsPerElecCycle_Lab]] | i/p | integer | N/A | The number of points per electric cycle for the Maxwell model |
| [[motorcad/parameter_database/parameters/Pole_MotorLAB|Pole_MotorLAB]] | i/p | integer | N/A | Number of poles |
| [[motorcad/parameter_database/parameters/PsiDModel_Lab|PsiDModel_Lab]] | i/p | double | Vs | Lab Saturation Model D-axis flux linkage values |
| [[motorcad/parameter_database/parameters/PsiD_coeff_MotorLAB|PsiD_coeff_MotorLAB]] | i/p | double | N/A | No description |
| [[motorcad/parameter_database/parameters/PsiQModel_Lab|PsiQModel_Lab]] | i/p | double | Vs | Lab Saturation Model Q-axis flux linkage values |
| [[motorcad/parameter_database/parameters/PsiQ_coeff_MotorLAB|PsiQ_coeff_MotorLAB]] | i/p | double | N/A | No description |
| [[motorcad/parameter_database/parameters/Resistance_ModelBuild_Lab|Resistance_ModelBuild_Lab]] | i/p | double | Ohms | Winding Resistance Per Phase in current Lab Model Build |
| [[motorcad/parameter_database/parameters/ResultsPath_MotorLAB|ResultsPath_MotorLAB]] | i/p | OleStr | N/A | Folder path to Lab results folder |
| [[motorcad/parameter_database/parameters/RotorCopperLossCalc_Lab|RotorCopperLossCalc_Lab]] | i/p | integer | N/A | Rotor Copper Loss calculation type |
| [[motorcad/parameter_database/parameters/RotorCoreLossComponents_Maxwell_Lab|RotorCoreLossComponents_Maxwell_Lab]] | i/p | OleStr | N/A | The rotor core loss components in the Maxwell-Lab model. |
| [[motorcad/parameter_database/parameters/RotorWindingName_Maxwell_Lab|RotorWindingName_Maxwell_Lab]] | i/p | OleStr | N/A | The name of the rotor winding used for the Maxwell lab model. |
| [[motorcad/parameter_database/parameters/RotorWindingResistance_Lab|RotorWindingResistance_Lab]] | i/p | double | Ohms | Rotor winding resistance |
| [[motorcad/parameter_database/parameters/RotorWindingTempCoeffResistivity_Lab|RotorWindingTempCoeffResistivity_Lab]] | i/p | double | N/A | Temperature coefficient of resistivity for rotor winding (used in electromagnetic calculations) |
| [[motorcad/parameter_database/parameters/RotorWindingTemp_Calc_Lab|RotorWindingTemp_Calc_Lab]] | i/p | double | °C | Rotor winding temperature used in electromagnetic calculations |
| [[motorcad/parameter_database/parameters/RotorWindingTemp_Ref_Lab|RotorWindingTemp_Ref_Lab]] | i/p | double | °C | Reference rotor winding temperature for resistance value |
| [[motorcad/parameter_database/parameters/SatModelBuildPoints_Lab|SatModelBuildPoints_Lab]] | i/p | integer | N/A | Number of points in Lab saturation model build |
| [[motorcad/parameter_database/parameters/SatModelPoints_MotorLAB|SatModelPoints_MotorLAB]] | i/p | integer | N/A | Resolution of the Lab saturation model for BPM, BPMOR and SYNCREL motors. When custom is selected then the same resolution will be used for the FEA map loss model. |
| [[motorcad/parameter_database/parameters/SatModel_Gamma_Lab|SatModel_Gamma_Lab]] | i/p | double | EDeg | Lab Saturation Model phase advance values |
| [[motorcad/parameter_database/parameters/SatModel_Is_Lab|SatModel_Is_Lab]] | i/p | double | Amps | Lab Saturation Model stator current values |
| [[motorcad/parameter_database/parameters/SatModel_Speed_Lab|SatModel_Speed_Lab]] | i/p | double | rpm | Lab Saturation Model rotor speed values |
| [[motorcad/parameter_database/parameters/SaturationModelGoodness_Lab|SaturationModelGoodness_Lab]] | i/p | double | Percent | Average agreement (%) between the flux linkage data points and saturation model curve fit. |
| [[motorcad/parameter_database/parameters/SaturationModelGoodness_RotorCurrent_Lab|SaturationModelGoodness_RotorCurrent_Lab]] | i/p | double | Percent | Average percentage error between the flux linkage data points and saturation model for each Sync rotor current level. |
| [[motorcad/parameter_database/parameters/SaturationModelInterpolation_Lab|SaturationModelInterpolation_Lab]] | i/p | integer | N/A | Interpolation method used for the flux linkages in the Lab model (linear or cubic spline) |
| [[motorcad/parameter_database/parameters/SaturationModelMethod_Lab|SaturationModelMethod_Lab]] | recommended | integer | N/A | Method used to calculate the flux linkages in the Lab model |
| [[motorcad/parameter_database/parameters/SleeveComponentNames_Maxwell_Lab|SleeveComponentNames_Maxwell_Lab]] | i/p | OleStr | N/A | The names of the sleeve for the Maxwell lab model |
| [[motorcad/parameter_database/parameters/SleeveLossCalc_Lab|SleeveLossCalc_Lab]] | i/p | integer | N/A | Lab Sleeve loss calculation method |
| [[motorcad/parameter_database/parameters/SleeveLossCoefficient_Lab|SleeveLossCoefficient_Lab]] | i/p | double | N/A | Lab Sleeve loss speed scaling coefficient |
| [[motorcad/parameter_database/parameters/Slots_MotorLAB|Slots_MotorLAB]] | i/p | integer | N/A | Number of slots (Lab model) |
| [[motorcad/parameter_database/parameters/SpeedVariationType_Lab|SpeedVariationType_Lab]] | i/p | integer | N/A | Use speed mapping or speed scaling in Lab model |
| [[motorcad/parameter_database/parameters/StatorCoreLossComponents_Maxwell_Lab|StatorCoreLossComponents_Maxwell_Lab]] | i/p | OleStr | N/A | The stator core loss components in the Maxwell-Lab model. |
| [[motorcad/parameter_database/parameters/StatorWindingResistivityAt20C_Maxwell_Lab|StatorWindingResistivityAt20C_Maxwell_Lab]] | i/p | double | N/A | The electrical resistivity of the stator winding at 20C for the Maxwell lab model |
| [[motorcad/parameter_database/parameters/StatorWindings_SYNC_Maxwell_Lab|StatorWindings_SYNC_Maxwell_Lab]] | i/p | OleStr | N/A | The names of the stator windings used for the Maxwell SYNC lab model. |
| [[motorcad/parameter_database/parameters/SyncRel_MotorLAB|SyncRel_MotorLAB]] | i/p | boolean | N/A | Machine is synchronous reluctance |
| [[motorcad/parameter_database/parameters/Sync_FeEddyLoss_Lab|Sync_FeEddyLoss_Lab]] | i/p | double | Watts | Lab Sync eddy current losses |
| [[motorcad/parameter_database/parameters/Sync_FeHysLoss_Lab|Sync_FeHysLoss_Lab]] | i/p | double | Watts | Lab Sync hysteresis losses |
| [[motorcad/parameter_database/parameters/Sync_IrSatModel_Lab|Sync_IrSatModel_Lab]] | i/p | double | Amps | Lab Saturation Model rotor current values (Sync) |
| [[motorcad/parameter_database/parameters/Sync_ModelPoints_Lab|Sync_ModelPoints_Lab]] | i/p | integer | N/A | Resolution of the Lab saturation/loss models for SYNC motors. |
| [[motorcad/parameter_database/parameters/Sync_ModelSkewMethod_Lab|Sync_ModelSkewMethod_Lab]] | compatibility | integer | N/A | Method used to calculate skew for Sync motors during Lab model build |
| [[motorcad/parameter_database/parameters/Sync_NumIrPoints_Lab|Sync_NumIrPoints_Lab]] | i/p | integer | N/A | Number of rotor current points in Lab Sync model build |
| [[motorcad/parameter_database/parameters/Sync_SaturationModelType_Lab|Sync_SaturationModelType_Lab]] | i/p | integer | N/A | Saturation model type (Sync) |
| [[motorcad/parameter_database/parameters/TimeoutMultiplier_Lab|TimeoutMultiplier_Lab]] | i/p | integer | N/A | Multiplier for Lab timeout limits. |
| [[motorcad/parameter_database/parameters/TmagnetCalc_MotorLAB|TmagnetCalc_MotorLAB]] | i/p | double | °C | Magnet temperature used in Lab electromagnetic calculations |
| [[motorcad/parameter_database/parameters/TorqueRippleModel_Lab|TorqueRippleModel_Lab]] | i/p | double | Nm | Torque Ripple (Lab FEA map model) |
| [[motorcad/parameter_database/parameters/TurnsCalc_MotorLAB|TurnsCalc_MotorLAB]] | i/p | double | N/A | No. of turns per coil used in calculations |
| [[motorcad/parameter_database/parameters/TurnsRef_MotorLAB|TurnsRef_MotorLAB]] | i/p | double | N/A | No. of turns per coil used in model build |
| [[motorcad/parameter_database/parameters/TwindingCalc_MotorLAB|TwindingCalc_MotorLAB]] | i/p | double | °C | Winding temperature used in Lab electromagnetic calculations |
| [[motorcad/parameter_database/parameters/Vdrop_MotorLAB|Vdrop_MotorLAB]] | i/p | boolean | N/A | Include voltage drop across winding resistance |
| [[motorcad/parameter_database/parameters/WindingAlpha_MotorLAB|WindingAlpha_MotorLAB]] | i/p | double | N/A | Scaling of DC winding resistance with temperature |
| [[motorcad/parameter_database/parameters/WindingGroupNames_FEAACLoss_Maxwell_Lab|WindingGroupNames_FEAACLoss_Maxwell_Lab]] | i/p | OleStr | N/A | The names of the winding groups used for the full FEA AC loss calculation in the Maxwell lab model. |
| [[motorcad/parameter_database/parameters/XEndLeak_MotorLAB|XEndLeak_MotorLAB]] | i/p | double | N/A | Adjustment factor for PM flux components |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
