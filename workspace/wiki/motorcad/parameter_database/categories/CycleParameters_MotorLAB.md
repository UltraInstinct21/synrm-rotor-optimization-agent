---
type: motorcad_parameter_category
category_name: CycleParameters_MotorLAB
parameter_count: 43
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: CycleParameters_MotorLAB

## Overview
The **CycleParameters_MotorLAB** category contains **43** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/A_f_MotorLAB|A_f_MotorLAB]] | i/p | double | N/A | Frontal area |
| [[motorcad/parameter_database/parameters/B_cont_MotorLAB|B_cont_MotorLAB]] | i/p | double | N/A | Contribution of motor to negative torque points |
| [[motorcad/parameter_database/parameters/C_d_MotorLAB|C_d_MotorLAB]] | i/p | double | N/A | Drag coefficient |
| [[motorcad/parameter_database/parameters/DCExtDataType_Lab|DCExtDataType_Lab]] | i/p | integer | N/A | Deprecated value, only used when loading old format Lab duty cycles via ActiveX |
| [[motorcad/parameter_database/parameters/DriveCycleCalcComplete_MotorLAB|DriveCycleCalcComplete_MotorLAB]] | i/p | boolean | N/A | Whether the Lab duty cycle calculation has been completed |
| [[motorcad/parameter_database/parameters/DriveCycle_Lab|DriveCycle_Lab]] | i/p | integer | N/A | Selects which automotive drive cycle to simulate in the Lab duty cycle calculation |
| [[motorcad/parameter_database/parameters/DutyCycleAverageEfficiency_EnergyUse|DutyCycleAverageEfficiency_EnergyUse]] | o/p | double | Percent | Average efficiency during the duty cycle calculated using energy use method |
| [[motorcad/parameter_database/parameters/DutyCycleAverageEfficiency_EnergyUse_Motor|DutyCycleAverageEfficiency_EnergyUse_Motor]] | o/p | double | Percent | Average efficiency during the duty cycle calculated using energy use method as reported at the motor |
| [[motorcad/parameter_database/parameters/DutyCycleAverageEfficiency_Point|DutyCycleAverageEfficiency_Point]] | o/p | double | Percent | Average efficiency during the duty cycle calculated using point by point method |
| [[motorcad/parameter_database/parameters/DutyCycleCalcStatus_MotorLAB|DutyCycleCalcStatus_MotorLAB]] | i/p | OleStr | N/A | Status of the Lab duty cycle calculation |
| [[motorcad/parameter_database/parameters/DutyCycleOperation_Generating|DutyCycleOperation_Generating]] | o/p | double | Percent | Percentage of the duty cycle points that are in generating mode |
| [[motorcad/parameter_database/parameters/DutyCycleOperation_Motoring|DutyCycleOperation_Motoring]] | o/p | double | Percent | Percentage of the duty cycle points that are in motoring mode |
| [[motorcad/parameter_database/parameters/DutyCycleTotalEnergy_Electrical_Input|DutyCycleTotalEnergy_Electrical_Input]] | o/p | double | Wh | Total electrical input energy provided to the motor during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalEnergy_Electrical_Input_Motor|DutyCycleTotalEnergy_Electrical_Input_Motor]] | o/p | double | Wh | Total electrical input energy provided to the motor during the duty cycle as reported at the motor |
| [[motorcad/parameter_database/parameters/DutyCycleTotalEnergy_Electrical_Output|DutyCycleTotalEnergy_Electrical_Output]] | o/p | double | Wh | Total electrical output energy recovered while generating during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalEnergy_Electrical_Output_Motor|DutyCycleTotalEnergy_Electrical_Output_Motor]] | o/p | double | Wh | Total electrical output energy recovered while generating during the duty cycle as reported at the motor |
| [[motorcad/parameter_database/parameters/DutyCycleTotalEnergy_Shaft_Input|DutyCycleTotalEnergy_Shaft_Input]] | o/p | double | Wh | Total shaft input energy provided to the motor while generating during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalEnergy_Shaft_Output|DutyCycleTotalEnergy_Shaft_Output]] | o/p | double | Wh | Total shaft output energy produced while motoring during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss|DutyCycleTotalLoss]] | o/p | double | Wh | Total losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss_Iron|DutyCycleTotalLoss_Iron]] | o/p | double | Wh | Total iron losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss_Magnet|DutyCycleTotalLoss_Magnet]] | o/p | double | Wh | Total magnet losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss_Mechanical|DutyCycleTotalLoss_Mechanical]] | o/p | double | Wh | Total mechanical losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss_Motor|DutyCycleTotalLoss_Motor]] | o/p | double | Wh | Total motor losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss_RotorCage|DutyCycleTotalLoss_RotorCage]] | o/p | double | Wh | Total rotor cage losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss_RotorCopper|DutyCycleTotalLoss_RotorCopper]] | o/p | double | Wh | Total rotor copper losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleTotalLoss_StatorCopper|DutyCycleTotalLoss_StatorCopper]] | o/p | double | Wh | Total stator copper losses during the duty cycle |
| [[motorcad/parameter_database/parameters/DutyCycleType_Lab|DutyCycleType_Lab]] | i/p | integer | N/A | Type of Lab duty cycle (custom duty cycle or automotive drive cycle) |
| [[motorcad/parameter_database/parameters/Duty_Cycle_SyncCurrentLimit_Method_Lab|Duty_Cycle_SyncCurrentLimit_Method_Lab]] | compatibility | integer | N/A | Improved method uses the model current limits rather than the efficiency map limits |
| [[motorcad/parameter_database/parameters/Duty_Cycle_Vehicle_MassMethod|Duty_Cycle_Vehicle_MassMethod]] | compatibility | integer | N/A | Improved method uses the vehicle Mass Correction Factor for rolling resistance |
| [[motorcad/parameter_database/parameters/IncludeMotorInertiaInVehicleModel|IncludeMotorInertiaInVehicleModel]] | compatibility | boolean | N/A | When true, include rotor and shaft intertia in vehicle model |
| [[motorcad/parameter_database/parameters/K_r_MotorLAB|K_r_MotorLAB]] | i/p | double | N/A | Rolling resistance coefficient |
| [[motorcad/parameter_database/parameters/M_o_MotorLAB|M_o_MotorLAB]] | i/p | double | N/A | Mass correction factor |
| [[motorcad/parameter_database/parameters/Mass_MotorLAB|Mass_MotorLAB]] | i/p | double | kg | Vehicle mass |
| [[motorcad/parameter_database/parameters/N_d_MotorLAB|N_d_MotorLAB]] | i/p | double | N/A | Gear ratio (final drive ratio) in the vehicle model |
| [[motorcad/parameter_database/parameters/R_w_MotorLAB|R_w_MotorLAB]] | i/p | double | N/A | Wheel radius |
| [[motorcad/parameter_database/parameters/SpeedCapTrue_MotorLAB|SpeedCapTrue_MotorLAB]] | i/p | boolean | N/A | Limit duty cycle to maximum speed |
| [[motorcad/parameter_database/parameters/SpeedCap_MotorLAB|SpeedCap_MotorLAB]] | i/p | double | rpm | Maximum speed limit in duty cycle |
| [[motorcad/parameter_database/parameters/T_cont_MotorLAB|T_cont_MotorLAB]] | i/p | double | N/A | Contribution of motor to positive torque points |
| [[motorcad/parameter_database/parameters/TorqueCapTrue_MotorLAB|TorqueCapTrue_MotorLAB]] | i/p | boolean | N/A | Limit duty cycle to maximum torque |
| [[motorcad/parameter_database/parameters/TorqueCap_MotorLAB|TorqueCap_MotorLAB]] | i/p | double | Nm | Maximum torque limit in duty cycle |
| [[motorcad/parameter_database/parameters/WheelInertia|WheelInertia]] | i/p | double | kg.m² | Inertia of all wheels on the vehicle |
| [[motorcad/parameter_database/parameters/WheelInertiaTorqueMethod|WheelInertiaTorqueMethod]] | compatibility | integer | N/A | Method of calculating wheel inertia torque for the vehicle model |
| [[motorcad/parameter_database/parameters/rho_MotorLAB|rho_MotorLAB]] | i/p | double | kg/m³ | Air density |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
