---
type: pymotorcad_api
title: "PyMotorCAD Graphs API"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - graphs
  - results
  - visualization
  - fea
  - magnetic
  - thermal
  - api
aliases:
  - pymotorcad_graphs
  - motorcad_graphs
related_pages:
  - "[[pymotorcad-emag-example]]"
  - "[[pymotorcad-thermal-example]]"
  - "[[pymotorcad-calculations-api]]"
  - "[[pymotorcad-motorcad-api]]"
confidence: verified
---

# PyMotorCAD Graphs API

## Overview

The Graphs API provides methods to extract detailed result data from Motor-CAD as arrays suitable for plotting and analysis. After running a calculation, the graph methods retrieve spatial, temporal, and harmonic data for electromagnetic fields, temperatures, power losses, and heat flows.

All graph methods return data as NumPy arrays or lists that can be directly plotted with matplotlib or processed numerically.

---

## FEA Graphs

### `get_fea_graph()`

#### Purpose

Retrieves a complete FEA (Finite Element Analysis) result graph for a specified variable, returning the full spatial or temporal distribution.

#### Signature

```python
get_fea_graph(graph_type: str) -> list
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Identifier for the FEA graph type |

#### Description

Returns the full array of FEA solution data. Common graph types include:

- Flux density distribution along a path
- Field intensity distribution
- Vector potential distribution
- Force distribution on stator teeth

#### Example

```python
import ansys.motorcad.core as pymotorcad
import matplotlib.pyplot as plt

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)

mc.do_magnetic_calculation()

# Get flux density along airgap
flux_data = mc.get_fea_graph("Airgap_Flux_Density")

plt.plot(flux_data)
plt.xlabel("Position (degrees)")
plt.ylabel("Flux Density (T)")
plt.title("Airgap Flux Density Distribution")
plt.grid(True)
plt.show()
```

---

### `get_fea_graph_point()`

#### Purpose

Retrieves a single point value from an FEA result graph at a specified index.

#### Signature

```python
get_fea_graph_point(graph_type: str, point_index: int) -> float
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Identifier for the FEA graph type |
| `point_index` | `int` | Index of the point to retrieve |

#### Description

More efficient than `get_fea_graph()` when only a single value is needed. Useful for extracting peak values, specific spatial locations, or specific time steps.

#### Example

```python
# Get flux density at the 10th spatial point
flux_at_point = mc.get_fea_graph_point("Airgap_Flux_Density", 9)
print(f"Flux density at point 10: {flux_at_point:.4f} T")

# Find peak value by iterating
flux_full = mc.get_fea_graph("Airgap_Flux_Density")
peak_flux = max(abs(f) for f in flux_full)
print(f"Peak flux density: {peak_flux:.4f} T")
```

---

## Magnetic Graphs

### `get_magnetic_graph()`

#### Purpose

Retrieves a complete magnetic result graph, including waveforms of flux, current, voltage, torque, and other electromagnetic quantities over one electrical cycle.

#### Signature

```python
get_magnetic_graph(graph_type: str) -> list
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Magnetic graph type identifier |

#### Description

Returns waveform data over one electrical cycle. Common magnetic graph types:

| Graph Type | Description |
|---|---|
| `PhaseCurrent` | Phase current waveform |
| `PhaseVoltage` | Phase voltage waveform |
| `Flux_Linkage` | Flux linkage waveform |
| `Torque` | Instantaneous torque waveform |
| `AirgapFluxDensity` | Radial flux density in airgap |
| `BackEMF` | Back-EMF waveform |

#### Example

```python
mc.do_magnetic_calculation()

# Get torque waveform
torque_waveform = mc.get_magnetic_graph("Torque")

import matplotlib.pyplot as plt
import numpy as np

angle = np.linspace(0, 360, len(torque_waveform))
plt.plot(angle, torque_waveform)
plt.xlabel("Electrical Angle (deg)")
plt.ylabel("Torque (Nm)")
plt.title("Instantaneous Torque Waveform")
plt.grid(True)
plt.show()

