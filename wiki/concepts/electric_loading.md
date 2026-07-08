---
type: concept
name: Electric Loading
aliases: [ampere-conductor density]
motor_types: [SynRM, PMSM, IPMSM]
topics: [current_density, winding, sizing]
source_pages: []
related_equations: ["equations/current_density", "equations/d2l_sizing"]
related_motorcad_variables: []
confidence: Verified
---

# Electric Loading

## Definition

The linear current density along the airgap surface, defined as ampere-conductors per unit length:

$$A = \frac{m N_{ph} I_s}{\pi D_{is}}$$

Where:
- $m$ = number of phases
- $N_{ph}$ = series turns per phase
- $I_s$ = RMS phase current
- $D_{is}$ = stator inner diameter

## Why It Matters

Electric loading combined with magnetic loading determines torque:

$$T = \frac{\pi}{4} D_{is}^2 L_{sk} \cdot B_{avg} \cdot A \cdot k_w$$

Higher electric loading → higher torque, but limited by:
- Copper losses ($I^2R$)
- Thermal limits
- Slot fill factor

## Physics

Electric loading represents how many ampere-conductors are packed along the airgap. It depends on:
- Slot count and geometry
- Winding pattern (distributed/concentrated)
- Current density in conductors
- Slot fill factor

Typical values:
- Low-performance: 20–40 kA/m
- Medium-performance: 40–70 kA/m
- High-performance: 70–120 kA/m

## Design Impact

- Higher $A$ → higher torque density
- Limited by thermal management
- Interacts with slot design and winding type
- Current density $J$ and electric loading $A$ are related but distinct

## MotorCAD Mapping

MotorCAD computes electric loading from winding and current settings. Key variables:
- Phase current
- Turns per phase
- Slot geometry

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/magnetic_loading]]
- [[concepts/saturation]]
- [[equations/current_density]]
- [[equations/d2l_sizing]]
- [[design_guidelines/current_density_limits]]
- [[design_guidelines/slot_selection]]
