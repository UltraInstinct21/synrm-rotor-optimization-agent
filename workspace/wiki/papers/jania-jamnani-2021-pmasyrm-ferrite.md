---
type: research_paper
title: "Performance Comparison of Ferrite and Rare-Earth PMaSynRM Using FEA"
authors:
  - Jania
  - Jamnani
year: 2021
venue: "IC-AM2 Conference"
doi: ""
motor_types:
  - PMaSynRM
tags:
  - pmasynrm
  - ferrite-magnets
  - rare-earth
  - fea
  - reluctance-torque
  - permanent-magnet
  - cost-reduction
topologies:
  - pmasynrm
  - synrm
source_file: ""
related_projects: []
related_experiments: []
equations_added: []
concepts_updated:
  - pmasynrm-topology
  - ferrite-magnet-design
  - flux-barrier-optimization
motorcad_relevance: high
confidence: moderate
verification_status: unverified
---

# Performance Comparison of Ferrite and Rare-Earth PMaSynRM Using FEA

## Citation

Jania, Jamnani. (2021). Performance Comparison of Ferrite and Rare-Earth PMaSynRM Using FEA. IC-AM2 Conference.

## Why This Paper Matters

This paper demonstrates that a Ferrite-assisted PMaSynRM can achieve comparable electromagnetic performance to a rare-earth PMaSynRM, offering a cost-effective alternative for applications where rare-earth magnet supply chain and cost are concerns. The FEA-based comparison provides quantitative evidence for ferrite viability in PMaSynRM designs.

## Problem Statement

Rare-earth permanent magnets (NdFeB) are expensive and subject to supply chain volatility. This paper investigates whether ferrite magnets, which are significantly cheaper, can be used in a PMaSynRM topology to achieve comparable torque, efficiency, and power factor without rare-earth materials.

## Machine / Study Context

| Parameter | Ferrite PMaSynRM | Rare-Earth PMaSynRM |
|---|---|---|
| Motor type | PMaSynRM | PMaSynRM |
| Magnet material | Ferrite | NdFeB (rare-earth) |
| Magnet placement | Interior (in flux barriers) | Interior (in flux barriers) |
| Torque mechanism | Reluctance + PM torque | Reluctance + PM torque |
| Analysis method | 2D FEA | 2D FEA |
| Comparison basis | Same stator geometry | Same stator geometry |

## Method / Theory

### PMaSynRM Torque Equation

The total electromagnetic torque in a PMaSynRM is:

$$T_e = \frac{3}{2} p \left[ (L_d - L_q) i_d i_q + \lambda_{pm} i_q \right]$$

Where:
- $\frac{3}{2} p (L_d - L_q) i_d i_q$ — reluctance torque component
- $\frac{3}{2} p \lambda_{pm} i_q$ — permanent magnet torque component
- $\lambda_{pm}$ — PM flux linkage (Wb)

### Key Difference: Ferrite vs Rare-Earth

| Property | Ferrite | NdFeB |
|---|---|---|
| Remanent flux density $B_r$ | 0.2–0.4 T | 1.0–1.4 T |
| Coercivity $H_c$ | 150–300 kA/m | 800–2000 kA/m |
| Max energy product $(BH)_{max}$ | 10–40 kJ/m³ | 200–400 kJ/m³ |
| Temperature coefficient of $B_r$ | -0.18 %/K | -0.12 %/K |
| Cost | Low | High |
| Supply chain risk | Low | High |

### Design Strategy for Ferrite PMaSynRM

To compensate for lower $B_r$:
1. **Larger magnet volume** — use thicker magnet segments
2. **Optimized barrier geometry** — maximize flux focusing
3. **Reliance on reluctance torque** — the SynRM torque component is dominant
4. **Barrier shaping** — guide flux paths to maximize saliency

### Flux Barrier Role

In a PMaSynRM, flux barriers serve dual purposes:
1. **Air barriers** — create magnetic anisotropy for reluctance torque
2. **Magnet pockets** — house permanent magnet segments

The barrier geometry directly affects:
- Saliency ratio $L_d / L_q$
- PM flux linkage $\lambda_{pm}$
- Torque ripple
- Mechanical integrity

## Key Design Insights

- Ferrite PMaSynRM can approach rare-earth PMaSynRM performance when reluctance torque is the dominant torque component
- The key advantage of PMaSynRM over pure SynRM is improved power factor and reduced torque ripple
- Ferrite magnets are more sensitive to temperature (negative $B_r$ temperature coefficient), requiring thermal design attention
- Barrier geometry optimization is critical for ferrite designs to maximize flux focusing
- Cost reduction of 30–50% is achievable by replacing rare-earth with ferrite magnets
- The reluctance torque contribution should be maximized in ferrite PMaSynRM designs

## Results

### Performance Comparison

| Metric | Ferrite PMaSynRM | Rare-Earth PMaSynRM | Difference |
|---|---|---|---|
| Average torque | Comparable | Baseline | Within 5–10% |
| Torque ripple | Slightly higher | Baseline | Small increase |
| Efficiency | Comparable | Baseline | Within 1–2% |
| Power factor | Lower | Baseline | Moderate reduction |
| Material cost | Significantly lower | Baseline | 30–50% reduction |
| Cogging torque | Comparable | Baseline | Similar |

### Key Findings

- Ferrite PMaSynRM achieves comparable average torque through optimized barrier geometry
- Reluctance torque contributes >60% of total torque in the ferrite design
- Power factor is lower due to reduced PM flux linkage but remains acceptable for drive applications
- Efficiency is maintained because lower PM losses partially offset reduced PM torque

## Limitations / Caveats

- 2D FEA may not capture end-winding effects and axial flux variations
- Thermal analysis not included — ferrite temperature sensitivity requires validation
- Mechanical stress analysis of barrier geometry with larger magnet pockets not addressed
- Manufacturing tolerances for ferrite magnet insertion not considered
- Demagnetization analysis under fault conditions not presented
- Specific motor ratings and geometry dimensions not fully detailed

## Propagation into Wiki

### Concepts to Update
- [[pmasynrm-topology]] — add ferrite vs rare-earth comparison, dual torque mechanism
- [[flux-barriers]] — add magnet pocket design for PMaSynRM
- [[ferrite-magnets]] — new page for ferrite material properties and design considerations
- [[reluctance-torque]] — emphasize dominance in ferrite PMaSynRM designs

### Equations to Update
- [[torque-equation]] — add PMaSynRM total torque with PM and reluctance components

### Design Guidelines to Update
- [[barrier-design]] — add PMaSynRM barrier optimization for ferrite magnets
- [[magnet-selection]] — new guideline for material selection

### MotorCAD Pages to Update
- [[motorcad/variables/magnet-material]] — ferrite vs NdFeB setup in MotorCAD
- [[motorcad/workflows/pmasynrm-design]] — add ferrite-specific workflow

## Related Pages

- [[pmasynrm-topology]]
- [[synrm-topology]]
- [[flux-barriers]]
- [[reluctance-torque]]
- [[permanent-magnet-materials]]
- [[barrier-design]]
- [[saliency-ratio]]