# Calculate torque ripple
torque_ripple = (max(torque_waveform) - min(torque_waveform)) / np.mean(torque_waveform) * 100
print(f"Torque Ripple: {torque_ripple:.1f}%")
```

---

### `get_magnetic_graph_point()`

#### Purpose

Retrieves a single point from a magnetic result graph.

#### Signature

```python
get_magnetic_graph_point(graph_type: str, point_index: int) -> float
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Magnetic graph type identifier |
| `point_index` | `int` | Index of the point to retrieve |

#### Example

```python
# Get peak torque from waveform
torque_waveform = mc.get_magnetic_graph("Torque")
peak_torque = mc.get_magnetic_graph_point("Torque", np.argmax(torque_waveform))
print(f"Peak torque: {peak_torque:.2f} Nm")
```

---

### `get_magnetic_graph_harmonics()`

#### Purpose

Performs harmonic analysis on a magnetic graph, returning the amplitude and phase of each harmonic component.

#### Signature

```python
get_magnetic_graph_harmonics(graph_type: str) -> tuple
```

#### Returns

A tuple of two lists:
- `amplitudes`: Amplitude of each harmonic component
- `phases`: Phase angle of each harmonic component (degrees)

#### Description

Decomposes a magnetic waveform into its harmonic spectrum using FFT. This is essential for:

- Torque ripple analysis
- Vibration and NVH prediction
- Loss estimation (iron loss depends on harmonic content)
- Power quality assessment

#### Example

```python
mc.do_magnetic_calculation()

# Get torque harmonic spectrum
amplitudes, phases = mc.get_magnetic_graph_harmonics("Torque")

# Plot harmonic spectrum
harmonics = range(len(amplitudes))
plt.bar(harmonics, amplitudes)
plt.xlabel("Harmonic Order")
plt.ylabel("Amplitude (Nm)")
plt.title("Torque Harmonic Spectrum")
plt.grid(True)
plt.show()

# Print dominant harmonics
for i, (amp, phs) in enumerate(zip(amplitudes, phases)):
    if amp > 0.1 * max(amplitudes):  # Show harmonics > 10% of max
        print(f"Harmonic {i}: {amp:.3f} Nm at {phs:.1f} deg")
```

#### Key Harmonic Orders for SynRM

| Harmonic | Significance |
|---|---|
| 0th (DC) | Average torque |
| 2nd | Main torque ripple component (4-pole) |
| 4th | Secondary torque ripple |
| 6th | Higher-order ripple, NVH concern |
| 12th | Slot harmonics |

---

## 3D Magnetic Graphs

### `get_magnetic_3d_graph()`

#### Purpose

Retrieves a 3D magnetic result graph, providing data as a 2D matrix (e.g., flux density as a function of both position and time).

#### Signature

```python
get_magnetic_3d_graph(graph_type: str) -> list
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | 3D magnetic graph type identifier |

#### Description

Returns a 2D array where rows represent spatial positions and columns represent time steps (or vice versa). This is used for:

- Spatiotemporal flux density maps
- Rotating field visualization
- Space-time harmonic analysis

#### Example

```python
mc.do_magnetic_calculation()

# Get 3D flux density map
flux_3d = mc.get_magnetic_3d_graph("AirgapFluxDensity_3D")

import matplotlib.pyplot as plt
import numpy as np

flux_array = np.array(flux_3d)
plt.imshow(flux_array, aspect='auto', cmap='jet',
           extent=[0, 360, 0, 360])
plt.xlabel("Electrical Angle (deg)")
plt.ylabel("Mechanical Angle (deg)")
plt.title("Airgap Flux Density Map")
plt.colorbar(label="Flux Density (T)")
plt.show()
```

---

### `get_magnetic_3d_graph_point()`

#### Purpose

Retrieves a single point from a 3D magnetic graph at specified spatial and temporal indices.

#### Signature

```python
get_magnetic_3d_graph_point(graph_type: str, spatial_index: int, temporal_index: int) -> float
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | 3D magnetic graph type identifier |
| `spatial_index` | `int` | Spatial position index |
| `temporal_index` | `int` | Time step index |

#### Example

