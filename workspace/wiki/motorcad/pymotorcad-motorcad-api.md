---
type: motorcad_api
title: PyMotorCAD MotorCAD Constructor API
source: ansys-motorcad-core documentation
tags: [motorcad, pymotorcad, constructor, connection, api]
aliases: [MotorCAD constructor, pymotorcad connection]
---

# PyMotorCAD MotorCAD Constructor API

## Overview

The `MotorCAD()` constructor establishes a connection to a Motor-CAD instance. It is the primary entry point for all PyMotorCAD scripts.

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
```

## Constructor Signature

```python
pymotorcad.MotorCAD(
    port=None,
    open_new_instance=True,
    enable_exceptions=True,
    enable_success_variable=False,
    reuse_parallel_instances=False,
    keep_instance_open=False,
    url=None,
    use_blackbox_licence=False,
)
```

## Parameters

### port

| Type | Default |
|------|---------|
| int | None |

Port number for connecting to an existing Motor-CAD instance. If None, a new instance is launched or an available instance is reused.

```python
mc = pymotorcad.MotorCAD(port=50000)
```

### open_new_instance

| Type | Default |
|------|---------|
| bool | True |

If True, launches a new Motor-CAD instance. If False, attempts to connect to an existing instance.

```python
# Launch new instance
mc = pymotorcad.MotorCAD(open_new_instance=True)

# Connect to existing instance
mc = pymotorcad.MotorCAD(open_new_instance=False)
```

### enable_exceptions

| Type | Default |
|------|---------|
| bool | True |

If True, Motor-CAD errors raise Python exceptions. If False, errors are returned as status codes.

```python
mc = pymotorcad.MotorCAD(enable_exceptions=True)
```

### enable_success_variable

| Type | Default |
|------|---------|
| bool | False |

If True, enables checking a success variable after each operation to verify completion.

```python
mc = pymotorcad.MotorCAD(enable_success_variable=True)
```

### reuse_parallel_instances

| Type | Default |
|------|---------|
| bool | False |

If True, allows reusing Motor-CAD instances across parallel script runs for efficiency.

```python
mc = pymotorcad.MotorCAD(reuse_parallel_instances=True)
```

### keep_instance_open

| Type | Default |
|------|---------|
| bool | False |

If True, the Motor-CAD instance remains open after the script finishes. Useful for inspecting results in the GUI.

```python
mc = pymotorcad.MotorCAD(keep_instance_open=True)
```

### url

| Type | Default |
|------|---------|
| str | None |

URL for connecting to a remote Motor-CAD instance. Use when Motor-CAD runs on a different machine.

```python
mc = pymotorcad.MotorCAD(url="http://remote-server:50000")
```

### use_blackbox_licence

| Type | Default |
|------|---------|
| bool | False |

If True, uses a blackbox licence which does not require a GUI display. Ideal for headless/CI environments.

```python
mc = pymotorcad.MotorCAD(use_blackbox_licence=True)
```

## Typical Connection Patterns

### Basic connection (GUI visible)

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD()
mc.load_from_file(r"D:\models\SRM_1.mot")
```

### Headless with blackbox licence

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD(
    open_new_instance=True,
    use_blackbox_licence=True,
    keep_instance_open=False,
)
mc.set_variable("MessageDisplayState", 2)
mc.load_from_file(r"D:\models\SRM_1.mot")
```

### Reusing existing instance

```python
import ansys.motorcad.core as pymotorcad

mc = pymotorcad.MotorCAD(open_new_instance=False)
```

## Cross-References

- [[pymotorcad-getting-started]] — Installation and verification
- [[pymotorcad-general-api]] — File I/O, results, and export methods
- [[pymotorcad-compatibility-api]] — Legacy ActiveX compatibility
- [[pymotorcad-setup]] — Registration and parameter names

## Tags

#motorcad #pymotorcad #constructor #connection #api #blackbox #headless
