---
type: concept
name: Torque Ripple
aliases: []
motor_types: [SynRM, SRM, PMSM]
topics: [torque_quality, vibration, noise]
source_pages: ["raw/papers/"]
related_equations: []
related_motorcad_variables: []
confidence: Verified
---

# Torque Ripple

## Definition

The periodic variation of electromagnetic torque as the rotor rotates, expressed as:

$$TR = \frac{T_{max} - T_{min}}{T_{avg}} \times 100\%$$

## Why It Matters

Torque ripple causes:
- Vibration and acoustic noise
- Speed oscillations
- Reduced precision in position control
- Fatigue in mechanical components

SynRM is particularly prone to high torque ripple (10–30% unoptimized) due to barrier geometry harmonics.

## Physics

Sources of torque ripple in SynRM:
1. **Stator slotting** — slot openings create permeance variations
2. **Barrier geometry** — flux barrier shapes create harmonic MMF distributions
3. **Saturation** — local saturation varies with rotor position
4. **Current harmonics** — non-sinusoidal current waveforms

## Design Impact

| Source | Mitigation |
|--------|-----------|
| Slotting | Optimize slot/pole combination, skewing |
| Barrier harmonics | Barrier shaping, optimal barrier angles |
| Saturation | Avoid over-design, wider ribs |
| Current harmonics | Better current control, FOC |

## Typical Ranges

| Design State | Torque Ripple |
|-------------|---------------|
| Unoptimized SynRM | 15–30% |
| Optimized SynRM | 5–10% |
| Skewed SynRM | 3–7% |
| PMaSynRM | 3–8% |
| Well-designed PMSM | 2–5% |

## MotorCAD Mapping

MotorCAD computes torque vs. position for ripple analysis. Key outputs:
- Torque waveform over electrical cycle
- FFT of torque for harmonic analysis

## Sources

- [[research/papers/nagarkar_optimized_rotor_synrm]]
- [[research/papers/design_torque_ripple_reduction_srm]]
- [[research/papers/synrm_barrier_review_2025]]

## Related Pages

- [[concepts/saliency_ratio]]
- [[heuristics/torque_ripple_reduction]]
- [[design_guidelines/barrier_design]]
- [[topologies/synrm]]
