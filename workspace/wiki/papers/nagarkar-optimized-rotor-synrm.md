---
type: research_paper
title: "Optimized Rotor Design of Synchronous Reluctance Motor Using Analytical Methods and FEA Validation"
authors:
  - Nagarkar
  - Srinivas
year: 2023
venue: "IIT Madras"
motor_types:
  - SynRM
tags:
  - rotor-design
  - analytical-methods
  - fea-validation
  - flux-barriers
  - bridge-optimization
  - ev
  - reluctance-torque
source_file: "raw/papers/nagarkar-2023-optimized-rotor-synrm.pdf"
---

# Optimized Rotor Design of Synchronous Reluctance Motor Using Analytical Methods and FEA Validation

## Citation

Nagarkar, Srinivas, "Optimized Rotor Design of Synchronous Reluctance Motor Using Analytical Methods and FEA Validation," IIT Madras, 2023.

---

## Why This Paper Matters

This paper from IIT Madras presents a systematic approach to SynRM rotor barrier design combining **analytical modeling** with **FEA validation**. The analytical framework enables rapid initial design space exploration before committing to expensive FEA iterations. The focus on 3-layer barrier geometry and bridge thickness optimization directly addresses the core challenge in SynRM design: maximizing saliency and torque while maintaining mechanical integrity.

---

## Problem Statement

SynRM rotor barrier design involves competing objectives:
- **Maximize $(L_d - L_q)$** for high reluctance torque
- **Minimize torque ripple** for smooth operation
- **Maintain mechanical integrity** of the rotor laminate at high speed
- **Limit bridge saturation** to avoid leakage flux paths that reduce saliency

Analytical methods can quickly explore the design space but lack accuracy near saturation. FEA provides accuracy but is computationally expensive. The paper bridges this gap with a two-stage methodology.

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | SynRM (Interior U-Shape rotor) |
| Pole number | 4 |
| Barrier layers | 3 |
| Application | EV traction (45 kW class) |
| Rotor diameter | ~214 mm (derived from stator bore 215 mm, airgap 0.5 mm) |
| Shaft diameter | 80 mm |
| Lamination material | 50C250, 0.50 mm |

---

## Method / Theory

### Reluctance Torque

The fundamental torque equation for SynRM:

$$T = \frac{3}{2} p (L_d - L_q) i_d i_q$$

This can be rewritten in terms of current magnitude $I_s$ and current advance angle $\beta$:

$$T = \frac{3}{4} p (L_d - L_q) I_s^2 \sin(2\beta)$$

Maximum torque occurs at $\beta = 45°$, giving:

$$T_{max} = \frac{3}{4} p (L_d - L_q) I_s^2$$

### Inductance Calculations

The d-axis and q-axis inductances depend on rotor geometry:

$$L_d = \frac{3}{2} \frac{\psi_d}{i_d}, \quad L_q = \frac{3}{2} \frac{\psi_q}{i_q}$$

For the analytical model, inductances are computed from flux linkage:

$$\psi_d = N_{ph} \cdot k_{w1} \cdot \frac{\hat{B}_\delta \cdot D_{ro} \cdot L_{stk}}{p} \cdot f_d(\text{geometry})$$

where $f_d(\text{geometry})$ captures the effect of barrier dimensions on d-axis flux path.

### Barrier Geometry Parameters

For a 3-layer barrier, each layer $k$ is characterized by:

| Parameter | Symbol | Description |
|---|---|---|
| Diameter | $D_k$ | Radial extent of barrier $k$ |
| Bridge thickness | $b_{b,k}$ | Mechanical bridge at barrier end |
| Web thickness | $b_{w,k}$ | Web (radial bridge) thickness |
| Outer angle offset | $\theta_{o,k}$ | Angular position of barrier outer edge |
| Outer thickness | $t_{o,k}$ | Angular thickness of barrier outer portion |
| Inner thickness | $t_{i,k}$ | Angular thickness of barrier inner portion |

### Analytical Flux Model

The d-axis flux path passes through the iron bridges between barriers. The effective airgap seen by d-axis flux is increased by the barriers:

$$g_{eff,d} = g + \sum_{k=1}^{N_b} \frac{t_{b,k}}{\mu_r}$$

where $t_{b,k}$ is the radial thickness of barrier $k$ and $\mu_r$ is the relative permeability of the barrier material (≈1 for air/vacuum).

The q-axis flux path passes through the iron ribs between barriers. The effective airgap for q-axis is:

$$g_{eff,q} = g + \text{(minimal barrier effect, flux threads through iron)}$$

### Bridge Thickness Optimization

