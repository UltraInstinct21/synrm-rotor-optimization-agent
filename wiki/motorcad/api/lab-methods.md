---
type: motorcad_api
method_group: "Lab"
module: "ansys.motorcad.core"
source_files: ["Lab — pymotorcad-core.md"]
confidence: Verified
---

# Lab Methods

## Methods

| Method | Description |
|--------|-------------|
| `add_external_custom_loss(name, ...)` | Add external custom loss |
| `add_internal_custom_loss(name, function, ...)` | Add internal custom loss |
| `build_model_lab()` | Build the Lab model |
| `calculate_duty_cycle_lab()` | Run Lab duty cycle |
| `calculate_generator_lab()` | Calculate generator performance |
| `calculate_magnetic_lab()` | Run Lab magnetic calculation |
| `calculate_operating_point_lab()` | Run Lab operating point calculation |
| `calculate_test_performance_lab()` | Calculate test performance |
| `calculate_thermal_lab()` | Run Lab thermal calculation |
| `clear_model_build_lab()` | Clear Lab model build |
| `export_concept_ev_model(**kwargs)` | Export efficiency map in concept EV format |
| `export_duty_cycle_lab()` | Export duty cycle data to thermal model |
| `export_figure_lab(calculation_type)` | Export image of Lab results graph |
| `export_lab_model(file_path)` | Export lab model |
| `get_model_built_lab()` | Test if Lab model needs building |
| `load_external_model_lab(file_path)` | Load external model data file |
| `remove_external_custom_loss(name)` | Remove external custom loss |
| `remove_internal_custom_loss(name)` | Remove internal custom loss |
| `show_results_viewer_lab(calculation_type)` | Load results viewer for Lab calculation type |

## Related Pages

- [[motorcad/api/calculations-methods]] — Core calculation methods
- [[motorcad/workflows/lab-model-example]] — Lab model example script
