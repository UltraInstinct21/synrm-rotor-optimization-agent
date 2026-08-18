---
title: Motor-CAD Parameters
created: 2026-07-05
---

# Motor-CAD Parameters

## Summary

Reference for key Motor-CAD parameters used in SynRM / PMaSynRM design.

## Geometry parameters

| Parameter | Description | Typical range |
|-----------|-------------|---------------|
| Stack length | Lamination stack length | 100–300 mm |
| Stator OD | Outer diameter | 200–400 mm |
| Rotor OD | Outer diameter | stator OD - airgap |
| Airgap length | Mechanical airgap | 0.3–0.8 mm |
| Number of poles | Pole count | 4, 6 |
| Number of stator slots | Slot count | 36, 48, 72 |
| Barrier layers | Number of flux barrier layers | 3–5 |

## Winding parameters

| Parameter | Description |
|-----------|-------------|
| Turns per coil | Number of turns |
| Parallel paths | Number of parallel winding paths |
| Fill factor | Copper fill factor |
| Wire diameter | Conductor diameter |

## Rating

| Parameter | Description |
|-----------|-------------|
| Rated power | Output power (e.g., 45 kW) |
| Rated speed | Base speed (e.g., 3000 rpm) |
| Rated torque | T = P / ω (e.g., 143 Nm at 45 kW, 3000 rpm) |
| DC bus voltage | Inverter DC link voltage |
| Current density | Typically 5–8 A/mm² |

## Related

- [[motorcad/parameter_database/index|Complete Motor-CAD Parameter Database (13,004 Parameters)]]
- [[motorcad/workflow]]
