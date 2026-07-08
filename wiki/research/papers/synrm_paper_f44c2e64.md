---
type: research_paper
title: "Rotor Design Optimization of Permanent Magnet–Assisted Synchronous Reluctance Machines for Traction Applications"
authors: "Mohammad Hossain Mohammadi"
year: "2015"
venue: "McGill University — Master of Engineering Thesis"
doi: ""
motor_types: ["SynRM", "PM-assisted SynRM", "IPM"]
topics: ["rotor design optimization", "torque ripple reduction", "surrogate modelling", "Pareto optimization", "multi-objective genetic algorithm", "flux barrier geometry", "permanent magnet assist", "traction motors", "robustness analysis", "FEA validation"]
topologies: ["TLA (Transversally-Laminated Anisotropic)", "single-barrier", "double-barrier", "PM-assisted double-barrier"]
source_files: ["raw/papers/f44c2e64-a3f1-43d7-92dd-375db1563be0.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: ["dq_voltage_current_flux", "torque_components", "saliency_ratio", "mpf_condition", "mpf_angle", "voltage_limit", "current_limit", "average_torque", "torque_ripple", "rotor_insulation_ratio", "full_factorial_sampling", "moa_objective", "minimum_volume_ellipse", "pm_area_constraint", "current_sum_constraint", "objective_sensitivity", "transient_fea_pde", "maxwell_stress_torque", "vs_max_from_vdc"]
concepts_updated: ["SynRM", "PM-assisted SynRM", "IPM parameter plane", "MTPA", "flux weakening", "MTPV", "insulation ratio", "Pareto front", "surrogate modelling", "torque ripple", "saliency ratio", "power factor"]
motorcad_relevance: "Highly relevant — provides complete rotor design optimization methodology for SynRM/PM-assisted SynRM rotors using FEA. Covers flux barrier geometry (single/double barrier), permanent magnet insertion strategy, torque ripple minimization via asymmetric barriers, insulation ratio matching, and MTPA/FW control analysis. The optimization framework (global via MOGA + local refinement) and robustness analysis are directly applicable to PyMotorCAD workflows."
confidence: Verified
---

# Rotor Design Optimization of PM-Assisted Synchronous Reluctance Machines for Traction Applications

## Citation

Mohammad Hossain Mohammadi, "Rotor Design Optimization of Permanent Magnet–Assisted Synchronous Reluctance Machines for Traction Applications," Master of Engineering Thesis, Department of Electrical and Computer Engineering, McGill University, Montreal, Quebec, Canada, November 2015.

## Why This Paper Matters

This thesis presents a **complete, computationally efficient methodology** for optimizing PM-assisted SynRM rotors — from global search to local refinement to PM insertion — validated against an industrial direct-drive motor (TM4 Sumo MD). It directly addresses the core challenge in [[SynRM]] design: balancing high torque density with low torque ripple and acceptable power factor, while reducing reliance on expensive rare-earth magnets.

Key contributions for our project:
1. **Global optimization algorithm** using BRNN surrogates + MOGA to find Pareto-optimal single-barrier rotors with minimal FEA calls
2. **Ellipse constraint** analytically capturing the high-torque region of the design space — usable to restrict sampling in multi-barrier designs
3. **Single-to-multiple barrier generalization** via linear width summation, validated with FEA
4. **PM insertion strategy** using low-cost Ceramic 10 or bonded NdFeB magnets, with geometry optimization of angled flux barriers
5. **Robustness analysis** showing torque ripple is far more sensitive to parameter variations than average torque
6. **IPM parameter plane analysis** comparing [[PM-assisted SynRM]] vs [[IPM]] torque/speed characteristics

## Problem Statement

Rare-earth permanent magnet price volatility drives the search for cheaper motor topologies. A pure [[SynRM]] has low material cost and simple rotor manufacturing, but suffers from:
- Low [[power factor]] → requires inverter kVA oversizing
- Limited [[constant power speed range]] (CPSR) → poor flux-weakening capability
- High [[torque ripple]] → NVH issues

Adding low-cost PMs inside the SynRM rotor (PM-assisted SynRM) addresses these, but finding an optimal design is computationally expensive due to nonlinear FEA requirements and a high-dimensional geometric search space.

## Machine / Study Context

**Reference motor:** TM4 Sumo MD — a high-torque, low-speed direct-drive SMPM motor for heavy-duty HEVs (city buses, delivery trucks).

| Specification | Value |
|---|---|
| $T_{avg}^{MAX}$ | 2100 Nm |
| $T_{avg}^{CONT}$ | 1000 Nm |
| $P_{FW}^{MAX}$ / $P_{FW}^{CONT}$ | 200 / 180 kW |
| $\eta^{MAX}$ | 95.0% |
| $N_{max}$ | 3100 RPM |

**Initial IPM motor** (inner rotor, V-shaped NdFeB PMs) modeled to fix volume/stator for rotor-only optimization:

| Parameter | Value |
|---|---|
| Stator slots $n_s$ | 33 |
| Stator OD $D_{so}$ | 325 mm |
| Stack length $l_{stk}$ | 275 mm |
| Air gap $W_{ag}$ | 0.75 mm |
| Rotor OD $D_{ro}$ | 220 mm |
| Rated line current $I_{rated}$ | 470 Arms |
| DC voltage $V_{dc}$ | 450 V |
| Rated speed $N_{base}$ | 700 RPM |
| Continuous torque $T_{avg}^{CONT}$ | 967 Nm |
| FW output power $P_{FW}$ | 160 kW |

**NdFeB PM cost:** $409.50 (~60% of total material cost of $704.60). The optimization seeks to replace these with cheaper alternatives.

**8-pole TLA rotor** selected as optimal configuration ($n_s/n_p = 33/8 = 4.125$ — asymmetric barrier arrangement gives lowest torque ripple).

## Method / Theory

### Overall Algorithm

Two-step approach:
1. **Global optimization** of a single-barrier SynRM rotor → find Pareto front + ellipse constraint
2. **Local optimization** of a multiple-barrier rotor → generalize from single-barrier space, insert PMs

### Control Strategies Used

- **MTPA (Maximum-Torque-per-Ampere):** Optimizes advance angle $\gamma$ for maximum torque at given $I_s$ — primary strategy for all FEA evaluations
- **Flux Weakening (FW):** Analyzed via current-limit circle + voltage-limit ellipse in the $(I_d, I_q)$ plane
- **MTPV (Maximum-Torque-per-Volt):** Theoretical limit at infinite speed

### Design Variables (Single-Barrier)

Continuous: flux carrier width $W_c$, flux barrier width $W_b$ (per rotor pole)
Discrete: number of rotor poles $n_p \in \{4, 8, 10\}$

Feasibility constraint: $W_c + W_b \le W_{lim}$ (convex triangle)

### Optimization Pipeline

1. **Sampling:** Full factorial within feasibility triangle (90 points per $n_p$)
2. **FEA data acquisition:** 2D time-stepping FEA, 1/6 electrical period, 48 samples
3. **Surrogate modelling:** BRNN (Bayesian Regularization Backpropagation Neural Network) — 5 neurons for $T_{avg}$, 40 for $T_{rip}$
4. **Multi-objective optimization:** MOGA (population=100, max generations=600, 10 independent runs)
5. **Ellipse constraint:** Minimum Volume Ellipsoid covering high-$T_{avg}$ Pareto solutions
6. **Validation:** Cross-check MOGA predictions against direct FEA

## Important Equations

### dq-Axis Stator Current (eq. 1)

$$\bar{I}_s = \begin{bmatrix} I_d \\ I_q \end{bmatrix} = I_s \begin{bmatrix} -\sin\gamma \\ +\cos\gamma \end{bmatrix}$$

- **Variables:** $I_s$ = stator current magnitude [A], $\gamma$ = current advance angle measured CCW from q-axis [° or rad], $I_d, I_q$ = dq-axis stator currents [A]
- **Units:** Currents in Amperes, angle in degrees or radians
- **Assumptions:** Balanced 3-phase operation, no field/damper windings, no cross-coupling

### dq-Axis Stator Flux Linkage (eq. 2)

$$\bar{\lambda}_s = \begin{bmatrix} \lambda_d \\ \lambda_q \end{bmatrix} = \begin{bmatrix} L_d & 0 \\ 0 & L_q \end{bmatrix} \bar{I}_s + \begin{bmatrix} \lambda_m \\ 0 \end{bmatrix}$$

- **Variables:** $L_d, L_q$ = dq-axis stator self-inductances [H], $\lambda_m$ = PM flux linkage [V·s], $\lambda_d, \lambda_q$ = dq-axis flux linkages [V·s]
- **Assumptions:** No cross-coupling between dq-axes, no core losses

### dq-Axis Stator Voltage (eq. 3)

$$\bar{V}_s = \begin{bmatrix} V_d \\ V_q \end{bmatrix} = \begin{bmatrix} R_s + pL_d & -\omega_e L_q \\ \omega_e L_d & R_s + pL_q \end{bmatrix} \begin{bmatrix} I_d \\ I_q \end{bmatrix} + \begin{bmatrix} 0 \\ \omega_e \lambda_m \end{bmatrix}$$

- **Variables:** $R_s$ = stator winding resistance [Ω], $\omega_e$ = electrical angular speed [rad/s], $p$ = time derivative operator
- **Assumptions:** Steady-state (p→0 for DC analysis), no core losses, no damper windings

### Electromagnetic Torque (eq. 4–5)

$$\bar{T}_{em} = \frac{3}{2} n_p (\bar{\lambda}_s \times \bar{I}_s) = \frac{3}{2} n_p (\lambda_d I_q - \lambda_q I_d) \hat{z}$$

$$\bar{T}_{em} = \underbrace{\frac{3}{2} n_p \lambda_m I_s \cos\gamma}_{T_{pm}} + \underbrace{\frac{3}{2} n_p \frac{1}{2}(L_q - L_d) I_s^2 \sin 2\gamma}_{T_{rel}}$$

- **Variables:** $T_{em}$ = electromagnetic torque [Nm], $n_p$ = number of rotor poles, $T_{pm}$ = PM torque component [Nm], $T_{rel}$ = reluctance torque component [Nm]
- **Key insight:** PM torque ∝ $\cos\gamma$, reluctance torque ∝ $\sin 2\gamma$ — maximizing both requires careful $\gamma$ selection. For pure SynRM ($\lambda_m = 0$): only $T_{rel}$ exists. For pure PM ($L_d = L_q$): only $T_{pm}$ exists.
- **Assumptions:** 3-phase motor, no core losses, no cross-coupling

### Magnetic Saliency Ratio (eq. 6)

$$\xi = L_q / L_d$$

- **Variables:** $\xi$ = magnetic saliency ratio [dimensionless]
- **Notes:** $\xi > 1$ for reluctance machines, $\xi = 1$ for pure PM machines. Higher $\xi$ → higher power factor and reluctance torque. TLA rotors: typically $\xi < 10$ under saturation.

### Maximum Power Factor (eq. 10–11)

$$\cos\phi^{MPF} = \frac{\xi - 1}{\xi + 1}$$

$$\gamma^{MPF} = \tan^{-1}\sqrt{\xi}$$

- **Variables:** $\cos\phi$ = power factor, $\gamma^{MPF}$ = advance angle at MPF [°]
- **Example:** For $\xi = 7$: $\cos\phi^{MPF} \approx 0.75$, $\gamma^{MPF} \approx 69°$
- **Key insight:** Power factor is fundamentally limited by saliency ratio in pure SynRMs. PM flux linkage is needed to improve power factor toward unity.

### Voltage-Limit Ellipse (eq. 14–15)

$$\left(\frac{V_s}{\omega_e L_d}\right)^2 = I_q^2 + \xi^2 \left(I_d + \frac{\lambda_m}{L_d}\right)^2$$

$$V_s^{MAX} = \frac{2}{\pi} V_{dc}$$

- **Variables:** $V_s$ = per-phase voltage magnitude [V], $V_{dc}$ = DC bus voltage [V]
- **Notes:** Ellipse centered at $(-\lambda_m/L_d, 0)$ in the $(I_d, I_q)$ plane. Higher $\xi$ stretches ellipse along d-axis. Center offset from origin enables FW capability — critical for traction applications.

### Current-Limit Circle (eq. 13)

$$I_s^2 = I_d^2 + I_q^2$$

- Defines feasible $(I_d, I_q)$ operating points for given inverter current rating

### Per-Unit Torque Components (eq. 7–8)

$$T_{rel,pu} = \frac{1}{2} L_d (\xi - 1) I_s^2 \sin 2\gamma$$

$$T_{pm,pu} = \lambda_{mn} I_s \cos\gamma$$

- **Variables:** $\lambda_{mn} = \lambda_m / \lambda_s$ = normalized PM flux linkage [pu]
- **Use:** IPM parameter plane analysis — two independent parameters $(\xi, \lambda_{mn})$ fully characterize drive behavior

### Rotor Insulation Ratio (eq. 16)

$$k_{air,r} = \frac{W_b}{(D_{ro} - D_{ri})/2}$$

- **Variables:** $W_b$ = total insulation (barrier) width [mm], $D_{ro}$ = rotor outer diameter [mm], $D_{ri}$ = rotor inner diameter [mm]
- **Key insight:** For balanced saturation, $k_{air,r} \approx k_{air,s}$ (stator insulation ratio). If $k_{air,r} < k_{air,s}$, rotor saturation dominates → higher torque, higher ripple, lower power factor. Optimal range: $k_{air,r} \in [0.3, 0.5]$.

### Average Torque & Torque Ripple (eq. 24–25)

$$T_{avg}(\bar{W}) = \frac{1}{N} \sum_{i=1}^{N} T_i$$

$$T_{rip}(\bar{W}) = \frac{|\max(T) - \min(T)|}{T_{avg}(\bar{W})}$$

- **Variables:** $T_i$ = instantaneous torque at sample $i$ [Nm], $N$ = number of samples per period
- **Notes:** $T_{avg}$ is insensitive to FEA accuracy setting; $T_{rip}$ is highly sensitive (drops from 125% to 11% as setting increases from 1 to 3)

### Full Factorial Sampling (eq. 21)

$$n = \prod_{i=1}^{m} l_i$$

- **Variables:** $m$ = number of design variables, $l_i$ = number of levels per variable
- **For this work:** $m=2$ variables, $l_i=13$ levels → 169 points → 90 feasible (after triangle constraint)

### Multi-Objective Optimization Formulation (eq. 26–27)

$$\min \left(-T_{avg}(\bar{W}),\; T_{rip}(\bar{W})\right)$$
$$\text{s.t. } \bar{W} \in \mathcal{F}_{\Delta}, \quad n_p \in \{4, 8, 10\}$$

- **Implementation:** $T_{avg}$ multiplied by $-1$ so both objectives are minimized. Population: 100 individuals, max 600 generations, 10 independent runs per current level.

### Minimum Volume Ellipsoid (eq. 29–30)

$$\max \sqrt{\det \bar{\bar{A}}}$$
$$\text{s.t. } \|\bar{\bar{A}}\,\bar{W} + \bar{b}\|_2 \le 1$$

- **Variables:** $\bar{\bar{A}}$ = matrix governing ellipse eccentricity, $\bar{b}$ = vector governing ellipse center
- **Purpose:** Analytically encloses all high-$T_{avg}$ Pareto solutions in design space. Solved via CVX (convex optimization tool in MATLAB). Validates that optimal single-barrier solutions cluster in an elliptical region.

### Multiple-Barrier Width Summation (eq. 32)

$$W_{c/b} = \sum_{k=1}^{n_b} W_{c/b_k}$$

- **Variables:** $n_b$ = number of barriers, $W_{c_k}, W_{b_k}$ = carrier/barrier widths for barrier $k$
- **Use:** Maps double-barrier $(W_c^1, W_b^1, W_c^2, W_b^2)$ to single-barrier $(W_c, W_b)$ space for comparison

### PM Area Constraint (eq. 33)

$$\sum_{k=1}^{n_b} (W_{i_k} + W_{o_k}) W_{c_k} \le A_{lim}$$

- **Variables:** $W_{i_k}$ = inner magnet width [mm], $W_{o_k}$ = outer magnet width [mm], $A_{lim}$ = PM area limit per rotor pole [mm²]
- **Notes:** Fixes total PM volume; inner magnets maximized first (produce most PM torque), then outer magnets varied.

### Current Sum Constraint (eq. 34)

$$i_s^C(t) = -i_s^A(t) - i_s^B(t)$$

- Used in robustness analysis for 3-phase current imbalance ($\pm 5\%$ variation in $I_s^A$, $I_s^B$)

### Objective Sensitivity (eq. 35)

$$\Delta f_r = \frac{|\max(f) - \min(f)|}{|f_{nom}|}$$

- **Variables:** $\Delta f_r$ = relative objective sensitivity [%], $f_{nom}$ = nominal objective value
- **Use:** Quantifies robustness of $T_{avg}$ and $T_{rip}$ to parameter variations

### Transient 2D FEA PDE (eq. 17)

$$\vec{\nabla} \times (\vec{\mu}^{-1} \cdot \vec{\nabla} \times \vec{A}) + \vec{\sigma} \cdot \left(\frac{\partial \vec{A}}{\partial t} - \vec{v} \times \vec{\nabla} \times \vec{A}\right) = -\vec{\sigma} \cdot \vec{\nabla} V$$

- **Variables:** $\vec{A}$ = magnetic vector potential [T·m], $\vec{\mu}$ = magnetic permeability [T·m/A], $\vec{\sigma}$ = electrical conductivity [S/m], $\vec{v}$ = velocity [m/s], $V$ = electric scalar potential
- **Method:** Solved via Galerkin's method with triangular mesh elements

### Maxwell Stress Tensor Torque (eq. 20)

$$T_i = \frac{l_{stk}}{\mu_0} \int_0^{2\pi} r^2 B_r B_t \, d\varphi$$

- **Variables:** $l_{stk}$ = stack length [m], $\mu_0$ = permeability of free space [T·m/A], $r$ = integration path radius [m], $B_r, B_t$ = radial/tangential flux density [T]

### MTPA Per-Unit Torque (eq. 7–8)

See Per-Unit Torque Components above. The MTPA condition maximizes total torque for given $I_s$ by optimizing $\gamma$.

## Key Design Insights

1. **8-pole TLA rotor is optimal** for 33-slot stator ($n_s/n_p = 4.125$ — fractional slot-per-pole gives asymmetric barriers → lowest ripple). 4-pole and 10-pole configurations have significantly higher $T_{rip}$.

2. **Insulation ratio matching:** $k_{air,r} \approx k_{air,s}$ ensures balanced stator/rotor saturation. For 33-slot stator: $k_{air,s} = 0.47$, achieved 8-pole design: $k_{air,r} = 0.44$ at 2.0$I_{rated}$.

3. **Single-barrier → double-barrier generalization works:** Linear width summation ($W_{c/b} = W_{c/b}^1 + W_{c/b}^2$) maps double-barrier designs into single-barrier space with <0.04 pu center shift. Ellipse constraint from single-barrier space effectively restricts double-barrier sampling.

4. **Torque ripple drops ~50% with double barrier:** Single-barrier $T_{rip} = 12.0\%$ → double-barrier $T_{rip} = 6.0\%$ at 2.0$I_{rated}$. Average torque increases ~3% (842 → 864 Nm).

5. **PM assist is essential for traction:** Pure SynRM cannot meet torque-to-volume and CPSR requirements. Adding low-cost PMs (bonded NdFeB, 0.8T) brings power factor from ~0.43 (pure SynRM) to 0.935 and FW power to 174 kW (meets 180 kW requirement).

6. **Cheaper PMs outperform expensive ones at high load:** 2B-PMa SynRM with bonded NdFeB produces more torque at high currents than initial IPM with sintered NdFeB, because optimized reluctance torque dominates overloaded conditions.

7. **Torque ripple is the most sensitive objective:** Robustness analysis shows $T_{rip}$ sensitivity: 24.9% (geometric), 25.9% (magnet $B_r$), 44.2% (current imbalance) — while $T_{avg}$ sensitivity stays below 8.3% across all variations.

8. **BRNN with 40 neurons needed for $T_{rip}$** (multimodal response surface with peaks/valleys), while only 5 neurons suffice for $T_{avg}$ (smooth unimodal surface).

9. **FEA Speed/Accuracy setting of 3** is the optimal tradeoff — torque ripple converges above setting 3, but computational cost grows exponentially.

10. **Inner PMs contribute most to PM torque** — verified by robustness analysis showing $B_r^1$ (inner magnet) has highest sensitivity impact.

## Optimization Setup

### Objectives
- **Maximize** average torque $T_{avg}$ [Nm]
- **Minimize** torque ripple $T_{rip}$ [%]

### Design Space
| Variable | Type | Range |
|---|---|---|
| $W_c$ (flux carrier width) | Continuous | $[W_l, W_{lim}]$ per pole |
| $W_b$ (flux barrier width) | Continuous | $[W_l, W_{lim}]$ per pole |
| $n_p$ (number of poles) | Discrete | $\{4, 8, 10\}$ |
| $W_c + W_b \le W_{lim}$ | Constraint | Linear sum |

### Sampling & Evaluation
- Full factorial: 90 feasible points per $n_p$ → 270 total rotor models
- FEA: 2D time-stepping, 1/6 electrical period, 48 samples, Speed/Accuracy = 3
- Current levels: 50%, 100%, 200% of $I_{rated}$
- MTPA peak finding algorithm (iterative quadratic fit)

### Surrogate Model
- BRNN (Bayesian Regularization Backpropagation Neural Network)
- Single hidden layer: 5 neurons ($T_{avg}$), 40 neurons ($T_{rip}$)
- Training/validation/testing: 60%/25%/15%
- $R^2_{test} > 0.95$ for all objectives

### Multi-Objective Optimization
- MOGA: population=100, max generations=600
- 10 independent runs per current level
- Pareto front extracted from combined runs

### Local Optimization (Double-Barrier)
- Latin Hypercube sampling: 188 points within/around ellipse constraint
- Barrier refinement: circular → angled flux barriers
- PM insertion: 6 rectangular magnets per pole, $A_{lim}$ constraint
- PM orientation optimization: $\theta^1, \theta^2 \in [40°, 65°]$ in 5° steps

## Results (numerical)

### Single-Barrier Pareto Front (8-pole, max $T_{avg}$)

| $I_s / I_{rated}$ | $T_{avg}$ [Nm] | $T_{rip}$ [%] | $k_{air,r}$ |
|---|---|---|---|
| 0.5 | 271 | 6.8 | 0.20 |
| 1.0 | 526 | 13.3 | 0.39 |
| 2.0 | 842 | 12.0 | 0.44 |

### Double-Barrier Improved Design (8-pole)

| $I_s / I_{rated}$ | $T_{avg}$ [Nm] | $T_{rip}$ [%] | $k_{air,r}$ |
|---|---|---|---|
| 0.5 | 284 | 6.0 | — |
| 1.0 | 543 | 7.4 | — |
| 2.0 | 864 | 6.0 | 0.45 |

### 2B-PMa SynRM with Ceramic 10 (0.4T)

| $I_s / I_{rated}$ | $T_{avg}$ [Nm] | $T_{rip}$ [%] |
|---|---|---|
| 0.5 | 428 | 8.92 |
| 2.0 | 1360 | 2.33 |

### Final Design Comparison (2B-PMa SynRM with bonded NdFeB, 0.8T)

| Metric | TM4 Sumo MD | Initial IPM | 2B-PMa SynRM |
|---|---|---|---|
| Volume [L] | 22.81 | — | — |
| $T_{avg}^{MAX}$ [Nm] | 2100 | 1468 | 2231 |
| $T_{rip}$ [%] | — | 6.15 | 2.67 |
| $T_{avg}^{CONT}$ [Nm] | 1000 | 1389 | 1122 |
| $P_{FW}^{CONT}$ [kW] | 180 | 160 | 183 |
| $\eta^{MAX}$ [%] | 96.0 | 95.0 | 95.5 |
| $\cos\phi$ (at 0.5$I_{rated}$) | — | 0.925 | 0.935 |

### Power-Speed Characteristic
- 2B-PMa SynRM peaks at **174 kW** at 1.0$I_{rated}$ in FW region → meets 180 kW continuous requirement
- Maximum speed: 3100 RPM (matches TM4 Sumo MD)

### BRNN Training Quality

| Objective | $R^2_{train}$ | $R^2_{val}$ | $R^2_{test}$ (typical) |
|---|---|---|---|
| $T_{avg}$ | 1.000 | 1.000 | 0.999+ |
| $T_{rip}$ | 0.975–0.998 | 0.950–0.985 | 0.957–0.995 |

### FEA Validation Errors

| $I_s / I_{rated}$ | $\mu(e_r)$ $T_{avg}$ | $\max(e_r)$ $T_{avg}$ | $\mu(e_r)$ $T_{rip}$ | $\max(e_r)$ $T_{rip}$ |
|---|---|---|---|---|
| 0.5 | 0.16% | 0.24% | 5.36% | 8.74% |
| 1.0 | 0.14% | 0.26% | 3.39% | 8.02% |
| 2.0 | 0.15% | 0.33% | 2.35% | 5.37% |

### Robustness Sensitivity (at 1.34$I_{rated}$)

| Variation Source | $\Delta f_r$ $T_{avg}$ [%] | $\Delta f_r$ $T_{rip}$ [%] |
|---|---|---|
| Geometric (6 params, 1 pole) | 1.82 | 24.93 |
| $B_r$ all magnets (1 pole) | 5.34 | 25.90 |
| $B_r^1$ only (8 poles) | 2.73 | 27.84 |
| Phase current $\pm 5\%$ (1 pole) | 8.24 | 44.18 |

## Limitations / Caveats

1. **Only two objectives considered:** Average torque and torque ripple. Efficiency, power factor, and cogging torque were not included as optimization objectives — adding them would increase dimensionality and computational cost.

2. **2D FEA only:** End effects ignored (justified by long stack length relative to stator OD). 3D effects may be relevant for shorter motors.

3. **No thermal modeling:** Cooling assumed liquid-cooled at fixed temperature. Temperature-dependent magnet properties not modeled during optimization (only 20°C analysis).

4. **Demagnetization ignored:** Magnet demagnetization curves considered only for material selection, not as an optimization constraint.

5. **No experimental validation:** All results validated only against FEA simulations, not physical prototypes.

6. **BRNN limitations for multimodal data:** Torque ripple's complex response surface leads to higher surrogate errors (~5% mean) compared to average torque (<0.2%). Kriging may offer better convergence.

7. **Ellipse constraint case-study specific:** Generalizability to other slot/pole combinations, motor sizes, and stator configurations not proven. Physical interpretation of the ellipse through magnetic circuit analysis remains unexplored.

8. **Single and double barrier only:** Higher barrier counts (3+) not explored but expected to further reduce ripple. Methodology is stated as extendable.

9. **PWM switching losses ignored:** Current hysteresis method used for FW analysis does not account for inverter switching losses.

10. **Lower torque-to-volume than IPM:** The 2B-PMa SynRM is physically larger than the initial IPM for equivalent torque — a trade-off for reduced rare-earth content.

## Propagation Into Wiki

- [[SynRM]] — update with rotor design methodology, saliency ratio relationships, insulation ratio guidelines
- [[PM-assisted SynRM]] — update with PM insertion strategy, magnet grade selection, angled barrier design
- [[IPM]] — update with IPM parameter plane comparison, drive class analysis
- [[torque_ripple]] — update with asymmetric barrier reduction technique, double-barrier improvement
- [[optimization]] — update with MOGA + BRNN surrogate pipeline, ellipse constraint methodology
- [[flux_barrier_design]] — new page or update covering geometric modeling, single-to-multiple barrier generalization
- [[MTPA]] — update with peak finding algorithm, advance angle optimization
- [[flux_weakening]] — update with voltage-limit ellipse analysis, FW power-speed characteristics
- [[power_factor]] — update with saliency ratio relationship, PM assist improvement
- [[insulation_ratio]] — update with $k_{air,r} \approx k_{air,s}$ guideline, rotor/stator saturation matching
- [[robustness_analysis]] — update with sensitivity methodology, torque ripple sensitivity findings
- [[motorcad_workflow]] — update with FEA validation approach, speed/accuracy tradeoff setting

## Related Pages

- [[SynRM]]
- [[PM-assisted SynRM]]
- [[IPM]]
- [[torque_ripple]]
- [[MTPA]]
- [[flux_weakening]]
- [[power_factor]]
- [[saliency_ratio]]
- [[insulation_ratio]]
- [[flux_barrier_design]]
- [[optimization]]
- [[FEA]]
- [[robustness_analysis]]
- [[motorcad_workflow]]
