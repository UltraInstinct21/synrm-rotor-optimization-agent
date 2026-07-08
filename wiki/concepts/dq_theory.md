---
type: concept
name: DQ Theory
aliases: [d-q reference frame, Park transformation]
motor_types: [SynRM, PMSM, IPMSM, PMaSynRM]
topics: [control, modeling, reference_frame]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md"]
related_equations: ["equations/torque_synrm"]
related_motorcad_variables: []
confidence: Verified
---

# DQ Theory (d-q Reference Frame)

## Definition

A mathematical transformation that converts three-phase AC quantities (voltages, currents, fluxes) into a rotating reference frame aligned with the rotor, producing DC-like quantities for analysis and control.

## Why It Matters

The d-q frame is the standard model for SynRM analysis and control. It simplifies:
- Torque expression
- Current control (FOC)
- Inductance characterization
- Loss calculation

## Physics

The Park transformation rotates the reference frame at electrical rotor speed $\omega_e$:

- **d-axis**: Aligned with minimum reluctance path (maximum inductance $L_d$)
- **q-axis**: 90° electrical ahead (maximum reluctance, minimum inductance $L_q$)

For SynRM (no rotor excitation):

$$V_{ds} = r_s I_{ds} + \frac{d\lambda_{ds}}{dt} - \omega_e \lambda_{qs}$$

$$V_{qs} = r_s I_{qs} + \frac{d\lambda_{qs}}{dt} + \omega_e \lambda_{ds}$$

Where:
$$\lambda_{ds} = L_d I_{ds}, \quad \lambda_{qs} = L_q I_{qs}$$

## Key Relationships

- $L_d > L_q$ in SynRM (d-axis is low-reluctance)
- Torque depends on $(L_d - L_q)$ and current angle
- Optimal current angle depends on speed and voltage limit

## Design Impact

- $L_d$ and $L_q$ are the primary design targets
- Saturation causes $L_d$ and $L_q$ to vary with current level
- Cross-coupling between d and q axes affects control

## MotorCAD Mapping

MotorCAD uses d-q framework for electromagnetic analysis:
- d-axis and q-axis inductances
- d-axis and q-axis currents
- Current angle from d-axis

## Sources

- [[research/papers/nagarkar_optimized_rotor_synrm]]
- [[references/boldea]]

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/reluctance_torque]]
- [[equations/torque_synrm]]
- [[topologies/synrm]]
