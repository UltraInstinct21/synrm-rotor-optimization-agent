---
type: motorcad_workflow
name: "Force Extraction and NVH Example"
purpose: "Set up force/NVH calculation and extract key force orders from 2D FFT"
prerequisites: ["Motor-CAD", "e9 template or similar"]
source_files: ["Motor-CAD force extraction example script — pymotorcad-core.md"]
confidence: Verified
---

# Force Extraction and NVH Example

## Purpose

Configure and run electromagnetic force calculations, then extract specific force orders from the 2D FFT for NVH analysis.

## Step-by-Step Procedure

### 1. Setup Operating Points

```python
mc = pymotorcad.MotorCAD()
mc.set_variable("MessageDisplayState", 2)
mc.load_template("e9")

mc.set_variable("TorquePointsPerCycle", 90)  # Up to 45th electrical order
mc.set_variable("MultiForceThreading", 0)     # Multithreaded

# Speed/torque operating points
operating_points_speed = [250, 4000, 8000]   # RPM
operating_points_torque = [250, 250, 100]     # Nm
mc.set_variable("NumLoadPoints", 3)

for i in range(3):
    mc.set_array_variable("LoadPoint_Speed_Array", i, operating_points_speed[i])
    mc.set_array_variable("LoadPoint_Torque_Array", i, operating_points_torque[i])
```

### 2. Run Force Calculation

```python
mc.do_multi_force_calculation()
```

### 3. Extract Force Orders

```python
# Define orders of interest: [space_order, electrical_time_order]
required_orders = [[0, 12], [0, 24], [8, 2], [-8, 10], [8, 14]]

for operating_point in range(num_operating_points):
    for required_order in required_orders:
        space_order = required_order[0]
        electrical_order = required_order[1]

        # Handle negative space orders
        if space_order < 0:
            raw_space_order = space_order + 2 * mech_force_space_order_max
        else:
            raw_space_order = space_order

        raw_time_order = electrical_order * electrical_cycles

        _, amplitude = mc.get_magnetic_3d_graph_point(
            "Fr_Density_Stator_FFT_Amplitude_OL" + "_Th" + str(operating_point + 1),
            rotor_slice + 1, raw_space_order, raw_time_order,
        )
```

## Key Variables

| Variable | Purpose |
|----------|---------|
| `TorquePointsPerCycle` | Frequency resolution (90 → up to 45th order) |
| `MultiForceThreading` | 0=multithreaded, 1=single |
| `ForceMaxOrder_Space_Stator_OL` | Maximum space order available |

## Key Methods

| Method | Purpose |
|--------|---------|
| `do_multi_force_calculation()` | Run multi-point force FEA |
| `get_magnetic_3d_graph_point()` | Extract specific FFT component |

## Related Pages

- [[motorcad/api/calculations-methods]] — do_multi_force_calculation
- [[motorcad/api/graphs-methods]] — get_magnetic_3d_graph_point
- [[motorcad/workflows/force-export-ansys-motion]] — Export for Ansys Motion
