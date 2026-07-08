---
type: research_paper
title: "Performance Analysis and Comparison of PM-Assisted Synchronous Reluctance Motor with Ferrites and Rare-earth Magnet Materials"
authors: "Swapnil N. Jani, Jitendra G. Jamnani"
year: "2021"
venue: "International Conference on Additive Manufacturing and Advanced Materials (IC-AM2)"
doi: ""
motor_types: ["PMASyRM", "SynRM"]
topics: ["PM material selection", "ferrite magnets", "rare-earth magnets", "hybrid PM", "performance analysis", "FEA", "torque ripple", "cost reduction"]
topologies: ["V-shaped buried rotor", "4 flux barrier rotor"]
source_files: ["raw/papers/jg.jamnani_Conf_IC-AM2-Oct2021.md"]
related_projects: []
related_experiments: []
equations_added: ["rotor_diameter_sizing", "leakage_inductance", "slot_permeance", "wedge_permeance", "end_winding_permeance", "stator_end_winding_length", "magnetizing_inductance", "phase_resistance"]
concepts_updated: ["PMASyRM", "ferrite_vs_rare_earth", "hybrid_PM_materials", "saliency_ratio", "flux_barrier_design"]
motorcad_relevance: "High — analytical sizing equations and PM material properties directly applicable to MotorCAD SynRM/PMASyRM design workflows. Hybrid ferrite+rare-earth strategy relevant for [[AGENTS]] cost constraints."
confidence: Verified
---

# Performance Analysis and Comparison of PM-Assisted Synchronous Reluctance Motor with Ferrites and Rare-earth Magnet Materials

## Citation

Jani, S. N. & Jamnani, J. G. (2021). "Performance Analysis and Comparison of PM-Assisted Synchronous Reluctance Motor with Ferrites and Rare-earth Magnet Materials." *International Conference on Additive Manufacturing and Advanced Materials (IC-AM2)*, 2021.

## Why This Paper Matters

This paper directly addresses the core [[AGENTS]] challenge of cost-effective SynRM design for EV applications. It demonstrates that **hybrid PM configurations** (ferrite-dominant + small rare-earth additions) in flux barriers can achieve near-rare-earth performance at significantly lower cost. The analytical sizing equations and [[PM_material_properties]] data tables are directly reusable in [[MotorCAD]] design workflows. The 200 kW / 8-pole machine specification provides a concrete reference point for [[motor_design]] scaling.

## Problem Statement

Rare-earth PM materials (NdFeB, SmCo) used in PMSMs and PMASyRMs are expensive and globally scarce. Pure ferrite magnets have insufficient flux density and demagnetization resistance for standalone use in flux barriers. The paper investigates whether **hybrid PM material combinations** (ferrite + small rare-earth volume) in a PMASyRM rotor can achieve acceptable torque, efficiency, and torque ripple while reducing rare-earth content and cost.

## Machine / Study Context

| Parameter | Value |
|-----------|-------|
| Peak / Continuous output power | 200 kW / 100 kW |
| Base / Maximum speed | 1500 RPM / 6000 RPM |
| Number of poles / slots | 8 / 24 |
| DC bus voltage | 650 V |
| Stator outer diameter | 355 mm |
| Rotor outer diameter | 240 mm |
| Active stack length | 125 mm |
| Air gap thickness | 1 mm |
| RMS line current | 375 A |
| Total number of turns | 3 |
| Parallel paths | 1 |
| Length of winding turn | 524 mm |
| Coil fill factor | 55% |
| Stator phase resistance | 7.99 mΩ |
| End winding resistance | 4.17 mΩ |
| End winding inductance | 13.01 mH |
| Peak RMS current density | 25.1 A/mm² |
| Continuous RMS current density | 10.1 A/mm² |

**Rotor topology:** V-shaped buried structure with 4 flux barriers. Internal rotor. PM materials placed in flux barriers opposing q-axis flux to increase saliency ratio.

**Materials:**
- Stator/Rotor core: M-19 29 Ga steel
- Magnets: N36Z_20 (NdFeB, Br ~1.2 T) for rare-earth cases; Ceramic 8 (Ferrite, Br ~0.4 T) for ferrite cases
- Conductors: Copper

**FEA tool:** ANSYS Maxwell (2D and 3D transient analysis)

## Method / Theory

### PMASyRM Operating Principle

The PMASyRM combines reluctance torque (from flux barriers creating d-q axis saliency) with magnet torque (from PMs in flux barriers). PMs oppose q-axis flux, increasing the saliency ratio (Ld/Lq) and thus improving both torque density and power factor compared to a pure [[Synchronous_Reluctance_Motor|SynRM]].

