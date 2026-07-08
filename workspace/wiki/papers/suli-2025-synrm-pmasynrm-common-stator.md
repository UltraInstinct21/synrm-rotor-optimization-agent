---
type: research_paper
title: "Common Stator Platform for SynRM and PMaSynRM: MOGA Optimization for EV Applications"
authors:
  - Suli et al.
year: 2025
venue: "Energy Reports (Elsevier)"
motor_types:
  - SynRM
  - PMaSynRM
tags:
  - common-stator
  - moga
  - ev
  - multi-objective
  - saliency
  - efficiency
  - flux-barriers
source_file: "raw/papers/suli-2025-synrm-pmasynrm-common-stator.pdf"
---

# Common Stator Platform for SynRM and PMaSynRM: MOGA Optimization for EV Applications

## Citation

Suli et al., "Common Stator Platform for SynRM and PMaSynRM," *Energy Reports*, Elsevier, 2025.

---

## Why This Paper Matters

This paper addresses a practical EV powertrain challenge: designing a **single stator geometry** that can serve as a common platform for both [[synrm-topology|SynRM]] and [[pmasynrm-topology|PMaSynRM]] rotors. This enables manufacturers to use identical stator stamping, winding, and housing across motor variants, reducing tooling cost and supply chain complexity while offering performance differentiation through rotor swaps alone. The Multi-Objective Genetic Algorithm (MOGA) optimization framework provides a systematic way to navigate the conflicting objectives of torque, efficiency, power factor, and saliency.

---

## Problem Statement

In EV powertrain design, cost reduction and manufacturing simplicity are critical. Producing separate stators for SynRM and PMaSynRM variants doubles stator tooling and winding tooling. The paper asks: **can a single stator geometry be optimized to deliver acceptable performance for both rotor types?**

Key conflicts:
- SynRM benefits from high saliency and reluctance torque; PMaSynRM adds magnet torque contribution
- Stator slot geometry, tooth width, and bore diameter affect winding inductance differently for each rotor type
- Efficiency targets (IE5, ≥96% at 45 kW) must be met for both variants

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | SynRM / PMaSynRM (common stator) |
| Stator OD | 340 mm |
| Stator bore | 215 mm |
| Slot number | 48 |
| Pole number | 4 |
| Application | EV traction |
| Power rating | ~45 kW class |
| Cooling | Assumed water jacket (typical for EV) |

### Fixed Stator Parameters

| Parameter | Value |
|---|---|
| Tooth width | 7.5 mm |
| Slot depth | 29 mm |
| Slot corner radius | 4.7 mm |
| Tooth tip depth | 0.6 mm |
| Slot opening | 2.9 mm |
| Tooth tip angle | 15 deg |
| Slot type | Parallel tooth |
| Lamination material | 50C250, 0.50 mm |

### Winding Parameters

| Parameter | Value |
|---|---|
| Wire diameter | 1.715 mm |
| Copper slot fill | 0.40 |
| Liner thickness | 0.25 mm |
| Coil style | Stranded |

---

## Method / Theory

### Torque Production

The electromagnetic torque for both SynRM and PMaSynRM is expressed as:

$$T = \frac{3}{2} p \left[ \psi_m i_q + (L_d - L_q) i_d i_q \right]$$

where:
- $p$ = pole pair number
- $\psi_m$ = flux linkage from permanent magnets (zero for SynRM, nonzero for PMaSynRM)
- $L_d$, $L_q$ = d-axis and q-axis inductances
- $i_d$, $i_q$ = d-axis and q-axis currents

For the SynRM variant ($\psi_m = 0$):

$$T_{SynRM} = \frac{3}{2} p (L_d - L_q) i_d i_q$$

For the PMaSynRM variant:

$$T_{PMaSynRM} = \frac{3}{2} p \left[ \psi_m i_q + (L_d - L_q) i_d i_q \right]$$

**Key insight**: The reluctance torque term $\frac{3}{2} p (L_d - L_q) i_d i_q$ is common to both. A stator geometry that maximizes $(L_d - L_q)$ benefits both variants.

### Saliency Ratio

The saliency ratio is defined as:

$$\xi = \frac{L_d}{L_q}$$

Higher saliency improves:
- Reluctance torque contribution
- Power factor
- Field-weakening capability

For SynRM, typical target: $\xi > 3$. For PMaSynRM, $\xi > 2$ is often sufficient due to magnet torque contribution.

### Power Factor

The power factor is approximated as:

$$PF \approx \cos\left(\arctan\left(\frac{L_d i_d - \psi_m}{L_q i_q}\right)\right)$$

For SynRM ($\psi_m = 0$):

$$PF_{SynRM} \approx \cos\left(\arctan\left(\frac{L_d i_d}{L_q i_q}\right)\right)$$

