---
type: design_guideline
title: Rotor Bridge Design
aliases: [rotor-rib-design, bridge-thickness]
tags: [synrm, rotor, bridge, mechanical, stress-analysis, design-guideline]
motor_types: [synrm, pmasynrm]
topics: [bridge-thickness, mechanical-integrity, stress-analysis, rotor-structure]
related_pages: [flux-barriers, rotor-barrier-design, saliency-ratio]
source_files: []
confidence: high
---

# Rotor Bridge Design

## Purpose

Rotor bridges are the thin iron segments that mechanically connect the rotor lamination segments separated by flux barriers. They are a critical compromise between electromagnetic performance (high saliency needs thin bridges) and mechanical integrity (high-speed operation needs strong bridges). This page provides design guidelines for bridge thickness, stress analysis, and safety verification.

---

## Bridge Function

### Structural role

- Bridges carry the centrifugal load of the rotor segments during rotation.
- They form the mechanical "spokes" that hold the rotor lamination stack together.
- Without adequate bridges, rotor segments detach under centrifugal force → catastrophic failure.

### Electromagnetic penalty

- Bridges provide a low-reluctance flux leakage path across the q-axis.
- Flux leaking through bridges reduces the effective d-axis/q-axis inductance difference.
- **Thinner bridges → higher saliency → better electromagnetic performance.**
- **Thicker bridges → stronger rotor → better mechanical reliability.**

This is the fundamental tradeoff in bridge design.

---

## Minimum Thickness

### Manufacturing limit

- **1.0 mm absolute minimum** — this is the stamping/lamination manufacturing limit for most suppliers.
- Bridges thinner than 1.0 mm are prone to tearing during stamping, warping during annealing, and cracking during assembly.
- Some advanced lamination processes can achieve 0.8 mm, but this is specialty manufacturing.

### Design guideline

| Application | Recommended bridge minimum |
|---|---|
| General industrial | 1.5–3.0 mm |
| High-speed (>10,000 RPM) | 2.0–4.0 mm |
| Low-cost / low-speed | 1.0–1.5 mm |
| Automotive / high-reliability | 2.0–3.0 mm |

---

## Typical Range

| Parameter | Range | Notes |
|---|---|---|
| Bridge thickness | 0.5–3.0 mm | Electromagnetic optimum is near minimum |
| Web thickness | 5–30 mm | Structural connection between barriers |
| Typical industrial | 1.5–2.5 mm | Balance of performance and strength |
| High-speed (>6000 RPM) | 2.0–4.0 mm | Centrifugal stress increases with ω² |

---

## Electromagnetic Tradeoff

### Effect on saliency

The bridge flux leakage reduces the effective saliency ratio. For a bridge of thickness t_bridge:

- Reducing t_bridge from 2.0 mm to 1.0 mm can increase saliency by 10–25%.
- Beyond a point, further thinning yields diminishing returns as other leakage paths dominate.

### Effect on torque

$$\Delta T \propto \frac{1}{L_q} - \frac{1}{L_d}$$

Thinner bridges increase L_d more than L_q (because bridges primarily affect q-axis leakage), so the torque increases.

### Effect on power factor

Thinner bridges improve power factor by increasing the saliency ratio, which reduces the reactive power requirement.

---

## Mechanical Stress Analysis

### Centrifugal stress

The centrifugal stress on a bridge depends on:

$$\sigma_{centrifugal} = \rho \cdot \omega^2 \cdot R_{mean} \cdot A_{segment} / A_{bridge}$$

Where:
- σ = stress (Pa)
- ρ = material density (kg/m³, ~7800 for steel)
- ω = angular velocity (rad/s)
- R_mean = mean radius of the segment (m)
- A_segment = cross-sectional area of the segment being supported (m²)
- A_bridge = cross-sectional area of the bridge (m²)

### Key relationships

- Stress scales with **ω²** — doubling speed quadruples stress.
- Stress scales with **R²** — larger rotors experience higher stress.
- Longer rotor stacks experience higher stress per unit length (more mass to support).

### Safety factor

$$SF = \frac{\sigma_{yield}}{\sigma_{max}}$$

- **Minimum safety factor: 2.0** for general industrial motors.
- **Safety factor ≥ 2.5** recommended for high-reliability or high-speed applications.
- Safety factor accounts for material variability, manufacturing tolerances, and transient overloads.

---

## Neuber / Glinka Plastic Correction

### When needed

- At high speeds, the elastic stress calculation may exceed the material yield strength.
- In this regime, **plastic deformation** occurs at stress concentration points (bridge corners, barrier edges).
- The Neuber or Glinka rule corrects the elastic FEA stress to estimate the actual elastic-plastic stress.

### Neuber's rule

$$\sigma_{actual} \cdot \epsilon_{actual} = \sigma_{elastic} \cdot \epsilon_{elastic}$$

Where:
- σ_actual, ε_actual = actual stress and strain at the notch
- σ_elastic, ε_elastic = stress and strain from linear elastic FEA

### Glinka's rule (energy-based)

$$\sigma_{actual} = \sigma_{elastic} \cdot \left(\frac{\sigma_{elastic}}{E \cdot \epsilon_{elastic}}\right)^{n/(1+n)}$$

Where:
- E = Young's modulus
- n = strain hardening exponent

### Practical approach

1. Run linear elastic FEA to get peak elastic stress.
2. Apply Neuber/Glinka correction to estimate actual stress-strain state.
3. Compare corrected stress to material fatigue or yield limit.
4. If corrected stress exceeds limit → increase bridge thickness or modify geometry.

---

## Bridge Geometry Considerations

### Cross-section

- Rectangular cross-section is simplest to manufacture.
- Rounded corners reduce stress concentrations (add fillet radius ≥ 0.3 mm).
- Tapered bridges (thinner at center, wider at ends) can distribute stress more uniformly.

### Position

- Bridges closer to the shaft experience lower centrifugal stress (smaller radius).
- Bridges near the rotor OD experience the highest stress.
- **Outer bridges are the critical design point** — size them for worst-case stress.

### Connection to web

- The bridge-web junction is a stress concentration point.
- Fillet radii at this junction are critical for fatigue life.
- Minimum fillet radius: 0.5 mm (larger is better).

---

## Verification Checklist

- [ ] Bridge thickness ≥ 1.0 mm (manufacturing limit)
- [ ] Safety factor ≥ 2.0 at rated speed
- [ ] Safety factor ≥ 2.0 at maximum overspeed (typically 1.2× rated)
- [ ] Neuber/Glinka correction applied if elastic stress exceeds yield
- [ ] Stress concentration factors included for fillet radii
- [ ] Fatigue assessment performed if variable speed operation
- [ ] FEA validation for complex geometries

---

## References

- Hausmann, G. — rotor bridge stress analysis for SynRM
- Lopez, T. — mechanical limits of SynRM rotor bridges
- Neuber, H. — stress-strain relation at notches
- Glinka, G. — energy-based plastic correction rule
- Pyrhönen, J. — rotational electrical machines (mechanical design chapter)

---

## Related Pages

- [[flux-barriers]] — how barriers create the reluctance paths that bridges must span
- [[rotor-barrier-design]] — barrier geometry that determines bridge loading
- [[saliency-ratio]] — electromagnetic benefit of thin bridges
- [[synrm-topology]] — overall rotor topology
