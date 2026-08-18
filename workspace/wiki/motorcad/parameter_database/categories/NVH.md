---
type: motorcad_parameter_category
category_name: NVH
parameter_count: 76
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: NVH

## Overview
The **NVH** category contains **76** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AreaMomentInertia_Yoke|AreaMomentInertia_Yoke]] | o/p | double | mm⁴ | The yoke area moment of inertia used in NVH calculations |
| [[motorcad/parameter_database/parameters/CalculateNVHModels|CalculateNVHModels]] | setting | integer | N/A | Whether to calculate NVH models after transient force calculations. |
| [[motorcad/parameter_database/parameters/EndBellsCorrectionFactor|EndBellsCorrectionFactor]] | o/p | double | N/A | The end bells correction factor used in NVH calculations |
| [[motorcad/parameter_database/parameters/ForceAnalysisElecCycles_Definition|ForceAnalysisElecCycles_Definition]] | setting | integer | N/A | Set the method of defining the minimum and maximum temporal cycles used within force harmonic analysis |
| [[motorcad/parameter_database/parameters/ForceAnalysisElecCycles_Max_OC|ForceAnalysisElecCycles_Max_OC]] | setting | integer | N/A | The maximum time step used within open circuit harmonic force analysis |
| [[motorcad/parameter_database/parameters/ForceAnalysisElecCycles_Max_OL|ForceAnalysisElecCycles_Max_OL]] | setting | integer | N/A | The maximum time step used within on load harmonic force analysis |
| [[motorcad/parameter_database/parameters/ForceAnalysisElecCycles_Min_OC|ForceAnalysisElecCycles_Min_OC]] | setting | integer | N/A | The minimum time step used within open circuit harmonic force analysis |
| [[motorcad/parameter_database/parameters/ForceAnalysisElecCycles_Min_OL|ForceAnalysisElecCycles_Min_OL]] | setting | integer | N/A | The minimum time step used within on load harmonic force analysis |
| [[motorcad/parameter_database/parameters/ForceFFTScalingMethod|ForceFFTScalingMethod]] | compatibility | integer | N/A | Improved method does not double the magnitude of the 1d FFT component at the Nyquist frequency |
| [[motorcad/parameter_database/parameters/MassCorrectionFactor_Rotational|MassCorrectionFactor_Rotational]] | o/p | double | N/A | The rotational mass correction factor used for modal analysis |
| [[motorcad/parameter_database/parameters/MassCorrectionFactor_Translational|MassCorrectionFactor_Translational]] | o/p | double | N/A | The translational mass correction factor used for modal analysis |
| [[motorcad/parameter_database/parameters/Mass_YokeBackIron|Mass_YokeBackIron]] | o/p | double | kg | The mass of the yoke back iron used in NVH calculations |
| [[motorcad/parameter_database/parameters/MaxOrderSound_Frequency|MaxOrderSound_Frequency]] | o/p | double | Hz | The sound frequency at which the single order sound power is at a maximum |
| [[motorcad/parameter_database/parameters/MaxOrderSound_PowerLevel|MaxOrderSound_PowerLevel]] | o/p | double | N/A | The maximum sound power level for any space and time order |
| [[motorcad/parameter_database/parameters/MaxOrderSound_SpaceOrder|MaxOrderSound_SpaceOrder]] | o/p | double | N/A | The space order at which the single order sound power is at a maximum |
| [[motorcad/parameter_database/parameters/MaxOrderSound_Speed|MaxOrderSound_Speed]] | o/p | double | rpm | The speed at which the single order sound power is at a maximum |
| [[motorcad/parameter_database/parameters/MaxOrderSound_TimeOrder|MaxOrderSound_TimeOrder]] | o/p | double | N/A | The time order  at which the single order sound power is at a maximum |
| [[motorcad/parameter_database/parameters/MaxTotalSound_PowerLevel|MaxTotalSound_PowerLevel]] | o/p | double | N/A | The maximum total sound power level for all space and time orders combined |
| [[motorcad/parameter_database/parameters/MaxTotalSound_Speed|MaxTotalSound_Speed]] | o/p | double | rpm | The speed at which the total sound power is at a maximum |
| [[motorcad/parameter_database/parameters/ModalOverride_Damping|ModalOverride_Damping]] | i/p | double | N/A | Override the default mode shape damping ratio |
| [[motorcad/parameter_database/parameters/ModalOverride_Mode|ModalOverride_Mode]] | i/p | integer | N/A | Which mode to override the automatically calculated modal parameters for |
| [[motorcad/parameter_database/parameters/ModalOverride_NaturalFrequency|ModalOverride_NaturalFrequency]] | i/p | double | Hz | Override the automatically calculated mode shape natural frequency |
| [[motorcad/parameter_database/parameters/ModalOverride_Stiffness|ModalOverride_Stiffness]] | i/p | double | N/m | Override the automatically calculated mode shape stiffness |
| [[motorcad/parameter_database/parameters/NVHAcousticModel|NVHAcousticModel]] | setting | integer | N/A | What acoustic model to use |
| [[motorcad/parameter_database/parameters/NVHAcousticWeighting|NVHAcousticWeighting]] | setting | integer | N/A | What acoustic weighting to apply |
| [[motorcad/parameter_database/parameters/NVHAirDensity|NVHAirDensity]] | i/p | double | kg/m³ | The density of air at a given altitude and temperature |
| [[motorcad/parameter_database/parameters/NVHCampbellSelection|NVHCampbellSelection]] | setting | integer | N/A | NVH Campbell diagram selected in user interface |
| [[motorcad/parameter_database/parameters/NVHDampingFactor|NVHDampingFactor]] | i/p | double | N/A | The damping factor used for NVH structural analysis |
| [[motorcad/parameter_database/parameters/NVHExportFile|NVHExportFile]] | setting | OleStr | N/A | The file name used for NVH results export to file. |
| [[motorcad/parameter_database/parameters/NVHExport_Acceleration|NVHExport_Acceleration]] | setting | boolean | N/A | Whether to export acceleration NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_AnsysSound|NVHExport_AnsysSound]] | setting | boolean | N/A | Whether to export NVH results orders to an Ansys Sound file. |
| [[motorcad/parameter_database/parameters/NVHExport_Displacement_Dynamic|NVHExport_Displacement_Dynamic]] | setting | boolean | N/A | Whether to export dynamic displacement NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_Displacement_Static|NVHExport_Displacement_Static]] | setting | boolean | N/A | Whether to export static displacement NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_MagFactor|NVHExport_MagFactor]] | setting | boolean | N/A | Whether to export magnification factor NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_RadiatedPower_M|NVHExport_RadiatedPower_M]] | setting | boolean | N/A | Whether to export radiated power (space tracked) NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_RadiatedPower_MN|NVHExport_RadiatedPower_MN]] | setting | boolean | N/A | Whether to export radiated power (frequency and space tracked) NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_RadiatedPower_N|NVHExport_RadiatedPower_N]] | setting | boolean | N/A | Whether to export radiated power (frequency tracked) NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_Velocity|NVHExport_Velocity]] | setting | boolean | N/A | Whether to export velocity NVH results to file. |
| [[motorcad/parameter_database/parameters/NVHExport_Wav|NVHExport_Wav]] | setting | boolean | N/A | Whether to export NVH results orders to wave sound file |
| [[motorcad/parameter_database/parameters/NVHExport_Wav_WithRPM|NVHExport_Wav_WithRPM]] | setting | boolean | N/A | Whether RPM information should be included as a second channel in the wave sound file |
| [[motorcad/parameter_database/parameters/NVHForceCombination|NVHForceCombination]] | compatibility | integer | N/A | Improved method includes tangential forces when calculating analytical response for bending modes |
| [[motorcad/parameter_database/parameters/NVHFreqAxisType|NVHFreqAxisType]] | setting | integer | N/A | NVH Frequency axis type, Plot vs Frequency or Frequency Orders |
| [[motorcad/parameter_database/parameters/NVHInterpolationMethod|NVHInterpolationMethod]] | compatibility | integer | N/A | Improved method performs interpolation on imaginary and real components of force |
| [[motorcad/parameter_database/parameters/NVHMagnitudeScaleType|NVHMagnitudeScaleType]] | setting | integer | N/A | Set the magnitude type used for NVH structural and acoustic plots |
| [[motorcad/parameter_database/parameters/NVHMaxFrequencyOrder_OL|NVHMaxFrequencyOrder_OL]] | setting | integer | N/A | The maximum frequency order used in NVH Modal, Structural, Acoustic on load calculations |
| [[motorcad/parameter_database/parameters/NVHMaxSpaceOrder_OL|NVHMaxSpaceOrder_OL]] | setting | integer | N/A | The maximum space order used in NVH Modal, Structural, Acoustic on load calculations |
| [[motorcad/parameter_database/parameters/NVHMaximumOrderDefinition|NVHMaximumOrderDefinition]] | setting | integer | N/A | Set the method to determine the maximum harmonic order used in NVH analysis |
| [[motorcad/parameter_database/parameters/NVHMaximumSoundFrequency|NVHMaximumSoundFrequency]] | setting | double | Hz | The maximum sound frequency for acoustic variable speed charts in the user interface |
| [[motorcad/parameter_database/parameters/NVHMechanicalOrderMethodIM|NVHMechanicalOrderMethodIM]] | compatibility | integer | N/A | Improved method calculates true mechanical order, considering induction motor slip |
| [[motorcad/parameter_database/parameters/NVHModal_IncludeHousing|NVHModal_IncludeHousing]] | setting | boolean | N/A | When enabled the housing mass and stiffness is included in the modal calculation |
| [[motorcad/parameter_database/parameters/NVHModal_IncludeWindingMass|NVHModal_IncludeWindingMass]] | setting | boolean | N/A | When enabled the winding mass is included in the NVH stator modal calculation |
| [[motorcad/parameter_database/parameters/NVHNumColourInterpolationSegments|NVHNumColourInterpolationSegments]] | setting | integer | N/A | The number of colour interpolation segments between each calculated value from NVH models |
| [[motorcad/parameter_database/parameters/NVHNumInterpolationPoints|NVHNumInterpolationPoints]] | setting | integer | N/A | The number of Interpolation Points for varyiable speed  analysis on structural/ acoustic analysis |
| [[motorcad/parameter_database/parameters/NVHOrderTrackingHarmonics_Freq|NVHOrderTrackingHarmonics_Freq]] | setting | integer | N/A | The number or harmonics shown for frequency order tracking |
| [[motorcad/parameter_database/parameters/NVHOrderTrackingHarmonics_Space|NVHOrderTrackingHarmonics_Space]] | setting | integer | N/A | The number or harmonics shown for space order tracking |
| [[motorcad/parameter_database/parameters/NVHOrderTrackingHarmonics_Space_Freq|NVHOrderTrackingHarmonics_Space_Freq]] | setting | integer | N/A | The number or harmonics shown for frequency and space order tracking |
| [[motorcad/parameter_database/parameters/NVHOrderTrackingSelection|NVHOrderTrackingSelection]] | setting | integer | N/A | NVH order tracking selection in user interface |
| [[motorcad/parameter_database/parameters/NVHOrderTracking_XAxis|NVHOrderTracking_XAxis]] | setting | integer | N/A | NVH Order tracking X axis type |
| [[motorcad/parameter_database/parameters/NVHReplayNormalise94dBSPL|NVHReplayNormalise94dBSPL]] | setting | boolean | N/A | If the replay should normalise and clip results to 94 dB SPL (1 Pa RMS) |
| [[motorcad/parameter_database/parameters/NVHSkewModel|NVHSkewModel]] | compatibility | integer | N/A | Improved method calculates the average forces from all slices for structural analysis |
| [[motorcad/parameter_database/parameters/NVHSoundPressureDirectivityFactor|NVHSoundPressureDirectivityFactor]] | i/p | double | N/A | Proportion of a full sphere the sound is radiating into, e.g. 1 for free space, 2 for sound source over a reflecting plane |
| [[motorcad/parameter_database/parameters/NVHSoundPressureDistance|NVHSoundPressureDistance]] | i/p | double | mm | Distance at which Sound Pressure Level (SPL) will be calculated |
| [[motorcad/parameter_database/parameters/NVHSpatiogramSelection|NVHSpatiogramSelection]] | setting | integer | N/A | NVH Spatiogram diagram selected in user interface |
| [[motorcad/parameter_database/parameters/NVHStructural_Slice|NVHStructural_Slice]] | setting | integer | N/A | The slice number used within NVH analysis graphs |
| [[motorcad/parameter_database/parameters/NVHTimeOrderType|NVHTimeOrderType]] | setting | integer | N/A | Sets if the time order is based on one mechanical or electrical cycle |
| [[motorcad/parameter_database/parameters/NonDimensionalThickness|NonDimensionalThickness]] | o/p | double | kg | The non dimensional thickness used in NVH calculations |
| [[motorcad/parameter_database/parameters/Num_ModalOverride|Num_ModalOverride]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/RadiationEfficiency|RadiationEfficiency]] | i/p | double | N/A | The radiation efficiency |
| [[motorcad/parameter_database/parameters/ShowDXFImportProcessingSettings|ShowDXFImportProcessingSettings]] | setting | boolean | N/A | Show the DXF Import division and geometry tabs for processing DXF Imports |
| [[motorcad/parameter_database/parameters/SpeedOfSound|SpeedOfSound]] | i/p | double | m/s | The speed of sound at a given altitude and temperature |
| [[motorcad/parameter_database/parameters/VibratoryRef_Acceleration|VibratoryRef_Acceleration]] | i/p | double | m/s² | The Reference vibratory acceleration level for NVH analysis |
| [[motorcad/parameter_database/parameters/VibratoryRef_Displacement|VibratoryRef_Displacement]] | i/p | double | mm | The Reference vibratory displacement level for NVH analysis |
| [[motorcad/parameter_database/parameters/VibratoryRef_Force|VibratoryRef_Force]] | i/p | double | N | The Reference vibratory force level for NVH analysis |
| [[motorcad/parameter_database/parameters/VibratoryRef_ForceDensity|VibratoryRef_ForceDensity]] | i/p | double | N/m² | The Reference vibratory force density level for NVH analysis |
| [[motorcad/parameter_database/parameters/VibratoryRef_SoundPower|VibratoryRef_SoundPower]] | i/p | double | Watts | The Reference vibratory sound power level for NVH analysis |
| [[motorcad/parameter_database/parameters/VibratoryRef_Velocity|VibratoryRef_Velocity]] | i/p | double | rpm | The Reference vibratory velocity level for NVH analysis |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
