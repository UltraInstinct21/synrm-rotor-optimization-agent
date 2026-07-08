---
type: motorcad_workflow
name: "Thermal Twin Builder ROM Export"
purpose: "Export thermal reduced-order model for Twin Builder Motor-CAD ROM component"
prerequisites: ["Motor-CAD v2024 R2+", "Ansys Twin Builder 2024 R2+"]
source_files: ["Motor-CAD Thermal Twin Builder ROM — pymotorcad-core.md"]
confidence: Verified
---

# Thermal Twin Builder ROM Export

## Purpose

Generate the data files needed to create a Motor-CAD thermal ROM (Reduced Order Model) component in Ansys Twin Builder. The ROM interpolates between multiple operating points for accurate thermal simulation.

## Prerequisites

- Twin Builder 2024 R2 or later
- Motor-CAD thermal model with losses defined

## Background

Motor-CAD's LPTN (Lumped Parameter Thermal Network) is exported as thermal matrices at multiple operating points. Twin Builder interpolates between these during simulation, including coolant flow model.

## Step-by-Step Procedure

### 1. Create MotorCADTwinModel Object

```python
MotorCADTwin = MotorCADTwinModel(inputMotFilePath, outputDir)
```

### 2. Generate Data

```python
MotorCADTwin.generateTwinData(
    parameters={"rpm": [200, 500, 1000]},
    housingAmbientTemperatures=housingAmbientTemps,
    airgapTemperatures=[40, 50, 65],
    coolingSystemsInputs={
        "Housing Water Jacket": {
            "rpm": rpms,
            "FR": [9.77e-05, 0.000103, 0.000109],
            "inletTemp": [40, 65],
        }
    },
)
```

### 3. Key Operations

The class performs:

1. **Node data extraction** — identifies thermal nodes, groupings, inlet nodes
2. **Cooling system network** — maps fluid flow paths using graph analysis (networkx)
3. **DoE samples** — solves thermal model at each RPM, exports matrices
4. **Loss distribution** — determines per-node loss fractions for each loss type
5. **Housing temp dependency** — characterizes natural convection at housing
6. **Airgap temp dependency** — characterizes temperature-dependent airgap resistance

### 4. Generated Files

| File/Folder | Purpose |
|-------------|---------|
| `dp000000/` to `dpNNNNNN/` | Thermal matrices per operating point |
| `doe.csv` | Design of experiments (RPM values) |
| `CoolingSystems.csv` | Cooling system node flow paths |
| `LossDistribution.csv` | Per-node loss distribution matrix |
| `HousingTempDependency/` | Natural convection characterization |
| `AirGapTempDependency/` | Airgap heat transfer characterization |
| `config.txt` | Model configuration flags |

### 5. Import into Twin Builder

In Ansys Electronics Desktop: **Twin Builder → Add Component → Add Motor-CAD ROM Component…** and point to the output folder.

## Key Matrices Exported

| Matrix | File | Content |
|--------|------|---------|
| Resistance | `.rmf` | Thermal resistances between nodes |
| Capacitance | `.cmf` | Thermal capacitances |
| Power | `.pmf` | Power distribution to nodes |
| Temperature | `.tmf` | Node temperatures |
| Node names | `.nmf` | Node numbers, names, groupings |

## Related Pages

- [[motorcad/api/calculations-methods]] — do_steady_state_analysis, export_matrices
- [[motorcad/workflows/emag-twin-builder-ece]] — Electromagnetic ECE export
- [[motorcad/workflows/thermal-example-script]] — Basic thermal analysis
