---
title: Motor-CAD Result Fields
created: 2026-07-05
---

# Motor-CAD Result Fields

## Summary

Key output metrics extracted from Motor-CAD electromagnetic analysis.

## Performance metrics

| Metric | Unit | Description |
|--------|------|-------------|
| Torque | Nm | Average electromagnetic torque |
| Efficiency | % | Ratio of output mechanical power to input electrical power |
| Power factor | — | cos(φ), ratio of real to apparent power |
| Speed | rpm | Rotational speed |
| Output power | kW | Mechanical output power |

## Inductance parameters

| Metric | Unit | Description |
|--------|------|-------------|
| Ld | H | d-axis inductance |
| Lq | H | q-axis inductance |
| Saliency | — | Lq / Ld ratio (high for SynRM, >5 is good) |

## Loss breakdown

| Metric | Unit | Description |
|--------|------|-------------|
| Iron loss | W | Core losses (hysteresis + eddy current) |
| Copper loss | W | Winding resistive losses |
| Magnet loss | W | Eddy current loss in PMs (PMaSynRM) |
| Mechanical loss | W | Friction + windage |

## Result extraction

In PyMotorCAD, after running the magnetic context:

```python
torque = mc.get_variable("Torque")
efficiency = mc.get_variable("Efficiency")
power_factor = mc.get_variable("Power Factor")
```

## Related

- [[motorcad/workflow]]
- [[motorcad/parameters]]
