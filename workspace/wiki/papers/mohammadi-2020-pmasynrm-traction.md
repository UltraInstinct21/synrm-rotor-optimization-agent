---
type: research_paper
title: "Multi-Objective Rotor Optimization of a PMaSynRM for Traction Applications"
authors: ["Mohammadi"]
year: 2020
venue: "McGill University Master's Thesis"
motor_types: ["PMaSynRM"]
topics: ["rotor optimization", "MOGA", "multi-objective optimization", "traction", "barrier geometry", "saliency", "torque ripple"]
tags: [pmasynrm, optimization, moga, traction, rotor-design, saliency, torque-ripple, barrier-geometry]
source_file: "raw/papers/mohammadi_2020_mcasynrm_traction.pdf"
related_pages: ["[[pmasynrm-topology]]", "[[flux-barriers]]", "[[saliency-ratio]]"]
confidence: high
---

# Mohammadi (2020) — PMaSynRM Rotor Optimization for Traction

## Citation

Mohammadi, A. (2020). "Multi-Objective Rotor Optimization of a PMaSynRM for Traction Applications." Master's thesis, McGill University, Montreal, Canada.

**Motor type:** Permanent Magnet assisted Synchronous Reluctance Motor (PMaSynRM)
**Application:** Electric vehicle traction
**Optimization method:** Multi-Objective Genetic Algorithm (MOGA)
**Rotor parameters:** 12 barrier geometry variables

---

## Problem Statement

PMaSynRM combines the benefits of SynRM (robust rotor, wide speed range) with permanent magnets (higher torque density, improved power factor). However, optimizing the rotor geometry involves **competing objectives**:

1. **Maximize average torque** — for vehicle acceleration
2. **Minimize torque ripple** — for NVH (noise, vibration, harshness)
3. **Maximize saliency ratio** — for field weakening and wide speed range
4. **Maintain mechanical integrity** — at maximum speed

This thesis develops a **multi-objective optimization framework** using MOGA to find Pareto-optimal rotor designs that balance these conflicting objectives for an automotive traction PMaSynRM.

**Core question:** How can 12 rotor barrier parameters be simultaneously optimized to achieve high torque, low ripple, and high saliency for an EV traction PMaSynRM?

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | PMaSynRM |
| Application | EV traction (automotive) |
| Rotor type | Interior, multi-barrier with PM insertion |
| Barrier layers | Multi-layer (specific count in thesis) |
| PM material | Ferrite or NdFeB (ferrite preferred for cost) |
| Cooling | Water jacket (assumed for automotive) |
| Target speed range | 0–12,000 RPM (typical EV) |
| Pole count | 4 or 6 (typical for traction) |

---

## Method / Theory

### Multi-Objective Genetic Algorithm (MOGA)

The optimization uses a genetic algorithm with multiple objectives:

$$\min_{\mathbf{x}} \mathbf{f}(\mathbf{x}) = \left[-T_{avg}(\mathbf{x}), \; TR(\mathbf{x}), \; -\xi(\mathbf{x})\right]$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| **x** | Vector of 12 barrier parameters | various |
| T_avg | Average torque (maximize → negate for minimization) | Nm |
| TR | Torque ripple percentage (minimize) | % |
| ξ | Saliency ratio L_d/L_q (maximize → negate for minimization) | — |

### Design Variables (12 Parameters)

| # | Variable | Description | Typical Range |
|---|---|---|---|
| 1 | L1_Diameter | Inner barrier diameter | 80–120 mm |
| 2 | L1_Bridge_Thickness | Inner bridge thickness | 1–5 mm |
| 3 | L1_Web_Thickness | Inner web thickness | 5–25 mm |
| 4 | L1_Outer_Angle_Offset | Inner barrier angular offset | -20–0 deg |
| 5 | L1_Outer_Thickness | Inner barrier outer thickness | 2–8 mm |
| 6 | L1_Inner_Thickness | Inner barrier inner thickness | 2–8 mm |
| 7 | L2_Diameter | Middle barrier diameter | 120–150 mm |
| 8 | L2_Bridge_Thickness | Middle bridge thickness | 1–5 mm |
| 9 | L2_Web_Thickness | Middle web thickness | 20–60 mm |
| 10 | L3_Diameter | Outer barrier diameter | 150–180 mm |
| 11 | L3_Bridge_Thickness | Outer bridge thickness | 1–5 mm |
| 12 | L3_Web_Thickness | Outer web thickness | 50–100 mm |

### Geometry Constraints

These constraints must be satisfied for a valid rotor geometry:

$$L1_{Diameter} < L2_{Diameter} < L3_{Diameter} < Rotor_{OD}$$

$$L1_{Diameter} > Shaft_{Diameter}$$

$$Each \; Bridge_{Thickness} \geq 1 \; mm$$

$$L3_{Diameter} + L3_{Outer\_Thickness} < Rotor_{OD}$$

### Evaluation Pipeline

Each candidate design is evaluated through:

1. **Geometry generation** — 12 parameters → rotor cross-section
2. **电磁分析 (EM analysis)** — FEA or MotorCAD to compute torque, inductances
3. **Objective evaluation** — compute T_avg, TR, ξ
4. **Constraint check** — reject invalid geometries

### Pareto Front

The MOGA produces a **Pareto front** of non-dominated solutions:

```
          Torque Ripple (TR)
               ↑
               |    * Pareto front
               |   * *
               |  *   *
               | *     *
               |*       *
               +----------→ Saliency (ξ)
```

