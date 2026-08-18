---
type: motorcad_parameter_category
category_name: Transient_Settings
parameter_count: 37
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Transient_Settings

## Overview
The **Transient_Settings** category contains **37** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AllowableTemperatureVariation|AllowableTemperatureVariation]] | i/p | double | °C | Allowable change in temperature before recalculating internal integration |
| [[motorcad/parameter_database/parameters/AllowableTimeVariation|AllowableTimeVariation]] | i/p | double | sec | Allowable change in time before recalculating internal integration |
| [[motorcad/parameter_database/parameters/Altitude_TransLogging|Altitude_TransLogging]] | i/p | boolean | N/A | Log altitude during thermal transient calculations |
| [[motorcad/parameter_database/parameters/Capacitances_All_TransLogging|Capacitances_All_TransLogging]] | i/p | boolean | N/A | Log all capacitances during thermal transient calculations |
| [[motorcad/parameter_database/parameters/ES_HeatTransferCoeff_TransLogging|ES_HeatTransferCoeff_TransLogging]] | i/p | boolean | N/A | Log end space heat transfer coefficients during thermal transient calculations |
| [[motorcad/parameter_database/parameters/ES_Velocity_TransLogging|ES_Velocity_TransLogging]] | i/p | boolean | N/A | Log end space velocity during thermal transient calculations |
| [[motorcad/parameter_database/parameters/EnableTemperatureVariationWithinStep|EnableTemperatureVariationWithinStep]] | i/p | boolean | N/A | When set this enabled then the parameters that vary with temperature are updated during the integration step |
| [[motorcad/parameter_database/parameters/FileName_TransLogging|FileName_TransLogging]] | i/p | OleStr | N/A | Name of logging file during thermal transient calculations |
| [[motorcad/parameter_database/parameters/FileValueSeparator_TransLogging|FileValueSeparator_TransLogging]] | i/p | integer | N/A | Value separator for logging file during thermal transient calculations |
| [[motorcad/parameter_database/parameters/FluidData_All_TransLogging|FluidData_All_TransLogging]] | i/p | boolean | N/A | Log all fluid data during thermal transient calculations |
| [[motorcad/parameter_database/parameters/FluidHeatFlowMethod|FluidHeatFlowMethod]] | compatibility | integer | N/A | Method of modelling heat flow in fluid |
| [[motorcad/parameter_database/parameters/ForcedConv_HeatTransferCoeff_TransLogging|ForcedConv_HeatTransferCoeff_TransLogging]] | i/p | boolean | N/A | Log forced convection heat transfer coefficient during thermal transient calculations |
| [[motorcad/parameter_database/parameters/HousingWJ_FlowResistances_TransLogging|HousingWJ_FlowResistances_TransLogging]] | i/p | boolean | N/A | Log housing water jacket flow resistances during thermal transient calculations |
| [[motorcad/parameter_database/parameters/HousingWJ_HeatTransferCoeff_TransLogging|HousingWJ_HeatTransferCoeff_TransLogging]] | i/p | boolean | N/A | Log housing water jacket heat transfer coefficient during thermal transient calculations |
| [[motorcad/parameter_database/parameters/HousingWJ_Pressures_TransLogging|HousingWJ_Pressures_TransLogging]] | i/p | boolean | N/A | Log housing water jacket pressures during thermal transient calculations |
| [[motorcad/parameter_database/parameters/HousingWJ_Velocity_TransLogging|HousingWJ_Velocity_TransLogging]] | i/p | boolean | N/A | Log housing water jacket velocity during thermal transient calculations |
| [[motorcad/parameter_database/parameters/HousingWJ_VolumeFlowRate_TransLogging|HousingWJ_VolumeFlowRate_TransLogging]] | i/p | boolean | N/A | Log housing water jacket volume flow rate during thermal transient calculations |
| [[motorcad/parameter_database/parameters/Losses_All_TransLogging|Losses_All_TransLogging]] | i/p | boolean | N/A | Log all losses during thermal transient calculations |
| [[motorcad/parameter_database/parameters/NatConv_HeatTransferCoeff_TransLogging|NatConv_HeatTransferCoeff_TransLogging]] | i/p | boolean | N/A | Log natural convection heat transfer coefficient during thermal transient calculations |
| [[motorcad/parameter_database/parameters/NodePowers_TransLogging|NodePowers_TransLogging]] | i/p | boolean | N/A | Log node powers during thermal transient calculations |
| [[motorcad/parameter_database/parameters/Running_FMU_Model|Running_FMU_Model]] | persistent | boolean | N/A | When true this parameter indicates to the thermal transient calculation that the FMU is running |
| [[motorcad/parameter_database/parameters/ShaftSpeed_TransLogging|ShaftSpeed_TransLogging]] | i/p | boolean | N/A | Log shaft speed during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_FlowResistances_TransLogging|TVent_FlowResistances_TransLogging]] | i/p | boolean | N/A | Log TVent flow resistances during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_FluidDissipCalc_TransLogging|TVent_FluidDissipCalc_TransLogging]] | i/p | boolean | N/A | Log TVent fluid dissipation (calculated) during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_FluidDissipSolvedCircuit_TransLogging|TVent_FluidDissipSolvedCircuit_TransLogging]] | i/p | boolean | N/A | Log TVent fluid dissipation (solved circuit) during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_FluidTemperatures_TransLogging|TVent_FluidTemperatures_TransLogging]] | i/p | boolean | N/A | Log TVent fluid temperatures during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_HeatTransferCoeffs_TransLogging|TVent_HeatTransferCoeffs_TransLogging]] | i/p | boolean | N/A | Log TVent heat transfer coefficients during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_Pressures_TransLogging|TVent_Pressures_TransLogging]] | i/p | boolean | N/A | Log TVent pressures during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_Velocity_TransLogging|TVent_Velocity_TransLogging]] | i/p | boolean | N/A | Log TVent velocity during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TVent_VolumeFlowRates_TransLogging|TVent_VolumeFlowRates_TransLogging]] | i/p | boolean | N/A | Log TVent volume flow rates during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TemperatureVariationWithinStep|TemperatureVariationWithinStep]] | i/p | integer | N/A | This controls how the temperatures are updated during the integration step |
| [[motorcad/parameter_database/parameters/Temperatures_All_TransLogging|Temperatures_All_TransLogging]] | i/p | boolean | N/A | Log all temperatures during thermal transient calculations |
| [[motorcad/parameter_database/parameters/TransientResultsAnalysisEnabled|TransientResultsAnalysisEnabled]] | i/p | boolean | N/A | When enabled the transient results are loaded from a file |
| [[motorcad/parameter_database/parameters/TransientResultsAnalysisFile|TransientResultsAnalysisFile]] | i/p | OleStr | N/A | This is the file where the transient results are loaded from |
| [[motorcad/parameter_database/parameters/TransientResultsAnalysisPeriod|TransientResultsAnalysisPeriod]] | i/p | integer | N/A | This is the period from the file file where the transient results are viewed |
| [[motorcad/parameter_database/parameters/TransientResultsView|TransientResultsView]] | i/p | integer | N/A | This controls which view is updated during the transient run. |
| [[motorcad/parameter_database/parameters/TransientTotalNumberPoints|TransientTotalNumberPoints]] | o/p | integer | N/A | This is the number of transient points calculated by transient solver. |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
