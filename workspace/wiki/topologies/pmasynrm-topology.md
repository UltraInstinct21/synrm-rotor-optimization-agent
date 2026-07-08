---
type: topology
title: PM-Assisted Synchronous Reluctance Motor (PMaSynRM)
aliases: [PMaSynRM, PM-assisted SynRM, Ferrite-assisted SynRM]
tags: [topology, pmasynrm, synrm, reluctance, pm, ferrite]
motor_type: pmasynrm
topics: [operating-principle, rotor-design, torque-production, power-factor, pm-design]
related_pages: [synrm-topology, flux-barriers, power-factor, saliency-ratio, torque-equation, ipmsm-topology]
confidence: verified
---

# PM-Assisted Synchronous Reluctance Motor (PMaSynRM)

## Operating Principle

The PMaSynRM combines **reluctance torque** from magnetic anisotropy with **PM torque** from embedded permanent magnets. It is essentially a [[synrm-topology]] with magnets added inside the flux barriers to:

1. **Boost air-gap flux density** → higher torque density
2. **Improve power factor** → reduce magnetizing current demand
3. **Enable flux weakening** → extend constant-power speed range

The total torque equation becomes:

$$T = \frac{3}{2} p \left[ \lambda_{PM} i_q + (L_d - L_q) i_d i_q \right]$$

Both the PM torque term ($\lambda_{PM} i_q$) and reluctance torque term ($(L_d - L_q) i_d i_q$) contribute positively when the rotor is designed correctly.

### Torque Sharing

The relative contribution of PM torque vs. reluctance torque depends on:
- Magnet volume and grade (ferrite vs. NdFeB)
- Barrier geometry (saliency ratio)
- Operating current angle

Typical torque sharing in a well-designed PMaSynRM:
- **Reluctance torque**: 40–70%
- **PM torque**: 30–60%

This is fundamentally different from [[ipmsm-topology]], where PM torque typically dominates (70–90%).

## Rotor Construction

The PMaSynRM rotor retains the flux barrier structure of a SynRM with **magnets inserted into selected barriers**.

### Magnet Placement

| Strategy | Description | Trade-off |
|---|---|---|
| All barriers magnetized | Magnets in every barrier layer | Maximum PM torque, highest cost |
| Outer barriers only | Magnets in outer 1–2 layers | Moderate PM torque, lower cost |
| Inner barriers only | Magnets in inner layers | Lower saliency impact |
| Selective placement | Magnets in specific layers | Optimized trade-off |

### Magnet Materials

| Material | Remanence | Cost | Demag Risk | Typical Use |
|---|---|---|---|---|
| Ferrite | 0.2–0.4 T | Very low | Low | Cost-sensitive PMaSynRM |
| NdFeB (standard) | 1.0–1.4 T | High | Moderate | High-performance PMaSynRM |
| NdFeB (high temp) | 0.9–1.2 T | Very high | Low | High-temperature applications |

**Ferrite magnets** are the most common choice for PMaSynRM because:
- Low cost eliminates rare-earth dependency
- Lower remanence is sufficient (reluctance torque provides the bulk)
- Good thermal stability
- No demagnetization risk at normal operating temperatures

### Barrier-Magnet Interaction

Adding magnets to flux barriers changes the magnetic circuit:
- Magnets **reduce effective barrier reluctance** in the magnetization direction
- This can **reduce saliency ratio** if not carefully designed
- Barrier geometry must be re-optimized after magnet insertion
- The magnet height (thickness) directly affects the d-axis flux path

## Key Performance Characteristics

### Power Factor Improvement

The primary motivation for adding magnets is **power factor improvement**:

- Ferrite PMaSynRM: PF typically 0.80–0.90
- NdFeB PMaSynRM: PF typically 0.85–0.95
- Pure SynRM: PF typically 0.50–0.70

The magnets provide excitation flux that reduces the reactive current demanded from the inverter.

### Torque Density

PMaSynRM achieves **higher torque density** than pure SynRM:
- 20–50% torque increase over equivalent SynRM (magnet-dependent)
- Still lower than [[ipmsm-topology]] with equivalent magnet volume
- Ferrite PMaSynRM can approach induction motor torque density

### Efficiency

