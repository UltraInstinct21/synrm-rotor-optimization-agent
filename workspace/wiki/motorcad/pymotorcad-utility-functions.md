---
type: pymotorcad_api
title: "PyMotorCAD Utility Functions"
source: "PyMotorCAD Official Documentation"
tags:
  - pymotorcad
  - motorcad
  - utility
  - api
  - configuration
  - connection
aliases:
  - pymotorcad_utils
  - motorcad_utilities
related_pages:
  - "[[pymotorcad-motorcad-api]]"
  - "[[pymotorcad-getting-started]]"
  - "[[pymotorcad-connection-setup]]"
confidence: verified
---

# PyMotorCAD Utility Functions

## Overview

Utility functions in PyMotorCAD provide infrastructure-level configuration for connecting to and controlling Motor-CAD instances. These functions set up the communication layer between the Python script and the Motor-CAD application before any modeling or calculation work begins.

---

## `set_default_instance(port)`

### Purpose

Sets the default Motor-CAD instance that all subsequent PyMotorCAD API calls will target. This is essential when multiple Motor-CAD instances are running simultaneously and you need to direct commands to a specific one.

### Signature

```python
set_default_instance(port: int) -> None
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `port` | `int` | The port number of the target Motor-CAD instance |

### Description

When Motor-CAD is launched, it binds to a specific communication port. By default, PyMotorCAD targets the most recently opened instance. Use `set_default_instance()` to explicitly redirect all API calls to a specific instance identified by its port.

This is particularly useful in batch processing workflows where multiple Motor-CAD models are being evaluated in parallel or sequentially across different instances.

### Example

```python
import ansys.motorcad.core as pymotorcad

# Launch two Motor-CAD instances
mc1 = pymotorcad.MotorCAD()
mc2 = pymotorcad.MotorCAD()

# mc1 and mc2 are on different ports
# Set default to mc1's port
pymotorcad.set_default_instance(mc1._port)

# Now all top-level API calls target mc1
```

### Use Cases

- Multi-model parallel evaluation
- Batch optimization loops across separate instances
- Switching between reference model and design candidate
- Debugging by isolating instance-specific behavior

### Notes

- The port is automatically assigned when a `MotorCAD()` object is created
- Access the port via `mc._port` on any active MotorCAD instance
- This function sets the **global default** — it affects all subsequent calls unless an explicit instance is referenced

---

## `set_motorcad_exe(exe_location)`

### Purpose

Configures the file path to the Motor-CAD executable that PyMotorCAD will use when launching new instances.

### Signature

```python
set_motorcad_exe(exe_location: str) -> None
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `exe_location` | `str` | Full file path to the Motor-CAD `.exe` file |

### Description

PyMotorCAD needs to know where the Motor-CAD executable is installed in order to launch new instances. This function sets that path globally for the current Python session. If not set, PyMotorCAD attempts to find Motor-CAD via environment variables or default installation paths.

This function must be called **before** creating any `MotorCAD()` instances if the default detection fails.

### Example

```python
import ansys.motorcad.core as pymotorcad

# Set the Motor-CAD executable path
pymotorcad.set_motorcad_exe(
    r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"
)

# Now launching instances will use this executable
mc = pymotorcad.MotorCAD()
```

### Typical Installation Paths

| Version | Default Path |
|---|---|
| 2025.1.1 | `C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe` |
| 2024.2 | `C:\Ansys_Motor-CAD\2024_2\Motor-CAD_2024_2.exe` |

### Use Cases

- Non-standard Motor-CAD installation locations
- Multiple Motor-CAD versions coexisting on one machine
- CI/CD environments where the path is injected at runtime
- Virtual machine or containerized deployments

### Notes

- The path must point to the `.exe` file, not the installation directory
- Use raw strings (`r"..."`) on Windows to avoid escape character issues
- This is a **session-level** setting — it persists until changed or the Python session ends
- If the path is invalid, `MotorCAD()` constructor will raise an error when attempting to launch

---

## `set_server_ip(ip)`

### Purpose

