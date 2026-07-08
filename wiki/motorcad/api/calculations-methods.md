---
type: motorcad_api
method_group: "Calculations"
module: "ansys.motorcad.core"
source_files: ["Calculations — pymotorcad-core.md"]
confidence: Verified
---

# Calculations Methods

## Methods

| Method | Description |
|--------|-------------|
| `calculate_force_harmonics_spatial()` | Calculate 1D force harmonics on space axis |
| `calculate_force_harmonics_temporal()` | Calculate 1D force harmonics on time axis |
| `calculate_im_saturation_model()` | Calculate saturation lookup tables for IM machines |
| `calculate_saturation_map()` | Generate electromagnetic saturation and loss data |
| `calculate_torque_envelope()` | Calculate torque envelope for the machine |
| `create_winding_pattern()` | Create winding pattern |
| `do_magnetic_calculation()` | Run the Motor-CAD magnetic calculation |
| `do_magnetic_thermal_calculation()` | Run coupled e-magnetic and thermal calculations |
| `do_mechanical_calculation()` | Run the Motor-CAD mechanical calculation |
| `do_multi_force_calculation()` | Run multiforce operating point calculation |
| `do_steady_state_analysis()` | Run thermal steady state analysis |
| `do_transient_analysis()` | Run thermal transient analysis |
| `do_weight_calculation()` | Run Motor-CAD weight calculation |
| `get_force_frequency_domain_amplitude(row, ...)` | Export matrix value from force space-time harmonics for 2D FFT |
| `update_force_analysis_results(fft_data_type)` | Update force analysis results for multiforce operating point |

## Related Pages

- [[motorcad/api/general-methods]] — General methods (save/load/export)
- [[motorcad/api/graphs-methods]] — Graph data retrieval
- [[motorcad/workflows/e-magnetic-calculation]] — E-magnetic workflow
- [[motorcad/workflows/thermal-steady-state]] — Thermal steady-state workflow