### Design Approach

1. **Rotor geometry sizing** — determine rotor OD, stack length, air gap from pole pitch relationships
2. **Flux barrier parameterization** — barrier thickness (Tm), iron thickness (Ts), barrier width (Wm, Wb), barrier end angle (αm)
3. **PM material selection** — compare ferrite (Ceramic 8), AlNiCo, SmCo, NdFeB on remanence, coercivity, energy product, temperature stability
4. **Hybrid PM configuration** — majority ferrite + minority rare-earth in flux barriers
5. **FEA validation** — ANSYS Maxwell transient analysis for flux density, field strength, torque, current waveforms

### Key [[PM_material_properties]] Comparison

| Property | Ferrites (Ceramic 8) | AlNiCo (AlNiCo5) | SmCo (REC-26) | NdFeB (NMX-42BH) |
|----------|---------------------|-------------------|---------------|-------------------|
| Br (kG) | 4.0 | 12.5 | 10.5 | 13.1 |
| α(Br) (%/°C) | -0.18 | -0.02 | -0.03 | -0.11 |
| (BH)_max (MGOe) | 3.8 | 5.5 | 26 | 42 |
| H_d (kOe) | 3.3 | 0.64 | 10+ | 14 |
| α(Hc) (%/°C) | 0.4 | -0.015 | -0.3 | -0.6 |
| H_s (kOe) | 10 | 3 | 30 | 25 |
| T_c (°C) | 450 | 890 | 825 | 310 |

## Important Equations

### 1. Rotor Outer Diameter Sizing

$$D = 2 n_p \frac{\tau}{\pi}$$

- **Normalized form:** D = (2·n_p·τ) / π
- **Original notation:** Eq. (1) from paper
- **Variables:**
  - `D` — Rotor outer diameter [m]
  - `n_p` — Number of pole pairs [—]
  - `τ` — Pole pitch [m]
- **Units:** All lengths in meters
- **Assumptions:** Pole pitch τ is a function of d-axis air-gap flux density, pole pairs, saturation factor, and electromagnetic torque. Stack length L = λ·τ where λ is the stack aspect ratio.
- **MotorCAD relevance:** Direct sizing equation for [[MotorCAD]] rotor geometry setup.

### 2. Leakage Inductance

$$\sigma = 2\mu_0 n_s^2 N_{spp} n_p (\lambda_s + \lambda_z + \lambda_f)$$

- **Normalized form:** σ = 2·μ₀·n_s²·N_spp·n_p·(λ_s + λ_z + λ_f)
- **Original notation:** Eq. (2)
- **Variables:**
  - `σ` — Total leakage inductance per phase [H]
  - `μ₀` — Permeability of free space (4π×10⁻⁷ H/m)
  - `n_s` — Number of stator slots [—]
  - `N_spp` — Number of turns per pole per phase [—]
  - `n_p` — Number of pole pairs [—]
  - `λ_s` — Slot permeance factor [—]
  - `λ_z` — Wedge permeance factor [—]
  - `λ_f` — End-winding permeance factor [—]
- **Units:** Henry [H]
- **Assumptions:** Linear magnetic circuit for leakage calculation; valid for distributed windings.
- **MotorCAD relevance:** Maps to [[MotorCAD]] inductance parameter calculations.

### 3. Slot Permeance Factor

$$\lambda_s \cong \frac{2h_{s2}}{3(b_{s1} + b_{s2})} + \frac{2h_{s1}}{b_{s1} + b_{s0}} + \frac{h_{s0}}{b_{s0}}$$

- **Normalized form:** λ_s = (2·h_s2)/(3·(b_s1+b_s2)) + (2·h_s1)/(b_s1+b_s0) + h_s0/b_s0
- **Original notation:** Eq. (3)
- **Variables:**
  - `h_s0`, `h_s1`, `h_s2` — Slot geometry heights at different sections [m]
  - `b_s0`, `b_s1`, `b_s2` — Slot geometry widths at different sections [m]
- **Units:** Dimensionless
- **Assumptions:** Trapezoidal slot approximation; standard double-layer winding slot geometry.
- **MotorCAD relevance:** Slot geometry parameters map directly to [[MotorCAD]] stator slot definition.

### 4. Wedge Permeance Factor

$$\lambda_z = \frac{5g}{5b_{so} + 4g}$$

- **Normalized form:** λ_z = (5·g)/(5·b_so + 4·g)
- **Original notation:** Eq. (4)
- **Variables:**
  - `g` — Air gap length [m]
  - `b_so` — Slot opening width [m]
