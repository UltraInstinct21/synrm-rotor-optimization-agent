---
type: research_paper
title: "Optimal Rotor Design of Synchronous Reluctance Machines Considering the Effect of Current Angle"
authors: "Hegazy Rezk, Kotb B. Tawfiq, Peter Sergeant, Mohamed N. Ibrahim"
year: 2021
venue: "Mathematics"
doi: "10.3390/math9040344"
motor_types: [SynRM]
topics: [rotor_optimization, flux_barrier_design, current_angle, torque_ripple, saliency_ratio]
topologies: [synchronous_reluctance]
source_files: ["raw/papers/Optimal Rotor design of SRM.md"]
related_projects: []
related_experiments: []
equations_added: ["PSO_velocity_update", "GWO_encircling", "GWO_position_update", "cost_function"]
concepts_updated: [flux_barrier_parameters, current_angle_optimization, saliency_ratio]
motorcad_relevance: "High — directly applicable flux-barrier geometry parameters and optimization methodology for SynRM rotor design in MotorCAD workflows"
confidence: Verified
---

# Optimal Rotor Design of Synchronous Reluctance Machines Considering the Effect of Current Angle

## Citation

Rezk, H.; Tawfiq, K.B.; Sergeant, P.; Ibrahim, M.N. "Optimal Rotor Design of Synchronous Reluctance Machines Considering the Effect of Current Angle." *Mathematics* **2021**, *9*, 344. https://doi.org/10.3390/math9040344

## Why This Paper Matters

This paper demonstrates that the **current angle should be treated as an optimization variable** rather than fixed during SynRM rotor geometry design. When the current angle is included as a variable, output power improves by ~3.32% compared to fixed-angle cases, and the optimization converges faster. The paper also provides a complete set of optimized flux-barrier parameters for a 5.5 kW SynRM across five different current-angle regimes, offering a valuable benchmark for [[SynRM]] rotor design in [[optimize_synrm_v4|existing optimization workflows]].

## Problem Statement

Existing SynRM rotor optimization studies fix the current angle at an arbitrary value (typically 45°–56.5°) during the geometry optimization process. This suboptimal approach ignores the coupling between current angle and optimal rotor geometry, potentially yielding suboptimal torque density, torque ripple, and efficiency.

## Machine / Study Context

| Parameter | Value |
|-----------|-------|
| Type | 3-phase SynRM (induction motor stator repurposed) |
| Stator inner diameter | 110 mm |
| Stator outer diameter | 180 mm |
| Rotor outer diameter | 109.4 mm |
| Shaft diameter | 35 mm |
| Axial length | 140 mm |
| Air gap length | 0.3 mm |
| Stator slots / Rotor poles | 36 / 4 |
| Rated frequency | 100 Hz |
| Rated power | 5.5 kW |
| RMS rated current | 12.3 A |
| Rotor flux barriers per pole | 3 |
| Stator steel | M270-50A |
| Rotor steel | M330-50A |

## Method / Theory

### Optimization Algorithm: Hybrid PSOGWO

A hybrid of Particle Swarm Optimization (PSO) and Grey Wolf Optimizer (GWO) was used. PSO provides exploration via social thinking; GWO provides local search and prevents premature convergence. The hybrid balances exploitation and exploration throughout the optimization.

### Rotor Parameterization

Twelve geometric parameters define the rotor flux barriers per pole (see [[flux_barrier_parameters]]):

- **Angles:** θ_b1, θ_b2, θ_b3
- **Widths:** W_b1, W_b2, W_b3
- **Lengths:** L_b1, L_b2, L_b3
- **Positions:** p_b1, p_b2, p_b3

### Five Current-Angle Cases

| Case | Current Angle Range | Description |
|------|-------------------|-------------|
| 1 | 30°–40° | Below maximum-torque angle |
| 2 | 40°–45° | Near maximum-torque angle (no saturation) |
| 3 | 45° fixed | Theoretical max-torque angle (neglecting saturation) |
| 4 | 45°–65° | Wide range including saturation effects |
| 5 | 50°–55° | Narrow range near typical literature values |

Each case ran 210 design evaluations. The stator was held fixed; only the 12 rotor parameters and current angle were optimized.

## Important Equations

### PSO Velocity Update (Eq. 1)

$$v_i^{t+1} = w \cdot v_i^t + C_1 \cdot r_1 \cdot (P_{best_i} - x_i^t) + C_2 \cdot r_2 \cdot (G_{best} - x_i^t)$$

