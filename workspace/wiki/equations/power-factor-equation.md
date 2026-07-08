---
type: equation
title: Power Factor Equation
aliases: [power factor, PF, power factor improvement, PF maximization]
tags: [equations, power-factor, saliency, dq-theory, SynRM]
motor_types: [SynRM, PMaSynRM, IPMSM]
topics: [power-factor, saliency, dq-theory, design-optimization]
source_pages: []
related_concepts: [saliency-ratio, dq-theory, torque-equation]
related_motorcad_variables: [PhaseAdvance, PowerFactor, Ld, Lq]
confidence: high
verification_status: verified
---

# Power Factor Equation

## Statement

### Maximum Power Factor (SynRM)

$$PF_{max} = \frac{\zeta - 1}{\zeta + 1}$$

where $\zeta = L_d / L_q$ is the saliency ratio.

### Phase Angle

$$\varphi = \arctan\left(\frac{i_d}{i_q}\right) + \arctan\left(\frac{\psi_q}{\psi_d}\right)$$

$$PF = \cos(\varphi)$$

### With PM Flux (PMaSynRM)

$$PF_{PM} = \frac{\zeta - 1}{\zeta + 1} + \Delta PF_{PM}$$

where $\Delta PF_{PM}$ is the improvement from PM flux adding to d-axis flux.

---

## Original Notation

| Source | Notation | Meaning |
|--------|----------|---------|
| Saxena et al. | $PF_{max} = (\zeta-1)/(\zeta+1)$ | Maximum achievable PF |
| Bao et al. | $\varphi = \arctan(i_d/i_q) + \arctan(\psi_q/\psi_d)$ | Total phase angle |
| Lopez et al. | $\Delta PF_{PM}$ from $\Psi_{pm}$ | PM contribution |

---

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $PF$ | Power factor | — (dimensionless, 0 to 1) |
| $PF_{max}$ | Maximum achievable PF (SynRM) | — |
| $\zeta$ | Saliency ratio ($L_d / L_q$) | — |
| $\varphi$ | Phase angle between voltage and current | rad or ° |
| $i_d$ | d-axis current | A |
| $i_q$ | q-axis current | A |
| $\psi_d$ | d-axis flux linkage | Wb |
| $\psi_q$ | q-axis flux linkage | Wb |
| $\Psi_{pm}$ | PM flux linkage | Wb |

---

## Assumptions

- Steady-state, sinusoidal MMF
- No magnetic saturation (linear model)
- Negligible stator resistance and core loss for the $PF_{max}$ formula
- Symmetric machine (balanced 3-phase)
- The $\zeta$ value used is the **apparent** saliency at the operating point, not the unsaturated value

---

## Physical Interpretation

### Why SynRM Has Low Power Factor

In a pure SynRM, the stator current must supply **both** the magnetizing flux (d-axis) and the torque-producing flux (q-axis). The phase angle between voltage and current is large because:

- Voltage leads current by approximately $90° + \arctan(i_d/i_q)$
- The higher the saliency ratio, the closer the voltage and current align
- But even with infinite saliency, $PF_{max} \to 1$ only asymptotically

### Saliency Ratio Impact

| Saliency $\zeta$ | $PF_{max}$ | Practical? |
|-------------------|-------------|------------|
| 2 | 0.333 | Poor — typical early SynRM |
| 4 | 0.600 | Moderate — achievable with good barriers |
| 6 | 0.714 | Good — advanced barrier design |
| 9 | 0.800 | Very good — state-of-art SynRM |
| 15 | 0.875 | Excellent — approaching PM motor levels |
| $\infty$ | 1.000 | Theoretical limit only |

### PM Flux Contribution

Adding PM flux ($\Psi_{pm}$) to the d-axis:
- Increases $\psi_d$ without requiring additional d-axis current
- Reduces the phase angle $\varphi$
- Can push PF above the pure reluctance limit
- PMaSynRM typically achieves PF 0.85–0.95

### Phase Angle Components

1. **$\arctan(i_d/i_q)$**: Current angle relative to q-axis (controlled by PhaseAdvance)
2. **$\arctan(\psi_q/\psi_d)$**: Flux angle relative to d-axis (determined by machine saliency)

---

## Design Relevance

1. **Saliency is king**: Higher $\zeta$ → higher PF — this is why barrier optimization is critical
2. **Current angle optimization**: PhaseAdvance (MotorCAD) controls the $i_d/i_q$ split
3. **Inverter sizing**: Low PF means higher current for same power → larger inverter → higher cost
4. **PM addition**: For applications requiring PF > 0.8, PMaSynRM may be preferred over pure SynRM
5. **Saturation degrades PF**: At high currents, $L_d$ drops faster than $L_q$ in some designs, reducing effective saliency
6. **Tradeoff with torque**: Maximizing PF (high $i_d$) may reduce torque per ampere (MTPA condition)

---

## MotorCAD Mapping

| Equation Term | MotorCAD Variable | Notes |
|---------------|-------------------|-------|
| $PF$ | `PowerFactor` | Output from EMag calculation |
| $\varphi$ | Derived from voltage/current waveforms | Post-processing |
| $i_d$, $i_q$ | Derived from `PhaseAdvance` and `PeakCurrent` | Current decomposition |
| $L_d$, $L_q$ | From `do_magnetic_calculation()` | Inductance output |
| Phase advance | `PhaseAdvance` | Sets current angle (fixed at 45°) |

---

## Sources

- Saxena, N.V. — Power factor analysis in SynRM
- Bao, X. — PF improvement with PM assistance
- Lopez, P. — PMaSynRM power factor characterization
- Miller, T.J.E. — Electric Machinery Fundamentals

---

## Related Pages

- [[saliency-ratio]] — Ld/Lq ratio definition and optimization
- [[torque-equation]] — Torque depends on saliency and current angle
- [[inductance-equations]] — How Ld and Lq are determined
- [[synrm-topology]] — SynRM motor overview and PF limitations
- [[pmasynrm-topology]] — PMaSynRM for PF improvement
- [[loss-equations]] — Efficiency tradeoffs
