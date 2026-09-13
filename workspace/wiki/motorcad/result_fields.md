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

## Verified common parameters (exempt from pre-search mandate)

Exact Motor-CAD variable strings confirmed against the parameter database
(`parameter_database/parameters/<Name>.md` sheets and category listings) or the
code sample above. These may be used directly in scripts WITHOUT searching the
parameter database first. Any variable NOT listed here must still be verified
via a parameter-database search before use.

| Variable | Type | Source |
|----------|------|--------|
| Torque | output | code sample above |
| Efficiency | output | code sample above |
| Power Factor | output | code sample above |
| ShaftTorque | output | parameters/ShaftTorque.md, Magnetics category |
| InputPower | output | parameters/InputPower.md, Magnetics category |
| OutputPower | output | parameters/OutputPower.md, Magnetics category |
| DCBusVoltage | input/output | parameters/DCBusVoltage.md, Magnetics category |
| PhaseCurrent | output | parameters/PhaseCurrent.md, Magnetics category |
| LineLineVoltage | parameter | parameters/LineLineVoltage.md |
| StatorIronLoss_Total | output | parameters/StatorIronLoss_Total.md |
| RotorIronLoss_Total | output | parameters/RotorIronLoss_Total.md |

## Related

- [[motorcad/workflow]]
- [[motorcad/parameters]]
