---
type: motorcad_parameter_category
category_name: User_Options
parameter_count: 36
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: User_Options

## Overview
The **User_Options** category contains **36** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AFM_DrawAxes_Linear|AFM_DrawAxes_Linear]] | i/p | boolean | N/A | The option for drawing axes in the linear view |
| [[motorcad/parameter_database/parameters/AFM_RadialStatorView|AFM_RadialStatorView]] | i/p | integer | N/A | The stator view/slice drawn in AFM Radial Geometry |
| [[motorcad/parameter_database/parameters/AFM_SelectedComponent|AFM_SelectedComponent]] | i/p | integer | N/A | The selected Axial Flux component in the user interface |
| [[motorcad/parameter_database/parameters/AFM_StatorView_CustomPosition|AFM_StatorView_CustomPosition]] | i/p | integer | N/A | Custom plane position (%) for AFM Radial Stator view |
| [[motorcad/parameter_database/parameters/ActiveXCacheSize|ActiveXCacheSize]] | persistent | integer | N/A | The maximum size of the ActiveX cache, used to speed up getting/setting variables via ActiveX. |
| [[motorcad/parameter_database/parameters/AdaptiveScript_ExternalIDE_Enabled|AdaptiveScript_ExternalIDE_Enabled]] | setting | boolean | N/A | Whether to use external IDE or internal script editor |
| [[motorcad/parameter_database/parameters/AutomaticFileBackup|AutomaticFileBackup]] | i/p | boolean | N/A | When enabled a copy of the old file will be saved when the model is saved |
| [[motorcad/parameter_database/parameters/AutomationParameterTypeFilter|AutomationParameterTypeFilter]] | setting | integer | N/A | Filter for automation parameter types |
| [[motorcad/parameter_database/parameters/AxialCuboidTempDisplay|AxialCuboidTempDisplay]] | setting | integer | N/A | Display of the average or maximum winding temperatures in the axial temperatures view |
| [[motorcad/parameter_database/parameters/CoordinateSystem|CoordinateSystem]] | setting | integer | N/A | The coordinate system used in the geometry editor |
| [[motorcad/parameter_database/parameters/DrawVirtualBoundaries|DrawVirtualBoundaries]] | setting | boolean | N/A | When true, virtual boundaries will be drawn in the geometry editor (e.g. boundary between rotor back iron/embedded magnet pole) |
| [[motorcad/parameter_database/parameters/ForwardsCompatibilitySetting|ForwardsCompatibilitySetting]] | persistent | integer | N/A | When enabled, saved model files will be more compatible with older versions of Motor-CAD |
| [[motorcad/parameter_database/parameters/FreqDomain_MinAmplitude_ForceDensity|FreqDomain_MinAmplitude_ForceDensity]] | setting | double | N/m² | Sets the minimum harmonic amplitude to plot in 2D Frequency Domain graph for force density |
| [[motorcad/parameter_database/parameters/GeometryEditor_FocusedRegion|GeometryEditor_FocusedRegion]] | setting | integer | N/A | The region which is focused in the geometry editor |
| [[motorcad/parameter_database/parameters/GeometryEditor_SelectedRegions_EMag|GeometryEditor_SelectedRegions_EMag]] | setting | OleStr | N/A | The regions which are selected in the geometry editor in E-Magnetic context |
| [[motorcad/parameter_database/parameters/GeometryEditor_SelectedRegions_Mech|GeometryEditor_SelectedRegions_Mech]] | setting | OleStr | N/A | The regions which are selected in the geometry editor in the Mechanical context |
| [[motorcad/parameter_database/parameters/GeometryEditor_SelectedRegions_Thermal|GeometryEditor_SelectedRegions_Thermal]] | setting | OleStr | N/A | The regions which are selected in the geometry editor in the Thermal context |
| [[motorcad/parameter_database/parameters/GeometryEngine_SpatialSubRegions|GeometryEngine_SpatialSubRegions]] | compatibility | integer | N/A | Whether to include some geometry dependent regions as sub regions |
| [[motorcad/parameter_database/parameters/GeometryEngine_UniqueNaming|GeometryEngine_UniqueNaming]] | compatibility | integer | N/A | Whether geometry engine uses unique region naming in FEA |
| [[motorcad/parameter_database/parameters/HintDelayTime|HintDelayTime]] | setting | double | N/A | Length of time after hovering the mouse over a control for a hint to display [s] |
| [[motorcad/parameter_database/parameters/HintDisplayTime|HintDisplayTime]] | setting | double | N/A | Length of time for which hints are displayed [s] |
| [[motorcad/parameter_database/parameters/MachineFluxDirection|MachineFluxDirection]] | i/p | integer | N/A | The direction of the flux within the machine, radial/axial |
| [[motorcad/parameter_database/parameters/Maxwell_RotorPocket_Subtraction|Maxwell_RotorPocket_Subtraction]] | compatibility | integer | N/A | The magnet/rotor pocket subtraction type used for Maxwell |
| [[motorcad/parameter_database/parameters/PreviewFolderLocation|PreviewFolderLocation]] | i/p | OleStr | N/A | The location of the folder containing model preview images. |
| [[motorcad/parameter_database/parameters/Rotation3D_X|Rotation3D_X]] | setting | double | MDeg | Set rotation angle around the y axis of the 3D geometry view |
| [[motorcad/parameter_database/parameters/Rotation3D_Y|Rotation3D_Y]] | setting | double | MDeg | Set rotation angle around the x axis of the 3D geometry view |
| [[motorcad/parameter_database/parameters/SteadyStateResultsDecimalSeparator|SteadyStateResultsDecimalSeparator]] | i/p | OleStr | N/A | When this is not empty then this overrides the decimal separator used in the steady state results file |
| [[motorcad/parameter_database/parameters/SteadyStateResultsEnabled|SteadyStateResultsEnabled]] | i/p | boolean | N/A | The steady state results are stored in a file when this is enabled |
| [[motorcad/parameter_database/parameters/TVentFluidTempCheck|TVentFluidTempCheck]] | i/p | boolean | N/A | When enabled the transient will stop if the fluid temperature is less than the lower of ambient or inlet temperature |
| [[motorcad/parameter_database/parameters/TestDataFile|TestDataFile]] | i/p | OleStr | N/A | The test data file name |
| [[motorcad/parameter_database/parameters/ThermalCalcType|ThermalCalcType]] | i/p | integer | N/A | The thermal calculation type to be run |
| [[motorcad/parameter_database/parameters/ThermalModelSize|ThermalModelSize]] | i/p | integer | N/A | The size of the thermal model. |
| [[motorcad/parameter_database/parameters/ThermalModelType|ThermalModelType]] | i/p | integer | N/A | When 2D model is enabled then Motor-CAD model is Pseudo 2D for comparison with 2D FEA |
| [[motorcad/parameter_database/parameters/TransientResultsDecimalSeparator|TransientResultsDecimalSeparator]] | i/p | OleStr | N/A | When this is not empty then this overrides the the decimal separator used in the transient results file |
| [[motorcad/parameter_database/parameters/TransientResultsEnabled|TransientResultsEnabled]] | i/p | boolean | N/A | The transient results are stored in a file when this is enabled |
| [[motorcad/parameter_database/parameters/WeightCalculationMethod|WeightCalculationMethod]] | compatibility | integer | N/A | Method used to calculate machine part weights. Original method using standard geometry, improved method uses adaptive geometry. |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
