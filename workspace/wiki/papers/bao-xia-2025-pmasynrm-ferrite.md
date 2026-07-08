---
type: research_paper
title: "Ferrite-Assisted PMaSynRM with Fluid-Shaped Barriers for Cost-Effective High-Efficiency Design"
authors:
  - Bao
  - Xia
year: 2025
venue: "2025"
motor_types:
  - PMaSynRM
tags:
  - ferrite
  - rare-earth-free
  - fluid-shaped-barriers
  - cost-reduction
  - pmasynrm
  - hybrid-pm
source_file: "raw/papers/bao-xia-2025-pmasynrm-ferrite.pdf"
---

# Ferrite-Assisted PMaSynRM with Fluid-Shaped Barriers for Cost-Effective High-Efficiency Design

## Citation

Bao, Xia, "Ferrite-Assisted PMaSynRM with Fluid-Shaped Barriers for Cost-Effective High-Efficiency Design," 2025.

---

## Why This Paper Matters

This paper addresses the **cost-critical challenge** of eliminating rare-earth magnets from high-efficiency motors. By using **ferrite magnets** (which cost ~5–10% of NdFeB per kg) in a PMaSynRM topology with **fluid-shaped barriers**, the design achieves high efficiency without rare-earth dependency. The "fluid-shaped" barrier concept is a novel geometry that optimizes flux paths for both reluctance and magnet torque. This is directly relevant for cost-sensitive EV and industrial applications.

---

## Problem Statement

High-efficiency motors (>96%) typically require rare-earth magnets (NdFeB or SmCo), which:
- Are subject to volatile pricing and supply chain risks
- Are geographically concentrated (China produces ~60% of rare earths)
- Increase motor cost by 20–40% compared to rare-earth-free designs

Ferrite magnets offer a rare-earth-free alternative but have:
- Lower remanence: $B_r \approx 0.2–0.4$ T (vs. 1.0–1.4 T for NdFeB)
- Lower energy product: $(BH)_{max} \approx 10–40$ kJ/m³ (vs. 200–400 kJ/m³ for NdFeB)
- Negative temperature coefficient of $B_r$: $\alpha_{B_r} \approx -0.2$ %/°C

The paper asks: **can a ferrite-assisted PMaSynRM achieve IE5 efficiency using optimized barrier geometry?**

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | PMaSynRM (Hybrid PM-Assisted Reluctance) |
| Magnet type | Ferrite (rare-earth-free) |
| Application | EV traction / industrial drive |
| Power rating | ~45 kW class |
| Pole number | 4 |
| Key innovation | Fluid-shaped flux barriers |

---

## Key Concept: HP-PMaSynRM (Hybrid PM-Assisted Reluctance)

The HP-PMaSynRM combines:
1. **Reluctance torque** from optimized flux barriers (SynRM contribution)
2. **Magnet torque** from ferrite magnets inserted in the barriers (PM contribution)

$$T_{total} = \underbrace{\frac{3}{2} p (L_d - L_q) i_d i_q}_{\text{Reluctance torque}} + \underbrace{\frac{3}{2} p \psi_m i_q}_{\text{Magnet torque}}$$

The hybrid approach means:
- Reluctance torque can contribute 50–70% of total torque
- Ferrite magnets only need to provide 30–50% of torque
- This reduces the required magnet volume and flux density requirement

### Why Ferrite Works in PMaSynRM

In IPMSM, magnets must provide most of the airgap flux (high $B_r$ needed). In PMaSynRM:
- Reluctance torque provides a significant share
- The magnet flux supplements rather than dominates
- Lower $B_r$ is acceptable because the reluctance contribution compensates

---

## Fluid-Shaped Barriers

### Concept

Traditional flux barriers have straight or simple arc shapes. **Fluid-shaped barriers** use curves designed to follow the natural flux flow lines in the rotor, similar to fluid dynamics streamlines.

The barrier shape is defined by:
$$r(\theta) = f(\theta; \text{design parameters})$$

where $f$ is a parametric curve (e.g., Bézier, spline, or analytical function) optimized to:
1. Minimize flux path length in iron (reduce saturation)
2. Maximize flux barrier effectiveness (maximize $L_d / L_q$ ratio)
3. Provide space for ferrite magnet insertion
4. Maintain mechanical integrity

### Advantages over Conventional Barriers

| Feature | Conventional | Fluid-Shaped |
|---|---|---|
| Flux path | Angular, with sharp turns | Smooth, follows natural flow |
| Saturation | Concentrated at corners | Distributed along path |
| Saliency | Moderate | Higher (better flux guiding) |
| Magnet space | Limited by barrier shape | Optimized for magnet placement |
| Manufacturing | Simple stamping | More complex but feasible |

### Design Parameters

For each fluid-shaped barrier layer:

| Parameter | Description |
|---|---|
| Radial extent | How far from shaft to rotor OD |
| Angular span | Width of barrier in electrical degrees |
| Curvature | Shape of the barrier edges (Bézier control points) |
| Magnet slot width | Width of the magnet pocket within the barrier |
| Bridge locations and thickness | Mechanical connections at barrier ends |

