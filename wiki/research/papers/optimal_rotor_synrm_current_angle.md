---
type: research_paper
title: "Optimal Rotor Design of Synchronous Reluctance Machines Considering the Effect of Current Angle"
authors: "Hegazy Rezk, Kotb B. Tawfiq, Peter Sergeant, Mohamed N. Ibrahim"
year: "2021"
venue: "Mathematics, 9(4), 344"
doi: "10.3390/math9040344"
motor_types: ["SynRM"]
topics: ["rotor optimization", "flux barriers", "current angle", "torque ripple", "PSOGWO"]
topologies: ["multi-barrier rotor"]
source_files: ["raw/papers/Optimal Rotor Design of Synchronous Reluctance Machines Considering the Effect of Current Angle.md"]
related_projects: []
related_experiments: []
equations_added: ["cost_function_synrm_rotor_opt", "psogwo_velocity_update", "gwo_encircling_distance", "gwo_position_update"]
concepts_updated: ["rotor_flux_barrier_design", "saliency_ratio", "torque_ripple"]
motorcad_relevance: "Directly applicable — rotor barrier parameterization (angles, widths, lengths, positions) maps to MotorCAD rotor geometry variables. Optimizable with FEM coupling."
confidence: Verified
---

# Optimal Rotor Design of Synchronous Reluctance Machines Considering the Effect of Current Angle

## Citation

Rezk, H.; Tawfiq, K.B.; Sergeant, P.; Ibrahim, M.N. Optimal Rotor Design of Synchronous Reluctance Machines Considering the Effect of Current Angle. *Mathematics* **2021**, *9*, 344. https://doi.org/10.3390/math9040344

## Why This Paper Matters

Demonstrates that treating the **current angle as a design variable** (rather than fixing it arbitrarily during optimization) yields better SynRM rotor geometries — 3.32% higher output power and significantly lower torque ripple. Most prior SynRM rotor optimization studies fixed the current angle based on a rule of thumb (45°–60°), which suboptimizes the geometry for a specific operating point rather than the true best point.

## Problem Statement

When optimizing SynRM rotor flux-barrier geometry, the **current angle** (the angle between stator current vector and the q-axis) is conventionally held fixed. This paper asks: **does treating the current angle as an optimization variable change the resulting optimal rotor geometry and its performance?**

## Machine / Study Context

| Parameter | Value |
|---|---|
| Rated power | 5.5 kW |
| Stator | 36-slot, 180 mm OD, 110 mm ID |
| Rotor | 4-pole, 109.4 mm OD, 3 flux barriers/pole |
| Steel | Stator: M270-50A, Rotor: M330-50A |
| Air gap | 0.3 mm |
| Axial length | 140 mm |
| Rated frequency | 100 Hz |
| RMS rated current | 12.3 A |
| Speed | 3000 rpm (rated) |
| Source stator | Standard induction machine stator (fixed) |

## Method / Theory

1. **Optimization algorithm**: Hybrid PSOGWO (Particle Swarm Optimizer + Grey Wolf Optimizer). Combines PSO's social-thinking exploration with GWO's local-search exploitation to avoid local minima.

2. **Optimization variables**: 12 rotor parameters + current angle:
   - Barrier angles: θ_b1, θ_b2, θ_b3
   - Barrier widths: W_b1, W_b2, W_b3
   - Barrier lengths: L_b1, L_b2, L_b3
   - Barrier positions: p_b1, p_b2, p_b3
   - Current angle (γ) — treated as variable in Cases 1, 2, 4, 5; fixed at 45° in Case 3

3. **Five optimization cases** with different current angle ranges:
   - Case 1: 30°–40°
   - Case 2: 40°–45°
   - Case 3: Fixed 45°
   - Case 4: 45°–65°
   - Case 5: 50°–55°

4. **Simulation**: 2D finite element method (FEM) coupled with PSOGWO. 210 designs per case.

5. **Experimental validation**: 5.5 kW prototype (Case 4 geometry) tested on a dynamometer with a 10 kW induction motor load, DSP1103 controller, 3-phase inverter (SVM, 6.6 kHz, 600 V DC bus).

## Important Equations

### Cost Function for Rotor Optimization
$$cost = T_r^2 + \frac{1}{T_{av}} \tag{10}$$

- **Original notation**: T_r = torque ripple (%), T_av = average torque
- **Normalized form**: min(T_r² + 1/T_av) — simultaneously minimizes ripple and maximizes average torque
- **Variables**: T_r [%], T_av [Nm]
- **Units**: Dimensionless (cost function value)
- **Assumptions**: Both objectives are equally important; the squared ripple term penalizes high-ripple designs more aggressively

