---
type: motorcad_workflow
name: "EMag Twin Builder ECE Export"
purpose: "Export equivalent circuit model for PMSM to Ansys Twin Builder"
prerequisites: ["Motor-CAD", "Ansys Twin Builder", "JSON config file"]
source_files: ["Motor-CAD EMag Twin Builder ECE — pymotorcad-core.md"]
confidence: Verified
---

# EMag Twin Builder ECE Export

## Purpose

Export an equivalent circuit extraction (ECE) model for PMSMs from Motor-CAD to Ansys Twin Builder for system-level simulation.

## Prerequisites

- JSON configuration file (`ece_config.json`) in same directory as script
- Config contains: mot_file, shaft_speed, dc_bus_voltage, temperatures, current limits

## Step-by-Step Procedure

### 1. Load Configuration

```python
with open("ece_config.json", "r") as f:
    in_data = json.load(f)

shaft_speed = in_data["shaft_speed"]
dc_bus_voltage = float(in_data["dc_bus_voltage"])
machine_temp = float(in_data["machine_temp"])
```

### 2. Determine Alignment Angle

Run open-circuit back EMF calculation:

```python
mc.set_variable("PeakCurrent", 0)
mc.set_variable("DCBusVoltage", dc_bus_voltage)
mc.do_magnetic_calculation()

e_deg, flux_a = mc.get_magnetic_graph("FluxLinkageOCPh1")
drive_offset = mc.get_variable("DriveOffsetAngleLoad")
alignment_angle = 90 + drive_offset
```

### 3. Calculate Saturation Map

```python
mc.set_variable("SaturationMap_InputDefinition", 1)  # D/Q axis currents
mc.set_variable("SaturationMap_CalculationMethod", 1)  # FEA
mc.set_variable("SaturationMap_Current_D_Max", Id_max)
mc.calculate_saturation_map()
```

### 4. Generate Look-up Table

Build D-Q flux and torque look-up tables from saturation map data:

```python
final_table = np.array([
    index_1, flux_d_2, flux_q_3, flux_0_4,
    torque_5, id_6, iq_7, phase_ad_8, rotor_pos_9
])
```

### 5. Write TXT and SML Files

- **TXT file**: Phase resistance, inductance, D/Q current grids, flux/torque tables
- **SML file**: Twin Builder model definition with electrical ports, look-up tables, and D-Q transform

## Output Files

| File | Purpose |
|------|---------|
| `*.txt` | ECE parameters in text format |
| `*.sml` | Twin Builder model definition |
| `*.mat` | Saturation map data |

## Related Pages

- [[motorcad/api/lab-methods]] — calculate_saturation_map
- [[motorcad/api/calculations-methods]] — do_magnetic_calculation
- [[motorcad/workflows/thermal-twin-builder-rom]] — Thermal ROM export
