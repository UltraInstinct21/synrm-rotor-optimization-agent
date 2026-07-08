---
type: topology
title: Synchronous Reluctance Motor (SynRM)
aliases: [SynRM, SyncRel, Synchronous Reluctance]
tags: [topology, synrm, reluctance, synchronous, no-magnet]
motor_type: synrm
topics: [operating-principle, rotor-design, torque-production, power-factor]
related_pages: [flux-barriers, saliency-ratio, torque-equation, dq-theory, pmasynrm-topology, srm-topology, ipmsm-topology]
confidence: verified
---

# Synchronous Reluctance Motor (SynRM)

## Operating Principle

The SynRM produces torque solely through **reluctance torque** arising from magnetic anisotropy in the rotor. When a rotating stator MMF is applied, the rotor aligns its path of minimum reluctance (d-axis) with the stator field. The torque is proportional to the difference between d-axis and q-axis inductances:

$$T = \frac{3}{2} p (L_d - L_q) i_d i_q$$

This is the **reluctance torque** component of the general dq torque equation, with no PM flux linkage term ($\lambda_{PM} = 0$).

### Key Condition

For nonzero torque, the rotor must exhibit **magnetic saliency**: $L_d \neq L_q$. In a SynRM, this is achieved entirely through geometric anisotropy — flux barriers in the rotor create a high-reluctance q-axis path while the iron ribs provide a low-reluctance d-axis path.

## Rotor Construction

The SynRM rotor contains **no magnets, no windings, and no cage** (in the synchronous variant). Torque anisotropy is created by:

- **Flux barriers**: Axial slots or cutouts in the rotor laminations that interrupt q-axis flux paths
- **Iron ribs (webs)**: Thin iron segments that mechanically hold the rotor segments together
- **Bridges**: Thin iron connections at the rotor periphery that close the barriers

### Barrier Configurations

| Configuration | Description | Typical Use |
|---|---|---|
| Simple barriers | 1–2 layers of flux barriers | Low-cost, low-performance |
| Multi-layer barriers | 3–5+ layers | Higher saliency, industrial drives |
| U-shape | Barriers follow U-shaped contour | Good mechanical integrity |
| V-shape | Barriers angled inward | Moderate saliency |
| spoke-type | Barriers radiate outward | High saliency, complex manufacturing |

### Rotor Geometry Parameters

The barrier geometry directly determines the saliency ratio and hence motor performance. Key parameters include:

- Barrier count (number of layers)
- Barrier angle
- Barrier width
- Bridge/rib thickness
- Web thickness
- Barrier radial position

These are the primary variables in SynRM rotor optimization. See [[flux-barriers]] for detailed barrier design principles.

## Stator Design

The SynRM uses a **standard distributed winding** stator, identical to induction motor stators:

- Sinusoidal MMF distribution
- 3-phase, typically 48-slot or 36-slot for 4-pole
- Short-pitched or full-pitch coils
- No special stator features required

The stator design is generally **not the differentiator** — performance gains come from rotor optimization.

## Key Performance Characteristics

### Torque Density

SynRM torque density is **lower** than PM motors because reluctance torque alone is limited by the saliency ratio. Typical saliency ratios ($L_d/L_q$) range from 3–10 depending on barrier design.

### Power Factor

The most significant limitation of SynRM is **low power factor**, typically 0.5–0.7. This is because:

- High inductance is required for reluctance torque
- High inductance draws large magnetizing current
- The magnetizing current is purely reactive

Power factor can be improved through:
- Optimized barrier geometry
- Increasing number of barrier layers
- Using higher current densities (at the cost of losses)

See [[power-factor]] for detailed analysis.

### Efficiency

SynRM efficiency is **competitive** with induction motors and can approach IE5 levels:

- No rotor copper losses (no rotor windings)
- No magnet eddy current losses
- Stator copper losses dominate
- Iron losses from rotor flux pulsation

### Speed Range

- Constant torque region up to base speed
- Field weakening extends to 2–3× base speed
- No back-EMF constraint (no magnets), so field weakening is straightforward

## Advantages

| Advantage | Explanation |
|---|---|
| No rare-earth magnets | Eliminates supply chain risk and cost volatility |
| Simple rotor construction | Laminated steel only, no windings or magnets |
| Robust mechanical structure | No magnets to crack, no windings to degrade |
| Good efficiency | No rotor copper losses |
| Low rotor losses | Especially at high speeds |
| Low cost | Material cost dominated by steel and copper |
| High speed capability | No magnet retention concerns |
| Field weakening | Straightforward due to high inductance |
| IE5 achievable | With optimized design |

## Disadvantages

| Disadvantage | Explanation |
|---|---|
| Low power factor (0.5–0.7) | Requires large magnetizing current from inverter |
| Low torque density | Reluctance torque limited by saliency ratio |
| Torque ripple | Can be significant without careful barrier optimization |
| Inverter sizing | High reactive current requires oversized inverter |
| Acoustic noise | Torque ripple contributes to vibration |
| Complex rotor optimization | Barrier geometry strongly affects all performance metrics |
| Sensitive to manufacturing tolerances | Bridge thickness variations affect saliency |

## Applications

### Primary Applications

- **Industrial variable-speed drives** (pumps, fans, compressors)
- **HVAC systems**
- **General-purpose industrial motors**

### Emerging Applications

- **Electric vehicle traction** (with PM assistance → [[pmasynrm-topology]])
- **High-efficiency pump drives**
- **Wind turbine generators**

### Not Suitable For

- Applications requiring very high torque density (use [[ipmsm-topology]])
- Servo applications requiring very smooth torque (torque ripple)
- Cost-sensitive applications where induction motor suffices

## Comparison with Other Topologies

| Parameter | SynRM | IPMSM | PMaSynRM | Induction |
|---|---|---|---|---|
| Torque mechanism | Reluctance only | PM + reluctance | PM + reluctance | Induction |
| Magnets | None | NdFeB/NdFeB | Ferrite/NdFeB | None |
| Power factor | 0.5–0.7 | 0.8–0.95 | 0.8–0.9 | 0.8–0.85 |
| Efficiency | Good | Excellent | Very good | Good |
| Cost | Low | High | Medium | Low |
| Torque density | Low | High | Medium-high | Medium |

## Key Equations

- Torque: [[torque-equation]]
- Saliency ratio: [[saliency-ratio]]
- Power factor: [[power-factor]]
- dq theory: [[dq-theory]]

## Research References

### Foundational

- **Li et al.** — Comprehensive overview of SynRM design and control
- **Nagarkar et al.** — Rotor flux barrier design optimization
- **Saxena et al.** — Control strategies for SynRM drives

### Design Optimization

- Barrier geometry optimization methods
- Multi-objective optimization for torque, PF, and torque ripple
- Manufacturability constraints in barrier design

## Related Pages

- [[flux-barriers]] — Flux barrier design principles
- [[saliency-ratio]] — Saliency ratio definition and optimization
- [[torque-equation]] — Torque production equations
- [[dq-theory]] — dq reference frame theory
- [[power-factor]] — Power factor analysis
- [[pmasynrm-topology]] — PM-assisted variant
- [[srm-topology]] — Switched reluctance motor (different topology)
- [[ipmsm-topology]] — Interior PM motor

## Tags

#topology #synrm #reluctance #synchronous #no-magnet #flux-barriers #saliency #power-factor
