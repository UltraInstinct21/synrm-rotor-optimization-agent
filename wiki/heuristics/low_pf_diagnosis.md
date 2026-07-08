---
type: heuristic
name: Low Power Factor Diagnosis
aliases: [PF fix, power factor improvement]
motor_types: [SynRM]
topics: [power_factor, troubleshooting, improvement]
source_pages: []
related_concepts: ["concepts/power_factor", "concepts/saliency_ratio"]
related_equations: []
confidence: High confidence
---

# Low Power Factor Diagnosis

## Symptom

Power factor below 0.5 in SynRM operation.

## Diagnostic Logic

### If PF < 0.4:

1. **Check saliency ratio** — Is $L_d/L_q > 4$?
   - No → Barrier design issue. Increase barrier count or optimize angles.
   - Yes → Check other causes.

2. **Check current angle** — Is $\gamma$ near optimal?
   - Optimal $\gamma$ depends on speed and voltage limit
   - At low speed: $\gamma_{opt} \approx 45°$
   - At field weakening: $\gamma$ increases

3. **Check saturation** — Is $L_d$ reduced by saturation?
   - High current → saturation → lower effective saliency
   - Reduce current or redesign barriers for less saturation

4. **Check flux leakage** — Are bridges/ribs too thick?
   - Thicker bridges → more leakage → lower effective $L_d - L_q$

### If PF is moderate (0.4–0.6):

- Consider PM assistance (→ [[topologies/pmasynrm]])
- Optimize barrier angles for better saliency
- Reduce flux leakage paths

## Improvement Methods

| Method | Effect | Complexity |
|--------|--------|-----------|
| Barrier optimization | +0.05–0.15 PF | Moderate |
| PM assistance | +0.15–0.30 PF | High |
| Current angle optimization | +0.02–0.05 PF | Low |
| Consequent-pole design | +0.05–0.10 PF | Moderate |

## MotorCAD Mapping

Use MotorCAD to:
1. Compute $L_d$ and $L_q$ at operating point
2. Verify saliency ratio
3. Test barrier geometry changes
4. Evaluate PM assistance options

## Related Pages

- [[concepts/power_factor]]
- [[concepts/saliency_ratio]]
- [[heuristics/saliency_improvement]]
- [[design_guidelines/barrier_design]]
- [[topologies/synrm]]
- [[topologies/pmasynrm]]
