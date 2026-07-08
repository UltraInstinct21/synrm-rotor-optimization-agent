---
type: equation
title: Loss Equations
aliases: [losses, copper loss, iron loss, windage loss, efficiency]
tags: [equations, losses, efficiency, copper-loss, iron-loss, windage]
motor_types: [SynRM, PMaSynRM, IPMSM, SPM, Induction]
topics: [losses, efficiency, thermal-design, optimization]
source_pages: []
related_concepts: [torque-equation, synrm-topology, thermal-design]
related_motorcad_variables: [StatorCopperLossAC, StatorIronLoss_Total, Efficiency, InputPower, ShaftTorque]
confidence: high
verification_status: verified
---

# Loss Equations

## Statement

### Copper Loss

$$P_{cu} = m \cdot R_s \cdot I_{rms}^2$$

### Iron Loss (Steinmetz)

$$P_{fe} = k_h \cdot \left(\frac{\omega}{2}\pi\right) \cdot B_{pk}^n + k_e \cdot \left(\frac{\omega}{2\pi} \cdot B_{pk}\right)^2$$

### Windage Loss

$$P_w = k_w \cdot \omega^3 \cdot D^5$$

### Total Loss

$$P_{total} = P_{cu} + P_{fe} + P_{windage} + P_{mechanical}$$

### Efficiency

$$\eta = \frac{P_{out}}{P_{out} + P_{total}} \times 100\%$$

---

## Original Notation

| Source | Notation | Meaning |
|--------|----------|---------|
| Lopez et al. | $P_{cu} = m R_s I_{rms}^2$ | Standard Joule loss |
| Steinmetz | $P_{fe} = k_h f B^n + k_e (fB)^2$ | Hysteresis + eddy current |
| Pyrhönen et al. | $P_w = k_w \omega^3 D^5$ | Windage empirical form |

---

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $P_{cu}$ | Copper (winding) loss | W |
| $P_{fe}$ | Iron (core) loss | W |
| $P_w$ | Windage loss | W |
| $P_{total}$ | Total electromagnetic loss | W |
| $P_{out}$ | Mechanical output power | W |
| $\eta$ | Efficiency | % |
| $m$ | Number of phases | — |
| $R_s$ | Stator phase resistance (AC) | Ω |
| $I_{rms}$ | RMS phase current | A |
| $k_h$ | Steinmetz hysteresis coefficient | W/(m³·T^n·Hz) |
| $k_e$ | Steinmetz eddy current coefficient | W/(m³·T²·Hz²) |
| $\omega$ | Angular frequency | rad/s |
| $f$ | Electrical frequency ($\omega / 2\pi$) | Hz |
| $B_{pk}$ | Peak flux density in iron | T |
| $n$ | Steinmetz exponent (typically 1.6–2.0) | — |
| $k_w$ | Windage loss coefficient | — |
| $D$ | Rotor outer diameter | m |
| $P_{mechanical}$ | Bearing and friction loss | W |

---

## Assumptions

### Copper Loss
- DC resistance only (AC skin effect neglected unless specified)
- Uniform current distribution in conductors
- Constant resistance (no temperature correction applied)
- Three-phase balanced system

### Iron Loss
- Steinmetz model: empirical fit, valid for sinusoidal excitation
- Does not capture excess loss or anomalous loss components
- $B_{pk}$ is the peak flux density in the lamination
- Frequency dependence: hysteresis $\propto f$, eddy current $\propto f^2$
- Material-specific coefficients ($k_h$, $k_e$) from datasheet or measurement

### Windage Loss
- Empirical proportionality — coefficient $k_w$ depends on surface roughness, air gap, rotor surface speed
- Significant at high speeds (> 3000 RPM) and large diameters
- Negligible for low-speed, small-diameter machines

---

## Physical Interpretation

