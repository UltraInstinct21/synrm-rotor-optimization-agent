---
type: equation
name: SynRM Electromagnetic Torque
aliases: [reluctance torque equation]
motor_types: [SynRM]
topics: [torque, dq_model]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md"]
related_concepts: ["concepts/reluctance_torque", "concepts/dq_theory", "concepts/saliency_ratio"]
related_motorcad_variables: []
confidence: Verified
verification_status: Verified
---

# SynRM Electromagnetic Torque

## Statement

$$T_e = \frac{3}{2} \frac{P}{2} (L_d - L_q) I_d I_q$$

Or equivalently using current angle $\gamma$ (measured from d-axis):

$$T_e = \frac{3}{4} \frac{P}{2} (L_d - L_q) I_s^2 \sin(2\gamma)$$

## Original Notation

From Nagarkar et al.:

$$T_e = \frac{3}{2} \frac{P}{2} (\lambda_{ds} I_{qs} - \lambda_{qs} I_{ds})$$

With $\lambda_{ds} = L_d I_{ds}$ and $\lambda_{qs} = L_q I_{qs}$, this reduces to the form above.

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $T_e$ | Electromagnetic torque | N·m |
| $P$ | Number of poles | — |
| $L_d$ | d-axis inductance | H |
| $L_q$ | q-axis inductance | H |
| $I_d$ | d-axis current | A |
| $I_q$ | q-axis current | A |
| $I_s$ | RMS phase current magnitude | A |
| $\gamma$ | Current angle from d-axis | rad (or °) |

## Assumptions

- Steady-state operation
- Sinusoidal MMF distribution
- No rotor excitation (pure reluctance)
- Magnetic co-energy variation averages to zero over one rotation
- Linear or nonlinear magnetic circuit (equation form holds; $L_d$, $L_q$ become functions of current under saturation)

## Interpretation

The torque is proportional to:
1. The difference $(L_d - L_q)$ — magnetic anisotropy
2. The product $I_d I_q$ — or equivalently $I_s^2 \sin(2\gamma)$

Maximum torque occurs at $\gamma = 45°$ when $L_d$ and $L_q$ are constant. Under saturation, the optimal angle shifts.

## Design Relevance

- Maximize $(L_d - L_q)$ through rotor barrier design
- Control current angle for maximum torque or maximum efficiency
- Saturation reduces effective $(L_d - L_q)$ at high currents
- This equation is the basis for all SynRM rotor optimization

## MotorCAD Mapping

MotorCAD computes torque through FEA. The analytical form above is used for:
- Initial sizing
- Current angle optimization
- Loss model formulation

## Sources

- Nagarkar et al., "An Optimized Rotor Design of SynRM for Improved Torque Characteristics"
- Boldea, "Synchronous Reluctance Machines and Drives"
- Pyrhonen et al., "Design of Rotating Electrical Machines"

## Related Pages

- [[concepts/reluctance_torque]]
- [[concepts/saliency_ratio]]
- [[concepts/dq_theory]]
- [[equations/saliency_ratio_eq]]
- [[topologies/synrm]]
