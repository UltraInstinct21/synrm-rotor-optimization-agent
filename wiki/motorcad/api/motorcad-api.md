---
type: motorcad_api
method_name: "MotorCAD()"
module: "ansys.motorcad.core"
source_files: ["MotorCAD API — pymotorcad-core.md"]
confidence: Verified
---

# MotorCAD API

## Signature

```python
MotorCAD(
    port=-1,
    open_new_instance=True,
    enable_exceptions=True,
    enable_success_variable=False,
    reuse_parallel_instances=False,
    keep_instance_open=False,
    url='',
    use_blackbox_licence=None
)
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `port` | int | -1 | Port for communication |
| `open_new_instance` | bool | True | Open new instance or connect to existing |
| `enable_exceptions` | bool | True | Show Motor-CAD errors as Python exceptions |
| `enable_success_variable` | bool | False | Methods return success variable (first in tuple) |
| `reuse_parallel_instances` | bool | False | Reuse instances in parallel (must free after use) |
| `keep_instance_open` | bool | False | Keep instance open after becoming free |
| `url` | str | "" | Full URL for connection to existing instance |
| `use_blackbox_licence` | bool | None | Consume blackbox licence (None = default behaviour) |

## Returns

`MotorCAD` object.

## Examples

```python
import ansys.motorcad.core as pymotorcad

# Standard usage - opens new instance
mc = pymotorcad.MotorCAD()

# Connect to existing instance
mc = pymotorcad.MotorCAD(open_new_instance=False)

# Keep instance open after script
mc = pymotorcad.MotorCAD(keep_instance_open=True)
```

## Related Pages

- [[motorcad/api/motorcad-compatibility-api]] — MotorCADCompatibility for ActiveX compatibility
- [[motorcad/api/motorcad-errors]] — MotorCADError
- [[motorcad/overview/getting-started]] — Installation
- [[motorcad/overview/motorcad-setup]] — Registration and parameter names
