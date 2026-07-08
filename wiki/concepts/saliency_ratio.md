---
type: concept
name: Saliency Ratio
aliases: [Ld/Lq ratio, inductance ratio]
motor_types: [SynRM, IPMSM, PMaSynRM]
topics: [inductance, torque_production, power_factor]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md"]
related_equations: ["equations/saliency_ratio_eq", "equations/torque_synrm"]
related_motorcad_variables: []
confidence: Verified
---

# Saliency Ratio

## Definition

The saliency ratio is the ratio of d-axis inductance to q-axis inductance:

$$\xi = \frac{L_d}{L_q}$$

See [[equations/saliency_ratio_eq]].

## Why It Matters

The saliency ratio is the single most important figure of merit for reluctance-based torque production. It directly determines:

- **Torque density**: Higher saliency → higher reluctance torque for the same current
- **Power factor**: Higher saliency → higher power factor
- **Current angle**: Optimal current angle depends on saliency

## Physics

In a SynRM, the d-axis path passes through iron (low reluctance, high inductance $L_d$), while the q-axis path crosses flux barriers (high reluctance, low inductance $L_q$).

The difference $(L_d - L_q)$ creates the anisotropy that produces reluctance torque.

## Key Relationships

- Reluctance torque $\propto (L_d - L_q) I_s^2 \sin(2\gamma)$ — see [[equations/torque_synrm]]
- Power factor improves with saliency — see [[concepts/power_factor]]
- Optimal current angle: $\gamma_{opt} = \frac{1}{2} \arctan\left(\frac{V_s}{\omega_s L_q I_s}\right)$

## Design Impact

| Saliency Ratio | Torque | Power Factor | Application |
|----------------|--------|--------------|-------------|
| 2–3 | Low | Poor | Rarely useful |
| 3–5 | Moderate | Moderate | Basic industrial |
| 5–8 | Good | Good | High-performance |
| >8 | Excellent | Very good | Optimized / PM-assisted |

Achieving saliency > 6 in practice is difficult due to:
- Magnetic saturation (reduces $L_d$ more than $L_q$)
- Flux leakage through bridges and ribs
- Cross-coupling between d and q axes

## MotorCAD Mapping

MotorCAD computes $L_d$ and $L_q$ through electromagnetic simulation. Relevant variables:
- `MotorCAD variables Ld, Lq` — inductance outputs
- `MotorCAD variables Id, Iq` — current components

## Sources

- [[research/papers/nagarkar_optimized_rotor_synrm]]
- [[research/papers/synrm_drive_design]]
- [[research/papers/overview_high_efficiency_synrm]]
- [[references/boldea]]

## Related Pages

- [[concepts/reluctance_torque]]
- [[concepts/power_factor]]
- [[concepts/dq_theory]]
- [[equations/torque_synrm]]
- [[equations/saliency_ratio_eq]]
- [[design_guidelines/barrier_design]]
- [[topologies/synrm]]
