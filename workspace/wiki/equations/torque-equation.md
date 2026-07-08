---
type: equation
title: Electromagnetic Torque Equation
aliases: [torque, reluctance torque, SynRM torque]
tags: [equations, torque, SynRM, dq-theory, reluctance-torque]
motor_types: [SynRM, PMaSynRM, IPMSM]
topics: [torque-production, dq-theory, reluctance-torque]
source_pages: []
related_concepts: [dq-theory, saliency-ratio, reluctance-torque]
related_motorcad_variables: [ShaftTorque, PhaseAdvance, PeakCurrent]
confidence: high
verification_status: verified
---

# Electromagnetic Torque Equation

## Statement

### Pure Reluctance Form (SynRM)

$$T = \frac{3}{2} \cdot \frac{P}{2} \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

### With PM Flux (PMaSynRM / IPMSM)

$$T = \frac{m}{2} \cdot p \cdot \left[(L_d - L_q) \cdot i_d \cdot i_q - \Psi_{mpq} \cdot i_d\right]$$

where $m$ is the number of phases (typically 3) and $p$ is the number of pole pairs.

---

## Original Notation

| Source | Notation | Meaning |
|--------|----------|---------|
| Saxena et al. | $T = \frac{3}{2}P(L_d - L_q)i_di_q$ | $P$ = pole pairs |
| Lopez et al. | $T = \frac{m}{2}p[\ldots]$ | $p$ = pole pairs, $m$ = phases |
| Miller (classic) | $T \propto (L_d - L_q)i_di_q$ | Simplified reluctance form |

---

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $T$ | Electromagnetic torque | Nm |
| $P$ | Pole pairs (same as $p$) | — |
| $L_d$ | d-axis inductance | H |
| $L_q$ | q-axis inductance | H |
| $i_d$ | d-axis current | A |
| $i_q$ | q-axis current | A |
| $\Psi_{mpq}$ | PM flux linkage (q-axis component) | Wb |
| $m$ | Number of phases | — |

---

## Assumptions

- Steady-state operation
- Sinusoidal MMF distribution (fundamental component only)
- No magnetic saturation (linear magnetic circuit)
- Negligible core loss and cross-coupling effects
- Uniform air gap approximation for reluctance torque term
- In the pure reluctance form: no PM flux ($\Psi_{mpq} = 0$)

---

## Interpretation

The torque equation has two distinct physical contributions:

### Reluctance Torque Term
$$T_{rel} = \frac{3}{2} \cdot \frac{P}{2} \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

- Arises from the **saliency** $(L_d - L_q)$ — the difference in inductance between d- and q-axes
- For SynRM: this is the **only** torque-producing mechanism
- Maximizing $L_d - L_q$ (saliency ratio) is the primary design objective
- The product $i_d \cdot i_q$ is maximized when current angle $\beta = 45°$ from the d-axis

### PM Torque Term (PMaSynRM / IPMSM)
$$T_{PM} = -\frac{3}{2} \cdot \frac{P}{2} \cdot \Psi_{mpq} \cdot i_d$$

- Interaction between PM flux and d-axis current
- For IPMSM: adds to reluctance torque; can be positive or negative depending on flux orientation
- For PMaSynRM: provides additional torque and improves power factor

---

## Design Relevance

1. **Maximize $(L_d - L_q)$**: Primary objective for SynRM design — optimize flux barriers to reduce $L_q$ while maintaining high $L_d$
2. **Optimize $i_d \cdot i_q$ product**: Controlled by current advance angle (PhaseAdvance in MotorCAD)
3. **Saliency ratio $\zeta = L_d / L_q$**: Higher saliency → higher reluctance torque for same current
4. **Current angle**: Maximum torque per ampere (MTPA) occurs when $\beta = \arctan\left(\frac{L_d \cdot i_d}{L_q \cdot i_q}\right)$
5. **Saturation effects**: At high currents, $L_d$ and $L_q$ decrease non-linearly, reducing torque below the linear prediction

---

## MotorCAD Mapping

| Equation Term | MotorCAD Variable | Notes |
|---------------|-------------------|-------|
| $T$ | `ShaftTorque` | Output from EMag calculation |
| $i_d$, $i_q$ | Derived from `PhaseAdvance` and `PeakCurrent` | Current decomposition |
| $L_d$, $L_q` | Computed via `do_magnetic_calculation()` | Inductance from flux/current |
| $P/2$ | `Pole_Number` / 2 | Set as 4 poles (2 pairs) |

---

## Sources

- Saxena, N.V. — SynRM torque analysis
- Lopez, P. — PMaSynRM torque formulation
- Miller, T.J.E. — Classic reluctance motor theory
- Pyrhönen, J. — Electric Machine Design (textbook)

---

## Related Pages

- [[dq-theory]] — d-q axis reference frame theory
- [[saliency-ratio]] — Ld/Lq ratio and its significance
- [[inductance-equations]] — Detailed inductance computation
- [[power-factor-equation]] — Power factor relationship with saliency
- [[loss-equations]] — Loss models affecting efficiency
- [[synrm-topology]] — Synchronous Reluctance Motor overview
