---
type: motorcad_parameter_report
report_name: coverage
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Motor-CAD Parameter Ingestion Coverage Report

## Summary Metrics
- **CSV Rows Processed**: 13,005
- **Unique Parameters Created**: 13,004
- **Duplicate Parameter Names**: 1
- **Parameters Missing Descriptions**: 581 (4.47%)
- **Parameters Missing Categories**: 0 (0.00%)
- **Parameters Without Units**: 5,314 (40.86%)

## Category Breakdown
| Category | Parameter Count |
|---|---|
| Magnetics | 1468 |
| EWdg_Spray_Cooling | 1419 |
| Through_Vent | 1124 |
| End_Space | 812 |
| Calc_Options | 695 |
| Water_Jacket_Data | 556 |
| Dimensions | 510 |
| TVent_Data | 418 |
| ThermalResults | 371 |
| Interface_Gaps | 273 |
| ModelParameters_MotorLAB | 236 |
| Water_Jacket_Slot | 206 |
| Wet_Rotor_Data | 178 |
| Rt | 155 |
| Mat_Weight_Notes | 135 |
| Surface_Area | 133 |
| Transient | 130 |
| Spiral_Groove_Shaft | 125 |
| Material | 123 |
| Weight_Multiplier | 121 |
| Weight_Addition | 121 |
| Mat_Cp | 119 |
| Mat_Density | 119 |
| Winding_Design | 118 |
| Mat_Conductivity | 118 |
| Weights | 109 |
| FEA_Settings | 107 |
| Winding | 106 |
| Ratios | 99 |
| lumped circuit node number data | 93 |
| Heat_Exchanger | 90 |
| SimulationParameters_MotorLAB | 87 |
| Natural_Convection | 87 |
| OperatingPointParameters_Lab | 84 |
| Weight_Total | 83 |
| Weight_Calc | 82 |
| Forced_Convection | 78 |
| Mechanical | 77 |
| NVH | 76 |
| h_Forced_Con_Input | 75 |
| Spray_Cooling_Data | 72 |
| Loss and Injected Power Values | 65 |
| h_Rad | 64 |
| Radiation_Notes | 62 |
| LossParameters_MotorLAB | 62 |
| Miscellaneous | 58 |
| Emissivity | 50 |
| Blown_Over | 48 |
| Material Specific Heat Capacity | 48 |
| View_Factor | 45 |
| CycleParameters_MotorLAB | 43 |
| ThermalParameters_MotorLAB | 42 |
| Radiation | 42 |
| h_Mixed_Conv | 42 |
| OutputSheets | 40 |
| Design_Options | 37 |
| Transient_Settings | 37 |
| User_Options | 36 |
| Thermal | 36 |
| Losses_At_RPM_Ref | 35 |
| Water_Jacket_Rotor | 30 |
| Airgap | 28 |
| SaturationMap | 28 |
| h_Nat_Con_Adjust | 28 |
| h_Nat_Con_Input | 28 |
| Nat_Con_Notes | 28 |
| h_Nat_Con_Output | 28 |
| h_Nat_Con_Model | 28 |
| Imported_DXF_Geometry | 27 |
| h_Nat_Conv | 26 |
| Loss_RPM_Ref | 25 |
| Loss_RPM_Coeff | 25 |
| GeneratorParameters_Lab | 25 |
| Speed_Program | 23 |
| Volumes | 23 |
| h_Forced_Con_Adjust | 23 |
| h_Forced_Con_Vel_Mult | 22 |
| Forced_Con_Notes | 22 |
| h_Forced_Con_Output | 22 |
| Units | 22 |
| Forced Convection Model Data | 20 |
| h_Forced_Conv | 20 |
| Airgap_Data | 19 |
| Rotor_Winding | 19 |
| Misc | 19 |
| Ansys | 18 |
| Geometry_Export | 16 |
| Custom_Outputs | 14 |
| Fluids | 13 |
| Cowling | 12 |
| Discovery | 12 |
| Fluid_Data | 12 |
| AdaptiveTemplates | 12 |
| FileParameters_MotorLAB | 11 |
| Transient_Graph | 11 |
| Shaft_Jacket_Data | 10 |
| Copper_Loss_Distribution | 10 |
| OptimisationParameters | 10 |
| Proximity_Loss | 9 |
| Spray Cooling Model Data | 9 |
| Periphery | 9 |
| Scripting_Options | 8 |
| Termination | 8 |
| Phasor_Diagram | 8 |
| BPM_Rating_Test | 8 |
| CalibrationParameters_MotorLAB | 7 |
| Reduced_Node_Model | 7 |
| Through Ventilation Model Data | 7 |
| Loss_Current_Values | 6 |
| Header | 6 |
| Region_Options | 6 |
| h_Table_Params | 6 |
| Fan_Char | 5 |
| Time_Constant | 5 |
| Loss_Distribution | 4 |
| lumped circuit data | 4 |
| Char_Length | 4 |
| Fan Characteristics Data | 3 |
| Scripting | 2 |
| Python_Scripting | 2 |
| Cuboidal_Model | 2 |
| EquivalentCircuit_Diagram | 2 |
| Copper_Loss_Vary | 2 |
| File_Notes | 1 |
| Node_Temp | 1 |
| Node_Power | 1 |
| Node_Cap | 1 |
| Calculation_Notes | 1 |
| Internal_Parameters | 1 |
| CoolingOptions_Notes | 1 |
| Losses_Notes | 1 |
| Transient_Notes | 1 |
| Transient Data | 1 |
| nodal delta temperature data | 1 |
| nodal temperature data | 1 |
| nodal power data | 1 |
| nodal thermal capacitance data | 1 |
| Thermal network thermal resistances (2-d network) | 1 |
| Power_Flow data | 1 |
| Vel_Forced_Conv | 1 |

## Data Type Breakdown
| Data Type | Parameter Count |
|---|---|
| double | 9859 |
| integer | 1676 |
| OleStr | 1062 |
| boolean | 384 |
| String | 15 |
| double 1d Array | 5 |
| string | 1 |
| double 2d Array, gives the resistance from Node1 to Node2 | 1 |
| double 2d Array, gives the Power Flow between Node1 and Node2 | 1 |
| double 2d Array | 1 |

## Ingestion Warnings & Notes
- Cleaned directory before build.
- Filenames and Wikilinks containing invalid filesystem characters or brackets (`/`, `\`, `:`, `*`, `?`, `"`, `<`, `>`, `|`, `,`, `[`, `]`) were sanitized safely using `_` for files and `(` / `)` for wikilink labels.
- Zero YAML frontmatter syntax errors encountered.
- Zero filename collisions were encountered during sanitization.
