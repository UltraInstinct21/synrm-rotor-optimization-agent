---
type: research_paper
title: "Analytical Design of Synchronous Reluctance Motor Rotor with Multi-Barrier Geometry"
authors: ["Orlova et al."]
year: 2014
venue: "IEEE Transactions on Industrial Electronics / Conference proceedings"
motor_types: ["SynRM"]
topics: ["rotor design", "analytical methods", "d-q inductance", "barrier geometry", "flux barriers"]
tags: [synrm, rotor-design, analytical, flux-barriers, inductance, barrier-optimization]
source_file: "raw/papers/orlova_2014.pdf"
related_pages: ["[[flux-barriers]]", "[[inductance-equations]]", "[[rotor-barrier-design]]"]
confidence: moderate
---

# Orlova et al. (2014) — Analytical Rotor Design for SynRM

## Citation

Orlova, S. et al. (2014). "Analytical design of synchronous reluctance motor rotor with multi-barrier geometry." *IEEE Transactions on Industrial Electronics / Conference proceedings*, 2014.

**Motor type:** Synchronous Reluctance Motor (SynRM)
**Stator:** W21 frame
**Rotor:** Interior U-shape, 3+3+3 barrier configuration

---

## Problem Statement

SynRM performance is fundamentally determined by the rotor barrier geometry. The saliency ratio (L_d/L_q) and torque capability depend critically on barrier count, placement, thickness, and shape. This paper develops an **analytical framework** for designing rotor barriers that maximizes torque and saliency without relying solely on FEA iterations.

**Core question:** How can barrier geometry parameters be analytically related to d-axis and q-axis inductances to enable systematic rotor design?

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | SynRM |
| Stator frame | W21 |
| Rotor type | Interior U-shape |
| Barrier layers | 3 (total), arranged as 3+3+3 geometry |
| Application | Industrial drive |
| Airgap | ~0.5 mm (typical for this frame) |

The 3+3+3 designation indicates three groups of barriers, each containing three barrier segments, distributed across the rotor pole to shape flux paths for d-axis flux and block q-axis flux.

---

## Method / Theory

### Analytical Framework

The paper develops closed-form expressions for:

1. **d-axis inductance** (L_d) — maximum inductance path (flux flows through barriers)
2. **q-axis inductance** (L_q) — minimum inductance path (flux flows through iron bridges)
3. **Saliency ratio** (ξ = L_d / L_q) — ratio determining reluctance torque capability

The approach models the rotor as a **series magnetic circuit** where:

- Each barrier contributes reluctance
- Iron bridges (webs) contribute iron reluctance (low)
- Barriers contribute air-gap-equivalent reluctance (high)

### D-Axis Inductance Model

The d-axis flux path traverses the rotor radially, passing through the barriers and iron bridges. The equivalent magnetic circuit is a series combination of reluctances:

```
R_d = R_bridge_1 + R_barrier_1 + R_web_1 + R_barrier_2 + R_web_2 + R_barrier_3 + R_web_3
```

Where:

- **R_barrier_i** = reluctance of the i-th barrier (air gap dominant, high)
- **R_web_i** = reluctance of the i-th iron web between barriers (low, iron path)
- **R_bridge_i** = reluctance of the i-th bridge at the barrier edge (low, mechanical connection)

The d-axis inductance:

$$L_d = \frac{N^2 \cdot k_w^2}{R_d}$$

Where:
- **N** = number of turns per phase
- **k_w** = winding factor
- **R_d** = total d-axis reluctance

### Q-Axis Inductance Model

The q-axis flux path is constrained to flow through the narrow iron bridges between barriers. Since the bridges are thin and carry flux through iron, L_q is substantially lower than L_d:

$$L_q = \frac{N^2 \cdot k_w^2}{R_q}$$

Where R_q is dominated by the reluctance of the iron bridges, which depends on bridge thickness and the iron path length.

### Saliency Ratio

$$\xi = \frac{L_d}{L_q} = \frac{R_q}{R_d}$$

To maximize saliency:
- **Minimize R_d** → make barriers thin, bridges thin, and iron paths short in d-axis
- **Maximize R_q** → make bridges narrow (but mechanically viable) and iron paths long in q-axis

---

## Key Design Equations

### Barrier Reluctance (for each barrier layer i)

