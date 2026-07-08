---
type: research_paper
title: "Design of a Synchronous Reluctance Motor Drive"
authors: "T. J. E. Miller, Alan Hutton, Calum Cossar, David A. Staton"
year: "1991"
venue: "IEEE Transactions on Industry Applications"
doi: ""
motor_types: [SynRM, BLDC, IM, SRM]
topics: [synrm_design, rotor_lamination, inductance_ratio, torque_comparison, variable_speed_drive, drive_control]
topologies: [synchronous_reluctance, interior_magnet_hybrid, switched_reluctance, induction, brushless_dc_pm]
source_files: ["raw/papers/Design of a synchronous reluctance motor drive - Industry Applications, IEEE Transactions on.md"]
related_projects: [motor-deepagent]
related_experiments: []
equations_added: [synrm_torque_dq, saliency_limit_approx]
concepts_updated: [SynRM_rotor_design, flux_barrier_rib_saturation, motor_type_comparison, synrm_vs_srm, synrm_vs_im]
motorcad_relevance: "High — rotor lamination geometry with single flux barrier directly mappable to MotorCAD rotor editor; inductance ratio measurement workflow applicable to design validation; comparison data provides benchmark targets for SynRM optimization"
confidence: Verified
---

# Design of a Synchronous Reluctance Motor Drive

## Citation
Miller, T. J. E., Hutton, A., Cossar, C., and Staton, D. A., "Design of a Synchronous Reluctance Motor Drive," *IEEE Transactions on Industry Applications*, vol. 27, no. 4, pp. 656–664, Jul./Aug. 1991. (Paper IPCSD 91-17, presented at 1989 IAS Annual Meeting, San Diego, CA.)

## Why This Paper Matters
Foundational experimental comparison of SynRM against IM, SRM, and BLDC drives under identical test conditions (same stator, copper weight, frame size). Demonstrates that a simple single-barrier transverse-lamination SynRM rotor achieves ~76% of BLDC torque at equal copper loss while being magnet-free, quiet, and compatible with standard induction-motor stators and sine-wave control. The inductance ratio measurements (L_q/L_d up to 4.0) and the analytical saliency-limit formula provide baseline targets for [[SynRM_design]] optimization and [[MotorCAD]] rotor geometry sweeps.

## Problem Statement
Despite theoretical advantages — no PM cost, temperature-independent torque per ampere, compatibility with standard ac inverter hardware — the cageless synchronous reluctance motor has seen little development for variable-frequency drives. Its reputation for poor efficiency and low power factor persists. This paper investigates whether acceptable drive performance can be achieved with a manufacturable transverse-lamination rotor design, and benchmarks it against induction, switched-reluctance, and brushless dc PM motors of identical size.

## Machine / Study Context
- **Motor type:** Segmental-rotor synchronous reluctance motor (termed "SYNCHREL")
- **Stator:** 78 mm OD, 50 mm stack length, shared across all ac motor types tested (SynRM, PMH, IM)
- **Phases/poles:** 2-phase, 4-pole (SynRM and IM); 3-phase for SRM and BLDC
- **Rotor material:** Losil 800 (Fe-Si lamination steel)
- **Rotor type:** Transverse lamination, single rectangular flux barrier per pole
- **Two rotors built and tested:**
  - Rotor 1: pole arc 68.0°, airgap 0.45 mm, web width 1.0 mm — narrow webs, designed to accommodate 5.4 mm magnets
  - Rotor 2: pole arc 62.3°, airgap 0.15 mm, web width 2.5 mm — wider webs, optimized for pure reluctance operation
- **Rib width (both):** 0.5 mm
- **Flux barrier thickness (both):** 5.4 mm
- **Optional magnets:** NdFeB (1.1 T remanence) or ceramic (0.4 T) can be inserted in the barrier for PMH hybrid mode
- **Control:** Current-regulated PWM inverter, 360-pulse magnetoresistive encoder, hysteresis-type current regulators, EPROM-based sin/cos commutation
- **Test speed:** 200 rpm (low speed to minimize windage and core loss effects)
- **Comparison motors:** BLDC (calculated), PMH-1 (NdFeB), PMH-2 (ceramic), IM-1 through IM-4 (airgap 0.1–0.4 mm), SR-1 through SR-3 (airgap 0.2–0.4 mm)

