---
type: design_guideline
title: Rotor Barrier Design
aliases: [flux-barrier-geometry, barrier-layer-design]
tags: [synrm, rotor, barriers, saliency, design-guideline, flux-barriers]
motor_types: [synrm, pmasynrm]
topics: [barrier-geometry, saliency-ratio, reluctance-torque, rotor-structure]
related_pages: [flux-barriers, saliency-ratio, rotor-bridge-design, dq-theory, reluctance-torque]
source_files: []
confidence: high
---

# Rotor Barrier Design

## Purpose

Rotor flux barriers are the defining geometric feature of a Synchronous Reluctance Motor (SynRM). Their count, shape, angle, and width directly determine saliency ratio, torque capability, torque ripple, power factor, and mechanical integrity. This page consolidates practical design guidelines for barrier geometry.

---

## Number of Barrier Layers

### Typical range

| Layers | Typical application | Notes |
|---|---|---|
| 1–2 | Low-cost, low-performance | Poor saliency, high torque ripple |
| 3–4 | Industrial SynRM (most common) | Good balance of saliency and mechanical strength |
| 5–6 | High-performance, high saliency | Diminishing saliency returns, manufacturing difficulty |
| 7+ | Research / exotic | Mechanical fragility, very difficult to manufacture |

### Design rule

- **3–5 layers** is the practical sweet spot for industrial SynRM.
- Each additional layer increases the number of flux paths, improving the d-axis flux while maintaining high q-axis reluctance.
- Beyond 5 layers, the incremental saliency gain is small (~1–3% per layer), but mechanical stress and manufacturing complexity increase significantly.
- More barriers increase **torque ripple** if barrier angles are not carefully optimized.

### Tradeoff summary

```
More barriers → Higher saliency → Higher torque density
             → Lower mechanical strength
             → Higher manufacturing difficulty
             → Higher torque ripple (if not optimized)
```

---

## Barrier Angle

### Fundamental relation

The barrier angle α (the angular span of a single barrier layer) is related to the pole count p and the number of barriers k:

$$\alpha = \frac{\pi / p}{k + 1}$$

Where:
- α = angular span per barrier (rad or deg)
- p = pole pairs
- k = number of barrier layers per pole

### Example (4-pole, 3 layers)

$$\alpha = \frac{\pi / 2}{3 + 1} = \frac{\pi}{8} = 22.5°$$

### Practical considerations

- Barriers should be **evenly distributed** across the pole arc to produce uniform flux distribution.
- Uneven barrier spacing can create localized flux concentrations and increase torque ripple.
- The **first barrier** (closest to the shaft) typically has the largest angular span; outer barriers are narrower.
- Barrier angles can be optimized away from the均匀 distribution to shape the airgap flux waveform and reduce harmonic content.

---

## Barrier Width Sizing

### Principle

Barrier widths should be sized so that the iron segments between barriers (the flux-carrying ribs and segments) reach **equal magnetic saturation** in the d-axis.

If one segment saturates before others, the flux path becomes constricted and the effective saliency drops.

### Design procedure

1. Calculate the d-axis flux per pole: Φ_d = B_peak × A_pole
2. For each segment between barriers, set the width so that B_segment ≈ B_sat (typically 1.8–2.0 T for silicon steel).
3. Wider segments carry more flux before saturating — use this to balance saturation across layers.

### Rules of thumb

- Inner segments (closer to shaft) carry less total flux → can be narrower.
- Outer segments (closer to airgap) carry more flux → should be wider.
- Typical inner segment width: 3–8 mm.
- Typical outer segment width: 5–15 mm.

---

## Segment Width Ratio (MMF Matching)

### Principle

The ratio of adjacent segment widths should approximate the ratio of the MMF drops across them:

$$\frac{S_i}{S_{i+1}} = \frac{MMF_i}{MMF_{i+1}}$$

Where:
- S_i = width of segment i
- MMF_i = MMF drop across segment i

### Physical meaning

- Each barrier "consumes" MMF as flux crosses it.
- Segments closer to the airgap must carry more total flux and experience a larger MMF drop.
- Matching the width ratio to the MMF ratio ensures uniform saturation and maximizes the use of iron.

---

## Barrier Shape: Curved vs. Straight

### Straight barriers

- Simple to manufacture.
- Produce somewhat non-uniform flux density in the segments.
- Acceptable for low-to-medium performance motors.

### Curved barriers

- Improve flux distribution within the iron segments.
- Reduce peak flux density and localized saturation.
- Lower torque ripple compared to straight barriers.
- More complex to stamp/laminate.
- **Preferred for high-performance SynRM**.

### Practical note

- Curved barriers can be designed as arcs of circles, ellipses, or splines.
- Smooth curvature avoids stress concentrations in the laminations.
- Manufacturing tooling cost is higher, but the electromagnetic benefit is significant at high performance levels.

---

## U-Shape vs. V-Shape Barrier Topology

| Feature | U-Shape | V-Shape |
|---|---|---|
| Saliency ratio | Higher (typically 5–10% better) | Lower |
| Torque density | Higher | Moderate |
| Mechanical strength | Lower (long unsupported spans) | Higher (shorter spans, better bracing) |
| Manufacturing | More complex | Simpler |
| Thermal robustness | Moderate | Better |
| Typical application | High-performance SynRM | Cost-sensitive, high-speed applications |

### Design choice

- **U-shape** is preferred when maximizing saliency and torque density is the priority.
- **V-shape** is preferred when mechanical robustness, manufacturability, or high-speed capability is the priority.
- Hybrid shapes (modified U with tapered legs) can combine benefits.

---

## Effect on Key Performance Metrics

| Parameter | More barriers | Wider barriers | Curved barriers |
|---|---|---|---|
| Saliency ratio | ↑ | ↑ (to a point) | ↑ slightly |
| Torque | ↑ | ↑ | ↑ slightly |
| Power factor | ↑ | ↑ (to a point) | — |
| Torque ripple | ↑ (if not optimized) | ↑ | ↓ |
| Mechanical strength | ↓ | ↓ | Neutral |
| Manufacturing difficulty | ↑ | Neutral | ↑ |

---

## References

- Orlova, M. S. — barrier shape optimization for SynRM
- Nagarkar, A. — multi-barrier rotor design
- Lopez, T. — SynRM barrier geometry and mechanical limits
- Korman, B. — U-shape vs V-shape comparison
- Pyrhönen, J. — rotational electrical machines (textbook)

---

## Related Pages

- [[flux-barriers]] — detailed barrier physics and flux path behavior
- [[saliency-ratio]] — definition, calculation, and improvement methods
- [[rotor-bridge-design]] — mechanical bridge sizing and tradeoffs
- [[dq-theory]] — d-q axis theory underlying barrier design
- [[reluctance-torque]] — torque production mechanism
- [[synrm-topology]] — overall SynRM motor topology
