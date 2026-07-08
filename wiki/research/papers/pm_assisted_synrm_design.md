---
type: research_paper
title: "Design of a PM-Assisted Synchronous Reluctance Motor with Enhanced Performance and Lower Cost for Household Appliances"
authors: "Yuli Bao, Chenyang Xia"
year: "2025"
venue: "Machines (MDPI), Vol. 13, 954"
doi: "https://doi.org/10.3390/machines13100954"
motor_types: ["PMaSynRM", "PM-Assisted Synchronous Reluctance Motor"]
topics: ["ferrite PM-assisted SynRM", "cost reduction", "fluid-shaped flux barriers", "torque ripple reduction", "power factor improvement", "rare-earth-free design"]
topologies: ["4-pole 3-phase", "2-layer fluid-shaped flux barriers", "ISDW stator winding", "ferrite-filled barriers with cut-off region"]
source_files: ["raw/papers/Design of a PM-Assisted Synchronous Reluctance Motor.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: ["electromagnetic_torque_pmasynrm", "ferrite_insulation_ratio"]
concepts_updated: ["torque_ripple", "power_factor", "fluid_shaped_barriers", "ferrite_PM", "cost_optimization", "cut_off_region"]
motorcad_relevance: "Highly relevant — rotor geometry optimization (barrier angles, cut-off parameters, insulation ratio) directly applicable to Motor-CAD parametric sweeps. Ferrite vs rare-earth cost comparison and torque ripple sensitivity maps inform motorcad/parameters constraints. Structural FEA workflow (ANSYS) complements Motor-CAD electromagnetic analysis."
confidence: Verified
---

# Design of a PM-Assisted SynRM with Enhanced Performance and Lower Cost for Household Appliances

## Citation

Bao, Y. & Xia, C. (2025). "Design of a PM-Assisted Synchronous Reluctance Motor with Enhanced Performance and Lower Cost for Household Appliances." *Machines*, 13(10), 954. https://doi.org/10.3390/machines13100954

## Why This Paper Matters

This paper demonstrates a **rare-earth-free** PMaSynRM that **outperforms** a rare-earth benchmark on every key metric — power factor, efficiency, torque quality — while cutting rotor material cost by 59.6%. For [[motor-deepagent]], this matters because:

1. It proves **ferrite-only designs can beat rare-earth designs** with the right barrier geometry — relevant for [[motorcad/parameters]] cost constraints.
2. The **fluid-shaped flux barrier** approach using Joukowski air potential functions is a concrete, reproducible rotor geometry technique applicable to Motor-CAD barrier shape parametrization.
3. The **MOGA-II multi-objective optimization** (maximize average torque, minimize torque ripple) is directly applicable to [[motorcad/workflow]] optimization setups.
4. The **cut-off region sensitivity analysis** shows torque ripple can vary by 3x depending on geometric parameters — critical for [[known_issues]] around torque ripple sensitivity.
5. Both motors were **manufactured and experimentally validated** on a SUGAWARA dynamometer, providing ground-truth FEA-vs-experiment benchmarks.

## Problem Statement

Conventional PMaSynRMs with rectangular sintered rare earth PMs (e.g., N30H NdFeB) achieve good performance but at high cost due to rare-earth pricing ($68.5/kg). Conventional PMaSynRMs with only sintered ferrite have limited power factor and efficiency. **Can a ferrite-only PMaSynRM with optimized barrier geometry outperform a rare-earth PMaSynRM on electromagnetic performance while reducing cost?**

## Machine / Study Context

- **Application:** Household appliances (cost-sensitive, mass production)
- **Comparison:** Two 4-pole, 3-phase machines with identical stators
  - **M1 (Benchmark):** Conventional HP-PMaSynRM — 3 rectangular rare earth PMs (N30H) per flux barrier, 3 barrier layers
  - **M2 (Proposed):** Novel HP-PMaSynRM — 2 fluid-shaped flux barriers filled with sintered ferrite (Y-40) + cut-off region
- **Stator:** Single-layer integral slot distributed winding (ISDW), selected for maximum saliency ratio
- **Speed range:** 100–5400 rpm (rated), max 7200 rpm
- **Controller:** Cheap STM32-based (for economic validation)

### Key Material Properties

| Property | N30H (Rare Earth) | Y-40 (Ferrite) | Unit |
|----------|-------------------|----------------|------|
| Remanence Br | — | 0.45 | T |
| Coercivity Hcb | — | 342.4 | kA/m |
| Intrinsic coercivity Hcj | — | 357.26 | kA/m |
| Demagnetization knee Bmd | — | 0.12 | T |
| Unit price | 68.5 | 10.96 | US$/kg |

### M1 Baseline Parameters

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Rotor outer diameter | D_re | 53.3 | mm |
| Rotor inner diameter | D_ri | 12.96 | mm |
| Pole pairs | p | 2 | — |
| Radial rib thickness | W_rad | 0.45 | mm |
| Tangential rib thickness | W_tan | 0.45 | mm |
| 1st layer PM width | W_pm1 | 5.4 | mm |
| 1st layer PM height | h_pm1 | 1.8 | mm |
| 2nd layer PM width | W_pm2 | 10.8 | mm |
| 2nd layer PM height | h_pm2 | 2.4 | mm |
| 3rd layer PM width | W_pm3 | 10.8 | mm |
| 3rd layer PM height | h_pm3 | 2.4 | mm |
| Rated torque | T_av | 1.9 | Nm |
| Rated speed | omega | 5400 | rpm |
| Rated power | P_out | 1074.4 | W |
| DC-link voltage | V_dc | 310 | V |
| Rated phase current | I_ph | 3.4 | Arms |
| Rated phase voltage | V_ph | 118.6 | Vrms |
| Power factor | PF | 0.925 | — |
| Copper loss | P_cu | 37.89 | W |
| Iron loss | P_fe | 30.2 | W |
| Efficiency | eta | 94.04 | % |
| Torque ripple | T_rip | 14.57 | % |

### M2 Optimized Parameters

| Parameter | Symbol | Value | Unit | Optimized? |
|-----------|--------|-------|------|------------|
| Rotor outer diameter | D_re | 53.3 | mm | No |
| Rotor inner diameter | D_ri | 12.96 | mm | No |
| Tangential rib thickness | W_tan | 0.45 | mm | No |
| Barrier end opening radius | r | 1.15 | mm | No |
| Barrier angle 1 | theta_b1 | 29.1 | deg | Yes |
| Barrier angle 2 | theta_b2 | 42 | deg | Yes |
| Barrier end opening angle 1 | delta_b1 | 1 | deg | No |
| Barrier end opening angle 2 | delta_b2 | 1 | deg | No |
| Ferrite insulation ratio | k_ferrite | 0.42 | — | Yes |
| Cut-off center distance | C_cut | 26.65 | mm | Yes |
| Cut-off angle | theta_cut | 11.15 | deg | Yes |

## Method / Theory

### Torque Equation (Eq. 1)

The total electromagnetic torque for a PMaSynRM is:

$$T_e = \frac{3}{2} p \left[ \lambda_{pm} i_d + (L_d - L_q) i_d i_q \right] \tag{1}$$

| Variable | Description | Unit |
|----------|-------------|------|
| T_e | Total electromagnetic torque | Nm |
| p | Number of pole pairs | — |
| lambda_pm | PM flux linkage | Wb |
| i_d | d-axis current | A |
| i_q | q-axis current | A |
| L_d | d-axis inductance | H |
| L_q | q-axis inductance | H |

**Assumptions:** Steady-state, sinusoidal back-EMF, negligible saturation cross-coupling. The first term is magnetic torque, the second is reluctance torque.

**Key insight from the paper:** M2 achieves +5.07% total torque improvement over M1 by increasing the magnetic torque component (+13.15%) while reluctance torque decreases negligibly (-0.56%). This demonstrates that optimized ferrite geometry can compensate for lower remanence.

### Ferrite Insulation Ratio (Eq. 2)

$$k_{ferrite} = \frac{L_{ferrite}}{L_{total}} \tag{2}$$

| Variable | Description | Unit |
|----------|-------------|------|
| k_ferrite | Ferrite insulation ratio (analogous to insulation ratio in SynRMs) | — |
| L_ferrite | Total ferrite length in q-axis | mm |
| L_total | Total q-axis length (ferrite + iron + air) | mm |

**Assumption:** Ferrite permeability is approximately equal to air permeability, so k_ferrite is treated as an insulation ratio analogous to conventional SynRM design.

**Normalized form:** k_ferrite = 0.42 (optimized value). For comparison, M1 has no insulation ratio parameter because rare earth PMs are rectangular inserts rather than barrier-filling elements.

### Fluid-Shaped Flux Barrier Geometry

The flux barrier edges are drawn using the **N. E. Joukowski air potential function**, a mathematical model describing "natural flux." The method (originally proposed by Rajabi Moghaddam) maximizes reluctance torque by shaping barriers to follow natural flux paths. Each arc center lies on the q-axis (rotor symmetry).

### Cut-Off Region

A cubic-function-modified curve at the q-axis, parameterized by C_cut (distance from center to rotor center) and theta_cut (angle). Purpose: control iron saturation in the cut-off region to minimize torque ripple. The cut-off region is the primary sensitivity parameter for torque ripple.

### Ferrite Anti-Demagnetization Design

Small air regions are added at each flux barrier end to prevent ferrite demagnetization from high saturation in the tangential rib region. Without the air region, ferrite flux density drops below the 0.12 T demagnetization knee. With the air region, minimum flux density across a full electrical cycle is 0.1789 T (safely above knee).

## Important Equations

### Eq. 1 — PMaSynRM Electromagnetic Torque

$$T_e = \frac{3}{2} p \left[ \lambda_{pm} i_d + (L_d - L_q) i_d i_q \right]$$

- **Original notation:** As published
- **Variables:** T_e (torque), p (pole pairs), lambda_pm (PM flux linkage), i_d, i_q (d/q-axis currents), L_d, L_q (d/q-axis inductances)
- **Units:** Nm, Wb, A, H
- **Assumptions:** Steady-state, sinusoidal, no cross-saturation
- **Normalized (MTPA at rated):** T_e ≈ 1.9 Nm with i_d ≈ -1.63 A, i_q ≈ 2.84 A (estimated from MTPA angle 47 deg for M1, 44 deg for M2)
- **Relevance:** Foundation equation for all PMaSynRM design — used throughout [[motorcad/parameters]] torque decomposition

### Eq. 2 — Ferrite Insulation Ratio

$$k_{ferrite} = \frac{L_{ferrite}}{L_{total}}$$

- **Original notation:** As published
- **Variables:** k_ferrite (insulation ratio), L_ferrite (ferrite length q-axis), L_total (total q-axis length)
- **Units:** Dimensionless
- **Assumptions:** Ferrite permeability ≈ air permeability
- **Optimized value:** 0.42
- **Relevance:** Analogous to insulation ratio in SynRM rotor design — maps to barrier width fractions in [[motorcad/parameters]]

## Key Design Insights

1. **Fluid-shaped barriers beat rectangular PMs:** Joukowski-profile barriers filled with ferrite produce more magnetic torque than rectangular rare-earth inserts, because the barrier shape better matches natural flux paths.

2. **Cut-off region is critical for torque ripple:** Torque ripple sensitivity to C_cut and theta_cut is extreme — from optimized 12.34% to over 40% at poor parameter combinations. Average torque is relatively insensitive (0.8% variation), but torque ripple varies by 3x.

3. **Air gaps at barrier ends prevent demagnetization:** Without the air gap, ferrite at barrier ends drops below the demagnetization knee (0.12 T). With it, minimum B stays at 0.1789 T — a simple but essential design feature.

4. **Cost-performance inversion is real:** Ferrite Y-40 ($10.96/kg) replaces N30H ($68.5/kg). Despite needing 3.4x more PM volume (54,607 mm^3 vs 16,044 mm^3), the total PM cost drops from $8.24 to $2.93. Rotor material cost reduction: 59.6%.

5. **Power factor improvement is wide-band:** M2 achieves PF > 0.96 across ~75% of the operating range vs ~50% for M1. At light loads (torque < 1 Nm), M2 reaches PF > 0.99.

6. **Torque ripple harmonics:** The 6th harmonic order in M2 is only 63% of M1's. M2 also shows lower 12th and 18th harmonics, though 24th and 36th are slightly higher.

7. **Both reluctance and magnetic torque matter:** In both M1 and M2, reluctance torque contributes ~56-59% and magnetic torque ~41-44% of total torque. The optimization goal is maximizing both components through geometry.

8. **Experimental vs FEA agreement is excellent:** Efficiency and power factor match within 0.5% and 0.02 respectively across all 6 operating points. Torque ripple FEA-to-experiment difference is < 0.8%.

## Optimization Setup

- **Method:** MOGA-II multi-objective genetic algorithm (ModeFrontier)
- **Objectives:** (1) Minimize torque ripple, (2) Maximize average torque
- **Mode:** MTPA (Maximum Torque Per Ampere) at rated phase current 3.26 Arms
- **Optimized parameters:** theta_b1, theta_b2, k_ferrite, C_cut, theta_cut (5 variables)
- **Fixed parameters:** D_re, D_ri, W_tan, r, delta_b1, delta_b2
- **Pareto front:** ~40+ solutions; final solution selected at theta_b1=29.1, theta_b2=42, k_ferrite=0.42, C_cut=26.65, theta_cut=11.15

## Results (Numerical)

### M1 vs M2 at Rated Condition (FEA)

| Metric | M1 | M2 | Improvement |
|--------|----|----|-------------|
| Average torque | 1.9 Nm | 1.9 Nm | — |
| MTPA phase current | 3.4 Arms | 3.26 Arms | -4.12% |
| Torque ripple | 14.57% | 12.34% | -15.3% |
| Power factor | 0.925 | 0.944 | +2.05% |
| Copper loss | 37.89 W | 35.01 W | -7.6% |
| Iron loss | 30.2 W | 30.6 W | +1.3% |
| Efficiency | 94.04% | 94.27% | +0.23% |
| Rotor material cost | $9.12 | $3.68 | -59.6% |

### Torque Component Breakdown (at 3.26 Arms MTPA)

| Component | M1 (Nm) | M2 (Nm) | Change |
|-----------|---------|---------|--------|
| Total | 1.815 | 1.907 | +5.07% |
| Reluctance | 1.070 | 1.064 | -0.56% |
| Magnetic | 0.745 | 0.843 | +13.15% |

### Structural FEA (M2 at 7200 rpm)

| Metric | Value | Limit | Margin |
|--------|-------|-------|--------|
| Max von Mises stress | 92 MPa | 460 MPa (tensile) | 5.0x |
| Max deformation | 1.6 um | — | — |

### Experimental Validation (6 Operating Points)

| Point | Speed (rpm) | T (Nm) | M1 PF | M2 PF | M1 eta (%) | M2 eta (%) |
|-------|-------------|--------|-------|-------|------------|------------|
| 1 | 1200 | 1.0 | 0.952 | 0.981 | 87.00 | 87.64 |
| 2 | 1800 | 1.2 | 0.931 | 0.991 | 90.15 | 90.62 |
| 3 | 2400 | 1.4 | 0.921 | 0.975 | 91.32 | 91.72 |
| 4 | 3600 | 1.5 | 0.919 | 0.967 | 92.98 | 93.48 |
| 5 | 4200 | 1.8 | 0.911 | 0.952 | 93.19 | 93.48 |
| 6 (rated) | 5400 | 1.9 | 0.915 | 0.939 | 93.48 | 93.85 |

### Experimental Torque Ripple

| Motor | Measured T_ripple | FEA T_ripple | Measured T_avg | FEA T_avg |
|-------|-------------------|--------------|----------------|-----------|
| M1 | 15.25% | 14.57% | 1.855 Nm | 1.9 Nm |
| M2 | 13.10% | 12.34% | 1.856 Nm | 1.9 Nm |

## Limitations / Caveats

1. **Household appliance scale only:** Results are for a ~1 kW motor. Scalability to larger sizes (e.g., [[motor-deepagent]] 45 kW class) is unverified. Fluid-shaped barriers may need re-optimization at different scales.
2. **Ferrite brittleness:** Y-40 has tensile strength of only 35 MPa vs 460 MPa for M235-35A iron. Mechanical integrity at 7200 rpm is confirmed by FEA, but long-term fatigue under thermal cycling is not addressed.
3. **Single operating point optimization:** MOGA-II optimization was performed at a single rated current (3.26 Arms). Wide-speed-range optimization across the full torque-speed map is not reported.
4. **Controller limitation:** STM32-based controller is low-cost but limits achievable bandwidth and current control quality. Higher-performance controllers might change measured results.
5. **No thermal analysis:** Thermal performance of the ferrite-filled barriers (ferrite Curie temperature ~450 deg C vs NdFeB ~310 deg C) is not discussed. Unlikely to be an issue at household appliance loads but relevant for higher-power applications.
6. **Manufacturing complexity:** Fluid-shaped barriers are more complex to stamp than rectangular barrier cuts. Cost comparison only accounts for material, not manufacturing process differences.
7. **Demagnetization knee analysis is partial:** Only the ferrite end region is checked for demagnetization. Full motor demagnetization under fault conditions (e.g., short circuit) is not reported.

## Propagation Into Wiki

Pages to update with findings from this paper:

- [[motorcad/parameters]] — Add fluid-shaped barrier parametrization (Joukowski profile), ferrite insulation ratio k_ferrite, cut-off region parameters (C_cut, theta_cut), and anti-demagnetization air gap design
- [[motorcad/workflow]] — Add MOGA-II multi-objective optimization setup for PMaSynRM (max torque + min ripple), Pareto front selection methodology
- [[known_issues]] — Document torque ripple sensitivity to cut-off region parameters (3x variation), and the importance of barrier end air gaps for ferrite demagnetization prevention
- [[architecture/orchestrator]] — Reference cost-performance tradeoff methodology (ferrite vs rare-earth, volume vs unit price)
- [[codebase_map]] — Reference fluid-shaped barrier geometry as a reusable rotor design technique

## Related Pages

- [[motorcad/parameters]] — Rotor geometry parameters, barrier design, optimization constraints
- [[motorcad/workflow]] — Motor-CAD parametric optimization workflow
- [[motorcad/result_fields]] — Torque decomposition, efficiency maps, power factor maps
- [[known_issues]] — Torque ripple sensitivity, manufacturing constraints
- [[motorcad/experiments]] — Experimental validation methodology (dynamometer testing)
- [[papers/nagarkar_optimized_rotor_synrm]] — Related SynRM rotor optimization methodology
- [[papers/torque_ripple_reduction_srm]] — Torque ripple reduction techniques comparison
