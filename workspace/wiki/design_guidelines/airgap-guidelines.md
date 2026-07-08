---
type: design_guideline
title: Airgap Guidelines
aliases: [mechanical-airgap, airgap-selection]
tags: [synrm, airgap, sizing, manufacturing, design-guideline]
motor_types: [synrm, pmasynrm, ipmsm, spm, induction]
topics: [airgap, sizing, manufacturing-tolerance, power-factor, inductance]
related_pages: [sizing-equation, synrm-topology, saliency-ratio]
source_files: []
confidence: high
---

# Airgap Guidelines

## Purpose

The mechanical airgap g is the radial distance between the rotor OD and the stator bore. It is a critical design parameter affecting inductance, power factor, losses, manufacturing difficulty, and mechanical reliability. This page provides guidelines for selecting the airgap in SynRM and other motor types.

---

## Typical Airgap Range

| Motor type | Typical airgap | Notes |
|---|---|---|
| Small SynRM (<5 kW) | 0.3–0.5 mm | Manufacturing-dominated |
| Medium SynRM (5–50 kW) | 0.4–0.8 mm | Industrial sweet spot |
| Large SynRM (>50 kW) | 0.6–1.2 mm | Mechanical reliability dominated |
| IPM / SPM | 0.5–1.5 mm | Magnet retention considerations |
| Induction motor | 0.3–1.0 mm | Rotor bar/airgap interaction |

### Industrial SynRM (45 kW class)

- **Recommended: 0.5–0.8 mm** (per side).
- The AGENTS.md specification uses g = 0.5 mm — this is at the lower end and appropriate for a well-manufactured motor.

---

## Pyrhönen Formula

### Empirical sizing formula

For motors in the range 1–100 kW:

$$g = \frac{0.18 + 0.006 \cdot P^{0.4}}{1000} \text{ (meters)}$$

Where:
- g = mechanical airgap (m)
- P = rated power (W)

### Example (45 kW)

$$g = \frac{0.18 + 0.006 \cdot (45000)^{0.4}}{1000}$$

$$g = \frac{0.18 + 0.006 \cdot 41.6}{1000} = \frac{0.18 + 0.25}{1000} = \frac{0.43}{1000} = 0.43 \text{ mm}$$

### Interpretation

- The formula gives a **minimum recommended airgap** based on power level.
- Actual airgap may be larger for manufacturing tolerance, rotor eccentricity, or high-speed operation.
- For the 45 kW SynRM, 0.5 mm is slightly above the Pyrhönen minimum — consistent with good design practice.

---

## Effect on Inductance

### d-axis inductance

$$L_d \propto \frac{1}{g + g_{sat}}$$

Where:
- g = mechanical airgap
- g_sat = equivalent airgap due to saturation (increases with flux density)

### q-axis inductance

$$L_q \propto \frac{1}{g + g_{sat,q}}$$

For SynRM, L_q is dominated by the barrier reluctance, so the airgap has less effect on L_q than on L_d.

### Key insight

- Reducing g increases L_d more than L_q → **increases saliency ratio**.
- This is why smaller airgaps are preferred for electromagnetic performance.
- However, the effect diminishes because g_sat becomes significant at high flux densities.

---

## Effect on Power Factor

### Relation

Power factor in SynRM depends on the saliency ratio L_d/L_q:

$$PF = \cos\left(\arctan\left(\frac{L_d - L_q}{L_d + L_q}\right)\right)$$

### Airgap effect

- Smaller g → higher L_d/L_q → higher PF.
- The effect is moderate: reducing g from 0.8 mm to 0.5 mm typically improves PF by 2–5%.
- Beyond a point, further reduction yields diminishing returns as saturation dominates.

### Design implication

- Airgap selection is a **secondary lever** for PF improvement.
- Barrier geometry and current angle optimization have a larger impact on PF.

---

## Effect on Losses

### Airgap friction (windage) loss

$$P_{windage} \propto \frac{\omega^2 \cdot R^3 \cdot L}{g}$$