| Variable | Meaning | Units |
|----------|---------|-------|
| v_i^{t+1} | Updated velocity of particle i | dimensionless (normalized) |
| w | Inertia factor | — |
| C_1 | Cognitive coefficient | — |
| C_2 | Social coefficient | — |
| r_1, r_2 | Random values in [0,1] | — |
| P_{best_i} | Personal best position of particle i | same as x |
| G_{best} | Global best position | same as x |
| x_i^t | Current position of particle i | same as design variables |

**Assumptions:** Standard PSO formulation. Three sections control exploration (inertia), individual learning (cognitive), and social sharing.

### PSO Position Update (Eq. 2)

$$x_i^{t+1} = x_i^t + v_i^{t+1}$$

### GWO Encircling (Eqs. 3–6)

$$D = |C \cdot X_p(t) - X(t)|$$

$$X(t+1) = X_p(t) - A \cdot D$$

$$A = a \cdot (2r_1 - 1)$$

$$C = 2r_2$$

where a decreases linearly from 2 to 0 over iterations. X_p is the prey position; X is the wolf position.

### GWO Position Update (Eqs. 7–9)

$$D_\alpha = |C_1 \cdot X_\alpha(t) - X(t)|$$

$$D_\beta = |C_2 \cdot X_\beta(t) - X(t)|$$

$$D_\delta = |C_3 \cdot X_\delta(t) - X(t)|$$

$$X_1 = X_\alpha - a_1 \cdot D_\alpha$$

$$X_2 = X_\beta - a_2 \cdot D_\beta$$

$$X_3 = X_\delta - a_3 \cdot D_\delta$$

$$X_p(t+1) = \frac{X_1 + X_2 + X_3}{3}$$

The best three wolves (α, β, δ) guide the pack toward the prey.

### Optimization Cost Function (Eq. 10)

$$\text{cost} = T_r^2 + \frac{1}{T_{av}}$$

| Variable | Meaning | Units |
|----------|---------|-------|
| T_r | Torque ripple | % (percentage) |
| T_{av} | Average torque | N·m |

**Assumptions:** Dual objective (minimize ripple, maximize torque) combined into a single scalar cost. The squared ripple term penalizes high ripple; the inverse torque term rewards higher torque.

## Key Design Insights

1. **Current angle as a variable improves geometry:** Case 1 (30°–40° range) produced the highest output power — 3.32% higher than the fixed 45° case and 5.65% higher than Case 2.

2. **Fixed current angle yields geometry sensitive to the chosen value:** The optimal rotor geometry for Case 3 (45° fixed) differed significantly from literature reference [[Ibrahim_2016|Ibrahim et al. 2016]] which used 56.5°.

3. **Current angle range affects rotor iron volume:** Case 3 (fixed 45°) produced 11% more rotor iron volume than Case 4, meaning higher inertia and slower dynamic response.

4. **Torque ripple is highly sensitive to fixed current angle:** At 45°, torque ripple was 34.2% lower than at 56.5° (from prior literature). This underscores that the "standard" current angle choice materially affects the optimized geometry.

5. **Optimal current angle differs across cases:** Cases 1–3 converged to an optimal current angle of 52.11°, while Cases 4–5 converged to 56.8°. This confirms saturation shifts the optimal operating point away from the theoretical 45°.

6. **Saliency ratio varies with current angle range:** Case 1 achieved the highest saliency ratio (5.36), 11.7% higher than Case 3 (4.8).

## Optimization Setup

- **Algorithm:** Hybrid PSOGWO
- **Population / evaluations:** 210 designs per case
- **Coupled FEM:** Each candidate evaluated via 2D finite element magnetic simulation
- **Objective:** Maximize average torque, minimize torque ripple (Eq. 10)
- **Variables:** 12 rotor geometric parameters + current angle (where applicable)
- **Constraints:** Geometric feasibility constraints on flux barrier dimensions (Table 2 limits)
- **Stator:** Fixed — standard 5.5 kW induction motor stator, 36 slots

### Rotor Variable Bounds

