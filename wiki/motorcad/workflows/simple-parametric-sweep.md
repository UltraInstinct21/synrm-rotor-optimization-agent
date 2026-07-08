---
type: motorcad_workflow
name: "Simple Parametric Sweep"
purpose: "Run 2D parametric sweep varying multiple motor parameters"
prerequisites: ["Motor-CAD", "e3 WFSM template or similar"]
source_files: ["Simple parametric sweep for SYNC machine — pymotorcad-core.md"]
confidence: Verified
---

# Simple Parametric Sweep

## Purpose

Run a two-dimensional parametric sweep for a wound field synchronous motor, varying stator skew and field current, then analyze NVH results.

## Step-by-Step Procedure

### 1. Setup Motor-CAD

```python
mc = pymotorcad.MotorCAD()
mc.set_variable("MessageDisplayState", 2)
mc.load_template("e3")

# Enable required calculations
mc.set_variable("TorqueCalculation", True)
mc.set_variable("ElectromagneticForcesCalc_Load", True)
mc.set_variable("SkewType", 1)  # Continuous stator skew
```

### 2. Define Sweep Parameters

```python
skew_angles = [0, 7.5]
field_currents = [5, 10]
```

### 3. Run Sweep

```python
for skew_angle in skew_angles:
    for field_current in field_currents:
        mc.set_variable("StatorSkew", skew_angle)
        mc.set_variable("DCFieldCurrent", field_current)

        print(f"Running skew: {skew_angle} Field current: {field_current}")
        mc.do_magnetic_calculation()

        # Get NVH data
        nvh_data_raw = mc.get_magnetic_3d_graph("NVH_RadiatedPower_Level_OL", 1)

        # Process and sort results
        nvh_list = []
        for raw_time_order in range(len(nvh_data_raw.y)):
            electrical_order = raw_time_order / numberOfCycles
            for raw_space_order in range(len(nvh_data_raw.x)):
                space_order = raw_space_order - index_offset_space
                nvh_list.append((
                    nvh_data_raw.data[raw_space_order][raw_time_order],
                    electrical_order,
                    space_order,
                ))

        nvh_list.sort(reverse=True)
        print("Sound power level [dB], electrical time order, space order:")
        for i in range(min(5, len(nvh_list))):
            print(nvh_list[i])
```

## Key Pattern

- Nested loops for multi-parameter sweeps
- `do_magnetic_calculation()` per parameter combination
- NVH data extracted via `get_magnetic_3d_graph()`
- Results sorted by sound power level to find dominant orders

## Related Pages

- [[motorcad/api/calculations-methods]] — do_magnetic_calculation
- [[motorcad/api/graphs-methods]] — get_magnetic_3d_graph
- [[motorcad/api/general-methods]] — set_variable, get_variable
