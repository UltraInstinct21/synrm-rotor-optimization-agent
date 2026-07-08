---
type: heuristic
name: Torque Ripple Reduction
aliases: [reduce torque ripple, minimize ripple]
motor_types: [SynRM]
topics: [torque_ripple, optimization, noise]
source_pages: ["raw/papers/"]
related_concepts: ["concepts/torque_ripple"]
related_equations: []
confidence: High confidence
---

# Torque Ripple Reduction

## Strategy Ladder

1. **Barrier angle optimization** — Most effective for SynRM
   - Adjust barrier angles to reduce harmonic MMF
   - Each barrier angle affects specific harmonics
   - Optimization needed (GA/PSO)

2. **Barrier width optimization** — Vary barrier widths
   - Non-uniform widths can reduce ripple
   - Trade-off with saliency

3. **Skewing** — Rotor or stator skew
   - 1 slot skew is common starting point
   - Reduces both ripple and average torque
   - Manufacturing complexity increases

4. **Slot/pole combination** — Choose better combinations
   - GCD(slots, poles) affects cogging
   - Fractional slot/pole can help

5. **Current harmonics injection** — Add 5th/7th harmonics
   - Compensates for MMF harmonics
   - Requires advanced control

## Quantitative Impact

| Method | Ripple Reduction | Torque Penalty |
|--------|-----------------|----------------|
| Barrier optimization | 30–50% | 0–5% |
| 1-slot skew | 40–60% | 5–10% |
| Current injection | 20–40% | 0–2% |
| Combined | 60–80% | 5–12% |

## MotorCAD Approach

1. Compute torque vs. position waveform
2. Analyze FFT of torque
3. Identify dominant harmonics
4. Optimize barrier angles to target specific harmonics
5. Verify with FEA

## Related Pages

- [[concepts/torque_ripple]]
- [[heuristics/barrier_tuning_rules]]
- [[design_guidelines/barrier_design]]
- [[topologies/synrm]]