- Very high efficiency possible (IE5+)
- No rotor copper losses (like SynRM)
- Reduced stator copper losses due to higher PF
- Magnet eddy current losses are small (ferrite)

### Field Weakening

- Excellent field weakening capability
- PM flux can be partially counteracted by d-axis current
- Reluctance torque continues to contribute in field-weakened region
- Wide constant-power speed range (CPSR) achievable

## Advantages

| Advantage | Explanation |
|---|---|
| Higher power factor | PM flux reduces magnetizing current demand |
| Higher torque density | Combined PM + reluctance torque |
| No rare-earth option | Ferrite magnets eliminate rare-earth dependency |
| High efficiency | No rotor copper losses, reduced stator losses |
| Good field weakening | Wide CPSR from reluctance torque contribution |
| Robust rotor | Magnets protected inside flux barriers |
| Lower inverter cost | Improved PF reduces required inverter kVA |

## Disadvantages

| Disadvantage | Explanation |
|---|---|
| More complex rotor | Barrier geometry + magnet insertion |
| Magnet cost | Even ferrite adds material cost |
| Manufacturing complexity | Magnet bonding or insertion into barriers |
| Demagnetization risk | NdFeB at high temperatures or fault currents |
| Reduced saliency | Magnets can reduce Ld-Lq difference |
| Assembly challenges | Magnets must be precisely placed |
| Temperature sensitivity | Ferrite performance degrades at high temperature |

## Applications

### Primary Applications

- **Electric vehicle traction** — excellent balance of cost, efficiency, and power density
- **Industrial variable-speed drives** — IE5 efficiency with cost-effective magnets
- **HVAC compressors** — high efficiency at partial loads
- **Pump drives** — where efficiency and PF matter

### Application sweet spots

- **Ferrite PMaSynRM**: Cost-sensitive applications where rare-earth-free is valued
- **NdFeB PMaSynRM**: Performance applications needing higher torque density

### Compared to Alternatives

| Application | Best topology | Reason |
|---|---|---|
| EV traction (cost) | PMaSynRM (ferrite) | Good performance, no rare earth |
| EV traction (performance) | [[ipmsm-topology]] | Higher torque density |
| Industrial drive | [[synrm-topology]] | Lowest cost if PF acceptable |
| High-speed drive | PMaSynRM | Good CPSR, no magnet retention issues |

## Design Considerations

### Magnet Volume Optimization

- Too little magnet: Insufficient PF and torque improvement
- Too much magnet: Diminishing returns, reduced saliency, higher cost
- Optimal volume depends on target PF, torque density, and cost constraints

### Barrier Re-optimization

When adding magnets to an existing SynRM design:
1. Keep barrier angles similar
2. Adjust barrier widths to accommodate magnet height
3. Re-optimize bridge/rib thickness
4. Verify saliency ratio remains > 3
5. Check demagnetization margin under fault conditions

### Thermal Design

- Ferrite magnets lose ~0.2%/°C of remanence
- Maximum operating temperature typically 150–200°C for ferrite
- NdFeB: 120–180°C depending on grade
- Rotor temperature must be estimated or measured for demag verification

## Key Equations

- Torque (combined PM + reluctance): [[torque-equation]]
- Saliency ratio with magnets: [[saliency-ratio]]
- Power factor: [[power-factor]]
- PM flux linkage: depends on magnet grade and volume

## Research References

### Key Papers

- **Bao et al.** — Ferrite-assisted SynRM design and optimization
- **Lopez et al.** — Reliable PMaSynRM design with ferrite magnets
- **Mohammadi et al.** — Traction application of PMaSynRM

### Design Topics

- Magnet placement optimization
- Ferrite vs. NdFeB trade-off analysis
- Demagnetization withstand capability
- Manufacturing methods for magnet insertion

## Related Pages

- [[synrm-topology]] — Base SynRM topology
- [[flux-barriers]] — Flux barrier design principles
- [[power-factor]] — Power factor analysis
- [[saliency-ratio]] — Saliency ratio definition
- [[torque-equation]] — Torque production equations
- [[ipmsm-topology]] — Interior PM motor (higher PM contribution)
- [[dq-theory]] — dq reference frame theory

## Tags

#topology #pmasynrm #synrm #reluctance #pm #ferrite #ndfeb #power-factor #ev-traction