| Variable | Lower | Upper |
|----------|-------|-------|
| θ_b1 | 5° | 9.3° |
| θ_b2 | 15° | 20° |
| θ_b3 | 25° | 30° |
| W_b1 | 6 mm | 8.3 mm |
| W_b2 | 5 mm | 6.5 mm |
| W_b3 | 3 mm | 4 mm |
| L_b1 | 20 mm | 30 mm |
| L_b2 | 20 mm | 25 mm |
| L_b3 | 10 mm | 16 mm |
| p_b1 | 20 mm | 23 mm |
| p_b2 | 9 mm | 13.6 mm |
| p_b3 | 8 mm | 11.8 mm |
| radii | — | 25% of W_b |

## Results (numerical)

### Performance at Optimal Current Angle (FEM)

| Metric | Case 1 | Case 2 | Case 3 | Case 4 | Case 5 |
|--------|--------|--------|--------|--------|--------|
| Optimal current angle | 52.11° | 52.11° | 52.11° | 56.8° | 56.8° |
| Output power [W] | 5385 | 5097 | 5212 | 5273 | 5221 |
| Torque ripple [%] | 7.4 | 6.5 | 7.9 | 5.85 | 10.58 |
| Power factor | 0.6297 | 0.6185 | 0.6182 | 0.6628 | 0.6555 |
| Saliency ratio | 5.36 | 4.84 | 4.80 | 5.25 | 5.06 |

### Rotor Iron Volume

| Case | Volume [m³] |
|------|-------------|
| 1 | 1.780 × 10⁻⁴ |
| 2 | 1.763 × 10⁻⁴ |
| 3 | 1.932 × 10⁻⁴ |
| 4 | 1.736 × 10⁻⁴ |
| 5 | 1.842 × 10⁻⁴ |

### Key Comparisons

- **Case 1 vs Case 3:** +3.32% output power, −6.3% torque ripple, +11.7% saliency ratio
- **Case 4:** Lowest torque ripple (5.85%) and lowest iron volume (fastest dynamics)
- **Case 4 vs reference [26] (56.5°):** Power factor of 0.6628 vs prior ~0.62; torque ripple 5.85% vs ~12%
- **Torque ripple at 45° vs 56.5°:** 34.2% reduction

### Experimental Validation (Case 4 prototype)

- Prototype: 5.5 kW, 36-slot stator, 4-pole rotor
- Coupled to 10 kW induction motor (torque control mode)
- Inverter: 6.6 kHz switching, 600 V DC bus, SVM control
- Measured vs simulated torque showed good agreement at half speed/current
- Torque linear with current up to 2× rated
- Power factor showed step-change with current due to shifting optimal current angle
- Efficiency map confirmed operation across speed range including flux weakening

## Limitations / Caveats

- **2D FEM only:** 3D effects (skewing, end-winding, axial flux variation) not modeled. Unverified whether 3D effects would change optimal geometry rankings.
- **Iron loss model accuracy:** Experimental efficiency showed slight deviation from simulation due to neglected mechanical/switching losses and inaccurate iron loss model parameters (noted by authors).
- **No rotor saturation in cost function:** The cost function (Eq. 10) does not explicitly penalize saturation; saturation is only implicitly captured through the current angle range.
- **Single machine frame:** Results validated on one specific 5.5 kW frame. Generalization to other power levels or slot/pole combinations is unverified.
- **No structural analysis:** Mechanical integrity of flux barriers (stress, critical speed) not evaluated during optimization.
- **Population size fixed at 210:** No convergence analysis for different population sizes.

## Propagation Into Wiki

- [[flux_barrier_parameters]] — add the 12-parameter rotor geometry model and variable bounds from Table 2
- [[SynRM]] — update with current-angle optimization insights and the 3.32% power improvement finding
- [[torque_ripple_reduction]] — add the 34.2% reduction by current angle selection and Case 4 result (5.85%)
- [[optimize_synrm_v4|existing optimization workflows]] — cross-reference PSOGWO as an alternative to the current optimizer
- [[saliency_ratio]] — update with measured values (4.8–5.36 across cases)
- [[motor_design_guidelines]] — add guideline: always include current angle as a variable in SynRM optimization
- [[electrical_steel|M270-50A / M330-50A]] — note material grades used in this study

## Related Pages

- [[SynRM]]
- [[flux_barrier_parameters]]
- [[torque_ripple_reduction]]
- [[saliency_ratio]]
- [[optimize_synrm_v4]]
- [[motor_design_guidelines]]
- [[Ibrahim_2016]] — prior work referenced as baseline (current angle 56.5°, torque ripple ~12%)
