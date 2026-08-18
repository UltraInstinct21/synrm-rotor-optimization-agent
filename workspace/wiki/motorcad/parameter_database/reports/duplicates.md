---
type: motorcad_parameter_report
report_name: duplicates
duplicate_count: 1
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Duplicate Parameter Resolution Report

## Overview
A total of **1** parameter names were found with multiple entries in `ActiveXParameters.xlsx`.

## Duplicate Resolution Rules Applied
1. Unique parameter pages were created for each unique Automation Name.
2. Metadata from duplicate rows was merged.
3. Primary category and data type were assigned from the first occurrence, and alternate categories/data types were noted.
4. Conflict details were preserved in both the parameter page and this report.

## Duplicate Parameters Details

### Parameter: `Notes_Inlet_Stator_Duct_Contraction`
- **Row Numbers**: [11606, 12551]
- **Categories**: ['Through_Vent', 'Through Ventilation Model Data']
- **Data Types**: ['OleStr', 'String']
- **Descriptions**: ['Notes Inlet Stator Duct Contraction']
- **Resolution**: Merged 2 CSV rows (Numbers: [11606, 12551]). Alternate Categories: Through Ventilation Model Data. Alternate Data Types: String.
- **Parameter Page**: [[motorcad/parameter_database/parameters/Notes_Inlet_Stator_Duct_Contraction|Notes_Inlet_Stator_Duct_Contraction]]

