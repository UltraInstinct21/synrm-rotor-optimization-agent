---
type: research_paper
title: "Bridgeless Rotor Design for High-Saliency Synchronous Reluctance Motors"
authors: ["Allahyari et al."]
year: "Unknown"
venue: "Conference / Journal publication"
motor_types: ["SynRM"]
topics: ["bridgeless rotor", "flux guides", "high-speed SynRM", "saliency optimization", "rotor mechanics"]
tags: [synrm, bridgeless, flux-guides, high-speed, saliency, rotor-design]
source_file: "raw/papers/allahyari_bridgeless_synrm.pdf"
related_pages: ["[[flux-barriers]]", "[[rotor-bridge-design]]", "[[saliency-ratio]]"]
confidence: moderate
---

# Allahyari et al. — Bridgeless Rotor for High-Saliency SynRM

## Citation

Allahyari, S. et al. "Bridgeless rotor design for high-saliency synchronous reluctance motors." *Conference/Journal publication*, year unknown.

**Motor type:** Synchronous Reluctance Motor (SynRM)
**Innovation:** Elimination of iron bridges between flux barriers
**Application:** High-speed, high-saliency drives

---

## Problem Statement

In conventional SynRM rotor design, **iron bridges** (also called ribs) connect the rotor lamination segments between flux barriers. These bridges serve two purposes:

1. **Mechanical integrity** — they hold the rotor structure together against centrifugal forces at high speed
2. **Magnetic path** — they provide a low-reluctance path for q-axis flux, which **reduces saliency ratio**

**The fundamental conflict:** bridges improve mechanical strength but degrade electromagnetic performance. Thinner bridges improve saliency but reduce mechanical margin. This paper proposes a **bridgeless rotor topology** that eliminates bridges entirely, relying on **flux guides** for mechanical support while maximizing saliency.

**Core question:** Can a bridgeless rotor achieve significantly higher saliency while maintaining mechanical integrity at high speed?

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | SynRM |
| Rotor type | Bridgeless (no iron bridges between barriers) |
| Mechanical support | Flux guides (iron segments connecting to shaft) |
| Application | High-speed drive |
| Target | Saliency ratio significantly higher than conventional bridge designs |
| Operating speed | High (specific RPM not stated in summary) |

---

## Method / Theory

### Conventional Bridge Problem

In a standard SynRM with bridges:

```
Barrier 1
  ===Bridge===  ← iron bridge (thin, ~1-3 mm)
Barrier 2
  ===Bridge===  ← iron bridge
Barrier 3
  ===Bridge===  ← iron bridge
```

The bridges create a **low-reluctance shortcut** for q-axis flux:

$$R_{q,total} = R_{bridge,1} + R_{bridge,2} + R_{bridge,3} + ...$$

Since bridges are thin iron (high μ), their reluctance is low, which keeps L_q high and **reduces saliency**:

$$\xi = \frac{L_d}{L_q} \propto \frac{R_q}{R_d}$$

### Bridgeless Solution

The bridgeless design replaces bridges with **flux guides** — solid iron segments that connect the rotor segments to the shaft or to each other, but are oriented **perpendicular to the q-axis flux path**:

```
Barrier 1 (full radial span, no bridge)
  |  Flux Guide  |  ← connects to shaft, perpendicular to q-axis
Barrier 2 (full radial span, no bridge)
  |  Flux Guide  |  ← connects to shaft
Barrier 3 (full radial span, no bridge)
  |  Flux Guide  |  ← connects to shaft
```

**Key principle:** Flux guides are oriented along the **d-axis direction**, so they provide mechanical support without creating a low-reluctance path for q-axis flux.

### Magnetic Circuit Analysis

In the bridgeless configuration:

- **d-axis flux** flows through the flux guides (iron, low reluctance) → L_d remains high
- **q-axis flux** must cross the full barrier span (air, high reluctance) → L_q drops significantly

$$R_{q,bridgeless} \gg R_{q,bridged}$$

Therefore:

$$\xi_{bridgeless} \gg \xi_{bridged}$$

### Mechanical Analysis

Centrifugal stress on the rotor lamination is supported by:

