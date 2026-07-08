---
type: equation
title: Inductance Equations
aliases: [inductance, Ld, Lq, d-axis inductance, q-axis inductance]
tags: [equations, inductance, dq-theory, reluctance-network, flux-barriers]
motor_types: [SynRM, PMaSynRM, IPMSM]
topics: [inductance, dq-theory, reluctance-network, flux-barriers]
source_pages: []
related_concepts: [flux-barriers, saliency-ratio, dq-theory]
related_motorcad_variables: [Ld, Lq, Barrier_Layers, L1_Diameter, L2_Diameter, L3_Diameter]
confidence: high
verification_status: verified
---

# Inductance Equations

## Statement

### Definition from Flux Linkage

$$L_d = \frac{\lambda_d}{i_d}, \quad L_q = \frac{\lambda_q}{i_q}$$

### Reluctance Network Form

$$L = \frac{N^2}{\mathcal{R}}$$

### d-Axis Reluctance (Air Gap Path)

$$\mathcal{R}_d = \frac{l_g}{\mu_0 \cdot A_d}$$

### q-Axis Reluctance (With Barriers)

$$\mathcal{R}_q = \frac{l_g}{\mu_0 \cdot A_q} + \sum_{k=1}^{n_b} \frac{l_{b,k}}{\mu_0 \cdot A_{b,k}}$$

---

## Original Notation

| Source | Notation | Meaning |
|--------|----------|---------|
| Orlova et al. | $L_d = \lambda_d / i_d$ | Standard definition |
| Lopez et al. | $\mathcal{R}_q = \mathcal{R}_{g,q} + \sum \mathcal{R}_{b,k}$ | Barrier reluctance sum |
| Classic EM theory | $L = N^2 / \mathcal{R}$ | Reluctance form |

---

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $L_d$ | d-axis inductance | H |
| $L_q$ | q-axis inductance | H |
| $\lambda_d$ | d-axis flux linkage | Wb |
| $\lambda_q$ | q-axis flux linkage | Wb |
| $i_d$ | d-axis current | A |
| $i_q$ | q-axis current | A |
| $N$ | Number of series turns per phase | — |
| $\mathcal{R}$ | Reluctance | 1/H (A/Wb) |
| $\mathcal{R}_d$ | d-axis reluctance | 1/H |
| $\mathcal{R}_q$ | q-axis reluctance | 1/H |
| $l_g$ | Air gap length | m |
| $\mu_0$ | Permeability of free space | $4\pi \times 10^{-7}$ H/m |
| $A_d$ | d-axis effective cross-sectional area | m² |
| $A_q$ | q-axis effective cross-sectional area | m² |
| $n_b$ | Number of flux barriers | — |
| $l_{b,k}$ | Length of k-th barrier in flux path | m |
| $A_{b,k}$ | Cross-sectional area of k-th barrier | m² |

---

## Assumptions

- Linear magnetic circuit (no saturation)
- Uniform flux distribution in each axis
- Barriers are filled with air (or non-magnetic material, $\mu_r \approx 1$)
- Effective air gap includes Carter coefficient for slotting effects
- Negligible end-winding inductance (2D FEA assumption)
- Cross-coupling between d and q axes is neglected

---

## Physical Interpretation

### d-Axis Inductance ($L_d$)

The d-axis flux path crosses the air gap **directly** — flux barriers do not significantly impede d-axis flux because:

- d-axis flux travels **radially** across the air gap
- Barriers are oriented **circumferentially** and do not block the radial d-axis path
- $L_d$ is primarily determined by:
  - Air gap length $l_g$
  - Stator/rotor iron permeability (assumed infinite in ideal case)
  - Effective pole area $A_d$

### q-Axis Inductance ($L_q$)

The q-axis flux path is **blocked by flux barriers**:

- q-axis flux must cross barriers perpendicularly
- Each barrier adds reluctance proportional to $l_b / (\mu_0 A_b)$
- More barriers → higher $\mathcal{R}_q$ → lower $L_q$
- This is the **key mechanism** for achieving saliency in SynRM

### Saliency Relationship

$$\zeta = \frac{L_d}{L_q} = \frac{\mathcal{R}_q}{\mathcal{R}_d}$$

Since $\mathcal{R}_q > \mathcal{R}_d$ (due to barriers), $L_d > L_q$ for SynRM.

---

## Design Relevance

1. **Barriers reduce $L_q$**: Each barrier layer adds q-axis reluctance, reducing $L_q$
2. **Air gap affects $L_d$**: Larger air gap reduces $L_d$ — tradeoff with $L_q$
3. **Barrier width matters**: Wider barriers → higher reluctance → lower $L_q$
4. **Number of barriers**: More barriers provide finer control of reluctance distribution
5. **Saturation effects**: At high flux density, iron reluctance increases, reducing both $L_d$ and $L_q$ but affecting $L_d$ more severely in some designs
6. **Manufacturing tolerance**: Barrier geometry precision directly impacts actual inductance values

---

## MotorCAD Mapping

| Equation Term | MotorCAD Variable | Notes |
|---------------|-------------------|-------|
| Barrier count | `Barrier_Layers` | Set to 3 in current design |
| Barrier diameters | `L1_Diameter`, `L2_Diameter`, `L3_Diameter` | Layer positions |
| Barrier widths | `L1_Web_Thickness`, `L2_Web_Thickness`, `L3_Web_Thickness` | Web = barrier width |
| Bridge thickness | `L1_Bridge_Thickness`, etc. | Mechanical connection |
| Air gap | `Airgap` | Affects $L_d$ directly |
| Computed $L_d$, $L_q$ | From `do_magnetic_calculation()` | Post-processing output |

---

## Sources

- Orlova, S. — Inductance analysis in SynRM
- Lopez, P. — Reluctance network modeling
- Miller, T.J.E. — Electric Machinery (classic textbook)
- Pyrhönen, J. — Electric Machine Design

---

## Related Pages

- [[flux-barriers]] — Barrier geometry and design
- [[saliency-ratio]] — Ld/Lq ratio optimization
- [[torque-equation]] — Torque depends on Ld - Lq
- [[power-factor-equation]] — PF depends on saliency
- [[synrm-topology]] — SynRM motor overview
