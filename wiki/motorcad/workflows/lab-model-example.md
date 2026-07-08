---
type: motorcad_workflow
name: "Motor-CAD Lab Model Example"
purpose: "Build Lab model, calculate performance maps, and operating points"
prerequisites: ["Motor-CAD", "e8 template"]
source_files: ["Motor-CAD Lab model example script — pymotorcad-core.md"]
confidence: Verified
---

# Motor-CAD Lab Model Example

## Purpose

Build a Motor-CAD Lab model for rapid performance calculations, generate torque-speed maps, and evaluate operating points.

## Step-by-Step Procedure

### 1. Setup and Build Model

```python
mcad = pymotorcad.MotorCAD()
mcad.set_variable("MessageDisplayState", 2)
mcad.load_template("e8")

# Configure Lab model
mcad.set_variable("ModelType_MotorLAB", 1)
mcad.set_variable("SatModelPoints_MotorLAB", 0)
mcad.set_variable("LossModel_Lab", 0)
mcad.set_variable("ModelBuildSpeed_MotorLAB", 10000)
mcad.set_variable("MaxModelCurrent_MotorLAB", 480)
mcad.set_variable("BuildSatModel_MotorLAB", True)

mcad.set_motorlab_context()
mcad.clear_model_build_lab()
mcad.build_model_lab()
```

### 2. Calculate E-Magnetic Performance

```python
mcad.set_variable("EmagneticCalcType_Lab", 0)
mcad.set_variable("SpeedMax_MotorLAB", 10000)
mcad.set_variable("Speedinc_MotorLAB", 250)
mcad.set_variable("SpeedMin_MotorLAB", 500)
mcad.set_variable("Imax_MotorLAB", 480)

mcad.calculate_magnetic_lab()

# Load results from .mat file
data = io.loadmat(os.path.join(working_folder, mcad_name, "Lab", "MotorLAB_elecdata.mat"))
speed = data["Speed"]
shaft_torque = data["Shaft_Torque"]
shaft_power = data["Shaft_Power"]
```

### 3. Calculate Operating Point

```python
mcad.set_variable("OpPointSpec_MotorLAB", 1)
mcad.set_variable("StatorCurrentDemand_Lab", 480)
mcad.set_variable("SpeedDemand_MotorLAB", 4000)
mcad.set_variable("LabThermalCoupling", 0)
mcad.set_variable("LabMagneticCoupling", 0)

mcad.calculate_operating_point_lab()

shaft_torque = mcad.get_variable("LabOpPoint_ShaftTorque")
efficiency = mcad.get_variable("LabOpPoint_Efficiency")
```

## Key Methods

| Method | Purpose |
|--------|---------|
| `build_model_lab()` | Build the Lab lookup model |
| `calculate_magnetic_lab()` | Calculate torque-speed-current maps |
| `calculate_operating_point_lab()` | Evaluate specific operating point |
| `set_motorlab_context()` | Switch to Lab context |

## Related Pages

- [[motorcad/api/lab-methods]] — All Lab methods
- [[motorcad/api/calculations-methods]] — Calculation methods