## Method / Theory

### Classical SynRM Torque Production
The inverter-fed SynRM is freed from line-start constraints: no cage needed, torque angle set electronically for max torque per ampere at all operating points, and no amortisseur stability concerns. This permits design for maximum saliency without stability tradeoffs.

### Rotor Design Philosophy
The ideal reluctance rotor presents infinite permeance to q-axis flux and zero permeance to d-axis flux. The axially-laminated Cruickshank rotor [2] follows natural flux lines with thin alternating lamination/barrier layers but is difficult to manufacture. The transverse lamination with a single rectangular flux barrier is a practical compromise — simpler punching geometry, and the barrier can house optional permanent magnets (PMH hybrid mode).

### Rotor Rib and Web Design
- **Ribs** (mechanical support connecting pole pieces to shaft) must saturate at low current to minimize L_d (high d-axis reluctance)
- **Webs** must be wide enough to avoid saturation in the q-axis flux path, maximizing L_q
- Rotor 1's narrow webs (1.0 mm) caused q-axis saturation; Rotor 2's wider webs (2.5 mm) resolved this, nearly doubling L_q

### Motor Type Comparison Methodology
All motors compared at equal stator copper loss (~14 W, ~2/3 of frame dissipation capability) with copper weight normalized to 0.29 kg. BLDC used as per-unit benchmark (100%). SR motor results adjusted to equivalent copper weight using PC-SRD software but acknowledged as potentially underestimated by ~25%.

## Important Equations

### Eq. (1): Electromagnetic Torque — d-q Axis Form
$$T = \frac{m}{2} \, p \, I_d \, I_q \, (L_q - L_d)$$

**Normalized form:** $\hat{T} = \frac{m}{2} p \, \hat{I}_d \, \hat{I}_q \, (L_q - L_d) / L_{base}$

**Variables:**
- T — electromagnetic torque [N·m]
- m — number of phases
- p — number of pole-pairs
- I_d, I_q — rms phase current components along rotor d and q axes [A] (I_d negative when L_d < L_q for max torque per ampere)
- L_d, L_q — direct-axis and quadrature-axis synchronous inductances [H]
- X_d = 2πfL_d, X_q = 2πfL_q — synchronous reactances [Ω]

**Assumptions:** Sinusoidal MMF distribution; classical synchronous machine theory; torque independent of speed (when voltage boosted above constant V/Hz at low speed to compensate resistive drop). Torque per ampere maximized at 45° current angle (I_d = I_q in magnitude).

**Convention note:** The q-axis is the high-inductance axis in this paper (contrary to some line-start reluctance literature). This is consistent with the interior-magnet hybrid convention where the magnet axis is the low-inductance (d) axis, aligning with classical synchronous machine theory.

### Eq. (2): Theoretical Saliency Limit — Approximate
$$\frac{X_q}{X_d} = \frac{tR + g}{g} = \frac{tR}{g} + 1$$

**Variables:**
- X_q/X_d — saliency ratio (synchronous reactance ratio)
- t — average ratio of flux-barrier thickness to combined (lamination + barrier) thickness
- R — rotor radius [mm]
- g — airgap length [mm]

**Assumptions:** Thin laminations and barriers everywhere; infinite permeance of barrier material ignored (barriers assumed impermeable to d-axis flux); peak airgap flux density ~0.8 T, saturation ~1.7 T → t limited to ~0.5; leakage inductance adds "swamping term" to both numerator and denominator in practice; saturation further reduces achieved ratio.

**Example calculation:** With t = 0.5 and R/g ≈ 50 → theoretical maximum saliency ≈ 25. Practical values typically 10–15 due to leakage and saturation. The single-barrier transverse design achieves 2.6–4.0 (measured).

## Key Design Insights

1. **Manufacturability-saliency tradeoff:** The single transverse-lamination flux barrier achieves L_q/L_d of only 2.6–4.0, far below the theoretical limit of ~25. This is the price of simple punching geometry and the ability to accommodate optional magnets. [[Unverified]] whether multi-barrier designs would dramatically improve this in the same stator frame.

2. **Rib saturation is critical:** Ribs must saturate at low current to keep L_d low. At 0.5 mm width with Losil 800, ribs saturate effectively. This is a key design rule for [[SynRM_rotor_design]].