- **Units:** Dimensionless
- **Assumptions:** Carter's coefficient effect on slot opening permeance.
- **MotorCAD relevance:** Air gap and slot opening are direct [[MotorCAD]] parameters.

### 5. End-Winding Permeance Factor

$$\lambda_f = \frac{0.34q}{L}\left(l_f - 0.64\tau\right)$$

- **Normalized form:** λ_f = (0.34·q/L)·(l_f − 0.64·τ)
- **Original notation:** Eq. (5)
- **Variables:**
  - `q` — Number of slots per pole per phase [—]
  - `L` — Active stack length [m]
  - `l_f` — Stator end winding length [m]
  - `τ` — Pole pitch [m]
- **Units:** Dimensionless
- **Assumptions:** Empirical formula for concentric end winding; valid for fractional-slot windings.

### 6. Stator End Winding Length

$$l_f = \pi \frac{\tau}{2}$$

- **Normalized form:** l_f = π·τ/2
- **Original notation:** Unnumbered equation
- **Variables:**
  - `l_f` — End winding length [m]
  - `τ` — Pole pitch [m]
- **Units:** Meters
- **Assumptions:** Half-pitch end winding overhang approximation.

### 7. Magnetizing Inductance (Uniform Air Gap)

$$L_m = \frac{6\mu_0 \tau L \left(n_p N_{spp} K_{wi} n_s\right)^2}{\pi^2 n_p g K_c (1 + K_s)}$$

- **Normalized form:** L_m = (6·μ₀·τ·L·(n_p·N_spp·K_wi·n_s)²) / (π²·n_p·g·K_c·(1+K_s))
- **Original notation:** Eq. (6)
- **Variables:**
  - `L_m` — Magnetizing inductance [H]
  - `μ₀` — Permeability of free space (4π×10⁻⁷ H/m)
  - `τ` — Pole pitch [m]
  - `L` — Active stack length [m]
  - `n_p` — Number of pole pairs [—]
  - `N_spp` — Turns per pole per phase [—]
  - `K_wi` — Winding factor (ith harmonic) [—]
  - `n_s` — Number of stator slots [—]
  - `g` — Air gap length [m]
  - `K_c` — Carter's coefficient [—]
  - `K_s` — Saturation factor [—]
- **Units:** Henry [H]
- **Assumptions:** Uniform air gap (no rotor saliency considered in this formula); valid for analytical estimation before FEA refinement.
- **MotorCAD relevance:** Fundamental inductance parameter; maps to [[MotorCAD]] Ld/Lq calculation workflow.

### 8. Phase Resistance

$$R_s = \rho \, l_c \, n_p \, N_{spp} \, n_s^2 \, \frac{J}{n_s \, I}$$

- **Normalized form:** R_s = ρ·l_c·n_p·N_spp·n_s²·J/(n_s·I)
- **Original notation:** Eq. (7)
- **Variables:**
  - `R_s` — Stator phase resistance [Ω]
  - `ρ` — Conductor resistivity = 2.3×10⁻⁸ Ω·m (copper)
  - `l_c` — Conductor length per turn = 2(L + l_f) [m]
  - `L` — Active stack length [m]
  - `l_f` — End winding length [m]
  - `n_p` — Number of pole pairs [—]
  - `N_spp` — Turns per pole per phase [—]
  - `n_s` — Number of stator slots [—]
  - `J` — Current density [A/m²]
  - `I` — Phase current [A]
- **Units:** Ohms [Ω]
- **Assumptions:** DC resistance only (no skin/proximity effect); copper conductor; uniform current distribution.
- **MotorCAD relevance:** Maps to [[MotorCAD]] winding resistance calculation.

## Key Design Insights

1. **Hybrid PM strategy is cost-effective:** Ferrite-dominant + small rare-earth addition achieves performance close to full rare-earth configuration at significantly lower material cost. This directly supports the [[AGENTS]] cost constraint for the [[SynRM_45kW_IE5]] design space.

2. **PM placement opposes q-axis flux:** PMs in flux barriers reduce q-axis flux linkage, increasing the saliency ratio (Ld/Lq) and thus reluctance torque contribution. This is the fundamental operating principle of PMASyRM.

3. **Power factor improvement:** PM addition raises power factor, reducing the kVA rating requirement for the inverter — a significant system-level cost saving.

4. **Ferrite limitations:** Pure ferrite (Br ~0.4 T) is insufficient for standalone use in flux barriers due to low flux density and poor demagnetization resistance. A minimum rare-earth fraction is needed.

5. **Cogging torque introduction:** Rare-earth PMs introduce cogging torque and torque ripple that pure SynRMs avoid. Torque ripple reduction techniques were applied but residual ripple remained — identified as an area for further work.

