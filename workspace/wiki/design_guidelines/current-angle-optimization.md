---
type: design_guideline
title: Current Angle Optimization
aliases: [current-angle-beta, mtpa-angle]
tags: [synrm, control, current-angle, mtpa, torque-optimization, design-guideline]
motor_types: [synrm, pmasynrm, ipmsm]
topics: [current-angle, mtpa-control, dq-theory, torque-production, control-strategy]
related_pages: [mtpa-control, torque-equation, dq-theory, reluctance-torque]
source_files: []
confidence: high
---

# Current Angle Optimization

## Purpose

The current angle β (also called the current advance angle or torque angle) is the angle between the stator current vector I_s and the rotor d-axis. It is the primary control variable for maximizing torque per ampere (MTPA) in SynRM drives. This page provides guidelines for determining the optimal current angle across operating conditions.

---

## Current Angle Definition

### Convention

- β = angle between I_s and the d-axis (electrical degrees).
- β = 0° → current entirely along d-axis → zero reluctance torque.
- β = 90° → current entirely along q-axis → zero reluctance torque.
- Maximum reluctance torque occurs at β = 45° for the unsaturated, linear case.

### Relationship to torque angle δ

- Some literature uses δ = angle between I_s and the q-axis.
- δ = 90° − β.
- Ensure consistent convention when comparing references.

---

## Fundamental Torque Relation

### Reluctance torque (unsaturated)

For a pure SynRM (no magnets):

$$T = \frac{3}{2} p (L_d - L_q) i_d i_q$$

In terms of current angle β and magnitude I_s:

$$T = \frac{3}{4} p (L_d - L_q) I_s^2 \sin(2\beta)$$

### Key observations

- Torque is proportional to **sin(2β)** → maximum at β = 45°.
- Torque is proportional to **(L_d − L_q)** → saliency ratio is critical.
- Torque is proportional to **I_s²** → current magnitude matters, but angle determines how effectively it produces torque.

---

## Optimal Angle Under Saturation

### Why β shifts with current

At high current levels, magnetic saturation causes:

1. **L_d decreases** — d-axis flux path saturates (iron segments between barriers saturate).
2. **L_q may also decrease** — but typically less than L_d because q-axis flux path has less iron.
3. **The effective (L_d − L_q) ratio changes** with current magnitude.

Because saturation is asymmetric, the β that maximizes torque shifts away from 45°.

### Typical behavior

| Current level | Optimal β | Reason |
|---|---|---|
| Low (below knee) | ~45° | Linear regime, symmetric saturation |
| Medium (near knee) | 50–60° | d-axis saturates more, β shifts toward q-axis |
| High (well above knee) | 60–70° | Heavy saturation, further shift needed |
| Very high (deep saturation) | 65–75° | Extreme saturation, diminishing returns |

### Design implication

- A fixed β = 45° is optimal only at low-to-medium currents.
- For maximum performance across the full operating range, **β must be a function of I_s** (or i_d, i_q).
- This is typically implemented as a **look-up table (LUT)** in the motor controller.

---

## Implementation: Look-Up Table Approach

### Data source

- FEA parameter sweeps: vary I_s and β, record torque for each (I_s, β) pair.
- Build a 2D look-up table: T = f(I_s, β).

### MTPA table

For each I_s, find β_maxTorque that maximizes T. Store as:

| I_s (A) | β_optimal (°) |
|---|---|
| 10 | 44 |
| 20 | 48 |
| 30 | 55 |
| 40 | 62 |
| 50 | 68 |

### Controller implementation

1. Measure or estimate I_s (or i_d, i_q).
2. Interpolate the MTPA table to find β_optimal.
3. Command I_s at angle β_optimal.

### Practical notes

- Table resolution: 5–10 A steps in I_s, 2–5° steps in β.
- Interpolation: linear is sufficient for most applications.
- Table must be generated from FEA (analytical models are inaccurate under saturation).

---

## Field Weakening Considerations

### At high speeds

- Voltage limit: V_s_max constrains the available current at high speed.
- Current angle β must increase beyond the MTPA angle to reduce the d-axis current component.
- This is **field weakening** — it reduces flux to allow higher speed operation.

### β in field weakening

| Speed range | β behavior |
|---|---|
| Below base speed | MTPA angle (45–70° depending on current) |
| At base speed | Transition begins |
| Above base speed | β increases toward 90° (current shifts toward q-axis) |
| At maximum speed | β approaches 90° (minimal d-axis current) |

### Design implication

- The MTPA table and field weakening strategy are coupled.
- For high-speed applications (e.g., 6000+ RPM), the controller must handle both MTPA and field weakening.

---

## Effect of L_d/L_q Ratio on Optimal β

### High saliency ratio

- L_d/L_q > 4: Optimal β remains closer to 45° over a wider current range.
- Saturation effects are less pronounced because the q-axis reluctance is already very high.

### Low saliency ratio

- L_d/L_q < 3: Optimal β shifts more aggressively with current.
- Saturation of the d-axis has a proportionally larger impact.

### Design implication

- Motors with higher saliency ratio are more "forgiving" in control — a fixed β = 45° works over a wider range.
- Motors with lower saliency ratio require more precise β optimization.

---

## Torque Ripple and Current Angle

### Harmonic effects

- Non-sinusoidal flux distribution produces torque harmonics at 6th, 12th, etc. (for 3-phase).
- The amplitude of torque ripple depends on β.
- Certain β values may minimize specific harmonics.

### Optimization

- Simultaneous optimization of average torque and torque ripple is possible.
- Add a torque ripple penalty to the MTPA objective function:

$$J = T_{avg} - w_{ripple} \cdot T_{ripple}$$

- This produces a β that balances torque magnitude and smoothness.

---

## Practical Design Rules

1. **Start with β = 45°** for initial design and FEA validation.
2. **Perform FEA sweep** of β from 30° to 80° at multiple current levels.
3. **Build MTPA table** from FEA results.
4. **Validate at rated operating point** — ensure torque meets specification.
5. **Check field weakening range** if high-speed operation is required.
6. **Controller implementation** — use LUT with linear interpolation, update from FEA.

---

## References

- Saxena, R. — current angle optimization for SynRM
- Rezk, M. — MTPA strategies for reluctance motors
- Boldea, I. — reluctance synchronous motors (textbook)
- Pyrhönen, J. — rotational electrical machines (textbook)

---

## Related Pages

- [[mtpa-control]] — maximum torque per ampere control strategy
- [[torque-equation]] — detailed torque derivation
- [[dq-theory]] — d-q axis reference frame theory
- [[reluctance-torque]] — torque production mechanism in SynRM
- [[saliency-ratio]] — how saliency affects optimal current angle