$$R_{barrier,i} = \frac{g_{eff,i}}{\mu_0 \cdot A_{barrier,i}}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| g_{eff,i} | Effective barrier thickness (radial dimension) | m |
| μ₀ | Permeability of free space (4π×10⁻⁷) | H/m |
| A_{barrier,i} | Cross-sectional area of barrier perpendicular to flux | m² |

### Iron Bridge Reluctance

$$R_{bridge,i} = \frac{l_{bridge,i}}{\mu_{iron} \cdot t_{bridge,i} \cdot l_{axial}}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| l_bridge,i | Bridge length in flux direction | m |
| μ_iron | Iron permeability (high, nonlinear) | H/m |
| t_bridge,i | Bridge thickness (radial) | m |
| l_axial | Axial stack length | m |

### Torque from Saliency

$$T = \frac{3}{2} \cdot p \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

Where:
- **p** = number of pole pairs
- **i_d, i_q** = d-axis and q-axis currents

---

## Design Parameters — 3+3+3 Barrier Configuration

The rotor uses a symmetric 3+3+3 arrangement:

| Barrier Layer | Role | Key Parameters |
|---|---|---|
| Inner (L1) | Closest to shaft, largest area | Diameter, outer thickness, inner thickness |
| Middle (L2) | Mid-rotor, balanced flux path | Diameter, bridge thickness, web thickness |
| Outer (L3) | Closest to airgap, highest flux density | Diameter, bridge thickness, web thickness |

For each layer:
- **Diameter** — radial position of barrier center
- **Bridge Thickness** — iron bridge at barrier ends (mechanical constraint)
- **Web Thickness** — iron segment between adjacent barriers
- **Outer Thickness** — radial extent of barrier toward airgap
- **Inner Thickness** — radial extent of barrier toward shaft

### Design Tradeoffs

| Parameter | Effect on L_d | Effect on L_q | Effect on Saliency | Effect on Torque |
|---|---|---|---|---|
| ↑ Barrier thickness | ↑ (more air gap, reduced d-axis saturation) | — | ↑ | ↑ (up to saturation limit) |
| ↑ Bridge thickness | ↓ (shorter air path) | ↑ (more iron path) | ↓ | ↓ |
| ↑ Web thickness | ↑ slightly | — | — | — |
| More barrier layers | ↑ (better flux shaping) | ↓ (more bridges to block q-axis) | ↑↑ | ↑↑ |

---

## Key Design Insights

1. **More barriers improve saliency** — each additional barrier adds reluctance to the q-axis path while the d-axis path benefits from better flux shaping.

2. **Bridge thickness is the critical tradeoff** — thin bridges improve saliency but reduce mechanical integrity at high speed. A minimum of ~1 mm is typically required.

3. **Barrier placement is not uniform** — optimal barrier positions follow a distribution that equalizes flux density across the rotor cross-section.

4. **Analytical models agree with FEA within ~5-10%** — sufficient for initial design before FEA refinement.

5. **3+3+3 configuration provides good balance** — sufficient barriers for high saliency without excessive manufacturing complexity.

---

## Limitations

- Analytical model assumes linear iron (no saturation) for initial estimates
- Bridge stress analysis requires separate mechanical FEA
- Thermal effects on barrier geometry not considered
- Assumes sinusoidal MMF distribution
- Manufacturing tolerances not accounted for in analytical framework

---

## Propagation into Wiki

### Concepts to update
- [[flux-barriers]] — add 3+3+3 barrier configuration details
- [[saliency-ratio]] — add analytical framework for saliency optimization

### Equations to update
- [[inductance-equations]] — add d-axis and q-axis inductance models
- [[torque-equation]] — add saliency-based torque equation

### Design guidelines to update
- [[rotor-barrier-design]] — add analytical design procedure for barrier placement

### MotorCAD pages to update
- [[motorcad/variables/barrier-geometry]] — map 3+3+3 parameters to MotorCAD variables

---

## Related Pages

- [[flux-barriers]] — flux barrier theory and design principles
- [[inductance-equations]] — d-axis and q-axis inductance formulations
- [[rotor-barrier-design]] — practical rotor barrier design guidelines
- [[saliency-ratio]] — saliency ratio definition and optimization
- [[synrm-topology]] — Synchronous Reluctance Motor overview
- [[dq-theory]] — d-q reference frame theory for SynRM
