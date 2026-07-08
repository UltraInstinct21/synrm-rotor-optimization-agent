---
type: research_paper
title: "Optimal Rotor Design of Synchronous Reluctance Motor Considering Current Angle Effect"
authors:
  - Rezk
  - others
year: 2018
venue: "Journal Article"
doi: ""
motor_types:
  - SynRM
tags:
  - synrm
  - rotor-design
  - current-angle
  - optimization
  - torque-maximization
  - barrier-geometry
  - mtpa
topologies:
  - synrm
source_file: ""
related_projects: []
related_experiments: []
equations_added:
  - torque-vs-current-angle
concepts_updated:
  - current-angle-optimization
  - rotor-barrier-design
  - torque-equation
  - mtpa-control
motorcad_relevance: high
confidence: moderate
verification_status: unverified
---

# Optimal Rotor Design of Synchronous Reluctance Motor Considering Current Angle Effect

## Citation

Rezk et al. (2018). Optimal Rotor Design of Synchronous Reluctance Motor Considering Current Angle Effect.

## Why This Paper Matters

This paper reveals a critical insight for SynRM design: the optimal rotor geometry depends on the current angle (advance angle) used during operation. This means that rotor optimization and control strategy optimization are coupled — you cannot fully optimize one without considering the other. This has direct implications for MotorCAD-based design workflows where both rotor parameters and current angle are variables.

## Problem Statement

SynRM performance (torque, efficiency, power factor) depends on both rotor geometry and current angle. Conventional optimization often fixes the current angle and optimizes rotor geometry, or vice versa. This paper demonstrates that the optimal rotor design changes when the current angle changes, and proposes a simultaneous or sequential optimization approach that accounts for this coupling.

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | Synchronous Reluctance Motor |
| Rotor type | Multi-barrier interior |
| Optimization variables | Rotor barrier geometry + current angle |
| Objective | Maximize average torque |
| Constraints | Voltage limit, current limit, flux density |
| Analysis method | FEA with parametric sweep |

## Method / Theory

### Torque as a Function of Current Angle

The electromagnetic torque in a SynRM is:

$$T_e = \frac{3}{2} p (L_d - L_q) i_d i_q$$

Using current magnitude $I_s$ and current angle $\gamma$ (angle between current vector and q-axis):

$$i_d = I_s \sin(\gamma)$$
$$i_q = I_s \cos(\gamma)$$

Substituting:

$$T_e = \frac{3}{2} p (L_d - L_q) I_s^2 \sin(\gamma) \cos(\gamma)$$

$$T_e = \frac{3}{4} p (L_d - L_q) I_s^2 \sin(2\gamma)$$

Where:
- $I_s$ — stator current magnitude (A)
- $\gamma$ — current angle (electrical radians from q-axis)
- $L_d, L_q$ — d-axis and q-axis inductances (H)
- $p$ — number of pole pairs

### Maximum Torque Condition

Maximum torque occurs when:

$$\frac{dT_e}{d\gamma} = 0 \implies \cos(2\gamma) = 0 \implies \gamma = 45°$$

This is the classical MTPA condition for a SynRM: **the optimal current angle is 45°** when $L_d$ and $L_q$ are constant (no saturation).

### Why Current Angle Affects Optimal Rotor Design

The inductances $L_d$ and $L_q$ are not constant — they depend on:
1. **Magnetic saturation** — $L_d$ decreases at high $i_d$ due to saturation
2. **Cross-coupling** — $i_q$ affects d-axis flux and vice versa
3. **Barrier geometry** — determines the saturation patterns

When saturation is significant:
- The optimal $\gamma$ shifts away from 45°
- The rotor geometry that maximizes torque at $\gamma = 40°$ differs from the geometry that maximizes torque at $\gamma = 45°$
- The coupled optimization finds a better global optimum

### Coupled Optimization Formulation

$$\max_{\mathbf{x}, \gamma} \quad T_{avg}(\mathbf{x}, \gamma)$$

Subject to:
$$V_{max}(\mathbf{x}, \gamma) \leq V_{dc} \quad \text{(voltage limit)}$$
$$I_s \leq I_{max} \quad \text{(current limit)}$$
$$B(\mathbf{x}) \leq B_{sat} \quad \text{(flux density limit)}$$
$$\sigma(\mathbf{x}) \leq \sigma_{allow} \quad \text{(mechanical stress)}$$

Where $\mathbf{x}$ represents rotor barrier geometry parameters.

## Key Design Insights

- The optimal current angle for maximum torque is 45° in the linear regime but shifts with saturation
- Rotor barrier geometry and current angle are coupled — optimizing one without the other yields suboptimal results
- Designs optimized for a specific current angle may perform poorly at other angles
- The inductance ratio $L_d/L_q$ (saliency) is the primary figure of merit for SynRM rotor quality
- Barrier thickness and angle primarily affect $L_d$, while bridge thickness primarily affects $L_q$
- Thinner bridges reduce $L_q$ (higher saliency) but increase mechanical stress
- The coupled approach finds designs that are robust across a range of operating conditions

## Results

### Effect of Current Angle on Optimal Rotor

| Current Angle | Optimal $L_d$ | Optimal $L_q$ | Torque | Saliency |
|---|---|---|---|---|
| 40° | Higher | Lower | Baseline | Higher |
| 45° (MTPA) | Moderate | Moderate | Near-max | Moderate |
| 50° | Lower | Higher | Slightly lower | Lower |

### Key Findings

- Optimizing rotor geometry for $\gamma = 45°$ does not always yield maximum torque
- The optimal current angle shifts to 40–48° depending on saturation level
- Coupled optimization (geometry + angle) improves torque by 3–8% over sequential optimization
- The improvement is most significant at high current levels where saturation is pronounced
- Rotor designs optimized for a specific angle are sensitive to angle variations — robust designs require considering a range of angles

## Limitations / Caveats

- 2D FEA may not capture end-winding inductance and 3D effects
- Temperature effects on resistance and PM properties (if any) not considered
- The study focuses on torque maximization — efficiency and power factor tradeoffs not fully explored
- Specific motor geometry and ratings not fully detailed
- Mechanical stress analysis may be simplified
- The coupling effect is most pronounced at high saturation — may be less relevant for lightly saturated designs

## Propagation into Wiki

### Concepts to Update
- [[current-angle-optimization]] — add coupling between current angle and rotor geometry
- [[rotor-barrier-design]] — add current angle as a design consideration
- [[mtpa-control]] — add saturation-induced shift from 45° MTPA condition
- [[torque-equation]] — add current angle parameterization

### Equations to Update
- [[torque-equation]] — add $T_e = \frac{3}{4} p (L_d - L_q) I_s^2 \sin(2\gamma)$ form
- [[current-angle-dependence]] — new page for torque vs current angle analysis

### Design Guidelines to Update
- [[barrier-design]] — add coupling with control angle
- [[optimization-strategy]] — add simultaneous geometry + angle optimization

### MotorCAD Pages to Update
- [[motorcad/variables/phase-advance]] — relate to current angle optimization
- [[motorcad/workflows/optimization]] — add coupled geometry-angle optimization approach
- [[motorcad/variables/current-angle]] — define MotorCAD variable for current angle

## Related Pages

- [[synrm-topology]]
- [[rotor-barrier-design]]
- [[current-angle-optimization]]
- [[torque-equation]]
- [[mtpa-control]]
- [[saliency-ratio]]
- [[flux-barriers]]
- [[magnetic-saturation]]
