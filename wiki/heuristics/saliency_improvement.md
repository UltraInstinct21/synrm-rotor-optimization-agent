---
type: heuristic
name: Saliency Improvement Strategies
aliases: [increase Ld/Lq, improve saliency]
motor_types: [SynRM]
topics: [saliency, rotor_design, optimization]
source_pages: ["raw/papers/"]
related_concepts: ["concepts/saliency_ratio"]
related_equations: ["equations/saliency_ratio_eq"]
confidence: High confidence
---

# Saliency Improvement Strategies

## Strategy Ladder

From most effective to least:

1. **Add PM assistance** — Most effective single change
   - Adds alignment torque component
   - Increases effective saliency
   - Cost and supply chain trade-off

2. **Increase barrier count** — 3→4→5 barriers
   - More barriers create better d-q separation
   - Diminishing returns beyond 5
   - Manufacturing complexity increases

3. **Optimize barrier angles** — Adjust angle of each barrier
   - Non-uniform angles often outperform uniform
   - Optimization needed for specific geometry
   - Use GA or PSO for multi-barrier systems

4. **Reduce bridge/rib thickness** — Minimize flux leakage
   - Must satisfy mechanical constraints
   - Saturation helps (design bridges to saturate)

5. **Use curved/Bezier barriers** — Better flux shaping
   - More complex to manufacture
   - Significant saliency improvement possible

6. **Optimize barrier width ratio** — Barrier width vs iron width
   - Too wide: not enough iron for d-axis flux
   - Too narrow: not enough barrier for q-axis blocking

## Trade-offs

- Higher saliency often comes with:
  - Higher torque ripple (mitigate with barrier shaping)
  - Manufacturing complexity
  - Mechanical stress concerns

## MotorCAD Optimization Approach

1. Set up parametric model with barrier variables
2. Define objective: maximize $(L_d - L_q)$ or minimize torque ripple
3. Use GA or PSO for optimization
4. Verify with FEA

## Related Pages

- [[concepts/saliency_ratio]]
- [[equations/saliency_ratio_eq]]
- [[heuristics/barrier_tuning_rules]]
- [[design_guidelines/barrier_design]]
- [[topologies/synrm]]
