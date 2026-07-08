---
type: research_paper
title: "An Optimized Rotor Design of Synchronous Reluctance Motor for Improved Torque Characteristics"
authors: "Atul Nagarkar, Srirama Srinivas"
year: "2019"
venue: "IEEE Conference (likely ECCE or IEMDC)"
doi: ""
motor_types: [SynRM]
topics: [rotor_optimization, flux_barrier_design, torque_ripple_reduction, EV_drivetrain]
topologies: [synchronous_reluctance]
source_files: ["raw/papers/An Optimized Rotor Design of Synchronous Reluctance Motor for Improved Torque Characteristics.md"]
related_projects: [motor-deepagent]
related_experiments: []
equations_added: [synrm_dq_voltage, synrm_torque_expression, stator_sizing_ratio, air_gap_length, rotor_barrier_unitless_params, air_gap_coefficients, objective_function_weighted]
concepts_updated: [SynRM_rotor_design, flux_barrier_geometry, unitless_rotor_parameters, GA_optimization_FEA]
motorcad_relevance: "High — rotor flux barrier geometry directly mappable to MotorCAD rotor editor; unitless parameters provide systematic optimization space for SynRM rotor geometry"
confidence: Verified
---

# An Optimized Rotor Design of Synchronous Reluctance Motor for Improved Torque Characteristics

## Citation
Nagarkar, A. and Srinivas, S., "An Optimized Rotor Design of Synchronous Reluctance Motor for Improved Torque Characteristics," IEEE Conference, 2019. IIT Madras.

## Why This Paper Matters
Provides a systematic, parameterized approach to SynRM rotor design using unit-less variables that decouple mutual effects of flux barrier geometry. Demonstrates a complete analytical-to-FEA workflow with GA optimization achieving ~6% torque increase and ~74% ripple reduction. The unit-less parameterization is directly applicable to [[PyMotorCAD]] rotor geometry sweeps and can serve as the basis for [[SynRM_optimization]] workflows.

## Problem Statement
SynRM offers a rare-earth-free alternative to PMSM for EV traction, but suffers from low torque density and high torque ripple. Existing rotor optimization studies explore individual parameters in isolation, failing to capture mutual effects of multiple flux barrier geometries. The paper aims to: (1) maximize average electromagnetic torque and (2) minimize torque ripple through simultaneous multi-parameter optimization.

## Machine / Study Context
- **Machine type:** 3-phase, 4-pole [[SynRM]]
- **Rated power:** 7.5 HP (5.6 kW)
- **Rated torque:** 35.6 Nm
- **Rated speed:** 1500 rpm
- **Rated current:** 11.8 A (line)
- **Rated voltage:** 415 V (line-line)
- **Stator slots:** 36 (distributed winding, kw = 0.945)
- **Flux barriers per pole:** 3
- **Frame:** IEC132 (Do = 208 mm)
- **Lamination steel:** M19
- **Stack length:** 153 mm (λ = 1.5)
- **Air gap:** 0.5 mm
- **FEA tool:** ANSYS Maxwell 2D

## Method / Theory

### SynRM d-q Model
SynRM torque production relies on reluctance difference between d-axis and q-axis (no PM excitation). The d-q voltage and flux equations are standard [[Park_transform]] equations with field/damper winding terms removed.

### Analytical Stator Design
Uses Do³L sizing expressions (Honsinger) with inner/outer diameter ratio from [Lipo 2017]. Key sizing: slot geometry, tooth width, yoke height, and turns per phase all derived from flux density limits (Bts=1.6T, Bcs=1.5T, Bcr=1.4T).

### Unit-less Rotor Parameters (Key Contribution)
Six unit-less parameters fully define flux barrier shape:
- β_wri — ratio of consecutive flux carrier widths (controls radial iron distribution)
- β_dbj — ratio of consecutive barrier widths (controls barrier depth progression)
- β_θb1 — first barrier angle relative to pole pitch
- β_θb(j+1) — ratio of consecutive barrier angles
- β_wb1 — first barrier length normalized to geometry
- β_wb(j+1) — ratio of consecutive barrier lengths

Plus two dimensional parameters (wr1, db1) derived from air-gap saturation coefficients Kair,r and Kair,s.