Configures the IP address of a remote machine where Motor-CAD is running or should be launched, enabling remote execution of Motor-CAD from a local Python script.

### Signature

```python
set_server_ip(ip: str) -> None
```

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `ip` | `str` | IP address or hostname of the remote Motor-CAD server |

### Description

PyMotorCAD supports remote execution where the Motor-CAD application runs on a different machine than the Python script. This function sets the target server IP so that subsequent `MotorCAD()` instances connect to the remote Motor-CAD rather than launching a local one.

This enables:

- Running heavy Motor-CAD simulations on dedicated compute servers
- Centralized Motor-CAD license management
- Remote batch processing workflows
- HPC cluster integration

### Example

```python
import ansys.motorcad.core as pymotorcad

# Connect to Motor-CAD running on a remote server
pymotorcad.set_server_ip("192.168.1.100")

# Launch (or connect to) a remote Motor-CAD instance
mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\my_motor.mot")
```

### Example — Local + Remote in Same Script

```python
import ansys.motorcad.core as pymotorcad

# Local instance for quick checks
mc_local = pymotorcad.MotorCAD()

# Switch to remote for heavy computation
pymotorcad.set_server_ip("10.0.0.50")
mc_remote = pymotorcad.MotorCAD()

# Use mc_local for lightweight ops, mc_remote for EMag runs
```

### Use Cases

- Remote simulation servers
- Shared license server environments
- Multi-machine optimization workflows
- Separating GUI interaction (local) from computation (remote)

### Notes

- The remote machine must have Motor-CAD installed and accessible
- Network connectivity and firewall rules must allow the communication port
- This is a **session-level** setting
- Combining `set_server_ip()` with `set_default_instance()` allows full control over routing

---

## Execution Order and Dependencies

When setting up a PyMotorCAD workflow, the utility functions should generally be called in this order:

```python
import ansys.motorcad.core as pymotorcad

# 1. Set executable path (if non-default location)
pymotorcad.set_motorcad_exe(r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe")

# 2. Set remote server (if applicable)
pymotorcad.set_server_ip("192.168.1.100")

# 3. Create Motor-CAD instance
mc = pymotorcad.MotorCAD()

# 4. Set default instance (if multiple instances)
pymotorcad.set_default_instance(mc._port)

# 5. Proceed with modeling and calculations
mc.load_from_file(r"D:\models\my_motor.mot")
```

---

## Relationship to `MotorCAD()` Constructor

The utility functions configure the **environment** in which `MotorCAD()` objects are created. The `MotorCAD()` constructor itself accepts optional parameters that override or complement these global settings:

```python
mc = pymotorcad.MotorCAD(
    open_new_instance=True,       # Force new instance
    use_blackbox_licence=False,   # License type
    keep_instance_open=True,      # Don't close on script exit
)
```

The utility functions set defaults; the constructor can override per-instance.

---

## Error Handling

All utility functions are session-level and do not raise exceptions for invalid inputs at call time. Errors typically manifest when `MotorCAD()` is subsequently instantiated:

| Scenario | Error Type | When |
|---|---|---|
| Invalid exe path | `FileNotFoundError` | At `MotorCAD()` construction |
| Unreachable server | `ConnectionError` | At `MotorCAD()` construction |
| Invalid port for default instance | `RuntimeError` | At next API call |

### Defensive Pattern

```python
import os
import ansys.motorcad.core as pymotorcad

exe_path = r"C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe"

if not os.path.exists(exe_path):
    raise FileNotFoundError(f"Motor-CAD executable not found: {exe_path}")

pymotorcad.set_motorcad_exe(exe_path)
mc = pymotorcad.MotorCAD()
```

---

## Cross-References

- [[pymotorcad-motorcad-api]] — Full MotorCAD class API reference
- [[pymotorcad-getting-started]] — Installation and first-run setup guide
- [[pymotorcad-connection-setup]] — Detailed connection configuration
- [[pymotorcad-workflows]] — Common workflow patterns

---

## Tags

#pymotorcad #motorcad #api #utility #configuration #connection #setup #infrastructure
