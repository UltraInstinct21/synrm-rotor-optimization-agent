---
type: equation
name: D²L Sizing Equation
aliases: [sizing equation, output equation]
motor_types: [SynRM, PMSM, IPMSM]
topics: [sizing, preliminary_design]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md"]
related_concepts: ["concepts/magnetic_loading", "concepts/electric_loading"]
related_motorcad_variables: []
confidence: Verified
verification_status: Verified
---

# D²L Sizing Equation

## Statement

$$T = \frac{\pi}{4} D_{is}^2 L_{sk} \cdot B_{avg} \cdot A \cdot k_w \cdot \sqrt{2}$$

Or in terms of output power:

$$P_{out} = \frac{\pi^2}{120} n_s D_{is}^2 L_{sk} \cdot B_{avg} \cdot A \cdot k_w \cdot \eta$$

## Original Notation

From Nagarkar et al., the sizing expression uses $D_o^3 L_{sk}$ form with the ratio $D_{is}/D_o$.

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $T$ | Electromagnetic torque | N·m |
| $D_{is}$ | Stator inner diameter | m |
| $L_{sk}$ | Stack length | m |
| $B_{avg}$ | Average airgap flux density | T |
| $A$ | Electric loading | A/m |
| $k_w$ | Winding factor | — |
| $n_s$ | Synchronous speed | rpm |
| $\eta$ | Efficiency | — |

## Assumptions

- Steady-state, sinusoidal MMF
- Uniform flux distribution approximation
- Linear magnetic circuit (for preliminary sizing only)
- Applies to all rotating machine topologies

## Interpretation

The torque capability of a machine is proportional to the rotor volume $D_{is}^2 L_{sk}$, scaled by the product of magnetic loading ($B_{avg}$) and electric loading ($A$).

This is the fundamental sizing equation used in initial design to determine machine dimensions from specifications.

## Design Relevance

- Start with torque requirement → determine $D_{is}^2 L_{sk}$
- Choose $B_{avg}$ based on material limits and loss budget
- Choose $A$ based on thermal limits
- Select $D_{is}/L_{sk}$ ratio based on application constraints

Typical $D_{is}/L_{sk}$ ratios:
- High-speed: 0.3–0.5 (long and thin)
- General purpose: 0.5–1.0
- High-torque: 1.0–2.0 (short and wide)

## MotorCAD Mapping

MotorCAD uses these dimensions as input geometry:
- Stator inner diameter
- Stack length
- These are primary variables in model setup

## Sources

- Nagarkar et al., "An Optimized Rotor Design of SynRM"
- Boldea, "Synchronous Reluctance Machines and Drives"
- Pyrhonen et al., "Design of Rotating Electrical Machines"

## Related Pages

- [[concepts/magnetic_loading]]
- [[concepts/electric_loading]]
- [[design_guidelines/stack_length]]
- [[design_guidelines/rotor_diameter]]
- [[topologies/synrm]]