6. **Temperature stability trade-off:** Ferrites have the worst Br temperature coefficient (-0.18%/°C) but highest Curie temperature (450°C). NdFeB has moderate Br coefficient (-0.11%/°C) but lowest Curie temperature (310°C). This affects demagnetization risk assessment in [[thermal_analysis]].

## Optimization Setup

The paper presents a **tradeoff design methodology** (not a formal optimization algorithm) to balance:
- **Objectives:** High torque, high efficiency, low torque ripple
- **Design variables:** PM material type, PM volume in flux barriers, hybrid material ratio
- **Constraints:** Cost reduction (minimize rare-earth content), performance targets
- **Method:** Parametric FEA sweeps in ANSYS Maxwell comparing ferrite-only, rare-earth-only, and hybrid configurations

No formal optimizer (genetic algorithm, gradient-based) was used — the study is a comparative analysis of discrete material configurations.

## Results (numerical)

### Motor Performance Claims (Qualitative/Comparative)

| Metric | Ferrite-only | Hybrid (ferrite + rare-earth) | Rare-earth only |
|--------|-------------|-------------------------------|-----------------|
| Torque density | Baseline (lowest) | Improved | Highest |
| Power factor | Low | Improved | Highest |
| Torque ripple | Lower (no cogging from PM) | Higher (cogging present) | Highest |
| Cost | Lowest | Medium | Highest |
| Demagnetization risk | High (low Hc) | Low (rare-earth Hc protects) | Medium |

### Specific Numerical Values

- Stator phase resistance: **7.99 mΩ**
- End winding resistance: **4.17 mΩ**
- End winding inductance: **13.01 mH**
- Peak RMS current density: **25.1 A/mm²**
- Continuous RMS current density: **10.1 A/mm²**

### FEA Observations

- Flux density plots confirmed proper magnetic circuit operation with expected flux paths
- Torque waveform showed presence of cogging torque due to rare-earth PMs
- Input current waveform confirmed sinusoidal excitation
- Torque ripple reduction techniques were applied but waveform was "not smooth" — residual ripple acknowledged as needing further work

**Note:** No numerical torque values, efficiency percentages, or power factor values were explicitly reported for the comparison cases. The paper presents qualitative comparative conclusions supported by FEA plots rather than tabulated numerical results.

## Limitations / Caveats

1. **No experimental validation:** All results are FEA-based (ANSYS Maxwell). No prototype was built or tested. Claims are unverified by experiment.
2. **No numerical comparison data:** The paper does not provide explicit torque, efficiency, or power factor numbers for the different PM configurations. Comparative conclusions are qualitative.
3. **No cost quantification:** Despite cost being a primary motivation, no material cost analysis or cost-per-kW comparison is provided.
4. **No thermal analysis:** Demagnetization risk is discussed qualitatively but no thermal FEA or demagnetization analysis is presented.
5. **Torque ripple not fully resolved:** The authors acknowledge that torque ripple reduction was incomplete and "still work can be done in this area."
6. **Single operating point:** The study appears to analyze one speed/load condition rather than a full drive cycle.
7. **No demagnetization simulation:** Despite discussing demagnetization as a key concern, no formal demagnetization analysis under fault or high-temperature conditions is performed.

## Propagation Into Wiki

- Update [[PMASyRM_design]] — add hybrid PM strategy, analytical sizing equations, material comparison tables
- Update [[PM_material_properties]] — add Ceramic 8, AlNiCo5, REC-26, NMX-42BH property tables
- Update [[motor_design]] — add rotor OD sizing equation, flux barrier geometry parameters
- Update [[equations]] — add leakage inductance, magnetizing inductance, phase resistance equations
- Update [[AGENTS]] — reference hybrid PM approach for cost reduction strategy
- Update [[thermal_analysis]] — add PM Curie temperature and Br temperature coefficient data
- Update [[cost_analysis]] — add PM material cost hierarchy (ferrite < hybrid < rare-earth)
- Update [[torque_ripple]] — reference cogging torque introduction from rare-earth PMs
- Update [[power_factor]] — reference PF improvement from PM addition
- Update [[FEA_workflow]] — reference ANSYS Maxwell setup for PMASyRM analysis

## Related Pages

- [[PMASyRM_design]]
- [[Synchronous_Reluctance_Motor|SynRM]]
- [[PM_material_properties]]
- [[motor_design]]
- [[equations]]
- [[AGENTS]]
- [[SynRM_45kW_IE5]]
- [[thermal_analysis]]
- [[torque_ripple]]
- [[power_factor]]
- [[cost_analysis]]
- [[FEA_workflow]]
- [[electric_vehicle_motors]]
