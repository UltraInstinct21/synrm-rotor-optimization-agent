---
type: heuristic
name: Barrier Tuning Rules
aliases: [barrier optimization rules]
motor_types: [SynRM]
topics: [barrier_design, optimization, practical_rules]
source_pages: ["raw/papers/nagarkar_optimized_rotor_synrm.md"]
related_concepts: ["concepts/saliency_ratio", "concepts/torque_ripple"]
related_equations: ["equations/saliency_ratio_eq"]
confidence: High confidence
---

# Barrier Tuning Rules

## Rule 1: First Barrier Angle

The first barrier (closest to d-axis) has the largest impact on saliency.
- Start with 30°–45° from d-axis
- Wider angle → better saliency but more torque ripple

## Rule 2: Subsequent Barrier Angles

Subsequent barriers should increase in angle from d-axis.
- Typical spacing: 10°–15° between barriers
- Non-uniform spacing often outperforms uniform

## Rule 3: Barrier Width Ratio

Barrier width / (barrier width + iron width) ≈ 0.4–0.6
- Too high: not enough iron for flux → lower $L_d$
- Too low: not enough barrier → lower $L_q$ increase

## Rule 4: Outermost Barrier

The outermost barrier (closest to airgap) is most critical for:
- Torque ripple
- Flux concentration
- Mechanical stress

Optimize this one first if limited on time.

## Rule 5: Bridge Saturation

Design bridges to saturate at operating flux levels.
- Saturated bridge → lower effective permeability → less flux leakage
- This improves effective saliency

## Rule 6: Rib Saturation

Similar to bridges, ribs should saturate.
- Small rib thickness → easy saturation
- Must still meet mechanical requirements

## Optimization Approach

For a 4-barrier SynRM:
1. Fix bridge and rib dimensions (mechanical constraint)
2. Optimize 4 barrier angles (4 variables)
3. Objective: maximize $(L_d - L_q)$ or minimize ripple
4. Use GA with 50–100 population, 50–100 generations

## MotorCAD Implementation

Use parametric sweep in MotorCAD:
1. Define barrier angles as variables
2. Set up objective function
3. Run GA or PSO optimization
4. Verify results with detailed FEA

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/torque_ripple]]
- [[design_guidelines/barrier_design]]
- [[design_guidelines/bridge_design]]
- [[design_guidelines/rib_design]]
- [[topologies/synrm]]
