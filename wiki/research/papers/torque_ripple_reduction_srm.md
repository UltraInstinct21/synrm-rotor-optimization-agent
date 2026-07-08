---
type: research_paper
title: "Design and Torque Ripple Reduction Methods for Synchronous Reluctance Machine applied in Electric Power Take-off actuation"
authors: "Branko Ban, Andreas Andersson, Stjepan Stipetic"
year: "2022"
venue: "Conference paper (likely ICEM or similar IEEE conference)"
doi: ""
motor_types: ["SyRM", "Synchronous Reluctance Machine"]
topics: ["torque ripple reduction", "rotor skewing", "metamodel optimization", "ePTO", "commercial vehicle electrification"]
topologies: ["6-pole 54-slot SyRM", "4 flux barrier rotor", "integer slot distributed winding"]
source_files: ["raw/papers/Design and Torque Ripple Reduction Methods for SRM.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: ["skew_angle_formula", "flux_barrier_shift_formula"]
concepts_updated: ["torque_ripple", "rotor_skew", "metamodel_optimization", "asymmetric_poles"]
motorcad_relevance: "Directly applicable — Ansys Motor-CAD used for FEA, optimization via OptiSLang + Motor-CAD workflow. Skew angle calculation and torque ripple constraints are standard Motor-CAD workflow inputs."
confidence: Verified
---

# Design and Torque Ripple Reduction Methods for SyRM Applied in ePTO Actuation

## Citation

Ban, B., Andersson, A., & Stipetic, S. (2022). "Design and Torque Ripple Reduction Methods for Synchronous Reluctance Machine applied in Electric Power Take-off actuation." *Conference paper*.

## Why This Paper Matters

This paper provides a **complete, production-relevant comparison** of five torque ripple reduction methods for SyRMs, using a real ePTO (electric Power Take-Off) design as the baseline. It is directly relevant to [[motor-deepagent]] because:

1. It uses **Ansys Motor-CAD** for FEA and **OptiSLang** for metamodel-based optimization — the exact same toolchain referenced in [[motorcad/workflow]].
2. It quantifies the **torque ripple vs. manufacturing cost trade-off** for each skewing strategy.
3. It introduces a novel **variable-length segment skewing** technique that outperforms equal-length segments while remaining cost-competitive.
4. The constraint framework (stress yield, flux density limits, thermal loading, TPV) maps directly to [[motorcad/parameters]].

## Problem Statement

SyRMs inherently suffer from **higher torque ripple** compared to PM machines. For ePTO applications (hydraulic pump actuation on commercial EVs), torque ripple matters because it causes vibration and noise in the hydraulic system. The goal is to minimize torque ripple without significantly sacrificing average torque, and without adding excessive manufacturing complexity or cost.

## Machine / Study Context

- **Application:** Electric Power Take-Off (ePTO) for commercial multi-purpose vehicles (refuse trucks, hook loaders, vacuum trucks)
- **Machine:** 6-pole, 54-slot SyRM with 4 rotor flux barriers, integer slot distributed winding (2-layer)
- **Key rationale for 6-pole:** Higher theoretical torque density and lower torque ripple than 4-pole; low power factor is acceptable because the ePTO inverter is oversized (same rating as traction inverter)

### Baseline Design Parameters

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Stator diameter | D_s | 214 | mm |
| Shaft diameter | D_sh | 54 | mm |
| Airgap | δ | 0.7 | mm |
| Stator bore | D_b | 128.4 | mm |
| Split ratio | D_b/D_s | 0.6 | - |
| Rotor diameter | D_rotor | 127 | mm |
| Barrier bridge | w_bb | 0.3 | mm |
| Active length | l_s | 180 | mm |
| Phase number | N_ph | 3 | - |
| Turns per coil | N_c | 21 | - |
| Parallel paths | a_p | 6 | - |
| Coil throw | y_c | 9 | - |
| Barrier number | k | 4 | - |
| Slot number | N_s | 54 | - |
| Fill factor | - | 0.43 | - |
| Current density | J | 17 | A/mm² |
| DC voltage | U_DC | 610 | V |
| Mass | m | 44.1 | kg |

### Performance Requirements

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Base speed | n_b | 1700 | rpm |
| Max speed | n_max | 2500 | rpm |
| Max torque | T_max | ≥ 200 | Nm |
| Battery voltage | U_DC | 610 | V |
| Max phase current | I_s max | 300 | Arms |

## Method / Theory

### Optimization Workflow

The baseline design was obtained via **metamodel-based (surrogate) optimization** using:
- **FEA:** Ansys Motor-CAD
- **Optimization:** Ansys OptiSLang (genetic algorithm + meta-modeling)
- **Scripting:** MATLAB for model building and FEA communication

Typical optimization time: 2–3 days (reduced vs. direct FEA optimization via surrogate modeling).

### Constraint Framework

| Constraint | Description | Limit |
|------------|-------------|-------|
| g₁ | Stress yield factor at 1.2·n_max | FOS ≥ 2 |
| g₂ | Total loss | P_loss ≤ 6000 W |
| g₃ | Flux density in stator yoke | B_sy,max ≤ 1.6 T |
| g₄ | Flux density in stator tooth | B_st,max ≤ 1.9 T |
| g₅ | Thermal loading (J·A) | THL ≤ 1.9 MA²/m³ |
| g₆ | Torque per volume | TPV ≥ 25 Nm/dm³ |
| g₇ | Torque ripple (unskewed) | T_ripp ≤ 15% |

### Torque Ripple Reduction Methods Compared

Five post-optimization rotor modifications were evaluated:

1. **No skew** (baseline)
2. **Asymmetric rotor poles** via flux barrier shift (FBS)
3. **Equal-length 3-segment skew**
4. **Variable-length 3-segment skew** (novel contribution)
5. **Continuous rotor skew**

Stator skewing was excluded due to higher production complexity (winding insertion difficulty).

### Variable-Length Segment Skew (Novel Contribution)

In standard equal-length segment skewing, each segment has the same axial length. The torque waveform amplitude of each segment is proportional to its length. By varying individual segment lengths (with the constraint that l_seg1 + ... + l_segN = l_s), the total ripple can be minimized. The optimal segment lengths are found via a torque ripple minimization function based on proportional variation of individual segment torque waveforms obtained from equal-segment skewing.

This approach is applicable to **any machine that allows stepped skew** — not limited to SyRMs.

## Important Equations

### Skew Angle Formula

$$\vartheta_{\text{skew}} = \frac{360°}{p \cdot h}$$

- **Normalized form:** θ_skew = 360° / (p · h)
- **Original notation:** ϑ_skew (mechanical degrees)
- **Variables:**
  - p = number of pole pairs (dimensionless)
  - h = highest amplitude torque harmonic of the unskewed rotor (dimensionless, h > 0)
- **Units:** θ_skew in mechanical degrees
- **Assumptions:** One-slot-pitch step skew; applied to variants 2–4 (equal-length segments, variable-length segments, continuous skew). In this paper: p = 3, h = 18 → θ_skew = 360°/(3·18) = 6.67° mechanical.

### Flux Barrier Shift Angle (Asymmetric Poles)

$$\vartheta_{\text{FBS}} = \frac{360°}{2 \cdot p \cdot h}$$

- **Normalized form:** θ_FBS = 360° / (2·p·h)
- **Original notation:** ϑ_FBS (mechanical degrees)
- **Variables:**
  - p = number of pole pairs (dimensionless)
  - h = highest amplitude torque harmonic of the unskewed rotor (dimensionless, h > 0)
- **Units:** θ_FBS in mechanical degrees
- **Assumptions:** Based on the Ferrari et al. flux barrier shift approach. In this paper: θ_FBS = 360°/(2·3·18) = 3.33° mechanical. The shift is exactly half the skew angle.

### Thermal Loading Coefficient

$$\text{THL} = J \cdot A$$

- **Normalized form:** THL = J × A
- **Variables:**
  - J = current density (A/mm²)
  - A = electrical loading (A/m)
- **Units:** MA²/m³
- **Assumptions:** Water cooling possible if THL ≤ 1.9 MA²/m³ (empirical limit from machine manufacturers).

## Key Design Insights

1. **Skew vs. no-skew trade-off:** Skewing reduces torque ripple by ~70–80% but sacrifices 2–5% average torque. All skewed alternatives yield mechanical power in the 41–43 kW range.

2. **Variable-length segment skewing is the sweet spot:** It achieves 4.21% ripple (vs. 6.24% for equal-length segments) with comparable manufacturing cost, bridging the gap between segmented and continuous skew.

3. **Asymmetric poles are the cheapest option:** No stamping tool variation needed, straight keyway shaft. However, ripple reduction is direction-dependent — only unidirectional ePTO applications benefit fully.

4. **Continuous skewing remains the gold standard:** 2.79% ripple, but most complex manufacturing (skewed shaft keyway or angular laminate stamping offset).

5. **6-pole chosen over 4-pole for ePTO:** Higher torque density and inherently lower torque ripple; low power factor is irrelevant with oversized inverter.

6. **Optimization excluded skewing to save time:** Transient simulation scales linearly with segment count (5 segments = 5× simulation time). The unskewed constraint (g₇ ≤ 15%) ensured acceptable baseline quality.

## Optimization Setup

- **Algorithm:** Genetic algorithm (OptiSLang default) with metamodel-based surrogate
- **Objectives:** Minimize total loss (f₁̄), maximize torque per rotor volume (f₂)
- **Constraints:** 7 inequality constraints (see table above)
- **Pareto front:** 89 validated members satisfying all constraints
- **FEA tool:** Ansys Motor-CAD (magnetostatic for MTPA angle, transient for torque ripple)
- **Scripting:** MATLAB for automated model building and FEA communication
- **Rotor parametrization:** Follows [19] (Ban & Stipetic, 2022) — minimal parametric complexity for barrier topologies

## Results (numerical)

### Torque Ripple Comparison (base speed, 1700 rpm, I_rms = 95.7 Arms)

| Method | T_avg (Nm) | T_ripp (%) | cos φ | P_mech (kW) | γ (°) |
|--------|------------|------------|-------|-------------|-------|
| No skew (baseline) | 242.3 | 13.99 | 0.68 | 43.1 | 63.0 |
| Asymmetric poles (n>0) | 240.6 | 7.64 | 0.68 | 42.8 | 68.1 |
| Asymmetric poles (n<0) | 239.5 | 7.22 | 0.68 | 42.6 | 57.6 |
| Equal-length 3-seg skew | 231.1 | 6.24 | 0.65 | 41.1 | 59.7 |
| Variable-length 3-seg skew | 233.5 | 4.21 | 0.66 | 41.6 | 62.6 |
| Continuous skew | 235.7 | 2.79 | 0.66 | 42.0 | 61.0 |

- **Skew angle:** 6.67° mechanical (for segmented and continuous variants)
- **FBS angle:** 3.33° mechanical (for asymmetric poles)
- **Torque harmonic:** h = 18 is the dominant ripple harmonic (see Fig. 9 spectrum)
- **All variants:** Same active mass (44.1 kg), same active length (180 mm)

### Key Numerical Takeaways

- Variable-length segments reduce ripple by **37%** relative to equal-length segments (4.21% vs. 6.24%) with **1% more average torque** (233.5 vs. 231.1 Nm).
- Continuous skewing achieves **34% less ripple** than variable-length segments (2.79% vs. 4.21%) with **1% more average torque**.
- Asymmetric poles reduce ripple by ~45% with essentially zero manufacturing penalty, but only in one rotation direction.

## Limitations / Caveats

1. **Skewing economics are case-dependent:** The manufacturing cost comparisons are based on professional experience, not formal cost analysis. Production process details and commercial decisions vary by manufacturer.
2. **Variable-length skew optimization details not provided:** The paper states optimal segment lengths are found via a "torque ripple minimization function" but defers the methodology to a planned extended version.
3. **Unidirectional application assumed for asymmetric poles:** The asymmetric pole method produces different ripple depending on rotation direction; this is only viable for unidirectional loads (like hydraulic pumps).
4. **No thermal or efficiency map analysis:** Results are at a single operating point (base speed, rated current). Full efficiency maps and thermal behavior under duty cycles are not discussed.
5. **No vibration/acoustic analysis:** Torque ripple reduction is quantified electrically but not correlated to NVH (noise, vibration, harshness) performance.
6. **Single machine size studied:** Results may not generalize to significantly different machine sizes or pole/slot combinations.
7. **Stator skewing excluded entirely:** Only rotor-side methods compared; stator skewing was dismissed on cost grounds without quantitative comparison.

## Propagation Into Wiki

- [[motorcad/workflow]] — Update with OptiSLang + Motor-CAD optimization workflow reference
- [[motorcad/parameters]] — Add skew angle and FBS angle formulas as standard constraint inputs
- [[motorcad/result_fields]] — Add torque ripple (T_ripp) as a key output metric with 15% constraint threshold
- [[motorcad/experiments]] — Reference this paper's methodology for skew comparison experiments
- [[codebase_map]] — No update needed (analysis methodology reference, not code)
- [[known_issues]] — Potentially update torque ripple mitigation strategies

## Related Pages ([[wikilinks]])

- [[motorcad/workflow]]
- [[motorcad/parameters]]
- [[motorcad/result_fields]]
- [[motorcad/experiments]]
- [[architecture/orchestrator]]
- [[project_overview]]
