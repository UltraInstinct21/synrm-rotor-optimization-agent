---
type: concept
name: Power Factor
aliases: [PF]
motor_types: [SynRM, PMaSynRM]
topics: [power_factor, magnetizing_current]
source_pages: ["raw/papers/"]
related_equations: []
related_motorcad_variables: []
confidence: Verified
---

# Power Factor

## Definition

The ratio of real power to apparent power in the machine:

$$PF = \cos(\phi)$$

Where $\phi$ is the angle between voltage and current phasors.

## Why It Matters

Low power factor in SynRM means:
- Higher current for same real power → higher losses
- Larger inverter rating required
- Reduced system efficiency
- Limits practical applicability

SynRM typically achieves PF of 0.4–0.7, significantly lower than PMSM (0.85–0.95).

## Physics

In SynRM, the stator current must provide all magnetizing MMF (no rotor magnets). This creates a large reactive component:

$$PF \approx \frac{L_d - L_q}{L_d + L_q} \times \text{(load-dependent factor)}$$

Higher saliency ratio → higher PF.

## Key Relationships

- PF improves with saliency ratio $\xi = L_d/L_q$
- PF decreases at light loads (high magnetizing current relative to torque-producing current)
- PM assistance significantly improves PF (→ [[topologies/pmasynrm]])
- Saturation degrades PF at high loads

## Design Impact

| Saliency Ratio | Typical PF |
|----------------|-----------|
| 3 | 0.35–0.45 |
| 5 | 0.50–0.60 |
| 8 | 0.60–0.70 |
| >10 (PM-assisted) | 0.70–0.85 |

## Improvement Methods

1. Increase saliency ratio (barrier optimization)
2. PM assistance (PMaSynRM)
3. Consequent-pole designs
4. Optimized current angle control
5. Rotor geometry optimization

## MotorCAD Mapping

MotorCAD computes power factor from voltage and current phasors. Related outputs:
- Power factor at operating point
- Voltage angle
- Current angle

## Sources

- [[research/papers/nagarkar_optimized_rotor_synrm]]
- [[research/papers/synrm_drive_design]]
- [[research/papers/overview_high_efficiency_synrm]]
- [[heuristics/low_pf_diagnosis]]

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/reluctance_torque]]
- [[heuristics/low_pf_diagnosis]]
- [[heuristics/saliency_improvement]]
- [[topologies/synrm]]
- [[topologies/pmasynrm]]