### Copper Loss ($P_{cu}$)
- **Dominant at low speeds and high loads**
- Proportional to $I_{rms}^2$ — quadratic with current
- Reduced by: larger conductor cross-section, shorter end windings, lower current density
- AC copper loss (proximity/skin effect) can be 1.5–3× DC loss at high frequencies

### Iron Loss ($P_{fe}$)
- **Dominant at high speeds**
- Two components:
  - **Hysteresis loss**: energy lost per cycle in magnetizing/demagnetizing iron — proportional to frequency
  - **Eddy current loss**: circulating currents in laminations — proportional to frequency²
- Reduced by: thinner laminations, higher-grade electrical steel, lower flux density
- SynRM iron loss is typically **lower** than IPMSM due to no PM flux harmonics

### Windage Loss ($P_w$)
- Air friction on rotor surface
- Proportional to $\omega^3 D^5$ — **extremely sensitive to speed and diameter**
- Significant for high-speed motors (> 10,000 RPM) or large rotors
- Reduced by: surface smoothness, enclosed rotor, smaller diameter

### Efficiency Map
Total losses vary with operating point:
- **Low speed, high torque**: copper loss dominates
- **High speed, low torque**: iron loss and windage dominate
- **Peak efficiency**: typically at 75–100% rated load, moderate speed

---

## Design Relevance

1. **IE5 target**: Requires total losses < 4% at rated point — very tight budget
2. **Copper vs iron tradeoff**: Higher flux density → more torque but more iron loss; lower current → less copper loss but more flux needed
3. **Lamination selection**: 50C250 (0.50 mm) — balance between loss and mechanical strength
4. **Frequency impact**: At 3000 RPM, 4-pole → 100 Hz; iron loss coefficients scale with frequency
5. **Thermal coupling**: Losses generate heat → temperature rise → resistance increases → copper loss increases (feedback loop)
6. **MotorCAD outputs**: `StatorCopperLossAC` and `StatorIronLoss_Total` provide directly comparable loss breakdown

---

## MotorCAD Mapping

| Equation Term | MotorCAD Variable | Notes |
|---------------|-------------------|-------|
| $P_{cu}$ | `StatorCopperLossAC` | AC copper loss (includes skin effect) |
| $P_{fe}$ | `StatorIronLoss_Total` | Total iron loss (hysteresis + eddy) |
| $\eta$ | `Efficiency` | Computed efficiency |
| $P_{out}$ | `ShaftTorque` × speed | Mechanical output |
| $P_{in}$ | `InputPower` | Electrical input |
| $I_{rms}$ | Derived from `PeakCurrent` | Phase current |
| $R_s` | From `Stator Resistance` | Phase resistance |

---

## Loss Budget Example (45 kW SynRM at 3000 RPM)

| Loss Component | Typical % of Pin | Target (W) |
|----------------|-------------------|------------|
| Copper loss | 1.5–2.5% | 750–1250 W |
| Iron loss | 0.8–1.5% | 400–750 W |
| Windage | 0.1–0.3% | 50–150 W |
| Mechanical (bearings) | 0.1–0.2% | 50–100 W |
| **Total loss** | **2.5–4.5%** | **1250–2250 W** |
| **Efficiency** | **95.5–97.5%** | IE5 ≥ 96.0% |

---

## Sources

- Lopez, P. — Loss modeling in SynRM
- Pyrhönen, J. — Electric Machine Design (Steinmetz coefficients, windage)
- Miller, T.J.E. — Electric Machinery Fundamentals
- IEC 60034-2-1 — Efficiency measurement standard
- IEC 60034-30-2 — IE5 efficiency classification

---

## Related Pages

- [[torque-equation]] — Output power from torque × speed
- [[sizing-equation]] — Machine volume limits loss density
- [[synrm-topology]] — SynRM loss characteristics
- [[pmasynrm-topology]] — PMaSynRM loss comparison
- [[power-factor-equation]] — PF affects current and copper loss
- [[inductance-equations]] — Inductance affects current requirements