### Air-Gap Coefficients
Kair,r (rotor air ratio) and Kair,s (stator air ratio) must be kept equal (~0.48) for uniform saturation across machine.

### Optimization
Genetic Algorithm (GA) coupled with 2D FEA. Three objectives: (1) maximize T_avg, (2) minimize T_rip, (3) weighted multi-objective. Evaluated at single operating point (11.8A, γ=69°). Search bounds: β_dbj ∈ [0.5, 1], β_θbi ∈ [0.7, 1.3], β_wbi ∈ [0.4, 0.8].

## Important Equations

### Eq. (1)-(2): SynRM d-q Voltage Equations
$$V_{ds} = r_s I_{ds} + \frac{d\lambda_{ds}}{dt} - \omega_e \lambda_{qs}$$
$$V_{qs} = r_s I_{qs} + \frac{d\lambda_{qs}}{dt} + \omega_e \lambda_{ds}$$

**Normalized form:** Per-unit voltages: $\hat{v}_d = \hat{i}_d + p\hat{\psi}_d - \omega\hat{\psi}_q$, etc.
**Variables:** V_ds, V_qs — d/q stator voltage [V]; r_s — stator resistance [Ω]; I_ds, I_qs — d/q stator current [A]; λ_ds, λ_qs — d/q flux linkage [Wb]; ω_e — electrical rotor speed [rad/s]
**Assumptions:** Steady-state or quasi-static; balanced 3-phase; sinusoidal MMF distribution.

### Eq. (3)-(4): Flux Linkage
$$\lambda_{ds} = L_d I_{ds}, \quad \lambda_{qs} = L_q I_{qs}$$

**Variables:** L_d, L_q — d/q axis inductances [H]; L_md, L_mq — magnetizing inductances [H]; L_ls — leakage inductance [H]
**Assumptions:** No saturation coupling between axes; no PM flux (pure reluctance).

### Eq. (6): Electromagnetic Torque
$$T_e = \frac{3}{2} \frac{P}{2} (\lambda_{ds} I_{qs} - \lambda_{qs} I_{ds}) - \frac{\partial W_{mc}}{\partial \vartheta_m}$$

**Normalized form:** $\hat{T}_e = \frac{3}{2} \frac{P}{2} (\hat{\psi}_d \hat{i}_q - \hat{\psi}_q \hat{i}_d)$
**Variables:** P — number of poles; W_mc — magnetic co-energy [J]; ϑ_m — rotor mechanical position [rad]
**Assumptions:** Co-energy variation term averages to zero over one electrical cycle; ignored for average torque calculation.

### Eq. (7): Stator Inner/Outer Diameter Ratio
$$\frac{D_{is}}{D_o} = \frac{b}{a} + \frac{2K_s}{a k_{cu} J_s D_o} \pm \sqrt{\left(\frac{b}{a} + \frac{2K_s}{a k_{cu} J_s D_o}\right)^2 - \frac{1}{a}}$$

**Variables:** D_is — stator inner diameter [mm]; D_o — stator outer diameter [mm]; a, b — auxiliary parameters from Eq. (8); K_s — surface current density [A/mm]; k_cu — slot fill factor; J_s — current density [A/mm²]
**Assumptions:** M19 steel flux density limits; fixed J_s and K_s assignments.

### Eq. (11): Air Gap Length
$$g = 0.2 + 2\sqrt{D_{is} L_{sk}}$$

**Variables:** g — air gap [mm]; D_is — inner diameter [mm]; L_sk — stack length [mm]
**Assumptions:** Empirical formula from Say (1968); appropriate for medium-size machines.

### Eq. (22)-(27): Unit-less Rotor Parameters
$$\beta_{w_{ri}} = \frac{w_{r(i+1)}}{w_{ri}}, \quad \beta_{d_{bj}} = \frac{d_{b(j+1)}}{d_{bj}}, \quad \beta_{\theta_{b1}} = \frac{\theta_{b1}}{(\pi/P)}$$
$$\beta_{\theta_{b(j+1)}} = \frac{\theta_{b(j+1)}}{\theta_{bj}}, \quad \beta_{w_{b1}} = \frac{w_{b1}}{(D_{sh}/2) + w_{r1}} \cot\left(\frac{\pi}{P}\right), \quad \beta_{w_{b(j+1)}} = \frac{w_{b(j+1)}}{w_{bj}}$$