SynRM inherently has lower PF than PMaSynRM because it lacks magnet flux to boost the airgap flux linkage.

### Sizing Equation

The classic $D^2L$ sizing equation relates geometric parameters to electromagnetic torque:

$$T = \frac{\pi}{4} D_{ro}^2 L_{stk} \cdot \sigma_{mag} \cdot k_w \cdot \cos\alpha$$

where:
- $D_{ro}$ = rotor outer diameter
- $L_{stk}$ = stack length
- $\sigma_{mag}$ = magnetic loading (shear stress)
- $k_w$ = winding factor
- $\alpha$ = current advance angle

---

## Optimization: Multi-Objective Genetic Algorithm (MOGA)

### Objectives

The MOGA simultaneously optimizes for:
1. **Maximize torque** (or minimize torque error from target 143 Nm)
2. **Maximize efficiency** (target ≥96%)
3. **Maximize power factor** (target ≥0.85)
4. **Maximize saliency ratio** (target >3 for SynRM)

### Design Variables

| Variable | Search Range | Description |
|---|---|---|
| Stack length | 100–250 mm | Active axial length |
| Airgap | 0.3–1.0 mm | Mechanical airgap |
| Barrier layer count | 2–5 | Number of flux barriers per pole |
| Barrier angles | Varies per layer | Angular position of barriers |
| Bridge thickness | 0.5–3.0 mm | Mechanical bridges |
| Current density | 3–8 A/mm² | Electrical loading |

### Constraints

- Stator geometry fixed (340 mm OD, 215 mm bore, 48 slots)
- Mechanical integrity: bridge thickness ≥ 0.5 mm
- Thermal limits: winding temperature ≤ 180°C
- Manufacturing: slot fill factor compatible with automated winding

### Results

| Metric | SynRM (optimized) | PMaSynRM (optimized) |
|---|---|---|
| Saliency ratio (Ld/Lq) | 3.2–3.8 | 2.5–3.0 |
| Efficiency @ rated | ≥96.2% | ≥96.5% |
| Power factor | 0.85–0.88 | 0.90–0.93 |
| Torque @ 3000 RPM | ~143 Nm | ~143 Nm |
| Torque ripple | <6% | <5% |

### Key Finding

A **single stator geometry** can serve both SynRM and PMaSynRM rotors while meeting IE5 efficiency and PF ≥ 0.85 for both. The MOGA identifies Pareto-optimal stator designs that balance the competing requirements.

---

## Design Insights

1. **Common stator feasibility**: The stator bore, slot geometry, and winding can be shared without significant performance compromise for either rotor type.
2. **Saliency vs. PF tradeoff**: Increasing barrier count improves saliency but can reduce PF; MOGA finds the Pareto front.
3. **Stack length is dominant**: Stack length has the largest effect on torque density; barrier geometry fine-tunes saliency and PF.
4. **Airgap sensitivity**: Smaller airgap improves torque but increases manufacturing difficulty and cogging; 0.5 mm is a practical optimum.
5. **PMaSynRM advantage**: Ferrite-assisted PMaSynRM can achieve similar torque with lower saliency requirement, easing rotor design.

---

## Limitations / Caveats

- Study assumes specific stator geometry (340 mm OD class); results may not generalize to all frame sizes
- MOGA convergence depends on population size and generation count; global optimality not guaranteed
- Thermal analysis is simplified; detailed thermal FEA may shift optimal operating points
- Manufacturing tolerances not fully modeled; real-world performance may deviate
- Only evaluated at 3000 RPM rated point; full speed-range optimization not presented

---

## Propagation into Wiki

### Concepts to Update
- [[flux-barriers]] — barrier design for common stator platform
- [[saliency-ratio]] — MOGA-optimized saliency targets
- [[dq-theory]] — torque equations for SynRM and PMaSynRM
- [[power-factor]] — PF optimization under common stator constraint

### Equations to Update
- [[torque]] — SynRM and PMaSynRM torque formulations
- [[saliency-ratio-eq]] — saliency definition and targets
- [[power-factor-eq]] — PF approximation for reluctance motors

### Design Guidelines to Update
- [[barrier-design]] — barrier count and angle optimization
- [[stack-length]] — stack length as dominant sizing variable
- [[airgap]] — airgap selection for common stator

### MotorCAD Pages to Update
- [[motorcad-variables]] — stack length, airgap, barrier parameters
- [[motorcad-workflows]] — MOGA optimization workflow

### Optimization Pages to Update
- [[moga]] — MOGA application to motor design
- [[multi-objective-optimization]] — Pareto front interpretation

---

## Related Pages

- [[flux-barriers]]
- [[saliency-ratio]]
- [[torque-ripple]]
- [[dq-theory]]
- [[synrm-topology]]
- [[pmasynrm-topology]]
- [[power-factor]]
- [[moga]]
- [[torque]]
- [[stack-length]]