Each point on the Pareto front represents a design where **no objective can be improved without degrading another**.

---

## Key Design Equations

### Torque Ripple Definition

$$TR = \frac{T_{max} - T_{min}}{T_{avg}} \times 100\%$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| T_max | Maximum torque over one electrical cycle | Nm |
| T_min | Minimum torque over one electrical cycle | Nm |
| T_avg | Average torque over one electrical cycle | Nm |

### Average Torque

$$T_{avg} = \frac{1}{2\pi} \int_0^{2\pi} T(\theta_e) \, d\theta_e$$

Or from dq model:

$$T_{avg} = \frac{3}{2} \cdot p \cdot \left[(L_d - L_q) \cdot i_d \cdot i_q + \lambda_{PM} \cdot i_q\right]$$

Where λ_PM is the permanent magnet flux linkage (additional term vs pure SynRM).

### Saliency Ratio (PMaSynRM)

$$\xi = \frac{L_d}{L_q}$$

For PMaSynRM, the magnets are inserted in the flux barriers. The magnets:
- **Do not significantly affect L_d** — magnets are in the barrier space, d-axis flux flows through iron
- **Increase L_q** slightly — magnets have permeability close to air, but add flux linkage
- **Add PM torque component** — additional torque from magnet interaction with stator current

### Power Factor (PMaSynRM)

$$PF = \frac{(L_d - L_q) \cdot i_d \cdot i_q + \lambda_{PM} \cdot i_q}{\sqrt{(L_d \cdot i_d + \lambda_{PM})^2 + (L_q \cdot i_q)^2} \cdot \sqrt{i_d^2 + i_q^2}}$$

The PM flux linkage λ_PM improves power factor compared to pure SynRM.

---

## Optimization Results

### Reported Performance

| Metric | Value |
|---|---|
| Saliency ratio achieved | >5 |
| Torque ripple | Significantly reduced vs baseline |
| Average torque | Maintained or improved vs baseline |
| Pareto front solutions | Multiple non-dominated designs |

### Saliency Ratio > 5

The thesis reports achieving a **saliency ratio greater than 5**, which is:
- Higher than typical SynRM (3–4)
- Comparable to high-performance SynRM designs
- Enables effective field weakening for wide speed range

### Torque Ripple Reduction

Multiple Pareto-optimal designs achieve significant torque ripple reduction through:
- Optimized barrier angular positions
- Balanced barrier thicknesses
- Strategic barrier placement to cancel harmonics

### Pareto Front Characteristics

The Pareto front reveals:
- **High torque / high ripple region** — aggressive designs with narrow barriers
- **Low ripple / moderate torque region** — conservative designs with wider barriers
- **High saliency / moderate torque region** — designs optimized for field weakening

---

## Key Design Insights

1. **12 parameters provide sufficient design freedom** — the barrier diameter, thickness, and web parameters independently control different aspects of performance.

2. **Barrier diameter is the most sensitive parameter** — it determines the radial position of flux barriers and has the largest impact on both L_d and L_q.

3. **Bridge thickness strongly affects saliency** — thinner bridges increase saliency but may compromise mechanical integrity.

4. **Barrier angular offset affects torque ripple** — small angular adjustments to barrier positions can significantly reduce torque harmonics.

5. **PM insertion improves power factor** — magnets in barriers add flux linkage that compensates for the SynRM's inherently low PF.

6. **No single "best" design exists** — the Pareto front provides a family of optimal designs; the final choice depends on application priorities (acceleration vs NVH vs speed range).

7. **MOGA converges in ~50–100 generations** — with population size ~50–100, the algorithm finds well-distributed Pareto fronts.

---

## Limitations

- 2D FEA assumed — 3D effects (end winding, axial flux) not captured
- Thermal model not included in optimization — assumes adequate cooling
- Manufacturing tolerances not considered — nominal geometry only
- PM demagnetization not evaluated in optimization
- Mechanical stress analysis decoupled from electromagnetic optimization
- Specific motor ratings not provided in summary — refer to full thesis

---

## Propagation into Wiki

### Concepts to update
- [[pmasynrm-topology]] — add PMaSynRM rotor optimization context
- [[flux-barriers]] — add PM insertion effects on barrier design
- [[saliency-ratio]] — add MOGA optimization results for saliency

### Optimization pages to update
- [[moga-optimization]] — create if not exists, add MOGA setup for motor design
- [[multi-objective-optimization]] — add PMaSynRM case study
- [[pareto-front]] — add motor design Pareto front interpretation

### Design guidelines to update
- [[rotor-barrier-design]] — add 12-parameter optimization approach
- [[pmasynrm-barrier-design]] — create if not exists, add PMaSynRM-specific barrier guidelines

### MotorCAD pages to update
- [[motorcad/workflows/parameter-sweep]] — add 12-parameter sweep setup
- [[motorcad/variables/barrier-geometry]] — map optimization variables

---

## Related Pages

- [[pmasynrm-topology]] — PMaSynRM overview and advantages
- [[flux-barriers]] — flux barrier theory and design
- [[saliency-ratio]] — saliency ratio definition and optimization
- [[rotor-barrier-design]] — practical barrier design guidelines
- [[moga-optimization]] — Multi-Objective Genetic Algorithm for motor design
- [[torque-ripple]] — torque ripple sources and reduction methods
- [[ev-traction-motors]] — electric vehicle traction motor requirements
