---
type: motorcad_parameter_category
category_name: Magnetics
parameter_count: 1468
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Magnetics

## Overview
The **Magnetics** category contains **1468** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/ACConductorLossProportion|ACConductorLossProportion]] | o/p | double | N/A | The proportion of total conductors in slot in this cuboid |
| [[motorcad/parameter_database/parameters/ACConductorLossUserRatio|ACConductorLossUserRatio]] | i/p | double | N/A | The proportion of AC conductor loss in this cuboid |
| [[motorcad/parameter_database/parameters/ACLoadAdjustmentPhase2|ACLoadAdjustmentPhase2]] | i/p | double | N/A | The adjustment factor for phase 2 of the passive AC load |
| [[motorcad/parameter_database/parameters/ACLoadAdjustmentPhase3|ACLoadAdjustmentPhase3]] | i/p | double | N/A | The adjustment factor for phase 3 of the passive AC load |
| [[motorcad/parameter_database/parameters/ACLoadInductance|ACLoadInductance]] | i/p | double | Henry | The Inductance component of the passive AC load |
| [[motorcad/parameter_database/parameters/ACLoadInductances_Calculated|ACLoadInductances_Calculated]] | o/p | double | Henry | Inductance of each phase of the passive generator AC load |
| [[motorcad/parameter_database/parameters/ACLoadLineCurrents|ACLoadLineCurrents]] | o/p | double | Amps | Current in each line of the passive generator AC load |
| [[motorcad/parameter_database/parameters/ACLoadPowers|ACLoadPowers]] | o/p | double | Watts | Power dissipated in each line of the passive generator AC load |
| [[motorcad/parameter_database/parameters/ACLoadResistance|ACLoadResistance]] | i/p | double | Ohms | The resistance component of the passive AC load |
| [[motorcad/parameter_database/parameters/ACLoadResistances_Calculated|ACLoadResistances_Calculated]] | o/p | double | Ohms | Resistance of each phase of the passive generator AC load |
| [[motorcad/parameter_database/parameters/ACLoadVoltages|ACLoadVoltages]] | o/p | double | Volts | Voltage across each resistor in the passive generator AC load |
| [[motorcad/parameter_database/parameters/ACLoadWindingConnection|ACLoadWindingConnection]] | i/p | integer | N/A | The winding connection of the passive AC load. |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_FluxDensity|ACLoss_Hybrid_FluxDensity]] | o/p | double | Tesla | Average flux density used to calculate AC proximity loss per cuboid (Hybrid method) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_FluxDensity_L|ACLoss_Hybrid_FluxDensity_L]] | o/p | double | Tesla | Average flux density used to calculate AC proximity loss per cuboid in left side of slot (Hybrid method) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_FluxDensity_R|ACLoss_Hybrid_FluxDensity_R]] | o/p | double | Tesla | Average flux density used to calculate AC proximity loss per cuboid in right side of slot (Hybrid method) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_IncludeSkinEffectLoss|ACLoss_Hybrid_IncludeSkinEffectLoss]] | compatibility | boolean | N/A | Whether to include skin-effect loss in Hybrid AC loss calculation. |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_Prox|ACLoss_Hybrid_Prox]] | o/p | double | Watts | AC proximity losses of full machine per cuboid (Hybrid) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_Prox_L|ACLoss_Hybrid_Prox_L]] | o/p | double | Watts | AC proximity losses of full machine per cuboid (Hybrid) (Left) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_Prox_R|ACLoss_Hybrid_Prox_R]] | o/p | double | Watts | AC proximity losses of full machine per cuboid (Hybrid) (Right) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_Prox_Total|ACLoss_Hybrid_Prox_Total]] | o/p | double | Watts | Total AC proximity losses (Hybrid method) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_Prox_Total_L|ACLoss_Hybrid_Prox_Total_L]] | o/p | double | Watts | Total AC proximity losses in left hand side of slot (Hybrid method) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_Prox_Total_R|ACLoss_Hybrid_Prox_Total_R]] | o/p | double | Watts | Total AC proximity losses in right hand side of slot (Hybrid method) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_SkinEffect|ACLoss_Hybrid_SkinEffect]] | o/p | double | Watts | Skin-effect AC losses (Hybrid method) |
| [[motorcad/parameter_database/parameters/ACLoss_Hybrid_Total|ACLoss_Hybrid_Total]] | o/p | double | Watts | Total AC losses using Hybrid method (proximity + skin-effect) |
| [[motorcad/parameter_database/parameters/ACLoss_SkinEffect_ThermalTransferMethod|ACLoss_SkinEffect_ThermalTransferMethod]] | compatibility | integer | N/A | Improved method includes skin-effect losses when transferring EMag AC losses into Thermal. |
| [[motorcad/parameter_database/parameters/ACLosses_BundleAspectRatio|ACLosses_BundleAspectRatio]] | i/p | double | N/A | Bundle aspect ratio (height / width) used for AC loss calculation. 1=equal width and height. 0.5=half height to width, 2=double height to width |
| [[motorcad/parameter_database/parameters/ACLosses_BundleHeight|ACLosses_BundleHeight]] | o/p | double | mm | Bundle Height used for AC loss calculation |
| [[motorcad/parameter_database/parameters/ACLosses_BundleSize_CalcMethod|ACLosses_BundleSize_CalcMethod]] | compatibility | integer | N/A | Method used for calculating bundle size for round conductors for AC losses. |
| [[motorcad/parameter_database/parameters/ACLosses_BundleWidth|ACLosses_BundleWidth]] | o/p | double | mm | Bundle Width used for AC loss calculation |
| [[motorcad/parameter_database/parameters/AFM_NumSlices|AFM_NumSlices]] | i/p | integer | N/A | Number of slices used to magnetically model Axial Flux Machines in the FEA. |
| [[motorcad/parameter_database/parameters/AFM_SliceRadius_Array|AFM_SliceRadius_Array]] | i/p | double | mm | The radii of modelled slices for Axial Flux motors |
| [[motorcad/parameter_database/parameters/ActualTurnsRatio|ActualTurnsRatio]] | o/p | double | N/A | Actual ratio of aux/main winding turns |
| [[motorcad/parameter_database/parameters/AdjustedMeanCoilPitch|AdjustedMeanCoilPitch]] | o/p | double | mm | The length of average endwinding pitch adjusted to take into account the endwinding multiplier |
| [[motorcad/parameter_database/parameters/AdjustedMeanCoilPitch_Aux|AdjustedMeanCoilPitch_Aux]] | o/p | double | mm | The length of average aux endwinding pitch adjusted to take into account the aux endwinding multiplier |
| [[motorcad/parameter_database/parameters/AdjustedMeanCoilPitch_Inner|AdjustedMeanCoilPitch_Inner]] | o/p | double | mm | The length of average endwinding pitch on the inner side of the stator adjusted to take into account the endwinding multiplier |
| [[motorcad/parameter_database/parameters/AdjustedMeanCoilPitch_Outer|AdjustedMeanCoilPitch_Outer]] | o/p | double | mm | The length of average endwinding pitch on the outer side of the stator adjusted to take into account the endwinding multiplier |
| [[motorcad/parameter_database/parameters/Airgap_Temperature|Airgap_Temperature]] | i/p | double | °C | The temperature of the airgap used for windage loss calculations |
| [[motorcad/parameter_database/parameters/AlignedInductance|AlignedInductance]] | o/p | double | Henry | Inductance of winding in the aligned position |
| [[motorcad/parameter_database/parameters/AnalyticTorqueCalc_SRM|AnalyticTorqueCalc_SRM]] | i/p | boolean | N/A | When selected, analytic torque calculation is run |
| [[motorcad/parameter_database/parameters/AnsysMechanicalExport_ForceType|AnsysMechanicalExport_ForceType]] | setting | integer | N/A | The type of force exported, either both, radial only or tangential only |
| [[motorcad/parameter_database/parameters/AnsysMechanicalExport_Xoffset|AnsysMechanicalExport_Xoffset]] | setting | double | mm | X origin of the motor in the FEA global coordinate system |
| [[motorcad/parameter_database/parameters/AnsysMechanicalExport_Yoffset|AnsysMechanicalExport_Yoffset]] | setting | double | mm | Y origin of the motor in the FEA global coordinate system |
| [[motorcad/parameter_database/parameters/AnsysMechanicalExport_Zoffset|AnsysMechanicalExport_Zoffset]] | setting | double | mm | Z origin of the motor in the FEA global coordinate system |
| [[motorcad/parameter_database/parameters/AnsysMotionExport_FileType|AnsysMotionExport_FileType]] | setting | integer | N/A | Export to Ansys Motion with Object Based or Element Based format |
| [[motorcad/parameter_database/parameters/ApparentPower|ApparentPower]] | o/p | double | Watts | Apparent input power of machine |
| [[motorcad/parameter_database/parameters/ArmatureConductorCSA|ArmatureConductorCSA]] | o/p | double | mm² | The cross sectional area of the armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureConductorCSA_2|ArmatureConductorCSA_2]] | o/p | double | mm² | The cross sectional area of the second armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureConductorCSA_3|ArmatureConductorCSA_3]] | o/p | double | mm² | The cross sectional area of the third armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureConductorCSA_Aux|ArmatureConductorCSA_Aux]] | o/p | double | mm² | The cross sectional area of the auxiliary armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureConductorCurrentDensity|ArmatureConductorCurrentDensity]] | o/p | double | Amps/mm² | The rms current density in the armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureConductorCurrentDensity_Aux|ArmatureConductorCurrentDensity_Aux]] | o/p | double | Amps/mm² | The rms current density in the auxiliary armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureConductorLengthPh|ArmatureConductorLengthPh]] | o/p | double | mm | The length of wire in each phase of the armature winding |
| [[motorcad/parameter_database/parameters/ArmatureConductorLengthPh_Aux|ArmatureConductorLengthPh_Aux]] | o/p | double | mm | The length of each wire in the aux winding |
| [[motorcad/parameter_database/parameters/ArmatureConductor_Resistivity|ArmatureConductor_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the armature conductors at armature conductor temperature |
| [[motorcad/parameter_database/parameters/ArmatureConductor_ResistivityAt20C|ArmatureConductor_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the armature conductors at reference temperature |
| [[motorcad/parameter_database/parameters/ArmatureConductor_ResistivityAt20C_Aux|ArmatureConductor_ResistivityAt20C_Aux]] | i/p | double | Ohm.m | The electrical resistivity for the auxiliary armature conductors at reference temperature |
| [[motorcad/parameter_database/parameters/ArmatureConductor_Resistivity_Aux|ArmatureConductor_Resistivity_Aux]] | o/p | double | Ohm.m | The electrical resistivity for the auxiliary armature conductors at armature conductor temperature |
| [[motorcad/parameter_database/parameters/ArmatureConductor_Temperature|ArmatureConductor_Temperature]] | i/p | double | °C | The temperature of the armature conductor used for loss calculation |
| [[motorcad/parameter_database/parameters/ArmatureEWdgInductance_Aux_Multiplier|ArmatureEWdgInductance_Aux_Multiplier]] | i/p | double | N/A | Multiplier used to adjust inductance of armature aux endwindings |
| [[motorcad/parameter_database/parameters/ArmatureEWdgInductance_Multiplier|ArmatureEWdgInductance_Multiplier]] | i/p | double | N/A | Multiplier used to adjust inductance of armature endwindings |
| [[motorcad/parameter_database/parameters/ArmatureEWdgMLT_Aux_Calculated|ArmatureEWdgMLT_Aux_Calculated]] | o/p | double | mm | Calculated mean length per turn of aux endwindings |
| [[motorcad/parameter_database/parameters/ArmatureEWdgMLT_Aux_Multiplier|ArmatureEWdgMLT_Aux_Multiplier]] | i/p | double | N/A | Multiplier used to adjust mean length per turn of armature aux endwindings |
| [[motorcad/parameter_database/parameters/ArmatureEWdgMLT_Calculated|ArmatureEWdgMLT_Calculated]] | o/p | double | mm | Calculated mean length per turn of armature endwindings |
| [[motorcad/parameter_database/parameters/ArmatureEWdgMLT_Multiplier|ArmatureEWdgMLT_Multiplier]] | i/p | double | N/A | Multiplier used to adjust mean length per turn of armature endwindings |
| [[motorcad/parameter_database/parameters/ArmatureMLT|ArmatureMLT]] | o/p | double | mm | The mean length per turn of the armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureMLT_Aux|ArmatureMLT_Aux]] | o/p | double | mm | The mean length per turn of the aux winding armature conductor |
| [[motorcad/parameter_database/parameters/ArmatureTimeConstant|ArmatureTimeConstant]] | o/p | double | sec | The time constant of the armature |
| [[motorcad/parameter_database/parameters/ArmatureTurnCSA|ArmatureTurnCSA]] | o/p | double | mm² | The cross sectional area of an armature turn (taking into account strands in hand and multiple wire sizes) |
| [[motorcad/parameter_database/parameters/ArmatureTurnsPerCoil|ArmatureTurnsPerCoil]] | o/p | double | N/A | The average number of turns per coil |
| [[motorcad/parameter_database/parameters/ArmatureTurnsPerCoil_Aux|ArmatureTurnsPerCoil_Aux]] | o/p | double | N/A | The average number of turns per coil in the aux winding |
| [[motorcad/parameter_database/parameters/ArmatureTurnsPerPhase|ArmatureTurnsPerPhase]] | o/p | integer | N/A | The number of turns per phase in each parallel path |
| [[motorcad/parameter_database/parameters/ArmatureTurnsPerPhase_Aux|ArmatureTurnsPerPhase_Aux]] | o/p | integer | N/A | The number of turns in each parallel path of the aux winding |
| [[motorcad/parameter_database/parameters/ArmatureWindingResistanceLineToLine|ArmatureWindingResistanceLineToLine]] | o/p | double | Ohms | The line to line resistance of winding at the armature conductor temperature |
| [[motorcad/parameter_database/parameters/ArmatureWindingResistancePh|ArmatureWindingResistancePh]] | o/p | double | Ohms | The resistance of each phase of winding at the armature conductor temperature |
| [[motorcad/parameter_database/parameters/ArmatureWindingResistancePh_Aux|ArmatureWindingResistancePh_Aux]] | o/p | double | Ohms | The aux winding phase resistance |
| [[motorcad/parameter_database/parameters/AvTorqueAlignment|AvTorqueAlignment]] | o/p | double | Nm | The average magnet torque during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/AvTorqueAnalytic|AvTorqueAnalytic]] | o/p | double | Nm | The average analytically calculated torque |
| [[motorcad/parameter_database/parameters/AvTorqueDQ|AvTorqueDQ]] | o/p | double | Nm | The average magnet and reluctance torque calculated using flux linkage method during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/AvTorqueEC|AvTorqueEC]] | o/p | double | Nm | The average torque calculated using energy conversion method during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/AvTorqueMS|AvTorqueMS]] | o/p | double | Nm | The average magnet and reluctance torque calculated using Maxwell stress method during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/AvTorqueMsVw|AvTorqueMsVw]] | o/p | double | Nm | The average torque calculated using Maxwell Stress and Virtual Works finite element methods during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/AvTorqueReluctance|AvTorqueReluctance]] | o/p | double | Nm | The average reluctance torque calculated during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/AvTorqueVW|AvTorqueVW]] | o/p | double | Nm | The average magnet and reluctance torque calculated using virtual work method during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/BMax_Airgap|BMax_Airgap]] | o/p | double | Tesla | Maximum flux density at midpoint in the airgap |
| [[motorcad/parameter_database/parameters/BMax_Airgap_Analytic|BMax_Airgap_Analytic]] | o/p | double | Tesla | Maximum flux density at midpoint in the airgap (from analytic solution) |
| [[motorcad/parameter_database/parameters/BMax_Airgap_Static|BMax_Airgap_Static]] | o/p | double | Tesla | Maximum flux density at midpoint in the airgap (Initial static solution) |
| [[motorcad/parameter_database/parameters/BMax_RotorBackIron|BMax_RotorBackIron]] | o/p | double | Tesla | Maximum flux density at midpoint in the rotor back iron |
| [[motorcad/parameter_database/parameters/BMax_RotorBackIron_Analytic|BMax_RotorBackIron_Analytic]] | o/p | double | Tesla | Maximum flux density at midpoint in the rotor back iron (from analytic solution) |
| [[motorcad/parameter_database/parameters/BMax_RotorBackIron_Static|BMax_RotorBackIron_Static]] | o/p | double | Tesla | Maximum flux density at midpoint in the rotor back iron (Initial static solution) |
| [[motorcad/parameter_database/parameters/BMax_RotorTooth|BMax_RotorTooth]] | o/p | double | Tesla | Maximum flux density at midpoint in the rotor tooth |
| [[motorcad/parameter_database/parameters/BMax_RotorToothTip|BMax_RotorToothTip]] | o/p | double | Tesla | Maximum flux density at midpoint in the rotor tooth tip |
| [[motorcad/parameter_database/parameters/BMax_RotorTooth_Analytic|BMax_RotorTooth_Analytic]] | o/p | double | Tesla | Maximum flux density at midpoint in the rotor tooth (from analytic solution) |
| [[motorcad/parameter_database/parameters/BMax_RotorTooth_Static|BMax_RotorTooth_Static]] | o/p | double | Tesla | Maximum flux density at midpoint in the rotor tooth (Initial static solution) |
| [[motorcad/parameter_database/parameters/BMax_StatorBackIron|BMax_StatorBackIron]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator back iron |
| [[motorcad/parameter_database/parameters/BMax_StatorBackIron_Analytic|BMax_StatorBackIron_Analytic]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator back iron (from analytic solution) |
| [[motorcad/parameter_database/parameters/BMax_StatorBackIron_PerSlice|BMax_StatorBackIron_PerSlice]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator back iron per slice |
| [[motorcad/parameter_database/parameters/BMax_StatorBackIron_Static|BMax_StatorBackIron_Static]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator back iron (Initial static solution) |
| [[motorcad/parameter_database/parameters/BMax_StatorTooth|BMax_StatorTooth]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator tooth |
| [[motorcad/parameter_database/parameters/BMax_StatorToothTip|BMax_StatorToothTip]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator tooth tip |
| [[motorcad/parameter_database/parameters/BMax_StatorTooth_Analytic|BMax_StatorTooth_Analytic]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator tooth (from analytic solution) |
| [[motorcad/parameter_database/parameters/BMax_StatorTooth_PerSlice|BMax_StatorTooth_PerSlice]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator tooth per slice |
| [[motorcad/parameter_database/parameters/BMax_StatorTooth_Static|BMax_StatorTooth_Static]] | o/p | double | Tesla | Maximum flux density at midpoint in the stator tooth (Initial static solution) |
| [[motorcad/parameter_database/parameters/BMean_AirGap|BMean_AirGap]] | o/p | double | Tesla | Mean flux density at midpoint in the airgap |
| [[motorcad/parameter_database/parameters/BMean_Airgap_Analytic|BMean_Airgap_Analytic]] | o/p | double | Tesla | Mean flux density at midpoint in the airgap (from analytic solution) |
| [[motorcad/parameter_database/parameters/BMins|BMins]] | o/p | double | Tesla | Minimum values of B for each magnet |
| [[motorcad/parameter_database/parameters/BPMDriveMode|BPMDriveMode]] | i/p | integer | N/A | The drive mode |
| [[motorcad/parameter_database/parameters/BPMShortCircuitCalc|BPMShortCircuitCalc]] | i/p | boolean | N/A | When selected BPM short circuit calculation is run |
| [[motorcad/parameter_database/parameters/BPMShortCircuitDuration|BPMShortCircuitDuration]] | i/p | double | sec | The duration of the short circuit calculation |
| [[motorcad/parameter_database/parameters/BPMShortCircuitLoadInertia|BPMShortCircuitLoadInertia]] | i/p | double | kg.m² | The short circuit external load inertia |
| [[motorcad/parameter_database/parameters/BPMShortCircuitMaxBrakingTorque|BPMShortCircuitMaxBrakingTorque]] | o/p | double | Nm | Short Circuit maximum transient Braking Torque |
| [[motorcad/parameter_database/parameters/BPMShortCircuitMaxBrakingTorqueSpeed|BPMShortCircuitMaxBrakingTorqueSpeed]] | o/p | double | rpm | Short Circuit speed at which maximum transient Braking Torque occurs |
| [[motorcad/parameter_database/parameters/BPMShortCircuitMaxDemagnetizingCurrent|BPMShortCircuitMaxDemagnetizingCurrent]] | o/p | double | Amps | Maximum D axis short circuit demagnetizing current (from waveform) |
| [[motorcad/parameter_database/parameters/BPMShortCircuitPoints|BPMShortCircuitPoints]] | i/p | integer | N/A | The number of points in the short circuit calculation |
| [[motorcad/parameter_database/parameters/BackEMFCalculation|BackEMFCalculation]] | i/p | boolean | N/A | When selected back EMF calculation is run |
| [[motorcad/parameter_database/parameters/BackEMFLossCalculation|BackEMFLossCalculation]] | i/p | boolean | N/A | When selected Back EMF calculation is run with iron and magnet loss calculations are done on open circuit |
| [[motorcad/parameter_database/parameters/BackEMF_RMS_Aux|BackEMF_RMS_Aux]] | o/p | double | Volts | The RMS back emf in the aux winding |
| [[motorcad/parameter_database/parameters/BackEMF_RMS_Main|BackEMF_RMS_Main]] | o/p | double | Volts | The RMS back emf in the main winding |
| [[motorcad/parameter_database/parameters/Banding2D3DFactor|Banding2D3DFactor]] | o/p | double | N/A | Factor used to convert banding loss in W/m to total losses for machine. Also takes into account any axial segmentation. |
| [[motorcad/parameter_database/parameters/BandingLoss|BandingLoss]] | o/p | double | Watts | Banding Loss of machine |
| [[motorcad/parameter_database/parameters/BandingLoss_OC|BandingLoss_OC]] | o/p | double | Watts | Banding Loss of machine |
| [[motorcad/parameter_database/parameters/Banding_Resistivity|Banding_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the Banding at Banding temperature |
| [[motorcad/parameter_database/parameters/Banding_ResistivityAt20C|Banding_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the Banding at reference temperature |
| [[motorcad/parameter_database/parameters/Banding_Temperature|Banding_Temperature]] | i/p | double | °C | The temperature of the Banding used for loss calculation |
| [[motorcad/parameter_database/parameters/BarCSArea|BarCSArea]] | o/p | double | mm² | Cross sectional area of a Rotor Bar |
| [[motorcad/parameter_database/parameters/BarResistance_NoSkin|BarResistance_NoSkin]] | o/p | double | Ohms | The rotor bar resistance without skin effects |
| [[motorcad/parameter_database/parameters/BarResistance_NoSkin_Ref|BarResistance_NoSkin_Ref]] | o/p | double | Ohms | The referred rotor bar resistance without skin effects |
| [[motorcad/parameter_database/parameters/BarResistance_Skin|BarResistance_Skin]] | o/p | double | Ohms | The rotor bar resistance with skin effects |
| [[motorcad/parameter_database/parameters/BarResistance_Skin_Ref|BarResistance_Skin_Ref]] | o/p | double | Ohms | The referred rotor bar resistance with skin effects |
| [[motorcad/parameter_database/parameters/Bearing_Temperature_F|Bearing_Temperature_F]] | i/p | double | °C | The temperature of the front bearing used for bearing loss calculations |
| [[motorcad/parameter_database/parameters/Bearing_Temperature_R|Bearing_Temperature_R]] | i/p | double | °C | The temperature of the rear bearing used for bearing loss calculations |
| [[motorcad/parameter_database/parameters/BottomRotorBarOpening_Resistivity|BottomRotorBarOpening_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity of the bottom rotor bar opening at rotor bar temperature |
| [[motorcad/parameter_database/parameters/BottomRotorBarOpening_ResistivityAt20|BottomRotorBarOpening_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity of the bottom rotor bar opening at 20C |
| [[motorcad/parameter_database/parameters/BottomRotorBar_Resistivity|BottomRotorBar_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity of the bottom rotor bar at rotor bar temperature |
| [[motorcad/parameter_database/parameters/BottomRotorBar_ResistivityAt20|BottomRotorBar_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity of the bottom rotor bar at 20C |
| [[motorcad/parameter_database/parameters/Br_AdjustmentFactors|Br_AdjustmentFactors]] | o/p | double | N/A | Br adjustment factors for individual magnets |
| [[motorcad/parameter_database/parameters/Brs_Calculated|Brs_Calculated]] | o/p | double | Tesla | Br at magnet temperature for each magnet |
| [[motorcad/parameter_database/parameters/Brs_RefTemp|Brs_RefTemp]] | o/p | double | Tesla | Br at reference temperature for each magnet |
| [[motorcad/parameter_database/parameters/Brs_Used|Brs_Used]] | o/p | double | Tesla | Br used for each magnet during magnetic calculations |
| [[motorcad/parameter_database/parameters/BrushContactVoltageDrop|BrushContactVoltageDrop]] | i/p | double | Volts | The total voltage drop in the circuit due to brush-commutator contacts |
| [[motorcad/parameter_database/parameters/BrushElectricalLoss_OnLoad|BrushElectricalLoss_OnLoad]] | o/p | double | Watts | The total electrical loss in all brushes |
| [[motorcad/parameter_database/parameters/BrushResistanceTotal|BrushResistanceTotal]] | o/p | double | Ohms | The total ohmic resistance of the brushes |
| [[motorcad/parameter_database/parameters/Brush_Resistivity|Brush_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity of the brushes at shaft temperature |
| [[motorcad/parameter_database/parameters/Brush_ResistivityAt20C|Brush_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity of the brushes at reference temperature |
| [[motorcad/parameter_database/parameters/Brush_Temperature|Brush_Temperature]] | i/p | double | °C | The temperature of the brushes used for loss calculation |
| [[motorcad/parameter_database/parameters/CS_Area_Rotor_Cage_Bottom|CS_Area_Rotor_Cage_Bottom]] | o/p | double | mm² | Cross sectional area of a Rotor Bar top section |
| [[motorcad/parameter_database/parameters/CS_Area_Rotor_Cage_Bottom_Opening|CS_Area_Rotor_Cage_Bottom_Opening]] | o/p | double | mm² | Cross sectional area of a Rotor Bar bottom section opening |
| [[motorcad/parameter_database/parameters/CS_Area_Rotor_Cage_Top|CS_Area_Rotor_Cage_Top]] | o/p | double | mm² | Cross sectional area of a Rotor Bar top section |
| [[motorcad/parameter_database/parameters/CS_Area_Rotor_Cage_Top_Opening|CS_Area_Rotor_Cage_Top_Opening]] | o/p | double | mm² | Cross sectional area of a Rotor Bar top section opening |
| [[motorcad/parameter_database/parameters/CalculatedCurrentsDriveCircuit|CalculatedCurrentsDriveCircuit]] | compatibility | integer | N/A | Enable resistance/capacitance/switching angle for square wave/calculated sine drives |
| [[motorcad/parameter_database/parameters/CalculatedCurrentsSquareDCBusCalculation|CalculatedCurrentsSquareDCBusCalculation]] | compatibility | integer | N/A | The improved method correctly considers freewheeling currents when calculating the DC bus current for square wave drive |
| [[motorcad/parameter_database/parameters/CalculationCancelled|CalculationCancelled]] | o/p | boolean | N/A | When set true the calculation is cancelled. |
| [[motorcad/parameter_database/parameters/CalculationRunning_EMag|CalculationRunning_EMag]] | o/p | boolean | N/A | When set true the EMag calculation is running |
| [[motorcad/parameter_database/parameters/CanLoss|CanLoss]] | o/p | double | Watts | Can (Banding) Loss of BPM machine |
| [[motorcad/parameter_database/parameters/CanLoss_OC|CanLoss_OC]] | o/p | double | Watts | Can (Banding) Loss of BPM machine |
| [[motorcad/parameter_database/parameters/CarterCoefficient_Rotor|CarterCoefficient_Rotor]] | o/p | double | N/A | The carter coefficient for the rotor |
| [[motorcad/parameter_database/parameters/CarterCoefficient_Stator|CarterCoefficient_Stator]] | o/p | double | N/A | The carter coefficient for the stator |
| [[motorcad/parameter_database/parameters/CarterCoefficient_Total|CarterCoefficient_Total]] | o/p | double | N/A | The total carter coefficient for the stator and rotor |
| [[motorcad/parameter_database/parameters/CentrifugalForceCalc|CentrifugalForceCalc]] | i/p | boolean | N/A | When selected rotor Centrifugal Force calculation is run |
| [[motorcad/parameter_database/parameters/CoggingFrequency|CoggingFrequency]] | o/p | double | Hz | Frequency of cogging cycles |
| [[motorcad/parameter_database/parameters/CoggingPeriod|CoggingPeriod]] | o/p | double | MDeg | Angle between cogging cycles |
| [[motorcad/parameter_database/parameters/CoggingTorqueCalculation|CoggingTorqueCalculation]] | i/p | boolean | N/A | When selected Cogging Torque calculation is run |
| [[motorcad/parameter_database/parameters/CoggingTorqueRippleCe|CoggingTorqueRippleCe]] | o/p | double | Nm | The cogging torque ripple calculated using Co-Energy finite element method during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/CoggingTorqueRippleVw|CoggingTorqueRippleVw]] | o/p | double | Nm | The cogging torque ripple calculated using Virtual Works finite element method during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/CoilSidesPerLayer|CoilSidesPerLayer]] | i/p | integer | N/A | The number of coil sides per layer |
| [[motorcad/parameter_database/parameters/CoilsPerPath_Array|CoilsPerPath_Array]] | i/p | integer | N/A | The number of coils per path in each phase |
| [[motorcad/parameter_database/parameters/ConductorLoss|ConductorLoss]] | o/p | double | Watts | DC Conductor Loss of the armature winding |
| [[motorcad/parameter_database/parameters/ConductorLoss_OC|ConductorLoss_OC]] | o/p | double | Watts | DC Conductor Loss of open circuit armature winding |
| [[motorcad/parameter_database/parameters/ConductorSkinDepth|ConductorSkinDepth]] | o/p | double | mm | The skin depth in conductors |
| [[motorcad/parameter_database/parameters/ContinuousSkewMethod|ContinuousSkewMethod]] | compatibility | integer | N/A | Method used to account for continuous skew |
| [[motorcad/parameter_database/parameters/ConverterEfficiency|ConverterEfficiency]] | o/p | double | Percent | Efficiency of converter (including external line losses) |
| [[motorcad/parameter_database/parameters/ConverterLosses|ConverterLosses]] | i/p | double | Watts | The dc bus converter losses |
| [[motorcad/parameter_database/parameters/CoreLossCurrent_Aux_RMS|CoreLossCurrent_Aux_RMS]] | o/p | double | Amps | The on load aux winding RMS core loss current |
| [[motorcad/parameter_database/parameters/CoreLossCurrent_Main_RMS|CoreLossCurrent_Main_RMS]] | o/p | double | Amps | The on load main winding RMS core loss current |
| [[motorcad/parameter_database/parameters/CoreLossResistance_Aux|CoreLossResistance_Aux]] | o/p | double | Ohms | The on load aux winding RMS core loss resistance |
| [[motorcad/parameter_database/parameters/CoreLoss_Aux_Analytic|CoreLoss_Aux_Analytic]] | o/p | double | Watts | The aux winding core losses |
| [[motorcad/parameter_database/parameters/CoreLoss_Main_Analytic|CoreLoss_Main_Analytic]] | o/p | double | Watts | The main winding core losses |
| [[motorcad/parameter_database/parameters/CurrentAngle|CurrentAngle]] | o/p | double | EDeg | Current Angle |
| [[motorcad/parameter_database/parameters/CurrentDefinition|CurrentDefinition]] | i/p | integer | N/A | Defines whether the current input is rms current, peak current or rms current density |
| [[motorcad/parameter_database/parameters/CurrentLoad_D|CurrentLoad_D]] | o/p | double | Amps | The single point rms phase current in D axis |
| [[motorcad/parameter_database/parameters/CurrentLoad_D_Average_Phase|CurrentLoad_D_Average_Phase]] | o/p | double | Amps | The average rms phase current in D axis |
| [[motorcad/parameter_database/parameters/CurrentLoad_Q|CurrentLoad_Q]] | o/p | double | Amps | The single point rms phase current in Q axis |
| [[motorcad/parameter_database/parameters/CurrentLoad_Q_Average_Phase|CurrentLoad_Q_Average_Phase]] | o/p | double | Amps | The average rms phase current in Q axis |
| [[motorcad/parameter_database/parameters/CurrentPoints_Calculated_MagnetisationCurves|CurrentPoints_Calculated_MagnetisationCurves]] | i/p | integer | N/A | The current points points in the magnetisation curves |
| [[motorcad/parameter_database/parameters/CustomDriveCycleFile|CustomDriveCycleFile]] | i/p | OleStr | N/A | Custom Drive Cycle file |
| [[motorcad/parameter_database/parameters/CustomDriveCyclePeakAmplitude|CustomDriveCyclePeakAmplitude]] | o/p | double | p.u. | Peak amplitude of the custom waveform |
| [[motorcad/parameter_database/parameters/CustomDriveCyclePeakLineCurrent|CustomDriveCyclePeakLineCurrent]] | o/p | double | Amps | Peak amplitude of the custom line current waveform |
| [[motorcad/parameter_database/parameters/CustomDriveCyclePointReduction|CustomDriveCyclePointReduction]] | i/p | integer | N/A | The point reduction used for importing custom drive cycles. When set to 1 then all data points are imported from a file. |
| [[motorcad/parameter_database/parameters/CustomDriveCyclePoints|CustomDriveCyclePoints]] | i/p | integer | N/A | Number of custom drive current points |
| [[motorcad/parameter_database/parameters/CustomDriveCycleRMSAmplitude|CustomDriveCycleRMSAmplitude]] | o/p | double | p.u. | RMS amplitude of the custom waveform |
| [[motorcad/parameter_database/parameters/CustomDriveCycleRMSLineCurrent|CustomDriveCycleRMSLineCurrent]] | o/p | double | Amps | RMS amplitude of the custom line current waveform |
| [[motorcad/parameter_database/parameters/CustomDriveCycle_PeakRMS_Method|CustomDriveCycle_PeakRMS_Method]] | compatibility | integer | N/A | Method for calculating peak and RMS currents of custom drive cycle |
| [[motorcad/parameter_database/parameters/CustomDriveDefinition|CustomDriveDefinition]] | i/p | integer | N/A | Waveforms or Harmonics definition |
| [[motorcad/parameter_database/parameters/CustomDriveFundamentalAmplitude|CustomDriveFundamentalAmplitude]] | o/p | double | p.u. | Amplitude of the fundamental harmonic of the custom waveform |
| [[motorcad/parameter_database/parameters/CustomDrivePeakToRMS_Amplitude|CustomDrivePeakToRMS_Amplitude]] | o/p | double | N/A | RMS : Peak ratio of the custom waveform |
| [[motorcad/parameter_database/parameters/CustomDrivePeakToRMS_LineCurrent|CustomDrivePeakToRMS_LineCurrent]] | o/p | double | N/A | RMS : Peak ratio of the custom line current waveform |
| [[motorcad/parameter_database/parameters/DCArmatureResistance|DCArmatureResistance]] | o/p | double | Ohms | Resistance of the armature windings |
| [[motorcad/parameter_database/parameters/DCArmatureWindingSense|DCArmatureWindingSense]] | i/p | integer | N/A | The sense of the winding pattern, progressive or regressive |
| [[motorcad/parameter_database/parameters/DCArmatureWindingStyle|DCArmatureWindingStyle]] | i/p | integer | N/A | The winding type, lap or wave |
| [[motorcad/parameter_database/parameters/DCBusVoltage|DCBusVoltage]] | i/p | double | Volts | The DC Bus Voltage |
| [[motorcad/parameter_database/parameters/DCConductorLoss_Armature_A|DCConductorLoss_Armature_A]] | o/p | double | Watts | DC Conductor Loss of active section of the armature winding |
| [[motorcad/parameter_database/parameters/DCConductorLoss_Field|DCConductorLoss_Field]] | o/p | double | Watts | DC Conductor Loss of the field winding |
| [[motorcad/parameter_database/parameters/DCCurrent|DCCurrent]] | i/p | double | Amps | The DC machine current |
| [[motorcad/parameter_database/parameters/DCCurrentDensity|DCCurrentDensity]] | i/p | double | Amps/mm² | The DC current density |
| [[motorcad/parameter_database/parameters/DCDriveDefinition|DCDriveDefinition]] | i/p | integer | N/A | Defines whether the input is current, current density or voltage |
| [[motorcad/parameter_database/parameters/DCFieldCurrent|DCFieldCurrent]] | i/p | double | Amps | The DC field current |
| [[motorcad/parameter_database/parameters/DCFilterCapacitance|DCFilterCapacitance]] | i/p | double | Farad | The capacitance component of the DC filter |
| [[motorcad/parameter_database/parameters/DCFilterInductance|DCFilterInductance]] | i/p | double | Henry | The inductance component of the DC filter |
| [[motorcad/parameter_database/parameters/DCLoadResistance|DCLoadResistance]] | i/p | double | Ohms | The resistance component of the filtered DC load |
| [[motorcad/parameter_database/parameters/DCLoadResistorPower|DCLoadResistorPower]] | o/p | double | Watts | The power dissipated by the DC load resistor |
| [[motorcad/parameter_database/parameters/DCLoadResistorVoltage|DCLoadResistorVoltage]] | o/p | double | Volts | The voltage over the load resistor |
| [[motorcad/parameter_database/parameters/DCLoadType|DCLoadType]] | i/p | integer | N/A | The type of DC load model powered by generator. |
| [[motorcad/parameter_database/parameters/DCLoadVoltage|DCLoadVoltage]] | i/p | double | Volts | The voltage component of the filtered DC load |
| [[motorcad/parameter_database/parameters/DCLoadVoltagePower|DCLoadVoltagePower]] | o/p | double | Watts | The power absorbed by the DC load voltage |
| [[motorcad/parameter_database/parameters/DamperBarCSArea|DamperBarCSArea]] | o/p | double | mm² | The cross sectional area of a damper bar |
| [[motorcad/parameter_database/parameters/DamperBarDifferentialLeakageInductance|DamperBarDifferentialLeakageInductance]] | o/p | double | Henry | The damper bar differential leakage inductance |
| [[motorcad/parameter_database/parameters/DamperBarOnLoadLoss|DamperBarOnLoadLoss]] | o/p | double | Watts | Damper Cage Loss of machine |
| [[motorcad/parameter_database/parameters/DamperBarResistance_NoSkin|DamperBarResistance_NoSkin]] | o/p | double | Ohms | The damper bar resistance |
| [[motorcad/parameter_database/parameters/DamperBarResistance_NoSkin_Ref|DamperBarResistance_NoSkin_Ref]] | o/p | double | Ohms | The referred damper bar resistance without skin effects |
| [[motorcad/parameter_database/parameters/DamperBarSlotLeakageInductance|DamperBarSlotLeakageInductance]] | o/p | double | Henry | The damper bar slot leakage inductance |
| [[motorcad/parameter_database/parameters/DamperBar_Resistivity|DamperBar_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the damper bars at the damper bar temperature |
| [[motorcad/parameter_database/parameters/DamperBar_ResistivityAt20|DamperBar_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity for the damper bars at the reference temperature |
| [[motorcad/parameter_database/parameters/DamperBar_Temperature|DamperBar_Temperature]] | i/p | double | °C | The temperature of the damper bars used for loss calculation |
| [[motorcad/parameter_database/parameters/DamperCageLeakageInductance_Total|DamperCageLeakageInductance_Total]] | o/p | double | Henry | The total damper cage leakage inductance |
| [[motorcad/parameter_database/parameters/DamperCageLeakageInductance_Total_Ref|DamperCageLeakageInductance_Total_Ref]] | o/p | double | Henry | The total damper cage leakage inductance referred to the stator |
| [[motorcad/parameter_database/parameters/DamperCageLeakageReactance_Total|DamperCageLeakageReactance_Total]] | o/p | double | Ohms | The total damper cage leakage reactance |
| [[motorcad/parameter_database/parameters/DamperCageLeakageReactance_Total_Ref|DamperCageLeakageReactance_Total_Ref]] | o/p | double | Ohms | The total damper cage leakage reactance referred to the stator |
| [[motorcad/parameter_database/parameters/DamperCageResistance_Total|DamperCageResistance_Total]] | o/p | double | Ohms | The total damper cage resistance |
| [[motorcad/parameter_database/parameters/DamperCageResistance_Total_Ref|DamperCageResistance_Total_Ref]] | o/p | double | Ohms | The total referred damper cape resistance |
| [[motorcad/parameter_database/parameters/DamperERInductance_F_InterBar|DamperERInductance_F_InterBar]] | o/p | double | Henry | The front end ring inductance between two damper bars |
| [[motorcad/parameter_database/parameters/DamperERInductance_F_Richter|DamperERInductance_F_Richter]] | o/p | double | Henry | The front damper end ring inductance using Richter method |
| [[motorcad/parameter_database/parameters/DamperERInductance_InterBar|DamperERInductance_InterBar]] | o/p | double | Henry | The end ring inductance between two damper bars |
| [[motorcad/parameter_database/parameters/DamperERInductance_R_InterBar|DamperERInductance_R_InterBar]] | o/p | double | Henry | The rear end ring inductance between two damper bars |
| [[motorcad/parameter_database/parameters/DamperERInductance_R_Richter|DamperERInductance_R_Richter]] | o/p | double | Henry | The rear damper end ring inductance using Richter method |
| [[motorcad/parameter_database/parameters/DamperERInductance_Richter|DamperERInductance_Richter]] | o/p | double | Henry | The damper end ring inductance using Richter method |
| [[motorcad/parameter_database/parameters/DamperERInductance_Richter_Ref|DamperERInductance_Richter_Ref]] | o/p | double | Henry | The damper end ring inductance using Richter method |
| [[motorcad/parameter_database/parameters/DamperEndRingResistance|DamperEndRingResistance]] | o/p | double | Ohms | The end ring resistance per damper bar |
| [[motorcad/parameter_database/parameters/DamperEndRingResistance_F|DamperEndRingResistance_F]] | o/p | double | Ohms | The front end ring resistance per damper bar |
| [[motorcad/parameter_database/parameters/DamperEndRingResistance_R|DamperEndRingResistance_R]] | o/p | double | Ohms | The rear end ring resistance per damper bar |
| [[motorcad/parameter_database/parameters/DamperEndRingResistance_Ref|DamperEndRingResistance_Ref]] | o/p | double | Ohms | The referred end ring resistance per damper bar |
| [[motorcad/parameter_database/parameters/DamperEnd_F_ResistivityAt20|DamperEnd_F_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity for the front damper end ring at the reference temperature |
| [[motorcad/parameter_database/parameters/DamperEnd_R_ResistivityAt20|DamperEnd_R_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity for the rear damper end ring at the reference temperature |
| [[motorcad/parameter_database/parameters/DamperEnd_Resistivity|DamperEnd_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the damper end rings at the damper end ring temperature |
| [[motorcad/parameter_database/parameters/DamperEnd_ResistivityAt20|DamperEnd_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity for the damper end rings at the reference temperature |
| [[motorcad/parameter_database/parameters/DamperEnd_Resistivity_F|DamperEnd_Resistivity_F]] | o/p | double | Ohm.m | The electrical resistivity for the front damper end ring at the damper end ring temperature |
| [[motorcad/parameter_database/parameters/DamperEnd_Resistivity_R|DamperEnd_Resistivity_R]] | o/p | double | Ohm.m | The electrical resistivity for the rear damper end ring at the damper end ring temperature |
| [[motorcad/parameter_database/parameters/DamperEnd_Temperature|DamperEnd_Temperature]] | i/p | double | °C | The temperature of the damper end rings used for loss calculation |
| [[motorcad/parameter_database/parameters/DamperEndringCSArea|DamperEndringCSArea]] | o/p | double | mm² | The average cross sectional area of damper end rings |
| [[motorcad/parameter_database/parameters/DamperEndringCSArea_F|DamperEndringCSArea_F]] | o/p | double | mm² | The cross sectional area of front damper end ring |
| [[motorcad/parameter_database/parameters/DamperEndringCSArea_R|DamperEndringCSArea_R]] | o/p | double | mm² | The cross sectional area of rear damper end ring |
| [[motorcad/parameter_database/parameters/DamperOpening_Resistivity|DamperOpening_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the damper opening at the damper bar temperature |
| [[motorcad/parameter_database/parameters/DamperOpening_ResistivityAt20|DamperOpening_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity for the damper opening at the reference temperature |
| [[motorcad/parameter_database/parameters/Date_Calculated_IMLookupCurves|Date_Calculated_IMLookupCurves]] | i/p | OleStr | N/A | The date of the last IM saturation model calculation |
| [[motorcad/parameter_database/parameters/Date_Calculated_MagnetisationCurves|Date_Calculated_MagnetisationCurves]] | i/p | OleStr | N/A | The time and date of the last magnetisation curves calculation |
| [[motorcad/parameter_database/parameters/DemagCurveMethod|DemagCurveMethod]] | recommended | integer | N/A | Specifies whether magnets should use a linear or non-linear demagnetisation curve |
| [[motorcad/parameter_database/parameters/DemagCurveTemperatures|DemagCurveTemperatures]] | i/p | double | °C | Temperatures for displaying demagnetization curves |
| [[motorcad/parameter_database/parameters/DemagKneePoint_Calculated|DemagKneePoint_Calculated]] | o/p | double | Tesla | Knee point below which magnet experiences irreversible demagnetization (automatically detected) |
| [[motorcad/parameter_database/parameters/DemagKneePointsInFEA|DemagKneePointsInFEA]] | o/p | double | Tesla | Demagnetization knee point used for specified material and temperature |
| [[motorcad/parameter_database/parameters/DemagProjectionMethod|DemagProjectionMethod]] | compatibility | integer | N/A | Method used for demagnetisation ratio when using projection method. |
| [[motorcad/parameter_database/parameters/DemagRatioMethod|DemagRatioMethod]] | i/p | integer | N/A | Method for calculating demagnetisation ratios |
| [[motorcad/parameter_database/parameters/DemagRatios|DemagRatios]] | o/p | double | N/A | Demagnetisation ratios of each magnet |
| [[motorcad/parameter_database/parameters/DemagnetizationCalc|DemagnetizationCalc]] | i/p | boolean | N/A | When selected demagnetization calculation is run |
| [[motorcad/parameter_database/parameters/DriveCalculationIterations|DriveCalculationIterations]] | o/p | integer | N/A | Number of iterations used in drive solver |
| [[motorcad/parameter_database/parameters/DriveChoppingMode|DriveChoppingMode]] | i/p | integer | N/A | The chopping mode of the inverter. |
| [[motorcad/parameter_database/parameters/DriveCurrent|DriveCurrent]] | o/p | double | Amps | The calculated peak drive line current from the square wave drive simulation |
| [[motorcad/parameter_database/parameters/DriveDiodeVoltage|DriveDiodeVoltage]] | i/p | double | Volts | The drive flywheel diode forward voltage |
| [[motorcad/parameter_database/parameters/DriveDutyCycle|DriveDutyCycle]] | i/p | double | N/A | The maximum square wave drive duty cycle. |
| [[motorcad/parameter_database/parameters/DriveEffectiveSwitchingFrequency|DriveEffectiveSwitchingFrequency]] | i/p | double | kHz | The drive simulation effective switching frequency |
| [[motorcad/parameter_database/parameters/DriveModulation|DriveModulation]] | i/p | integer | N/A | The drive modulation type |
| [[motorcad/parameter_database/parameters/DriveOffsetAngleLoad|DriveOffsetAngleLoad]] | o/p | double | EDeg | The drive offset in electrical degrees for on load |
| [[motorcad/parameter_database/parameters/DriveOffsetAngleOC|DriveOffsetAngleOC]] | o/p | double | EDeg | The drive offset in electrical degrees for open circuit |
| [[motorcad/parameter_database/parameters/DriveSwitchResistance|DriveSwitchResistance]] | i/p | double | Ohms | The drive switching device effective resistance |
| [[motorcad/parameter_database/parameters/DriveSwitchVoltage|DriveSwitchVoltage]] | i/p | double | Volts | The drive switching device forward voltage |
| [[motorcad/parameter_database/parameters/DriveSwitchingAngle|DriveSwitchingAngle]] | i/p | double | EDeg | The angle that drive switches are closed for |
| [[motorcad/parameter_database/parameters/DriveSwitchingFrequencyDefinition|DriveSwitchingFrequencyDefinition]] | i/p | integer | N/A | The definition method for the drive switching frequency. |
| [[motorcad/parameter_database/parameters/DriveType_BPM|DriveType_BPM]] | i/p | integer | N/A | The drive type |
| [[motorcad/parameter_database/parameters/DwellAngle_SRM|DwellAngle_SRM]] | i/p | double | EDeg | SRM drive dwell angle |
| [[motorcad/parameter_database/parameters/EWdgThermalWindingLayers_F|EWdgThermalWindingLayers_F]] | i/p | integer | N/A | Number of Winding Layers in Front End Winding |
| [[motorcad/parameter_database/parameters/EWdgThermalWindingLayers_R|EWdgThermalWindingLayers_R]] | i/p | integer | N/A | Number of Winding Layers in Rear End Winding |
| [[motorcad/parameter_database/parameters/EWdg_MLT_Aux_Used|EWdg_MLT_Aux_Used]] | o/p | double | mm | Mean length per turn of aux endwindings used in the calculation |
| [[motorcad/parameter_database/parameters/EddyLossBuildFactor|EddyLossBuildFactor]] | i/p | double | N/A | Multiplier used to adjust iron eddy losses |
| [[motorcad/parameter_database/parameters/Effective_Brs|Effective_Brs]] | o/p | double | Tesla | Effective (average) Br of each magnet accounting for irreversible demagnetisation |
| [[motorcad/parameter_database/parameters/ElectricalConstant|ElectricalConstant]] | o/p | double | msec | Electrical Constant |
| [[motorcad/parameter_database/parameters/ElectricalLoading|ElectricalLoading]] | o/p | double | Amps/m | Electrical Loading |
| [[motorcad/parameter_database/parameters/ElectricalLoading_Array|ElectricalLoading_Array]] | o/p | double | Amps/m | Electrical Loading for each Axial Flux machine slice |
| [[motorcad/parameter_database/parameters/ElectromagneticForcesCalc_Load|ElectromagneticForcesCalc_Load]] | i/p | boolean | N/A | When selected electromagnetic forces calculation is run |
| [[motorcad/parameter_database/parameters/ElectromagneticForcesCalc_OC|ElectromagneticForcesCalc_OC]] | i/p | boolean | N/A | When selected electromagnetic forces calculation is run |
| [[motorcad/parameter_database/parameters/ElectromagneticPower|ElectromagneticPower]] | o/p | double | Watts | Electromagnetic power of machine |
| [[motorcad/parameter_database/parameters/EndRingResistance|EndRingResistance]] | o/p | double | Ohms | The Endring Resistance between adjacent bars |
| [[motorcad/parameter_database/parameters/EndRingResistance_Ref|EndRingResistance_Ref]] | o/p | double | Ohms | The referred Endring Resistance between adjacent bars |
| [[motorcad/parameter_database/parameters/EndRing_Resistivity|EndRing_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the end rings at average end ring temperature |
| [[motorcad/parameter_database/parameters/EndRing_ResistivityAt20|EndRing_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity for the end rings at reference temperature |
| [[motorcad/parameter_database/parameters/EndRing_Temperature|EndRing_Temperature]] | i/p | double | °C | The average temperature of the front and rear end rings used for loss calculation |
| [[motorcad/parameter_database/parameters/EndWdgInductance_Aux_Calculated|EndWdgInductance_Aux_Calculated]] | o/p | double | Henry | The calculate inductance of the aux end windings |
| [[motorcad/parameter_database/parameters/EndWdgInductance_Aux_Used|EndWdgInductance_Aux_Used]] | o/p | double | Henry | The inductance of the aux end windings used in calculations |
| [[motorcad/parameter_database/parameters/EndWdgInductance_Calculated|EndWdgInductance_Calculated]] | o/p | double | Henry | The inductance of armature end windings calculated |
| [[motorcad/parameter_database/parameters/EndWdgInductance_Used|EndWdgInductance_Used]] | o/p | double | Henry | The inductance of armature end windings after user adjustment |
| [[motorcad/parameter_database/parameters/EndWdgReactance|EndWdgReactance]] | o/p | double | Ohms | The reactance of the armature end windings |
| [[motorcad/parameter_database/parameters/EndWdgReactance_Aux|EndWdgReactance_Aux]] | o/p | double | Ohms | The reactance of the aux end windings |
| [[motorcad/parameter_database/parameters/EndringCSArea|EndringCSArea]] | o/p | double | mm² | Cross sectional area of a Rotor end ring |
| [[motorcad/parameter_database/parameters/EndringInductance_InterBar|EndringInductance_InterBar]] | o/p | double | Henry | End ring inductance between two rotor bars |
| [[motorcad/parameter_database/parameters/EndringInductance_LiwschitzGarick|EndringInductance_LiwschitzGarick]] | o/p | double | Henry | End ring inductance using Liwshitz-Garick method |
| [[motorcad/parameter_database/parameters/EndringInductance_LiwschitzGarick_Ref|EndringInductance_LiwschitzGarick_Ref]] | o/p | double | Henry | End ring inductance using Liwshitz-Garick method referred to the stator |
| [[motorcad/parameter_database/parameters/EndringInductance_Richter|EndringInductance_Richter]] | o/p | double | Henry | End ring inductance using Richter method |
| [[motorcad/parameter_database/parameters/EndringInductance_Richter_Ref|EndringInductance_Richter_Ref]] | o/p | double | Henry | End ring inductance using Richter method |
| [[motorcad/parameter_database/parameters/EndringReactance_LiwschitzGarick|EndringReactance_LiwschitzGarick]] | o/p | double | Ohms | End ring reactance using Liwshitz-Garick method |
| [[motorcad/parameter_database/parameters/EndringReactance_LiwschitzGarick_Ref|EndringReactance_LiwschitzGarick_Ref]] | o/p | double | Ohms | End ring reactance using Liwshitz-Garick method referred to the stator |
| [[motorcad/parameter_database/parameters/EndringReactance_Richter|EndringReactance_Richter]] | o/p | double | Ohms | End ring reactance using Richter method |
| [[motorcad/parameter_database/parameters/EndringReactance_Richter_Ref|EndringReactance_Richter_Ref]] | o/p | double | Ohms | End ring reactance using Richter method referred to the stator |
| [[motorcad/parameter_database/parameters/EnergyConversionResistance_Ref|EnergyConversionResistance_Ref]] | o/p | double | Ohms | The referred energy conversion Resistance |
| [[motorcad/parameter_database/parameters/EnergyConversionResistance_Ref_L|EnergyConversionResistance_Ref_L]] | o/p | double | Ohms | The referred energy conversion Resistance |
| [[motorcad/parameter_database/parameters/Envelope_Speed_Array|Envelope_Speed_Array]] | i/p | double | rpm | Envelope Speed Array |
| [[motorcad/parameter_database/parameters/Envelope_Torque_Array|Envelope_Torque_Array]] | i/p | double | Nm | Envelope Torque Array |
| [[motorcad/parameter_database/parameters/ExcitationTimeConstant|ExcitationTimeConstant]] | o/p | double | sec | The time constant of the exciter |
| [[motorcad/parameter_database/parameters/ExternalLine_Area|ExternalLine_Area]] | i/p | double | mm² | Line cross sectional area of AC supply connections (copper) |
| [[motorcad/parameter_database/parameters/ExternalLine_Definition|ExternalLine_Definition]] | i/p | integer | N/A | Definition of the external line resistance, by value or copper dimensions |
| [[motorcad/parameter_database/parameters/ExternalLine_Length|ExternalLine_Length]] | i/p | double | mm | Line length of AC supply connections (copper) |
| [[motorcad/parameter_database/parameters/ExternalLine_Loss|ExternalLine_Loss]] | o/p | double | Watts | Losses dissipated in the AC supply lines. |
| [[motorcad/parameter_database/parameters/ExternalLine_Resistance|ExternalLine_Resistance]] | i/p | double | Ohms | Line resistance of the AC supply. |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_CalcMethod|FEAMeasurePath_CalcMethod]] | i/p | integer | N/A | Calculation method used along path |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_Calculation|FEAMeasurePath_Calculation]] | i/p | OleStr | N/A | Calculation to which path is applied to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_CoordSystem|FEAMeasurePath_CoordSystem]] | i/p | integer | N/A | Coordinate system used in path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_EndAngle|FEAMeasurePath_EndAngle]] | i/p | double | MDeg | Final angle (degrees) in path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_EndR|FEAMeasurePath_EndR]] | i/p | double | mm | Final radius (degrees) in straight path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_EndX|FEAMeasurePath_EndX]] | i/p | double | mm | Final X co-ordinate in straight path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_EndY|FEAMeasurePath_EndY]] | i/p | double | mm | Final Y co-ordinate in straight path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_Expression|FEAMeasurePath_Expression]] | i/p | OleStr | N/A | Expression which is measured along path (FEA) |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_IntegralForceCorrection|FEAMeasurePath_IntegralForceCorrection]] | compatibility | integer | N/A | The improved method calculates the force integral taking into account the half arc length of the first and last point. The original method scales all points. |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_Length|FEAMeasurePath_Length]] | o/p | double | mm | Calculated path length |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_NumPaths|FEAMeasurePath_NumPaths]] | i/p | integer | N/A | Number of defined paths for measuring from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_NumPoints|FEAMeasurePath_NumPoints]] | i/p | integer | N/A | Number of points in path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_PathLocation|FEAMeasurePath_PathLocation]] | i/p | integer | N/A | The location of path used to measure from FEA (stator or rotor) |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_PathName|FEAMeasurePath_PathName]] | i/p | OleStr | N/A | Name of path to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_PathType|FEAMeasurePath_PathType]] | i/p | integer | N/A | The type of path to use when measuring from FEA (straight or curved) |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_StartAngle|FEAMeasurePath_StartAngle]] | i/p | double | MDeg | Initial angle (degrees) in path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_StartR|FEAMeasurePath_StartR]] | i/p | double | mm | Initial radius in path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_StartX|FEAMeasurePath_StartX]] | i/p | double | mm | Initial X co-ordinate in straight path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEAMeasurePath_StartY|FEAMeasurePath_StartY]] | i/p | double | mm | Initial Y co-ordinate in straight path used to measure from FEA |
| [[motorcad/parameter_database/parameters/FEARotorSlotArea|FEARotorSlotArea]] | o/p | double | mm² | The rotor slot area calculated by the FEA and used for setting of current density in FEA model |
| [[motorcad/parameter_database/parameters/FEASlotArea|FEASlotArea]] | o/p | double | mm² | The slot area calculated by the FEA and used for setting of current density in FEA model |
| [[motorcad/parameter_database/parameters/FEATorqueCalc_SRM|FEATorqueCalc_SRM]] | i/p | boolean | N/A | When selected, FEA torque calculation is run |
| [[motorcad/parameter_database/parameters/FieldConductorCSA|FieldConductorCSA]] | o/p | double | mm² | The cross sectional area of the field conductor |
| [[motorcad/parameter_database/parameters/FieldConductorLength|FieldConductorLength]] | o/p | double | mm | The total length of wire in the field winding |
| [[motorcad/parameter_database/parameters/FieldConductor_Resistivity|FieldConductor_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the field conductors at field conductor temperature |
| [[motorcad/parameter_database/parameters/FieldConductor_ResistivityAt20C|FieldConductor_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the field conductors at reference temperature |
| [[motorcad/parameter_database/parameters/FieldConductor_Temperature|FieldConductor_Temperature]] | i/p | double | °C | The temperature of the field Conductor used for loss calculation |
| [[motorcad/parameter_database/parameters/FieldCurrentDefinition|FieldCurrentDefinition]] | i/p | integer | N/A | Defines whether the field current is DC current or current density |
| [[motorcad/parameter_database/parameters/FieldCurrentDensity|FieldCurrentDensity]] | i/p | double | Amps/mm² | The DC current density in the field conductor |
| [[motorcad/parameter_database/parameters/FieldCurrentDensity_Used|FieldCurrentDensity_Used]] | o/p | double | Amps/mm² | The DC current density in the field conductor used in FEA simulations |
| [[motorcad/parameter_database/parameters/FieldEWdgMLT_Calculated|FieldEWdgMLT_Calculated]] | o/p | double | mm | Calculated mean length per turn of the field endwindings |
| [[motorcad/parameter_database/parameters/FieldEWdgMLT_Multiplier|FieldEWdgMLT_Multiplier]] | i/p | double | N/A | Multiplier used to adjust mean length per turn of the field endwindings |
| [[motorcad/parameter_database/parameters/FieldMLT|FieldMLT]] | o/p | double | mm | The mean length per turn of the field conductor |
| [[motorcad/parameter_database/parameters/FieldWindingInductance|FieldWindingInductance]] | o/p | double | Henry | The inductance of the field windings |
| [[motorcad/parameter_database/parameters/FieldWindingReactance|FieldWindingReactance]] | o/p | double | Ohms | The reactance of the field windings |
| [[motorcad/parameter_database/parameters/FieldWindingReactance_Ref|FieldWindingReactance_Ref]] | o/p | double | Ohms | The reactance of the field windings referred to the armature |
| [[motorcad/parameter_database/parameters/FieldWindingResistance|FieldWindingResistance]] | o/p | double | Ohms | The resistance of field winding [Ohm] at the field conductor temperature |
| [[motorcad/parameter_database/parameters/FirstOrderDamperCageTransientConstant|FirstOrderDamperCageTransientConstant]] | o/p | double | sec | The first order damper cage transient time constant (Tdd') |
| [[motorcad/parameter_database/parameters/FirstOrderTransientReactance_D|FirstOrderTransientReactance_D]] | o/p | double | Ohms | The first order transient reactance in D axis |
| [[motorcad/parameter_database/parameters/FirstOrderTransientReactance_Q|FirstOrderTransientReactance_Q]] | o/p | double | Ohms | The first order transient reactance in Q axis |
| [[motorcad/parameter_database/parameters/FirstOrderTransientTimeConstant|FirstOrderTransientTimeConstant]] | o/p | double | sec | The first order transient time constant (Td') |
| [[motorcad/parameter_database/parameters/FluxLinkageLoad|FluxLinkageLoad]] | o/p | double | Vs | Average Flux linkage when on load |
| [[motorcad/parameter_database/parameters/FluxLinkageLoadSkew_D|FluxLinkageLoadSkew_D]] | o/p | double | Vs | Average Flux linkage along D axis when on load for skewed machine |
| [[motorcad/parameter_database/parameters/FluxLinkageLoadSkew_Q|FluxLinkageLoadSkew_Q]] | o/p | double | Vs | Average Flux linkage along Q axis when on load for skewed machine |
| [[motorcad/parameter_database/parameters/FluxLinkageLoad_D|FluxLinkageLoad_D]] | o/p | double | Vs | Average Flux linkage along D axis when on load |
| [[motorcad/parameter_database/parameters/FluxLinkageLoad_Q|FluxLinkageLoad_Q]] | o/p | double | Vs | Average Flux linkage along Q axis when on load |
| [[motorcad/parameter_database/parameters/FluxLinkageLookupCalc|FluxLinkageLookupCalc]] | i/p | boolean | N/A | When selected, magnetisation curves are calculated |
| [[motorcad/parameter_database/parameters/FluxLinkageMultiplier_D|FluxLinkageMultiplier_D]] | i/p | double | N/A | Multiplier used to adjust Direct axis flux linkage |
| [[motorcad/parameter_database/parameters/FluxLinkageMultiplier_Q|FluxLinkageMultiplier_Q]] | i/p | double | N/A | Multiplier used to adjust Quadrature axis flux linkage |
| [[motorcad/parameter_database/parameters/FluxLinkageOCSkew_D|FluxLinkageOCSkew_D]] | o/p | double | Vs | Average Flux linkage along D axis when on open circuit for skewed machine |
| [[motorcad/parameter_database/parameters/FluxLinkageOCSkew_Q|FluxLinkageOCSkew_Q]] | o/p | double | Vs | Average Flux linkage along Q axis when on open circuit for skewed machine |
| [[motorcad/parameter_database/parameters/FluxLinkageOC_D|FluxLinkageOC_D]] | o/p | double | Vs | Average Flux linkage along D axis when on open circuit |
| [[motorcad/parameter_database/parameters/FluxLinkageOC_Field|FluxLinkageOC_Field]] | o/p | double | Vs | Average field flux linkage when armature is open circuit |
| [[motorcad/parameter_database/parameters/FluxLinkageOC_Q|FluxLinkageOC_Q]] | o/p | double | Vs | Average Flux linkage along Q axis when on open circuit |
| [[motorcad/parameter_database/parameters/FluxLinkageQAxisCurrentSkew_D|FluxLinkageQAxisCurrentSkew_D]] | o/p | double | Vs | Average Flux linkage along D axis when only Q axis current for skewed machine |
| [[motorcad/parameter_database/parameters/FluxLinkageQAxisCurrentSkew_Q|FluxLinkageQAxisCurrentSkew_Q]] | o/p | double | Vs | Average Flux linkage along Q axis when only Q axis current for skewed machine |
| [[motorcad/parameter_database/parameters/FluxLinkageQAxisCurrent_D|FluxLinkageQAxisCurrent_D]] | o/p | double | Vs | Average Flux linkage along D axis when only Q axis current |
| [[motorcad/parameter_database/parameters/FluxLinkageQAxisCurrent_Q|FluxLinkageQAxisCurrent_Q]] | o/p | double | Vs | Average Flux linkage along Q axis when only Q axis current |
| [[motorcad/parameter_database/parameters/FluxSkewFactor|FluxSkewFactor]] | i/p | double | N/A | Factor applied to the rotor flux when continuous skew is used with harmonics + flux method |
| [[motorcad/parameter_database/parameters/FluxSkewFactorCalc|FluxSkewFactorCalc]] | recommended | boolean | N/A | When selected the flux skew factor is recalculated using multistatic back EMF (for continuous skew) |
| [[motorcad/parameter_database/parameters/ForceExportCycleType|ForceExportCycleType]] | setting | integer | N/A | The force export cycle type either whole mechanical cycle or all force data calculated |
| [[motorcad/parameter_database/parameters/ForceExportFormat|ForceExportFormat]] | setting | integer | N/A | The format of forces export |
| [[motorcad/parameter_database/parameters/ForceExport_DataType|ForceExport_DataType]] | setting | integer | N/A | The forces data type used in force export |
| [[motorcad/parameter_database/parameters/FundamentalFrequency|FundamentalFrequency]] | o/p | double | Hz | The fundamental frequency of machine |
| [[motorcad/parameter_database/parameters/FundamentalWindingFactor|FundamentalWindingFactor]] | o/p | double | N/A | The Fundamental Winding Factor |
| [[motorcad/parameter_database/parameters/FundamentalWindingFactor_Aux|FundamentalWindingFactor_Aux]] | o/p | double | N/A | Aux winding fundamental winding factor |
| [[motorcad/parameter_database/parameters/FundamentalWindingFactor_Unskewed|FundamentalWindingFactor_Unskewed]] | o/p | double | N/A | The Fundamental Winding Factor (without skew effects) |
| [[motorcad/parameter_database/parameters/GeometryMeshEnabled|GeometryMeshEnabled]] | i/p | boolean | N/A | When set to false then the geometry and mesh are not recreated - assumes geometry is same as previous calculation (this should normally be set to true) |
| [[motorcad/parameter_database/parameters/HMins|HMins]] | o/p | double | A/m | Minimum values of H for each magnet |
| [[motorcad/parameter_database/parameters/HairpinPathPattern|HairpinPathPattern]] | i/p | OleStr | N/A | Comma-separated list of elementary paths combined for each custom parallel path e.g. 1,2 |
| [[motorcad/parameter_database/parameters/Hairpin_ChordingPitch|Hairpin_ChordingPitch]] | o/p | integer | N/A | Chording Pitch for Hairpin Windings |
| [[motorcad/parameter_database/parameters/HalbachDefinition|HalbachDefinition]] | compatibility | integer | N/A | Method for setting magnet Br angles for sinusoidal Halbach arrays |
| [[motorcad/parameter_database/parameters/HalbachMagFunction_Method|HalbachMagFunction_Method]] | compatibility | integer | N/A | Method used to define Halbach magnetization functions |
| [[motorcad/parameter_database/parameters/HalbachMagType_AFM|HalbachMagType_AFM]] | i/p | integer | N/A | Type of Halbach magnetization selected for AFM machines |
| [[motorcad/parameter_database/parameters/HalbachMagnetization|HalbachMagnetization]] | i/p | integer | N/A | Type of Halbach magnetization selected |
| [[motorcad/parameter_database/parameters/HalbachMagnetizationBr1Function|HalbachMagnetizationBr1Function]] | i/p | OleStr | N/A | The function definition of a continuous halbach type. |
| [[motorcad/parameter_database/parameters/HalbachMagnetizationBr2Function|HalbachMagnetizationBr2Function]] | i/p | OleStr | N/A | The function definition of a continuous halbach type. |
| [[motorcad/parameter_database/parameters/HarmonicAmplitude_Array|HarmonicAmplitude_Array]] | i/p | double | N/A | Harmonic Amplitude Array |
| [[motorcad/parameter_database/parameters/HarmonicAngle_Array|HarmonicAngle_Array]] | i/p | double | N/A | Harmonic Angle Array |
| [[motorcad/parameter_database/parameters/HarmonicOrder_Array|HarmonicOrder_Array]] | i/p | double | N/A | Harmonic Order Array |
| [[motorcad/parameter_database/parameters/HarmonicView|HarmonicView]] | setting | integer | N/A | Winding Harmonics View (mechanical or electrical)) |
| [[motorcad/parameter_database/parameters/Harmonic_Airgap_Torque|Harmonic_Airgap_Torque]] | o/p | double | Nm | Airgap torque contribution from each harmonic order |
| [[motorcad/parameter_database/parameters/Harmonic_Effective_Speed_Term|Harmonic_Effective_Speed_Term]] | o/p | double | N/A | The effective per unit speed term for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_Effective_Turns_Ratio|Harmonic_Effective_Turns_Ratio]] | o/p | double | N/A | The effective turns ratio for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_MagnetizingReactance_Aux|Harmonic_MagnetizingReactance_Aux]] | o/p | double | Ohms | The aux winding component of the magnetizing reactance for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_MagnetizingReactance_Main|Harmonic_MagnetizingReactance_Main]] | o/p | double | Ohms | The main winding component of the magnetizing reactance for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_MagnetizingVoltage_Aux|Harmonic_MagnetizingVoltage_Aux]] | o/p | double | Volts | The voltage across the aux winding component of the magnetizing reactance for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_MagnetizingVoltage_Main|Harmonic_MagnetizingVoltage_Main]] | o/p | double | Volts | The voltage across the main winding component of the magnetizing reactance for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_Pulsating_Torque|Harmonic_Pulsating_Torque]] | o/p | double | Nm | Pulsating torque contribution from each harmonic order |
| [[motorcad/parameter_database/parameters/Harmonic_RotorBarLoss_Aux|Harmonic_RotorBarLoss_Aux]] | o/p | double | Watts | Losses in rotor bar resistance referred to the aux winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorBarLoss_Main|Harmonic_RotorBarLoss_Main]] | o/p | double | Watts | Losses in rotor bar resistance referred to the main winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorCurrent_Aux|Harmonic_RotorCurrent_Aux]] | o/p | double | Amps | Rotor current referred to the aux winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorCurrent_Main|Harmonic_RotorCurrent_Main]] | o/p | double | Amps | Rotor current referred to the main winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorLeakageReactance_Aux|Harmonic_RotorLeakageReactance_Aux]] | o/p | double | Ohms | Rotor leakage reactance referred to the aux winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorLeakageReactance_Main|Harmonic_RotorLeakageReactance_Main]] | o/p | double | Ohms | Rotor leakage reactance referred to the main winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorLeakageVoltage_Aux|Harmonic_RotorLeakageVoltage_Aux]] | o/p | double | Volts | Voltage across rotor leakage reactance referred to the aux winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorLeakageVoltage_Main|Harmonic_RotorLeakageVoltage_Main]] | o/p | double | Volts | Voltage across rotor leakage reactance referred to the main winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorResistance_Aux|Harmonic_RotorResistance_Aux]] | o/p | double | Ohms | Rotor resistance referred to the aux winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorResistance_Main|Harmonic_RotorResistance_Main]] | o/p | double | Ohms | Rotor resistance referred to the main winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorVoltage_Aux|Harmonic_RotorVoltage_Aux]] | o/p | double | Volts | Voltage drop across rotor resistance referred to the aux winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_RotorVoltage_Main|Harmonic_RotorVoltage_Main]] | o/p | double | Volts | Voltage drop across rotor resistance referred to the main winding for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_Skew_Factor|Harmonic_Skew_Factor]] | o/p | double | N/A | The skew factor for each harmonic order in the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/Harmonic_V2_Aux|Harmonic_V2_Aux]] | o/p | double | Volts | Voltage source V2 (aux winding) (IM1PH stator equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/Harmonic_V2_Main|Harmonic_V2_Main]] | o/p | double | Volts | Voltage source V2 (main winding) (IM1PH stator equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/Harmonic_V3_Aux|Harmonic_V3_Aux]] | o/p | double | Volts | Voltage source V3 (aux winding) (IM1PH rotor equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/Harmonic_V3_Main|Harmonic_V3_Main]] | o/p | double | Volts | Voltage source V3 (main winding) (IM1PH rotor equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/Harmonic_V4_Aux|Harmonic_V4_Aux]] | o/p | double | Volts | Voltage source V4 (aux winding) (IM1PH rotor equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/Harmonic_V4_Main|Harmonic_V4_Main]] | o/p | double | Volts | Voltage source V4 (main winding) (IM1PH rotor equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/Harmonic_V5_Aux|Harmonic_V5_Aux]] | o/p | double | Volts | Voltage source V5 (aux winding) (IM1PH rotor equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/Harmonic_V5_Main|Harmonic_V5_Main]] | o/p | double | Volts | Voltage source V5 (main winding) (IM1PH rotor equivalent circuit) (for each harmonic order) |
| [[motorcad/parameter_database/parameters/HousingLoss_Eddy|HousingLoss_Eddy]] | o/p | double | Watts | Housingn losses from eddy currents |
| [[motorcad/parameter_database/parameters/HousingLoss_Eddy_Adj|HousingLoss_Eddy_Adj]] | o/p | double | Watts | Housing losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/HousingLoss_Eddy_Adj_OC|HousingLoss_Eddy_Adj_OC]] | o/p | double | Watts | Housing losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/HousingLoss_Eddy_OC|HousingLoss_Eddy_OC]] | o/p | double | Watts | Housing losses from eddy currents |
| [[motorcad/parameter_database/parameters/HousingLoss_Excess|HousingLoss_Excess]] | o/p | double | Watts | Housing excess losses |
| [[motorcad/parameter_database/parameters/HousingLoss_Excess_OC|HousingLoss_Excess_OC]] | o/p | double | Watts | Housing excess losses |
| [[motorcad/parameter_database/parameters/HousingLoss_Fundamental_Hys|HousingLoss_Fundamental_Hys]] | o/p | double | Watts | Housing losses from hysteresis |
| [[motorcad/parameter_database/parameters/HousingLoss_Fundamental_Hys_OC|HousingLoss_Fundamental_Hys_OC]] | o/p | double | Watts | Housing losses from fundamental frequency hysteresis |
| [[motorcad/parameter_database/parameters/HousingLoss_Hys|HousingLoss_Hys]] | o/p | double | Watts | Housing losses from hysteresis |
| [[motorcad/parameter_database/parameters/HousingLoss_Hys_Adj|HousingLoss_Hys_Adj]] | o/p | double | Watts | Housing losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/HousingLoss_Hys_Adj_OC|HousingLoss_Hys_Adj_OC]] | o/p | double | Watts | Housing losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/HousingLoss_Hys_OC|HousingLoss_Hys_OC]] | o/p | double | Watts | Housing losses from hysteresis |
| [[motorcad/parameter_database/parameters/HousingLoss_Minor_Hys|HousingLoss_Minor_Hys]] | o/p | double | Watts | Housing losses from hysteresis |
| [[motorcad/parameter_database/parameters/HousingLoss_Minor_Hys_OC|HousingLoss_Minor_Hys_OC]] | o/p | double | Watts | Housing losses from minor loops hysteresis |
| [[motorcad/parameter_database/parameters/HousingLoss_Total|HousingLoss_Total]] | o/p | double | Watts | Total Housing losses |
| [[motorcad/parameter_database/parameters/HousingLoss_Total_Adj|HousingLoss_Total_Adj]] | o/p | double | Watts | Housing losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/HousingLoss_Total_Adj_OC|HousingLoss_Total_Adj_OC]] | o/p | double | Watts | Housing losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/HousingLoss_Total_OC|HousingLoss_Total_OC]] | o/p | double | Watts | Total Housing losses |
| [[motorcad/parameter_database/parameters/HousingOverhangFactor|HousingOverhangFactor]] | i/p | double | N/A | The overhang adjustment factor applied to the B values of the housing material. |
| [[motorcad/parameter_database/parameters/Housing_Resistivity|Housing_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the Housing at Housing temperature |
| [[motorcad/parameter_database/parameters/Housing_ResistivityAt20C|Housing_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the Housing at reference temperature |
| [[motorcad/parameter_database/parameters/Housing_Temperature|Housing_Temperature]] | i/p | double | °C | The temperature of the Housing used for loss calculation |
| [[motorcad/parameter_database/parameters/HysteresisLossBuildFactor|HysteresisLossBuildFactor]] | i/p | double | N/A | Multiplier used to adjust iron hysteresis losses |
| [[motorcad/parameter_database/parameters/IM1PHEquivalentCircuitSolverMethod|IM1PHEquivalentCircuitSolverMethod]] | i/p | integer | N/A | Method used to solve the IM1PH equivalent circuit |
| [[motorcad/parameter_database/parameters/IM1PH_AuxCapacitorVoltage|IM1PH_AuxCapacitorVoltage]] | o/p | double | Volts | Voltage drop over auxiliary circuit capacitor |
| [[motorcad/parameter_database/parameters/IM1PH_AuxImpedance|IM1PH_AuxImpedance]] | o/p | double | Ohms | Total impedance of auxiliary circuit |
| [[motorcad/parameter_database/parameters/IM1PH_AuxReactance|IM1PH_AuxReactance]] | o/p | double | Ohms | Reactance of auxiliary circuit capacitor |
| [[motorcad/parameter_database/parameters/IM1PH_AuxResistorLoss|IM1PH_AuxResistorLoss]] | o/p | double | Watts | Power loss dissipated in auxiliary circuit resistor |
| [[motorcad/parameter_database/parameters/IM1PH_AuxResistorVoltage|IM1PH_AuxResistorVoltage]] | o/p | double | Volts | Voltage drop over auxiliary circuit resistor |
| [[motorcad/parameter_database/parameters/IM1PH_Motor_Type|IM1PH_Motor_Type]] | i/p | integer | N/A | Type of single-phase induction motor |
| [[motorcad/parameter_database/parameters/IM1PH_NumHarmonicOrders|IM1PH_NumHarmonicOrders]] | i/p | integer | N/A | Number of harmonic orders used in equivalent circuit solution |
| [[motorcad/parameter_database/parameters/IM1PH_Run_Capacitance|IM1PH_Run_Capacitance]] | i/p | double | Farad | Running Capacitance for IM1PH |
| [[motorcad/parameter_database/parameters/IM1PH_Run_Reactance|IM1PH_Run_Reactance]] | o/p | double | Ohms | Running Reactance for IM1PH |
| [[motorcad/parameter_database/parameters/IM1PH_Run_Resistance|IM1PH_Run_Resistance]] | i/p | double | Ohms | Running Resistance for IM1PH |
| [[motorcad/parameter_database/parameters/IM1PH_Start_Capacitance|IM1PH_Start_Capacitance]] | i/p | double | Farad | Starting Capacitance for IM1PH |
| [[motorcad/parameter_database/parameters/IM1PH_Start_Reactance|IM1PH_Start_Reactance]] | o/p | double | Ohms | Starting Reactance for IM1PH |
| [[motorcad/parameter_database/parameters/IM1PH_Start_Resistance|IM1PH_Start_Resistance]] | i/p | double | Ohms | Starting Resistance for IM1PH |
| [[motorcad/parameter_database/parameters/IM1PH_Starting_ControlStrategy|IM1PH_Starting_ControlStrategy]] | i/p | integer | N/A | Control strategy used to switch from start to run impedances |
| [[motorcad/parameter_database/parameters/IM1PH_Starting_CutoffSlip|IM1PH_Starting_CutoffSlip]] | o/p | double | N/A | Slip at which the cutoff switch is activated |
| [[motorcad/parameter_database/parameters/IM1PH_Starting_CutoffSpeed|IM1PH_Starting_CutoffSpeed]] | i/p | double | rpm | Speed at which the cutoff switch is activated |
| [[motorcad/parameter_database/parameters/IMAccelerationCalc|IMAccelerationCalc]] | i/p | boolean | N/A | When selected Induction machine acceleration calculation is run |
| [[motorcad/parameter_database/parameters/IMAccelerationDuration|IMAccelerationDuration]] | i/p | double | sec | The duration of the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMAccelerationFanInertia|IMAccelerationFanInertia]] | i/p | double | p.u. | The per unit inertia of the fan relative to the rotor inertia in the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMAccelerationLoadInertia|IMAccelerationLoadInertia]] | i/p | double | p.u. | The per unit inertia of the load relative to the rotor inertia in the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMAccelerationLoadTorqueAt0rpm|IMAccelerationLoadTorqueAt0rpm]] | i/p | double | Nm | The load torque at 0 rpm for the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMAccelerationLoadTorqueAtRpm|IMAccelerationLoadTorqueAtRpm]] | i/p | double | Nm | The load torque at specified rpm for the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMAccelerationLoadTorqueCoef|IMAccelerationLoadTorqueCoef]] | i/p | double | rpm | The coefficient for the load torque point the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMAccelerationLoadTorqueRpmRef|IMAccelerationLoadTorqueRpmRef]] | i/p | double | rpm | The specified rpm for the load torque point the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMAccelerationPoints|IMAccelerationPoints]] | i/p | integer | N/A | The number of points in the IM acceleration calculation |
| [[motorcad/parameter_database/parameters/IMApparentPower|IMApparentPower]] | o/p | double | VA | The apparent power |
| [[motorcad/parameter_database/parameters/IMBGapUnsaturated|IMBGapUnsaturated]] | o/p | double | Tesla | Flux density in airgap (unsaturated) at a position of 0 electrical degrees |
| [[motorcad/parameter_database/parameters/IMBreakdownPointAnalyticCalc|IMBreakdownPointAnalyticCalc]] | i/p | boolean | N/A | When selected Induction machine breakdown point analytic calculation is run |
| [[motorcad/parameter_database/parameters/IMBreakdown_ActivePower_Input|IMBreakdown_ActivePower_Input]] | o/p | double | Watts | The breakdown active power input |
| [[motorcad/parameter_database/parameters/IMBreakdown_ActivePower_Output|IMBreakdown_ActivePower_Output]] | o/p | double | Watts | The breakdown active power output |
| [[motorcad/parameter_database/parameters/IMBreakdown_RMSCurrent_Line|IMBreakdown_RMSCurrent_Line]] | o/p | double | Amps | The breakdown rms line current |
| [[motorcad/parameter_database/parameters/IMBreakdown_RMSCurrent_Phase|IMBreakdown_RMSCurrent_Phase]] | o/p | double | Amps | The breakdown rms phase current |
| [[motorcad/parameter_database/parameters/IMBreakdown_RMSVoltage_Line|IMBreakdown_RMSVoltage_Line]] | o/p | double | Volts | The breakdown rms line voltage |
| [[motorcad/parameter_database/parameters/IMBreakdown_RMSVoltage_Phase|IMBreakdown_RMSVoltage_Phase]] | o/p | double | Volts | The breakdown rms phase voltage |
| [[motorcad/parameter_database/parameters/IMBreakdown_ShaftTorque|IMBreakdown_ShaftTorque]] | o/p | double | Nm | The Breakdown shaft torque |
| [[motorcad/parameter_database/parameters/IMBreakdown_Slip|IMBreakdown_Slip]] | o/p | double | p.u. | The Breakdown slip |
| [[motorcad/parameter_database/parameters/IMBreakdown_Speed|IMBreakdown_Speed]] | o/p | double | rpm | The Breakdown speed |
| [[motorcad/parameter_database/parameters/IMBreakdown_StrayLoadLoss|IMBreakdown_StrayLoadLoss]] | o/p | double | Watts | The breakdown stray load loss |
| [[motorcad/parameter_database/parameters/IMBreakdown_Torque|IMBreakdown_Torque]] | o/p | double | Nm | The Breakdown airgap torque |
| [[motorcad/parameter_database/parameters/IMCalibratedLookupDataEnabled|IMCalibratedLookupDataEnabled]] | i/p | boolean | N/A | Whether calibrated IM analytic lookup data is used |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_L1|IMCalibrationFactor_L1]] | i/p | double | N/A | Array of stator leakage inductance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_L1_Points|IMCalibrationFactor_L1_Points]] | i/p | integer | N/A | Number of points for which the stator leakage inductance calibration factor is defined |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_L1_Speed|IMCalibrationFactor_L1_Speed]] | i/p | double | rpm | Speeds associated with the stator leakage inductance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_L2|IMCalibrationFactor_L2]] | i/p | double | N/A | Array of rotor leakage inductance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_L2_Points|IMCalibrationFactor_L2_Points]] | i/p | integer | N/A | Number of points for which the rotor leakage inductance calibration factor is defined |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_L2_Speed|IMCalibrationFactor_L2_Speed]] | i/p | double | rpm | Speeds associated with the rotor leakage inductance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_Lm|IMCalibrationFactor_Lm]] | i/p | double | N/A | Array of magnetizing inductance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_Lm_Current|IMCalibrationFactor_Lm_Current]] | i/p | double | Amps | Magnetizing currents associated with the magnetizing inductance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_Lm_Points|IMCalibrationFactor_Lm_Points]] | i/p | integer | N/A | Number of points for which the magnetizing inductance calibration factor is defined |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_R2|IMCalibrationFactor_R2]] | i/p | double | N/A | Array of referred rotor resistance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_R2_Points|IMCalibrationFactor_R2_Points]] | i/p | integer | N/A | Number of points for which the referred rotor resistance calibration factor is defined |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_R2_Speed|IMCalibrationFactor_R2_Speed]] | i/p | double | rpm | Speeds associated with the referred rotor resistance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_Rfe|IMCalibrationFactor_Rfe]] | i/p | double | N/A | Array of core loss resistance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_Rfe_BackEMF|IMCalibrationFactor_Rfe_BackEMF]] | i/p | double | Volts | Back EMFs associated with the core loss resistance calibration factors |
| [[motorcad/parameter_database/parameters/IMCalibrationFactor_Rfe_Points|IMCalibrationFactor_Rfe_Points]] | i/p | integer | N/A | Number of points for which the magnetizing core loss resistance calibration factor is defined |
| [[motorcad/parameter_database/parameters/IMCircuitCyclesAtEachAverage|IMCircuitCyclesAtEachAverage]] | i/p | integer | N/A | When averaging in equivalent circuit solver, the number of cycles for which the solver will run before increasing the number in average |
| [[motorcad/parameter_database/parameters/IMCircuitIterationsBeforeAverage|IMCircuitIterationsBeforeAverage]] | i/p | integer | N/A | Number of iterations used in equivalent circuit solver before averaging is used |
| [[motorcad/parameter_database/parameters/IMCircuitMaxIterationsInAverage|IMCircuitMaxIterationsInAverage]] | i/p | integer | N/A | When averaging in equivalent circuit solver, maximum number of iteration steps to average over |
| [[motorcad/parameter_database/parameters/IMCoreLossCalc|IMCoreLossCalc]] | i/p | boolean | N/A | When selected Induction machine no load synchronous speed core loss calculation is run |
| [[motorcad/parameter_database/parameters/IMCoreLossResistance_Analytic|IMCoreLossResistance_Analytic]] | o/p | double | Ohms | The core loss equivalent resistance (Analytic on load) |
| [[motorcad/parameter_database/parameters/IMCoreLossResistance_L|IMCoreLossResistance_L]] | o/p | double | Ohms | The core loss equivalent resistance (L-circuit) |
| [[motorcad/parameter_database/parameters/IMCoreLossResistance_Static|IMCoreLossResistance_Static]] | o/p | double | Ohms | The core loss equivalent resistance in the no load case |
| [[motorcad/parameter_database/parameters/IMCoreLoss_CurrentProp|IMCoreLoss_CurrentProp]] | i/p | double | N/A | The proportions of current used in core loss calculation |
| [[motorcad/parameter_database/parameters/IMCoreLoss_Points|IMCoreLoss_Points]] | i/p | integer | N/A | Number of different current values used in core loss calculation |
| [[motorcad/parameter_database/parameters/IMDoubleRotorCageCalcMethod|IMDoubleRotorCageCalcMethod]] | compatibility | integer | N/A | Selects the calculation that is used for rotor cage parameters when there is a second bar present |
| [[motorcad/parameter_database/parameters/IMDriveFrequency|IMDriveFrequency]] | i/p | double | Hz | The drive frequency |
| [[motorcad/parameter_database/parameters/IMEquivCircMultipliersDefinition|IMEquivCircMultipliersDefinition]] | setting | integer | N/A | Whether equivalent circuit multipliers are specified as a constant or calibrated value |
| [[motorcad/parameter_database/parameters/IMEquivalentCircuitAveragingMethod|IMEquivalentCircuitAveragingMethod]] | i/p | integer | N/A | Method of averaging results in equivalent circuit solver |
| [[motorcad/parameter_database/parameters/IMEquivalentCircuitError|IMEquivalentCircuitError]] | o/p | double | N/A | Final error (%) in iterative equivalent circuit solver |
| [[motorcad/parameter_database/parameters/IMEquivalentCircuitHarmonicOrders|IMEquivalentCircuitHarmonicOrders]] | i/p | integer | N/A | Harmonic orders included in equivalent circuit solution |
| [[motorcad/parameter_database/parameters/IMEquivalentCircuitIterations|IMEquivalentCircuitIterations]] | o/p | integer | N/A | Number of iterations used in equivalent circuit solver |
| [[motorcad/parameter_database/parameters/IMEquivalentCircuitMaxIterations|IMEquivalentCircuitMaxIterations]] | i/p | integer | N/A | Maximum number of iterations allowed in equivalent circuit solver |
| [[motorcad/parameter_database/parameters/IMEquivalentCircuitTolerance|IMEquivalentCircuitTolerance]] | i/p | double | N/A | Maximum error (%) allowed in iterative equivalent circuit solver |
| [[motorcad/parameter_database/parameters/IMFlux_ErrorMax|IMFlux_ErrorMax]] | o/p | double | N/A | Maximum convergence error in magnetic flux density calculation (IM) |
| [[motorcad/parameter_database/parameters/IMFlux_Iterations|IMFlux_Iterations]] | o/p | integer | N/A | Number of iterations to calculate magnetic flux density (IM) |
| [[motorcad/parameter_database/parameters/IMInductance_CurrentProp|IMInductance_CurrentProp]] | i/p | double | N/A | The proportions of current used in inductance calculation |
| [[motorcad/parameter_database/parameters/IMInductance_PeakCurrent|IMInductance_PeakCurrent]] | o/p | double | Amps | The peak current values used for inductance calculation |
| [[motorcad/parameter_database/parameters/IMInductance_Points|IMInductance_Points]] | i/p | integer | N/A | Number of different current values used in inductance calculation |
| [[motorcad/parameter_database/parameters/IMInitialSaturationFactor|IMInitialSaturationFactor]] | i/p | double | N/A | Initial Saturation Factor |
| [[motorcad/parameter_database/parameters/IMKRotor|IMKRotor]] | o/p | double | N/A | K Rotor |
| [[motorcad/parameter_database/parameters/IMLeakageInductance_Stator|IMLeakageInductance_Stator]] | o/p | double | Henry | The slot leakage inductance |
| [[motorcad/parameter_database/parameters/IMLockedRotorAnalyticCalc|IMLockedRotorAnalyticCalc]] | i/p | boolean | N/A | When selected Induction machine locked rotor analytic calculation is run |
| [[motorcad/parameter_database/parameters/IMLockedRotorCalc|IMLockedRotorCalc]] | i/p | boolean | N/A | When selected Induction machine locked rotor FEA calculation is run |
| [[motorcad/parameter_database/parameters/IMLockedRotor_AvTorque|IMLockedRotor_AvTorque]] | o/p | double | Nm | The average of virtual work and Maxwell stress torque in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_DqTorque|IMLockedRotor_DqTorque]] | o/p | double | Nm | The flux linkage torque in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_Frequency|IMLockedRotor_Frequency]] | o/p | double | Hz | The drive frequency values used in Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_MSTorque|IMLockedRotor_MSTorque]] | o/p | double | Nm | The Maxwell stress torque in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_ParallelEquivInductance|IMLockedRotor_ParallelEquivInductance]] | o/p | double | Henry | The equivalent inductance in parallel circuit in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_ParallelEquivResistance|IMLockedRotor_ParallelEquivResistance]] | o/p | double | Ohms | The equivalent resistance in parallel circuit in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_PeakCurrent|IMLockedRotor_PeakCurrent]] | o/p | double | Amps | The peak current used for the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_PhaseInductance|IMLockedRotor_PhaseInductance]] | o/p | double | Henry | The phase inductance used in the locked rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_Power_Input|IMLockedRotor_Power_Input]] | o/p | double | Watts | The locked rotor input power |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RMSCurrent_Line|IMLockedRotor_RMSCurrent_Line]] | o/p | double | Amps | The locked rotor rms line current |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RMSCurrent_Phase|IMLockedRotor_RMSCurrent_Phase]] | o/p | double | Amps | The locked rotor rms phase current |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RMSVoltage_Line|IMLockedRotor_RMSVoltage_Line]] | o/p | double | Volts | The locked rotor rms line voltage |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RMSVoltage_Phase|IMLockedRotor_RMSVoltage_Phase]] | o/p | double | Volts | The locked rotor rms phase voltage |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RotorBarLeakageInductance_Ref|IMLockedRotor_RotorBarLeakageInductance_Ref]] | o/p | double | Henry | The referred rotor bar leakage inductance in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RotorBarLosses|IMLockedRotor_RotorBarLosses]] | o/p | double | Watts | The core loss resistance calculated in Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RotorBarResistance_Ref|IMLockedRotor_RotorBarResistance_Ref]] | o/p | double | Ohms | The referred rotor bar resistance in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RotorLeakageInductance_Ref|IMLockedRotor_RotorLeakageInductance_Ref]] | o/p | double | Henry | The referred rotor leakage inductance in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_RotorResistance_Ref|IMLockedRotor_RotorResistance_Ref]] | o/p | double | Ohms | The referred rotor resistance in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_SeriesEquivInductance|IMLockedRotor_SeriesEquivInductance]] | o/p | double | Henry | The equivalent inductance in series circuit in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_SeriesEquivResistance|IMLockedRotor_SeriesEquivResistance]] | o/p | double | Ohms | The equivalent resistance in series circuit in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_StoredMagneticCoenergy|IMLockedRotor_StoredMagneticCoenergy]] | o/p | double | J | The stored magnetic coenergy in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_StoredMagneticEnergy|IMLockedRotor_StoredMagneticEnergy]] | o/p | double | J | The stored magnetic energy in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLockedRotor_Torque|IMLockedRotor_Torque]] | o/p | double | Nm | The Locked rotor airgap torque |
| [[motorcad/parameter_database/parameters/IMLockedRotor_VWTorque|IMLockedRotor_VWTorque]] | o/p | double | Nm | The virtual work torque in the Locked Rotor case |
| [[motorcad/parameter_database/parameters/IMLookupMethod|IMLookupMethod]] | compatibility | integer | N/A | Whether Emag IM saturation model uses magnetizing inductance or reactance |
| [[motorcad/parameter_database/parameters/IMLookup_ExtensionFactor|IMLookup_ExtensionFactor]] | i/p | double | N/A | Factor to estimate max magnetizing current for voltage driven machines |
| [[motorcad/parameter_database/parameters/IMLookup_Imag|IMLookup_Imag]] | i/p | double | Amps | The magnetizing current used to calculate the IM saturation model |
| [[motorcad/parameter_database/parameters/IMLookup_LastExtensionFactor|IMLookup_LastExtensionFactor]] | i/p | double | N/A | Extension factor from last completed saturation model calculation |
| [[motorcad/parameter_database/parameters/IMLookup_Magnetizing_Inductance|IMLookup_Magnetizing_Inductance]] | i/p | double | Henry | The magnetizing inductance calculated in the IM saturation model |
| [[motorcad/parameter_database/parameters/IMLookup_Magnetizing_Reactance|IMLookup_Magnetizing_Reactance]] | i/p | double | Henry | The magnetizing reactance calculated in the IM saturation model |
| [[motorcad/parameter_database/parameters/IMLookup_MaxImagRequired|IMLookup_MaxImagRequired]] | o/p | double | Amps | Maximum magnetizing current encountered in magnetic calculation |
| [[motorcad/parameter_database/parameters/IMLookup_Phase_Inductance|IMLookup_Phase_Inductance]] | i/p | double | Henry | The phase inductance calculated in the IM FEA saturation model |
| [[motorcad/parameter_database/parameters/IMLookup_SaturationFactor|IMLookup_SaturationFactor]] | i/p | double | N/A | The saturation factor calculated in the IM saturation model |
| [[motorcad/parameter_database/parameters/IMLookup_StatorLeakageInductance|IMLookup_StatorLeakageInductance]] | i/p | double | Henry | The stator leakage inductance calculated in the IM FEA saturation model |
| [[motorcad/parameter_database/parameters/IMMagneticAxialLength|IMMagneticAxialLength]] | o/p | double | mm | The magnetic length of induction machine taking into account stacking factors, stator and rotor lamination lengths |
| [[motorcad/parameter_database/parameters/IMMaxPeakCurrent_SaturationCalc|IMMaxPeakCurrent_SaturationCalc]] | i/p | double | Amps | Maximum Peak Current for Saturation Model Calculation |
| [[motorcad/parameter_database/parameters/IMMaxPeakVoltage_Calibration|IMMaxPeakVoltage_Calibration]] | i/p | double | Volts | Maximum peak voltage for calibration calculations |
| [[motorcad/parameter_database/parameters/IMMaxPeakVoltage_SaturationCalc|IMMaxPeakVoltage_SaturationCalc]] | i/p | double | Volts | Maximum Peak Voltage for Saturation Model Calculation |
| [[motorcad/parameter_database/parameters/IMMaxRMSCurrent_SaturationCalc|IMMaxRMSCurrent_SaturationCalc]] | i/p | double | Amps | Maximum RMS Current for Saturation Model Calculation |
| [[motorcad/parameter_database/parameters/IMMaxRMSVoltage_Calibration|IMMaxRMSVoltage_Calibration]] | i/p | double | Volts | Maximum RMS voltage for calibration calculations |
| [[motorcad/parameter_database/parameters/IMMaxRMSVoltage_SaturationCalc|IMMaxRMSVoltage_SaturationCalc]] | i/p | double | Volts | Maximum RMS Voltage for Saturation Model Calculation |
| [[motorcad/parameter_database/parameters/IMNoLoadAnalyticCalc|IMNoLoadAnalyticCalc]] | i/p | boolean | N/A | When selected Induction machine no load analytic calculation is run |
| [[motorcad/parameter_database/parameters/IMNoLoadInducedVoltage|IMNoLoadInducedVoltage]] | o/p | double | Volts | Induced Voltage (no load) |
| [[motorcad/parameter_database/parameters/IMNoLoadInducedVoltage_Aux|IMNoLoadInducedVoltage_Aux]] | o/p | double | Volts | Induced Voltage (Aux) (no load) |
| [[motorcad/parameter_database/parameters/IMNoLoadIronLoss|IMNoLoadIronLoss]] | o/p | double | Watts | The total machine iron losses for No Load case |
| [[motorcad/parameter_database/parameters/IMNoLoadMagnetizingCurrent|IMNoLoadMagnetizingCurrent]] | o/p | double | Amps | Magnetizing Current (no load) |
| [[motorcad/parameter_database/parameters/IMNoLoadMagnetizingCurrent_Aux|IMNoLoadMagnetizingCurrent_Aux]] | o/p | double | Amps | The no-load magnetizing current in aux winding circuit |
| [[motorcad/parameter_database/parameters/IMNoLoadMagnetizingInductanceSaturated|IMNoLoadMagnetizingInductanceSaturated]] | o/p | double | Henry | The Magnetizing Inductance (including any skewing effects) (no load) |
| [[motorcad/parameter_database/parameters/IMNoLoadMagnetizingInductanceSaturated_Aux|IMNoLoadMagnetizingInductanceSaturated_Aux]] | o/p | double | Henry | The magnetizing inductance (no load) (aux winding) |
| [[motorcad/parameter_database/parameters/IMNoLoadMagnetizingReactanceSaturated|IMNoLoadMagnetizingReactanceSaturated]] | o/p | double | Ohms | The saturated Magnetizing Reactance (including any skewing effects) (no load) |
| [[motorcad/parameter_database/parameters/IMNoLoadMagnetizingReactanceSaturated_Aux|IMNoLoadMagnetizingReactanceSaturated_Aux]] | o/p | double | Henry | The magnetizing reactance (no load) (aux winding) |
| [[motorcad/parameter_database/parameters/IMNoLoadRMSBackEMF|IMNoLoadRMSBackEMF]] | o/p | double | Volts | The RMS back EMF for No Load case |
| [[motorcad/parameter_database/parameters/IMNoLoadSaturationFactor|IMNoLoadSaturationFactor]] | o/p | double | N/A | The saturation factor (no load) |
| [[motorcad/parameter_database/parameters/IMNoLoadSaturationFactor_Aux|IMNoLoadSaturationFactor_Aux]] | o/p | double | N/A | The saturation factor (no load) (aux winding) |
| [[motorcad/parameter_database/parameters/IMNoLoadStatorLeakageReactance_Total|IMNoLoadStatorLeakageReactance_Total]] | o/p | double | Ohms | The total stator leakage reactance (no load) |
| [[motorcad/parameter_database/parameters/IMNoLoad_ActivePower_Input|IMNoLoad_ActivePower_Input]] | o/p | double | Watts | The no load active power input |
| [[motorcad/parameter_database/parameters/IMNoLoad_PeakPhaseCurrent|IMNoLoad_PeakPhaseCurrent]] | o/p | double | Amps | The no load peak phase current |
| [[motorcad/parameter_database/parameters/IMNoLoad_Psi_m|IMNoLoad_Psi_m]] | o/p | double | Vs | The machine flux linkage value value calculated for No Load case |
| [[motorcad/parameter_database/parameters/IMNoLoad_Psi_m_D|IMNoLoad_Psi_m_D]] | o/p | double | Vs | The machine D axis flux linkage value value calculated for No Load case |
| [[motorcad/parameter_database/parameters/IMNoLoad_Psi_m_Q|IMNoLoad_Psi_m_Q]] | o/p | double | Vs | The machine Q axis flux linkage value value calculated for No Load case |
| [[motorcad/parameter_database/parameters/IMNoLoad_RC|IMNoLoad_RC]] | o/p | double | Ohms | The core loss resistance calculated in No Load case |
| [[motorcad/parameter_database/parameters/IMNoLoad_RMSCurrent|IMNoLoad_RMSCurrent]] | o/p | double | Amps | The rms current values used for the no load calculation |
| [[motorcad/parameter_database/parameters/IMNoLoad_RMSCurrent_Line|IMNoLoad_RMSCurrent_Line]] | o/p | double | Amps | The no load rms line current |
| [[motorcad/parameter_database/parameters/IMNoLoad_RMSCurrent_Phase|IMNoLoad_RMSCurrent_Phase]] | o/p | double | Amps | The no load rms phase current |
| [[motorcad/parameter_database/parameters/IMNoLoad_RMSVoltage_Line|IMNoLoad_RMSVoltage_Line]] | o/p | double | Volts | The no load rms line voltage |
| [[motorcad/parameter_database/parameters/IMNoLoad_RMSVoltage_Phase|IMNoLoad_RMSVoltage_Phase]] | o/p | double | Volts | The no load rms phase voltage |
| [[motorcad/parameter_database/parameters/IMNoLoad_SaturationFactor|IMNoLoad_SaturationFactor]] | o/p | double | N/A | The saturation factors used for the No Load case |
| [[motorcad/parameter_database/parameters/IMOnLoadPower_User|IMOnLoadPower_User]] | i/p | double | Watts | The on load power that user has requested |
| [[motorcad/parameter_database/parameters/IMOnLoadTorque_User|IMOnLoadTorque_User]] | i/p | double | Nm | The on load torque that user has requested |
| [[motorcad/parameter_database/parameters/IMOnLoad_AverageTorque|IMOnLoad_AverageTorque]] | o/p | double | Nm | The on load airgap torque (neglecting drag losses) |
| [[motorcad/parameter_database/parameters/IMOnLoad_EnergyConversionVoltage_Ref_L|IMOnLoad_EnergyConversionVoltage_Ref_L]] | o/p | double | Volts | The on load rms equivalent energy conversion voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_EnergyConversionVoltage_Ref_T|IMOnLoad_EnergyConversionVoltage_Ref_T]] | o/p | double | Volts | The on load rms equivalent energy conversion voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_InputActivePower|IMOnLoad_InputActivePower]] | o/p | double | Watts | The ideal on load input active power |
| [[motorcad/parameter_database/parameters/IMOnLoad_InputReactivePower|IMOnLoad_InputReactivePower]] | o/p | double | VA | The on load input reactive power |
| [[motorcad/parameter_database/parameters/IMOnLoad_IronLosses|IMOnLoad_IronLosses]] | o/p | double | Watts | The on load iron losses from FEA calculations |
| [[motorcad/parameter_database/parameters/IMOnLoad_IronLosses_Analytic|IMOnLoad_IronLosses_Analytic]] | o/p | double | Watts | The on load iron losses (analytic calculation) |
| [[motorcad/parameter_database/parameters/IMOnLoad_IronLosses_Static|IMOnLoad_IronLosses_Static]] | o/p | double | Watts | The on load iron losses (initial static solution) |
| [[motorcad/parameter_database/parameters/IMOnLoad_PhaseFluxLinkage_D|IMOnLoad_PhaseFluxLinkage_D]] | o/p | double | Volts | The on load d axis flux linkage per second |
| [[motorcad/parameter_database/parameters/IMOnLoad_PhaseFluxLinkage_Q|IMOnLoad_PhaseFluxLinkage_Q]] | o/p | double | Volts | The on load q axis flux linkage per second |
| [[motorcad/parameter_database/parameters/IMOnLoad_PowerBalance|IMOnLoad_PowerBalance]] | o/p | double | Watts | The on load input active power from the power balance |
| [[motorcad/parameter_database/parameters/IMOnLoad_PowerFactor|IMOnLoad_PowerFactor]] | o/p | double | N/A | The on load power factor from the phasors |
| [[motorcad/parameter_database/parameters/IMOnLoad_PowerFactor_Balance|IMOnLoad_PowerFactor_Balance]] | o/p | double | N/A | The on load power factor from the power balance |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSCoreLossCurrent_L|IMOnLoad_RMSCoreLossCurrent_L]] | o/p | double | Amps | The on load rms core loss current in L circuit |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSCoreLossCurrent_T|IMOnLoad_RMSCoreLossCurrent_T]] | o/p | double | Amps | The on load rms core loss current in T circuit |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSEndRingCurrent|IMOnLoad_RMSEndRingCurrent]] | o/p | double | Amps | The rms on load endring current (from Equivalent circuit) |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSLineBackEMF_L|IMOnLoad_RMSLineBackEMF_L]] | o/p | double | Volts | The rms back emf in L equivalent circuit across all the stator flux impedances |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSLineBackEMF_T|IMOnLoad_RMSLineBackEMF_T]] | o/p | double | Volts | The rms back emf in T equivalent circuit across the magnetizing reactance |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSLineCurrent|IMOnLoad_RMSLineCurrent]] | o/p | double | Amps | The on load rms stator line current |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSMagnetizingCurrent|IMOnLoad_RMSMagnetizingCurrent]] | o/p | double | Amps | The on load rms magnetizing current |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSMagnetizingCurrent_Alt|IMOnLoad_RMSMagnetizingCurrent_Alt]] | o/p | double | Amps | The on load rms magnetizing current (alternative calculation method) |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSMagnetizingCurrent_L|IMOnLoad_RMSMagnetizingCurrent_L]] | o/p | double | Amps | The on load rms magnetizing current |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSPhaseBackEMF_L|IMOnLoad_RMSPhaseBackEMF_L]] | o/p | double | Volts | The rms back emf in L equivalent circuit across all the stator flux impedances |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSPhaseBackEMF_T|IMOnLoad_RMSPhaseBackEMF_T]] | o/p | double | Volts | The rms back emf in T equivalent circuit across the magnetizing reactance |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSPhaseCurrent|IMOnLoad_RMSPhaseCurrent]] | o/p | double | Amps | The on load rms stator phase current |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSRotorBarCurrent|IMOnLoad_RMSRotorBarCurrent]] | o/p | double | Amps | The rms on load rotor bar current (from Equivalent circuit) |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSRotorCurrent|IMOnLoad_RMSRotorCurrent]] | o/p | double | Amps | The referred rms on load rotor current (from losses) |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSRotorCurrent_Referred|IMOnLoad_RMSRotorCurrent_Referred]] | o/p | double | Amps | The referred rms on load rotor current (T circuit) |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSRotorCurrent_Referred_L|IMOnLoad_RMSRotorCurrent_Referred_L]] | o/p | double | Amps | The referred rms on load rotor current (from Equivalent circuit) |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSRotorLeakageVoltage|IMOnLoad_RMSRotorLeakageVoltage]] | o/p | double | Volts | The on load rms rotor leakage voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSRotorLeakageVoltage_L|IMOnLoad_RMSRotorLeakageVoltage_L]] | o/p | double | Volts | The on load rms rotor leakage voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSStatorLeakageVoltage_L|IMOnLoad_RMSStatorLeakageVoltage_L]] | o/p | double | Volts | The on load rms stator leakage voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSStatorLeakageVoltage_T|IMOnLoad_RMSStatorLeakageVoltage_T]] | o/p | double | Volts | The on load rms stator leakage voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSStatorTerminalLineVoltage|IMOnLoad_RMSStatorTerminalLineVoltage]] | o/p | double | Volts | The on load rms stator line terminal voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_RMSStatorTerminalPhaseVoltage|IMOnLoad_RMSStatorTerminalPhaseVoltage]] | o/p | double | Volts | The on load rms stator phase terminal voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_RotorCopperLosses|IMOnLoad_RotorCopperLosses]] | o/p | double | Watts | The on load rotor copper losses |
| [[motorcad/parameter_database/parameters/IMOnLoad_RotorVoltage_Ref_L|IMOnLoad_RotorVoltage_Ref_L]] | o/p | double | Volts | The on load rms rotor voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_RotorVoltage_Ref_T|IMOnLoad_RotorVoltage_Ref_T]] | o/p | double | Volts | The on load rms rotor voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_StatorCopperLosses|IMOnLoad_StatorCopperLosses]] | o/p | double | Watts | The on load stator copper losses |
| [[motorcad/parameter_database/parameters/IMOnLoad_StatorWindingLosses|IMOnLoad_StatorWindingLosses]] | o/p | double | Watts | The on load stator winding losses |
| [[motorcad/parameter_database/parameters/IMOnLoad_StatorWindingVoltagePh|IMOnLoad_StatorWindingVoltagePh]] | o/p | double | Volts | The on load rms stator winding phase voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_StrayLoadLossVoltagePh|IMOnLoad_StrayLoadLossVoltagePh]] | o/p | double | Volts | The on load rms stray load phase voltage |
| [[motorcad/parameter_database/parameters/IMOnLoad_StrayLoadLosses|IMOnLoad_StrayLoadLosses]] | o/p | double | Watts | Stray load losses |
| [[motorcad/parameter_database/parameters/IMPeakSupplyCurrent|IMPeakSupplyCurrent]] | i/p | double | Amps | The line peak supply current |
| [[motorcad/parameter_database/parameters/IMPeakSupplyVoltage|IMPeakSupplyVoltage]] | i/p | double | Volts | The peak line-line supply voltage |
| [[motorcad/parameter_database/parameters/IMRatio_BreakDownLockedRotorCurrent|IMRatio_BreakDownLockedRotorCurrent]] | o/p | double | p.u. | Ratio of breakdown / locked rotor current |
| [[motorcad/parameter_database/parameters/IMRatio_BreakDownLockedRotorTorque|IMRatio_BreakDownLockedRotorTorque]] | o/p | double | p.u. | Ratio of locked-rotor/locked rotor airgap torque |
| [[motorcad/parameter_database/parameters/IMRatio_BreakDownLockedRotorVoltage|IMRatio_BreakDownLockedRotorVoltage]] | o/p | double | p.u. | Ratio of breakdown / locked rotor voltage |
| [[motorcad/parameter_database/parameters/IMRatio_BreakDownOnLoadCurrent|IMRatio_BreakDownOnLoadCurrent]] | o/p | double | p.u. | Ratio of breakdown/on load current |
| [[motorcad/parameter_database/parameters/IMRatio_BreakDownOnLoadTorque|IMRatio_BreakDownOnLoadTorque]] | o/p | double | p.u. | Ratio of breakdown/on load airgap torque |
| [[motorcad/parameter_database/parameters/IMRatio_BreakDownOnLoadVoltage|IMRatio_BreakDownOnLoadVoltage]] | o/p | double | p.u. | Ratio of breakdown/on load voltage |
| [[motorcad/parameter_database/parameters/IMRatio_LockedRotorOnLoadCurrent|IMRatio_LockedRotorOnLoadCurrent]] | o/p | double | p.u. | Ratio of locked rotor/on load current |
| [[motorcad/parameter_database/parameters/IMRatio_LockedRotorOnLoadTorque|IMRatio_LockedRotorOnLoadTorque]] | o/p | double | p.u. | Ratio of locked rotor/on load airgap torque |
| [[motorcad/parameter_database/parameters/IMRatio_LockedRotorOnLoadVoltage|IMRatio_LockedRotorOnLoadVoltage]] | o/p | double | p.u. | Ratio of locked rotor/on load voltage |
| [[motorcad/parameter_database/parameters/IMRecalculateSaturationModel|IMRecalculateSaturationModel]] | i/p | boolean | N/A | If selected, the saturation model will be rebuilt for every magnetic calculation |
| [[motorcad/parameter_database/parameters/IMReferredRotorParametersMethod|IMReferredRotorParametersMethod]] | compatibility | integer | N/A | Method for calculating referred rotor resistance and leakage inductance |
| [[motorcad/parameter_database/parameters/IMRmsSupplyCurrent|IMRmsSupplyCurrent]] | i/p | double | Amps | The rms supply current (sinusoidal waveform) |
| [[motorcad/parameter_database/parameters/IMRmsSupplyVoltage|IMRmsSupplyVoltage]] | i/p | double | Volts | The rms line-line supply voltage |
| [[motorcad/parameter_database/parameters/IMRotorBarRegionType|IMRotorBarRegionType]] | i/p | integer | N/A | Whether rotor bars are treated as conductors or air in core loss FEA calculation |
| [[motorcad/parameter_database/parameters/IMRotorEddyLossMethod|IMRotorEddyLossMethod]] | compatibility | integer | N/A | Method for calculating IM rotor eddy losses (improved scales with slip) |
| [[motorcad/parameter_database/parameters/IMRotorFluxDensityCalc|IMRotorFluxDensityCalc]] | compatibility | integer | N/A | The calculation of the rotor back iron flux density based on flux and cross sectional area |
| [[motorcad/parameter_database/parameters/IMSaturationCalcMethod|IMSaturationCalcMethod]] | i/p | integer | N/A | Saturation Model Method (recommend FEA for highly saturated models) |
| [[motorcad/parameter_database/parameters/IMSaturationConvergenceTolerance|IMSaturationConvergenceTolerance]] | i/p | double | N/A | Saturation Model Convergence Tolerance |
| [[motorcad/parameter_database/parameters/IMSaturationRelaxationFactor|IMSaturationRelaxationFactor]] | i/p | double | N/A | Saturation Model Under-Relaxation Factor |
| [[motorcad/parameter_database/parameters/IMSeriesEquivalentInductanceMethod|IMSeriesEquivalentInductanceMethod]] | compatibility | integer | N/A | Method for calculating IM series equivalent inductance |
| [[motorcad/parameter_database/parameters/IMShaftSpeedMax|IMShaftSpeedMax]] | i/p | double | rpm | The maximum shaft speed used for calculating the torque/speed curve |
| [[motorcad/parameter_database/parameters/IMShaftSpeedMin|IMShaftSpeedMin]] | i/p | double | rpm | The minimum shaft speed used for calculating the torque/speed curve |
| [[motorcad/parameter_database/parameters/IMSingleLoadCurrentRamp_Cycles|IMSingleLoadCurrentRamp_Cycles]] | compatibility | integer | N/A | The number of cycles for the current ramp used at the start of an induction motor transient or locked rotor calculation. |
| [[motorcad/parameter_database/parameters/IMSingleLoadCurrentRamp_Type|IMSingleLoadCurrentRamp_Type]] | i/p | integer | N/A | The type of ramp function used at the start of an induction motor transient or locked rotor calculation. |
| [[motorcad/parameter_database/parameters/IMSingleLoadError_NonRotating|IMSingleLoadError_NonRotating]] | o/p | double | N/A | Final error (%) in single load point (non-rotating) solver |
| [[motorcad/parameter_database/parameters/IMSingleLoadError_Rotating|IMSingleLoadError_Rotating]] | o/p | double | N/A | Final error (%) in single load point (rotating) solver |
| [[motorcad/parameter_database/parameters/IMSingleLoadNumberCycles_Initial|IMSingleLoadNumberCycles_Initial]] | i/p | integer | N/A | Number of additional static cycles calculated for initialisation before a full motion IM transient analysis |
| [[motorcad/parameter_database/parameters/IMSingleLoadNumberCycles_InitialRotating|IMSingleLoadNumberCycles_InitialRotating]] | recommended | integer | N/A | Number of additional rotating cycles calculated for initialisation before a full motion IM transient analysis |
| [[motorcad/parameter_database/parameters/IMSingleLoadPointFEACalc|IMSingleLoadPointFEACalc]] | i/p | boolean | N/A | When selected reduced induction machine single load point FEA calculation is run |
| [[motorcad/parameter_database/parameters/IMSingleLoadPointFEACalc_Rotating|IMSingleLoadPointFEACalc_Rotating]] | i/p | boolean | N/A | When selected full induction machine single load point FEA calculation is run |
| [[motorcad/parameter_database/parameters/IMSingleLoadPointFEACalc_Rotating_Initialisation|IMSingleLoadPointFEACalc_Rotating_Initialisation]] | compatibility | integer | N/A | Improved method includes static initialisation cycles before full motion simulation, to improve convergence |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_AvTorque|IMSingleLoadPoint_AvTorque]] | o/p | double | Nm | The average of virtual work and Maxwell stress torque in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_ConverterEfficiency|IMSingleLoadPoint_ConverterEfficiency]] | o/p | double | Percent | Efficiency of the converter in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_CoreLossResistance|IMSingleLoadPoint_CoreLossResistance]] | o/p | double | Ohms | The core loss equivalent resistance in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_DqTorque|IMSingleLoadPoint_DqTorque]] | o/p | double | Nm | The flux linkage torque in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_FluxLinkageD|IMSingleLoadPoint_FluxLinkageD]] | o/p | double | Vs | IM D-axis flux in the stator current dq frame in the single load point FEA |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_FluxLinkageQ|IMSingleLoadPoint_FluxLinkageQ]] | o/p | double | Vs | IM Q-axis flux in the stator current dq frame in the single load point FEA |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_InputPower|IMSingleLoadPoint_InputPower]] | o/p | double | Watts | Electrical input power in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_MSTorque|IMSingleLoadPoint_MSTorque]] | o/p | double | Nm | The Maxwell stress torque in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_MotorEfficiency|IMSingleLoadPoint_MotorEfficiency]] | o/p | double | Percent | Efficiency of the motor in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_OutputPower|IMSingleLoadPoint_OutputPower]] | o/p | double | Watts | Mechanical output power (electromagnetic power less losses) in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_PBTorque|IMSingleLoadPoint_PBTorque]] | o/p | double | Nm | The power balance torque in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_ParallelEquivInductance|IMSingleLoadPoint_ParallelEquivInductance]] | o/p | double | Henry | The equivalent inductance in parallel circuit in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_ParallelEquivResistance|IMSingleLoadPoint_ParallelEquivResistance]] | o/p | double | Ohms | The equivalent resistance in parallel circuit in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_PeakBackEMFLine|IMSingleLoadPoint_PeakBackEMFLine]] | o/p | double | Volts | Peak back EMF line voltage in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_PeakBackEMFPhase|IMSingleLoadPoint_PeakBackEMFPhase]] | o/p | double | Volts | Peak back EMF phase voltage in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_PeakCurrent|IMSingleLoadPoint_PeakCurrent]] | o/p | double | Amps | The peak current used for the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_PowerFactor|IMSingleLoadPoint_PowerFactor]] | o/p | double | N/A | IM power factor in single load point FEA |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RmsBackEMFLine|IMSingleLoadPoint_RmsBackEMFLine]] | o/p | double | Volts | RMS back EMF line to line voltage in the single load point FEA case (over last electrical cycle) |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RmsBackEMFPhase|IMSingleLoadPoint_RmsBackEMFPhase]] | o/p | double | Volts | RMS back EMF phase voltage in the single load point FEA case (over last electrical cycle) |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RmsLineLineVoltage|IMSingleLoadPoint_RmsLineLineVoltage]] | o/p | double | Volts | RMS Phase Voltage at the terminals of the machine in the single load point FEA case (over last cycle) |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RmsPhaseVoltage|IMSingleLoadPoint_RmsPhaseVoltage]] | o/p | double | Volts | RMS Phase Voltage at the terminals of the machine in the single load point FEA case (over last electrical cycle) |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RotorBarLeakageInductance_Ref|IMSingleLoadPoint_RotorBarLeakageInductance_Ref]] | o/p | double | Henry | The referred rotor bar leakage inductance in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RotorBarLosses|IMSingleLoadPoint_RotorBarLosses]] | o/p | double | Watts | The rotor bar losses calculated in the Single Load Point case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RotorBarResistance_Ref|IMSingleLoadPoint_RotorBarResistance_Ref]] | o/p | double | Ohms | The referred rotor bar resistance in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RotorCageLosses|IMSingleLoadPoint_RotorCageLosses]] | o/p | double | Watts | The rotor cage losses calculated in the Single Load Point case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RotorEndRingLosses|IMSingleLoadPoint_RotorEndRingLosses]] | o/p | double | Watts | The rotor endring losses calculated in the Single Load Point case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RotorLeakageInductance_Ref|IMSingleLoadPoint_RotorLeakageInductance_Ref]] | o/p | double | Henry | The referred rotor leakage inductance in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_RotorResistance_Ref|IMSingleLoadPoint_RotorResistance_Ref]] | o/p | double | Ohms | The referred rotor resistance in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_SeriesEquivInductance|IMSingleLoadPoint_SeriesEquivInductance]] | o/p | double | Henry | The equivalent inductance in series circuit in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_SeriesEquivResistance|IMSingleLoadPoint_SeriesEquivResistance]] | o/p | double | Ohms | The equivalent resistance in series circuit in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_ShaftTorque|IMSingleLoadPoint_ShaftTorque]] | o/p | double | Nm | Torque at shaft of machine taking into account drag losses in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_StatorCurrentD|IMSingleLoadPoint_StatorCurrentD]] | o/p | double | Amps | IM D-axis stator current in the stator current dq frame in the single load point FEA |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_StatorCurrentQ|IMSingleLoadPoint_StatorCurrentQ]] | o/p | double | Amps | IM Q-axis stator current in the stator current dq frame in the single load point FEA |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_StoredMagneticCoenergy|IMSingleLoadPoint_StoredMagneticCoenergy]] | o/p | double | J | The stored magnetic coenergy in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_StoredMagneticEnergy|IMSingleLoadPoint_StoredMagneticEnergy]] | o/p | double | J | The stored magnetic energy in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_StrayLoadLosses|IMSingleLoadPoint_StrayLoadLosses]] | o/p | double | Watts | Stray load losses from single load point FEA calculation |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_SystemEfficiency|IMSingleLoadPoint_SystemEfficiency]] | o/p | double | Percent | Efficiency of the system in the single load point FEA case |
| [[motorcad/parameter_database/parameters/IMSingleLoadPoint_VWTorque|IMSingleLoadPoint_VWTorque]] | o/p | double | Nm | The virtual work torque in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSinglePointLoad_PhaseInductance|IMSinglePointLoad_PhaseInductance]] | o/p | double | Henry | The phase inductance used in the Single Load Point FEA case |
| [[motorcad/parameter_database/parameters/IMSkinEffectApplication|IMSkinEffectApplication]] | recommended | integer | N/A | Defines which rotor bars skin effect is applied to. |
| [[motorcad/parameter_database/parameters/IMSlip|IMSlip]] | i/p | double | N/A | The slip |
| [[motorcad/parameter_database/parameters/IMSlipFrequency|IMSlipFrequency]] | o/p | double | Hz | The rotor electrical frequency |
| [[motorcad/parameter_database/parameters/IMSlipMax|IMSlipMax]] | i/p | double | N/A | The maximum slip used for calculating the torque/speed curve |
| [[motorcad/parameter_database/parameters/IMSlipMin|IMSlipMin]] | i/p | double | N/A | The minimum slip used for calculating the torque/speed curve |
| [[motorcad/parameter_database/parameters/IMSlipRangeDefinition|IMSlipRangeDefinition]] | i/p | integer | N/A | The definition of min/max slip for calculating the torque/speed curve |
| [[motorcad/parameter_database/parameters/IMSlotLeakageInductance_Rotor|IMSlotLeakageInductance_Rotor]] | o/p | double | Henry | The rotor slot leakage inductance |
| [[motorcad/parameter_database/parameters/IMSlotLeakageInductance_Rotor_Bottom|IMSlotLeakageInductance_Rotor_Bottom]] | o/p | double | Henry | The rotor slot leakage inductance |
| [[motorcad/parameter_database/parameters/IMSlotLeakageInductance_Rotor_Top|IMSlotLeakageInductance_Rotor_Top]] | o/p | double | Henry | The rotor slot leakage inductance |
| [[motorcad/parameter_database/parameters/IMSlotLeakagePermeanceFactor_Rotor_Bottom|IMSlotLeakagePermeanceFactor_Rotor_Bottom]] | o/p | double | N/A | The rotor slot leakage permeance factor used for calculation of the rotor leakage inductance |
| [[motorcad/parameter_database/parameters/IMSlotLeakagePermeanceFactor_Rotor_Top|IMSlotLeakagePermeanceFactor_Rotor_Top]] | o/p | double | N/A | The rotor slot leakage permeance factor used for calculation of the rotor leakage inductance |
| [[motorcad/parameter_database/parameters/IMSlotLeakagePermeanceFactor_Stator|IMSlotLeakagePermeanceFactor_Stator]] | o/p | double | N/A | The stator slot leakage permeance factor used for calculation of the slot leakage inductance |
| [[motorcad/parameter_database/parameters/IMSlotLeakageReactance_Rotor|IMSlotLeakageReactance_Rotor]] | o/p | double | Ohms | The rotor slot leakage reactance |
| [[motorcad/parameter_database/parameters/IMSpeedDefinition|IMSpeedDefinition]] | i/p | integer | N/A | The drive mode |
| [[motorcad/parameter_database/parameters/IMSynchronousSpeed|IMSynchronousSpeed]] | o/p | double | rpm | The synchronous speed |
| [[motorcad/parameter_database/parameters/IMTorqueSpeedCalc|IMTorqueSpeedCalc]] | i/p | boolean | N/A | When selected Induction machine analytic torque / speed calculation is run |
| [[motorcad/parameter_database/parameters/IMTorqueSpeedNumPoints|IMTorqueSpeedNumPoints]] | i/p | integer | N/A | The number of points calculated in the IM torque/speed curve |
| [[motorcad/parameter_database/parameters/IMUserData_L1|IMUserData_L1]] | i/p | double | Henry | Array of stator leakage inductances from user test data |
| [[motorcad/parameter_database/parameters/IMUserData_L2|IMUserData_L2]] | i/p | double | Henry | Array of rotor leakage inductances from user test data |
| [[motorcad/parameter_database/parameters/IMUserData_Lm|IMUserData_Lm]] | i/p | double | Henry | Array of magnetizing inductances from user test data |
| [[motorcad/parameter_database/parameters/IMUserData_Lm_Current|IMUserData_Lm_Current]] | i/p | double | Amps | Magnetizing currents associated with the magnetizing inductance user data |
| [[motorcad/parameter_database/parameters/IMUserData_Lm_Points|IMUserData_Lm_Points]] | i/p | integer | N/A | Number of points for which the magnetizing inductance user data is defined |
| [[motorcad/parameter_database/parameters/IMUserData_Load_Points|IMUserData_Load_Points]] | i/p | integer | N/A | Number of points for which the on load user data is defined |
| [[motorcad/parameter_database/parameters/IMUserData_Load_Speed|IMUserData_Load_Speed]] | i/p | double | rpm | Speeds associated with the on load user data |
| [[motorcad/parameter_database/parameters/IMUserData_R2|IMUserData_R2]] | i/p | double | Ohms | Array of referred rotor resistance from user test data |
| [[motorcad/parameter_database/parameters/IMUserData_Rfe|IMUserData_Rfe]] | i/p | double | Ohms | Array of core loss resistanves from user test data |
| [[motorcad/parameter_database/parameters/IMUserData_Rfe_BackEMF|IMUserData_Rfe_BackEMF]] | i/p | double | Volts | Back EMFs associated with the core loss resistance user data |
| [[motorcad/parameter_database/parameters/IMUserData_Rfe_Points|IMUserData_Rfe_Points]] | i/p | integer | N/A | Number of points for which the core loss resistance user data is defined |
| [[motorcad/parameter_database/parameters/IM_LCircuit_Alpha|IM_LCircuit_Alpha]] | o/p | double | N/A | The T to L equivalent circuit conversion factor |
| [[motorcad/parameter_database/parameters/IM_MagnetizingInductance|IM_MagnetizingInductance]] | o/p | double | Henry | The magnetizing inductance |
| [[motorcad/parameter_database/parameters/IM_MutualInductance|IM_MutualInductance]] | o/p | double | Henry | The stator winding mutual inductance |
| [[motorcad/parameter_database/parameters/IM_PhaseInductance|IM_PhaseInductance]] | o/p | double | Henry | The stator winding phase inductance |
| [[motorcad/parameter_database/parameters/IM_SelfInductance|IM_SelfInductance]] | o/p | double | Henry | The stator winding self inductance |
| [[motorcad/parameter_database/parameters/IM_StatorLeakageInductance|IM_StatorLeakageInductance]] | o/p | double | Henry | The stator winding leakage inductance |
| [[motorcad/parameter_database/parameters/InductanceCalc|InductanceCalc]] | i/p | boolean | N/A | When selected inductance calculation is run |
| [[motorcad/parameter_database/parameters/InductanceCurrent_D|InductanceCurrent_D]] | o/p | double | Vs | Inductance x Current product in D axis |
| [[motorcad/parameter_database/parameters/InductanceCurrent_Q|InductanceCurrent_Q]] | o/p | double | Vs | Inductance x Current product in Q axis |
| [[motorcad/parameter_database/parameters/InductanceLineToLine|InductanceLineToLine]] | o/p | double | Henry | The line to line inductance from self and mutual inductance calculation |
| [[motorcad/parameter_database/parameters/InductanceLineToLineFromDQ|InductanceLineToLineFromDQ]] | o/p | double | Henry | The line to line inductance from DQ inductance calculation |
| [[motorcad/parameter_database/parameters/InductanceLineToLineSkew|InductanceLineToLineSkew]] | o/p | double | Henry | The line to line inductance from self and mutual inductance calculation for skewed machine |
| [[motorcad/parameter_database/parameters/InductanceLineToLineSkewFromDQ|InductanceLineToLineSkewFromDQ]] | o/p | double | Henry | The line to line inductance from DQ inductance calculation for skewed machine |
| [[motorcad/parameter_database/parameters/InductanceLoadSkew_D|InductanceLoadSkew_D]] | o/p | double | Henry | The inductance in D axis for skewed machine |
| [[motorcad/parameter_database/parameters/InductanceLoadSkew_Q|InductanceLoadSkew_Q]] | o/p | double | Henry | The inductance in Q axis for skewed machine |
| [[motorcad/parameter_database/parameters/InductanceLoad_D|InductanceLoad_D]] | o/p | double | Henry | The inductance in D axis |
| [[motorcad/parameter_database/parameters/InductanceLoad_Q|InductanceLoad_Q]] | o/p | double | Henry | The inductance in Q axis |
| [[motorcad/parameter_database/parameters/InductanceRatio|InductanceRatio]] | o/p | double | N/A | The ratio of aligned inductance to unaligned inductance |
| [[motorcad/parameter_database/parameters/InputCircuit|InputCircuit]] | i/p | integer | N/A | The filter type used at input of machine, used for calculating the required drive voltage |
| [[motorcad/parameter_database/parameters/InputPower|InputPower]] | o/p | double | Watts | Electrical input power |
| [[motorcad/parameter_database/parameters/IronLossBuildFactorDefinition|IronLossBuildFactorDefinition]] | i/p | integer | N/A | Definition of iron loss build factors |
| [[motorcad/parameter_database/parameters/IronLossCalculationType|IronLossCalculationType]] | i/p | integer | N/A | Method used for calculating the iron losses |
| [[motorcad/parameter_database/parameters/IronLossCoefficientDataPoints|IronLossCoefficientDataPoints]] | i/p | integer | N/A | Number of data points for Iron Loss Coefficient Calculation |
| [[motorcad/parameter_database/parameters/KDamperEndRing_F|KDamperEndRing_F]] | o/p | double | N/A | Front K Damper End Ring |
| [[motorcad/parameter_database/parameters/KDamperEndRing_R|KDamperEndRing_R]] | o/p | double | N/A | Rear K Damper End Ring |
| [[motorcad/parameter_database/parameters/KEndRing|KEndRing]] | o/p | double | N/A | K Endring |
| [[motorcad/parameter_database/parameters/Ke|Ke]] | o/p | double | Vs/rad | Back EMF Constant Ke |
| [[motorcad/parameter_database/parameters/Ke_Fundamental|Ke_Fundamental]] | o/p | double | Vs/rad | Back EMF Constant Ke based on the fundamental harmonic |
| [[motorcad/parameter_database/parameters/Km|Km]] | o/p | double | Nm(Watts^0.5) | Motor Constant |
| [[motorcad/parameter_database/parameters/Ks1|Ks1]] | o/p | double | N/A | The skew factor of fundamental harmonic (Ks1) use for flux linkage calculation |
| [[motorcad/parameter_database/parameters/Ks2|Ks2]] | o/p | double | N/A | The skew factor of second harmonic (Ks2) use for inductance calculation |
| [[motorcad/parameter_database/parameters/Kt|Kt]] | o/p | double | Nm/A | Torque Constant Kt |
| [[motorcad/parameter_database/parameters/Lab_Threads_Enabled|Lab_Threads_Enabled]] | i/p | boolean | N/A | When checked Lab will use multiple threads as appropriate based on system resources |
| [[motorcad/parameter_database/parameters/LastIMLookupPoints_Saturation|LastIMLookupPoints_Saturation]] | i/p | integer | N/A | Model resolution used in most recent saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMLookupPoints_Saturation_Backup|LastIMLookupPoints_Saturation_Backup]] | i/p | integer | N/A | The resolution used in the most recent user-initiated saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMMaxPeakCurrent_SaturationCalc|LastIMMaxPeakCurrent_SaturationCalc]] | i/p | double | Amps | Maximum Peak Current of latest calculated saturation model |
| [[motorcad/parameter_database/parameters/LastIMMaxPeakCurrent_SaturationCalc_Backup|LastIMMaxPeakCurrent_SaturationCalc_Backup]] | i/p | double | Amps | The maximum peak current used in the most recent user-initiated saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMMaxPeakVoltage_SaturationCalc|LastIMMaxPeakVoltage_SaturationCalc]] | i/p | double | Volts | Maximum Peak Voltage of latest calculated saturation model |
| [[motorcad/parameter_database/parameters/LastIMMaxPeakVoltage_SaturationCalc_Backup|LastIMMaxPeakVoltage_SaturationCalc_Backup]] | i/p | double | Volts | The maximum peak voltage used in the most recent user-initiated saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMMaxRMSCurrent_SaturationCalc|LastIMMaxRMSCurrent_SaturationCalc]] | i/p | double | Amps | Maximum RMS Current of latest calculated saturation model |
| [[motorcad/parameter_database/parameters/LastIMMaxRMSCurrent_SaturationCalc_Backup|LastIMMaxRMSCurrent_SaturationCalc_Backup]] | i/p | double | Amps | The maximum RMS current used in the most recent user-initiated saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMMaxRMSVoltage_SaturationCalc|LastIMMaxRMSVoltage_SaturationCalc]] | i/p | double | Volts | Maximum RMS Voltage of latest calculated saturation model |
| [[motorcad/parameter_database/parameters/LastIMMaxRMSVoltage_SaturationCalc_Backup|LastIMMaxRMSVoltage_SaturationCalc_Backup]] | i/p | double | Volts | The maximum RMS voltage used in the most recent user-initiated saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMNoLoadMagnetizingCurrent|LastIMNoLoadMagnetizingCurrent]] | i/p | double | Amps | No Load Magnetizing current, determines maximum magnetization current +for Saturation Model |
| [[motorcad/parameter_database/parameters/LastIMSaturationCalcMethod|LastIMSaturationCalcMethod]] | i/p | integer | N/A | Calculation method used in most recent saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMSaturationCalcMethod_Backup|LastIMSaturationCalcMethod_Backup]] | i/p | integer | N/A | The calculation method used in the most recent user-initiated saturation model calculation |
| [[motorcad/parameter_database/parameters/LastIMSupplyDefinition_SaturationCalc|LastIMSupplyDefinition_SaturationCalc]] | i/p | integer | N/A | Supply definition of most recent calculation of saturation model |
| [[motorcad/parameter_database/parameters/LastIMSupplyDefinition_SaturationCalc_Backup|LastIMSupplyDefinition_SaturationCalc_Backup]] | i/p | integer | N/A | The supply definition used in the most recent user-initiated saturation model calculation |
| [[motorcad/parameter_database/parameters/LeakageFactor|LeakageFactor]] | o/p | double | N/A | Leakage Factor |
| [[motorcad/parameter_database/parameters/LineLineVoltage|LineLineVoltage]] | o/p | double | Volts | The rms line to line Voltage at the output of the supply |
| [[motorcad/parameter_database/parameters/LoadPoint_Calculated_Torque_Array|LoadPoint_Calculated_Torque_Array]] | i/p | double | Nm | LoadPoint Calculated Torque Array |
| [[motorcad/parameter_database/parameters/LoadPoint_Current_Array|LoadPoint_Current_Array]] | i/p | double | Amps | LoadPoint Current Array |
| [[motorcad/parameter_database/parameters/LoadPoint_DCFieldCurrent_Array|LoadPoint_DCFieldCurrent_Array]] | i/p | double | Amps | LoadPoint DC Field Current Array |
| [[motorcad/parameter_database/parameters/LoadPoint_OffAngle_Array|LoadPoint_OffAngle_Array]] | i/p | double | EDeg | LoadPoint OffAngle Array |
| [[motorcad/parameter_database/parameters/LoadPoint_OnAngle_Array|LoadPoint_OnAngle_Array]] | i/p | double | EDeg | LoadPoint OnAngle Array |
| [[motorcad/parameter_database/parameters/LoadPoint_PhaseAdvance_Array|LoadPoint_PhaseAdvance_Array]] | i/p | double | EDeg | LoadPoint PhaseAdvance Array |
| [[motorcad/parameter_database/parameters/LoadPoint_Slip_Array|LoadPoint_Slip_Array]] | i/p | double | N/A | LoadPoint Slip Array |
| [[motorcad/parameter_database/parameters/LoadPoint_Speed_Array|LoadPoint_Speed_Array]] | i/p | double | rpm | LoadPoint Speed Array |
| [[motorcad/parameter_database/parameters/LoadPoint_Torque_Array|LoadPoint_Torque_Array]] | i/p | double | Nm | LoadPoint Torque Array |
| [[motorcad/parameter_database/parameters/LoopTorqueMethod|LoopTorqueMethod]] | compatibility | integer | N/A | Method used to calculate the loop torque |
| [[motorcad/parameter_database/parameters/Loss_Total|Loss_Total]] | o/p | double | Watts | The total machine losses |
| [[motorcad/parameter_database/parameters/Loss_Total_Analytic|Loss_Total_Analytic]] | o/p | double | Watts | The total machine losses from the analytic calculation |
| [[motorcad/parameter_database/parameters/Loss_Total_OC|Loss_Total_OC]] | o/p | double | Watts | The total machine losses |
| [[motorcad/parameter_database/parameters/MMFMax|MMFMax]] | o/p | double | Amp Turns | The maximum MMF at any slot for a sine waveform |
| [[motorcad/parameter_database/parameters/MMFMin|MMFMin]] | o/p | double | Amp Turns | The minimum MMF at any slot for a sine waveform |
| [[motorcad/parameter_database/parameters/MagPathType|MagPathType]] | i/p | integer | N/A | Path Type - Central, Upper and Lower, or Right and Left |
| [[motorcad/parameter_database/parameters/MagPhaseDistribution|MagPhaseDistribution]] | i/p | integer | N/A | Phase distribution for multiphase machines - independently controlled phases or multiple 3-phase systems |
| [[motorcad/parameter_database/parameters/MagPhases|MagPhases]] | i/p | integer | N/A | Number of phases in winding |
| [[motorcad/parameter_database/parameters/MagThreads_AutoNumber|MagThreads_AutoNumber]] | i/p | boolean | N/A | When checked Motor-CAD chooses maximum simultaneous threads based on available system resources |
| [[motorcad/parameter_database/parameters/MagThreads_Number|MagThreads_Number]] | i/p | integer | N/A | Override automatic simultaneous threads for user selectable number of cores |
| [[motorcad/parameter_database/parameters/MagThreads_Option|MagThreads_Option]] | i/p | integer | N/A | When selected BPM calculations operate simultaneously |
| [[motorcad/parameter_database/parameters/MagThrow|MagThrow]] | i/p | integer | N/A | Coil Throw |
| [[motorcad/parameter_database/parameters/MagTurnsConductor|MagTurnsConductor]] | i/p | integer | N/A | Number Of Turns Per Coil |
| [[motorcad/parameter_database/parameters/MagTurnsConductorField|MagTurnsConductorField]] | i/p | integer | N/A | Number Of Turns Per Coil in the field winding |
| [[motorcad/parameter_database/parameters/MagWindingOffset|MagWindingOffset]] | i/p | integer | N/A | Winding Offset |
| [[motorcad/parameter_database/parameters/Magnet2D3DCalculation|Magnet2D3DCalculation]] | compatibility | integer | N/A | Method used for calculating the magnet losses to take into account segmentation and 3D effects |
| [[motorcad/parameter_database/parameters/Magnet2D3DFactor|Magnet2D3DFactor]] | o/p | double | N/A | Factor to convert 2D magnet loss to total losses for machine, taking into account axial segmentation. |
| [[motorcad/parameter_database/parameters/Magnet2D3DFactorMethod|Magnet2D3DFactorMethod]] | i/p | integer | N/A | Method used to calculate Magnet 2D3D Factor for magnet losses |
| [[motorcad/parameter_database/parameters/Magnet2D3DFactor_Ruoho|Magnet2D3DFactor_Ruoho]] | o/p | double | N/A | Factor to convert 2D magnet loss to total losses for machine, taking into account axial segmentation (Ruoho method). |
| [[motorcad/parameter_database/parameters/Magnet2D3DFactor_Wakao|Magnet2D3DFactor_Wakao]] | o/p | double | N/A | Factor to convert 2D magnet loss to total losses for machine, taking into account axial segmentation (Wakao-Fujiwara method). |
| [[motorcad/parameter_database/parameters/Magnet2D3DFactor_Wakao_ConvergenceTolerance|Magnet2D3DFactor_Wakao_ConvergenceTolerance]] | o/p | double | N/A | Convergence tolerance for calculation of Magnet 2D3D Factor (Wakao-Fujiwara method) (percentage) |
| [[motorcad/parameter_database/parameters/Magnet2D3DFactor_Wakao_Divergent|Magnet2D3DFactor_Wakao_Divergent]] | o/p | boolean | N/A | Warning flag indicating if calculation of Magnet 2D3D Factor (Wakao-Fujiwara method) was divergent. |
| [[motorcad/parameter_database/parameters/Magnet2D3DFactor_Wakao_MaxIterationOrder|Magnet2D3DFactor_Wakao_MaxIterationOrder]] | o/p | integer | N/A | Maximum order to go to in sum to calculate Magnet 2D3D Factor (Wakao-Fujiwara method) |
| [[motorcad/parameter_database/parameters/Magnet2D3DWidth|Magnet2D3DWidth]] | o/p | double | mm | Average Magnet block width used in calculating the magnet loss factor. |
| [[motorcad/parameter_database/parameters/Magnet2D3DWidth_Calc|Magnet2D3DWidth_Calc]] | compatibility | integer | N/A | Method used for calculating the magnet width to take into account segmentation and 3D effects |
| [[motorcad/parameter_database/parameters/MagnetDemagKneePoint|MagnetDemagKneePoint]] | o/p | double | Tesla | The flux density at the demagnetization knee point |
| [[motorcad/parameter_database/parameters/MagnetDemagRatio|MagnetDemagRatio]] | o/p | double | N/A | The proportion of magnet area with flux density below the knee point |
| [[motorcad/parameter_database/parameters/MagnetDemagRatio_Array|MagnetDemagRatio_Array]] | o/p | double | N/A | The proportion of magnet area with flux density below the knee point |
| [[motorcad/parameter_database/parameters/MagnetIntrinsicPermeanceCoefficient|MagnetIntrinsicPermeanceCoefficient]] | o/p | double | N/A | The magnet Intrinsic Permeance Coefficient |
| [[motorcad/parameter_database/parameters/MagnetIntrinsicPermeances|MagnetIntrinsicPermeances]] | o/p | double | N/A | Intrinsic permeance of each magnet |
| [[motorcad/parameter_database/parameters/MagnetLoss|MagnetLoss]] | o/p | double | Watts | Magnet Loss of BPM machine |
| [[motorcad/parameter_database/parameters/MagnetLossBuildFactor|MagnetLossBuildFactor]] | i/p | double | N/A | Multiplier used to adjust magnet losses |
| [[motorcad/parameter_database/parameters/MagnetLoss_Adj|MagnetLoss_Adj]] | o/p | double | Watts | Magnet Loss of BPM machine adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/MagnetLoss_Adj_OC|MagnetLoss_Adj_OC]] | o/p | double | Watts | Magnet Loss of BPM machine adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/MagnetLoss_OC|MagnetLoss_OC]] | o/p | double | Watts | Magnet Loss of BPM machine |
| [[motorcad/parameter_database/parameters/MagnetNamesInFEA|MagnetNamesInFEA]] | o/p | OleStr | N/A | Region names of magnets present in the FEA solver |
| [[motorcad/parameter_database/parameters/MagnetPermeanceCoefficient|MagnetPermeanceCoefficient]] | o/p | double | N/A | The magnet permeance coefficient (recoil demagnetization slope) |
| [[motorcad/parameter_database/parameters/MagnetPermeances|MagnetPermeances]] | o/p | double | N/A | Permeance of each magnet |
| [[motorcad/parameter_database/parameters/MagnetRefTempItem|MagnetRefTempItem]] | i/p | integer | N/A | Which magnet temperature is selected as the reference temperature. |
| [[motorcad/parameter_database/parameters/MagnetRefTemp_Defined|MagnetRefTemp_Defined]] | i/p | double | °C | Reference temperature for magnet data, defined by the user. |
| [[motorcad/parameter_database/parameters/MagnetRefTemps|MagnetRefTemps]] | o/p | double | °C | Reference temperature for each magnet |
| [[motorcad/parameter_database/parameters/MagnetTempLinkMethod|MagnetTempLinkMethod]] | recommended | integer | N/A | Magnet Temperature (central slice, max or average) that is transferred to E-Magnetic/Lab from Thermal |
| [[motorcad/parameter_database/parameters/Magnet_BAv|Magnet_BAv]] | o/p | double | Tesla | The average flux density in magnet |
| [[motorcad/parameter_database/parameters/Magnet_BAv_Array|Magnet_BAv_Array]] | o/p | double | Tesla | The average flux density in magnet segment |
| [[motorcad/parameter_database/parameters/Magnet_BMax|Magnet_BMax]] | o/p | double | Tesla | The maximum flux density in magnet |
| [[motorcad/parameter_database/parameters/Magnet_BMax_Array|Magnet_BMax_Array]] | o/p | double | Tesla | The maximum flux density in magnet segment |
| [[motorcad/parameter_database/parameters/Magnet_BMin|Magnet_BMin]] | o/p | double | Tesla | The minimum flux density in magnet |
| [[motorcad/parameter_database/parameters/Magnet_BMin_Array|Magnet_BMin_Array]] | o/p | double | Tesla | The minimum flux density in magnet segment |
| [[motorcad/parameter_database/parameters/Magnet_Br_Calculated|Magnet_Br_Calculated]] | o/p | double | Tesla | Remanent flux density of magnet calculated for magnet temperature |
| [[motorcad/parameter_database/parameters/Magnet_Br_Multiplier|Magnet_Br_Multiplier]] | i/p | double | N/A | Multiplier used to adjust magnet remanence |
| [[motorcad/parameter_database/parameters/Magnet_Br_Used|Magnet_Br_Used]] | o/p | double | Tesla | Remanent flux density of magnet used in calculation |
| [[motorcad/parameter_database/parameters/Magnet_Br_at_RefTemp|Magnet_Br_at_RefTemp]] | i/p | double | Tesla | Remanent flux density of magnet at reference temperature |
| [[motorcad/parameter_database/parameters/Magnet_HAv|Magnet_HAv]] | o/p | double | A/m | The average field strength in magnet |
| [[motorcad/parameter_database/parameters/Magnet_HAv_Array|Magnet_HAv_Array]] | o/p | double | A/m | Magnet HAv Array |
| [[motorcad/parameter_database/parameters/Magnet_HMax|Magnet_HMax]] | o/p | double | A/m | The maximum field strength in magnet |
| [[motorcad/parameter_database/parameters/Magnet_HMax_Array|Magnet_HMax_Array]] | o/p | double | A/m | Magnet HMax Array |
| [[motorcad/parameter_database/parameters/Magnet_HMin|Magnet_HMin]] | o/p | double | A/m | The minimum field strength in magnet |
| [[motorcad/parameter_database/parameters/Magnet_HMin_Array|Magnet_HMin_Array]] | o/p | double | A/m | Magnet HMin Array |
| [[motorcad/parameter_database/parameters/Magnet_HcJ_Calculated|Magnet_HcJ_Calculated]] | o/p | double | A/m | Intrinsic Coercivity of magnet calculated for magnet temperature |
| [[motorcad/parameter_database/parameters/Magnet_HcJ_at_RefTemp|Magnet_HcJ_at_RefTemp]] | i/p | double | A/m | Intrinsic coercivity of magnet at reference temperature |
| [[motorcad/parameter_database/parameters/Magnet_RefTemp|Magnet_RefTemp]] | i/p | double | °C | Temperature at which magnet data measured |
| [[motorcad/parameter_database/parameters/Magnet_Resistivity|Magnet_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the magnet at the magnet temperature |
| [[motorcad/parameter_database/parameters/Magnet_ResistivityAt20C|Magnet_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the magnet at reference temperature |
| [[motorcad/parameter_database/parameters/Magnet_SquarenessFactor|Magnet_SquarenessFactor]] | i/p | double | N/A | Factor determining the sharpness of the demagnetization knee point |
| [[motorcad/parameter_database/parameters/Magnet_TBr_Coeff|Magnet_TBr_Coeff]] | i/p | double | N/A | Magnet temperature coefficient of remanence |
| [[motorcad/parameter_database/parameters/Magnet_THcJ_Coeff|Magnet_THcJ_Coeff]] | i/p | double | %/°C | Reversible temperature coefficient of HcJ for current magnet |
| [[motorcad/parameter_database/parameters/Magnet_Temperature|Magnet_Temperature]] | i/p | double | °C | The temperature of the magnet |
| [[motorcad/parameter_database/parameters/Magnet_ur|Magnet_ur]] | i/p | double | N/A | Relative permeability of magnet |
| [[motorcad/parameter_database/parameters/MagneticAxialLengthMultiplier|MagneticAxialLengthMultiplier]] | i/p | double | N/A | Multiplier used to adjust the magnetic axial length |
| [[motorcad/parameter_database/parameters/MagneticContextVisible|MagneticContextVisible]] | setting | boolean | N/A | This is true when the electromagnetic context is visible |
| [[motorcad/parameter_database/parameters/MagneticLength_Array|MagneticLength_Array]] | o/p | double | mm | Magnetic length of each slice modelled by the FEA |
| [[motorcad/parameter_database/parameters/MagneticShaft|MagneticShaft]] | i/p | boolean | N/A | When set the machine has a magnetic shaft |
| [[motorcad/parameter_database/parameters/MagneticSymmetry|MagneticSymmetry]] | recommended | integer | N/A | When selected symmetry is used to reduce model size |
| [[motorcad/parameter_database/parameters/MagneticSymmetryFactor|MagneticSymmetryFactor]] | i/p | integer | N/A | When symmetry is selected then this is symmetry factor |
| [[motorcad/parameter_database/parameters/MagneticThermalCoupling|MagneticThermalCoupling]] | i/p | integer | N/A | How the electromagnetic and thermal model data is transferred for the steady state calculation |
| [[motorcad/parameter_database/parameters/MagneticThermalMaxError|MagneticThermalMaxError]] | i/p | double | N/A | Maximum error for convergence |
| [[motorcad/parameter_database/parameters/MagneticThermalMaxIterations|MagneticThermalMaxIterations]] | i/p | integer | N/A | Maximum number of iterataions to run |
| [[motorcad/parameter_database/parameters/MagneticWindingType|MagneticWindingType]] | i/p | integer | N/A | Winding Type - Lap, Concentric or Custom |
| [[motorcad/parameter_database/parameters/MagneticWindingTypeHairpin|MagneticWindingTypeHairpin]] | i/p | integer | N/A | Hairpin Winding Type - Custom or Wave |
| [[motorcad/parameter_database/parameters/MagnetisationCurveSymmetry|MagnetisationCurveSymmetry]] | recommended | integer | N/A | Whether magnetisation curve is mirrored at 180° for symmetric data |
| [[motorcad/parameter_database/parameters/MagnetisationCurvesPlotSelect|MagnetisationCurvesPlotSelect]] | setting | integer | N/A | Select the axis parameters of the magnetisation curves. |
| [[motorcad/parameter_database/parameters/MagnetisationCurves_Current|MagnetisationCurves_Current]] | i/p | double | Amps | Magnetisation curves current values |
| [[motorcad/parameter_database/parameters/MagnetisationCurves_File|MagnetisationCurves_File]] | i/p | OleStr | N/A | File Path of Saved/Loaded Magnetisation Curves |
| [[motorcad/parameter_database/parameters/MagnetisationCurves_FluxLinkage|MagnetisationCurves_FluxLinkage]] | i/p | double | Vs | Magnetisation curves flux linkage values |
| [[motorcad/parameter_database/parameters/MagnetisationCurves_Position|MagnetisationCurves_Position]] | i/p | double | EDeg | Magnetisation curves position values |
| [[motorcad/parameter_database/parameters/Magnetization|Magnetization]] | i/p | integer | N/A | Magnetization direction |
| [[motorcad/parameter_database/parameters/MagnetizingCurrent_Aux_RMS|MagnetizingCurrent_Aux_RMS]] | o/p | double | Amps | The on load aux winding RMS magnetizing current |
| [[motorcad/parameter_database/parameters/MagnetizingInductanceLoad_D|MagnetizingInductanceLoad_D]] | o/p | double | Henry | The magnetizing inductance in D axis |
| [[motorcad/parameter_database/parameters/MagnetizingInductanceLoad_Q|MagnetizingInductanceLoad_Q]] | o/p | double | Henry | The magnetizing inductance in Q axis |
| [[motorcad/parameter_database/parameters/MagnetizingInductanceSaturated|MagnetizingInductanceSaturated]] | o/p | double | Henry | The Magnetizing Inductance (including any skewing effects) (on load) |
| [[motorcad/parameter_database/parameters/MagnetizingInductanceUnsaturated|MagnetizingInductanceUnsaturated]] | o/p | double | Henry | The Magnetizing Inductance (including any skewing effects) |
| [[motorcad/parameter_database/parameters/MagnetizingInductanceUnsaturated_WithoutSkew|MagnetizingInductanceUnsaturated_WithoutSkew]] | o/p | double | Henry | The Magnetizing Inductance (without any skewing effects) |
| [[motorcad/parameter_database/parameters/MagnetizingInductance_Aux_Multiplier|MagnetizingInductance_Aux_Multiplier]] | i/p | double | N/A | Multiplier used to adjust the aux winding magnetizing inductance |
| [[motorcad/parameter_database/parameters/MagnetizingInductance_Aux_Unsaturated|MagnetizingInductance_Aux_Unsaturated]] | o/p | double | Henry | The aux winding unsaturated magnetizing inductance |
| [[motorcad/parameter_database/parameters/MagnetizingInductance_Aux_Unsaturated_WithoutSkew|MagnetizingInductance_Aux_Unsaturated_WithoutSkew]] | o/p | double | Henry | The aux winding unsaturated magnetizing inductance (without any skewing effects) |
| [[motorcad/parameter_database/parameters/MagnetizingInductance_Multiplier|MagnetizingInductance_Multiplier]] | i/p | double | N/A | Multiplier used to adjust the magnetizing inductance |
| [[motorcad/parameter_database/parameters/MagnetizingReactanceLoad_D|MagnetizingReactanceLoad_D]] | o/p | double | Ohms | The magnetizing reactance in D axis |
| [[motorcad/parameter_database/parameters/MagnetizingReactanceLoad_Q|MagnetizingReactanceLoad_Q]] | o/p | double | Ohms | The magnetizing reactance in Q axis |
| [[motorcad/parameter_database/parameters/MagnetizingReactanceSaturated|MagnetizingReactanceSaturated]] | o/p | double | Ohms | The saturated Magnetizing Reactance (including any skewing effects) (on load) |
| [[motorcad/parameter_database/parameters/MagnetizingReactanceSaturated_L|MagnetizingReactanceSaturated_L]] | o/p | double | Ohms | The saturated Magnetizing Reactance (including any skewing effects) |
| [[motorcad/parameter_database/parameters/MagnetizingReactanceUnsaturated|MagnetizingReactanceUnsaturated]] | o/p | double | Ohms | The unsaturated Magnetizing Reactance (including any skewing effects) |
| [[motorcad/parameter_database/parameters/MagnetizingReactance_Aux_Unsaturated|MagnetizingReactance_Aux_Unsaturated]] | o/p | double | Ohms | The aux winding unsaturated magnetizing reactance |
| [[motorcad/parameter_database/parameters/MaxAngleBetweenPhasors|MaxAngleBetweenPhasors]] | o/p | double | EDeg | The maximum angle between any two phasors |
| [[motorcad/parameter_database/parameters/MaxCurrent_Calculated_MagnetisationCurves|MaxCurrent_Calculated_MagnetisationCurves]] | i/p | double | N/A | The maximum current used for calculating the magnetisation curves |
| [[motorcad/parameter_database/parameters/MaxTorque|MaxTorque]] | o/p | double | Nm | The maximum possible magnet and reluctance torque |
| [[motorcad/parameter_database/parameters/MaxTorqueAngle|MaxTorqueAngle]] | o/p | double | EDeg | Angle at which the magnet and reluctance torque give maximum torque |
| [[motorcad/parameter_database/parameters/MaxTorqueCalcAngle|MaxTorqueCalcAngle]] | o/p | double | EDeg | Angle of phase advance for which the maximum possible magnet and reluctance torque was calculated |
| [[motorcad/parameter_database/parameters/MaxTorque_SRM|MaxTorque_SRM]] | o/p | double | Nm | The maximum torque possible with an ideal current waveform |
| [[motorcad/parameter_database/parameters/MaxwellForces_AverageTorque_OC|MaxwellForces_AverageTorque_OC]] | o/p | double | Nm | The average torque over one electrical cycle calculated from the OC tangential forces |
| [[motorcad/parameter_database/parameters/MaxwellForces_AverageTorque_OL|MaxwellForces_AverageTorque_OL]] | o/p | double | Nm | The average torque over one electrical cycle calculated from the OL tangential forces |
| [[motorcad/parameter_database/parameters/MeanCoilPitch|MeanCoilPitch]] | o/p | double | mm | The length of average endwinding pitch |
| [[motorcad/parameter_database/parameters/MeanCoilPitch_Aux|MeanCoilPitch_Aux]] | o/p | double | mm | The length of average aux endwinding pitch |
| [[motorcad/parameter_database/parameters/MeanCoilPitch_Inner|MeanCoilPitch_Inner]] | o/p | double | mm | The length of average endwinding pitch on the inner side of the stator |
| [[motorcad/parameter_database/parameters/MeanCoilPitch_Outer|MeanCoilPitch_Outer]] | o/p | double | mm | The length of average endwinding pitch on the outer side of the stator |
| [[motorcad/parameter_database/parameters/MeanDCLoadPower|MeanDCLoadPower]] | o/p | double | Watts | The mean power supplied to the DC bus |
| [[motorcad/parameter_database/parameters/MeanDCLoadVoltage|MeanDCLoadVoltage]] | o/p | double | Volts | The mean voltage of the loads DC bus |
| [[motorcad/parameter_database/parameters/MeanDCSupplyCurrent|MeanDCSupplyCurrent]] | o/p | double | Amps | The mean supply current from DC bus |
| [[motorcad/parameter_database/parameters/MechanicalConstant|MechanicalConstant]] | o/p | double | msec | Mechanical Constant |
| [[motorcad/parameter_database/parameters/MechanicalFrequency|MechanicalFrequency]] | o/p | double | Hz | Frequency of mechanical cycles |
| [[motorcad/parameter_database/parameters/MinSupplyVoltage|MinSupplyVoltage]] | o/p | double | Volts | The minimum supply voltage |
| [[motorcad/parameter_database/parameters/MotorAndTorqueConstantsMethod|MotorAndTorqueConstantsMethod]] | compatibility | integer | N/A | Method used to calculate the Motor Constant and the Torque Constant |
| [[motorcad/parameter_database/parameters/MotorEfficiency|MotorEfficiency]] | o/p | double | Percent | Efficiency of motor |
| [[motorcad/parameter_database/parameters/MotorLABContextVisible|MotorLABContextVisible]] | o/p | boolean | N/A | This is true when the Lab context is visible |
| [[motorcad/parameter_database/parameters/MultiForceCalcsRunning|MultiForceCalcsRunning]] | o/p | boolean | N/A | Whether Torque calculations for multiple operating point force calculations are running |
| [[motorcad/parameter_database/parameters/MultiForceEnvelopePoints|MultiForceEnvelopePoints]] | i/p | integer | N/A | The number of points used in calculating the torque speed envelope for multi-point force calculations |
| [[motorcad/parameter_database/parameters/MultiForceEnvelopeSetOperatingPoints|MultiForceEnvelopeSetOperatingPoints]] | i/p | integer | N/A | If the torque envelope should be used to re-set the operating points |
| [[motorcad/parameter_database/parameters/MultiForceEnvelopeStepSize|MultiForceEnvelopeStepSize]] | i/p | double | rpm | The step size used in calculating the torque speed envelope for multi-point force calculations |
| [[motorcad/parameter_database/parameters/MultiForceExportFile|MultiForceExportFile]] | i/p | OleStr | N/A | The Forces Export filename |
| [[motorcad/parameter_database/parameters/MultiForceLoadPointDefinition|MultiForceLoadPointDefinition]] | i/p | integer | N/A | The load point definition for multiple point force calculations using either current / phase advance or torque |
| [[motorcad/parameter_database/parameters/MultiForceMaxEnvelopeSpeed|MultiForceMaxEnvelopeSpeed]] | i/p | integer | rpm | The Maximum speed used in calculating the torque speed envelope for multi-point force calculations |
| [[motorcad/parameter_database/parameters/MultiForceMinEnvelopeSpeed|MultiForceMinEnvelopeSpeed]] | i/p | integer | rpm | The Minimum speed used in calculating the torque speed envelope for multi-point force calculations |
| [[motorcad/parameter_database/parameters/MultiForceThreading|MultiForceThreading]] | setting | integer | N/A | Whether to use single or multiple threads when undertaking multiple operating point forces calculation. |
| [[motorcad/parameter_database/parameters/MultiForce_LoadPointToAnalyse|MultiForce_LoadPointToAnalyse]] | setting | integer | N/A | The selected single load point for Force Analysis |
| [[motorcad/parameter_database/parameters/Multimodel_Threads_MaxNumber|Multimodel_Threads_MaxNumber]] | i/p | integer | N/A | Maximum number of threads used in multithreaded Lab/Romax calculations |
| [[motorcad/parameter_database/parameters/MultiplexOffset|MultiplexOffset]] | i/p | integer | N/A | Slot offset for 3 or 5 phase Multiplex Winding groups |
| [[motorcad/parameter_database/parameters/Multiplicity|Multiplicity]] | i/p | integer | N/A | The multiplicity of the windings (plex) |
| [[motorcad/parameter_database/parameters/MutualInductance|MutualInductance]] | o/p | double | Henry | Mutual Inductance of winding |
| [[motorcad/parameter_database/parameters/MutualInductanceSkew|MutualInductanceSkew]] | o/p | double | Henry | Mutual Inductance of winding for skewed machine |
| [[motorcad/parameter_database/parameters/NoLoadSpeed|NoLoadSpeed]] | o/p | double | rpm | The machine speed at which torque will reach 0 [Nm] with no phase advance |
| [[motorcad/parameter_database/parameters/NumDemagCurveTemperatures|NumDemagCurveTemperatures]] | i/p | integer | N/A | Number of different temperatures to be displayed on demagnetization chart |
| [[motorcad/parameter_database/parameters/NumForcePointsPerNode_Rotor|NumForcePointsPerNode_Rotor]] | i/p | integer | N/A | The number of force points calculated for each rotor node. |
| [[motorcad/parameter_database/parameters/NumForcePointsPerNode_Stator|NumForcePointsPerNode_Stator]] | i/p | integer | N/A | The number of force points calculated for each stator node. |
| [[motorcad/parameter_database/parameters/NumHarmonicDataPoints|NumHarmonicDataPoints]] | setting | integer | N/A | Number of custom Harmonic Data points |
| [[motorcad/parameter_database/parameters/NumIMFluxNodes|NumIMFluxNodes]] | o/p | integer | N/A | Number of nodes in magnetic flux density calculation (IM) |
| [[motorcad/parameter_database/parameters/NumLoadPoints|NumLoadPoints]] | i/p | integer | N/A | The number of load points. |
| [[motorcad/parameter_database/parameters/NumMagnetsInFEA|NumMagnetsInFEA]] | o/p | integer | N/A | Total number of magnets present in FEA analysis (per slice) |
| [[motorcad/parameter_database/parameters/NumTotalForcePoints_Rotor|NumTotalForcePoints_Rotor]] | o/p | integer | N/A | The total number of force points on the rotor over 360 mechanical degrees. |
| [[motorcad/parameter_database/parameters/NumTotalForcePoints_Stator|NumTotalForcePoints_Stator]] | o/p | integer | N/A | The total number of force points on the stator over 360 mechanical degrees. |
| [[motorcad/parameter_database/parameters/NumberOfCoils|NumberOfCoils]] | i/p | integer | N/A | Number Of Coils In a Phase |
| [[motorcad/parameter_database/parameters/NumberRadialForceHarmonics_OC|NumberRadialForceHarmonics_OC]] | o/p | integer | N/A | The number of radial force harmonic orders extracted from Open Circuit force data |
| [[motorcad/parameter_database/parameters/NumberRadialForceHarmonics_OL|NumberRadialForceHarmonics_OL]] | o/p | integer | N/A | The number of radial force harmonic orders extracted from On Load force data |
| [[motorcad/parameter_database/parameters/NumberRotorLamination|NumberRotorLamination]] | o/p | double | N/A | The number of rotor laminations in machine based on stacking factor and rotor length |
| [[motorcad/parameter_database/parameters/NumberStatorLamination|NumberStatorLamination]] | o/p | double | N/A | The number of stator laminations in machine based on stacking factor and stator length |
| [[motorcad/parameter_database/parameters/NumberStrandsHand|NumberStrandsHand]] | i/p | integer | N/A | Number of strands in hand for each turn of winding |
| [[motorcad/parameter_database/parameters/NumberStrandsHand_2|NumberStrandsHand_2]] | i/p | integer | N/A | Number of strands in hand of the second wire size for each turn of winding |
| [[motorcad/parameter_database/parameters/NumberStrandsHand_3|NumberStrandsHand_3]] | i/p | integer | N/A | Number of strands in hand of the third wire size for each turn of winding |
| [[motorcad/parameter_database/parameters/NumberStrandsHand_Aux|NumberStrandsHand_Aux]] | i/p | integer | N/A | Number of strands in hand of the Aux wire for each turn of winding |
| [[motorcad/parameter_database/parameters/NumberStrandsHand_Field|NumberStrandsHand_Field]] | i/p | integer | N/A | Number of strands in hand for each turn of field winding |
| [[motorcad/parameter_database/parameters/NumberTangentialForceHarmonics_OC|NumberTangentialForceHarmonics_OC]] | o/p | integer | N/A | The number of tangential force harmonic orders extracted from Open Circuit force data |
| [[motorcad/parameter_database/parameters/NumberTangentialForceHarmonics_OL|NumberTangentialForceHarmonics_OL]] | o/p | integer | N/A | The number of tangential force harmonic orders extracted from On Load force data |
| [[motorcad/parameter_database/parameters/OnLoadCalculation|OnLoadCalculation]] | i/p | boolean | N/A | When selected on load calculation is run (this should normally be set to true) |
| [[motorcad/parameter_database/parameters/OnLoadDQTorque|OnLoadDQTorque]] | o/p | double | Nm | The magnet and reluctance torque calculated using flux linkage method at static load point |
| [[motorcad/parameter_database/parameters/OnLoadLossCalculation|OnLoadLossCalculation]] | i/p | boolean | N/A | When selected iron and magnet loss calculations are done on load |
| [[motorcad/parameter_database/parameters/OnLoad_RotorPeripheralVelocity|OnLoad_RotorPeripheralVelocity]] | o/p | double | m/s | The on load rotor peripheral velocity |
| [[motorcad/parameter_database/parameters/OpenCircuitCalculation|OpenCircuitCalculation]] | i/p | boolean | N/A | When selected open circuit calculation is run. Only applicable to PMDC machines. |
| [[motorcad/parameter_database/parameters/OperatingMode|OperatingMode]] | i/p | integer | N/A | The operating mode (motor, generator or brake) |
| [[motorcad/parameter_database/parameters/OptimumSkewingAngle|OptimumSkewingAngle]] | o/p | double | MDeg | The optimum skewing angle for reducing cogging torque |
| [[motorcad/parameter_database/parameters/OutputPower|OutputPower]] | o/p | double | Watts | Mechanical output power (electromagnetic power less losses) |
| [[motorcad/parameter_database/parameters/OutputPower_Electrical|OutputPower_Electrical]] | o/p | double | Watts | Electrical output power (mechanical power less losses) |
| [[motorcad/parameter_database/parameters/OutputPower_Mechanical|OutputPower_Mechanical]] | o/p | double | Watts | Mechanical output power (electromagnetic power less losses) |
| [[motorcad/parameter_database/parameters/ParallelPaths|ParallelPaths]] | i/p | integer | N/A | Number Of Parallel Paths |
| [[motorcad/parameter_database/parameters/ParallelPaths_Aux|ParallelPaths_Aux]] | i/p | integer | N/A | Number of parallel paths in the aux winding |
| [[motorcad/parameter_database/parameters/ParallelPaths_Field|ParallelPaths_Field]] | i/p | integer | N/A | Number Of Parallel Paths in the field winding |
| [[motorcad/parameter_database/parameters/ParallelPaths_Hairpin|ParallelPaths_Hairpin]] | i/p | integer | N/A | Number of Parallel Paths (hairpin) |
| [[motorcad/parameter_database/parameters/PassiveGeneratorLoadType|PassiveGeneratorLoadType]] | i/p | integer | N/A | The type of passive generator load (AC or DC). |
| [[motorcad/parameter_database/parameters/PeakBackEMFLine|PeakBackEMFLine]] | o/p | double | Volts | Peak back EMF line to line voltage in open circuit |
| [[motorcad/parameter_database/parameters/PeakBackEMFLine_Fundamental|PeakBackEMFLine_Fundamental]] | o/p | double | Volts | Peak of the fundamental harmonic of back EMF line to line voltage in open circuit |
| [[motorcad/parameter_database/parameters/PeakBackEMFPhase|PeakBackEMFPhase]] | o/p | double | Volts | Peak back EMF phase voltage in open circuit |
| [[motorcad/parameter_database/parameters/PeakBackEMF_PMDC|PeakBackEMF_PMDC]] | o/p | double | Volts | Peak back EMF voltage in open circuit |
| [[motorcad/parameter_database/parameters/PeakCurrent|PeakCurrent]] | i/p | double | Amps | The peak line current available |
| [[motorcad/parameter_database/parameters/PeakCurrentDensity|PeakCurrentDensity]] | o/p | double | Amps/mm² | The peak current density (current limited waveform) |
| [[motorcad/parameter_database/parameters/PeakLineLineVoltage|PeakLineLineVoltage]] | o/p | double | Volts | The peak line to line Voltage at the terminals of the machine (taken from terminal voltage graph) |
| [[motorcad/parameter_database/parameters/PeakPhaseVoltage|PeakPhaseVoltage]] | o/p | double | Volts | The peak Phase Voltage at the terminals of the machine (taken from terminal voltage graph) |
| [[motorcad/parameter_database/parameters/PeakTerminalVoltage_PMDC|PeakTerminalVoltage_PMDC]] | o/p | double | Volts | The peak voltage at the terminals of the machine on load (taken from terminal voltage graph) |
| [[motorcad/parameter_database/parameters/PhaseAdvance|PhaseAdvance]] | i/p | double | EDeg | The phase advance in electrical degrees |
| [[motorcad/parameter_database/parameters/PhaseCurrent|PhaseCurrent]] | o/p | double | Amps | The Phase Current (peak) |
| [[motorcad/parameter_database/parameters/PhaseCurrentAngle_Aux|PhaseCurrentAngle_Aux]] | o/p | double | EDeg | Angle of the aux winding phase current |
| [[motorcad/parameter_database/parameters/PhaseCurrentAngle_Main|PhaseCurrentAngle_Main]] | o/p | double | EDeg | Angle of the main winding phase current |
| [[motorcad/parameter_database/parameters/PhaseCurrent_Aux_RMS|PhaseCurrent_Aux_RMS]] | o/p | double | Amps | The aux winding RMS phase current |
| [[motorcad/parameter_database/parameters/PhaseCurrent_Main_RMS|PhaseCurrent_Main_RMS]] | o/p | double | Amps | The main winding RMS phase current |
| [[motorcad/parameter_database/parameters/PhaseVoltage|PhaseVoltage]] | o/p | double | Volts | The rms Phase Voltage at the output of the supply |
| [[motorcad/parameter_database/parameters/PhasorAngle|PhasorAngle]] | o/p | double | EDeg | The Phasor Angle calculated for initial rotor position from winding pattern |
| [[motorcad/parameter_database/parameters/PhasorDiagram_PhaseAdvanceAngle|PhasorDiagram_PhaseAdvanceAngle]] | i/p | double | EDeg | Phase Advance angle used in phasor diagram |
| [[motorcad/parameter_database/parameters/PhasorDiagram_PhaseAdvanceSetting|PhasorDiagram_PhaseAdvanceSetting]] | i/p | integer | N/A | Automatic will use the phase advance set in the calculation sheet, user allows user to specify own value |
| [[motorcad/parameter_database/parameters/PhasorLength|PhasorLength]] | o/p | double | N/A | The Phasor Length calculated from winding pattern |
| [[motorcad/parameter_database/parameters/PhasorLoadAngle|PhasorLoadAngle]] | o/p | double | EDeg | Load Angle from phasor diagram |
| [[motorcad/parameter_database/parameters/PhasorOffsetAngle|PhasorOffsetAngle]] | o/p | double | EDeg | The Phasor Offset Angle calculated for initial rotor position from winding pattern |
| [[motorcad/parameter_database/parameters/PhasorPowerFactor|PhasorPowerFactor]] | o/p | double | N/A | Power Factor from phasor diagram |
| [[motorcad/parameter_database/parameters/PhasorPowerFactorAngle|PhasorPowerFactorAngle]] | o/p | double | EDeg | Power Factor Angle from phasor diagram |
| [[motorcad/parameter_database/parameters/PhasorPowerFactorAngleMethod|PhasorPowerFactorAngleMethod]] | compatibility | integer | N/A | Method used to calculate the Phasor Power Factor Angle |
| [[motorcad/parameter_database/parameters/PhasorRmsPhaseVoltage|PhasorRmsPhaseVoltage]] | o/p | double | Volts | The rms Phase Voltage at the terminals of the machine from phasor diagram |
| [[motorcad/parameter_database/parameters/PhasorRmsPhaseVoltage_D|PhasorRmsPhaseVoltage_D]] | o/p | double | Volts | The rms Phase Voltage at the terminals of the machine from phasor diagram |
| [[motorcad/parameter_database/parameters/PhasorRmsPhaseVoltage_Q|PhasorRmsPhaseVoltage_Q]] | o/p | double | Volts | The rms Phase Voltage at the terminals of the machine from phasor diagram |
| [[motorcad/parameter_database/parameters/PhysicalModelType|PhysicalModelType]] | setting | integer | N/A | This defines the type of model (magnetic+thermal, magnetic, thermal, mechanical) |
| [[motorcad/parameter_database/parameters/PositionPoints_Calculated_MagnetisationCurves|PositionPoints_Calculated_MagnetisationCurves]] | i/p | integer | N/A | The number of position points in the magnetisation curves |
| [[motorcad/parameter_database/parameters/PulsatingTorque|PulsatingTorque]] | o/p | double | Nm | The pulsating torque |
| [[motorcad/parameter_database/parameters/QAxisCurrentCalculation|QAxisCurrentCalculation]] | i/p | boolean | N/A | When selected Q axis only current calculation is run (this should normally be set to true) |
| [[motorcad/parameter_database/parameters/RMSBackEMFLine|RMSBackEMFLine]] | o/p | double | Volts | RMS back EMF line to line voltage in open circuit |
| [[motorcad/parameter_database/parameters/RMSCurrent|RMSCurrent]] | i/p | double | Amps | The rms line current |
| [[motorcad/parameter_database/parameters/RMSCurrentDensity|RMSCurrentDensity]] | i/p | double | Amps/mm² | The rms current density |
| [[motorcad/parameter_database/parameters/RMSExternalLineResistiveVoltage|RMSExternalLineResistiveVoltage]] | o/p | double | Volts | The rms external resistive Voltage |
| [[motorcad/parameter_database/parameters/RMSExternalLineResistiveVoltage_D|RMSExternalLineResistiveVoltage_D]] | o/p | double | Volts | The rms D axis external resistive Voltage |
| [[motorcad/parameter_database/parameters/RMSExternalLineResistiveVoltage_Q|RMSExternalLineResistiveVoltage_Q]] | o/p | double | Volts | The rms Q axis external resistive Voltage |
| [[motorcad/parameter_database/parameters/RMSPhaseCurrent|RMSPhaseCurrent]] | o/p | double | Amps | The calculated rms phase current |
| [[motorcad/parameter_database/parameters/RMSPhaseCurrent_D|RMSPhaseCurrent_D]] | o/p | double | Amps | The Phase Current (rms)[D axis] |
| [[motorcad/parameter_database/parameters/RMSPhaseCurrent_Q|RMSPhaseCurrent_Q]] | o/p | double | Amps | The Phase Current (rms)[Q axis] |
| [[motorcad/parameter_database/parameters/RMSPhaseReactiveVoltage_D|RMSPhaseReactiveVoltage_D]] | o/p | double | Volts | The reactive voltage drop D axis (Q axis current x Q axis inductance) |
| [[motorcad/parameter_database/parameters/RMSPhaseReactiveVoltage_Q|RMSPhaseReactiveVoltage_Q]] | o/p | double | Volts | The reactive voltage drop in Q axis (D axis current x D axis inductance) |
| [[motorcad/parameter_database/parameters/RMSPhaseResistiveVoltage|RMSPhaseResistiveVoltage]] | o/p | double | Volts | The rms Phase resistive Voltage |
| [[motorcad/parameter_database/parameters/RMSPhaseResistiveVoltage_D|RMSPhaseResistiveVoltage_D]] | o/p | double | Volts | The rms D axis Phase resistive Voltage |
| [[motorcad/parameter_database/parameters/RMSPhaseResistiveVoltage_Q|RMSPhaseResistiveVoltage_Q]] | o/p | double | Volts | The rms Q axis Phase resistive Voltage |
| [[motorcad/parameter_database/parameters/RMSTerminalVoltage_PMDC|RMSTerminalVoltage_PMDC]] | o/p | double | Volts | The RMS voltage at the terminals of the machine on load (taken from terminal voltage graph) |
| [[motorcad/parameter_database/parameters/RadialForceHarmonicAngles_OC|RadialForceHarmonicAngles_OC]] | o/p | double | MDeg | Radial force harmonic angles created from Open Circuit calculations |
| [[motorcad/parameter_database/parameters/RadialForceHarmonicAngles_OL|RadialForceHarmonicAngles_OL]] | o/p | double | MDeg | Radial force harmonic angles created from On Load calculations |
| [[motorcad/parameter_database/parameters/RadialForceHarmonics_OC|RadialForceHarmonics_OC]] | o/p | double | N | Radial force harmonics created from Open Circuit calculations |
| [[motorcad/parameter_database/parameters/RadialForceHarmonics_OL|RadialForceHarmonics_OL]] | o/p | double | N | Radial force harmonics created from On Load calculations |
| [[motorcad/parameter_database/parameters/RadialForceRipple_OC_Rotor|RadialForceRipple_OC_Rotor]] | o/p | double | N | The maximum peak-peak variation in rotor force during the open circuit transient at any point in the machine |
| [[motorcad/parameter_database/parameters/RadialForceRipple_OC_Stator|RadialForceRipple_OC_Stator]] | o/p | double | N | The maximum peak-peak variation in stator force during the open circuit transient at any point in the machine |
| [[motorcad/parameter_database/parameters/RadialForceRipple_OL_Rotor|RadialForceRipple_OL_Rotor]] | o/p | double | N | The maximum peak-peak variation in rotor force during the on load transient at any point in the machine |
| [[motorcad/parameter_database/parameters/RadialForceRipple_OL_Stator|RadialForceRipple_OL_Stator]] | o/p | double | N | The maximum peak-peak variation in stator force during the on load transient at any point in the machine |
| [[motorcad/parameter_database/parameters/RadialForce_OC|RadialForce_OC]] | o/p | double | N | The open circuit radial force |
| [[motorcad/parameter_database/parameters/RadialForce_OL|RadialForce_OL]] | o/p | double | N | The On Load radial force |
| [[motorcad/parameter_database/parameters/ReactanceLineToLineFromDQ|ReactanceLineToLineFromDQ]] | o/p | double | Ohms | The line to line reactance from DQ inductance calculation |
| [[motorcad/parameter_database/parameters/ReactanceLineToLineSkewFromDQ|ReactanceLineToLineSkewFromDQ]] | o/p | double | Ohms | The line to line reactance from DQ inductance calculation for skewed machine |
| [[motorcad/parameter_database/parameters/ReactanceLoadSkew_D|ReactanceLoadSkew_D]] | o/p | double | Ohms | The reactance in D axis for skewed machine |
| [[motorcad/parameter_database/parameters/ReactanceLoadSkew_Q|ReactanceLoadSkew_Q]] | o/p | double | Ohms | The reactance in Q axis for skewed machine |
| [[motorcad/parameter_database/parameters/ReactanceLoad_D|ReactanceLoad_D]] | o/p | double | Ohms | The reactance in D axis |
| [[motorcad/parameter_database/parameters/ReactanceLoad_Q|ReactanceLoad_Q]] | o/p | double | Ohms | The reactance in Q axis |
| [[motorcad/parameter_database/parameters/RectifierDiodePower|RectifierDiodePower]] | o/p | double | Watts | The power dissipated by the rectifier diodes |
| [[motorcad/parameter_database/parameters/RectifierLosses|RectifierLosses]] | o/p | double | Watts | The passive rectifier losses |
| [[motorcad/parameter_database/parameters/RectifierOutputResistance|RectifierOutputResistance]] | i/p | double | Ohms | The output resistance of the passive generator rectifier |
| [[motorcad/parameter_database/parameters/RectifierResistorPower|RectifierResistorPower]] | o/p | double | Watts | The power dissipated by the rectifier output resistance |
| [[motorcad/parameter_database/parameters/RectifierResistorVoltage|RectifierResistorVoltage]] | o/p | double | Volts | The voltage over the rectifier output resistance |
| [[motorcad/parameter_database/parameters/RmsBackEMFPhase|RmsBackEMFPhase]] | o/p | double | Volts | RMS back EMF phase voltage in open circuit |
| [[motorcad/parameter_database/parameters/RmsBackEMF_PMDC|RmsBackEMF_PMDC]] | o/p | double | Volts | RMS back EMF voltage in open circuit |
| [[motorcad/parameter_database/parameters/RmsCurrentCalc|RmsCurrentCalc]] | o/p | double | Amps | The calculated rms line current |
| [[motorcad/parameter_database/parameters/RmsLineLineVoltage|RmsLineLineVoltage]] | o/p | double | Volts | The rms line to line Voltage at the terminals of the machine (taken from terminal voltage graph) |
| [[motorcad/parameter_database/parameters/RmsPhaseDriveVoltage|RmsPhaseDriveVoltage]] | o/p | double | Volts | The required rms Phase Voltage at the output of the drive taking into account sine filter |
| [[motorcad/parameter_database/parameters/RmsPhaseDriveVoltage_D|RmsPhaseDriveVoltage_D]] | o/p | double | Volts | The required rms D axis Phase Voltage at the output of the drive taking into account sine filter |
| [[motorcad/parameter_database/parameters/RmsPhaseDriveVoltage_Q|RmsPhaseDriveVoltage_Q]] | o/p | double | Volts | The required rms Q axis Phase Voltage at the output of the drive taking into account sine filter |
| [[motorcad/parameter_database/parameters/RmsPhaseDrive_Current|RmsPhaseDrive_Current]] | o/p | double | Amps | The rms current from drive through the sine filter inductance |
| [[motorcad/parameter_database/parameters/RmsPhaseDrive_Current_D|RmsPhaseDrive_Current_D]] | o/p | double | Amps | The rms current through the sine filter inductance |
| [[motorcad/parameter_database/parameters/RmsPhaseDrive_Current_Q|RmsPhaseDrive_Current_Q]] | o/p | double | Amps | The rms current through the sine filter inductance |
| [[motorcad/parameter_database/parameters/RmsPhaseVoltage|RmsPhaseVoltage]] | o/p | double | Volts | The rms Phase Voltage at the terminals of the machine (taken from terminal voltage graph) |
| [[motorcad/parameter_database/parameters/RmsSineFilterCapacitance_PhaseCurrent|RmsSineFilterCapacitance_PhaseCurrent]] | o/p | double | Amps | The rms current through the sine filter capacitance |
| [[motorcad/parameter_database/parameters/RmsSineFilterCapacitance_PhaseCurrent_D|RmsSineFilterCapacitance_PhaseCurrent_D]] | o/p | double | Amps | The rms current through the sine filter capacitance in D axis |
| [[motorcad/parameter_database/parameters/RmsSineFilterCapacitance_PhaseCurrent_Q|RmsSineFilterCapacitance_PhaseCurrent_Q]] | o/p | double | Amps | The rms current through the sine filter capacitance in Q axis |
| [[motorcad/parameter_database/parameters/RmsSineFilterInductance_Voltage|RmsSineFilterInductance_Voltage]] | o/p | double | Volts | The rms Voltage across the sine filter inductance |
| [[motorcad/parameter_database/parameters/RmsSineFilterInductance_Voltage_D|RmsSineFilterInductance_Voltage_D]] | o/p | double | Volts | The D axis rms Voltage across the sine filter inductance |
| [[motorcad/parameter_database/parameters/RmsSineFilterInductance_Voltage_Q|RmsSineFilterInductance_Voltage_Q]] | o/p | double | Volts | The Q axis rms Voltage across the sine filter inductance |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy|RotorBackIronLoss_Eddy]] | o/p | double | Watts | Rotor back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy_Adj|RotorBackIronLoss_Eddy_Adj]] | o/p | double | Watts | Rotor back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy_Adj_OC|RotorBackIronLoss_Eddy_Adj_OC]] | o/p | double | Watts | Rotor back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy_Analytic|RotorBackIronLoss_Eddy_Analytic]] | o/p | double | Watts | Rotor back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy_Analytic_Adj|RotorBackIronLoss_Eddy_Analytic_Adj]] | o/p | double | Watts | Rotor back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy_OC|RotorBackIronLoss_Eddy_OC]] | o/p | double | Watts | Rotor back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy_Static|RotorBackIronLoss_Eddy_Static]] | o/p | double | Watts | Rotor back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Eddy_Static_Adj|RotorBackIronLoss_Eddy_Static_Adj]] | o/p | double | Watts | Rotor back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Exc_Analytic|RotorBackIronLoss_Exc_Analytic]] | o/p | double | Watts | Rotor back iron excess losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Exc_Static|RotorBackIronLoss_Exc_Static]] | o/p | double | Watts | Rotor back iron excess losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Excess|RotorBackIronLoss_Excess]] | o/p | double | Watts | Rotor back iron excess losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Excess_OC|RotorBackIronLoss_Excess_OC]] | o/p | double | Watts | Rotor back iron excess losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Fundamental_Hys|RotorBackIronLoss_Fundamental_Hys]] | o/p | double | Watts | Rotor back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys|RotorBackIronLoss_Hys]] | o/p | double | Watts | Rotor back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys_Adj|RotorBackIronLoss_Hys_Adj]] | o/p | double | Watts | Rotor back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys_Adj_OC|RotorBackIronLoss_Hys_Adj_OC]] | o/p | double | Watts | Rotor back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys_Analytic|RotorBackIronLoss_Hys_Analytic]] | o/p | double | Watts | Rotor back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys_Analytic_Adj|RotorBackIronLoss_Hys_Analytic_Adj]] | o/p | double | Watts | Rotor back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys_OC|RotorBackIronLoss_Hys_OC]] | o/p | double | Watts | Rotor back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys_Static|RotorBackIronLoss_Hys_Static]] | o/p | double | Watts | Rotor back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Hys_Static_Adj|RotorBackIronLoss_Hys_Static_Adj]] | o/p | double | Watts | Rotor back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Minor_Hys|RotorBackIronLoss_Minor_Hys]] | o/p | double | Watts | Rotor back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total|RotorBackIronLoss_Total]] | o/p | double | Watts | Total Rotor back iron losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total_Adj|RotorBackIronLoss_Total_Adj]] | o/p | double | Watts | Rotor back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total_Adj_OC|RotorBackIronLoss_Total_Adj_OC]] | o/p | double | Watts | Rotor back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total_Analytic|RotorBackIronLoss_Total_Analytic]] | o/p | double | Watts | Total Rotor back iron losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total_Analytic_Adj|RotorBackIronLoss_Total_Analytic_Adj]] | o/p | double | Watts | Total Rotor back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total_OC|RotorBackIronLoss_Total_OC]] | o/p | double | Watts | Total Rotor back iron losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total_Static|RotorBackIronLoss_Total_Static]] | o/p | double | Watts | Total Rotor back iron losses |
| [[motorcad/parameter_database/parameters/RotorBackIronLoss_Total_Static_Adj|RotorBackIronLoss_Total_Static_Adj]] | o/p | double | Watts | Total Rotor back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorBarFillFactor_Bottom|RotorBarFillFactor_Bottom]] | i/p | double | N/A | Multiplier used to adjust cross-sectional area of bottom rotor bar and opening |
| [[motorcad/parameter_database/parameters/RotorBarFillFactor_Top|RotorBarFillFactor_Top]] | i/p | double | N/A | Multiplier used to adjust cross-sectional area of top rotor bar and opening |
| [[motorcad/parameter_database/parameters/RotorBarLoss|RotorBarLoss]] | o/p | double | Watts | Rotor Bar Loss of IM machine |
| [[motorcad/parameter_database/parameters/RotorBar_Resistivity|RotorBar_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the rotor bars at rotor bar temperature |
| [[motorcad/parameter_database/parameters/RotorBar_ResistivityAt20|RotorBar_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity for the rotor bars at reference temperature |
| [[motorcad/parameter_database/parameters/RotorBar_Temperature|RotorBar_Temperature]] | i/p | double | °C | The temperature of the rotor bars used for loss calculation |
| [[motorcad/parameter_database/parameters/RotorCentreOffset_R|RotorCentreOffset_R]] | i/p | double | mm | The rotor centre eccentricity distance |
| [[motorcad/parameter_database/parameters/RotorCentreOffset_T|RotorCentreOffset_T]] | i/p | double | MDeg | The eccentricity angle [mechanical degrees] of rotor centre |
| [[motorcad/parameter_database/parameters/RotorDifferentialLeakageInductance|RotorDifferentialLeakageInductance]] | o/p | double | Henry | Rotor Differential Leakage Inductance |
| [[motorcad/parameter_database/parameters/RotorDifferentialLeakageReactance|RotorDifferentialLeakageReactance]] | o/p | double | Ohms | Rotor Differential Leakage Reactance |
| [[motorcad/parameter_database/parameters/RotorDifferentialLeakageReactance_Ref|RotorDifferentialLeakageReactance_Ref]] | o/p | double | Ohms | Rotor Differential Leakage Reactance |
| [[motorcad/parameter_database/parameters/RotorEccentricityType|RotorEccentricityType]] | i/p | integer | N/A | The rotor eccentricity type |
| [[motorcad/parameter_database/parameters/RotorHysterisisCalculation|RotorHysterisisCalculation]] | compatibility | integer | N/A | Method used for calculating the rotor hysteresis losses |
| [[motorcad/parameter_database/parameters/RotorHysterisisCalculation_SRM|RotorHysterisisCalculation_SRM]] | compatibility | integer | N/A | Method used for calculating the rotor hysteresis losses for SRM |
| [[motorcad/parameter_database/parameters/RotorInertia|RotorInertia]] | o/p | double | kg.m² | Rotor Inertia |
| [[motorcad/parameter_database/parameters/RotorIronLossBuildFactor|RotorIronLossBuildFactor]] | i/p | double | N/A | Multiplier used to adjust rotor iron losses |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total|RotorIronLoss_Total]] | o/p | double | Watts | Total Rotor iron losses |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total_Adj|RotorIronLoss_Total_Adj]] | o/p | double | Watts | Total Rotor iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total_Adj_OC|RotorIronLoss_Total_Adj_OC]] | o/p | double | Watts | Total Rotor iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total_Analytic|RotorIronLoss_Total_Analytic]] | o/p | double | Watts | Total Rotor iron losses |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total_Analytic_Adj|RotorIronLoss_Total_Analytic_Adj]] | o/p | double | Watts | Total Rotor iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total_OC|RotorIronLoss_Total_OC]] | o/p | double | Watts | Total Rotor iron losses |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total_Static|RotorIronLoss_Total_Static]] | o/p | double | Watts | Total Rotor iron losses |
| [[motorcad/parameter_database/parameters/RotorIronLoss_Total_Static_Adj|RotorIronLoss_Total_Static_Adj]] | o/p | double | Watts | Total Rotor iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorLam_Resistivity|RotorLam_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the rotor lamination at rotor temperature |
| [[motorcad/parameter_database/parameters/RotorLam_ResistivityAt20C|RotorLam_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the rotor lamination at reference temperature |
| [[motorcad/parameter_database/parameters/RotorLam_Temperature|RotorLam_Temperature]] | i/p | double | °C | The temperature of the rotor lamination used for loss calculation |
| [[motorcad/parameter_database/parameters/RotorLaminations|RotorLaminations]] | i/p | integer | N/A | Whether rotor is laminated or solid |
| [[motorcad/parameter_database/parameters/RotorLeakageInductance_Multiplier|RotorLeakageInductance_Multiplier]] | i/p | double | N/A | Multiplier used to adjust the Rotor leakage inductance |
| [[motorcad/parameter_database/parameters/RotorLeakageInductance_Skewed|RotorLeakageInductance_Skewed]] | o/p | double | Henry | The additional rotor leakage inductance component due to skew |
| [[motorcad/parameter_database/parameters/RotorLeakageInductance_Total|RotorLeakageInductance_Total]] | o/p | double | Henry | The total rotor leakage inductance |
| [[motorcad/parameter_database/parameters/RotorLeakageInductance_Total_Ref|RotorLeakageInductance_Total_Ref]] | o/p | double | Henry | The total rotor leakage inductance referred to the stator |
| [[motorcad/parameter_database/parameters/RotorLeakageInductance_Total_Ref_Aux|RotorLeakageInductance_Total_Ref_Aux]] | o/p | double | Henry | The total rotor leakage inductance referred to the aux windings |
| [[motorcad/parameter_database/parameters/RotorLeakageReactance_Skewed|RotorLeakageReactance_Skewed]] | o/p | double | Ohms | The additional rotor leakage reactance component due to skew |
| [[motorcad/parameter_database/parameters/RotorLeakageReactance_Total|RotorLeakageReactance_Total]] | o/p | double | Ohms | The total rotor leakage reactance |
| [[motorcad/parameter_database/parameters/RotorLeakageReactance_Total_Ref|RotorLeakageReactance_Total_Ref]] | o/p | double | Ohms | The total rotor leakage reactance referred to the stator |
| [[motorcad/parameter_database/parameters/RotorLeakageReactance_Total_Ref_L|RotorLeakageReactance_Total_Ref_L]] | o/p | double | Ohms | The total rotor leakage reactance |
| [[motorcad/parameter_database/parameters/RotorLoss_Eddy|RotorLoss_Eddy]] | o/p | double | Watts | Rotor iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorLoss_Eddy_Adj|RotorLoss_Eddy_Adj]] | o/p | double | Watts | Rotor iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorLoss_Eddy_Adj_OC|RotorLoss_Eddy_Adj_OC]] | o/p | double | Watts | Rotor iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorLoss_Eddy_OC|RotorLoss_Eddy_OC]] | o/p | double | Watts | Rotor iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorLoss_Excess|RotorLoss_Excess]] | o/p | double | Watts | Rotor iron excess losses |
| [[motorcad/parameter_database/parameters/RotorLoss_Excess_OC|RotorLoss_Excess_OC]] | o/p | double | Watts | Rotor iron excess losses |
| [[motorcad/parameter_database/parameters/RotorLoss_Fundamental_Hys|RotorLoss_Fundamental_Hys]] | o/p | double | Watts | Rotor iron losses from hysteresis (fundamental component) |
| [[motorcad/parameter_database/parameters/RotorLoss_Hys|RotorLoss_Hys]] | o/p | double | Watts | Rotor iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorLoss_Hys_Adj|RotorLoss_Hys_Adj]] | o/p | double | Watts | Rotor iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorLoss_Hys_Adj_OC|RotorLoss_Hys_Adj_OC]] | o/p | double | Watts | Rotor iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorLoss_Hys_OC|RotorLoss_Hys_OC]] | o/p | double | Watts | Rotor iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorLoss_Minor_Hys|RotorLoss_Minor_Hys]] | o/p | double | Watts | Rotor iron losses from hysteresis (minor loops component) |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Eddy|RotorMagnetPoleLoss_Eddy]] | o/p | double | Watts | Rotor magnet pole losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Eddy_Adj|RotorMagnetPoleLoss_Eddy_Adj]] | o/p | double | Watts | Rotor magnet pole losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Eddy_Adj_OC|RotorMagnetPoleLoss_Eddy_Adj_OC]] | o/p | double | Watts | Rotor magnet pole losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Eddy_OC|RotorMagnetPoleLoss_Eddy_OC]] | o/p | double | Watts | Rotor magnet pole losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Excess|RotorMagnetPoleLoss_Excess]] | o/p | double | Watts | Rotor magnet pole excess losses |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Excess_OC|RotorMagnetPoleLoss_Excess_OC]] | o/p | double | Watts | Rotor magnet pole excess losses |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Fundamental_Hys|RotorMagnetPoleLoss_Fundamental_Hys]] | o/p | double | Watts | Rotor magnet pole losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Hys|RotorMagnetPoleLoss_Hys]] | o/p | double | Watts | Rotor magnet pole losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Hys_Adj|RotorMagnetPoleLoss_Hys_Adj]] | o/p | double | Watts | Rotor magnet pole losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Hys_Adj_OC|RotorMagnetPoleLoss_Hys_Adj_OC]] | o/p | double | Watts | Rotor magnet pole losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Hys_OC|RotorMagnetPoleLoss_Hys_OC]] | o/p | double | Watts | Rotor magnet pole losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Minor_Hys|RotorMagnetPoleLoss_Minor_Hys]] | o/p | double | Watts | Rotor magnet pole losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Total|RotorMagnetPoleLoss_Total]] | o/p | double | Watts | Total Rotor magnet pole losses |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Total_Adj|RotorMagnetPoleLoss_Total_Adj]] | o/p | double | Watts | Rotor magnet pole losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Total_Adj_OC|RotorMagnetPoleLoss_Total_Adj_OC]] | o/p | double | Watts | Rotor magnet pole losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorMagnetPoleLoss_Total_OC|RotorMagnetPoleLoss_Total_OC]] | o/p | double | Watts | Total Rotor magnet pole losses |
| [[motorcad/parameter_database/parameters/RotorResistance_Referred_BPM|RotorResistance_Referred_BPM]] | o/p | double | Ohms | The referred resistance of the rotor |
| [[motorcad/parameter_database/parameters/RotorResistance_Total|RotorResistance_Total]] | o/p | double | Ohms | The total rotor Resistance |
| [[motorcad/parameter_database/parameters/RotorResistance_Total_Ref|RotorResistance_Total_Ref]] | o/p | double | Ohms | The total referred rotor Resistance |
| [[motorcad/parameter_database/parameters/RotorResistance_Total_Ref_L|RotorResistance_Total_Ref_L]] | o/p | double | Ohms | The total referred rotor Resistance |
| [[motorcad/parameter_database/parameters/RotorSaturationMultiplier|RotorSaturationMultiplier]] | i/p | double | N/A | Multiplier used to adjust the level of rotor saturation |
| [[motorcad/parameter_database/parameters/RotorSkewAngle_Array|RotorSkewAngle_Array]] | i/p | double | MDeg | The rotor skew angle for BPM machines |
| [[motorcad/parameter_database/parameters/RotorSkewLengthProp_Array|RotorSkewLengthProp_Array]] | i/p | double | mm | The proportional rotor skew length for BPM machines |
| [[motorcad/parameter_database/parameters/RotorSkewSlices|RotorSkewSlices]] | i/p | integer | N/A | Number of rotor skew slices |
| [[motorcad/parameter_database/parameters/RotorStatorTransformCurrent|RotorStatorTransformCurrent]] | o/p | double | N/A | Muliplication factor to get the referred stator parameters from the rotor |
| [[motorcad/parameter_database/parameters/RotorStatorTransformCurrent_Aux|RotorStatorTransformCurrent_Aux]] | o/p | double | N/A | Muliplication factor to get the referred stator currents from the rotor (aux winding) |
| [[motorcad/parameter_database/parameters/RotorStatorTransformImpedance|RotorStatorTransformImpedance]] | o/p | double | N/A | Muliplication factor to get the referred stator parameters from the rotor |
| [[motorcad/parameter_database/parameters/RotorStatorTransformImpedance_Aux|RotorStatorTransformImpedance_Aux]] | o/p | double | N/A | Muliplication factor to get the referred stator impedances from the rotor (aux winding) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy|RotorToothLoss_Eddy]] | o/p | double | Watts | Rotor tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy_Adj|RotorToothLoss_Eddy_Adj]] | o/p | double | Watts | Rotor tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy_Adj_OC|RotorToothLoss_Eddy_Adj_OC]] | o/p | double | Watts | Rotor tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy_Analytic|RotorToothLoss_Eddy_Analytic]] | o/p | double | Watts | Rotor tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy_Analytic_Adj|RotorToothLoss_Eddy_Analytic_Adj]] | o/p | double | Watts | Rotor tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy_OC|RotorToothLoss_Eddy_OC]] | o/p | double | Watts | Rotor tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy_Static|RotorToothLoss_Eddy_Static]] | o/p | double | Watts | Rotor tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Eddy_Static_Adj|RotorToothLoss_Eddy_Static_Adj]] | o/p | double | Watts | Rotor tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Exc_Analytic|RotorToothLoss_Exc_Analytic]] | o/p | double | Watts | Rotor tooth excess losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Exc_Static|RotorToothLoss_Exc_Static]] | o/p | double | Watts | Rotor tooth excess losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Excess|RotorToothLoss_Excess]] | o/p | double | Watts | Rotor tooth excess losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Excess_OC|RotorToothLoss_Excess_OC]] | o/p | double | Watts | Rotor tooth excess losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Fundamental_Hys|RotorToothLoss_Fundamental_Hys]] | o/p | double | Watts | Rotor tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys|RotorToothLoss_Hys]] | o/p | double | Watts | Rotor tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys_Adj|RotorToothLoss_Hys_Adj]] | o/p | double | Watts | Rotor tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys_Adj_OC|RotorToothLoss_Hys_Adj_OC]] | o/p | double | Watts | Rotor tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys_Analytic|RotorToothLoss_Hys_Analytic]] | o/p | double | Watts | Rotor tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys_Analytic_Adj|RotorToothLoss_Hys_Analytic_Adj]] | o/p | double | Watts | Rotor tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys_OC|RotorToothLoss_Hys_OC]] | o/p | double | Watts | Rotor tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys_Static|RotorToothLoss_Hys_Static]] | o/p | double | Watts | Rotor tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Hys_Static_Adj|RotorToothLoss_Hys_Static_Adj]] | o/p | double | Watts | Rotor tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Minor_Hys|RotorToothLoss_Minor_Hys]] | o/p | double | Watts | Rotor tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total|RotorToothLoss_Total]] | o/p | double | Watts | Total Rotor tooth losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total_Adj|RotorToothLoss_Total_Adj]] | o/p | double | Watts | Total Rotor tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total_Adj_OC|RotorToothLoss_Total_Adj_OC]] | o/p | double | Watts | Rotor tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total_Analytic|RotorToothLoss_Total_Analytic]] | o/p | double | Watts | Total Rotor tooth losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total_Analytic_Adj|RotorToothLoss_Total_Analytic_Adj]] | o/p | double | Watts | Total Rotor tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total_OC|RotorToothLoss_Total_OC]] | o/p | double | Watts | Total Rotor tooth losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total_Static|RotorToothLoss_Total_Static]] | o/p | double | Watts | Total Rotor tooth losses |
| [[motorcad/parameter_database/parameters/RotorToothLoss_Total_Static_Adj|RotorToothLoss_Total_Static_Adj]] | o/p | double | Watts | Total Rotor tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/SaturationFactor|SaturationFactor]] | o/p | double | N/A | The saturation factor (on load) |
| [[motorcad/parameter_database/parameters/SecondOrderTransientReactance_D|SecondOrderTransientReactance_D]] | o/p | double | Ohms | The second order transient reactance in D axis |
| [[motorcad/parameter_database/parameters/SecondOrderTransientReactance_Q|SecondOrderTransientReactance_Q]] | o/p | double | Ohms | The second order transient reactance in Q axis |
| [[motorcad/parameter_database/parameters/SecondOrderTransientTimeConstant|SecondOrderTransientTimeConstant]] | o/p | double | sec | The second order transient time constant (Td'') |
| [[motorcad/parameter_database/parameters/SelfInductance|SelfInductance]] | o/p | double | Henry | Self Inductance of winding |
| [[motorcad/parameter_database/parameters/SelfInductanceSkew|SelfInductanceSkew]] | o/p | double | Henry | Self Inductance of winding for skewed machine |
| [[motorcad/parameter_database/parameters/ShaftCentreOffset_R|ShaftCentreOffset_R]] | i/p | double | mm | The shaft centre eccentricity distance |
| [[motorcad/parameter_database/parameters/ShaftCentreOffset_T|ShaftCentreOffset_T]] | i/p | double | MDeg | The eccentricity angle [mechanical degrees] of shaft centre |
| [[motorcad/parameter_database/parameters/ShaftHole_Inertia_Calc|ShaftHole_Inertia_Calc]] | compatibility | integer | N/A | The calculation method of shaft and rotor inertia for machines with a shaft hole or spokes |
| [[motorcad/parameter_database/parameters/ShaftInertia|ShaftInertia]] | o/p | double | kg.m² | Shaft Inertia |
| [[motorcad/parameter_database/parameters/ShaftLossBuildFactor|ShaftLossBuildFactor]] | i/p | double | N/A | Multiplier used to adjust shaft iron losses |
| [[motorcad/parameter_database/parameters/ShaftLoss_Eddy|ShaftLoss_Eddy]] | o/p | double | Watts | Shaft losses from eddy currents |
| [[motorcad/parameter_database/parameters/ShaftLoss_Eddy_OC|ShaftLoss_Eddy_OC]] | o/p | double | Watts | Shaft losses from eddy currents |
| [[motorcad/parameter_database/parameters/ShaftLoss_Excess|ShaftLoss_Excess]] | o/p | double | Watts | Shaft excess losses |
| [[motorcad/parameter_database/parameters/ShaftLoss_Excess_OC|ShaftLoss_Excess_OC]] | o/p | double | Watts | Shaft excess losses |
| [[motorcad/parameter_database/parameters/ShaftLoss_Hys|ShaftLoss_Hys]] | o/p | double | Watts | Shaft losses from hysteresis |
| [[motorcad/parameter_database/parameters/ShaftLoss_Hys_OC|ShaftLoss_Hys_OC]] | o/p | double | Watts | Shaft losses from hysteresis |
| [[motorcad/parameter_database/parameters/ShaftLoss_Total|ShaftLoss_Total]] | o/p | double | Watts | Total shaft losses |
| [[motorcad/parameter_database/parameters/ShaftLoss_Total_Adj|ShaftLoss_Total_Adj]] | o/p | double | Watts | Shaft losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/ShaftLoss_Total_Adj_OC|ShaftLoss_Total_Adj_OC]] | o/p | double | Watts | Shaft losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/ShaftLoss_Total_OC|ShaftLoss_Total_OC]] | o/p | double | Watts | Total shaft losses |
| [[motorcad/parameter_database/parameters/ShaftTorque|ShaftTorque]] | o/p | double | Nm | Torque at shaft of machine taking into account drag losses |
| [[motorcad/parameter_database/parameters/Shaft_Resistivity|Shaft_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the shaft at shaft temperature |
| [[motorcad/parameter_database/parameters/Shaft_ResistivityAt20C|Shaft_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the shaft at reference temperature |
| [[motorcad/parameter_database/parameters/Shaft_Temperature|Shaft_Temperature]] | i/p | double | °C | The temperature of the shaft used for loss calculation |
| [[motorcad/parameter_database/parameters/ShortCircuitBrakingTorque|ShortCircuitBrakingTorque]] | o/p | double | Nm | Short Circuit Braking Torque |
| [[motorcad/parameter_database/parameters/ShortCircuitCurrentDensity_Peak|ShortCircuitCurrentDensity_Peak]] | o/p | double | Amps/mm² | The peak short circuit current density |
| [[motorcad/parameter_database/parameters/ShortCircuitCurrentDensity_Rms|ShortCircuitCurrentDensity_Rms]] | o/p | double | Amps/mm² | The rms short circuit current density |
| [[motorcad/parameter_database/parameters/ShortCircuitLineCurrent|ShortCircuitLineCurrent]] | o/p | double | Amps | The peak short circuit line current |
| [[motorcad/parameter_database/parameters/SineFilter_Capacitance|SineFilter_Capacitance]] | i/p | double | Farad | Size of sine filter capacitance used at input of machine (µF), used for calculating the required drive voltage |
| [[motorcad/parameter_database/parameters/SineFilter_Inductance|SineFilter_Inductance]] | i/p | double | Henry | Size of sine filter inductance used at input of machine (mH), used for calculating the required drive voltage |
| [[motorcad/parameter_database/parameters/SinglePointDemagCalcMethod|SinglePointDemagCalcMethod]] | compatibility | integer | N/A | Method used for demagnetisation calculations when using single point FEA |
| [[motorcad/parameter_database/parameters/SkewAngle_FluxSkewFactor|SkewAngle_FluxSkewFactor]] | i/p | double | N/A | Skew Angle used when flux skew factor was last calculated |
| [[motorcad/parameter_database/parameters/SkewType|SkewType]] | i/p | integer | N/A | Stator skew type |
| [[motorcad/parameter_database/parameters/SkinDepth_Magnet|SkinDepth_Magnet]] | o/p | double | mm | Skin depth of magnets |
| [[motorcad/parameter_database/parameters/Sleeve2D3DFactor|Sleeve2D3DFactor]] | o/p | double | N/A | Factor used to convert sleeve loss in W/m to total losses for machine. Also takes into account any axial segmentation. |
| [[motorcad/parameter_database/parameters/SleeveAxialLengthMultiplier|SleeveAxialLengthMultiplier]] | i/p | double | N/A | Multiplier used to adjust the sleeve eddy-currents axial length |
| [[motorcad/parameter_database/parameters/SleeveLength_Adjusted|SleeveLength_Adjusted]] | o/p | double | mm | Stator sleeve length used in calculating sleeve loss factor |
| [[motorcad/parameter_database/parameters/SleeveLength_Effective|SleeveLength_Effective]] | o/p | double | mm | Stator sleeve length for calculating sleeve loss factor |
| [[motorcad/parameter_database/parameters/SleeveLoss|SleeveLoss]] | o/p | double | Watts | Sleeve Loss of machine |
| [[motorcad/parameter_database/parameters/SleeveLoss_OC|SleeveLoss_OC]] | o/p | double | Watts | Sleeve Loss of machine |
| [[motorcad/parameter_database/parameters/Sleeve_Resistivity|Sleeve_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the sleeve at sleeve temperature |
| [[motorcad/parameter_database/parameters/Sleeve_ResistivityAt20C|Sleeve_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the sleeve at reference temperature |
| [[motorcad/parameter_database/parameters/Sleeve_Temperature|Sleeve_Temperature]] | i/p | double | °C | The temperature of the sleeve used for loss calculation |
| [[motorcad/parameter_database/parameters/SlotForMagneticCalc_Aux|SlotForMagneticCalc_Aux]] | o/p | integer | N/A | Winding slot used for aux winding magnetic calculations |
| [[motorcad/parameter_database/parameters/SlotForMagneticCalc_Main|SlotForMagneticCalc_Main]] | o/p | integer | N/A | Winding slot used for main winding magnetic calculations |
| [[motorcad/parameter_database/parameters/SlotLeakageInductance_Stator|SlotLeakageInductance_Stator]] | o/p | double | Henry | The stator slot leakage inductance |
| [[motorcad/parameter_database/parameters/SlotLeakageReactance_Stator|SlotLeakageReactance_Stator]] | o/p | double | Ohms | The stator slot leakage reactance |
| [[motorcad/parameter_database/parameters/SlotLeakageReactance_Stator_Aux|SlotLeakageReactance_Stator_Aux]] | o/p | double | Ohms | The slot leakage reactance for the aux stator windings |
| [[motorcad/parameter_database/parameters/SolutionSymmetryAngle|SolutionSymmetryAngle]] | o/p | double | N/A | This is the minimum rotation angle required to capture a full set of transient results. |
| [[motorcad/parameter_database/parameters/SpaceVectorDriveGainFactorG2|SpaceVectorDriveGainFactorG2]] | i/p | double | N/A | Used as a multiplier for the line voltage in the space vector drive gain calculation |
| [[motorcad/parameter_database/parameters/SpeedForConstantTorque|SpeedForConstantTorque]] | o/p | double | rpm | The upper limit of machine speed for constant torque region |
| [[motorcad/parameter_database/parameters/SpeedForZeroCurrent|SpeedForZeroCurrent]] | o/p | double | rpm | The maximum machine speed at which q axis current can be applied |
| [[motorcad/parameter_database/parameters/SquareWaveDutyCycle|SquareWaveDutyCycle]] | o/p | double | N/A | The average square wave drive duty cycle after current limiting. |
| [[motorcad/parameter_database/parameters/StackingFactor_Magnetics|StackingFactor_Magnetics]] | recommended | integer | N/A | Method used for applying stacking factor in E-Magnetic calculations |
| [[motorcad/parameter_database/parameters/StallCurrent|StallCurrent]] | o/p | double | Amps | Stall current of machine with direct dc supply |
| [[motorcad/parameter_database/parameters/StallTorque|StallTorque]] | o/p | double | Nm | Stall torque of machine with direct dc supply |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy|StatorBackIronLoss_Eddy]] | o/p | double | Watts | Stator back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Adj|StatorBackIronLoss_Eddy_Adj]] | o/p | double | Watts | Stator back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Adj_OC|StatorBackIronLoss_Eddy_Adj_OC]] | o/p | double | Watts | Stator back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Analytic|StatorBackIronLoss_Eddy_Analytic]] | o/p | double | Watts | Stator back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Analytic_Adj|StatorBackIronLoss_Eddy_Analytic_Adj]] | o/p | double | Watts | Stator back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_OC|StatorBackIronLoss_Eddy_OC]] | o/p | double | Watts | Stator back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Static|StatorBackIronLoss_Eddy_Static]] | o/p | double | Watts | Stator back iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Static_Adj|StatorBackIronLoss_Eddy_Static_Adj]] | o/p | double | Watts | Stator back iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Static_Adj_PerSlice|StatorBackIronLoss_Eddy_Static_Adj_PerSlice]] | o/p | double | Watts | Stator back iron losses from eddy currents (adjusted for build factor) (per slice) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Eddy_Static_PerSlice|StatorBackIronLoss_Eddy_Static_PerSlice]] | o/p | double | Watts | Stator back iron losses from eddy currents (per slice) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Exc_Analytic|StatorBackIronLoss_Exc_Analytic]] | o/p | double | Watts | Stator back iron excess losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Exc_Static|StatorBackIronLoss_Exc_Static]] | o/p | double | Watts | Stator back iron excess losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Exc_Static_PerSlice|StatorBackIronLoss_Exc_Static_PerSlice]] | o/p | double | Watts | Stator back iron excess losses (per slice) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Excess|StatorBackIronLoss_Excess]] | o/p | double | Watts | Stator back iron excess losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Excess_OC|StatorBackIronLoss_Excess_OC]] | o/p | double | Watts | Stator back iron excess losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Fundamental_Hys|StatorBackIronLoss_Fundamental_Hys]] | o/p | double | Watts | Stator back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys|StatorBackIronLoss_Hys]] | o/p | double | Watts | Stator back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Adj|StatorBackIronLoss_Hys_Adj]] | o/p | double | Watts | Stator back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Adj_OC|StatorBackIronLoss_Hys_Adj_OC]] | o/p | double | Watts | Stator back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Analytic|StatorBackIronLoss_Hys_Analytic]] | o/p | double | Watts | Stator back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Analytic_Adj|StatorBackIronLoss_Hys_Analytic_Adj]] | o/p | double | Watts | Stator back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Fundamental_OC|StatorBackIronLoss_Hys_Fundamental_OC]] | o/p | double | Watts | Stator back iron losses from fundamental frequency hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Minor_OC|StatorBackIronLoss_Hys_Minor_OC]] | o/p | double | Watts | Stator back iron losses from minor loops hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_OC|StatorBackIronLoss_Hys_OC]] | o/p | double | Watts | Stator back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Static|StatorBackIronLoss_Hys_Static]] | o/p | double | Watts | Stator back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Static_Adj|StatorBackIronLoss_Hys_Static_Adj]] | o/p | double | Watts | Stator back iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Static_Adj_PerSlice|StatorBackIronLoss_Hys_Static_Adj_PerSlice]] | o/p | double | Watts | Stator back iron losses from hysteresis (adjusted for build factor) (per slice) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Hys_Static_PerSlice|StatorBackIronLoss_Hys_Static_PerSlice]] | o/p | double | Watts | Stator back iron losses from hysteresis per slice |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Minor_Hys|StatorBackIronLoss_Minor_Hys]] | o/p | double | Watts | Stator back iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total|StatorBackIronLoss_Total]] | o/p | double | Watts | Total Stator back iron losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Adj|StatorBackIronLoss_Total_Adj]] | o/p | double | Watts | Stator back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Adj_OC|StatorBackIronLoss_Total_Adj_OC]] | o/p | double | Watts | Stator back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Analytic|StatorBackIronLoss_Total_Analytic]] | o/p | double | Watts | Total Stator back iron losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Analytic_Adj|StatorBackIronLoss_Total_Analytic_Adj]] | o/p | double | Watts | Total Stator back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_OC|StatorBackIronLoss_Total_OC]] | o/p | double | Watts | Total Stator back iron losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Static|StatorBackIronLoss_Total_Static]] | o/p | double | Watts | Total Stator back iron losses |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Static_Adj|StatorBackIronLoss_Total_Static_Adj]] | o/p | double | Watts | Total Stator back iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Static_Adj_PerSlice|StatorBackIronLoss_Total_Static_Adj_PerSlice]] | o/p | double | Watts | Total Stator back iron losses adjusted to take into account build factor (per slice) |
| [[motorcad/parameter_database/parameters/StatorBackIronLoss_Total_Static_PerSlice|StatorBackIronLoss_Total_Static_PerSlice]] | o/p | double | Watts | Total Stator back iron losses (per slice) |
| [[motorcad/parameter_database/parameters/StatorDifferentialLeakageInductance|StatorDifferentialLeakageInductance]] | o/p | double | Henry | Stator Differential Leakage Inductance |
| [[motorcad/parameter_database/parameters/StatorDifferentialLeakageInductance_Aux|StatorDifferentialLeakageInductance_Aux]] | o/p | double | Henry | The differential leakage inductance for the aux stator windings |
| [[motorcad/parameter_database/parameters/StatorDifferentialLeakageReactance|StatorDifferentialLeakageReactance]] | o/p | double | Ohms | Stator Differential Leakage Reactance |
| [[motorcad/parameter_database/parameters/StatorDifferentialLeakageReactance_Aux|StatorDifferentialLeakageReactance_Aux]] | o/p | double | Ohms | The differential leakage reactance for the aux stator windings |
| [[motorcad/parameter_database/parameters/StatorIronLossBuildFactor|StatorIronLossBuildFactor]] | i/p | double | N/A | Multiplier used to adjust stator iron losses |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total|StatorIronLoss_Total]] | o/p | double | Watts | Total Stator iron losses |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_Adj|StatorIronLoss_Total_Adj]] | o/p | double | Watts | Total Stator iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_Adj_OC|StatorIronLoss_Total_Adj_OC]] | o/p | double | Watts | Total Stator iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_Analytic|StatorIronLoss_Total_Analytic]] | o/p | double | Watts | Total Stator iron losses |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_Analytic_Adj|StatorIronLoss_Total_Analytic_Adj]] | o/p | double | Watts | Total Stator iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_OC|StatorIronLoss_Total_OC]] | o/p | double | Watts | Total Stator iron losses |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_Static|StatorIronLoss_Total_Static]] | o/p | double | Watts | Total Stator iron losses |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_Static_Adj|StatorIronLoss_Total_Static_Adj]] | o/p | double | Watts | Total Stator iron losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorIronLoss_Total_Static_PerSlice|StatorIronLoss_Total_Static_PerSlice]] | o/p | double | Watts | Total Stator iron losses (per slice) |
| [[motorcad/parameter_database/parameters/StatorLam_Resistivity|StatorLam_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the stator lamination at stator temperature |
| [[motorcad/parameter_database/parameters/StatorLam_ResistivityAt20C|StatorLam_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the stator lamination at reference temperature |
| [[motorcad/parameter_database/parameters/StatorLam_Temperature|StatorLam_Temperature]] | i/p | double | °C | The temperature of the stator lamination used for loss calculation |
| [[motorcad/parameter_database/parameters/StatorLaminations|StatorLaminations]] | i/p | integer | N/A | Whether stator is laminated or solid |
| [[motorcad/parameter_database/parameters/StatorLeakageInductance_Aux_Multiplier|StatorLeakageInductance_Aux_Multiplier]] | i/p | double | N/A | Multiplier used to adjust the aux winding stator leakage inductance |
| [[motorcad/parameter_database/parameters/StatorLeakageInductance_Multiplier|StatorLeakageInductance_Multiplier]] | i/p | double | N/A | Multiplier used to adjust the stator leakage inductance |
| [[motorcad/parameter_database/parameters/StatorLeakageInductance_Skewed|StatorLeakageInductance_Skewed]] | o/p | double | Henry | The additional stator leakage inductance component due to skew |
| [[motorcad/parameter_database/parameters/StatorLeakageInductance_Total|StatorLeakageInductance_Total]] | o/p | double | Henry | The total stator leakage inductance |
| [[motorcad/parameter_database/parameters/StatorLeakageInductance_Total_Aux|StatorLeakageInductance_Total_Aux]] | o/p | double | Henry | The aux winding total stator leakage inductance |
| [[motorcad/parameter_database/parameters/StatorLeakageReactance_Skewed|StatorLeakageReactance_Skewed]] | o/p | double | Ohms | The additional stator leakage reactance component due to skew |
| [[motorcad/parameter_database/parameters/StatorLeakageReactance_Skewed_Aux|StatorLeakageReactance_Skewed_Aux]] | o/p | double | Ohms | The additional aux winding stator leakage reactance component due to skew |
| [[motorcad/parameter_database/parameters/StatorLeakageReactance_Total|StatorLeakageReactance_Total]] | o/p | double | Ohms | The total stator leakage reactance |
| [[motorcad/parameter_database/parameters/StatorLeakageReactance_Total_Aux|StatorLeakageReactance_Total_Aux]] | o/p | double | Ohms | The aux winding total stator leakage reactance |
| [[motorcad/parameter_database/parameters/StatorLeakageReactance_Total_L|StatorLeakageReactance_Total_L]] | o/p | double | Ohms | The total stator leakage reactance |
| [[motorcad/parameter_database/parameters/StatorLeakageVoltage_Aux_RMS|StatorLeakageVoltage_Aux_RMS]] | o/p | double | Volts | The rms voltage across the aux winding stator leakage reactance |
| [[motorcad/parameter_database/parameters/StatorLeakageVoltage_Main_RMS|StatorLeakageVoltage_Main_RMS]] | o/p | double | Volts | The rms voltage across the main winding stator leakage reactance |
| [[motorcad/parameter_database/parameters/StatorLoss_Eddy|StatorLoss_Eddy]] | o/p | double | Watts | Stator iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorLoss_Eddy_Adj|StatorLoss_Eddy_Adj]] | o/p | double | Watts | Stator iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorLoss_Eddy_Adj_OC|StatorLoss_Eddy_Adj_OC]] | o/p | double | Watts | Stator iron losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorLoss_Eddy_OC|StatorLoss_Eddy_OC]] | o/p | double | Watts | Stator iron losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorLoss_Excess|StatorLoss_Excess]] | o/p | double | Watts | Stator iron excess losses |
| [[motorcad/parameter_database/parameters/StatorLoss_Excess_OC|StatorLoss_Excess_OC]] | o/p | double | Watts | Stator iron excess losses |
| [[motorcad/parameter_database/parameters/StatorLoss_Fundamental_Hys|StatorLoss_Fundamental_Hys]] | o/p | double | Watts | Stator iron losses from hysteresis (fundamental component) |
| [[motorcad/parameter_database/parameters/StatorLoss_Fundamental_Hys_OC|StatorLoss_Fundamental_Hys_OC]] | o/p | double | Watts | Stator iron losses from fundamental frequency hysteresis |
| [[motorcad/parameter_database/parameters/StatorLoss_Hys|StatorLoss_Hys]] | o/p | double | Watts | Stator iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorLoss_Hys_Adj|StatorLoss_Hys_Adj]] | o/p | double | Watts | Stator iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorLoss_Hys_Adj_OC|StatorLoss_Hys_Adj_OC]] | o/p | double | Watts | Stator iron losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorLoss_Hys_OC|StatorLoss_Hys_OC]] | o/p | double | Watts | Stator iron losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorLoss_Minor_Hys|StatorLoss_Minor_Hys]] | o/p | double | Watts | Stator iron losses from hysteresis (minor loops component) |
| [[motorcad/parameter_database/parameters/StatorLoss_Minor_Hys_OC|StatorLoss_Minor_Hys_OC]] | o/p | double | Watts | Stator iron losses from minor loops hysteresis |
| [[motorcad/parameter_database/parameters/StatorSaturationMultiplier|StatorSaturationMultiplier]] | i/p | double | N/A | Multiplier used to adjust the level of stator saturation |
| [[motorcad/parameter_database/parameters/StatorSkew|StatorSkew]] | i/p | double | MDeg | Stator skew angle |
| [[motorcad/parameter_database/parameters/StatorTerminalVoltage_Aux_RMS|StatorTerminalVoltage_Aux_RMS]] | o/p | double | Volts | The aux winding RMS stator terminal voltage |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy|StatorToothLoss_Eddy]] | o/p | double | Watts | Stator tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Adj|StatorToothLoss_Eddy_Adj]] | o/p | double | Watts | Stator tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Adj_OC|StatorToothLoss_Eddy_Adj_OC]] | o/p | double | Watts | Stator tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Analytic|StatorToothLoss_Eddy_Analytic]] | o/p | double | Watts | Stator tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Analytic_Adj|StatorToothLoss_Eddy_Analytic_Adj]] | o/p | double | Watts | Stator tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_OC|StatorToothLoss_Eddy_OC]] | o/p | double | Watts | Stator tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Static|StatorToothLoss_Eddy_Static]] | o/p | double | Watts | Stator tooth losses from eddy currents |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Static_Adj|StatorToothLoss_Eddy_Static_Adj]] | o/p | double | Watts | Stator tooth losses from eddy currents (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Static_Adj_PerSlice|StatorToothLoss_Eddy_Static_Adj_PerSlice]] | o/p | double | Watts | Stator tooth losses from eddy currents (adjusted for build factor) (per slice) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Eddy_Static_PerSlice|StatorToothLoss_Eddy_Static_PerSlice]] | o/p | double | Watts | Stator tooth losses from eddy currents (per slice) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Exc_Analytic|StatorToothLoss_Exc_Analytic]] | o/p | double | Watts | Stator tooth excess losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Exc_Static|StatorToothLoss_Exc_Static]] | o/p | double | Watts | Stator tooth excess losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Exc_Static_PerSlice|StatorToothLoss_Exc_Static_PerSlice]] | o/p | double | Watts | Stator tooth excess losses (per slice) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Excess|StatorToothLoss_Excess]] | o/p | double | Watts | Stator tooth excess losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Excess_OC|StatorToothLoss_Excess_OC]] | o/p | double | Watts | Stator tooth excess losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Fundamental_Hys|StatorToothLoss_Fundamental_Hys]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys|StatorToothLoss_Hys]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Adj|StatorToothLoss_Hys_Adj]] | o/p | double | Watts | Stator tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Adj_OC|StatorToothLoss_Hys_Adj_OC]] | o/p | double | Watts | Stator tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Analytic|StatorToothLoss_Hys_Analytic]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Analytic_Adj|StatorToothLoss_Hys_Analytic_Adj]] | o/p | double | Watts | Stator tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Fundamental_OC|StatorToothLoss_Hys_Fundamental_OC]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Minor_OC|StatorToothLoss_Hys_Minor_OC]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_OC|StatorToothLoss_Hys_OC]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Static|StatorToothLoss_Hys_Static]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Static_Adj|StatorToothLoss_Hys_Static_Adj]] | o/p | double | Watts | Stator tooth losses from hysteresis (adjusted for build factor) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Static_Adj_PerSlice|StatorToothLoss_Hys_Static_Adj_PerSlice]] | o/p | double | Watts | Stator tooth losses from hysteresis (adjusted for build factor) (per slice) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Hys_Static_PerSlice|StatorToothLoss_Hys_Static_PerSlice]] | o/p | double | Watts | Stator tooth losses from hysteresis (per slice) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Minor_Hys|StatorToothLoss_Minor_Hys]] | o/p | double | Watts | Stator tooth losses from hysteresis |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total|StatorToothLoss_Total]] | o/p | double | Watts | Total Stator tooth losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Adj|StatorToothLoss_Total_Adj]] | o/p | double | Watts | Stator tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Adj_OC|StatorToothLoss_Total_Adj_OC]] | o/p | double | Watts | Stator tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Analytic|StatorToothLoss_Total_Analytic]] | o/p | double | Watts | Total Stator tooth losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Analytic_Adj|StatorToothLoss_Total_Analytic_Adj]] | o/p | double | Watts | Total Stator tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_OC|StatorToothLoss_Total_OC]] | o/p | double | Watts | Total Stator tooth losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Static|StatorToothLoss_Total_Static]] | o/p | double | Watts | Total Stator tooth losses |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Static_Adj|StatorToothLoss_Total_Static_Adj]] | o/p | double | Watts | Total Stator tooth losses adjusted to take into account build factor |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Static_Adj_PerSlice|StatorToothLoss_Total_Static_Adj_PerSlice]] | o/p | double | Watts | Total Stator tooth losses adjusted to take into account build factor (per slice) |
| [[motorcad/parameter_database/parameters/StatorToothLoss_Total_Static_PerSlice|StatorToothLoss_Total_Static_PerSlice]] | o/p | double | Watts | Total Stator tooth losses (per slice) |
| [[motorcad/parameter_database/parameters/StatorVoltageAngle_Aux|StatorVoltageAngle_Aux]] | o/p | double | EDeg | The angle of the voltage across the aux winding excluding start/run circuit |
| [[motorcad/parameter_database/parameters/StatorVoltage_Aux_RMS|StatorVoltage_Aux_RMS]] | o/p | double | Volts | The RMS voltage across the aux winding excluding start/run circuit |
| [[motorcad/parameter_database/parameters/StatorWindingLoss_Aux|StatorWindingLoss_Aux]] | o/p | double | Watts | The analytic aux stator winding losses |
| [[motorcad/parameter_database/parameters/StatorWindingLoss_Main|StatorWindingLoss_Main]] | o/p | double | Watts | The analytic aux stator winding losses |
| [[motorcad/parameter_database/parameters/StatorWindingVoltage_Aux_RMS|StatorWindingVoltage_Aux_RMS]] | o/p | double | Volts | The RMS voltage drop across the aux winding resistance |
| [[motorcad/parameter_database/parameters/StrayLoadLossPercentage_OutputPower|StrayLoadLossPercentage_OutputPower]] | i/p | double | N/A | Stray load loss value as a percentage of output power |
| [[motorcad/parameter_database/parameters/StrayLoadLossPercentage_Resistance|StrayLoadLossPercentage_Resistance]] | i/p | double | N/A | Stray load loss resistance value as a percentage of armature winding resistance |
| [[motorcad/parameter_database/parameters/StrayLoadLossResistancePh|StrayLoadLossResistancePh]] | o/p | double | Ohms | The resistance due to stray load losses at the armature conductor temperature |
| [[motorcad/parameter_database/parameters/SupplyCurrentMean|SupplyCurrentMean]] | o/p | double | Amps | Mean current from power supply |
| [[motorcad/parameter_database/parameters/SupplyDefinition|SupplyDefinition]] | i/p | integer | N/A | Defines whether the voltage is from mains or inverter |
| [[motorcad/parameter_database/parameters/SupplyFilterCapacitance|SupplyFilterCapacitance]] | i/p | double | Farad | Value of capacitor in parallel with power supply |
| [[motorcad/parameter_database/parameters/SupplyInternalResistance|SupplyInternalResistance]] | i/p | double | Ohms | Internal resistance of power supply |
| [[motorcad/parameter_database/parameters/SupplyVoltage|SupplyVoltage]] | i/p | double | Volts | Voltage of power supply |
| [[motorcad/parameter_database/parameters/SwitchingAngleDefinition_SRM|SwitchingAngleDefinition_SRM]] | i/p | integer | N/A | Select whether to define switch on angle or switch off angle |
| [[motorcad/parameter_database/parameters/SystemEfficiency|SystemEfficiency]] | o/p | double | Percent | Efficiency of system |
| [[motorcad/parameter_database/parameters/THDBackEMFLine|THDBackEMFLine]] | o/p | double | Percent | Total harmonic distortion of the back EMF line to line voltage in open circuit |
| [[motorcad/parameter_database/parameters/THDBackEMFPhase|THDBackEMFPhase]] | o/p | double | Percent | Total harmonic distortion of the back EMF phase voltage in open circuit |
| [[motorcad/parameter_database/parameters/THDLineCurrent|THDLineCurrent]] | o/p | double | Percent | Total harmonic distortion of the Line Current |
| [[motorcad/parameter_database/parameters/THDLineLineVoltage|THDLineLineVoltage]] | o/p | double | Percent | Total harmonic distortion of the Line to Line Voltage at the terminals of the machine |
| [[motorcad/parameter_database/parameters/THDPhaseCurrent|THDPhaseCurrent]] | o/p | double | Percent | Total harmonic distortion of the Phase Current |
| [[motorcad/parameter_database/parameters/THDPhaseVoltage|THDPhaseVoltage]] | o/p | double | Percent | Total harmonic distortion of the Phase Voltage at the terminals of the machine |
| [[motorcad/parameter_database/parameters/TangentialForceHarmonicAngles_OC|TangentialForceHarmonicAngles_OC]] | o/p | double | MDeg | Tangential force harmonic angles created from Open Circuit calculations |
| [[motorcad/parameter_database/parameters/TangentialForceHarmonicAngles_OL|TangentialForceHarmonicAngles_OL]] | o/p | double | MDeg | Tangential force harmonic angles created from On Load calculations |
| [[motorcad/parameter_database/parameters/TangentialForceHarmonics_OC|TangentialForceHarmonics_OC]] | o/p | double | N | Tangential force harmonics created from Open Circuit calculations |
| [[motorcad/parameter_database/parameters/TangentialForceHarmonics_OL|TangentialForceHarmonics_OL]] | o/p | double | N | Tangential force harmonics created from On Load calculations |
| [[motorcad/parameter_database/parameters/TangentialForce_OC|TangentialForce_OC]] | o/p | double | N | The open circuit tangential force |
| [[motorcad/parameter_database/parameters/TangentialForce_OL|TangentialForce_OL]] | o/p | double | N | The On Load tangential force |
| [[motorcad/parameter_database/parameters/TemperaturesInEmagThermCoupling|TemperaturesInEmagThermCoupling]] | compatibility | integer | N/A | The values of temperatures transferred to E-Magnetic from Thermal. The original method uses the central axial slice, and the improved method uses an average over all axial slices. |
| [[motorcad/parameter_database/parameters/Time_Calculated_IMLookupCurves|Time_Calculated_IMLookupCurves]] | i/p | OleStr | N/A | The time of the last IM saturation calculation |
| [[motorcad/parameter_database/parameters/TopRotorBarOpening_Resistivity|TopRotorBarOpening_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity of the top rotor bar opening at rotor bar temperature |
| [[motorcad/parameter_database/parameters/TopRotorBarOpening_ResistivityAt20|TopRotorBarOpening_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity of the top rotor bar opening at 20C |
| [[motorcad/parameter_database/parameters/TopRotorBar_Resistivity|TopRotorBar_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity of the top rotor bar at rotor bar temperature |
| [[motorcad/parameter_database/parameters/TopRotorBar_ResistivityAt20|TopRotorBar_ResistivityAt20]] | i/p | double | Ohm.m | The electrical resistivity of the top rotor bar at 20C |
| [[motorcad/parameter_database/parameters/TorqueCalculation|TorqueCalculation]] | i/p | boolean | N/A | When selected torque calculation is run |
| [[motorcad/parameter_database/parameters/TorquePerVolume|TorquePerVolume]] | o/p | double | kNm/m³ | Torque per unit volume of rotor |
| [[motorcad/parameter_database/parameters/TorqueProductionCurrent_Aux|TorqueProductionCurrent_Aux]] | o/p | double | Amps | The on load aux winding RMS torque production current |
| [[motorcad/parameter_database/parameters/TorqueProductionCurrent_Main|TorqueProductionCurrent_Main]] | o/p | double | Amps | The on load main winding RMS torque production current |
| [[motorcad/parameter_database/parameters/TorqueRippleAnalytic|TorqueRippleAnalytic]] | o/p | double | Nm | The torque ripple calculated using analytic methods |
| [[motorcad/parameter_database/parameters/TorqueRippleAnalyticPerCent|TorqueRippleAnalyticPerCent]] | o/p | double | Percent | The percent torque ripple calculated using analytic methods |
| [[motorcad/parameter_database/parameters/TorqueRippleMsVw|TorqueRippleMsVw]] | o/p | double | Nm | The torque ripple calculated using Maxwell Stress and Virtual Works finite element methods during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/TorqueRippleMsVwPerCent (MsVw)|TorqueRippleMsVwPerCent (MsVw)]] | o/p | double | Percent | The percent torque ripple calculated using Maxwell Stress and Virtual Works finite element methods during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/TorqueRippleRms|TorqueRippleRms]] | o/p | double | Nm | The Rms torque ripple |
| [[motorcad/parameter_database/parameters/TorqueRippleRmsPerCent|TorqueRippleRmsPerCent]] | o/p | double | Percent | The Rms torque ripple as a percentage of average torque |
| [[motorcad/parameter_database/parameters/TorqueSpeedCalculation|TorqueSpeedCalculation]] | i/p | boolean | N/A | When selected torque / speed calculation is run |
| [[motorcad/parameter_database/parameters/TotalConductors_Aux|TotalConductors_Aux]] | o/p | double | N/A | Total number of conductors in the aux winding |
| [[motorcad/parameter_database/parameters/TotalConductors_Main|TotalConductors_Main]] | o/p | double | N/A | Total number of conductors in the main winding |
| [[motorcad/parameter_database/parameters/TotalExternalResistance|TotalExternalResistance]] | i/p | double | Ohms | The total resistance of the external circuit |
| [[motorcad/parameter_database/parameters/TotalInertia|TotalInertia]] | o/p | double | kg.m² | Total Inertia (rotor + shaft) |
| [[motorcad/parameter_database/parameters/TotalLoss|TotalLoss]] | o/p | double | Watts | Total Loss of machine |
| [[motorcad/parameter_database/parameters/TotalPoints_Calculated_MagnetisationCurves|TotalPoints_Calculated_MagnetisationCurves]] | i/p | integer | N/A | The total number of points in the magnetisation curves calculation |
| [[motorcad/parameter_database/parameters/TurnOffAngle_SRM|TurnOffAngle_SRM]] | i/p | double | EDeg | SRM drive turn off angle |
| [[motorcad/parameter_database/parameters/TurnOnAngle_SRM|TurnOnAngle_SRM]] | i/p | double | EDeg | SRM drive turn on angle |
| [[motorcad/parameter_database/parameters/UnalignedInductance|UnalignedInductance]] | o/p | double | Henry | Inductance of winding in the unaligned position |
| [[motorcad/parameter_database/parameters/UnbalancedMagneticPull_Angle_OC|UnbalancedMagneticPull_Angle_OC]] | o/p | double | MDeg | The angle of the unbalanced magnetic pull (Open Circuit) |
| [[motorcad/parameter_database/parameters/UnbalancedMagneticPull_Angle_OL|UnbalancedMagneticPull_Angle_OL]] | o/p | double | MDeg | The angle of the unbalanced magnetic pull (On Load) |
| [[motorcad/parameter_database/parameters/UnbalancedMagneticPull_OC|UnbalancedMagneticPull_OC]] | o/p | double | N | The magnitude of the unbalanced magnetic pull (Open Circuit) |
| [[motorcad/parameter_database/parameters/UnbalancedMagneticPull_OL|UnbalancedMagneticPull_OL]] | o/p | double | N | The magnitude of the unbalanced magnetic pull (On Load) |
| [[motorcad/parameter_database/parameters/UseSpecifiedRefTemp|UseSpecifiedRefTemp]] | i/p | boolean | N/A | If selected, user can specify the reference temperature for the magnet data |
| [[motorcad/parameter_database/parameters/VoltageAngle|VoltageAngle]] | o/p | double | EDeg | Voltage Angle |
| [[motorcad/parameter_database/parameters/VoltageConversionFactor|VoltageConversionFactor]] | o/p | double | N/A | Maximum ratio of line-line to phase voltage |
| [[motorcad/parameter_database/parameters/VoltageDefinition|VoltageDefinition]] | i/p | integer | N/A | Defines whether the voltage is rms or peak voltage |
| [[motorcad/parameter_database/parameters/WaveformPowerFactor|WaveformPowerFactor]] | o/p | double | N/A | Power Factor from waveforms |
| [[motorcad/parameter_database/parameters/WaveformPowerFactorAngle|WaveformPowerFactorAngle]] | o/p | double | EDeg | Power Factor Angle from waveforms |
| [[motorcad/parameter_database/parameters/WaveformPowerFactor_THD|WaveformPowerFactor_THD]] | o/p | double | N/A | Power Factor from waveforms, including total harmonic distortion |
| [[motorcad/parameter_database/parameters/WedgeLoss|WedgeLoss]] | o/p | double | Watts | Slot Wedge Loss of machine |
| [[motorcad/parameter_database/parameters/WedgeLoss_OC|WedgeLoss_OC]] | o/p | double | Watts | Slot Wedge Loss of machine |
| [[motorcad/parameter_database/parameters/Wedge_Resistivity|Wedge_Resistivity]] | o/p | double | Ohm.m | The electrical resistivity for the Wedge at Wedge temperature |
| [[motorcad/parameter_database/parameters/Wedge_ResistivityAt20C|Wedge_ResistivityAt20C]] | i/p | double | Ohm.m | The electrical resistivity for the Wedge at reference temperature |
| [[motorcad/parameter_database/parameters/Wedge_Temperature|Wedge_Temperature]] | i/p | double | °C | The temperature of the Wedge used for loss calculation |
| [[motorcad/parameter_database/parameters/WindingConnection|WindingConnection]] | i/p | integer | N/A | The winding connection type |
| [[motorcad/parameter_database/parameters/WindingFactorSum|WindingFactorSum]] | o/p | double | N/A | The Winding Factor Sum |
| [[motorcad/parameter_database/parameters/WindingFactorSum_Aux|WindingFactorSum_Aux]] | o/p | double | N/A | The sum of the aux winding factors |
| [[motorcad/parameter_database/parameters/WindingLayers|WindingLayers]] | i/p | integer | N/A | Number of winding layers |
| [[motorcad/parameter_database/parameters/WindingSchematic_Style|WindingSchematic_Style]] | setting | integer | N/A | Winding Schematic View Preference (loops, paths or all) |
| [[motorcad/parameter_database/parameters/XForce_OC|XForce_OC]] | o/p | double | N | The unbalanced magnetic pull in the X-axis for Open Circuit |
| [[motorcad/parameter_database/parameters/XForce_OL|XForce_OL]] | o/p | double | N | The unbalanced magnetic pull in the X-axis for On Load |
| [[motorcad/parameter_database/parameters/YForce_OC|YForce_OC]] | o/p | double | N | The unbalanced magnetic pull in the Y-axis for Open Circuit |
| [[motorcad/parameter_database/parameters/YForce_OL|YForce_OL]] | o/p | double | N | The unbalanced magnetic pull in the Y-axis for On Load |
| [[motorcad/parameter_database/parameters/ZeroVoltageAngle_SRM|ZeroVoltageAngle_SRM]] | i/p | double | EDeg | SRM drive zero voltage commutation angle |
| [[motorcad/parameter_database/parameters/ZeroVoltageLoop_SRM|ZeroVoltageLoop_SRM]] | i/p | integer | N/A | Definition of zero voltage loop SRM current control |
| [[motorcad/parameter_database/parameters/loopTorque|loopTorque]] | o/p | double | Nm | The average magnet and reluctance torque calculated using loop torque method during rotation of rotor through 180 electrical degrees |
| [[motorcad/parameter_database/parameters/x_sigma|x_sigma]] | o/p | double | N/A | X_Sigma |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
