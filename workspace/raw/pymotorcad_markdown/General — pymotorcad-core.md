## General

| clear_duty_cycle ()                             | Clear the duty cycle in both the lab and<br>thermal contexts.                       |
|-------------------------------------------------|-------------------------------------------------------------------------------------|
| clear_message_log ()                            | Clear the message log file for the model.                                           |
| create_report (file_path, template_file_path)   | Create a Word report of the report tree<br>structure.                               |
| download_mot_file (file_path)                   | Download the current .mot file from Motor<br>CAD and write it to a local directory. |
| export_force_animation (animation, file_name)   | Export a force animation to a GIF file.                                             |
| export_matrices (directory_path)                | Export the resistance, power, and capacitance<br>matrices to files.                 |
| export_multi_force_data (file_name)             | Export calculated multiforce data to a file.                                        |
| export_nvh_results_data (file_name)             | Export NVH results data to a file.                                                  |
| export_results (solution_type, file_path)       | Export results from a solution to a CSV file.                                       |
| export_to_ansys_discovery (file_path)           | Export the model to a Python script file that<br>can be run in Ansys Discovery.     |
| export_to_ansys_electronics_desktop (file_path) | Export the model to a VBS script file that can<br>run in Ansys Electronics Desktop. |
| geometry_export ()                              | Export the geometry to the file specified in the<br>DXFFileName parameter.          |
| get_licence ()                                  | Check if a license is available for the current<br>context and machine type.        |
| get_license ()                                  | Check if a license is available for the current<br>context and machine type.        |
| get_messages (num_messages)                     | Get a list of the last N<br>messages from the<br>message history.                   |
| load_custom_drive_cycle (file_path)             | Load a custom waveform from a file.                                                 |
| load_duty_cycle (file_name)                     | Load a duty cycle from a DAT file.                                                  |

| load_dxf_file (file_name)                    | Load a DXF geometry file.                                                                  |
|----------------------------------------------|--------------------------------------------------------------------------------------------|
| load_fea_result (file_path, solution_number) | Load an existing FEA solution to allow viewing<br>of FEA results.                          |
| load_from_file (mot_file)                    | Load a MOT file into the Motor-CAD instance.                                               |
| load_magnetisation_curves (file_path)        | Load the magnetization curves from a text file.                                            |
| load_nvh_custom_response (file_name)         | Load custom characteristic noise response<br>functions from space/tab delimited text file. |
| load_report_structure (file_path)            | Load the tree structure of the report from a<br>file.                                      |
| load_report_tree ()                          | Load the report with the tree structure of the<br>modules and components.                  |
| load_results (solution_type)                 | Load the output results from an "EMagnetic"<br>or<br>"Thermal" solution.                   |
| load_template (template_name)                | Load a motor template.                                                                     |
| load_winding_pattern (file_path)             | Load the winding pattern from a text file.                                                 |
| quit ()                                      | Quit Motor-CAD.                                                                            |
| save_duty_cycle (file_path)                  | Save the duty cycle to a DAT file.                                                         |
| save_magnetisation_curves (file_name)        | Save the magnetisation curves to a text file.                                              |
| save_nvh_custom_response (file_name)         | Save custom characteristic noise response<br>functions to tab delimited text file.         |
| save_results (solution_type)                 | Save the output results from an "EMagnetic"<br>or<br>"Thermal" solution.                   |
| save_template (template_file_name, name,)    | Save the template to an MTT template file.                                                 |
| save_to_file (mot_file)                      | Save the MOT file.                                                                         |
| save_winding_pattern (file_path)             | Save the winding pattern to a file.                                                        |
|                                              |                                                                                            |

| set_free ()                 | Free the Motor-CAD instance.                                      |  |
|-----------------------------|-------------------------------------------------------------------|--|
| upload_mot_file (file_path) | Upload a .mot file to Motor-CAD instance from<br>local directory. |  |

© Copyright (c) 2026 ANSYS, Inc. All rights reserved.

Created using [Sphinx](https://www.sphinx-doc.org/) 8.1.3.

Built with the Ansys [Sphinx](https://sphinxdocs.ansys.com/version/stable/index.html) Theme 1.3.3. Last updated on April 15, 2026