---
type: motorcad_parameter_category
category_name: Scripting_Options
parameter_count: 8
source_file: D:/SRM/Agent/workspace/wiki/raw/ActiveXParameters.xlsx
---

# Category: Scripting_Options

## Overview
The **Scripting_Options** category contains **8** Motor-CAD automation parameters.

## Parameters in this Category

| Parameter Name | Input/Output | Data Type | Units | Description |
|---|---|---|---|---|
| [[motorcad/parameter_database/parameters/DisableSleep|DisableSleep]] | persistent | boolean | N/A | When true Motor-CAD will not allow computer to sleep |
| [[motorcad/parameter_database/parameters/OwnerProcessID|OwnerProcessID]] | persistent | integer | N/A | Process ID of the caller (if exists) of this instance of Motor-CAD |
| [[motorcad/parameter_database/parameters/ScriptAutoRun|ScriptAutoRun]] | i/p | integer | N/A | Automatically run the script before or during analysis |
| [[motorcad/parameter_database/parameters/ScriptAutoRun_PythonClasses|ScriptAutoRun_PythonClasses]] | i/p | integer | N/A | Automatically run the during analysis |
| [[motorcad/parameter_database/parameters/ScriptFileName|ScriptFileName]] | i/p | OleStr | N/A | The name of the script file |
| [[motorcad/parameter_database/parameters/ScriptFileName_Python|ScriptFileName_Python]] | i/p | OleStr | N/A | The name of the Python script file |
| [[motorcad/parameter_database/parameters/ScriptPythonFunctionType|ScriptPythonFunctionType]] | compatibility | integer | N/A | Run the script with new classes or old functions |
| [[motorcad/parameter_database/parameters/Scripting_Engine|Scripting_Engine]] | recommended | integer | N/A | Which Scripting Engine to use, Python (Default) or VBA |

## Navigation
- Back to [[motorcad/parameter_database/index|Parameter Database Index]]