```python
# Get flux density at specific position and time
flux_point = mc.get_magnetic_3d_graph_point("AirgapFluxDensity_3D", 10, 5)
print(f"Flux density at spatial point 10, time step 5: {flux_point:.4f} T")
```

---

## Temperature Graphs

### `get_temperature_graph()`

#### Purpose

Retrieves a temperature distribution graph, showing temperature as a function of position along a specified path or as a function of time.

#### Signature

```python
get_temperature_graph(graph_type: str) -> list
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Temperature graph type identifier |

#### Description

Common temperature graph types:

| Graph Type | Description |
|---|---|
| `Winding_Axial` | Temperature along winding axis |
| `Stator_Radial` | Temperature from bore to yoke |
| `Rotor_Radial` | Temperature from shaft to OD |
| `Transient_Winding` | Winding temperature vs. time |
| `Transient_Magnet` | Magnet temperature vs. time |

#### Example

```python
mc.do_steady_state_analysis()

# Get winding temperature distribution (axial)
winding_temp = mc.get_temperature_graph("Winding_Axial")

import matplotlib.pyplot as plt
import numpy as np

position = np.linspace(0, 180, len(winding_temp))  # mm along axis
plt.plot(position, winding_temp)
plt.xlabel("Axial Position (mm)")
plt.ylabel("Temperature (C)")
plt.title("Winding Temperature Distribution")
plt.grid(True)
plt.show()

print(f"Max winding temperature: {max(winding_temp):.1f} C")
print(f"Min winding temperature: {min(winding_temp):.1f} C")
```

---

### `get_temperature_graph_point()`

#### Purpose

Retrieves a single temperature value at a specified position along a temperature graph path.

#### Signature

```python
get_temperature_graph_point(graph_type: str, point_index: int) -> float
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Temperature graph type identifier |
| `point_index` | `int` | Index of the point to retrieve |

#### Example

```python
# Get temperature at the middle of the winding axially
winding_temp = mc.get_temperature_graph("Winding_Axial")
midpoint = len(winding_temp) // 2
temp_at_mid = mc.get_temperature_graph_point("Winding_Axial", midpoint)
print(f"Temperature at mid-axial position: {temp_at_mid:.1f} C")
```

---

## Power Graphs

### `get_power_graph()`

#### Purpose

Retrieves a power loss distribution graph, showing loss breakdown as a function of position, frequency, or time.

#### Signature

```python
get_power_graph(graph_type: str) -> list
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Power graph type identifier |

#### Description

Common power graph types:

| Graph Type | Description |
|---|---|
| `IronLoss_Radial` | Iron loss vs. radial position |
| `IronLoss_Frequency` | Iron loss vs. frequency |
| `CopperLoss_Distribution` | Copper loss per slot |
| `TotalLoss_Breakdown` | Complete loss breakdown |

#### Example

```python
mc.do_magnetic_calculation()

# Get iron loss frequency spectrum
iron_loss_freq = mc.get_power_graph("IronLoss_Frequency")

import matplotlib.pyplot as plt
import numpy as np

freq = np.arange(len(iron_loss_freq)) * 100  # Assuming 100 Hz resolution
plt.plot(freq, iron_loss_freq)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Iron Loss (W)")
plt.title("Iron Loss Frequency Spectrum")
plt.grid(True)
plt.show()
```

---

### `get_power_graph_point()`

#### Purpose

Retrieves a single value from a power loss graph.

#### Signature

```python
get_power_graph_point(graph_type: str, point_index: int) -> float
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Power graph type identifier |
| `point_index` | `int` | Index of the point to retrieve |

#### Example

```python
# Get total iron loss by summing frequency components
iron_loss_freq = mc.get_power_graph("IronLoss_Frequency")
total_iron_loss = sum(iron_loss_freq)
print(f"Total iron loss: {total_iron_loss:.2f} W")
```

---

## Heat Flow Graphs

### `get_heatflow_graph()`

#### Purpose

Retrieves a heat flow graph, showing the rate of heat transfer between thermal nodes in the motor's thermal network.

#### Signature

```python
get_heatflow_graph(graph_type: str) -> list
```

#### Parameters