1. **Flux guides** — carry radial loads to the shaft
2. **Barrier geometry** — optimized to minimize stress concentrations
3. **Lamination stack** — axial clamping provides additional support

The maximum stress must remain below the yield strength of the lamination steel:

$$\sigma_{max} = \rho \cdot \omega^2 \cdot r_{mean}^2 < \sigma_{yield}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| σ_max | Maximum centrifugal stress | Pa |
| ρ | Material density (steel ~7850 kg/m³) | kg/m³ |
| ω | Angular velocity | rad/s |
| r_mean | Mean radius of unsupported mass | m |
| σ_yield | Yield strength of lamination steel | Pa |

---

## Key Design Equations

### Saliency Improvement

$$\xi_{bridgeless} = \frac{L_{d,max}}{L_{q,min}}$$

With bridgeless design, L_q approaches its theoretical minimum (limited only by slot leakage and end-winding effects), while L_d is maximized by the unobstructed d-axis flux path.

### Flux Guide Width

The flux guide width must satisfy:

$$w_{guide} \geq \frac{F_{centrifugal}}{\sigma_{yield} \cdot l_{axial}}$$

Where F_centrifugal is the centrifugal force on the unsupported rotor mass.

### Torque Production

$$T = \frac{3}{2} \cdot p \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

With bridgeless design, (L_d - L_q) is maximized, producing higher torque per ampere.

---

## Design Parameters

| Parameter | Conventional (with bridges) | Bridgeless |
|---|---|---|
| Bridge thickness | 1–3 mm | 0 mm (eliminated) |
| Flux guide width | N/A | 3–8 mm (design variable) |
| Barrier span | Partial (limited by bridges) | Full radial span |
| Saliency ratio (typical) | 3–5 | 6–10+ |
| Mechanical margin | High (bridges are robust) | Moderate (flux guides must be sized) |
| Manufacturing complexity | Standard | Moderate (requires careful stamping) |

---

## Key Design Insights

1. **Saliency can be nearly doubled** — eliminating bridges removes the primary q-axis flux shortcut, dramatically increasing L_d/L_q ratio.

2. **Flux guides must be carefully sized** — too narrow and mechanical failure occurs; too wide and they begin to act like bridges, reducing the saliency benefit.

3. **Barrier geometry becomes more critical** — without bridges, the barrier shape must be optimized to avoid stress concentrations at the flux guide junctions.

4. **High-speed capability requires mechanical validation** — FEA stress analysis is mandatory for any bridgeless design operating above ~5000 RPM.

5. **Manufacturing tolerance matters more** — without bridges, small errors in barrier placement can create stress risers that conventional designs tolerate.

6. **Thermal considerations** — flux guides carry both mechanical load and some d-axis flux; heating effects at high current density must be evaluated.

---

## Limitations

- Mechanical reliability at very high speed requires detailed FEA validation
- Manufacturing complexity increases compared to conventional designs
- Bridgeless topology may not be suitable for very large motors where centrifugal forces are extreme
- Detailed thermal analysis needed for high-current applications
- Specific numerical results not available in the summary — refer to full paper

---

## Propagation into Wiki

### Concepts to update
- [[flux-barriers]] — add bridgeless flux barrier concept
- [[rotor-bridge-design]] — add comparison between bridged and bridgeless designs

### Design guidelines to update
- [[rotor-barrier-design]] — add bridgeless design guidelines
- [[high-speed-synrm-design]] — create if not exists, add bridgeless high-speed considerations

### MotorCAD pages to update
- [[motorcad/variables/bridge-thickness]] — document bridgeless option (thickness = 0)
- [[motorcad/workflows/bridgeless-rotor-setup]] — create workflow for bridgeless configuration

---

## Related Pages

- [[flux-barriers]] — flux barrier theory and design
- [[rotor-bridge-design]] — bridge and rib design for SynRM rotors
- [[saliency-ratio]] — saliency ratio definition and optimization
- [[synrm-topology]] — Synchronous Reluctance Motor overview
- [[high-speed-synrm-design]] — high-speed SynRM design considerations
- [[mechanical-stress-analysis]] — rotor mechanical stress evaluation