3. **Web width dominates L_q:** Going from 1.0 mm (Rotor 1) to 2.5 mm (Rotor 2) webs increased L_q from 28.3 mH to 41.0 mH (measured), while L_d remained nearly constant (~10.3–10.8 mH). The inductance ratio improved from 2.6 to 4.0.

4. **Airgap sensitivity:** SynRM (like SRM and IM) is sensitive to airgap length. Rotor 2 with 0.15 mm airgap achieved significantly better performance than Rotor 1 with 0.45 mm. The BLDC motor tolerates 0.4 mm airgap with no torque penalty — SynRM cannot.

5. **Torque vs BLDC baseline:** At equal stator copper loss, the best SynRM (REL-2) produces 76% of BLDC torque — matching the best IM (IM-2 at 0.2 mm gap) but with zero rotor losses. PMH-1 with NdFeB magnets achieves 213% (unfair comparison due to rare-earth magnets).

6. **SynRM vs SRM:** SRM produces ~30% more torque than SynRM at same airgap and copper, but at significantly higher noise and torque ripple. SynRM is the quiet alternative. [[synrm_vs_srm]]

7. **SynRM vs IM:** At equal airgap (0.2 mm), SynRM and IM produce comparable torque (76% of BLDC), but SynRM has negligible rotor copper losses (7.1 W rotor loss in IM at 0.1 mm gap is eliminated). [[synrm_vs_im]]

8. **Material cost competitiveness:** SynRM is slightly more cost-effective per unit torque than IM due to simpler rotor (no cage), but less cost-effective than BLDC (ferrite magnets) in the 50–200 W range. PMH-1 is penalized by expensive NdFeB magnets.

9. **Torque per inertia (T/J):** SynRM achieves 70% of BLDC T/J, 20% better than IM. SRM excels here (307–414%) due to small rotor diameter and removed material between poles.

10. **Scalability caveat:** Results are valid only for small motors (50–200 W range). Extrapolation to integral-horsepower is noted as future work but acknowledged to be nonlinear.

## Optimization Setup (if applicable)

No formal optimization algorithm was used. The paper describes an evolutionary design process with two rotor iterations:

| Parameter | Rotor 1 | Rotor 2 |
|-----------|---------|---------|
| Pole arc (°) | 68.0 | 62.3 |
| Rotor diameter (mm) | 40.5 | 41.1 |
| Airgap (mm) | 0.45 | 0.15 |
| Rib width (mm) | 0.5 | 0.5 |
| Web width (mm) | 1.0 | 2.5 |
| Flux barrier (mm) | 5.4 | 5.4 |
| L_d measured (mH) | 10.8 | 10.3 |
| L_q measured (mH) | 28.3 | 41.0 |
| L_q/L_d measured | 2.6 | 4.0 |
| L_d FEA (mH) | 10.2 | 11.3 |
| L_q FEA (mH) | 27.7 | 50.3 |

Design tools: Linear magnetic theory from [9] for analytical L_d/L_q calculation; 2D FEA for flux plots and magnetization curves; measured magnetization curves (Fig. 7) to capture saturation effects; PC-SRD for SR motor adjustments.

## Results (numerical)

### Rotor Comparison (Low-Speed Torque vs Phase Current, Fig. 8)
- Torque calculated from Eq. (1) with L_d, L_q read from measured magnetization curves at operating current
- Rotor 2 consistently outperforms Rotor 1 across full current range due to higher inductance ratio
- Saturation evident in both rotors at higher currents (L_q decreases)

### Motor Type Performance Comparison (Table II, key values at equal stator copper loss)

| Motor | Torque [mNm] | Torque [% BLDC] | T/J [%] | T/Weight [%] | T/Material Cost [%] |
|-------|-------------|-----------------|---------|-------------|---------------------|
| BLDC (baseline) | 329 | 100 | 100 | 100 | 100 |
| PMH-1 (NdFeB) | 702 | 213 | 159 | 147 | 32 |
| PMH-2 (ceramic) | 295 | 90 | 75 | 78 | 85 |
| IM-2 (0.2 mm gap) | 250 | 76 | 57 | 59 | 76 |
| SR-1 (0.2 mm gap) | 346 | 105 | 414 | 102 | 128 |
| SR-2 (0.3 mm gap) | 256 | 78 | 307 | 76 | 94 |
| REL-1 (Rotor 1) | 109 | 33 | 30 | 25 | 36 |
| REL-2 (Rotor 2) | 250 | 76 | 70 | 58 | 83 |