The bridge at each barrier end is a critical design element:

- **Thinner bridge**: Higher saturation → less leakage flux → higher saliency
- **Thicker bridge**: Better mechanical integrity → lower stress at high speed

The bridge saturates at a flux density determined by the lamination material:

$$B_{sat} \approx 1.5 - 1.8 \text{ T (for 50C250 steel)}$$

The optimal bridge thickness balances:
1. Mechanical stress: $\sigma_{max} \leq \sigma_{yield} / SF$
2. Magnetic performance: bridge fully saturated during operation

### Mechanical Stress Constraint

At maximum speed (6000 RPM), the centrifugal stress in the bridge is:

$$\sigma_{centrifugal} = \rho \omega^2 r \cdot t_{bridge}$$

where:
- $\rho$ = material density (~7650 kg/m³ for electrical steel)
- $\omega$ = angular velocity (rad/s)
- $r$ = radial position of bridge
- $t_{bridge}$ = bridge thickness

The safety factor requirement: $SF = \sigma_{yield} / \sigma_{centrifugal} \geq 2.0$

---

## FEA Validation

### Setup

- Software: 2D FEA (likely MotorCAD or equivalent)
- Mesh: Adaptive, refined near bridges and barrier edges
- Operating point: 3000 RPM, rated current, 45° current advance angle
- Validation metrics: Torque, inductances, flux density distribution

### Results Comparison

| Metric | Analytical | FEA | Error |
|---|---|---|---|
| Torque | ~140 Nm | ~143 Nm | ~2% |
| Ld | Within 5% of FEA | Reference | — |
| Lq | Within 8% of FEA | Reference | — |
| Saliency ratio | Within 10% of FEA | Reference | — |

The analytical model provides reasonable initial estimates, with FEA needed for final refinement.

---

## Key Design Insights

1. **Bridge thickness is the single most sensitive parameter**: Small changes (±0.5 mm) significantly affect saliency and torque.
2. **3-layer barriers are a good compromise**: More layers improve saliency but increase manufacturing complexity and mechanical risk.
3. **Barrier angle optimization**: The angular position of each barrier layer should be staggered to avoid flux crowding.
4. **Analytical models are useful for screening**: They can evaluate hundreds of candidates in seconds, identifying promising regions for FEA.
5. **Saturation near bridges is beneficial**: Full bridge saturation during operation minimizes leakage and maximizes saliency.

---

## Design Parameters (Optimized)

| Parameter | Optimized Value |
|---|---|
| L1 Diameter | ~100 mm |
| L1 Bridge Thickness | ~3.5 mm |
| L1 Web Thickness | ~17 mm |
| L1 Outer Angle Offset | ~-10° |
| L1 Outer Thickness | ~4 mm |
| L1 Inner Thickness | ~5 mm |
| L2 Diameter | ~130 mm |
| L2 Bridge Thickness | ~4 mm |
| L2 Web Thickness | ~50 mm |
| L3 Diameter | ~160 mm |
| L3 Bridge Thickness | ~4.5 mm |
| L3 Web Thickness | ~82 mm |

---

## Limitations / Caveats

- Analytical model assumes uniform saturation; actual saturation is localized near bridges
- 2D FEA does not capture axial effects (skew, end-winding leakage)
- Manufacturing tolerances not modeled; real bridges may differ from nominal
- Thermal effects on saturation not included in analytical model
- Only steady-state performance evaluated; transient behavior (startup, fault) not analyzed

---

## Propagation into Wiki

### Concepts to Update
- [[flux-barriers]] — 3-layer barrier design methodology
- [[rotor-barrier-design]] — analytical + FEA workflow
- [[saliency-ratio]] — bridge thickness effect on saliency

### Equations to Update
- [[torque]] — reluctance torque with current advance angle
- [[inductance-calculations]] — d/q inductance from geometry
- [[bridge-stress]] — centrifugal stress in mechanical bridges

### Design Guidelines to Update
- [[barrier-design]] — barrier count, angle, and thickness optimization
- [[bridge-design]] — bridge thickness tradeoff (magnetic vs. mechanical)
- [[rotor-diameter]] — rotor OD selection for SynRM

### MotorCAD Pages to Update
- [[motorcad-variables]] — L1/L2/L3 diameter, bridge, web, angle parameters
- [[motorcad-workflows]] — analytical screening → FEA refinement workflow

---

## Related Pages

- [[flux-barriers]]
- [[rotor-barrier-design]]
- [[saliency-ratio]]
- [[torque]]
- [[bridge-design]]
- [[dq-theory]]
- [[synrm-topology]]
- [[motorcad-variables]]
