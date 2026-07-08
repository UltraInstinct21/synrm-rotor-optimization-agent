---
type: topology
name: Synchronous Reluctance Motor
aliases: [SynRM, SynRM, SYNCREL]
motor_types: [SynRM]
topics: [torque_production, rotor_design, barrier_geometry]
source_pages: ["raw/papers/"]
related_concepts: ["concepts/saliency_ratio", "concepts/reluctance_torque", "concepts/dq_theory"]
related_equations: ["equations/torque_synrm", "equations/saliency_ratio_eq"]
related_motorcad_variables: []
confidence: Verified
---

# Synchronous Reluctance Motor (SynRM)

## Operating Principle

The SynRM produces torque through magnetic anisotropy — the difference in reluctance between the d-axis and q-axis paths in the rotor. No permanent magnets or rotor windings are required.

The rotor contains flux barriers (air slots) that create high-reluctance paths along the q-axis while maintaining low-reluctance paths along the d-axis through iron.

## Torque Production Mechanism

Electromagnetic torque is produced by the difference in d-axis and q-axis inductances:

$$T_e = \frac{3}{2} \frac{P}{2} (L_d - L_q) I_s^2 \sin(2\gamma)$$

Where:
- $L_d$ = d-axis inductance (high, low-reluctance path)
- $L_q$ = q-axis inductance (high-reluctance path through barriers)
- $\gamma$ = current angle from d-axis
- $P$ = number of poles

See [[equations/torque_synrm]] for full derivation.

## Key Design Variables

| Variable | Effect |
|----------|--------|
| [[design_guidelines/barrier_design\|Barrier count and shape]] | Controls Ld/Lq ratio (saliency) |
| [[design_guidelines/rib_design\|Rib thickness]] | Mechanical integrity vs saturation |
| [[design_guidelines/bridge_design\|Bridge thickness]] | Mechanical integrity vs flux leakage |
| [[design_guidelines/airgap\|Airgap]] | Affects inductance and torque |
| [[design_guidelines/stack_length\|Stack length]] | Scales torque linearly |
| [[design_guidelines/rotor_diameter\|Rotor diameter]] | Affects torque density and speed |
| [[design_guidelines/pole_selection\|Pole count]] | 4-pole common; higher poles reduce reluctance torque |

## Saliency Ratio

The saliency ratio $\xi = L_d / L_q$ is the primary figure of merit:

- Higher saliency → higher torque density and power factor
- Typical SynRM range: 3–10
- Practical limit: ~6–8 due to saturation and桥leakage

See [[concepts/saliency_ratio]].

## Power Factor

SynRM inherently has low power factor (typically 0.4–0.7) due to high magnetizing current demand. Improvement methods:

- PM assistance (→ [[topologies/pmasynrm]])
- Optimized barrier geometry
- Current angle control
- Consequent-pole designs

See [[concepts/power_factor]] and [[heuristics/low_pf_diagnosis]].

## Torque Ripple

SynRM suffers from significant torque ripple (10–30% unoptimized) due to:

- Stator slotting harmonics
- Barrier geometry harmonics
- Saturation effects

Mitigation: barrier shaping, skewing, optimal barrier angles.

See [[concepts/torque_ripple]] and [[heuristics/torque_ripple_reduction]].

## Common Applications

- Industrial drives (pumps, fans, compressors)
- Electric vehicle traction (emerging)
- Applications requiring rare-earth-free motors

## Advantages

- No permanent magnets (cost, supply chain)
- Simple rotor construction
- Good efficiency at rated load
- Robust mechanical structure
- Wide constant-power speed range

## Disadvantages

- Low power factor
- High torque ripple (without optimization)
- Lower torque density than PMSM
- Requires rotor barriers → mechanical complexity

## Important References

- [[research/papers/nagarkar_optimized_rotor_synrm]]
- [[research/papers/synrm_drive_design]]
- [[research/papers/overview_high_efficiency_synrm]]
- [[research/papers/synrm_iit_madras]]
- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/reluctance_torque]]
- [[concepts/dq_theory]]
- [[equations/torque_synrm]]
- [[design_guidelines/barrier_design]]
- [[design_guidelines/rib_design]]
- [[design_guidelines/bridge_design]]
- [[topologies/pmasynrm]]
