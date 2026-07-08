---
type: equation
name: Saliency Ratio
aliases: [Ld/Lq ratio]
motor_types: [SynRM, IPMSM, PMaSynRM]
topics: [inductance, anisotropy]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md"]
related_concepts: ["concepts/saliency_ratio"]
related_motorcad_variables: []
confidence: Verified
verification_status: Verified
---

# Saliency Ratio

## Statement

$$\xi = \frac{L_d}{L_q}$$

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $\xi$ | Saliency ratio | — |
| $L_d$ | d-axis inductance | H |
| $L_q$ | q-axis inductance | H |

## Assumptions

- $L_d$ and $L_q$ are measured or computed at a specific operating point
- Values are current-dependent under saturation
- Cross-coupling effects are ignored in this simplified form

## Interpretation

$\xi > 1$ is required for reluctance torque production. Higher $\xi$ means:
- More reluctance torque for the same current
- Higher power factor
- Better utilization of magnetic anisotropy

## Design Relevance

The saliency ratio is the primary target of SynRM rotor optimization. All barrier design, bridge design, and rib design choices aim to maximize $\xi$ while maintaining mechanical integrity.

Practical limits:
- Air barriers only: $\xi$ ≈ 5–8
- PM-assisted: $\xi$ ≈ 8–15 (effective, including PM flux)

## MotorCAD Mapping

MotorCAD computes $L_d$ and $L_q$ from electromagnetic simulation. The ratio is derived from inductance results.

## Sources

- Nagarkar et al.
- Boldea

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/reluctance_torque]]
- [[equations/torque_synrm]]
- [[design_guidelines/barrier_design]]
- [[topologies/synrm]]