### Magnet Placement

Ferrite magnets are placed within the fluid-shaped barriers:
- **V-shape** or **flat** magnet arrangement within each barrier layer
- Magnet flux is guided by the barrier shape to maximize $q$-axis flux opposition

---

## Electromagnetic Analysis

### d-Axis Flux Path

With magnets in the barriers, the d-axis inductance:

$$L_d = \frac{N_{ph}^2 k_{w1}^2}{\mathcal{R}_d}$$

where $\mathcal{R}_d$ is the d-axis reluctance. The magnets increase $\mathcal{R}_d$ (ferrite has $\mu_r \approx 1.05–1.2$, close to air), but the fluid shape minimizes the increase.

### q-Axis Flux Path

The q-axis flux bypasses the barriers through the iron ribs:

$$L_q = \frac{N_{ph}^2 k_{w1}^2}{\mathcal{R}_q}$$

The fluid-shaped barriers are designed to keep $\mathcal{R}_q$ low (short iron path for q-axis flux).

### Saliency Ratio

$$\xi = \frac{L_d}{L_q}$$

Target: $\xi > 2.5$ for PMaSynRM with ferrite (lower than SynRM target of >3 because magnet torque compensates).

### Power Factor

$$PF \approx \cos\left(\arctan\left(\frac{L_d i_d - \psi_m}{L_q i_q}\right)\right)$$

The ferrite magnets improve PF by adding $\psi_m$ to the airgap flux linkage, partially compensating for the reluctance motor's inherently low PF.

---

## Results

| Metric | SynRM (baseline) | PMaSynRM (ferrite) | Improvement |
|---|---|---|---|
| Efficiency @ rated | 95.8% | 96.3% | +0.5% |
| Power factor | 0.82 | 0.89 | +0.07 |
| Saliency ratio | 3.1 | 2.7 | -0.4 (tradeoff) |
| Torque density | Baseline | +15% | Magnet contribution |
| Torque ripple | 7% | 5% | Improved |
| Magnet cost | $0 | Low (ferrite) | Rare-earth-free |

### Key Finding

The ferrite-assisted PMaSynRM with fluid-shaped barriers achieves **IE5 efficiency (≥96%)** while being **entirely rare-earth-free**. The fluid-shaped barrier design contributes ~0.5% efficiency improvement over conventional barriers by reducing localized saturation.

---

## Design Insights

1. **Fluid-shaped barriers improve flux distribution**: Smooth curvature eliminates flux crowding at barrier corners, reducing localized saturation and iron loss.
2. **Ferrite is sufficient for PMaSynRM**: Unlike IPMSM, PMaSynRM does not require high $B_r$ magnets; ferrite's lower $B_r$ is adequate because reluctance torque dominates.
3. **Cost advantage is significant**: Ferrite magnets cost 5–10% of NdFeB, making this topology attractive for cost-sensitive applications.
4. **Thermal considerations**: Ferrite's negative $\alpha_{B_r}$ means magnet flux decreases with temperature, but the reluctance torque component is unaffected, providing inherent thermal stability.
5. **Manufacturing**: Fluid-shaped barriers require more complex lamination stamping but are feasible with modern progressive die technology.

---

## Limitations / Caveats

- Ferrite magnets are brittle and sensitive to mechanical shock; rotor assembly requires care
- Lower energy product means larger magnet volume for equivalent magnet torque
- Negative temperature coefficient of $B_r$ reduces magnet contribution at high temperature (partially offset by reluctance torque stability)
- Fluid-shaped barrier optimization requires computational effort (genetic algorithm or similar)
- Study assumes specific stator geometry; generalizability to other frame sizes not demonstrated
- Demagnetization risk under fault conditions (especially at high temperature) not fully analyzed

---

## Propagation into Wiki

### Concepts to Update
- [[pmasynrm-topology]] — ferrite-assisted variant, HP-PMaSynRM concept
- [[flux-barriers]] — fluid-shaped barrier design
- [[power-factor]] — PF improvement via magnet assistance

### Equations to Update
- [[torque]] — hybrid reluctance + magnet torque
- [[saliency-ratio-eq]] — saliency targets for PMaSynRM
- [[power-factor-eq]] — PF with magnet flux linkage

### Materials to Update
- [[ferrite]] — properties, cost, temperature behavior
- [[ndfeb]] — comparison with ferrite

### Design Guidelines to Update
- [[barrier-design]] — fluid-shaped barrier methodology
- [[magnet-selection]] — ferrite vs. NdFeB tradeoffs for PMaSynRM
- [[cost-optimization]] — rare-earth-free design strategies

### MotorCAD Pages to Update
- [[motorcad-variables]] — fluid-shaped barrier parameters
- [[motorcad-workflows]] — ferrite magnet assignment

---

## Related Pages

- [[pmasynrm-topology]]
- [[flux-barriers]]
- [[power-factor]]
- [[saliency-ratio]]
- [[ferrite]]
- [[ndfeb]]
- [[synrm-topology]]
- [[dq-theory]]
- [[torque]]
- [[cost-optimization]]
