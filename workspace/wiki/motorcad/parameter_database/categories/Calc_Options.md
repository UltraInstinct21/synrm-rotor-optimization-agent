---
type: motorcad_parameter_category
category_name: Calc_Options
parameter_count: 695
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Calc_Options

## Overview
The **Calc_Options** category contains **695** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/ACLossHighFrequencyScaling_Method|ACLossHighFrequencyScaling_Method]] | compatibility | integer | N/A | The improved method introduces a further correction to Hybrid FEA AC losses when skin depth is significantly less than bundle height |
| [[motorcad/parameter_database/parameters/ACLossTemperatureScalingMethod|ACLossTemperatureScalingMethod]] | compatibility | integer | N/A | How the AC winding losses are scaled with temperature in the thermal model |
| [[motorcad/parameter_database/parameters/ActiveHousingAxialLengthCalc|ActiveHousingAxialLengthCalc]] | compatibility | integer | N/A | Calculation of the axial length of the active portion of the housing |
| [[motorcad/parameter_database/parameters/AirDividerFluidCalc|AirDividerFluidCalc]] | compatibility | integer | N/A | Air Divider Calculation with forced fluid concection |
| [[motorcad/parameter_database/parameters/AirgapLaminarVorticesMethod|AirgapLaminarVorticesMethod]] | recommended | integer | N/A | Calculation method used for the laminar flow with vortices airgap heat transfer |
| [[motorcad/parameter_database/parameters/AirgapModel|AirgapModel]] | compatibility | integer | N/A | Airgap heat transfer model can be made to be solely based on conduction or to include convection |
| [[motorcad/parameter_database/parameters/AirgapTempForEmagCalc|AirgapTempForEmagCalc]] | compatibility | integer | N/A | The Airgap Temperature value used in Emag calculations |
| [[motorcad/parameter_database/parameters/AirgapTurbulentMethod|AirgapTurbulentMethod]] | recommended | integer | N/A | Calculation method used for the turbulent flow airgap heat transfer |
| [[motorcad/parameter_database/parameters/AirgapTurbulentVorticesMethod|AirgapTurbulentVorticesMethod]] | recommended | integer | N/A | Calculation method used for the turbulent flow with vortices airgap heat transfer |
| [[motorcad/parameter_database/parameters/AlignmentGraph|AlignmentGraph]] | setting | boolean | N/A | Drawing options for the alignment torque graph |
| [[motorcad/parameter_database/parameters/AmbientTemperatureSetting|AmbientTemperatureSetting]] | recommended | integer | N/A | Ambient temperatures used in thermal calculation |
| [[motorcad/parameter_database/parameters/AnsysArcSegmentDegrees|AnsysArcSegmentDegrees]] | setting | double | N/A | The number of degrees per segment within polyline arc. |
| [[motorcad/parameter_database/parameters/AnsysArcSegmentMethod|AnsysArcSegmentMethod]] | setting | integer | N/A | The method used for specifying the number of line segments used for polyline arc. |
| [[motorcad/parameter_database/parameters/AnsysHairpinCoilTips|AnsysHairpinCoilTips]] | setting | integer | N/A | Whether to use the Ansys Maxwell HairpinCoil UDP coil tips to connect seperate hairpin coils |
| [[motorcad/parameter_database/parameters/AnsysHairpinUDP|AnsysHairpinUDP]] | setting | integer | N/A | Whether to use the Ansys Maxwell HairpinCoil UDP for hairpin windings in Ansys Export |
| [[motorcad/parameter_database/parameters/AnsysMeshSlider|AnsysMeshSlider]] | setting | integer | N/A | The mesh slider value used in Ansys Maxwell export |
| [[motorcad/parameter_database/parameters/AnsysRotationDirection|AnsysRotationDirection]] | setting | integer | N/A | The rotation direction used within Maxwell Export |
| [[motorcad/parameter_database/parameters/AnsysUDPSegAngle|AnsysUDPSegAngle]] | setting | double | N/A | The segmentation angle used to divide curves into line segments for Ansys Maxwell User Defined Primitives |
| [[motorcad/parameter_database/parameters/AutomaticStrayLoadLossMethod|AutomaticStrayLoadLossMethod]] | compatibility | integer | N/A | How automatic stray load losses are calculated for inverter fed machines |
| [[motorcad/parameter_database/parameters/AvWindingCalibration|AvWindingCalibration]] | i/p | double | N/A | Calibrate the analytic winding model average temperature with the FEA results to take account of the conductor placement. |
| [[motorcad/parameter_database/parameters/AverageCyclesMinPoint|AverageCyclesMinPoint]] | i/p | integer | N/A | The number of iterations run before averaging the steady state node temperatures to aid convergence. |
| [[motorcad/parameter_database/parameters/AxialSliceDefinition|AxialSliceDefinition]] | i/p | integer | N/A | The number of axial slices modelled |
| [[motorcad/parameter_database/parameters/Axle_Mounting|Axle_Mounting]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/BPMORToothRtCalc|BPMORToothRtCalc]] | compatibility | integer | N/A | The calculation method of the tooth to back iron resistance for BPMOR machines |
| [[motorcad/parameter_database/parameters/BPMORWdgExtPottingRtCalc|BPMORWdgExtPottingRtCalc]] | compatibility | integer | N/A | The thermal resistance calculation due the Potting between the Winding Extension and the Axle |
| [[motorcad/parameter_database/parameters/BPMOR_MagnetWeightDef|BPMOR_MagnetWeightDef]] | compatibility | integer | N/A | Method used for calculating magnet weights in BPMOR machines |
| [[motorcad/parameter_database/parameters/BPMShortCircuitGraph|BPMShortCircuitGraph]] | i/p | integer | N/A | The short circuit graph to view |
| [[motorcad/parameter_database/parameters/BPM_Fault_Type|BPM_Fault_Type]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/BackEMFNumberCycles|BackEMFNumberCycles]] | i/p | integer | N/A | Number of cycles to perform for Back EMF calculation |
| [[motorcad/parameter_database/parameters/BackEMFPointsPerCycle|BackEMFPointsPerCycle]] | i/p | integer | N/A | Number of points to calculate for each cycle of Back EMF calculation |
| [[motorcad/parameter_database/parameters/Banding2D3DFactorCalc|Banding2D3DFactorCalc]] | compatibility | integer | N/A | This determines the method for calculating the 2D to 3D factor for the rotor banding losses |
| [[motorcad/parameter_database/parameters/BearingLossMultiplier|BearingLossMultiplier]] | i/p | double | N/A | This is scale factor applied to the bearing losses given in the table below. |
| [[motorcad/parameter_database/parameters/BearingLossSource|BearingLossSource]] | i/p | integer | N/A | When this is set to automatic then the table of values is used to calculate the bearing losses |
| [[motorcad/parameter_database/parameters/BearingLossVisualisationSpeed|BearingLossVisualisationSpeed]] | i/p | double | rpm | This is speed shown on the graph. Not used for any calculations. |
| [[motorcad/parameter_database/parameters/BearingTempForEmagCalc|BearingTempForEmagCalc]] | compatibility | integer | N/A | The temperatures of the front and rear bearings used in emag calculations |
| [[motorcad/parameter_database/parameters/Bearing_Loss_Definition|Bearing_Loss_Definition]] | recommended | integer | N/A | This defines whether the bearing losses are placed on the bearing node or on the endcap and shaft nodes. |
| [[motorcad/parameter_database/parameters/Bearing_Loss_Values_Loss|Bearing_Loss_Values_Loss]] | i/p | double | Watts | Loss values for bearing loss data |
| [[motorcad/parameter_database/parameters/Bearing_Loss_Values_Speed|Bearing_Loss_Values_Speed]] | i/p | double | rpm | Speed values for bearing loss data |
| [[motorcad/parameter_database/parameters/Bearing_Loss_Values_Temp|Bearing_Loss_Values_Temp]] | i/p | double | °C | Temperature values for bearing loss data |
| [[motorcad/parameter_database/parameters/BearingsResistanceCalc|BearingsResistanceCalc]] | compatibility | integer | N/A | Calculation method of the bearings thermal resistance |
| [[motorcad/parameter_database/parameters/BidirectionalSolveMethod|BidirectionalSolveMethod]] | recommended | integer | N/A | Method for solving the fluid flow network |
| [[motorcad/parameter_database/parameters/Brush_Holder|Brush_Holder]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/CalculateInductanceDerivative|CalculateInductanceDerivative]] | i/p | boolean | N/A | When selected, variation in inductance will be calculated and used in the inverter fed current calculation |
| [[motorcad/parameter_database/parameters/CalculatedCurrentsBackEMFMethod|CalculatedCurrentsBackEMFMethod]] | setting | integer | N/A | If the open circuit back EMF or estimated on load back EMF is used for current calculation. |
| [[motorcad/parameter_database/parameters/CalculatedCurrentsInductanceMethod|CalculatedCurrentsInductanceMethod]] | compatibility | integer | N/A | Compatibility method for calculated currents inductance |
| [[motorcad/parameter_database/parameters/CalculationDevelopingFlow|CalculationDevelopingFlow]] | recommended | integer | N/A | Whether to use developing or fully developed flow for calculating heat transfer coefficients of ducts. |
| [[motorcad/parameter_database/parameters/CalculationRotatingDuct|CalculationRotatingDuct]] | recommended | integer | N/A | The channel correlation or rotating channel correlation used for rotor ducts. Rotating correlation will only be used for air fluid. |
| [[motorcad/parameter_database/parameters/CancelTransientOnMaxEvaluations|CancelTransientOnMaxEvaluations]] | i/p | boolean | N/A | When disabled the transient calculation will continue with next step even if current step has not solved |
| [[motorcad/parameter_database/parameters/CircuitEditing|CircuitEditing]] | setting | boolean | N/A | When enabled the circuit can be edited |
| [[motorcad/parameter_database/parameters/CircuitFlowEditing|CircuitFlowEditing]] | setting | boolean | N/A | When enabled the flow circuit can be edited |
| [[motorcad/parameter_database/parameters/CircularDuctsFlowCalc|CircularDuctsFlowCalc]] | compatibility | integer | N/A | Calculation method of the flow resistance and fluid velocity for Circular/Rectangular ducts |
| [[motorcad/parameter_database/parameters/CirculatingFlowFluidPaths|CirculatingFlowFluidPaths]] | compatibility | boolean | N/A | When enabled the fluid flow paths method is used for circulating flow. |
| [[motorcad/parameter_database/parameters/CoggingGraph|CoggingGraph]] | setting | boolean | N/A | Drawing options for the cogging torque graph |
| [[motorcad/parameter_database/parameters/CoggingHarmonicBaseFrequency|CoggingHarmonicBaseFrequency]] | setting | integer | N/A | Base frequency used for cogging harmonic graph |
| [[motorcad/parameter_database/parameters/CoggingNumberCycles|CoggingNumberCycles]] | i/p | integer | N/A | Number of cycles to perform for Cogging Torque calculation |
| [[motorcad/parameter_database/parameters/CoggingPointsPerCycle|CoggingPointsPerCycle]] | i/p | integer | N/A | Number of points to calculate for each cycle of Cogging Torque calculation |
| [[motorcad/parameter_database/parameters/CoggingTorqueGraph_CE|CoggingTorqueGraph_CE]] | setting | boolean | N/A | Draw the Co Energy cogging torque graph. |
| [[motorcad/parameter_database/parameters/CoggingTorqueGraph_VW|CoggingTorqueGraph_VW]] | setting | boolean | N/A | Draw the Virtual Work cogging torque graph. |
| [[motorcad/parameter_database/parameters/CommutatorCircuitCalc|CommutatorCircuitCalc]] | compatibility | integer | N/A | Whether to use the old or improved commutator circuit |
| [[motorcad/parameter_database/parameters/ComponentColours|ComponentColours]] | recommended | integer | N/A | When parts with same colours is used then components with same materials and no interface gaps are drawn as same colour. |
| [[motorcad/parameter_database/parameters/ConductionPositionStep|ConductionPositionStep]] | setting | double | mm | The step distance used for fine position adjustment of conductor positions |
| [[motorcad/parameter_database/parameters/ConductorCols_Left|ConductorCols_Left]] | setting | integer | N/A | This is the number of conductor columns in left hand side of slot |
| [[motorcad/parameter_database/parameters/ConductorCols_Right|ConductorCols_Right]] | setting | integer | N/A | This is the number of conductor columns in right hand side of slot |
| [[motorcad/parameter_database/parameters/ConductorMeshControl|ConductorMeshControl]] | recommended | boolean | N/A | When enabled then Motor-CAD specifies conductor positions in mesh grid in the thermal FEA |
| [[motorcad/parameter_database/parameters/ConductorPlacement|ConductorPlacement]] | setting | integer | N/A | This sets whether the layers of conductors are interleaved or overlapped in the winding editor. |
| [[motorcad/parameter_database/parameters/ConductorPositionLevel|ConductorPositionLevel]] | i/p | integer | N/A | This determines the checking precision for placement of conductors in winding drawing. |
| [[motorcad/parameter_database/parameters/ConductorPositions|ConductorPositions]] | setting | integer | N/A | This sets whether the conductors are positioned automatically or as set by user |
| [[motorcad/parameter_database/parameters/ConductorSeparationControl|ConductorSeparationControl]] | i/p | boolean | N/A | When selected the conductors spacing is even throughout slot |
| [[motorcad/parameter_database/parameters/ConductorToothSeparationCalc|ConductorToothSeparationCalc]] | compatibility | integer | N/A | Calculation of the conductor to tooth separation distance |
| [[motorcad/parameter_database/parameters/Constant_Speed_Fan|Constant_Speed_Fan]] | i/p | boolean | N/A | Constant speed fan (air velocity = constant) or shaft mounted fan (air velocity proportional to speed) |
| [[motorcad/parameter_database/parameters/CoolingSystem|CoolingSystem]] | i/p | integer | N/A | Cooling type [TENV, TEFC] |
| [[motorcad/parameter_database/parameters/CoreLossNumberCycles|CoreLossNumberCycles]] | i/p | integer | N/A | Number cycles to perform for open circuit synchronous speed calculation |
| [[motorcad/parameter_database/parameters/CoreLossPointsPerCycle|CoreLossPointsPerCycle]] | i/p | integer | N/A | Number of points to calculate for each cycle of open circuit synchronous speed calculation |
| [[motorcad/parameter_database/parameters/CoupledFluidNodesTransientTemp|CoupledFluidNodesTransientTemp]] | compatibility | integer | N/A | The method used to update the temperatures of coupled fluid nodes during transient calculation |
| [[motorcad/parameter_database/parameters/CoupledSprayCoolingFlowRateCalc|CoupledSprayCoolingFlowRateCalc]] | compatibility | integer | N/A | Method of determining flow rates of cooling systems coupled to user defined spray cooling, when grouped spray cooling is in use |
| [[motorcad/parameter_database/parameters/CoupledTransientBearingLossSplitMethod|CoupledTransientBearingLossSplitMethod]] | compatibility | integer | N/A | How the bearing losses are split between F/R thermal nodes during the Lab-Thermal close coupled transient |
| [[motorcad/parameter_database/parameters/CoupledTransientCustomLossMethod|CoupledTransientCustomLossMethod]] | compatibility | integer | N/A | How the custom losses are assigned to thermal nodes during the Lab-Thermal close coupled transient |
| [[motorcad/parameter_database/parameters/CuboidAreaMethod|CuboidAreaMethod]] | compatibility | integer | N/A | Method used to calculate winding Cuboidal area |
| [[motorcad/parameter_database/parameters/CuboidAvgAirCondCalc|CuboidAvgAirCondCalc]] | compatibility | integer | N/A | The calculation method of the air conductivity at the averaged cuboidal node temperature |
| [[motorcad/parameter_database/parameters/CuboidConductorOnlyModelCalc|CuboidConductorOnlyModelCalc]] | compatibility | integer | N/A | Calculation method of the Cuboid Conductivity Model |
| [[motorcad/parameter_database/parameters/CuboidEWdgConnection|CuboidEWdgConnection]] | compatibility | integer | N/A | Correction for cuboid endwinding model connections |
| [[motorcad/parameter_database/parameters/CuboidEWdgLengthCalc|CuboidEWdgLengthCalc]] | compatibility | integer | N/A | Consideration of the Throw and Path Type when calculating the cuboid endwinding model lengths |
| [[motorcad/parameter_database/parameters/CuboidHeightMethod|CuboidHeightMethod]] | compatibility | integer | N/A | Method for calculation of the cuboid height. |
| [[motorcad/parameter_database/parameters/CuboidHeightMethod_SlotWJ|CuboidHeightMethod_SlotWJ]] | compatibility | integer | N/A | Method for calculation of the cuboid height where Slot Water Jacket is used. |
| [[motorcad/parameter_database/parameters/CuboidLengthCalc|CuboidLengthCalc]] | compatibility | integer | N/A | Calculation method of the cuboid lengths |
| [[motorcad/parameter_database/parameters/CuboidalkValueDefinition|CuboidalkValueDefinition]] | recommended | integer | N/A | How the k values are defined in the cuboidal element model (automatic or user defined) |
| [[motorcad/parameter_database/parameters/CuboidalkValueDefinition_SyncRotor|CuboidalkValueDefinition_SyncRotor]] | recommended | integer | N/A | How the k values are defined in the Sync field cuboidal element model (automatic or user defined) |
| [[motorcad/parameter_database/parameters/CurrentConvergenceDamping|CurrentConvergenceDamping]] | compatibility | double | N/A | Damping factor for Voltage Driven Current Convergence (0= undamped, 0.9 = fully damped) |
| [[motorcad/parameter_database/parameters/CurrentGraphValues|CurrentGraphValues]] | setting | integer | N/A | Drawing options for the current graphs |
| [[motorcad/parameter_database/parameters/CurrentPoints_MagnetisationCurves|CurrentPoints_MagnetisationCurves]] | i/p | integer | N/A | The number of current points in the magnetisation curves calculation |
| [[motorcad/parameter_database/parameters/CustomMaterialLossMethod|CustomMaterialLossMethod]] | compatibility | integer | N/A | Improved method includes Custom Materials In standard loss components |
| [[motorcad/parameter_database/parameters/CustomMaterial_IronLossMethod|CustomMaterial_IronLossMethod]] | compatibility | integer | N/A | Iron loss calculation method for steel materials in custom material regions (affects machines with rotor skew) |
| [[motorcad/parameter_database/parameters/CustomMaterial_MeshLengthMethod|CustomMaterial_MeshLengthMethod]] | compatibility | integer | N/A | Improved method applies rotor/stator mesh length to appropriate custom regions |
| [[motorcad/parameter_database/parameters/CyclesAtEachAverage|CyclesAtEachAverage]] | i/p | integer | N/A | For use with automatic averaging to aid convergence; the number of cycles for which the solver will run before increasing the number in average. Range = [1..20] |
| [[motorcad/parameter_database/parameters/DXFFileName|DXFFileName]] | o/p | OleStr | N/A | The DXF file being used |
| [[motorcad/parameter_database/parameters/Default_EndSpace_Correlation|Default_EndSpace_Correlation]] | i/p | integer | N/A | Default end space convection correlation used in table below |
| [[motorcad/parameter_database/parameters/DistributedLossAreaSelection|DistributedLossAreaSelection]] | i/p | integer | N/A | The area selection of the loss distribution for thermal slot FEA |
| [[motorcad/parameter_database/parameters/DrawPoints_TorqueSpeed|DrawPoints_TorqueSpeed]] | setting | boolean | N/A | When selected then the data points are plotted in the torque/speed and power/speed graphs |
| [[motorcad/parameter_database/parameters/DuctContraction_FlowSolverMethod|DuctContraction_FlowSolverMethod]] | compatibility | integer | N/A | Method for including duct contraction and expansion in TVent fluid flow network |
| [[motorcad/parameter_database/parameters/EMFGraphValues|EMFGraphValues]] | setting | integer | N/A | Drawing options for the Back EMF graphs |
| [[motorcad/parameter_database/parameters/ESpaceRotorHTCCalc|ESpaceRotorHTCCalc]] | compatibility | integer | N/A | Calculation method of the heat transfer coefficients in the rotor components with TVent/flooded cooling |
| [[motorcad/parameter_database/parameters/EWdgAreaCalculation|EWdgAreaCalculation]] | compatibility | integer | N/A | Whether to use the previous endwinding area calculation. |
| [[motorcad/parameter_database/parameters/EWdgInductanceCalc|EWdgInductanceCalc]] | recommended | integer | N/A | The stator endwinding inductance calculation method used |
| [[motorcad/parameter_database/parameters/EWdg_Overhang_Specification|EWdg_Overhang_Specification]] | recommended | integer | N/A | Whether the End winding Overhang values are automatically calculated or user specified |
| [[motorcad/parameter_database/parameters/EditingCircuitComponentPosition|EditingCircuitComponentPosition]] | setting | boolean | N/A | When true the circuit is currently being edited |
| [[motorcad/parameter_database/parameters/EmbeddedMagnetCapacitanceMethod|EmbeddedMagnetCapacitanceMethod]] | compatibility | integer | N/A | The calculation method of embedded magnet capacitance |
| [[motorcad/parameter_database/parameters/EmbeddedMagnetPoleRadius_Method|EmbeddedMagnetPoleRadius_Method]] | compatibility | integer | N/A | Method used to calculate the radius between rotor back iron and embedded magnet pole |
| [[motorcad/parameter_database/parameters/EnableAdvancedUI_Drive|EnableAdvancedUI_Drive]] | i/p | boolean | N/A | Enables advanced interface for drive development features |
| [[motorcad/parameter_database/parameters/EnableAutomaticTransientGraphUpdate|EnableAutomaticTransientGraphUpdate]] | o/p | boolean | N/A | When enabled the transient graph will be updated during the calculation (every Periods Per Graph Update) |
| [[motorcad/parameter_database/parameters/EndCapSpecification|EndCapSpecification]] | i/p | integer | N/A | Defines which dimensions are used to specify the end cap |
| [[motorcad/parameter_database/parameters/EndCapVentCalculation|EndCapVentCalculation]] | compatibility | integer | N/A | This determines whether to use the original endcap vent calculation or to use the new method |
| [[motorcad/parameter_database/parameters/EndCapVents_Front|EndCapVents_Front]] | i/p | integer | N/A | Are the internal end sections of the motor closed or open to external air |
| [[motorcad/parameter_database/parameters/EndCapVents_Rear|EndCapVents_Rear]] | i/p | integer | N/A | Are the internal end sections of the motor closed or open to external air |
| [[motorcad/parameter_database/parameters/EndSpaceChangeRate|EndSpaceChangeRate]] | i/p | double | °C | The maximum rate of change of the end space fluid. When reduced it may aid convergence |
| [[motorcad/parameter_database/parameters/EndSpaceResistanceCalc|EndSpaceResistanceCalc]] | compatibility | integer | N/A | Method of calculating end space resistances. |
| [[motorcad/parameter_database/parameters/EndSpaceVelocitiesCalc|EndSpaceVelocitiesCalc]] | compatibility | integer | N/A | The method of calculation for air velocities in the end space. |
| [[motorcad/parameter_database/parameters/EndWdgEnamelModel|EndWdgEnamelModel]] | compatibility | integer | N/A | The model used for endwinding enamel |
| [[motorcad/parameter_database/parameters/EndWdgInductanceMethod|EndWdgInductanceMethod]] | compatibility | integer | N/A | Method used to calculate coil cross-sectional area in calculation of endwinding inductance |
| [[motorcad/parameter_database/parameters/EndWdgSpecification|EndWdgSpecification]] | i/p | integer | N/A | Defines which dimensions are used to specify the end winding |
| [[motorcad/parameter_database/parameters/EndWindingLengthMethod|EndWindingLengthMethod]] | compatibility | integer | N/A | The method used to calculate the stator endwinding length |
| [[motorcad/parameter_database/parameters/EndWindingLossSplitDefinition|EndWindingLossSplitDefinition]] | recommended | integer | N/A | How the end winding losses are split between front and rear end windings. |
| [[motorcad/parameter_database/parameters/EndcapCapacitanceCalc|EndcapCapacitanceCalc]] | compatibility | integer | N/A | The capacitance calculation for the Housing and Endcap when there is no Housing F/R |
| [[motorcad/parameter_database/parameters/EndcapFlangeCalc|EndcapFlangeCalc]] | compatibility | integer | N/A | Calculation method of Flange weight and natural convection |
| [[motorcad/parameter_database/parameters/EndringInductanceMethod|EndringInductanceMethod]] | i/p | integer | N/A | Select the method to use for endring inductances |
| [[motorcad/parameter_database/parameters/Export3DGeometryFileName|Export3DGeometryFileName]] | setting | OleStr | N/A | Filename for 3D geometry animation export |
| [[motorcad/parameter_database/parameters/ExternalApplicationCoupling|ExternalApplicationCoupling]] | setting | integer | N/A | Selects the external application to use for import/export coupling |
| [[motorcad/parameter_database/parameters/ExternalCircuitDutyCycleControl|ExternalCircuitDutyCycleControl]] | compatibility | integer | N/A | Specifies whether power and fixed temperature values defined inside external circuit or duty cycle are used for the duty cycle calculation |
| [[motorcad/parameter_database/parameters/ExternalPowerDistributionCalc|ExternalPowerDistributionCalc]] | compatibility | integer | N/A | Method used to apply external power injection/source to axially sliced central nodes |
| [[motorcad/parameter_database/parameters/FEALossCalcType|FEALossCalcType]] | compatibility | integer | N/A | The FEA integral method used for Bertotti and Steimetz iron loss calculations |
| [[motorcad/parameter_database/parameters/FEAPoleFixedTemperature|FEAPoleFixedTemperature]] | recommended | integer | N/A | This selects the pole fixed temperature surfaces |
| [[motorcad/parameter_database/parameters/FEASlotAreaCalculation|FEASlotAreaCalculation]] | compatibility | integer | N/A | Area calculation used by FEA for slot current densities |
| [[motorcad/parameter_database/parameters/FEASlotFixedTemperature|FEASlotFixedTemperature]] | recommended | integer | N/A | This selects the slot fixed temperature surfaces |
| [[motorcad/parameter_database/parameters/FEA_ThermalSlot_LossDistribution|FEA_ThermalSlot_LossDistribution]] | i/p | integer | N/A | The selection of the loss distribution for thermal slot FEA |
| [[motorcad/parameter_database/parameters/FEAverageGraph|FEAverageGraph]] | setting | boolean | N/A | Drawing options for the torque graph |
| [[motorcad/parameter_database/parameters/FEShadingFunctionString_Magnetic|FEShadingFunctionString_Magnetic]] | setting | OleStr | N/A | Set FE module shading function view for magnetic |
| [[motorcad/parameter_database/parameters/FEShadingFunctionString_Mechanical|FEShadingFunctionString_Mechanical]] | setting | OleStr | N/A | Set FE module shading function view for mechanical |
| [[motorcad/parameter_database/parameters/FEShadingFunctionString_Thermal|FEShadingFunctionString_Thermal]] | setting | OleStr | N/A | Set FE module shading function view for thermal |
| [[motorcad/parameter_database/parameters/FEShadingFunction_Magnetic|FEShadingFunction_Magnetic]] | setting | OleStr | N/A | Set FE module shading function view for magnetic |
| [[motorcad/parameter_database/parameters/FEShadingFunction_Mechanical|FEShadingFunction_Mechanical]] | setting | OleStr | N/A | Set FE module shading function view for mechanical |
| [[motorcad/parameter_database/parameters/FEShadingFunction_Thermal|FEShadingFunction_Thermal]] | setting | OleStr | N/A | Set FE module shading function view for thermal |
| [[motorcad/parameter_database/parameters/FEShadingRegionString_Magnetic|FEShadingRegionString_Magnetic]] | setting | OleStr | N/A | Set FE module shading region view for magnetic |
| [[motorcad/parameter_database/parameters/FEShadingRegionString_Mechanical|FEShadingRegionString_Mechanical]] | setting | OleStr | N/A | Set FE module shading region view for mechanical |
| [[motorcad/parameter_database/parameters/FEShadingRegionString_Thermal|FEShadingRegionString_Thermal]] | setting | OleStr | N/A | Set FE module shading region view for thermal |
| [[motorcad/parameter_database/parameters/FEShadingRegion_Magnetic|FEShadingRegion_Magnetic]] | setting | integer | N/A | Set FE module shading region view for magnetic |
| [[motorcad/parameter_database/parameters/FEShadingRegion_Mechanical|FEShadingRegion_Mechanical]] | setting | integer | N/A | Set FE module shading region view for mechanical |
| [[motorcad/parameter_database/parameters/FEShadingRegion_Thermal|FEShadingRegion_Thermal]] | setting | integer | N/A | Set FE module shading region view for thermal |
| [[motorcad/parameter_database/parameters/FEShading_Magnetic|FEShading_Magnetic]] | setting | integer | N/A | Set FE module shading view for magnetic |
| [[motorcad/parameter_database/parameters/FEShading_MagneticLosses|FEShading_MagneticLosses]] | setting | integer | N/A | Set FE module shading view for magnetic losses |
| [[motorcad/parameter_database/parameters/FEShading_Mechanical|FEShading_Mechanical]] | setting | integer | N/A | Set FE module shading view for mechanical |
| [[motorcad/parameter_database/parameters/FEShading_Thermal|FEShading_Thermal]] | setting | integer | N/A | Set FE module shading view for thermal |
| [[motorcad/parameter_database/parameters/Fault_Type|Fault_Type]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/FieldWdgSeparatorMechCalc|FieldWdgSeparatorMechCalc]] | compatibility | integer | N/A | When enabled the presence of a winding separator is taken into account when calculating the rotor mechanical stress |
| [[motorcad/parameter_database/parameters/FieldWindingLengthMethod|FieldWindingLengthMethod]] | compatibility | integer | N/A | The method used to calculate the field winding length |
| [[motorcad/parameter_database/parameters/Filled_Rotor_Pole_Space|Filled_Rotor_Pole_Space]] | i/p | integer | N/A | 0 = Not Filled,   1 = Filled |
| [[motorcad/parameter_database/parameters/FinInputOptions|FinInputOptions]] | i/p | double | N/A | parameters used to input fin dimensions |
| [[motorcad/parameter_database/parameters/FirstSetConductors|FirstSetConductors]] | setting | integer | N/A | Number of conductors in the first set |
| [[motorcad/parameter_database/parameters/FixedTemperatureMethod|FixedTemperatureMethod]] | compatibility | integer | N/A | This is method for fixing any fixed node temperatures in model |
| [[motorcad/parameter_database/parameters/Fixed_Axle_F_Temperature|Fixed_Axle_F_Temperature]] | i/p | boolean | °C | Fix Axle[F] temperature at set value (by injecting power into plate) |
| [[motorcad/parameter_database/parameters/Fixed_Axle_R_Temperature|Fixed_Axle_R_Temperature]] | i/p | boolean | °C | Fix Axle[R] temperature at set value (by injecting power into plate) |
| [[motorcad/parameter_database/parameters/Fixed_Base_Temperature|Fixed_Base_Temperature]] | i/p | boolean | °C | Fix plate temperature at set value (by injecting power into plate) |
| [[motorcad/parameter_database/parameters/Fixed_Endcap_F_Temperature|Fixed_Endcap_F_Temperature]] | i/p | boolean | °C | Fix endcap[F] temperature at set value (by injecting power into plate) |
| [[motorcad/parameter_database/parameters/Fixed_Endcap_R_Temperature|Fixed_Endcap_R_Temperature]] | i/p | boolean | °C | Fix endcap[R] temperature at set value (by injecting power into plate) |
| [[motorcad/parameter_database/parameters/Fixed_Plate_Temperature|Fixed_Plate_Temperature]] | i/p | boolean | °C | Fix base temperature at set value (by injecting power into base) |
| [[motorcad/parameter_database/parameters/Fixed_Shaft_F_Temperature|Fixed_Shaft_F_Temperature]] | i/p | boolean | °C | Fix shaft[F] temperature at set value (by injecting power into plate) |
| [[motorcad/parameter_database/parameters/Fixed_Shaft_R_Temperature|Fixed_Shaft_R_Temperature]] | i/p | boolean | °C | Fix shaft[R] temperature at set value (by injecting power into plate) |
| [[motorcad/parameter_database/parameters/FlangePlateAreaCalc|FlangePlateAreaCalc]] | compatibility | integer | N/A | The area calculation for the flange plate |
| [[motorcad/parameter_database/parameters/FlowAreaWindingIncludeSleeve|FlowAreaWindingIncludeSleeve]] | compatibility | integer | N/A | The calculation of the Flow Area around the Endwinding considering the presence of a sleeve |
| [[motorcad/parameter_database/parameters/FlowBetweenConductorsCuboidModel|FlowBetweenConductorsCuboidModel]] | recommended | integer | N/A | Consideration of the wire insulation and impregnation external to the cuboid for Slot WJ flow between conductors |
| [[motorcad/parameter_database/parameters/FlowBetweenRectangularConductorsAreaCalc|FlowBetweenRectangularConductorsAreaCalc]] | compatibility | integer | N/A | Calculation method of the rectangular conductor surface area when have Flow Between Conductors |
| [[motorcad/parameter_database/parameters/FlowResistanceTolerance|FlowResistanceTolerance]] | i/p | double | N/A | Used to help flow solving. Flow resistances greater than this value will be removed from circuit. |
| [[motorcad/parameter_database/parameters/FlowVisualisationArrowScaling|FlowVisualisationArrowScaling]] | setting | double | N/A | This sets the scaling multiplier of the flow arrows |
| [[motorcad/parameter_database/parameters/FlowVisualisationArrowSpacingFactor|FlowVisualisationArrowSpacingFactor]] | setting | double | N/A | This sets the arrow spacing factor per flow |
| [[motorcad/parameter_database/parameters/FlowVisualisationHeadWidth|FlowVisualisationHeadWidth]] | setting | double | N/A | This sets the width of the flow arrow head as proportion of airgap size |
| [[motorcad/parameter_database/parameters/FlowVisualisationMinArrowLength|FlowVisualisationMinArrowLength]] | setting | double | mm | This sets the minimum length of arrow per flow as proportion of airgap size |
| [[motorcad/parameter_database/parameters/FlowVisualisationTailWidth|FlowVisualisationTailWidth]] | setting | double | N/A | This sets the width of the flow arrow tail as proportion of airgap size |
| [[motorcad/parameter_database/parameters/FluidNodesExternalPowerInjectionCalc|FluidNodesExternalPowerInjectionCalc]] | compatibility | integer | N/A | Method used to apply external power injection to fluid nodes during transient calculation |
| [[motorcad/parameter_database/parameters/FluidPathsCompensationEnabled|FluidPathsCompensationEnabled]] | i/p | integer | N/A | This setting enables or disables the fluid path compensation factor. |
| [[motorcad/parameter_database/parameters/FluidPathsCompensationFactor|FluidPathsCompensationFactor]] | i/p | double | N/A | This is the maximum proportion of total machine losses used for the fluid compensation, this can be useful for improving transient convergence |
| [[motorcad/parameter_database/parameters/FluidPathsScaleFactor|FluidPathsScaleFactor]] | i/p | double | N/A | This is the scaling used for the fluid compensation, this can be useful for improving transient convergence. Smaller value should be aid convergence. |
| [[motorcad/parameter_database/parameters/FluxDensitySkewMethod|FluxDensitySkewMethod]] | compatibility | integer | N/A | The calculation method of skewed airgap flux densities |
| [[motorcad/parameter_database/parameters/FluxDensitySkewMethod_Iron|FluxDensitySkewMethod_Iron]] | compatibility | integer | N/A | The calculation method of skewed stator/rotor flux densities |
| [[motorcad/parameter_database/parameters/FluxLinkageGraph|FluxLinkageGraph]] | setting | boolean | N/A | Drawing options for the flux linkage torque graph |
| [[motorcad/parameter_database/parameters/ForceAnimationCaption|ForceAnimationCaption]] | setting | integer | N/A | Apply a caption to each frame of animation which describes the type of animation |
| [[motorcad/parameter_database/parameters/ForceAnimationExportRepeat|ForceAnimationExportRepeat]] | setting | integer | N/A | Set the animation to auto repeat in the exported force animation GIF file |
| [[motorcad/parameter_database/parameters/ForceAnimationExportSpeed|ForceAnimationExportSpeed]] | setting | integer | N/A | Set the speed for the exported force animation GIF file |
| [[motorcad/parameter_database/parameters/ForceAnimationFileName|ForceAnimationFileName]] | i/p | OleStr | N/A | The filepath for exporting force, harmonic and harmonic reconstruction animations to file |
| [[motorcad/parameter_database/parameters/ForceAnimationNormalisation|ForceAnimationNormalisation]] | setting | integer | N/A | Normalise animation based on overall maximum or individual harmonic maximum |
| [[motorcad/parameter_database/parameters/ForceAnimationRepeat|ForceAnimationRepeat]] | setting | integer | N/A | Option to auto repeat the aniamtions in the user interface |
| [[motorcad/parameter_database/parameters/ForceAnimations_SelectedAnimations|ForceAnimations_SelectedAnimations]] | setting | double | N/A | The NVH force animations selected in Forces interface |
| [[motorcad/parameter_database/parameters/ForceAnimations_SelectedAnimationsLength|ForceAnimations_SelectedAnimationsLength]] | setting | integer | N/A | The number of force animations selected within the NVH forces tab |
| [[motorcad/parameter_database/parameters/ForceDataType|ForceDataType]] | setting | integer | N/A | Select the machine location and type for force analysis - Stator/Rotor and Radial/Tangential forces |
| [[motorcad/parameter_database/parameters/ForceHarmonicOrder_Plot|ForceHarmonicOrder_Plot]] | setting | integer | N/A | Set the harmonic order axes method for the maximum harmonic order plotted |
| [[motorcad/parameter_database/parameters/ForceHarmonics|ForceHarmonics]] | i/p | integer | N/A | Whether to show harmonic analysis for radial or tangential forces |
| [[motorcad/parameter_database/parameters/ForceLocation|ForceLocation]] | i/p | integer | N/A | The location of force calculated |
| [[motorcad/parameter_database/parameters/ForceMaxOrder_Space_Rotor_OC|ForceMaxOrder_Space_Rotor_OC]] | setting | integer | N/A | Set the maximum rotor spatial harmonic order for open circuit force harmonic analysis |
| [[motorcad/parameter_database/parameters/ForceMaxOrder_Space_Rotor_OL|ForceMaxOrder_Space_Rotor_OL]] | setting | integer | N/A | Set the maximum rotor spatial harmonic order for on load force harmonic analysis |
| [[motorcad/parameter_database/parameters/ForceMaxOrder_Space_Stator_OC|ForceMaxOrder_Space_Stator_OC]] | setting | integer | N/A | Set the maximum stator spatial harmonic order for open circuit force harmonic analysis |
| [[motorcad/parameter_database/parameters/ForceMaxOrder_Space_Stator_OL|ForceMaxOrder_Space_Stator_OL]] | setting | integer | N/A | Set the maximum stator spatial harmonic order for on load force harmonic analysis |
| [[motorcad/parameter_database/parameters/ForceMaxOrder_Time_OC|ForceMaxOrder_Time_OC]] | setting | integer | N/A | Set the maximum temporal harmonic order for open circuit force harmonic analysis |
| [[motorcad/parameter_database/parameters/ForceMaxOrder_Time_OL|ForceMaxOrder_Time_OL]] | setting | integer | N/A | Set the maximum temporal harmonic order for on load force harmonic analysis |
| [[motorcad/parameter_database/parameters/ForceRadialGraph|ForceRadialGraph]] | i/p | boolean | N/A | When selected the radial force graphs are plotted |
| [[motorcad/parameter_database/parameters/ForceResultsCalculationType|ForceResultsCalculationType]] | compatibility | integer | N/A | Whether the force results for unbalanced magnetic pull should be calculated from transient data if available |
| [[motorcad/parameter_database/parameters/ForceTangentialGraph|ForceTangentialGraph]] | i/p | boolean | N/A | When selected the tangential force graphs are plotted |
| [[motorcad/parameter_database/parameters/ForceXGraph|ForceXGraph]] | i/p | boolean | N/A | When selected the x direction force graphs are plotted |
| [[motorcad/parameter_database/parameters/ForceYGraph|ForceYGraph]] | i/p | boolean | N/A | When selected the y direction force graphs are plotted |
| [[motorcad/parameter_database/parameters/ForcesInputType|ForcesInputType]] | setting | integer | N/A | Set whether using force (point) or force density (pressure) for analysis |
| [[motorcad/parameter_database/parameters/ForcesView_FrequencyDomain|ForcesView_FrequencyDomain]] | setting | integer | N/A | Select the frequency domain forces plot view to show in the user interface |
| [[motorcad/parameter_database/parameters/ForcesView_TimeDomain|ForcesView_TimeDomain]] | setting | integer | N/A | Select the time domain forces plot view to show in the user interface |
| [[motorcad/parameter_database/parameters/FormWoundConductorSeparation|FormWoundConductorSeparation]] | i/p | integer | N/A | This is the method of specifying the gaps between the conductors |
| [[motorcad/parameter_database/parameters/FormWoundRtCalc|FormWoundRtCalc]] | compatibility | integer | N/A | The calculation method of the form wound thermal resistances in the slot |
| [[motorcad/parameter_database/parameters/FreqDomain_MinAmplitude_PointForce|FreqDomain_MinAmplitude_PointForce]] | setting | double | N | Sets the minimum harmonic amplitude to plot in 2D Frequency Domain graph for force |
| [[motorcad/parameter_database/parameters/Full_Winding_Circuit_View|Full_Winding_Circuit_View]] | i/p | boolean | N/A | When this is false then the only a reduced winding circuit is shown in circuit editor |
| [[motorcad/parameter_database/parameters/GIFExport_Height|GIFExport_Height]] | setting | integer | N/A | Height of GIF export for force animations in Pixels |
| [[motorcad/parameter_database/parameters/GIFExport_Width|GIFExport_Width]] | setting | integer | N/A | Width of GIF export for force animations in Pixels |
| [[motorcad/parameter_database/parameters/HairpinACLossLocationMethod|HairpinACLossLocationMethod]] | compatibility | integer | N/A | Method used for location of Hybrid AC loss calculation of Hairpin windings |
| [[motorcad/parameter_database/parameters/HairpinActiveKValueCalc|HairpinActiveKValueCalc]] | compatibility | integer | N/A | Calculation method of the Active section Cuboid K Value for Hairpin Winding |
| [[motorcad/parameter_database/parameters/HairpinConductors_FEA|HairpinConductors_FEA]] | i/p | integer | N/A | Hairpin conductors modelling method for magnetic FEA |
| [[motorcad/parameter_database/parameters/HairpinEWdgWeightCalc|HairpinEWdgWeightCalc]] | compatibility | integer | N/A | Calculation method of the weight distribution of the Hairpin Armature EWdg |
| [[motorcad/parameter_database/parameters/HairpinEnamelThicknessCalc|HairpinEnamelThicknessCalc]] | compatibility | integer | N/A | Determines the enamel thickness used for the hairpin end winding thermal resistance calculation. |
| [[motorcad/parameter_database/parameters/HairpinWedgePathRtCalc|HairpinWedgePathRtCalc]] | compatibility | integer | N/A | Calculation of the resistances from the Hairpin Winding to the Slot Wedge |
| [[motorcad/parameter_database/parameters/HairpinWindingPatternMethod|HairpinWindingPatternMethod]] | i/p | integer | N/A | Method used to create hairpin winding pattern |
| [[motorcad/parameter_database/parameters/HarmonicAmplitude|HarmonicAmplitude]] | setting | integer | N/A | This gives the option to show the normalised harmonics graphs |
| [[motorcad/parameter_database/parameters/HeavyBuildCopperDiameterMethod|HeavyBuildCopperDiameterMethod]] | compatibility | integer | N/A | Method of calculating copper diameter when using heavy build slot fill |
| [[motorcad/parameter_database/parameters/HighestNumNode|HighestNumNode]] | o/p | integer | N/A | The highest node number in network |
| [[motorcad/parameter_database/parameters/HousingDiameterCalc|HousingDiameterCalc]] | compatibility | integer | N/A | Calculation of the stator lamination and housing diameters |
| [[motorcad/parameter_database/parameters/HousingWJActiveOnlyFlowCircuit|HousingWJActiveOnlyFlowCircuit]] | compatibility | integer | N/A | The calculation method for the Active Cooling Only Housing WJ flow circuit |
| [[motorcad/parameter_database/parameters/HousingWJActiveOnlyMethod|HousingWJActiveOnlyMethod]] | compatibility | integer | N/A | Housing Water Jacket in the stator now always uses Active Cooling Only. |
| [[motorcad/parameter_database/parameters/HousingWJCircularDuctCalc|HousingWJCircularDuctCalc]] | compatibility | integer | N/A | Calculation method of the Housing WJ Flow Resistance and Thermal Resistance for Circular/Rectangular Stator Ducts |
| [[motorcad/parameter_database/parameters/HousingWJCoupledCoolingCalc|HousingWJCoupledCoolingCalc]] | compatibility | integer | N/A | Calculation of the Housing WJ fluid temperature with series endcap flow when coupled to another cooling system |
| [[motorcad/parameter_database/parameters/HousingWJDuctWallThicknessCalc|HousingWJDuctWallThicknessCalc]] | compatibility | integer | N/A | Calculation method for Housing WJ parameters with non-zero duct wall thickness |
| [[motorcad/parameter_database/parameters/HousingWJFlowRemoved|HousingWJFlowRemoved]] | i/p | boolean | N/A | The flow is removed during the transient calculation period |
| [[motorcad/parameter_database/parameters/HousingWJFluidWeightCalc|HousingWJFluidWeightCalc]] | compatibility | integer | N/A | The calculation method for the Housing Water Jacket Fluid Weight and Capacitance |
| [[motorcad/parameter_database/parameters/HousingWJFrictionFactorCalc|HousingWJFrictionFactorCalc]] | compatibility | integer | N/A | Calculation method for Housing WJ friction factor with non-zero duct wall thickness, and Nusselt number with multiple duct layers |
| [[motorcad/parameter_database/parameters/HousingWJLengthL2Calc|HousingWJLengthL2Calc]] | compatibility | integer | N/A | Calculation method of the characteristic length of Housing Water L2 ducts |
| [[motorcad/parameter_database/parameters/HousingWJOutputTempsMethod|HousingWJOutputTempsMethod]] | compatibility | integer | N/A | Calculation method of the Housing WJ fluid output data temperatures |
| [[motorcad/parameter_database/parameters/HousingWJParallelPathsCalc|HousingWJParallelPathsCalc]] | compatibility | integer | N/A | Calculation method for the distribution of Housing WJ parallel flow paths and lengths used for rear htc calculation with multiple duct layers |
| [[motorcad/parameter_database/parameters/HousingWJRectangularDuctCalc|HousingWJRectangularDuctCalc]] | compatibility | integer | N/A | Calculation method of Housing WJ parameters for Rectangular Stator Ducts |
| [[motorcad/parameter_database/parameters/HousingWJ_RotorWJ_Connection|HousingWJ_RotorWJ_Connection]] | i/p | boolean | N/A | When selected the housing water jacket outlet is connected to the rotor water jacket inlet |
| [[motorcad/parameter_database/parameters/HousingWJ_SlotWJ_Connection|HousingWJ_SlotWJ_Connection]] | i/p | boolean | N/A | When selected the housing water jacket outlet is connected to the slot water jacket inlet |
| [[motorcad/parameter_database/parameters/HousingWJ_SprayCooling_Connection|HousingWJ_SprayCooling_Connection]] | i/p | boolean | N/A | When selected the housing water jacket outlet is connected to the spray cooling inlet |
| [[motorcad/parameter_database/parameters/Housing_Water_Jacket|Housing_Water_Jacket]] | i/p | boolean | N/A | Use housing water jacket model for forced cooling of housing spiral groove or axial zig-zag arrangement. |
| [[motorcad/parameter_database/parameters/HybridACLossMethod|HybridACLossMethod]] | compatibility | integer | N/A | This sets how the Hybrid FEA AC losses are calculated |
| [[motorcad/parameter_database/parameters/HysIronLossMethod|HysIronLossMethod]] | compatibility | integer | N/A | Method used by FEA to calculate hysteresis iron losses |
| [[motorcad/parameter_database/parameters/IM1PH_ImpregAreaRatiosCalculation|IM1PH_ImpregAreaRatiosCalculation]] | compatibility | integer | N/A | Calculation method for the proportions of total active impreg in Liner-Lam gap and in main body of winding for IM1PH |
| [[motorcad/parameter_database/parameters/IMAccelerationGraph|IMAccelerationGraph]] | i/p | integer | N/A | The acceleration graph to view |
| [[motorcad/parameter_database/parameters/IMCuboidal_BarHeight|IMCuboidal_BarHeight]] | o/p | double | mm | This is the height of the bar cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_BarLength|IMCuboidal_BarLength]] | o/p | double | mm | This is the length of the bar cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_BarWidth|IMCuboidal_BarWidth]] | o/p | double | mm | This is the width of the bar cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_EndringHeight_F|IMCuboidal_EndringHeight_F]] | o/p | double | mm | This is the height of the endring cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_EndringHeight_R|IMCuboidal_EndringHeight_R]] | o/p | double | mm | This is the height of the endring cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_EndringLength_F|IMCuboidal_EndringLength_F]] | o/p | double | mm | This is the length of the endring cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_EndringLength_R|IMCuboidal_EndringLength_R]] | o/p | double | mm | This is the length of the endring cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_EndringWidth_F|IMCuboidal_EndringWidth_F]] | o/p | double | mm | This is the width of the endring cuboid |
| [[motorcad/parameter_database/parameters/IMCuboidal_EndringWidth_R|IMCuboidal_EndringWidth_R]] | o/p | double | mm | This is the width of the endring cuboid |
| [[motorcad/parameter_database/parameters/IMEfficiencyGraph|IMEfficiencyGraph]] | i/p | integer | N/A | The efficiency graph to view |
| [[motorcad/parameter_database/parameters/IMEndringExt_htc_Calc|IMEndringExt_htc_Calc]] | compatibility | integer | N/A | Calculation method for htc values of IM Endring Extensions to the Endspace and Through Ventilated cooling. |
| [[motorcad/parameter_database/parameters/IMEndringExtensionCorrectionMethod|IMEndringExtensionCorrectionMethod]] | compatibility | integer | N/A | Correction of rotor bar resistivity to account for end ring extensions |
| [[motorcad/parameter_database/parameters/IMFEABarResistivityCorrectionMethod|IMFEABarResistivityCorrectionMethod]] | compatibility | integer | N/A | Correction of rotor bar resistivity to account for end ring resistance |
| [[motorcad/parameter_database/parameters/IMLockedRotorInductanceMethod|IMLockedRotorInductanceMethod]] | compatibility | integer | N/A | Method for calculating locked rotor referred rotor bar leakage inductance. |
| [[motorcad/parameter_database/parameters/IMLockedRotorTorqueAverageMethod|IMLockedRotorTorqueAverageMethod]] | compatibility | integer | N/A | Method for calculating the locked rotor average torques. Improved method uses final cycle, original method uses all cycles. |
| [[motorcad/parameter_database/parameters/IMLookupPoints_Loss|IMLookupPoints_Loss]] | i/p | integer | N/A | Number of points to calculate for loss lookup tables |
| [[motorcad/parameter_database/parameters/IMLookupPoints_Saturation|IMLookupPoints_Saturation]] | i/p | integer | N/A | Number of points to calculate for saturation lookup tables |
| [[motorcad/parameter_database/parameters/IMLookupResetMethod|IMLookupResetMethod]] | compatibility | integer | N/A | Method used to reset IM lookup tables |
| [[motorcad/parameter_database/parameters/IMLossSumMethod|IMLossSumMethod]] | compatibility | integer | N/A | Calculation method of losses for Locked Rotor and Core Loss performance tests |
| [[motorcad/parameter_database/parameters/IMRadialDuctMethod|IMRadialDuctMethod]] | compatibility | integer | N/A | Incorporation of radial ducts in IM analytic equations. |
| [[motorcad/parameter_database/parameters/IMRotorThermalCircuitMethod|IMRotorThermalCircuitMethod]] | compatibility | integer | N/A | The induction machine rotor thermal resistance calculation method to use (should use improved method) |
| [[motorcad/parameter_database/parameters/IMSingleLoadCompletedCycles_NonRotating|IMSingleLoadCompletedCycles_NonRotating]] | o/p | integer | N/A | Number of cycles completed by a non-rotating single load point calculation |
| [[motorcad/parameter_database/parameters/IMSingleLoadConvergenceMethod_NonRotating|IMSingleLoadConvergenceMethod_NonRotating]] | i/p | integer | N/A | Allow a non-rotating single load point calculation to end early if solution is converged |
| [[motorcad/parameter_database/parameters/IMSingleLoadMaximumCycles_NonRotating|IMSingleLoadMaximumCycles_NonRotating]] | i/p | integer | N/A | The maximum number of cycles to perform before stopping a non-rotating single load calculation |
| [[motorcad/parameter_database/parameters/IMSingleLoadNumberCycles_NonRotating|IMSingleLoadNumberCycles_NonRotating]] | i/p | integer | N/A | Number of cycles to perform for a non-rotating single load point calculation (IM) |
| [[motorcad/parameter_database/parameters/IMSingleLoadNumberCycles_Rotating|IMSingleLoadNumberCycles_Rotating]] | i/p | integer | N/A | Number of cycles to perform for a rotating single load point calculation (IM) |
| [[motorcad/parameter_database/parameters/IMSingleLoadPointRotorInductanceMethod|IMSingleLoadPointRotorInductanceMethod]] | compatibility | integer | N/A | Method for calculating single load point referred rotor bar leakage inductance. |
| [[motorcad/parameter_database/parameters/IMSingleLoadPointsPerCycle_NonRotating|IMSingleLoadPointsPerCycle_NonRotating]] | i/p | integer | N/A | Number of points to calculate for each cycle of a non-rotating single load point calculation (IM) |
| [[motorcad/parameter_database/parameters/IMSingleLoadPointsPerCycle_Rotating|IMSingleLoadPointsPerCycle_Rotating]] | i/p | integer | N/A | Number of points to calculate for each cycle of a rotating single load point calculation (IM) |
| [[motorcad/parameter_database/parameters/IMSingleLoadTolerance_NonRotating|IMSingleLoadTolerance_NonRotating]] | i/p | double | N/A | Error value at which to end a non-rotating single load point calculation early |
| [[motorcad/parameter_database/parameters/IMSkewingCalc_Compatibility|IMSkewingCalc_Compatibility]] | compatibility | integer | N/A | Whether to use the original or improved calculation for IM skew effect (original should be used for backwards compatibility only) |
| [[motorcad/parameter_database/parameters/IMSkewingMethod|IMSkewingMethod]] | i/p | integer | N/A | Select the method to use for calculating IM skew effect |
| [[motorcad/parameter_database/parameters/IMSkinEffectMethod|IMSkinEffectMethod]] | compatibility | integer | N/A | Calculation method of skin effect in IM rotor bars |
| [[motorcad/parameter_database/parameters/IMStatorCopperLossesMethod|IMStatorCopperLossesMethod]] | compatibility | integer | N/A | Calculation method of losses for induction machines with more than three phases. |
| [[motorcad/parameter_database/parameters/IMTorqueMethod|IMTorqueMethod]] | compatibility | integer | N/A | to use the original or improved method for IM analytic torque calculation (original should be used for backwards compatibility only) |
| [[motorcad/parameter_database/parameters/IM_BottomBar_TipAngle_DrawMethod|IM_BottomBar_TipAngle_DrawMethod]] | compatibility | integer | N/A | The method for drawing the IM Rectangular Bottom Bar |
| [[motorcad/parameter_database/parameters/IM_TopBar_TipAngle_DrawMethod|IM_TopBar_TipAngle_DrawMethod]] | compatibility | integer | N/A | The method for drawing the IM Rectangular Top Bar when the Tip Angle = 0 |
| [[motorcad/parameter_database/parameters/ImprovedFormWoundEWdgDrawing|ImprovedFormWoundEWdgDrawing]] | compatibility | boolean | N/A | When true then the improved form wound endwinding drawing to wedge is used |
| [[motorcad/parameter_database/parameters/Improved_RotorLam_Axial_Resistances|Improved_RotorLam_Axial_Resistances]] | compatibility | integer | N/A | Method used for calculation of rotor lamination axial thermal resistances |
| [[motorcad/parameter_database/parameters/IncludeCoilDividerNode|IncludeCoilDividerNode]] | i/p | boolean | N/A | When enabled a node is provided for the coil divider. This node is connected to the middle winding layer. |
| [[motorcad/parameter_database/parameters/IncludeDucts_Magnetic|IncludeDucts_Magnetic]] | i/p | integer | N/A | Whether the ducts are included in magnetic FEA simulations |
| [[motorcad/parameter_database/parameters/IncludeFinEfficiency|IncludeFinEfficiency]] | compatibility | boolean | N/A | Include Fin Efficiency included in lump-circuit model |
| [[motorcad/parameter_database/parameters/IncludeRadiation|IncludeRadiation]] | i/p | boolean | N/A | Include radiation in lump-circuit model |
| [[motorcad/parameter_database/parameters/IncludeRadiation_Internal|IncludeRadiation_Internal]] | i/p | boolean | N/A | Include Internal Radiation in lump-circuit model |
| [[motorcad/parameter_database/parameters/IncludeSteadyStatorPowerFlowError|IncludeSteadyStatorPowerFlowError]] | i/p | boolean | N/A | When selected the power flow error is included in the steady state error |
| [[motorcad/parameter_database/parameters/Include_Rt_Endcap_Axial|Include_Rt_Endcap_Axial]] | compatibility | boolean | N/A | Include endcap thermal resistances (axial direction) |
| [[motorcad/parameter_database/parameters/Include_Rt_Endcap_Radial|Include_Rt_Endcap_Radial]] | compatibility | boolean | N/A | Include endcap thermal resistances (radial direction) |
| [[motorcad/parameter_database/parameters/InductanceCalcMethod_BPM|InductanceCalcMethod_BPM]] | setting | integer | N/A | Method used to calculate inductance |
| [[motorcad/parameter_database/parameters/InductanceNumberCycles|InductanceNumberCycles]] | i/p | integer | N/A | Number cycles to perform for Inductance calculation |
| [[motorcad/parameter_database/parameters/InductancePointsPerCycle|InductancePointsPerCycle]] | i/p | integer | N/A | Number of points to calculate for each cycle of Inductance calculation |
| [[motorcad/parameter_database/parameters/InductanceSolver_BPM|InductanceSolver_BPM]] | setting | integer | N/A | Specify the inductance solver (for the Small Signal method only). |
| [[motorcad/parameter_database/parameters/InitialCoolantTemperature|InitialCoolantTemperature]] | i/p | double | °C | The initial temperature of the cooling system fluid for the transient calculation |
| [[motorcad/parameter_database/parameters/InitialFlangeTemperature|InitialFlangeTemperature]] | i/p | double | °C | The initial temperature of the flange for the transient calculation |
| [[motorcad/parameter_database/parameters/InitialHousingTemperature|InitialHousingTemperature]] | i/p | double | °C | The initial temperature of the housing for the transient calculation |
| [[motorcad/parameter_database/parameters/InitialMagnetTemperature|InitialMagnetTemperature]] | i/p | double | °C | The initial temperature of the magnets for the transient calculation |
| [[motorcad/parameter_database/parameters/InitialRotorCopperTemperature|InitialRotorCopperTemperature]] | i/p | double | °C | The initial temperature of the rotor copper (field winding or rotor bars) for the transient thermal calculation |
| [[motorcad/parameter_database/parameters/InitialRotorTemperature|InitialRotorTemperature]] | i/p | double | °C | The initial temperature of the rotor lamination for the transient calculation |
| [[motorcad/parameter_database/parameters/InitialStatorTemperature|InitialStatorTemperature]] | i/p | double | °C | The initial temperature of the stator for the transient calculation |
| [[motorcad/parameter_database/parameters/InitialTransientFluidAxialSliceMethod|InitialTransientFluidAxialSliceMethod]] | compatibility | integer | N/A | Method used to set axially sliced fluid node initial temperatures for transient calculation |
| [[motorcad/parameter_database/parameters/InitialTransientFluidTempMethod|InitialTransientFluidTempMethod]] | compatibility | integer | N/A | Method used to set initial fluid temperatures for transient calculation with specified machine starting temperature |
| [[motorcad/parameter_database/parameters/InitialTransientMachineTempMethod|InitialTransientMachineTempMethod]] | compatibility | integer | N/A | Method used to set initial specified machine temperatures for transient calculation |
| [[motorcad/parameter_database/parameters/InitialTransientMagTempMethod|InitialTransientMagTempMethod]] | compatibility | integer | N/A | Method used to set initial magnet temperatures for thermal transient calculation. |
| [[motorcad/parameter_database/parameters/InitialTransientTemperatureOption|InitialTransientTemperatureOption]] | i/p | integer | N/A | The transient calculation will be started with the machine temperatures specified. |
| [[motorcad/parameter_database/parameters/InitialTransientWdgTempMethod|InitialTransientWdgTempMethod]] | compatibility | integer | N/A | Method used to set initial winding temperatures for thermal transient calculation. |
| [[motorcad/parameter_database/parameters/InitialWindingTemperature|InitialWindingTemperature]] | i/p | double | °C | The initial temperature of the winding for the transient calculation |
| [[motorcad/parameter_database/parameters/Initial_Machine_Temperature|Initial_Machine_Temperature]] | i/p | double | °C | The initial temperature of the machine for the transient calculation |
| [[motorcad/parameter_database/parameters/InnerWindingESpaceAreaCalc|InnerWindingESpaceAreaCalc]] | compatibility | integer | N/A | The calculation method for the Endwinding End Space Areas for Inner Winding machines |
| [[motorcad/parameter_database/parameters/InnerWindingHeight|InnerWindingHeight]] | i/p | double | mm | This is the height of the winding cuboid towards slot opening |
| [[motorcad/parameter_database/parameters/InnerWindingWidth|InnerWindingWidth]] | i/p | double | mm | This is the width of the winding cuboid towards slot opening |
| [[motorcad/parameter_database/parameters/InsulationLifeRefTemp1|InsulationLifeRefTemp1]] | i/p | double | °C | This is reference temperature 1 for which material life is given |
| [[motorcad/parameter_database/parameters/InsulationLifeRefTemp2|InsulationLifeRefTemp2]] | i/p | double | °C | This is reference temperature 2 for which material life is given |
| [[motorcad/parameter_database/parameters/InsulationLifetimeAtTempRef1|InsulationLifetimeAtTempRef1]] | i/p | double | N/A | This is the insulation life at reference temperature 1 |
| [[motorcad/parameter_database/parameters/InsulationLifetimeAtTempRef2|InsulationLifetimeAtTempRef2]] | i/p | double | N/A | This is the insulation life at reference temperature 2 |
| [[motorcad/parameter_database/parameters/InsulationLifetimeMethod|InsulationLifetimeMethod]] | i/p | integer | N/A | When enabled the insulation lifetime is calculated based on the maximum winding temperature. |
| [[motorcad/parameter_database/parameters/InteriorFlatAreaCalc|InteriorFlatAreaCalc]] | compatibility | integer | N/A | Calculation method of the magnet, rotor and lamination area for Interior Flat rotor types |
| [[motorcad/parameter_database/parameters/InteriorVUMagnetResistanceCalc|InteriorVUMagnetResistanceCalc]] | compatibility | integer | N/A | Whether to use the original or improved calculation methods for Interior V and U Magnets |
| [[motorcad/parameter_database/parameters/IronLossFactorWithLossVariationTempLoad|IronLossFactorWithLossVariationTempLoad]] | i/p | boolean | N/A | When enabled iron loss multiplication factors can be entered in the duty cycle. This can be useful for variation with field weakening. |
| [[motorcad/parameter_database/parameters/IronLoss_BertottiMaxwellCoefficients_Method|IronLoss_BertottiMaxwellCoefficients_Method]] | compatibility | integer | N/A | Calculation method used for finding the coefficients for  Bertotti (Maxwell) iron loss |
| [[motorcad/parameter_database/parameters/IterationAverageCycles|IterationAverageCycles]] | i/p | integer | N/A | The number of steps used in averaging the steady state node temperatures to aid convergence. Range = [1..100] |
| [[motorcad/parameter_database/parameters/KEndringCalculationMethod|KEndringCalculationMethod]] | compatibility | integer | N/A | Calculation method of endring resistance |
| [[motorcad/parameter_database/parameters/K_AxialLitz_A|K_AxialLitz_A]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [active] in the axial direction |
| [[motorcad/parameter_database/parameters/K_AxialLitz_F|K_AxialLitz_F]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [front] in the axial direction |
| [[motorcad/parameter_database/parameters/K_AxialLitz_R|K_AxialLitz_R]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [rear] in the axial direction |
| [[motorcad/parameter_database/parameters/K_Axial_A|K_Axial_A]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [active] in the axial direction |
| [[motorcad/parameter_database/parameters/K_Axial_F|K_Axial_F]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [front] in the axial direction |
| [[motorcad/parameter_database/parameters/K_Axial_R|K_Axial_R]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [rear] in the axial direction |
| [[motorcad/parameter_database/parameters/K_Axial_User_A|K_Axial_User_A]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [active] in the axial direction |
| [[motorcad/parameter_database/parameters/K_Axial_User_F|K_Axial_User_F]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [front] in the axial direction |
| [[motorcad/parameter_database/parameters/K_Axial_User_R|K_Axial_User_R]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [rear] in the axial direction |
| [[motorcad/parameter_database/parameters/K_EquivWire_2|K_EquivWire_2]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the second wire |
| [[motorcad/parameter_database/parameters/K_EquivWire_3|K_EquivWire_3]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the third wire |
| [[motorcad/parameter_database/parameters/K_EquivWire_A|K_EquivWire_A]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the wire [active] |
| [[motorcad/parameter_database/parameters/K_EquivWire_F|K_EquivWire_F]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the wire [front] |
| [[motorcad/parameter_database/parameters/K_EquivWire_R|K_EquivWire_R]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the wire [rear] |
| [[motorcad/parameter_database/parameters/K_RadialLitz_A|K_RadialLitz_A]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [active] in the radial direction |
| [[motorcad/parameter_database/parameters/K_RadialLitz_F|K_RadialLitz_F]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [front] in the radial direction |
| [[motorcad/parameter_database/parameters/K_RadialLitz_R|K_RadialLitz_R]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [rear] in the radial direction |
| [[motorcad/parameter_database/parameters/K_Radial_A|K_Radial_A]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [active] in the radial direction |
| [[motorcad/parameter_database/parameters/K_Radial_F|K_Radial_F]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [front] in the radial direction |
| [[motorcad/parameter_database/parameters/K_Radial_R|K_Radial_R]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [rear] in the radial direction |
| [[motorcad/parameter_database/parameters/K_Radial_User_A|K_Radial_User_A]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [active] in the radial direction |
| [[motorcad/parameter_database/parameters/K_Radial_User_F|K_Radial_User_F]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [front] in the radial direction |
| [[motorcad/parameter_database/parameters/K_Radial_User_R|K_Radial_User_R]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [rear] in the radial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorAxial_A|K_SyncRotorAxial_A]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [active] in the axial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorAxial_F|K_SyncRotorAxial_F]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [front] in the axial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorAxial_R|K_SyncRotorAxial_R]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [rear] in the axial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorAxial_User_A|K_SyncRotorAxial_User_A]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [active] in the axial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorAxial_User_F|K_SyncRotorAxial_User_F]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [front] in the axial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorAxial_User_R|K_SyncRotorAxial_User_R]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [rear] in the axial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorEquivWire_A|K_SyncRotorEquivWire_A]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the sync rotor wire [active] |
| [[motorcad/parameter_database/parameters/K_SyncRotorEquivWire_F|K_SyncRotorEquivWire_F]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the sync rotor wire [front] |
| [[motorcad/parameter_database/parameters/K_SyncRotorEquivWire_R|K_SyncRotorEquivWire_R]] | o/p | double | W/m/°C | This is the equivalent thermal conductivity of the sync rotor wire [rear] |
| [[motorcad/parameter_database/parameters/K_SyncRotorRadial_A|K_SyncRotorRadial_A]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [active] in the radial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorRadial_F|K_SyncRotorRadial_F]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [front] in the radial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorRadial_R|K_SyncRotorRadial_R]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [rear] in the radial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorRadial_User_A|K_SyncRotorRadial_User_A]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [active] in the radial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorRadial_User_F|K_SyncRotorRadial_User_F]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [front] in the radial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorRadial_User_R|K_SyncRotorRadial_User_R]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [rear] in the radial direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorTangential_A|K_SyncRotorTangential_A]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [active] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorTangential_F|K_SyncRotorTangential_F]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [front] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorTangential_R|K_SyncRotorTangential_R]] | o/p | double | W/m/°C | This is the thermal conductivity of the sync field winding [rear] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorTangential_User_A|K_SyncRotorTangential_User_A]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [active] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorTangential_User_F|K_SyncRotorTangential_User_F]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [front] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_SyncRotorTangential_User_R|K_SyncRotorTangential_User_R]] | i/p | double | W/m/°C | This is the user input thermal conductivity of the sync field winding [rear] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_TangentialLitz_A|K_TangentialLitz_A]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [active] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_TangentialLitz_F|K_TangentialLitz_F]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [front] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_TangentialLitz_R|K_TangentialLitz_R]] | o/p | double | W/m/°C | This is the thermal conductivity of Litz bundle in winding [rear] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_Tangential_A|K_Tangential_A]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [active] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_Tangential_F|K_Tangential_F]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [front] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_Tangential_R|K_Tangential_R]] | o/p | double | W/m/°C | This is the thermal conductivity of winding [rear] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_Tangential_User_A|K_Tangential_User_A]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [active] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_Tangential_User_F|K_Tangential_User_F]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [front] in the tangential direction |
| [[motorcad/parameter_database/parameters/K_Tangential_User_R|K_Tangential_User_R]] | i/p | double | W/m/°C | This is the user input thermal conductivity of winding [rear] in the tangential direction |
| [[motorcad/parameter_database/parameters/LamHousingCoolingNodes|LamHousingCoolingNodes]] | recommended | integer | N/A | This is the method of specifying cooling nodes used for the TVent cooling through the lamination -  housing ducts |
| [[motorcad/parameter_database/parameters/Lam_H_Divider_Resistance|Lam_H_Divider_Resistance]] | compatibility | integer | N/A | The calculation method for the Circ Lam-H divider area and Through Ventilated resistances between stator/housing and Lam-H ducts. |
| [[motorcad/parameter_database/parameters/LimitToAirgapHToConduction|LimitToAirgapHToConduction]] | compatibility | integer | N/A | When enabled, the calculated value of airgap heat transfer is adjusted, as the correlations are assumed to be for heat transfer across gap rather than to the mid gap node. |
| [[motorcad/parameter_database/parameters/LinerToothSideRtCalc|LinerToothSideRtCalc]] | compatibility | integer | N/A | The calculation method of the tooth side liner resistance |
| [[motorcad/parameter_database/parameters/LockedRotorFrequencyPoints|LockedRotorFrequencyPoints]] | i/p | integer | N/A | Number of frequencies used for locked rotor calculation |
| [[motorcad/parameter_database/parameters/LockedRotorFrequencyProp|LockedRotorFrequencyProp]] | i/p | double | N/A | The proportions of the rated frequency used for locked rotor calculation |
| [[motorcad/parameter_database/parameters/LockedRotorNumberCycles|LockedRotorNumberCycles]] | i/p | integer | N/A | Number cycles to perform for locked rotor calculation |
| [[motorcad/parameter_database/parameters/LockedRotorPointsPerCycle|LockedRotorPointsPerCycle]] | i/p | integer | N/A | Number of points to calculate for each cycle of locked rotor calculation |
| [[motorcad/parameter_database/parameters/Loss_Function_Speed|Loss_Function_Speed]] | i/p | boolean | N/A | Are the thermal module losses a function of speed [y/n] |
| [[motorcad/parameter_database/parameters/MachineOrientation|MachineOrientation]] | i/p | integer | N/A | Is the motor mounted with horizontal or vertical orientation of the shaft |
| [[motorcad/parameter_database/parameters/MacroRecordFileName|MacroRecordFileName]] | o/p | OleStr | N/A | The path of the macrorecord output file |
| [[motorcad/parameter_database/parameters/MacroRecord_FileType|MacroRecord_FileType]] | o/p | integer | N/A | The file type macro record exports script to (.txt, .vbs, .mat) |
| [[motorcad/parameter_database/parameters/MacroRecord_NewOrAppendFile|MacroRecord_NewOrAppendFile]] | o/p | integer | N/A | Macro record option to either start a new file or append to a previously created file |
| [[motorcad/parameter_database/parameters/MacroRecord_PrintOldValue|MacroRecord_PrintOldValue]] | o/p | integer | N/A | Macro record option to print the current value or the current and previous value |
| [[motorcad/parameter_database/parameters/MagnetAreaCalc_BPMOR_PMDC|MagnetAreaCalc_BPMOR_PMDC]] | compatibility | integer | N/A | Specifies the calculation method for the magnet front and rear areas with BPMOR and PMDC machines |
| [[motorcad/parameter_database/parameters/MagnetCapacitanceWeight|MagnetCapacitanceWeight]] | compatibility | integer | N/A | Whether the magnet capacitance is weighted over the rotor lamination |
| [[motorcad/parameter_database/parameters/MagnetModelType|MagnetModelType]] | recommended | integer | N/A | This selects the type of magnet model to use |
| [[motorcad/parameter_database/parameters/MagnetRadialRtCalc|MagnetRadialRtCalc]] | compatibility | integer | N/A | Magnet Radial Resistance Calculation for Surface, Inset and Embedded magnets |
| [[motorcad/parameter_database/parameters/Magnetic3DView|Magnetic3DView]] | setting | integer | N/A | The viewing method for Magnetic3D data in graph viewer. |
| [[motorcad/parameter_database/parameters/MagneticGraphDrawing|MagneticGraphDrawing]] | setting | integer | N/A | Drawing options for the magnetic graphs |
| [[motorcad/parameter_database/parameters/MagneticGraphLegendLocation|MagneticGraphLegendLocation]] | setting | integer | N/A | Legend options for the magnetic graphs |
| [[motorcad/parameter_database/parameters/MagneticGraphPenWidth|MagneticGraphPenWidth]] | setting | integer | N/A | Pen width for the magnetic graphs |
| [[motorcad/parameter_database/parameters/MagneticHousingSetting|MagneticHousingSetting]] | i/p | integer | N/A | When selected the housing is included in the magnetic FEA |
| [[motorcad/parameter_database/parameters/MagneticSolverMethod|MagneticSolverMethod]] | i/p | integer | N/A | This specifies the magnetic solver to use. |
| [[motorcad/parameter_database/parameters/MaxCurrent_MagnetisationCurves|MaxCurrent_MagnetisationCurves]] | i/p | double | Amps | The max current required for the magnetisation curves |
| [[motorcad/parameter_database/parameters/MaxHarmonicOrder|MaxHarmonicOrder]] | i/p | integer | N/A | This specifies the maximum harmonic order used in harmonics calculations |
| [[motorcad/parameter_database/parameters/MaxWindingCalibration|MaxWindingCalibration]] | i/p | double | N/A | Calibrate the analytic winding model maximum temperature with the FEA results to take account of the conductor placement. |
| [[motorcad/parameter_database/parameters/MaxWindingHarmonicOrder|MaxWindingHarmonicOrder]] | i/p | integer | N/A | This specifies the maximum mechanical winding harmonic order used in harmonics calculations |
| [[motorcad/parameter_database/parameters/MaxwellAnalysis|MaxwellAnalysis]] | setting | OleStr | N/A | The Maxwell analysis name |
| [[motorcad/parameter_database/parameters/MaxwellDesign|MaxwellDesign]] | setting | OleStr | N/A | The Maxwell design name |
| [[motorcad/parameter_database/parameters/MaxwellFileName|MaxwellFileName]] | setting | OleStr | N/A | The Maxwell filename |
| [[motorcad/parameter_database/parameters/MaxwellProject|MaxwellProject]] | setting | OleStr | N/A | The Maxwell project name |
| [[motorcad/parameter_database/parameters/MaxwellStressGraph|MaxwellStressGraph]] | setting | boolean | N/A | Drawing options for the torque graph |
| [[motorcad/parameter_database/parameters/MinimumTemperatureTolerance|MinimumTemperatureTolerance]] | i/p | double | N/A | Tolerance for allowing temperature below minimum set in model |
| [[motorcad/parameter_database/parameters/Motor_Type|Motor_Type]] | i/p | integer | N/A | 0 = BPM, 1 = IM, 2 = SRM, 3 = BPM-OR, 4 = PMDC, 5 = Not in use, 6 = SYNC, 7 = CLAW, 8 = IM1PH, 9 = SYNCREL |
| [[motorcad/parameter_database/parameters/MountingType|MountingType]] | i/p | integer | N/A | Mounting Type |
| [[motorcad/parameter_database/parameters/NodeAveragingAnimation|NodeAveragingAnimation]] | setting | integer | N/A | Whether to use the full number of force points or average over each slot/node for animation |
| [[motorcad/parameter_database/parameters/NonSteelWedgeLossModel|NonSteelWedgeLossModel]] | compatibility | integer | N/A | Calculation method for wedge losses when wedge is not a steel |
| [[motorcad/parameter_database/parameters/NumberBearingLossPoints|NumberBearingLossPoints]] | i/p | integer | N/A | This is the number of points of bearing loss data. |
| [[motorcad/parameter_database/parameters/NumberOfCuboids|NumberOfCuboids]] | i/p | integer | N/A | The number of cuboids used in cuboidal winding model |
| [[motorcad/parameter_database/parameters/OuterWindingHeight|OuterWindingHeight]] | i/p | double | mm | This is the height of the winding cuboid towards slot bottom |
| [[motorcad/parameter_database/parameters/OuterWindingWidth|OuterWindingWidth]] | i/p | double | mm | This is the width of the winding cuboid towards slot bottom |
| [[motorcad/parameter_database/parameters/PeriodsPerGraphUpdate|PeriodsPerGraphUpdate]] | i/p | integer | N/A | This is number of periods between graph updates |
| [[motorcad/parameter_database/parameters/PhasorGraphValues|PhasorGraphValues]] | setting | integer | N/A | Drawing options for the phasor graph |
| [[motorcad/parameter_database/parameters/PlacementRotationAngle_L|PlacementRotationAngle_L]] | setting | double | N/A | This is the rotation angle (degrees) of conductor columns with respect to the tooth side |
| [[motorcad/parameter_database/parameters/PlacementRotationAngle_R|PlacementRotationAngle_R]] | setting | double | N/A | This is the rotation angle (degrees) of conductor columns with respect to the tooth side |
| [[motorcad/parameter_database/parameters/PlateInterfaceAreaCalc|PlateInterfaceAreaCalc]] | compatibility | integer | N/A | Method for calculating the interface area between the plate and the endcap/housing |
| [[motorcad/parameter_database/parameters/PlotAllInductancePhases|PlotAllInductancePhases]] | i/p | boolean | N/A | When selected the inductances of all phases will be plotted |
| [[motorcad/parameter_database/parameters/PlotSmallSignalBiasCurrents|PlotSmallSignalBiasCurrents]] | i/p | boolean | N/A | When selected, bias currents used during the inductance calculation will be plotted |
| [[motorcad/parameter_database/parameters/PortunusExportScaling|PortunusExportScaling]] | i/p | double | N/A | This is the scaling factor for drawing the circuit to Portunus |
| [[motorcad/parameter_database/parameters/PositionPoints_MagnetisationCurves|PositionPoints_MagnetisationCurves]] | i/p | integer | N/A | The number of position points in the magnetisation curves calculation |
| [[motorcad/parameter_database/parameters/PottingCapacitanceCalc|PottingCapacitanceCalc]] | compatibility | integer | N/A | The capacitance calculation for the Potting using the front and rear potting mass separately |
| [[motorcad/parameter_database/parameters/RMSPhaseCurrentMethod|RMSPhaseCurrentMethod]] | compatibility | integer | N/A | The method used to calculate the RMS phase current/current density when current waveforms are not sinusoidal |
| [[motorcad/parameter_database/parameters/RadialDuctAxialLengthCalc|RadialDuctAxialLengthCalc]] | compatibility | integer | N/A | Calculation of the axial lengths with radial ducts |
| [[motorcad/parameter_database/parameters/RadialDuctMagneticLengthCalc|RadialDuctMagneticLengthCalc]] | compatibility | integer | N/A | Improved method models radial ducts magnetically by using an equivalent stacking factor, rather than reducing the magnetic axial length |
| [[motorcad/parameter_database/parameters/RadialFlowVisualisation|RadialFlowVisualisation]] | setting | boolean | N/A | When enabled can see flow arrows in radial and axial views |
| [[motorcad/parameter_database/parameters/RadialHousingSprayCoolingWithSleeve|RadialHousingSprayCoolingWithSleeve]] | compatibility | integer | N/A | Method of determining which components are cooled by Spray Cooling (Radial from Housing) with stator sleeve |
| [[motorcad/parameter_database/parameters/RadialHousing_RotationalHTCCalc|RadialHousing_RotationalHTCCalc]] | compatibility | integer | N/A | Calculation method of the rotational HTC for Spray Cooling (Radial from Housing) |
| [[motorcad/parameter_database/parameters/Radiaton_View_Factor_Editable|Radiaton_View_Factor_Editable]] | i/p | boolean | N/A | When this is true then the radiation view factors can be edited |
| [[motorcad/parameter_database/parameters/RampSteps|RampSteps]] | i/p | integer | N/A | The number of steps used for ramping the fluid temperatures to aid convergence |
| [[motorcad/parameter_database/parameters/RatioSetting_MagnetReduction|RatioSetting_MagnetReduction]] | compatibility | integer | N/A | Include magnet reduction as a ratio or independent parameter in ratio mode. |
| [[motorcad/parameter_database/parameters/RatioSetting_SleeveBanding|RatioSetting_SleeveBanding]] | compatibility | integer | N/A | Include sleeve and banding thicknesses as a ratio or independent parameter in ratio mode. |
| [[motorcad/parameter_database/parameters/RatioSetting_SyncCoilOverlap|RatioSetting_SyncCoilOverlap]] | i/p | integer | N/A | Controls whether the ratios of the SYNC salient pole are calculated with overlapping coils or without overlap. |
| [[motorcad/parameter_database/parameters/RatioSetting_SyncPoleSurfaceOffset|RatioSetting_SyncPoleSurfaceOffset]] | compatibility | integer | N/A | Controls whether the Sync pole surface offset is parent to the pole surface radius or the nodes below. |
| [[motorcad/parameter_database/parameters/RectStatorDuctSurfaceAreaCalc|RectStatorDuctSurfaceAreaCalc]] | compatibility | integer | N/A | Calculation of the surface area of rectangular ducts in the stator/housing |
| [[motorcad/parameter_database/parameters/RectangularDuctCSAMethod|RectangularDuctCSAMethod]] | compatibility | integer | N/A | Use original or improved method for rectangular duct CSA calculations |
| [[motorcad/parameter_database/parameters/RectangularWireCSA_Calc|RectangularWireCSA_Calc]] | compatibility | integer | N/A | This sets how the cross-sectional area of rectangular wire without corner rounding is calculated. |
| [[motorcad/parameter_database/parameters/ReducedCircuitState|ReducedCircuitState]] | i/p | integer | N/A | This is the State we are in with regards to using Reduced circuit or full circuit models |
| [[motorcad/parameter_database/parameters/ReducedTorquePointsPerCycle|ReducedTorquePointsPerCycle]] | o/p | integer | N/A | Number of reduced points to calculate for each cycle of torque calculation |
| [[motorcad/parameter_database/parameters/ReluctanceGraph|ReluctanceGraph]] | setting | boolean | N/A | Drawing options for the reluctance torque graph |
| [[motorcad/parameter_database/parameters/RemoveMotorCADCircuit|RemoveMotorCADCircuit]] | setting | integer | N/A | When enabled the automatic circuit created by Motor-CAD is removed allowing the user to specify the circuit to be solved |
| [[motorcad/parameter_database/parameters/RemoveMotorCADCircuit_Flow|RemoveMotorCADCircuit_Flow]] | setting | integer | N/A | When enabled the automatic flow circuit created by Motor-CAD is removed allowing the user to specify the circuit to be solved |
| [[motorcad/parameter_database/parameters/ReportWriter_Date|ReportWriter_Date]] | setting | boolean | N/A | Add the date to the title page of report |
| [[motorcad/parameter_database/parameters/ReportWriter_EMagModule|ReportWriter_EMagModule]] | setting | boolean | N/A | Create tree including E-Magnetic module |
| [[motorcad/parameter_database/parameters/ReportWriter_FullFilePath|ReportWriter_FullFilePath]] | setting | boolean | N/A | Add the file path to the title page of report |
| [[motorcad/parameter_database/parameters/ReportWriter_Graphs|ReportWriter_Graphs]] | setting | boolean | N/A | Create tree including graphs within each tab in selected modules |
| [[motorcad/parameter_database/parameters/ReportWriter_Images|ReportWriter_Images]] | setting | boolean | N/A | Create tree including Images within each tab in selected modules |
| [[motorcad/parameter_database/parameters/ReportWriter_LabModule|ReportWriter_LabModule]] | setting | boolean | N/A | Create tree including Lab module |
| [[motorcad/parameter_database/parameters/ReportWriter_MechModule|ReportWriter_MechModule]] | setting | boolean | N/A | Create tree including Mechanical module |
| [[motorcad/parameter_database/parameters/ReportWriter_Notes|ReportWriter_Notes]] | setting | boolean | N/A | Add the file path to the title page of report |
| [[motorcad/parameter_database/parameters/ReportWriter_ScreenShots|ReportWriter_ScreenShots]] | setting | boolean | N/A | Create tree including screenshot of each tab in selected modules |
| [[motorcad/parameter_database/parameters/ReportWriter_Tables|ReportWriter_Tables]] | setting | boolean | N/A | Create tree including tables within each tab in selected modules |
| [[motorcad/parameter_database/parameters/ReportWriter_ThermalModule|ReportWriter_ThermalModule]] | setting | boolean | N/A | Create tree including Thermal module |
| [[motorcad/parameter_database/parameters/ReportWriter_Time|ReportWriter_Time]] | setting | boolean | N/A | Add the date to the time of creation to title page of report |
| [[motorcad/parameter_database/parameters/RotatingBlownOverVelocityCalc|RotatingBlownOverVelocityCalc]] | compatibility | integer | N/A | Calculation method of the velocity and velocity multipliers for rotating blown over machines |
| [[motorcad/parameter_database/parameters/RotorBarEndRingCorrectionMethod|RotorBarEndRingCorrectionMethod]] | compatibility | integer | N/A | Method for calculating the end ring resistance correction factor for IM and SYNC |
| [[motorcad/parameter_database/parameters/RotorBarToLamResistanceCalc|RotorBarToLamResistanceCalc]] | compatibility | integer | N/A | Method for calculating the thermal resistance between the rotor lamination and IM's rotor bars or SYNC's field winding. |
| [[motorcad/parameter_database/parameters/RotorCageLossSplit|RotorCageLossSplit]] | recommended | integer | N/A | This option specifies how the rotor cage losses are split between the rotor bars and endrings |
| [[motorcad/parameter_database/parameters/RotorCopperAreaMethod|RotorCopperAreaMethod]] | compatibility | integer | N/A | Method for calculating cross-sectional area of rotor copper for the electromagnetic loss calculations |
| [[motorcad/parameter_database/parameters/RotorCopperLossesVaryWithTemp|RotorCopperLossesVaryWithTemp]] | i/p | boolean | N/A | When selected the rotor copper losses vary with temperature |
| [[motorcad/parameter_database/parameters/RotorCopperStrayLoadLossesVaryWithTemp|RotorCopperStrayLoadLossesVaryWithTemp]] | i/p | boolean | N/A | When selected the Rotor Copper stray load losses vary with temperature |
| [[motorcad/parameter_database/parameters/RotorCopperStrayLoadTempAtWhichLossInput|RotorCopperStrayLoadTempAtWhichLossInput]] | i/p | double | °C | The temperature at which the Rotor Copper stray load losses are input |
| [[motorcad/parameter_database/parameters/RotorEWdg_Roughness_F|RotorEWdg_Roughness_F]] | i/p | double | N/A | The rotor endwinding roughness factor |
| [[motorcad/parameter_database/parameters/RotorEWdg_Roughness_R|RotorEWdg_Roughness_R]] | i/p | double | N/A | The rotor endwinding roughness factor |
| [[motorcad/parameter_database/parameters/RotorForceNodes_PerBar|RotorForceNodes_PerBar]] | i/p | integer | N/A | The number of force nodes per rotor bar for force calculations. |
| [[motorcad/parameter_database/parameters/RotorForceNodes_PerPole|RotorForceNodes_PerPole]] | i/p | integer | N/A | The number of force nodes per rotor pole for force calculations. |
| [[motorcad/parameter_database/parameters/RotorIronStrayLoadLossesVaryWithTemp|RotorIronStrayLoadLossesVaryWithTemp]] | i/p | boolean | N/A | When selected the Rotor iron stray load losses vary with temperature |
| [[motorcad/parameter_database/parameters/RotorIronStrayLoadTempAtWhichLossInput|RotorIronStrayLoadTempAtWhichLossInput]] | i/p | double | °C | The temperature at which the Rotor iron stray load losses are input |
| [[motorcad/parameter_database/parameters/RotorRotation|RotorRotation]] | i/p | double | N/A | The rotor rotation in mechanical degrees radial cross section view |
| [[motorcad/parameter_database/parameters/RotorThermalCircuit|RotorThermalCircuit]] | recommended | integer | N/A | Use of the Original or Improved (Experimental) rotor thermal circuit for Interior U-shape BPM/SYNCREL machines |
| [[motorcad/parameter_database/parameters/RotorWJArcDuctWidthCalculation|RotorWJArcDuctWidthCalculation]] | compatibility | integer | N/A | Method used to calculate the average width of all arc ducts used with Rotor Water Jacket cooling. |
| [[motorcad/parameter_database/parameters/RotorWJCentralInletCalc|RotorWJCentralInletCalc]] | compatibility | integer | N/A | The calculation method of the central RotorWJ inlet to fluid node thermal resistance |
| [[motorcad/parameter_database/parameters/RotorWJChannelNumberCalc|RotorWJChannelNumberCalc]] | compatibility | integer | N/A | To not include channels with ducts that have zero surface area in the channel number calculation for the RotorWJ. |
| [[motorcad/parameter_database/parameters/RotorWJHeatTransferCalc|RotorWJHeatTransferCalc]] | compatibility | integer | N/A | Calculation method for heat transfer coefficients using Rotor Water Jacket |
| [[motorcad/parameter_database/parameters/RotorWJNodeConnection_Method|RotorWJNodeConnection_Method]] | compatibility | integer | N/A | Method for connecting Rotor Water Jacket to rotor/shaft |
| [[motorcad/parameter_database/parameters/RotorWJ_SprayCooling_Connection|RotorWJ_SprayCooling_Connection]] | i/p | boolean | N/A | When selected the rotor water jacket outlet is connected to the spray cooling inlet |
| [[motorcad/parameter_database/parameters/Rotor_Mounting|Rotor_Mounting]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/Rotor_Water_Jacket|Rotor_Water_Jacket]] | i/p | boolean | N/A | Use rotor ducts for rotor liquid cooling (can set properies of fluid to air) |
| [[motorcad/parameter_database/parameters/RtAirgapSlicesCalc|RtAirgapSlicesCalc]] | compatibility | integer | N/A | Calculation method for the airgap resistance during a transient with axial slices and no airgap flow |
| [[motorcad/parameter_database/parameters/RtHousing_A_RadialCalc|RtHousing_A_RadialCalc]] | compatibility | integer | N/A | Thermal resistance calculation method for Back iron to housing path |
| [[motorcad/parameter_database/parameters/RtHousing_OHang_AxialCalc|RtHousing_OHang_AxialCalc]] | compatibility | integer | N/A | Thermal resistance calculation method for Housing Overhang front and rear axial paths. |
| [[motorcad/parameter_database/parameters/RtImpregSingleConductorColumnCalc|RtImpregSingleConductorColumnCalc]] | compatibility | integer | N/A | Calculation method for Tooth Side Impreg Resistance when all conductors are in a single column |
| [[motorcad/parameter_database/parameters/RtRotorAxialCalc|RtRotorAxialCalc]] | compatibility | integer | N/A | Method used for calculating rotor axial resistances including magnet-magnet interface gap |
| [[motorcad/parameter_database/parameters/SCPhaseCurrentMethod|SCPhaseCurrentMethod]] | compatibility | integer | N/A | The method used to calculate the initial phase currents for the short circuit calculation |
| [[motorcad/parameter_database/parameters/SRM_Fault_Type|SRM_Fault_Type]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/SecondSetConductors|SecondSetConductors]] | setting | integer | N/A | Number of conductors in the second set |
| [[motorcad/parameter_database/parameters/Sensitivity_ExportMatrices|Sensitivity_ExportMatrices]] | setting | boolean | N/A | When selected the thermal matrices from sensitivity analysis are exported to files in the results folder |
| [[motorcad/parameter_database/parameters/ShaftAxialResistanceCalc|ShaftAxialResistanceCalc]] | compatibility | integer | N/A | Calculation method of the shaft active axial thermal resistance |
| [[motorcad/parameter_database/parameters/ShaftRearWeightCalc|ShaftRearWeightCalc]] | compatibility | integer | N/A | Calculation method of the weight of the shaft rear with a rear shaft extension |
| [[motorcad/parameter_database/parameters/ShaftSG_RotorWJ_Connection|ShaftSG_RotorWJ_Connection]] | i/p | boolean | N/A | When selected the shaft spiral groove outlet is connected to the rotor water jacket inlet |
| [[motorcad/parameter_database/parameters/ShaftSG_SlotWJ_Connection|ShaftSG_SlotWJ_Connection]] | i/p | boolean | N/A | When selected the shaft spiral groove outlet is connected to the slot water jacket inlet |
| [[motorcad/parameter_database/parameters/ShaftSolve|ShaftSolve]] | recommended | integer | N/A | Control whether the shaft is include in the EMag FEA model |
| [[motorcad/parameter_database/parameters/ShaftSpiralGrooveDimensionsCalc|ShaftSpiralGrooveDimensionsCalc]] | compatibility | integer | N/A | Calculation of the Shaft Spiral Groove dimensions and area multipliers |
| [[motorcad/parameter_database/parameters/ShaftSpiralGrooveFrictionCalc|ShaftSpiralGrooveFrictionCalc]] | compatibility | integer | N/A | Whether the Area Adjustment and Velocity Multiplier are used to calculate the friction factor |
| [[motorcad/parameter_database/parameters/ShaftSpiralGrooveHTCCalc|ShaftSpiralGrooveHTCCalc]] | compatibility | integer | N/A | This determines whether to use the original or improved Shaft Spiral Groove heat transfer coefficient calculation |
| [[motorcad/parameter_database/parameters/ShaftSpiralGrooveSprayCoolingCalc|ShaftSpiralGrooveSprayCoolingCalc]] | compatibility | integer | N/A | Calculation of the Shaft Spiral Groove fluid temperature when coupled to Spray Cooling |
| [[motorcad/parameter_database/parameters/ShaftTorqueCalculationMethod|ShaftTorqueCalculationMethod]] | compatibility | integer | N/A | How shaft torque is calculated from FEA torque and losses |
| [[motorcad/parameter_database/parameters/Shaft_Spiral_Groove|Shaft_Spiral_Groove]] | i/p | boolean | N/A | Use shaft spiral groove for liquid cooling of rotor |
| [[motorcad/parameter_database/parameters/ShowAllMMFPlots|ShowAllMMFPlots]] | setting | boolean | N/A | Display the MMF distribution for each phase on a single plot |
| [[motorcad/parameter_database/parameters/ShowDQCurrents|ShowDQCurrents]] | setting | boolean | N/A | Display the DQ axis currents on the currents graph |
| [[motorcad/parameter_database/parameters/ShowMMFSumPlot|ShowMMFSumPlot]] | setting | boolean | N/A | Display the summation of the MMF distribution |
| [[motorcad/parameter_database/parameters/ShowWatermarks|ShowWatermarks]] | setting | boolean | N/A | When enabled the Motor-CAD watermarks are visible in the editors |
| [[motorcad/parameter_database/parameters/SingleEmissivityCalc|SingleEmissivityCalc]] | compatibility | integer | N/A | The radiation resistance calculation method with single emissivity value enabled |
| [[motorcad/parameter_database/parameters/SkewDefinition|SkewDefinition]] | i/p | integer | N/A | Select the skew method used |
| [[motorcad/parameter_database/parameters/Sleeve2D3DFactorCalc|Sleeve2D3DFactorCalc]] | compatibility | integer | N/A | This determines the method for calculating the 2D to 3D factor for the stator sleeve losses |
| [[motorcad/parameter_database/parameters/SleeveLengthCalc|SleeveLengthCalc]] | compatibility | integer | N/A | Method for determining sleeve axial length used to calculate sleeve losses |
| [[motorcad/parameter_database/parameters/SlotDividerLinerDrawingMethod|SlotDividerLinerDrawingMethod]] | compatibility | integer | N/A | Method used for drawing the slot liner where it meets the coil divider for parallel tooth and tapered slot types |
| [[motorcad/parameter_database/parameters/SlotLeakageInductanceMethod_Rotor|SlotLeakageInductanceMethod_Rotor]] | compatibility | integer | N/A | Method of calculating rotor slot leakage inductance |
| [[motorcad/parameter_database/parameters/SlotLeakageInductanceMethod_Stator|SlotLeakageInductanceMethod_Stator]] | compatibility | integer | N/A | Method of calculating stator slot leakage inductance |
| [[motorcad/parameter_database/parameters/SlotOpeningWidthSetting|SlotOpeningWidthSetting]] | compatibility | integer | N/A | The definition used to define the slot opening width |
| [[motorcad/parameter_database/parameters/SlotType|SlotType]] | i/p | integer | N/A | Slot shape (parallel tooth, parallel tooth square base, parallel slot or slotless) |
| [[motorcad/parameter_database/parameters/SlotWJAxialLengthCalc|SlotWJAxialLengthCalc]] | compatibility | integer | N/A | Calculation method of the axial length of Slot Water Jacket ducts for PMDC/WFC machines |
| [[motorcad/parameter_database/parameters/SlotWJCentreDuctsFlowRtCalc|SlotWJCentreDuctsFlowRtCalc]] | compatibility | integer | N/A | Calculation method of the flow resistance for Slot Water Jacket Flow in Slot Centre Ducts |
| [[motorcad/parameter_database/parameters/SlotWJCircuit|SlotWJCircuit]] | compatibility | integer | N/A | Whether to use the original or improved Slot WJ circuit |
| [[motorcad/parameter_database/parameters/SlotWJDuctDrawingMethod|SlotWJDuctDrawingMethod]] | compatibility | integer | N/A | Method used for drawing the Slot WJ duct opening and calculating duct width, area |
| [[motorcad/parameter_database/parameters/SlotWJDuctkWallFrictionCalc|SlotWJDuctkWallFrictionCalc]] | compatibility | integer | N/A | Method of calculating Slot WJ k value for Duct Wall Friction |
| [[motorcad/parameter_database/parameters/SlotWJHTCCalc|SlotWJHTCCalc]] | compatibility | integer | N/A | Method of calculating heat transfer coefficients for Slot WJ |
| [[motorcad/parameter_database/parameters/SlotWJSeparateDuctsRtCalc|SlotWJSeparateDuctsRtCalc]] | compatibility | integer | N/A | Calculation of the thermal resistance distribution per cuboid for separate slot water jacket cooling ducts |
| [[motorcad/parameter_database/parameters/SlotWJWallRoughnessHTCCalc|SlotWJWallRoughnessHTCCalc]] | compatibility | integer | N/A | Method of calculations heat transfer coefficients for Slot WJ with duct wall roughness and flow between conductors |
| [[motorcad/parameter_database/parameters/SlotWJ_HousingWJ_Connection|SlotWJ_HousingWJ_Connection]] | i/p | boolean | N/A | When selected the slot water jacket outlet is connected to the housing water jacket inlet |
| [[motorcad/parameter_database/parameters/Slot_Area_Calculation|Slot_Area_Calculation]] | compatibility | integer | N/A | Method of calculating slot and winding areas. |
| [[motorcad/parameter_database/parameters/Slot_Water_Jacket|Slot_Water_Jacket]] | i/p | boolean | N/A | Use slot ducts for liquid cooling (can set properies of fluid to air) |
| [[motorcad/parameter_database/parameters/Slotless_FormWound_DimensionsCalc|Slotless_FormWound_DimensionsCalc]] | compatibility | integer | N/A | The calculation method of the Slotless and Form Wound slot dimensions |
| [[motorcad/parameter_database/parameters/SpaceTimeContours|SpaceTimeContours]] | setting | integer | N/A | Select whether the space time forces plot contours are visible |
| [[motorcad/parameter_database/parameters/SpaceTimeForceFFTType|SpaceTimeForceFFTType]] | setting | integer | N/A | Select the FFT type used for harmonic force analysis in the user interface |
| [[motorcad/parameter_database/parameters/SpaceTimeForceSlice|SpaceTimeForceSlice]] | setting | integer | N/A | Select the slice shown in Space Time chart shown in user interface |
| [[motorcad/parameter_database/parameters/SpaceTimeHarmonicsForceSlice|SpaceTimeHarmonicsForceSlice]] | setting | integer | N/A | Select the slice shown in Space Time Harmonics chart shown in user interface |
| [[motorcad/parameter_database/parameters/SpatialForceHarmonic_TimeStep|SpatialForceHarmonic_TimeStep]] | setting | integer | N/A | The rotation step index used in force harmonic analysis |
| [[motorcad/parameter_database/parameters/SpeedDesignType|SpeedDesignType]] | i/p | integer | N/A | This is the SPEED calculation used for importing losses |
| [[motorcad/parameter_database/parameters/SpeedFileName|SpeedFileName]] | setting | OleStr | N/A | The SPEED filename |
| [[motorcad/parameter_database/parameters/SprayCoolingCircuit|SprayCoolingCircuit]] | compatibility | integer | N/A | This allows the spray cooling circuit to be changed |
| [[motorcad/parameter_database/parameters/SprayCoolingCorrelation|SprayCoolingCorrelation]] | i/p | integer | N/A | Specifies the correlation used to determine the spray cooling heat transfer coefficient |
| [[motorcad/parameter_database/parameters/SprayCoolingCoverageCalc|SprayCoolingCoverageCalc]] | compatibility | integer | N/A | Calculation of the coverage area used to determine the spray cooling heat transfer coefficient |
| [[motorcad/parameter_database/parameters/SprayCoolingHairpinFrontRInternalFlowCalc|SprayCoolingHairpinFrontRInternalFlowCalc]] | compatibility | integer | N/A | Calculation method of the spray cooling internal flow for the EW Front [Rear] |
| [[motorcad/parameter_database/parameters/SprayCoolingHousingWJCouplingCalc|SprayCoolingHousingWJCouplingCalc]] | compatibility | integer | N/A | The method used for selecting which HousingWJ fluid node to couple the spray cooling to when using user-defined nozzles |
| [[motorcad/parameter_database/parameters/SprayCoolingNozzleDefinition|SprayCoolingNozzleDefinition]] | i/p | integer | N/A | The nozzle definition used for Spray Cooling |
| [[motorcad/parameter_database/parameters/SprayCoolingRotorTargetLengthCalc|SprayCoolingRotorTargetLengthCalc]] | compatibility | integer | N/A | Calculation method of the spray cooling target length for the rotor pole of IPM machines |
| [[motorcad/parameter_database/parameters/SprayCoolingSubmerged|SprayCoolingSubmerged]] | compatibility | integer | N/A | Specifies the calculation method used for Submerged Jet Spray Cooling |
| [[motorcad/parameter_database/parameters/SprayCoolingSyncEWdgCalc|SprayCoolingSyncEWdgCalc]] | compatibility | integer | N/A | Calculation of the spray cooling area of the SYNC rotor pole |
| [[motorcad/parameter_database/parameters/Spray_Cooling|Spray_Cooling]] | i/p | boolean | N/A | Use spray cooling of end windings for cooling of internal sections of motor |
| [[motorcad/parameter_database/parameters/SquareWaveInductanceCalc|SquareWaveInductanceCalc]] | setting | integer | N/A | Specify whether to use average or varying inductance for current calculation |
| [[motorcad/parameter_database/parameters/StackingFactorIronLossMethod|StackingFactorIronLossMethod]] | compatibility | integer | N/A | Method for accounting for stacking factor in iron loss calculations. |
| [[motorcad/parameter_database/parameters/Stall_Copper_Loss_Dist|Stall_Copper_Loss_Dist]] | i/p | integer | N/A | 0 = All_Equal,    1 = Two_Phase_On,   2 = Sine_Dist_A_Max, 3 = Custom_Stall_Dist |
| [[motorcad/parameter_database/parameters/StatorBackIronUnevenLossAddition|StatorBackIronUnevenLossAddition]] | compatibility | integer | N/A | This defines the schematic addition to the stator back iron loss, for transient calculations with uneven copper loss distribution. |
| [[motorcad/parameter_database/parameters/StatorConductivityModel|StatorConductivityModel]] | i/p | integer | N/A | This is the stator conductivity model to be used |
| [[motorcad/parameter_database/parameters/StatorCopperLossSplit|StatorCopperLossSplit]] | recommended | integer | N/A | This option specifies how the stator copper losses are split between the active section and endwindings |
| [[motorcad/parameter_database/parameters/StatorCopperLossVariation|StatorCopperLossVariation]] | recommended | integer | N/A | Variation of stator copper losses with temperature, using either the average winding temperature or the local winding temperatures |
| [[motorcad/parameter_database/parameters/StatorCopperStrayLoadLossesVaryWithTemp|StatorCopperStrayLoadLossesVaryWithTemp]] | i/p | boolean | N/A | When selected the stator Copper stray load losses vary with temperature |
| [[motorcad/parameter_database/parameters/StatorCopperStrayLoadTempAtWhichLossInput|StatorCopperStrayLoadTempAtWhichLossInput]] | i/p | double | °C | The temperature at which the stator Copper stray load losses are input |
| [[motorcad/parameter_database/parameters/StatorForceNodes_PerTooth|StatorForceNodes_PerTooth]] | i/p | integer | N/A | The number of force nodes per stator tooth for force calculations. |
| [[motorcad/parameter_database/parameters/StatorIronStrayLoadLossesVaryWithTemp|StatorIronStrayLoadLossesVaryWithTemp]] | i/p | boolean | N/A | When selected the stator iron stray load losses vary with temperature |
| [[motorcad/parameter_database/parameters/StatorIronStrayLoadTempAtWhichLossInput|StatorIronStrayLoadTempAtWhichLossInput]] | i/p | double | °C | The temperature at which the stator iron stray load losses are input |
| [[motorcad/parameter_database/parameters/StatorLamWeightCalc|StatorLamWeightCalc]] | compatibility | integer | N/A | Calculation method of the weight of the stator lamination with no housing |
| [[motorcad/parameter_database/parameters/StatorLeakageInductanceMethod|StatorLeakageInductanceMethod]] | compatibility | integer | N/A | Method of calculating stator leakage inductance (FEA) |
| [[motorcad/parameter_database/parameters/StatorRotation|StatorRotation]] | i/p | double | N/A | The stator rotation in mechanical degrees radial cross section view |
| [[motorcad/parameter_database/parameters/StatorToothLossDistribution|StatorToothLossDistribution]] | compatibility | integer | N/A | This defines how the stator tooth losses are distributed between cuboids and axial slices. Applicable to uneven copper loss distribution, 0 speed or a transient fault |
| [[motorcad/parameter_database/parameters/StatorToothRtMethod|StatorToothRtMethod]] | compatibility | integer | N/A | Calculation method used for stator tooth thermal resistance |
| [[motorcad/parameter_database/parameters/SteadyAveragingMethod|SteadyAveragingMethod]] | i/p | integer | N/A | The method of averaging steady state results |
| [[motorcad/parameter_database/parameters/SteadyStateAveraging|SteadyStateAveraging]] | compatibility | integer | N/A | This is the method for calculating the steady state average value |
| [[motorcad/parameter_database/parameters/SteadyStateConvergenceMethod|SteadyStateConvergenceMethod]] | i/p | integer | °C | This is the method used for thermal steady state convergence |
| [[motorcad/parameter_database/parameters/SteadyStateMinIterations|SteadyStateMinIterations]] | i/p | integer | N/A | This is the minimum number of thermal steady state iterations to run |
| [[motorcad/parameter_database/parameters/SteadyStatorPowerFlowErrorSum|SteadyStatorPowerFlowErrorSum]] | o/p | double | Watts | The sum of the power flow errors |
| [[motorcad/parameter_database/parameters/Steady_State_Max_Convergence_Error_dT|Steady_State_Max_Convergence_Error_dT]] | i/p | double | °C | This is the maximum thermal steady state convergence error to allow for convergence |
| [[motorcad/parameter_database/parameters/Steady_State_Max_Iterations|Steady_State_Max_Iterations]] | i/p | integer | N/A | This is the maximum number of thermal steady state iterations to run |
| [[motorcad/parameter_database/parameters/StrayLoadLossCalculationType|StrayLoadLossCalculationType]] | recommended | integer | N/A | Method used to calculate stray load losses |
| [[motorcad/parameter_database/parameters/SurfaceBreadloafAreaCalc|SurfaceBreadloafAreaCalc]] | compatibility | integer | N/A | Calculation method to use for Surface Breadloaf magnet and rotor lamination areas |
| [[motorcad/parameter_database/parameters/SurroundingAirRegion_Boundary|SurroundingAirRegion_Boundary]] | setting | integer | N/A | Controls the surrounding air region boundary |
| [[motorcad/parameter_database/parameters/SurroundingAirRegion_CircleDiameter|SurroundingAirRegion_CircleDiameter]] | i/p | double | mm | Controls the surrounding air region circle diameter |
| [[motorcad/parameter_database/parameters/SyncFieldWdgAreasCalc|SyncFieldWdgAreasCalc]] | compatibility | integer | N/A | Compatibility for Sync field winding area used for thermal conducitivty calculation |
| [[motorcad/parameter_database/parameters/SyncLinerAreaCalculation|SyncLinerAreaCalculation]] | compatibility | integer | N/A | Method to use for the sync rotor liner area calculation. |
| [[motorcad/parameter_database/parameters/SyncLinerAreaWeightCalculations|SyncLinerAreaWeightCalculations]] | compatibility | integer | N/A | Method of calculating area and weight of sync rotor liner. |
| [[motorcad/parameter_database/parameters/SyncMotorStressCalc|SyncMotorStressCalc]] | compatibility | integer | N/A | When enabled the field liner will be separated from the rotor pole regions |
| [[motorcad/parameter_database/parameters/SyncPoleSurfaceOffsetBetaParameterisation|SyncPoleSurfaceOffsetBetaParameterisation]] | i/p | integer | N/A | Controls whether the pole surface offset is a ratio or absolute parameter for SYNC ratios with beta rotor parameterisation. Absolute offset defines pole tip side instead of pole tip depth. |
| [[motorcad/parameter_database/parameters/SyncRatioMaxShaftDiameter|SyncRatioMaxShaftDiameter]] | compatibility | integer | N/A | Whether surface offset is included in the max shaft diameter |
| [[motorcad/parameter_database/parameters/SyncRotorCircuit|SyncRotorCircuit]] | compatibility | integer | N/A | Whether to use the old or improved Sync rotor circuit. |
| [[motorcad/parameter_database/parameters/SyncRotorCuboidAreaMult|SyncRotorCuboidAreaMult]] | compatibility | integer | N/A | Method used to calculate winding area for Sync rotor cuboidal k values. Compatibility for Sync models made before v11.2.4 |
| [[motorcad/parameter_database/parameters/SyncRotorCuboidEWdgLengthCalc|SyncRotorCuboidEWdgLengthCalc]] | compatibility | integer | N/A | Calculation of the sync rotor endwinding length for the cuboidal model |
| [[motorcad/parameter_database/parameters/SyncRotorCuboidHalfSlotMult|SyncRotorCuboidHalfSlotMult]] | compatibility | integer | N/A | Method used to calculate the Sync rotor cuboid resistances from the k values. Compatibility for models created before v12.1.7 |
| [[motorcad/parameter_database/parameters/SyncRotorCuboidalWindingModel|SyncRotorCuboidalWindingModel]] | compatibility | integer | N/A | Method to use when calculating the Sync rotor cuboidal k values |
| [[motorcad/parameter_database/parameters/SyncRotorEWdgMLTCalc|SyncRotorEWdgMLTCalc]] | compatibility | integer | N/A | Calculation of the sync rotor endwinding MLT |
| [[motorcad/parameter_database/parameters/SyncRotorVolumeCalc|SyncRotorVolumeCalc]] | compatibility | integer | N/A | Compatibility for Sync Rotor Volume calculation |
| [[motorcad/parameter_database/parameters/SyncRotorWindingTempCalc|SyncRotorWindingTempCalc]] | compatibility | integer | N/A | This determines whether to use the old or improved method of averaging the sync rotor winding temperature. |
| [[motorcad/parameter_database/parameters/SyncRotorWindingTempCoupling|SyncRotorWindingTempCoupling]] | compatibility | integer | N/A | This determines whether to set the rotor winding temperature at which losses were calculated from Emag-Therm coupling. |
| [[motorcad/parameter_database/parameters/SyncWindingHeight|SyncWindingHeight]] | i/p | double | mm | This is the height of the winding cuboid |
| [[motorcad/parameter_database/parameters/SyncWindingSize|SyncWindingSize]] | i/p | integer | N/A | This sets how the cuboidal model sizes are defined. |
| [[motorcad/parameter_database/parameters/SyncWindingWidth|SyncWindingWidth]] | i/p | double | mm | This is the width of the winding cuboid |
| [[motorcad/parameter_database/parameters/Sync_Parallel_Tooth_Radial_Depth|Sync_Parallel_Tooth_Radial_Depth]] | compatibility | integer | N/A | Method of implementation for radial depth of sync parallel tooth rotors |
| [[motorcad/parameter_database/parameters/Sync_Rotor_Parameterisation|Sync_Rotor_Parameterisation]] | compatibility | integer | N/A | Implementation of ratio mode for sync rotors |
| [[motorcad/parameter_database/parameters/TVentBiDirectionDuctFlowRtCalc|TVentBiDirectionDuctFlowRtCalc]] | compatibility | integer | N/A | Calculation method of the stator duct flow resistance with Bi-Directional TVent Flow |
| [[motorcad/parameter_database/parameters/TVentBiDirectionFlowCircuitCalc|TVentBiDirectionFlowCircuitCalc]] | compatibility | integer | N/A | Calculation method of the Bi-Directional TVent flow circuit |
| [[motorcad/parameter_database/parameters/TVentCirculatingAirgapFlowPath|TVentCirculatingAirgapFlowPath]] | compatibility | integer | N/A | Calculation method of the TVent airgap contraction flow path with circulating flow |
| [[motorcad/parameter_database/parameters/TVentCoupledFluidResistanceCalc|TVentCoupledFluidResistanceCalc]] | compatibility | integer | N/A | Calculation of fluid node to fluid node thermal resistances used for through ventilated cooling with BiDirectional/Front Inlet-Circulating flow or when coupled to slot wj |
| [[motorcad/parameter_database/parameters/TVentEWdgOuterVelocityCalc|TVentEWdgOuterVelocityCalc]] | compatibility | integer | N/A | The calculation of the Flow Velocity around the Endwinding Outer |
| [[motorcad/parameter_database/parameters/TVentRadialDuctResistanceCalc|TVentRadialDuctResistanceCalc]] | compatibility | integer | N/A | Calculation of fluid node to fluid node thermal resistances used for through ventilated radial duct cooling |
| [[motorcad/parameter_database/parameters/TVentRotorDuctFlowCalc|TVentRotorDuctFlowCalc]] | compatibility | integer | N/A | Calculation method of the Through Ventilated rotor duct velocity |
| [[motorcad/parameter_database/parameters/TVentShaftCooling|TVentShaftCooling]] | i/p | integer | N/A | The location TVent shaft cooling path |
| [[motorcad/parameter_database/parameters/TVentSyncSalientPoleFlowAreaCalc|TVentSyncSalientPoleFlowAreaCalc]] | compatibility | integer | N/A | Calculation method of the flow area between Sync Salient Poles for Ventilated machines |
| [[motorcad/parameter_database/parameters/TVent_FrontRear_OutletFlowPath|TVent_FrontRear_OutletFlowPath]] | compatibility | integer | N/A | Calculation method of the Through Ventilated flow path with front/rear inlet flow direction |
| [[motorcad/parameter_database/parameters/TVent_HousingWJ_Connection|TVent_HousingWJ_Connection]] | i/p | boolean | N/A | When selected the TVent outlet is connected to the Housing WJ inlet |
| [[motorcad/parameter_database/parameters/TVent_PMDC_WFC_Calculation|TVent_PMDC_WFC_Calculation]] | compatibility | integer | N/A | Calculation of Endwinding gaps for TVent cooling for PMDC and WFC machines |
| [[motorcad/parameter_database/parameters/TVent_RotorSurfaceArea_CalcMethod|TVent_RotorSurfaceArea_CalcMethod]] | compatibility | integer | N/A | Improved method calculates the rotor surface area using the rotor lamination length rather than the embedded magnet length. |
| [[motorcad/parameter_database/parameters/TVent_SlotWJ_Connection|TVent_SlotWJ_Connection]] | i/p | boolean | N/A | When selected the TVent airgap and slot water jacket paths are in parallel |
| [[motorcad/parameter_database/parameters/TVent_SlotWJ_Connection_Method|TVent_SlotWJ_Connection_Method]] | compatibility | integer | N/A | Calculation method used when TVent_SlotWJ connection is enabled without a Slot WJ |
| [[motorcad/parameter_database/parameters/TemporalForceHarmonic_Node|TemporalForceHarmonic_Node]] | setting | integer | N/A | The force node index used in force harmonic analysis |
| [[motorcad/parameter_database/parameters/TerminalGraphValues|TerminalGraphValues]] | setting | integer | N/A | Drawing options for the Terminal Voltage graphs |
| [[motorcad/parameter_database/parameters/ThermalPowerFlowCalc|ThermalPowerFlowCalc]] | compatibility | integer | N/A | Calculation method of the thermal power flow in models with zero resistances |
| [[motorcad/parameter_database/parameters/ThroughVentilation|ThroughVentilation]] | i/p | boolean | N/A | Ventilation using fluid flowing through machine |
| [[motorcad/parameter_database/parameters/ToothAxialRtCalc|ToothAxialRtCalc]] | compatibility | integer | N/A | The calculation method of the tooth node axial resistances |
| [[motorcad/parameter_database/parameters/ToothCapacitanceSlicesCalc|ToothCapacitanceSlicesCalc]] | compatibility | integer | N/A | The calculation method of the tooth node capacitances with multiple axial slices |
| [[motorcad/parameter_database/parameters/TorqueCharacteristicPlotSelect|TorqueCharacteristicPlotSelect]] | i/p | integer | N/A | The torque characteristic graph to view |
| [[motorcad/parameter_database/parameters/TorqueGraphScale|TorqueGraphScale]] | setting | integer | N/A | Select the y axis scale of torque graph |
| [[motorcad/parameter_database/parameters/TorqueHarmonicGraph_BaseType|TorqueHarmonicGraph_BaseType]] | setting | integer | N/A | Base frequency of torque harmonic graph (Electrical/Mechanical) |
| [[motorcad/parameter_database/parameters/TorqueNumberCycles|TorqueNumberCycles]] | i/p | double | N/A | Number cycles to perform for torque calculation |
| [[motorcad/parameter_database/parameters/TorquePointsPerCycle|TorquePointsPerCycle]] | i/p | integer | N/A | Number of points to calculate for each cycle of torque calculation |
| [[motorcad/parameter_database/parameters/TorqueSpeedCalcs|TorqueSpeedCalcs]] | i/p | integer | N/A | The number of FEA calculations to run at different phase advances |
| [[motorcad/parameter_database/parameters/TorqueSpeedGraph|TorqueSpeedGraph]] | i/p | integer | N/A | The torque/speed graph to view |
| [[motorcad/parameter_database/parameters/TorqueSpeedPhaseAdv_Lower|TorqueSpeedPhaseAdv_Lower]] | i/p | double | N/A | Lower phase advance limit for torque/speed graph |
| [[motorcad/parameter_database/parameters/TorqueSpeedPhaseAdv_Upper|TorqueSpeedPhaseAdv_Upper]] | i/p | double | N/A | Upper phase advance limit for torque/speed graph |
| [[motorcad/parameter_database/parameters/TotalConductors|TotalConductors]] | o/p | integer | N/A | Total Number Of Conductors |
| [[motorcad/parameter_database/parameters/TotalCuboidArea|TotalCuboidArea]] | o/p | double | mm² | Area of all the cuboids combined |
| [[motorcad/parameter_database/parameters/TotalInsulationLifetime|TotalInsulationLifetime]] | o/p | double | sec | This is the estimated lifetime of the insulation system. |
| [[motorcad/parameter_database/parameters/TotalLossCalculationMethod|TotalLossCalculationMethod]] | compatibility | integer | N/A | Include wedge loss in total loss |
| [[motorcad/parameter_database/parameters/TransientDataLogging|TransientDataLogging]] | setting | boolean | N/A | When set then additional model parameters can be saved to file during a transient analysis. |
| [[motorcad/parameter_database/parameters/TransientErrorWeighting|TransientErrorWeighting]] | i/p | double | N/A | Error weighting setting for Transient |
| [[motorcad/parameter_database/parameters/TransientErrorWeightingMethod|TransientErrorWeightingMethod]] | compatibility | integer | N/A | Method used when calculating the error weighting in the thermal transient solver |
| [[motorcad/parameter_database/parameters/TransientGraphColours|TransientGraphColours]] | setting | integer | N/A | Allows selection of colour of thermal plots |
| [[motorcad/parameter_database/parameters/TransientGraphUpdateDisabled|TransientGraphUpdateDisabled]] | i/p | boolean | N/A | When set to 1 then transient graphs are no longer drawn. This has to be set to 0 before last transient run during append run to show full transient results graph. |
| [[motorcad/parameter_database/parameters/TransientIterationsExceeded|TransientIterationsExceeded]] | o/p | boolean | N/A | When true the transient calculation has continued although a step has not solved correctly |
| [[motorcad/parameter_database/parameters/TransientMaxIterations|TransientMaxIterations]] | i/p | double | N/A | The maximum number of iteration for Transient before current timestep calculation is stopped |
| [[motorcad/parameter_database/parameters/TransientMinCapMethod|TransientMinCapMethod]] | compatibility | integer | N/A | Calculation method when using a user-defined minimum capacitance value for the transient DAE solver. |
| [[motorcad/parameter_database/parameters/TransientMinimumCapacitance|TransientMinimumCapacitance]] | setting | double | J/°C | This is minimum capacitance used inside the DAE transient solver |
| [[motorcad/parameter_database/parameters/TransientMinimumCapacitanceEnabled|TransientMinimumCapacitanceEnabled]] | setting | integer | N/A | Whether to force a minimum capacitance inside DAE transient solver |
| [[motorcad/parameter_database/parameters/TransientPointsToPlot|TransientPointsToPlot]] | i/p | integer | N/A | When used will only plot every N points in transient |
| [[motorcad/parameter_database/parameters/TransientPowerInjectionCalc|TransientPowerInjectionCalc]] | compatibility | integer | N/A | Method used to apply the power injection from external components in transient calculations |
| [[motorcad/parameter_database/parameters/TransientRelativeError|TransientRelativeError]] | i/p | double | N/A | Relative error setting for Transient |
| [[motorcad/parameter_database/parameters/TransientTempOffset|TransientTempOffset]] | setting | double | °C | Temperature offset used to avoid convergence issues around 0C. |
| [[motorcad/parameter_database/parameters/URotorAreaSpokeSpiderCalc|URotorAreaSpokeSpiderCalc]] | compatibility | integer | N/A | Calculation method of the rotor area for U-shaped rotors with spider shaft and spoke ducts |
| [[motorcad/parameter_database/parameters/URotorMagnetPoleCentreCalc|URotorMagnetPoleCentreCalc]] | compatibility | integer | N/A | Calculation method of the magnet pole centre for U-shaped rotor resistance calculations |
| [[motorcad/parameter_database/parameters/URotorMagnetPoleInnerRadiusCalc|URotorMagnetPoleInnerRadiusCalc]] | compatibility | integer | N/A | Calculation method of the magnet pole inner radius for U-shaped rotor thermal calculations |
| [[motorcad/parameter_database/parameters/URotorPocketCondCalc|URotorPocketCondCalc]] | compatibility | integer | N/A | The calculation method of the pocket conductivity for U-shaped rotors |
| [[motorcad/parameter_database/parameters/URotorRadialDuctWeightCalc|URotorRadialDuctWeightCalc]] | compatibility | integer | N/A | Calculation method of the rotor area for U-shaped rotors with radial ducts |
| [[motorcad/parameter_database/parameters/UpdateCircuitDuringSolving|UpdateCircuitDuringSolving]] | i/p | boolean | N/A | When enabled the circuit editor is updated during the steady state solving process. This can be useful for understanding model convergence. |
| [[motorcad/parameter_database/parameters/UpperLower_ConductorBundle_Method|UpperLower_ConductorBundle_Method]] | compatibility | integer | N/A | Method used to bundle conductor turns for AC Loss calculation with Upper/Lower winding path type. |
| [[motorcad/parameter_database/parameters/UseMagnetTempLinkMethod_Lab|UseMagnetTempLinkMethod_Lab]] | compatibility | integer | N/A | Use MagnetTempLinkMethod (central slice, max or average) for Lab and Thermal loss calculations |
| [[motorcad/parameter_database/parameters/UseSeparateEndRingNodes|UseSeparateEndRingNodes]] | compatibility | boolean | N/A | When enabled separate rotor endring nodes are included in the model |
| [[motorcad/parameter_database/parameters/UseSeparateRotorEndNodes|UseSeparateRotorEndNodes]] | compatibility | boolean | N/A | When enabled separate rotor end nodes are included in the model |
| [[motorcad/parameter_database/parameters/UserCopperLossRatio_Active|UserCopperLossRatio_Active]] | i/p | double | N/A | This is the proportion of rotor cage losses that are on the rotor bars |
| [[motorcad/parameter_database/parameters/UserCopperLossRatio_EndRing_F|UserCopperLossRatio_EndRing_F]] | i/p | double | N/A | This is the proportion of rotor cage losses that are on the front endrings |
| [[motorcad/parameter_database/parameters/UserCopperLossRatio_EndRing_R|UserCopperLossRatio_EndRing_R]] | i/p | double | N/A | This is the proportion of rotor cage losses that are on the rear endrings |
| [[motorcad/parameter_database/parameters/UserStatorCopperLossRatio_Active|UserStatorCopperLossRatio_Active]] | i/p | double | N/A | This is the proportion of stator copper losses that are on the active section |
| [[motorcad/parameter_database/parameters/UserStatorCopperLossRatio_EndWdg_F|UserStatorCopperLossRatio_EndWdg_F]] | i/p | double | N/A | This is the proportion of stator copper losses that are on the front end winding |
| [[motorcad/parameter_database/parameters/UserStatorCopperLossRatio_EndWdg_R|UserStatorCopperLossRatio_EndWdg_R]] | i/p | double | N/A | This is the proportion of stator copper losses that are on the rear end winding |
| [[motorcad/parameter_database/parameters/UserStrayLoadLossRatio_RotorCopper|UserStrayLoadLossRatio_RotorCopper]] | i/p | double | N/A | Proportion of Stray Load Losses that are in the Rotor Windings |
| [[motorcad/parameter_database/parameters/UserStrayLoadLossRatio_RotorIron|UserStrayLoadLossRatio_RotorIron]] | i/p | double | N/A | Proportion of Stray Load Losses that are in the Rotor Iron |
| [[motorcad/parameter_database/parameters/UserStrayLoadLossRatio_StatorCopper|UserStrayLoadLossRatio_StatorCopper]] | i/p | double | N/A | Proportion of Stray Load Losses that are in the Stator Windings |
| [[motorcad/parameter_database/parameters/UserStrayLoadLossRatio_StatorIron|UserStrayLoadLossRatio_StatorIron]] | i/p | double | N/A | Proportion of Stray Load Losses that are in the Stator Iron |
| [[motorcad/parameter_database/parameters/VSimple_Positioning_Method|VSimple_Positioning_Method]] | compatibility | integer | N/A | The method for calculating the position of V Simple Layer segments |
| [[motorcad/parameter_database/parameters/VaryingArmatureCopperLoss_Calc|VaryingArmatureCopperLoss_Calc]] | compatibility | integer | N/A | Calculation method of varying armature copper loss with local winding temperatures |
| [[motorcad/parameter_database/parameters/VirtualWorkGraph|VirtualWorkGraph]] | setting | boolean | N/A | Drawing options for the torque graph |
| [[motorcad/parameter_database/parameters/WedgeDividerRtCalc|WedgeDividerRtCalc]] | compatibility | integer | N/A | Calculation of the wedge and divider thermal resistance for PMDC/WFC machine types |
| [[motorcad/parameter_database/parameters/WetRotorFluidResistanceCalc|WetRotorFluidResistanceCalc]] | compatibility | integer | N/A | The calculation method of the wet rotor fluid node to fluid node thermal resistances with central inlet or coupled slot flow |
| [[motorcad/parameter_database/parameters/WetRotor_RotorWJ_Connection|WetRotor_RotorWJ_Connection]] | i/p | boolean | N/A | When selected the wet rotor outlet is connected to the rotor water jacket inlet |
| [[motorcad/parameter_database/parameters/WetRotor_SlotWJ_Connection|WetRotor_SlotWJ_Connection]] | i/p | boolean | N/A | When selected the wet rotor airgap and slot water jacket paths are in parallel |
| [[motorcad/parameter_database/parameters/WetRotor_SlotWJ_FlowSplit|WetRotor_SlotWJ_FlowSplit]] | i/p | double | N/A | The proportion of flow down slot and airgap. 0 = no flow, all flow down airgap. 1 = all flow, no flow down airgap |
| [[motorcad/parameter_database/parameters/Wet_Rotor|Wet_Rotor]] | i/p | boolean | N/A | Use wet rotor model for forced cooling of internal sections of motor. |
| [[motorcad/parameter_database/parameters/Wet_Rotor_Inlet_Outlet_Position_Front|Wet_Rotor_Inlet_Outlet_Position_Front]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/Wet_Rotor_Inlet_Outlet_Position_Rear|Wet_Rotor_Inlet_Outlet_Position_Rear]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/Wet_Rotor_Shaft_Hole_Cooling|Wet_Rotor_Shaft_Hole_Cooling]] | i/p | integer | N/A | No description |
| [[motorcad/parameter_database/parameters/WindageGraph_MaxSpeed|WindageGraph_MaxSpeed]] | i/p | double | rpm | Maximum speed plotted on the windage loss graph. |
| [[motorcad/parameter_database/parameters/Windage_Loss_Definition|Windage_Loss_Definition]] | i/p | integer | N/A | When this is set to automatic then the fluid properties are used to calculate the windage losses |
| [[motorcad/parameter_database/parameters/Windage_Loss_Multiplier|Windage_Loss_Multiplier]] | i/p | double | N/A | This allows for adjustment of the calculated windage losses |
| [[motorcad/parameter_database/parameters/WindingBitmapSizeFactor|WindingBitmapSizeFactor]] | setting | double | N/A | This sets winding bitmap size. This can be reduced if machine has memory limitations or increased if have detailed winding. |
| [[motorcad/parameter_database/parameters/WindingCuboidPositionDefinition|WindingCuboidPositionDefinition]] | i/p | integer | N/A | This sets how the cuboidal model positions are defined. |
| [[motorcad/parameter_database/parameters/WindingHarmonicAmplitude|WindingHarmonicAmplitude]] | setting | integer | N/A | This gives the option to show the normalised winding harmonics graphs |
| [[motorcad/parameter_database/parameters/WindingLossProportionArray|WindingLossProportionArray]] | o/p | double | N/A | This is the proportion of active winding losses in the cuboid layer |
| [[motorcad/parameter_database/parameters/WindingLossProportionArray_F|WindingLossProportionArray_F]] | o/p | double | N/A | This is the proportion of front end winding losses in the cuboid layer |
| [[motorcad/parameter_database/parameters/WindingLossProportionArray_R|WindingLossProportionArray_R]] | o/p | double | N/A | This is the proportion of rear end winding losses in the cuboid layer |
| [[motorcad/parameter_database/parameters/WindingPatternDisplay|WindingPatternDisplay]] | setting | integer | N/A | The option for displaying the winding pattern arrows |
| [[motorcad/parameter_database/parameters/WindingPatternPenWidth|WindingPatternPenWidth]] | setting | integer | N/A | Pen width for the winding pattern diagram |
| [[motorcad/parameter_database/parameters/WindingSize|WindingSize]] | i/p | integer | N/A | This sets how the cuboidal model sizes are defined. |
| [[motorcad/parameter_database/parameters/WindingTemperatureMethod|WindingTemperatureMethod]] | compatibility | integer | N/A | Method used to calculate the average temperature of the active winding. |
| [[motorcad/parameter_database/parameters/WindingToLamCalculation|WindingToLamCalculation]] | compatibility | integer | N/A | Whether to use the new winding to slot liner resistance calculation. |
| [[motorcad/parameter_database/parameters/WireInsulationWeightsMethod|WireInsulationWeightsMethod]] | compatibility | integer | N/A | This sets how the wire insulation weight is calculated |
| [[motorcad/parameter_database/parameters/XCoord_L|XCoord_L]] | setting | double | mm | This is the x coordinate of centre position of the top left conductor in slot |
| [[motorcad/parameter_database/parameters/XCoord_R|XCoord_R]] | setting | double | mm | This is the x coordinate of centre position of the top left conductor in slot |
| [[motorcad/parameter_database/parameters/YCoord_L|YCoord_L]] | setting | double | mm | This is the y coordinate of centre position of the top left conductor in slot |
| [[motorcad/parameter_database/parameters/YCoord_R|YCoord_R]] | setting | double | mm | This is the y coordinate of centre position of the top left conductor in slot |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