### Key Comparison Observations
- **PMH-1 dominates** in raw torque (213%) but at 6.5× material cost of BLDC due to NdFeB magnets
- **SR-1** matches BLDC torque (105%) and leads in T/J (414%) and T/cost (128%), but is excessively noisy at that torque level
- **REL-2 matches IM-2** torque (76%) with zero rotor losses and compatible standard stator
- **REL-1** (33%) demonstrates the severe penalty of narrow webs and large airgap — removing magnets from PMH drops torque by more than half
- **All motors** have identical stator OD (77–78 mm), stack length (44.5–50 mm), and copper weight (0.29 kg)

## Limitations / Caveats

1. **Small motor only:** Results valid for 50–200 W range. [[Unverified]] for integral-horsepower scale — nonlinear scaling effects acknowledged.
2. **Single flux barrier:** Only a simple rectangular barrier was tested. Multi-barrier or axially-laminated designs would likely achieve much higher saliency ratios. The paper notes this explicitly.
3. **Low-speed comparison only:** Tests at 200 rpm to minimize windage/core losses. High-speed performance (field weakening, efficiency maps) not evaluated.
4. **No efficiency maps:** Comparison based on torque at equal copper loss, not full efficiency characterization. IM rotor losses (up to 7.1 W) not included in the equal-loss criterion.
5. **SR motor results adjusted, not directly measured:** SR torque values recalculated using PC-SRD for equivalent copper weight; acknowledged as potentially 16–25% underestimated.
6. **Two-phase stator:** SynRM and IM tested with 2-phase winding (does not affect electromagnetic performance per authors, but differs from standard 3-phase industrial drives).
7. **Fixed current angle:** Torque angle set at 45° for max torque per ampere in simplest control mode. No field-weakening or MTPA optimization across operating envelope.
8. **No thermal analysis:** Continuous ratings based on frame dissipation capability (~55°C rise), not detailed thermal modeling.
9. **No cogging torque or torque ripple data** for the SynRM (unlike the SRM where noise/ripple is discussed qualitatively).
10. **Inductance FEA vs measured discrepancy:** L_q FEA overestimates by ~22% for Rotor 2 (50.3 vs 41.0 mH), suggesting 2D FEA underestimates leakage or 3D effects.

## Propagation Into Wiki
- [[SynRM_design]] — add transverse lamination flux barrier approach, rib/web design rules, measured L_d/L_q values as baseline
- [[SynRM_rotor_design]] — add Rotor 1 vs Rotor 2 comparison as case study in web width optimization
- [[inductance_ratio]] — add measured values (2.6–4.0) and theoretical limit formula (Eq. 2)
- [[motor_type_comparison]] — add Table II benchmark data: SynRM vs IM vs SRM vs BLDC at equal copper loss
- [[flux_barrier_design]] — add single-barrier geometry as simplest manufacturable case; note tradeoff vs multi-barrier
- [[SynRM_equations]] — add Eq. (1) torque form and Eq. (2) saliency limit
- [[synrm_vs_srm]] — SynRM produces ~30% less torque but significantly quieter; standard ac stator compatibility
- [[synrm_vs_im]] — SynRM matches IM torque with zero rotor losses; standard stator sharing
- [[motorcad_rotor_sweep]] — map single-barrier parameters (barrier thickness, rib width, web width, airgap) to MotorCAD rotor editor
- [[variable_speed_drive_control]] — add current-regulated PWM with EPROM sin/cos commutation as baseline control architecture

## Related Pages ([[wikilinks]])
- [[SynRM]]
- [[SynRM_design]]
- [[SynRM_rotor_design]]
- [[inductance_ratio]]
- [[flux_barrier_design]]
- [[motor_type_comparison]]
- [[synrm_vs_srm]]
- [[synrm_vs_im]]
- [[SynRM_equations]]
- [[PyMotorCAD]]
- [[motorcad_rotor_sweep]]
- [[variable_speed_drive_control]]
- [[interior_magnet_motor]]
- [[switched_reluctance_motor]]
- [[induction_motor]]
- [[brushless_dc_motor]]
- [[rare_earth_free_machines]]
- [[FEA_workflow]]
