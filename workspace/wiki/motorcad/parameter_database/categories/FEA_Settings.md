---
type: motorcad_parameter_category
category_name: FEA_Settings
parameter_count: 107
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: FEA_Settings

## Overview
The **FEA_Settings** category contains **107** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/AdhesionFactor_DamperBars|AdhesionFactor_DamperBars]] | i/p | double | N/A | Adhesion factor used for the damper bars to lamination in mechanical analysis |
| [[motorcad/parameter_database/parameters/AdhesionFactor_Magnets|AdhesionFactor_Magnets]] | i/p | double | N/A | Adhesion factor used for the magnets to lamination in mechanical analysis |
| [[motorcad/parameter_database/parameters/AirgapLayersMethod|AirgapLayersMethod]] | recommended | integer | N/A | Method of specifying the number of airgap layers to be solved by the FEA |
| [[motorcad/parameter_database/parameters/AirgapMeshPoints_layers|AirgapMeshPoints_layers]] | i/p | double | N/A | This specifies the number of mesh points in the airgap and can be increased or reduced as required. Default = 360 |
| [[motorcad/parameter_database/parameters/AirgapMeshPoints_mesh|AirgapMeshPoints_mesh]] | i/p | double | N/A | This specifies the number of mesh points at the airgap surfaces and can be increased or reduced as required. Default = 360 |
| [[motorcad/parameter_database/parameters/AirgapMesh_NumLayers|AirgapMesh_NumLayers]] | i/p | integer | N/A | Number of airgap layers specified by the user |
| [[motorcad/parameter_database/parameters/AirgapMesh_NumLayers_Used|AirgapMesh_NumLayers_Used]] | o/p | integer | N/A | Number of layers the airgap is split into when meshing the machine |
| [[motorcad/parameter_database/parameters/BandingMeshLength|BandingMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the rotor banding. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/CustomFEARegions_Magnetic|CustomFEARegions_Magnetic]] | i/p | OleStr | N/A | String that holds the custom Magnetic FEA regions |
| [[motorcad/parameter_database/parameters/CustomFEARegions_Mechanical|CustomFEARegions_Mechanical]] | i/p | OleStr | N/A | String that holds the custom mechanical FEA regions |
| [[motorcad/parameter_database/parameters/CustomFEARegions_ThermalDXF|CustomFEARegions_ThermalDXF]] | i/p | OleStr | N/A | String that holds the custom thermal slot and pole FEA regions |
| [[motorcad/parameter_database/parameters/CustomFEARegions_ThermalPole|CustomFEARegions_ThermalPole]] | i/p | OleStr | N/A | String that holds the custom thermal pole FEA regions |
| [[motorcad/parameter_database/parameters/CustomFEARegions_ThermalSlot|CustomFEARegions_ThermalSlot]] | i/p | OleStr | N/A | String that holds the custom thermal slot FEA regions |
| [[motorcad/parameter_database/parameters/CustomLoadPointOutput|CustomLoadPointOutput]] | o/p | OleStr | N/A | String that holds the output of the custom load point calculations |
| [[motorcad/parameter_database/parameters/CustomLoadPointSettings|CustomLoadPointSettings]] | i/p | OleStr | N/A | String that holds the custom Load point values to run |
| [[motorcad/parameter_database/parameters/CustomRegionMagNames_Method|CustomRegionMagNames_Method]] | compatibility | integer | N/A | Method for getting names of magnets in the FEA when using custom regions |
| [[motorcad/parameter_database/parameters/DXFImportType|DXFImportType]] | setting | integer | N/A | The type of DXF import: 0 = Single Slot Pole, 1 = Single Rotor Pole, 2 = Single Stator Slot  +3 = Entire Machine, 4 = Entire Rotor, 5 = Entire Stator |
| [[motorcad/parameter_database/parameters/EnableMechanicalMesh_DamperBars|EnableMechanicalMesh_DamperBars]] | i/p | integer | N/A | Usage option for damper bars in mechanical analysis |
| [[motorcad/parameter_database/parameters/EnableMechanicalMesh_FieldWdg|EnableMechanicalMesh_FieldWdg]] | i/p | integer | N/A | Usage option for field winding in mechanical analysis |
| [[motorcad/parameter_database/parameters/EnableMechanicalMesh_RotorBars|EnableMechanicalMesh_RotorBars]] | i/p | integer | N/A | Usage option for rotor bars in mechanical analysis |
| [[motorcad/parameter_database/parameters/FEAAreaSelect|FEAAreaSelect]] | i/p | integer | N/A | This selects the area for FEA analysis |
| [[motorcad/parameter_database/parameters/FEAAutoShading_Magnetic|FEAAutoShading_Magnetic]] | setting | boolean | N/A | When enabled the shading scale is set automatically |
| [[motorcad/parameter_database/parameters/FEAAutoShading_Mechanical|FEAAutoShading_Mechanical]] | setting | boolean | N/A | When enabled the shading scale is set automatically |
| [[motorcad/parameter_database/parameters/FEAAutoShading_Thermal|FEAAutoShading_Thermal]] | setting | boolean | N/A | When enabled the shading scale is set automatically |
| [[motorcad/parameter_database/parameters/FEAAvMagnetTemp|FEAAvMagnetTemp]] | o/p | double | °C | This is the average magnet temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEAAvRotorBarTemp|FEAAvRotorBarTemp]] | o/p | double | °C | This is the average rotor bar temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEAAvWindingTemp|FEAAvWindingTemp]] | o/p | double | °C | This is the average slot winding temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEABndFactor|FEABndFactor]] | i/p | double | N/A | FEA Boundary Factor |
| [[motorcad/parameter_database/parameters/FEAEddyCurrentCalcMethod|FEAEddyCurrentCalcMethod]] | compatibility | integer | N/A | Specifies the calculation method for eddy currents in FEA solver |
| [[motorcad/parameter_database/parameters/FEAHighlightMax_Magnetic|FEAHighlightMax_Magnetic]] | setting | boolean | N/A | When enabled values above range maximum are not shaded |
| [[motorcad/parameter_database/parameters/FEAHighlightMax_Mechanical|FEAHighlightMax_Mechanical]] | setting | boolean | N/A | When enabled values above range maximum are not shaded |
| [[motorcad/parameter_database/parameters/FEAHighlightMax_Thermal|FEAHighlightMax_Thermal]] | setting | boolean | N/A | When enabled values above range maximum are not shaded |
| [[motorcad/parameter_database/parameters/FEAHighlightMin_Magnetic|FEAHighlightMin_Magnetic]] | setting | boolean | N/A | When enabled values below range minimum are not shaded |
| [[motorcad/parameter_database/parameters/FEAHighlightMin_Mechanical|FEAHighlightMin_Mechanical]] | setting | boolean | N/A | When enabled values below range minimum are not shaded |
| [[motorcad/parameter_database/parameters/FEAHighlightMin_Thermal|FEAHighlightMin_Thermal]] | setting | boolean | N/A | When enabled values below range minimum are not shaded |
| [[motorcad/parameter_database/parameters/FEALengthVectors_EMag|FEALengthVectors_EMag]] | setting | integer | N/A | The number of vectors shown for FEA analysis |
| [[motorcad/parameter_database/parameters/FEALengthVectors_Mechanical|FEALengthVectors_Mechanical]] | setting | integer | N/A | The number of vectors shown for FEA analysis |
| [[motorcad/parameter_database/parameters/FEALengthVectors_Therm|FEALengthVectors_Therm]] | setting | integer | N/A | The length of vectors shown for FEA analysis |
| [[motorcad/parameter_database/parameters/FEAMaxAngle|FEAMaxAngle]] | i/p | double | N/A | Maximum angle in FEA mesh triangles |
| [[motorcad/parameter_database/parameters/FEAMaxMagnetTemp|FEAMaxMagnetTemp]] | o/p | double | °C | This is the maximum magnet temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEAMaxRotorBarTemp|FEAMaxRotorBarTemp]] | o/p | double | °C | This is the maximum rotor bar temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEAMaxValue_Magnetic|FEAMaxValue_Magnetic]] | setting | double | N/A | This is the setting for the max value for scale |
| [[motorcad/parameter_database/parameters/FEAMaxValue_Mechanical|FEAMaxValue_Mechanical]] | setting | double | N/A | This is the setting for the max value for shading scale |
| [[motorcad/parameter_database/parameters/FEAMaxValue_Thermal|FEAMaxValue_Thermal]] | setting | double | °C | This is the maximum value for scaling the thermal FEA plot |
| [[motorcad/parameter_database/parameters/FEAMaxWindingTemp|FEAMaxWindingTemp]] | o/p | double | °C | This is the maximum slot winding temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEAMinMagnetTemp|FEAMinMagnetTemp]] | o/p | double | °C | This is the minimum magnet temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEAMinPointSeparation|FEAMinPointSeparation]] | i/p | double | mm | Specifies the minimum distance for FEA geometry point separation |
| [[motorcad/parameter_database/parameters/FEAMinRotorBarTemp|FEAMinRotorBarTemp]] | o/p | double | °C | This is the minimum rotor bar temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEAMinValue_Magnetic|FEAMinValue_Magnetic]] | setting | double | N/A | This is the setting for the min value for scale |
| [[motorcad/parameter_database/parameters/FEAMinValue_Mechanical|FEAMinValue_Mechanical]] | setting | double | N/A | This is the setting for the min value for shading scale |
| [[motorcad/parameter_database/parameters/FEAMinValue_Thermal|FEAMinValue_Thermal]] | setting | double | °C | This is the minimum value for scaling the thermal FEA plot |
| [[motorcad/parameter_database/parameters/FEAMinWindingTemp|FEAMinWindingTemp]] | o/p | double | °C | This is the minimum slot winding temperature calculated by FEA |
| [[motorcad/parameter_database/parameters/FEANumEquipotentialLines_EMag|FEANumEquipotentialLines_EMag]] | setting | integer | N/A | The number of equipotential lines shown for FEA analysis |
| [[motorcad/parameter_database/parameters/FEANumEquipotentialLines_Mechanical|FEANumEquipotentialLines_Mechanical]] | setting | integer | N/A | The number of equipotential lines shown for FEA analysis |
| [[motorcad/parameter_database/parameters/FEANumEquipotentialLines_Therm|FEANumEquipotentialLines_Therm]] | setting | integer | N/A | The number of equipotential lines shown for FEA analysis |
| [[motorcad/parameter_database/parameters/FEAScalingFactor|FEAScalingFactor]] | setting | double | N/A | Scaling factor for FEA elements |
| [[motorcad/parameter_database/parameters/FEASchematicNodeRadius|FEASchematicNodeRadius]] | i/p | double | mm | The standard radius of the Schematic Temperature Nodes used in Radial and Axial FEA |
| [[motorcad/parameter_database/parameters/FEASmallAngleMethod|FEASmallAngleMethod]] | compatibility | integer | N/A | Method used by FEA for meshing when lines join to arcs |
| [[motorcad/parameter_database/parameters/FEASmallAngleSize|FEASmallAngleSize]] | compatibility | double | N/A | FEA small angle size in degrees |
| [[motorcad/parameter_database/parameters/FEASolutionCycle|FEASolutionCycle]] | i/p | integer | N/A | Reduced or full solution cycle. |
| [[motorcad/parameter_database/parameters/FEA_MeshElements|FEA_MeshElements]] | o/p | integer | N/A | Number of mesh elements |
| [[motorcad/parameter_database/parameters/FEA_MeshNodes|FEA_MeshNodes]] | o/p | integer | N/A | Number of mesh nodes |
| [[motorcad/parameter_database/parameters/FE_Location|FE_Location]] | persistent | OleStr | N/A | Finite Element dll location |
| [[motorcad/parameter_database/parameters/FE_Version|FE_Version]] | persistent | OleStr | N/A | Finite Element dll version |
| [[motorcad/parameter_database/parameters/FeaSys_Suffix|FeaSys_Suffix]] | i/p | OleStr | N/A | Suffix for the feasys folder in the Motor-CAD Data folder: Useful for preventing access conflicts when running simultaneous copies of Motor-CAD with FEA |
| [[motorcad/parameter_database/parameters/FieldWdgAdhesionFactor|FieldWdgAdhesionFactor]] | i/p | double | N/A | Adhesion factor used for the field winding to lamination in mechanical analysis |
| [[motorcad/parameter_database/parameters/GeometryTestMode|GeometryTestMode]] | setting | integer | N/A | Select the testing mode of FEA geometry |
| [[motorcad/parameter_database/parameters/HasNonStandardRegions_EMag|HasNonStandardRegions_EMag]] | o/p | boolean | N/A | Whether model has different regions to the standard template geometry |
| [[motorcad/parameter_database/parameters/MagnetMeshLength|MagnetMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the magnets. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/MagneticPropertyFEAMethod|MagneticPropertyFEAMethod]] | compatibility | integer | N/A | When set to improved this sends magnetic properties to the FEA directly from the geometry structure |
| [[motorcad/parameter_database/parameters/MaxBndLength|MaxBndLength]] | o/p | double | mm | Maximum length of all FEA elements |
| [[motorcad/parameter_database/parameters/MechanicalInnerBoundaryStress|MechanicalInnerBoundaryStress]] | i/p | double | MPa | Specified stress imposed on inner surface of rotor |
| [[motorcad/parameter_database/parameters/MechanicalMeshLength_DamperBars|MechanicalMeshLength_DamperBars]] | i/p | double | mm | This specifies the size of mesh elements around the damper bars. Default = 0.1, 0 = automatic |
| [[motorcad/parameter_database/parameters/MechanicalMeshLength_Magnets|MechanicalMeshLength_Magnets]] | i/p | double | mm | This specifies the size of mesh elements in the magnets. Default = 1, 0 = automatic |
| [[motorcad/parameter_database/parameters/MechanicalMeshLength_RotorBars|MechanicalMeshLength_RotorBars]] | i/p | double | mm | This specifies the size of mesh elements in the rotor bars. Default = 1, 0 = automatic |
| [[motorcad/parameter_database/parameters/MechanicalMeshLength_RotorLam|MechanicalMeshLength_RotorLam]] | i/p | double | mm | This specifies the size of mesh elements in the rotor lamination. Default = 1, 0 = automatic |
| [[motorcad/parameter_database/parameters/MechanicalMeshLength_RotorVoids|MechanicalMeshLength_RotorVoids]] | i/p | double | mm | This specifies the size of mesh elements around the rotor voids. Default = 0.1, 0 = automatic |
| [[motorcad/parameter_database/parameters/MechanicalOption_InnerBoundaryCondition|MechanicalOption_InnerBoundaryCondition]] | i/p | integer | N/A | User option for setting boundary condition on inner surface of rotor in mechanical analysis |
| [[motorcad/parameter_database/parameters/MechanicalOption_Magnets|MechanicalOption_Magnets]] | i/p | integer | N/A | Usage option for magnets/rotor pockets in mechanical analysis |
| [[motorcad/parameter_database/parameters/MechanicalOption_OuterBoundaryCondition|MechanicalOption_OuterBoundaryCondition]] | i/p | integer | N/A | User option for setting boundary condition on outer surface of rotor in mechanical analysis |
| [[motorcad/parameter_database/parameters/MechanicalOuterBoundaryStress|MechanicalOuterBoundaryStress]] | i/p | double | MPa | Specified stress imposed on outer surface of rotor |
| [[motorcad/parameter_database/parameters/RecordFEALog|RecordFEALog]] | persistent | boolean | N/A | Record the FEA procedures called by MCAD |
| [[motorcad/parameter_database/parameters/RotorBarAdhesionFactor|RotorBarAdhesionFactor]] | i/p | double | N/A | Adhesion factor used for the rotor bar to lamination in mechanical analysis |
| [[motorcad/parameter_database/parameters/RotorBarMeshLength|RotorBarMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the rotor bars. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/RotorLamMeshLength|RotorLamMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the rotor lamination. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/RotorPocketMeshLength|RotorPocketMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the rotor pockets. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/ShaftMeshLength|ShaftMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the shaft. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/ShowModelAirgap|ShowModelAirgap]] | setting | boolean | N/A | Show the Motor-CAD model airgap |
| [[motorcad/parameter_database/parameters/SleeveMeshLength|SleeveMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the stator sleeve. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/StatorLamMeshLength|StatorLamMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the stator lamination. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/StatorSlotMeshLength|StatorSlotMeshLength]] | i/p | double | mm | This specifies the size of mesh elements in the stator slot. Default = 0 = automatic |
| [[motorcad/parameter_database/parameters/UseCustomFEARegions_Magnetic|UseCustomFEARegions_Magnetic]] | setting | boolean | N/A | Use the custom magnetic regions |
| [[motorcad/parameter_database/parameters/UseCustomFEARegions_Mechanical|UseCustomFEARegions_Mechanical]] | setting | boolean | N/A | Use the custom mechanical regions |
| [[motorcad/parameter_database/parameters/UseCustomFEARegions_ThermalPole|UseCustomFEARegions_ThermalPole]] | setting | boolean | N/A | Use the custom thermal pole regions |
| [[motorcad/parameter_database/parameters/UseCustomFEARegions_ThermalSlot|UseCustomFEARegions_ThermalSlot]] | setting | boolean | N/A | Use the custom thermal slot regions |
| [[motorcad/parameter_database/parameters/UseDXFImportForFEA_Magnetic|UseDXFImportForFEA_Magnetic]] | setting | boolean | N/A | Use imported DXF geometry for E-Magnetics FEA. |
| [[motorcad/parameter_database/parameters/UseDXFImportForFEA_Mechanical|UseDXFImportForFEA_Mechanical]] | setting | boolean | N/A | Use imported DXF geometry for Mechanical FEA. |
| [[motorcad/parameter_database/parameters/UseDXFImportForFEA_Thermal|UseDXFImportForFEA_Thermal]] | setting | boolean | N/A | Use imported DXF geometry for Thermal FEA. |
| [[motorcad/parameter_database/parameters/VerboseFEAOutput|VerboseFEAOutput]] | setting | boolean | N/A | When enabled additional FEA outputs are displayed |
| [[motorcad/parameter_database/parameters/VerboseFlag_Error|VerboseFlag_Error]] | setting | boolean | N/A | When enabled FEA solver errors are displayed in message window |
| [[motorcad/parameter_database/parameters/VerboseFlag_IOInfo|VerboseFlag_IOInfo]] | setting | boolean | N/A | When enabled FEA solver file info is displayed in message window |
| [[motorcad/parameter_database/parameters/VerboseFlag_Info|VerboseFlag_Info]] | setting | boolean | N/A | When enabled FEA solver info is displayed in message window |
| [[motorcad/parameter_database/parameters/VerboseFlag_Results|VerboseFlag_Results]] | setting | boolean | N/A | When enabled FEA solver result info is displayed in message window |
| [[motorcad/parameter_database/parameters/VerboseFlag_ScriptInfo|VerboseFlag_ScriptInfo]] | setting | boolean | N/A | When enabled FEA solver script info is displayed in message window |
| [[motorcad/parameter_database/parameters/VerboseFlag_TimedInfo|VerboseFlag_TimedInfo]] | setting | boolean | N/A | When enabled FEA solver timed info is displayed with VerboseFEAOutput |
| [[motorcad/parameter_database/parameters/VerboseFlag_Warning|VerboseFlag_Warning]] | setting | boolean | N/A | When enabled FEA solver warnings are displayed in message window |
| [[motorcad/parameter_database/parameters/VerboseMessageOutput|VerboseMessageOutput]] | setting | boolean | N/A | When enabled additional progress messages are displayed |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
