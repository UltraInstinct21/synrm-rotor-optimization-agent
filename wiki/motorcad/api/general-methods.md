---
type: motorcad_api
method_group: "General"
module: "ansys.motorcad.core"
source_files: ["General — pymotorcad-core.md"]
confidence: Verified
---

# General Methods

## File Operations

| Method | Description |
|--------|-------------|
| `load_from_file(mot_file)` | Load a MOT file into Motor-CAD |
| `save_to_file(mot_file)` | Save the MOT file |
| `download_mot_file(file_path)` | Download current .mot and write to local directory |
| `upload_mot_file(file_path)` | Upload .mot file to Motor-CAD instance |
| `load_template(template_name)` | Load a motor template |
| `save_template(template_file_name, name, ...)` | Save template to MTT file |

## Export Methods

| Method | Description |
|--------|-------------|
| `export_results(solution_type, file_path)` | Export results to CSV |
| `export_matrices(directory_path)` | Export resistance, power, capacitance matrices |
| `export_force_animation(animation, file_name)` | Export force animation to GIF |
| `export_multi_force_data(file_name)` | Export multiforce data |
| `export_nvh_results_data(file_name)` | Export NVH results |
| `export_to_ansys_discovery(file_path)` | Export to Discovery Python script |
| `export_to_ansys_electronics_desktop(file_path)` | Export to Electronics Desktop VBS script |
| `geometry_export()` | Export geometry to DXF file |

## Results

| Method | Description |
|--------|-------------|
| `load_results(solution_type)` | Load output results from EMagnetic or Thermal |
| `save_results(solution_type)` | Save output results from EMagnetic or Thermal |
| `load_fea_result(file_path, solution_number)` | Load existing FEA solution |

## Duty Cycle / Load Profile

| Method | Description |
|--------|-------------|
| `clear_duty_cycle()` | Clear duty cycle in lab and thermal contexts |
| `load_duty_cycle(file_name)` | Load duty cycle from DAT file |
| `save_duty_cycle(file_path)` | Save duty cycle to DAT file |
| `load_custom_drive_cycle(file_path)` | Load custom waveform from file |

## Material

| Method | Description |
|--------|-------------|
| `load_magnetisation_curves(file_path)` | Load magnetization curves from text file |
| `save_magnetisation_curves(file_name)` | Save magnetisation curves to text file |

## Messages & UI

| Method | Description |
|--------|-------------|
| `clear_message_log()` | Clear message log file |
| `get_messages(num_messages)` | Get last N messages from history |
| `quit()` | Quit Motor-CAD |
| `set_free()` | Free the Motor-CAD instance |
| `get_licence()` / `get_license()` | Check if license is available |
| `create_report(file_path, template_file_path)` | Create Word report |

## Winding

| Method | Description |
|--------|-------------|
| `load_winding_pattern(file_path)` | Load winding pattern from text file |
| `save_winding_pattern(file_path)` | Save winding pattern to file |

## NVH

| Method | Description |
|--------|-------------|
| `load_nvh_custom_response(file_name)` | Load custom noise response functions |
| `save_nvh_custom_response(file_name)` | Save custom noise response functions |

## Related Pages

- [[motorcad/api/calculations-methods]] — Calculation methods
- [[motorcad/api/graphs-methods]] — Graph retrieval
- [[motorcad/api/geometry-methods]] — Geometry methods