| Parameter | Type | Description |
|---|---|---|
| `graph_type` | `str` | Heat flow graph type identifier |

#### Description

Heat flow graphs show how heat moves through the motor's cooling paths. Useful for:

- Identifying thermal bottlenecks
- Evaluating cooling effectiveness
- Understanding heat path priorities
- Optimizing cooling system design

#### Example

```python
mc.do_steady_state_analysis()

# Get heat flow through cooling paths
heat_flows = mc.get_heatflow_graph("Cooling_Path")

# Identify dominant heat paths
for i, hf in enumerate(heat_flows):
    print(f"Path {i}: {hf:.2f} W")
```

---

## Common Graph Types Reference

### EMag Graph Types

| Graph Type | Description | Data Shape |
|---|---|---|
| `Airgap_Flux_Density` | Radial flux density in airgap | 1D array |
| `PhaseCurrent` | Phase current waveform | 1D array |
| `PhaseVoltage` | Phase voltage waveform | 1D array |
| `Torque` | Instantaneous torque | 1D array |
| `Flux_Linkage` | Flux linkage waveform | 1D array |
| `BackEMF` | Back-EMF waveform | 1D array |
| `IronLoss_Frequency` | Iron loss spectrum | 1D array |

### Thermal Graph Types

| Graph Type | Description | Data Shape |
|---|---|---|
| `Winding_Axial` | Axial temperature distribution | 1D array |
| `Stator_Radial` | Radial temperature in stator | 1D array |
| `Rotor_Radial` | Radial temperature in rotor | 1D array |
| `Transient_*` | Temperature vs. time | 1D array |

---

## Complete Graph Workflow Example

```python
import ansys.motorcad.core as pymotorcad
import matplotlib.pyplot as plt
import numpy as np

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\synrm_45kw.mot")

# Set operating point
mc.set_variable("Shaft_Speed_[RPM]", 3000)
mc.set_variable("PhaseAdvance", 45)

# Run EMag
mc.do_magnetic_calculation()

# --- Torque waveform and harmonics ---
torque = mc.get_magnetic_graph("Torque")
amplitudes, phases = mc.get_magnetic_graph_harmonics("Torque")

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

angle = np.linspace(0, 360, len(torque))
axes[0].plot(angle, torque)
axes[0].set_xlabel("Electrical Angle (deg)")
axes[0].set_ylabel("Torque (Nm)")
axes[0].set_title("Torque Waveform")
axes[0].grid(True)

axes[1].bar(range(len(amplitudes)), amplitudes)
axes[1].set_xlabel("Harmonic Order")
axes[1].set_ylabel("Amplitude (Nm)")
axes[1].set_title("Torque Harmonics")
axes[1].grid(True)

plt.tight_layout()
plt.savefig(r"D:\results\torque_analysis.png", dpi=150)
plt.show()

# --- Airgap flux density ---
flux = mc.get_fea_graph("Airgap_Flux_Density")
plt.figure(figsize=(8, 4))
plt.plot(flux)
plt.xlabel("Position")
plt.ylabel("Flux Density (T)")
plt.title("Airgap Flux Density")
plt.grid(True)
plt.savefig(r"D:\results\airgap_flux.png", dpi=150)
plt.show()

# --- Summary ---
avg_torque = np.mean(torque)
torque_ripple = (max(torque) - min(torque)) / avg_torque * 100
print(f"Average Torque: {avg_torque:.2f} Nm")
print(f"Torque Ripple: {torque_ripple:.1f}%")
print(f"Peak flux density: {max(abs(np.array(flux))):.4f} T")
```

---

## Cross-References

- [[pymotorcad-emag-example]] — Electromagnetic workflow using graph methods
- [[pymotorcad-thermal-example]] — Thermal workflow using temperature graphs
- [[pymotorcad-calculations-api]] — Calculation methods that produce graph data
- [[pymotorcad-motorcad-api]] — Full API reference
- [[pymotorcad-lab-api]] — Lab-level result extraction

---

## Tags

#pymotorcad #motorcad #api #graphs #visualization #fea #magnetic #thermal #power #heatflow #harmonics #results #plotting