Where:
- ω = angular velocity
- R = rotor radius
- L = stack length
- g = airgap

- Smaller airgap → **higher windage loss** (inversely proportional to g).
- Windage loss becomes significant at high speeds (>6000 RPM) and small airgaps.

### Iron loss

- Smaller airgap → higher flux density in teeth → higher iron loss.
- Effect is moderate and usually secondary to windage.

### Total loss tradeoff

- At low speed: windage loss is negligible → smaller airgap is better.
- At high speed: windage loss can dominate → larger airgap may be preferred.

---

## Manufacturing and Mechanical Considerations

### Rotor eccentricity

- No rotor is perfectly centered. Manufacturing tolerances create eccentricity e.
- Effective airgap varies: g_min = g − e, g_max = g + e.
- **Minimum airgap must accommodate eccentricity**:

$$g_{min} = g_{nominal} - e_{max} \geq 0.2 \text{ mm (absolute minimum)}$$

If g_min < 0.2 mm, there is risk of rotor-stator rub.

### Typical eccentricity

| Manufacturing quality | Eccentricity e |
|---|---|
| Standard (±0.05 mm) | 0.05–0.10 mm |
| Precision (±0.02 mm) | 0.02–0.05 mm |
| High-precision (±0.01 mm) | 0.01–0.02 mm |

### Design rule

$$g \geq e_{max} + g_{safety}$$

Where:
- g_safety ≥ 0.15–0.20 mm (minimum clearance after eccentricity)

### Thermal expansion

- Rotor and stator expand at different rates during operation.
- Rotor OD expansion reduces airgap.
- **Account for thermal growth**: g_thermal = g_cold − Δg_thermal.
- For steel rotors: Δg_thermal ≈ α × R × ΔT (typically 0.01–0.05 mm for moderate temperature rise).

### Bearing tolerance

- Bearing runout contributes to effective eccentricity.
- Ball bearing runout: 0.01–0.03 mm typical.
- Sleeve bearing: 0.02–0.05 mm typical.

---

## Airgap Selection Process

```
1. Calculate minimum airgap from Pyrhönen formula
2. Add manufacturing eccentricity margin
3. Add thermal expansion margin
4. Check electromagnetic performance (FEA with nominal g)
5. Check windage loss at operating speed
6. Verify no rub condition at worst-case eccentricity
7. Finalize g within typical range
```

---

## Effect on Other Design Parameters

| Parameter | Effect of reducing g |
|---|---|
| L_d | ↑ |
| L_q | ↑ (less than L_d) |
| Saliency ratio | ↑ |
| Power factor | ↑ (moderate) |
| Torque | ↑ slightly |
| Windage loss | ↑ |
| Iron loss | ↑ slightly |
| Manufacturing difficulty | ↑ |
| Rub risk | ↑ |
| Unbalanced magnetic pull | ↑ |

---

## Special Cases

### High-speed motors (>10,000 RPM)

- Windage loss dominates → consider larger airgap (1.0–2.0 mm).
- Rotor dynamics critical → eccentricity control essential.

### Fractional-slot concentrated winding motors

- High harmonic content in airgap flux → sensitive to airgap variations.
- Larger airgap may reduce cogging and torque ripple.

### Cryogenic or vacuum motors

- No air cooling → windage loss irrelevant → smaller airgap possible.
- Thermal expansion may be different → recalculate Δg_thermal.

---

## References

- Pyrhönen, J. — rotational electrical machines (airgap sizing formula)
- Boldea, I. — reluctance synchronous motors (airgap effects)
- Lopez, T. — SynRM airgap and manufacturing considerations
- Gieras, J. — airgap selection for PM motors (applicable principles)

---

## Related Pages

- [[sizing-equation]] — fundamental torque-volume relationship
- [[synrm-topology]] — overall SynRM design
- [[saliency-ratio]] — how airgap affects saliency
- [[stack-length-guidelines]] — interaction between airgap and stack length
- [[rotor-barrier-design]] — barrier geometry and its interaction with airgap