**Variables:** w_ri — width of i-th flux carrier [mm]; d_bj — width of j-th flux barrier [mm]; θ_bj — angular span of j-th barrier [rad]; w_bj — radial length of j-th barrier [mm]; D_sh — shaft diameter [mm]
**Assumptions:** 3 flux barriers per pole (i=1..3, j=1..2); barriers follow trapezoidal approximation of fluid barriers.

### Eq. (30)-(31): Air-Gap Saturation Coefficients
$$K_{air,r} = \frac{d_{b1} + d_{b2} + d_{b3}}{d_{b1} + d_{b2} + d_{b3} + w_{r1} + w_{r2} + w_{r3} + w_{r4}}$$
$$K_{air,s} = \frac{p_s - t}{p_s}$$

**Variables:** K_air,r — rotor air ratio; K_air,s — stator air ratio; p_s — stator slot pitch [mm]; t — tooth width [mm]
**Assumptions:** K_air,r = K_air,s = 0.48 for uniform saturation; derived from [Pellegrino et al. 2016].

### Eq. (33): First Barrier Width (db1)
$$d_{b1} = \frac{K_{air,r}}{1 - K_{air,r}} \cdot \frac{w_{r1} + w_{r2} + w_{r3} + w_{r4}}{1 + \beta_{d_{b1}} + \beta_{d_{b1}} \beta_{d_{b2}}}$$

**Variables:** All as above.
**Assumptions:** Derived from K_air,r constraint and unit-less parameter ratios.

### Eq. (35): First Carrier Width (wr1)
$$w_{r1} = \frac{B_{g1} D_{is}}{B_{cr} P k_{is} (1 + \beta_{w_{r1}} + \beta_{w_{r1}} \beta_{w_{r2}} + \beta_{w_{r1}} \beta_{w_{r2}} \beta_{w_{r3}})}$$

**Variables:** B_g1 — fundamental air gap flux density [T]; B_cr — rotor core flux density [T]; k_is — stacking factor
**Assumptions:** Flux conservation (φ_p from Eq. 34 = φ_p from Eq. 36); M19 B_cr = 1.4T.

### Eq. (37): Weighted Multi-Objective Function
$$F_1 = \left(\frac{T_{c-avg}}{T_{i-avg}} - \frac{T_{d-avg}}{T_{i-avg}}\right)^2 W_1 + \left(\frac{T_{c-rip}}{T_{i-rip}} - \frac{T_{d-rip}}{T_{i-rip}}\right)^2 W_2$$

**Variables:** T_c — calculated value; T_i — initial design value; T_d — desired value (38 Nm, 10%); W_1=1, W_2=2 (ripple weighted 2x)
**Assumptions:** Normalizes both objectives to initial design values; ripple penalty doubled to prioritize smooth torque.

### Eq. (21): Torque Ripple
$$T_{rip} = \frac{T_{max} - T_{min}}{T_{avg}} \times 100\%$$

## Key Design Insights

1. **Wider flux barriers** along q-axis increase reluctance torque by increasing L_d/L_q ratio, but saturation at barrier ribs limits gains.
2. **Barrier angle:** Maximum torque requires progressive widening of barrier angles (β_θb2 > 1, β_θb3 > 1). Ripple minimized when barriers are narrower and more evenly spaced.
3. **Barrier length:** Keeping β_wb1, β_wb2, β_wb3 close to each other (similar radial extent) maximizes d-axis flux path → higher T_avg.
4. **Flux carrier width (wr1):** Optimal at 6mm for this machine. Too small → rotor shaft saturation; too large → L_q increases, reducing reluctance torque.
5. **Equal carrier widths** (β_wri = 1) gives best combined torque/ripple performance — validated in sensitivity study.
6. **Round barrier ends** preferred over sharp ends for mechanical stress distribution.
7. **Three flux barriers** selected over four due to variable count and mechanical strength tradeoffs.
8. **Skew effect:** 10° skew reduces ripple to 6.27% but costs ~2.5% average torque.
9. **Multi-objective Case 3** achieves the best balance: +6% T_avg, -74% T_rip, 91.9% efficiency, 0.75 PF.

