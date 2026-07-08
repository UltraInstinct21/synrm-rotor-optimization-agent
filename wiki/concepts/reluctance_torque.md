---
type: concept
name: Reluctance Torque
aliases: []
motor_types: [SynRM, IPMSM, PMaSynRM]
topics: [torque_production, magnetic_anisotropy]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md"]
related_equations: ["equations/torque_synrm"]
related_motorcad_variables: []
confidence: Verified
---

# Reluctance Torque

## Definition

Torque produced by the tendency of a magnetic body to align with the minimum-reluctance path in a magnetic field. In SynRM, this is the sole torque-producing mechanism.

## Why It Matters

Reluctance torque is the fundamental operating principle of SynRM. Understanding it is essential for rotor design optimization.

## Physics

When current flows in the stator, it creates a magnetic field. The rotor, having different reluctances along d and q axes, experiences a torque that tries to align the low-reluctance (d-axis) path with the stator field.

The torque expression:

$$T_{rel} = \frac{3}{2} \frac{P}{2} (L_d - L_q) I_d I_q$$

Or equivalently with current angle $\gamma$ (from d-axis):

$$T_{rel} = \frac{3}{4} \frac{P}{2} (L_d - L_q) I_s^2 \sin(2\gamma)$$

## Key Relationships

- Maximum at $\gamma = 45°$ (when $L_d \gg L_q$)
- Proportional to $(L_d - L_q)$ — saliency ratio matters
- Proportional to $I_s^2$ — current squared
- Zero when $L_d = L_q$ (isotropic rotor)

## Design Impact

- Rotor barrier design directly controls $(L_d - L_q)$
- More barriers → better saliency → more reluctance torque
- Saturation reduces effective $(L_d - L_q)$ at high currents
- Bridge and rib thickness affect flux leakage and saliency

## MotorCAD Mapping

MotorCAD computes reluctance torque through electromagnetic FEA. The torque decomposition into alignment and reluctance components is available in results.

## Sources

- [[research/papers/nagarkar_optimized_rotor_synrm]]
- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/dq_theory]]
- [[equations/torque_synrm]]
- [[design_guidelines/barrier_design]]
- [[topologies/synrm]]