### PSO Velocity Update
$$v_i^{t+1} = w \cdot v_i^t + C_1 \cdot r_1 \cdot (Pbest_i - x_i^t) + C_2 \cdot r_2 \cdot (Gbest - x_i^t) \tag{1}$$

- **Original notation**: w = inertia factor, C_1/C_2 = cognitive/social coefficients, r_1/r_2 = random [0,1], Pbest = personal best, Gbest = global best
- **Units**: Same as position variables
- **Assumptions**: Standard PSO formulation; three sections provide exploration, self-learning, and social-learning

### PSO Position Update
$$x_i^{t+1} = x_i^t + v_i^{t+1} \tag{2}$$

### GWO Encircling Mechanism
$$D = |C \cdot X_p(t) - X(t)| \tag{3}$$
$$X(t+1) = X_p(t) - A \cdot D \tag{4}$$

- **Variables**: X_p = prey position, X = wolf position, A and C = coefficient vectors

### GWO Coefficient Vectors
$$A = a \cdot (2 \cdot r_1 - 1) \tag{5}$$
$$C = 2 \cdot r_2 \tag{6}$$

- **Variables**: a reduces linearly from 2 to 0 over iterations; r_1, r_2 = random [0,1]

### GWO Hierarchy Update (Alpha, Beta, Delta)
$$D_\alpha = |C_1 \cdot X_\alpha(t) - X(t)|$$
$$D_\beta = |C_2 \cdot X_\beta(t) - X(t)|$$
$$D_\delta = |C_3 \cdot X_\delta(t) - X(t)| \tag{7}$$

$$X_1 = X_\alpha - a_1 \cdot D_\alpha$$
$$X_2 = X_\beta - a_2 \cdot D_\beta$$
$$X_3 = X_\delta - a_3 \cdot D_\delta \tag{8}$$

$$X_p(t+1) = \frac{X_1 + X_2 + X_3}{3} \tag{9}$$

- **Variables**: X_α, X_β, X_δ = positions of the three best wolves
- **Assumptions**: Alpha wolf leads; final position is average of three leadership-guided estimates

## Key Design Insights

1. **Current angle as a variable improves geometry**: Case 1 (30°–40° range) produced a rotor with 3.32% higher output power than the fixed-angle Case 3 (45°). The optimizer found a better geometry by exploring different saturation levels.

2. **Flux barrier dimensions are sensitive to current angle**: Barrier angles shifted 2°–6°, widths by ~1.5 mm, lengths by ~1.8 mm, positions by ~1.6 mm between cases. The optimal geometry is NOT unique — it depends on the operating point assumed during design.

3. **Fixed current angle = suboptimal geometry**: A fixed angle of 45° yields a different (worse) geometry than allowing the optimizer to search. The geometry optimized for 45° is not the same as one optimized for the true optimal angle.

4. **Wider current angle range → better exploration**: Case 4 (45°–65°) found lower torque ripple (5.85%) and the highest power factor (0.6628), while Case 1 found the highest output power (5385 W).

5. **Torque ripple is strongly affected by the fixed angle choice**: At 45° fixed, torque ripple was 34.2% lower than at 56.5° (from prior literature). The choice of fixed current angle during optimization materially changes the resulting design.

6. **Saturation level varies with current angle**: Case 1 geometry showed less saturated flux density distribution than other cases, suggesting the optimizer naturally selects geometries that avoid over-saturation when given current angle freedom.

7. **Convergence speed**: Cases 1 and 4 converged faster (~60–80 iterations) than the fixed-angle Case 3 (~70 iterations), suggesting current angle freedom may help the optimizer find good solutions faster.

## Optimization Setup

| Parameter | Value |
|---|---|
| Algorithm | Hybrid PSOGWO |
| Population / designs per case | 210 |
| FEM solver | 2D magnetic finite element |
| Objectives | Maximize T_av, minimize T_r |
| Cost function | T_r² + 1/T_av |
| Variable bounds | 12 rotor params (Table 2) + current angle range (Table 3) |
| Stator | Fixed (36-slot induction machine stator) |
| Constraints | Geometric feasibility (min rib thickness, no barrier overlap) |
| Validation | 5.5 kW prototype, Case 4 geometry |

### Rotor Variable Bounds

| Variable | Lower | Upper |
|---|---|---|
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
| radius_1,2,3 | — | 25% of W_b1,2,3 |

## Results (numerical)

### Optimal Geometry Comparison (Table 4 in paper)

