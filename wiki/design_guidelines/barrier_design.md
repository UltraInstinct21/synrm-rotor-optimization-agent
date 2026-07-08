---
type: design_guideline
name: Flux Barrier Design
aliases: [barrier geometry, barrier shaping]
motor_types: [SynRM]
topics: [rotor_design, barriers, saliency]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md", "raw/papers/"]
related_equations: ["equations/saliency_ratio_eq", "equations/torque_synrm"]
related_motorcad_variables: []
confidence: High confidence
---

# Flux Barrier Design

## Description

Flux barriers are air slots cut into the SynRM rotor to create magnetic anisotropy. They are the primary design variable for controlling the saliency ratio.

## Typical Ranges

| Parameter | Typical Range |
|-----------|--------------|
| Barrier count | 3–6 per pole |
| Barrier angle (from d-axis) | 20°–70° |
| Barrier width ratio | 0.3–0.7 of pole pitch |
| Barrier depth | 60–90% of rotor radius |

## Barrier Count

| Count | Saliency | Torque Ripple | Mechanical |
|-------|----------|---------------|------------|
| 2–3 | Lower | Higher | Simpler |
| 4–5 | Higher | Lower | Moderate |
| 6+ | Marginal gain | Lowest | Complex |

More barriers generally improve saliency but with diminishing returns beyond 4–5.

## Barrier Shape

Common shapes:
- **Straight barriers**: Simple, easy to manufacture
- **U-shaped barriers**: Better saliency, more complex
- **Curved/Bezier barriers**: Optimal saliency, hardest to manufacture
- **Multi-barrier with varying widths**: Trade-off between saliency and ripple

## Barrier Angle Optimization

The angle of each barrier from the d-axis affects:
- Saliency ratio
- Torque ripple
- Flux concentration

Optimal angles depend on:
- Number of barriers
- Rotor diameter
- Airgap
- Bridge/rib dimensions

## Design Impact

- Barrier geometry is the PRIMARY target of SynRM optimization
- Trade-off between saliency (torque) and torque ripple
- Manufacturing constraints limit achievable shapes
- Bridge/rib dimensions interact with barrier design

## MotorCAD Mapping

MotorCAD defines barriers through:
- Barrier angles
- Barrier depths
- Barrier widths
- Bridge and rib dimensions

## Sources

- [[research/papers/nagarkar_optimized_rotor_synrm]]
- [[research/papers/synrm_barrier_review_2025]]
- [[research/papers/topology_optimization_synrm]]

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/reluctance_torque]]
- [[equations/saliency_ratio_eq]]
- [[design_guidelines/bridge_design]]
- [[design_guidelines/rib_design]]
- [[heuristics/barrier_tuning_rules]]
- [[topologies/synrm]]
