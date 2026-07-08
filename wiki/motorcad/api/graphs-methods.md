---
type: motorcad_api
method_group: "Graphs"
module: "ansys.motorcad.core"
source_files: ["Graphs — pymotorcad-core.md"]
confidence: Verified
---

# Graphs Methods

## Methods

| Method | Description |
|--------|-------------|
| `get_fea_graph(graph_name, section_number)` | Get points from FEA graph |
| `get_fea_graph_point(graph_id, ...)` | Get single point from FEA graph |
| `get_heatflow_graph(graph_name)` | Get points from heat flow graph |
| `get_magnetic_3d_graph(graph_name, section_number)` | Get points from Magnetic 3D graph |
| `get_magnetic_3d_graph_point(graph_name, ...)` | Get single point from magnetic 3D graph |
| `get_magnetic_graph(graph_name)` | Get points from magnetic graph |
| `get_magnetic_graph_harmonics(graph_name)` | Get harmonic analysis from magnetic graph |
| `get_magnetic_graph_point(graph_name, ...)` | Get single point from magnetic graph |
| `get_power_graph(graph_name)` | Get points from transient power loss graph |
| `get_power_graph_point(graph_name, point_number)` | Get single point from power graph |
| `get_temperature_graph(graph_name)` | Get points from transient temperature graph |
| `get_temperature_graph_point(graph_name, ...)` | Get single point from thermal graph |

## Common Graph Names

- `TorqueVW` — Torque waveform
- `NVH_NaturalFrequency` — NVH natural frequency
- `NVH_RadiatedPower_Level_OL` — NVH radiated power
- `Ft_Stator_OL_Lumped_Th1` — Stator tangential force (load point 1)
- `Fr_Stator_OL_Lumped_Th1` — Stator radial force (load point 1)

## Related Pages

- [[motorcad/api/calculations-methods]] — Methods that generate graph data
- [[motorcad/workflows/force-extraction-for-ansys-motion]] — Force export workflow