| Metric | Case 1 (30°–40°) | Case 2 (40°–45°) | Case 3 (45° fixed) | Case 4 (45°–65°) | Case 5 (50°–55°) |
|---|---|---|---|---|---|
| θ_b1, θ_b2, θ_b3 | 9.3°, 16.27°, 27.65° | 7.36°, 19.42°, 25.98° | 7.14°, 19.89°, 26.39° | 8.82°, 16.3°, 28.39° | 7.84°, 18.66°, 25.69° |
| W_b1, W_b2, W_b3 | 8.3, 5.8, 3.425 mm | 7.7, 6.49, 3.44 mm | 6.76, 5.05, 3.49 mm | 8.3, 5.8, 4 mm | 6.71, 6.5, 3 mm |
| L_b1, L_b2, L_b3 | 25.2, 24.52, 12.38 mm | 30, 21.5, 10.26 mm | 25.6, 22.7, 11.5 mm | 30, 22.32, 15.41 mm | 26.82, 21.5, 16 mm |
| p_b1, p_b2, p_b3 | 22.06, 5.3, 4.75 mm | 22.29, 3.13, 3 mm | 22.71, 3.9, 3.17 mm | 22.93, 3.74, 3 mm | 20.95, 4.3, 3.7 mm |
| Rotor iron volume | 1.780 × 10⁻⁴ m³ | 1.763 × 10⁻⁴ m³ | 1.932 × 10⁻⁴ m³ | 1.736 × 10⁻⁴ m³ | 1.842 × 10⁻⁴ m³ |

### Performance at Rated Conditions (Table 5 in paper)

| Metric | Case 1 | Case 2 | Case 3 | Case 4 | Case 5 |
|---|---|---|---|---|---|
| Optimal current angle | 52.11° | 52.11° | 52.11° | 56.8° | 56.8° |
| Output power [W] | **5385** | 5097 | 5212 | 5273 | 5221 |
| Torque ripple [%] | 7.4 | 6.5 | 7.9 | **5.85** | 10.58 |
| Power factor | 0.6297 | 0.6185 | 0.6182 | **0.6628** | 0.6555 |
| Saliency ratio [%] | **5.36** | 4.84 | 4.8 | 5.25 | 5.06 |

### Key Numerical Takeaways

- **Best output power**: Case 1 (5385 W) — 3.32% above Case 3 (fixed 45°)
- **Best torque ripple**: Case 4 (5.85%) — 26% below Case 3
- **Best power factor**: Case 4 (0.6628) — due to higher optimal current angle (56.8°)
- **Best saliency ratio**: Case 1 (5.36) — 11.7% higher than Case 3
- **Lowest rotor iron volume**: Case 4 (1.736 × 10⁻⁴ m³) — 11% less than Case 3, meaning lower inertia and faster dynamics
- **Torque ripple at 45° vs 56.5°**: 34.2% reduction when using 45° instead of 56.5° (comparison to prior work in [26])

## Limitations / Caveats

1. **2D FEM only** — no axial effects, skewing, or 3D flux paths captured.
2. **Single stator design** — conclusions are specific to the 36-slot, 4-pole induction motor stator used. Different stator/pole combinations may yield different sensitivities.
3. **No rotor skewing considered** — skewing is a common torque ripple mitigation technique not explored here.
4. **No structural/thermal analysis** — only electromagnetic performance was evaluated. Rib thickness constraints are geometric, not structural-stress validated.
5. **Iron loss model limitations** — experimental efficiency discrepancies attributed to inaccurate iron loss parameters and neglecting mechanical/switching losses.
6. **Current angle range selection** — ranges were chosen based on literature heuristics (45°–60°); a wider or unconstrained search might yield different results.
7. **Single-objective cost function** — the weighted combination T_r² + 1/T_av is one formulation; Pareto front approaches may reveal different tradeoffs.
8. **Fixed current during operation** — the paper optimizes for a range of current angles but evaluates performance at a single operating point (rated speed/current).

## Propagation Into Wiki

- [[rotor_flux_barrier_design]] — add parameterization scheme (12 variables: angles, widths, lengths, positions) and barrier angle sensitivity to current angle
- [[synrm_optimization]] — add cost function formulation (T_r² + 1/T_av) and PSOGWO algorithm reference
- [[torque_ripple_reduction]] — add finding: 34.2% reduction by choosing 45° vs 56.5° current angle during optimization
- [[saliency_ratio]] — add measurement: saliency ratio ranges from 4.8 to 5.36 depending on current angle range used during optimization
- [[current_angle_design]] — new page or update: current angle should be treated as a variable, not fixed, during SynRM rotor optimization
- [[motorcad_rotor_parameters]] — add mapping of 12 rotor variables to MotorCAD geometry inputs

## Related Pages ([[wikilinks]])

- [[synrm_design]]
- [[flux_barrier_optimization]]
- [[torque_ripple]]
- [[saliency_ratio]]
- [[fem_simulation]]
- [[pso_optimization]]
- [[gwo_optimization]]
- [[motorcad_rotor_parameters]]