## Optimization Setup (if applicable)

| Parameter | Value |
|-----------|-------|
| Optimizer | Genetic Algorithm (GA) |
| Population size | 30 |
| Max generations | 100 |
| Crossover probability | 0.75 |
| Mutation probability | 0.05 |
| FEA tool | ANSYS Maxwell 2D |
| Compute | Intel Xeon 12-core cluster |
| Runtime | 9–12.3 hours per case |
| Operating point | 11.8A, γ = 69°, 1500 rpm |
| Objective variables | β_dbj ∈ [0.5, 1], β_θbi ∈ [0.7, 1.3], β_wbi ∈ [0.4, 0.8] |
| Fixed parameters | β_wri = 1, wr1 = 6mm, wtr = wrr = 1mm, K_air,r = 0.48, bec_i = bo |

## Results (numerical)

### Initial Design vs Optimized Cases

| Metric | Initial | Case 1 (Max T) | Case 2 (Min Ripple) | Case 3 (Multi-obj) |
|--------|---------|----------------|--------------------|--------------------|
| T_avg [Nm] | 34.42 | 37.23 (+8.2%) | 31.58 (-8.3%) | 36.47 (+6.0%) |
| T_rip [%] | 39.13 | 42.68 (+9.1%) | 11.11 (-71.6%) | 10.21 (-73.9%) |
| Efficiency [%] | 91.2 | 91.56 | 90.74 | 91.91 |
| Power factor | 0.70 | 0.73 | 0.64 | 0.75 |

### Skew Effect on Case 1

| Skew [°] | T_avg [Nm] | T_rip [%] |
|----------|------------|-----------|
| 0 | 37.23 | 42.68 |
| 5 | 36.62 | 30.51 |
| 7.5 | 35.87 | 17.52 |
| 10 | 34.92 | 6.27 |

### FEA Verification (Initial Design)
- B_g1 = 0.82 T, B_ts = 1.65 T, B_cs = 1.55 T, B_cr = 1.5 T (close to design targets)
- T_avg = 34.42 Nm, T_rip = 39.13% at rated conditions

## Limitations / Caveats

1. **Single operating point optimization:** All three cases evaluated at one current/angle (11.8A, 69°). Performance at other load/speed points not verified — [[Unverified]] whether optimal geometry remains favorable across full torque-speed envelope.
2. **No cogging torque analysis** reported.
3. **No thermal or efficiency map** computed — only rated-point efficiency.
4. **Mechanical losses assumed at 2%** — not computed from geometry.
5. **2D FEA only:** End effects and skew modeled as post-processing correction, not 3D coupled.
6. **No experimental validation** — purely simulation-based study. [[Unverified]] vs measured hardware.
7. **No NVH or acoustic analysis.**
8. **GA convergence** not discussed — risk of local optima given limited population (30).
9. **PM-assisted SynRM** mentioned as possible extension but not explored.
10. **Stator is fixed** — rotor-only optimization may miss better overall machine designs.

## Propagation Into Wiki
- [[SynRM_design]] — add unitless parameter methodology and K_air coefficient approach
- [[flux_barrier_geometry]] — create/update with trapezoidal barrier parameterization
- [[torque_ripple_reduction]] — add barrier angle and skew findings
- [[rotor_optimization_GA]] — add GA+FEA setup details and runtime benchmarks
- [[SynRM_equations]] — add d-q model, torque expression, sizing equations
- [[air_gap_coefficients]] — new concept: K_air,r = K_air,s for uniform saturation
- [[motorcad_rotor_sweep]] — map unitless parameters to MotorCAD rotor editor variables

## Related Pages ([[wikilinks]])
- [[SynRM]]
- [[SynRM_design]]
- [[flux_barrier_geometry]]
- [[torque_ripple_reduction]]
- [[rotor_optimization_GA]]
- [[PyMotorCAD]]
- [[SynRM_optimization]]
- [[motorcad_rotor_sweep]]
- [[electric_vehicle_motors]]
- [[rare_earth_free_machines]]
- [[FEA_workflow]]
