---
type: equation
title: D²L Sizing Equation
aliases: [sizing equation, D2L, electromagnetic sizing, machine sizing]
tags: [equations, sizing, design, D2L, electromagnetic-loading]
motor_types: [SynRM, PMaSynRM, IPMSM, SPM, Induction]
topics: [machine-sizing, electromagnetic-loading, preliminary-design]
source_pages: []
related_concepts: [magnetic-loading, electric-loading, synrm-topology]
related_motorcad_variables: [Stator_Lam_Dia, Stator_bore, Rotor_Dia, Stator_Lam_Length]
confidence: high
verification_status: verified
---

# D²L Sizing Equation

## Statement

### Power–Size Relationship

$$P = C_{mec} \cdot D^2 \cdot L \cdot n$$

### Sizing Coefficient

$$C_{mec} = \frac{P}{D^2 \cdot L \cdot n}$$

### Form Factor

$$X \approx \frac{\pi}{4\sqrt{p}}$$

### Air Gap (Pyrhönen empirical)

$$g = \frac{0.18 + 0.006 \cdot P^{0.4}}{1000} \quad \text{(m)}$$

---

## Original Notation

| Source | Notation | Meaning |
|--------|----------|---------|
| Lopez et al. | $P = C_{mec} D^2 L n$ | Standard sizing form |
| Pyrhönen et al. | $g = (0.18 + 0.006P^{0.4})/1000$ | Air gap empirical formula |
| Classic EM theory | $C_{mec} \propto B_{\delta} \cdot A_s$ | Loading product |

---

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $P$ | Output power | W |
| $C_{mec}$ | Electromagnetic sizing coefficient | W/(m³·rpm) |
| $D$ | Rotor diameter | m |
| $L$ | Active stack length | m |
| $n$ | Rotational speed | rpm |
| $X$ | Form factor (depends on pole count) | — |
| $p$ | Number of pole pairs | — |
| $g$ | Air gap length | m |
| $B_{\delta}$ | Air gap flux density | T |
| $A_s$ | Specific electric loading | A/m |

---

## Assumptions

- Continuous duty (S1)
- Sinusoidal flux distribution
- Constant flux density and current density within operating range
- Air gap formula is empirical — valid for medium-sized machines (10–200 kW)
- Form factor approximation holds for pole pairs $p \geq 1$
- No thermal derating applied
- Standard cooling (TEFC or equivalent)

---

## Physical Interpretation

The D²L equation captures a fundamental truth: **machine power is proportional to its active volume** ($D^2 L$) and speed.

- $D^2$ captures the **torque-producing cross-section** (flux × current area)
- $L$ captures the **active length** over which torque is produced
- $n$ captures the **mechanical speed** (power = torque × speed)
- $C_{mec}$ encapsulates the **electromagnetic loading** (flux density × electric loading)

### Sizing Coefficient Components

$$C_{mec} = k_w \cdot B_{\delta} \cdot A_s \cdot \frac{\pi^2}{120}$$

where:
- $k_w$ = winding factor
- $B_{\delta}$ = peak air gap flux density (magnetic loading)
- $A_s$ = specific electric loading (A/m)

### Air Gap Formula

The Pyrhönen empirical air gap:
- Larger machines need proportionally larger air gaps
- Accounts for mechanical tolerances and saturation effects
- The 0.18 mm base accounts for minimum manufacturing clearance
- The $0.006 \cdot P^{0.4}$ term scales with machine size

---

## Design Relevance

1. **Preliminary sizing**: First step in any motor design — establish D and L from power/speed requirements
2. **Tradeoff D vs L**: 
   - Larger D → more torque per unit length, but higher rotor stress and windage
   - Larger L → more torque per unit diameter, but higher axle deflection and thermal challenges
3. **Speed impact**: Higher speed → smaller machine for same power (important for high-speed SynRM)
4. **Cooling limits**: $C_{mec}$ is ultimately limited by thermal constraints (current density, flux density)
5. **Application to SynRM**: SynRM typically has lower $C_{mec}$ than PM motors due to lower flux density and power factor
6. **MotorCAD input**: Stator OD and bore (which determines D) are primary geometry inputs

---

## MotorCAD Mapping

| Equation Term | MotorCAD Variable | Notes |
|---------------|-------------------|-------|
| $D$ (rotor dia) | `Stator_bore` - 2×`Airgap` | Derived from stator bore |
| $L$ (stack length) | `Stator_Lam_Length` | Active iron length |
| $n$ (speed) | `Shaft_Speed_[RPM]` | Operating speed |
| Stator OD | `Stator_Lam_Dia` | Fixed at 340 mm |
| Air gap | `Airgap` | Fixed at 0.5 mm |

---

## Sources

- Lopez, P. — Sizing methodology for SynRM
- Pyrhönen, J. — Electric Machine Design (air gap formula)
- Miller, T.J.E. — Electric Machinery Fundamentals
- Gieras, J.F. — Advancements in Electric Machines

---

## Related Pages

- [[synrm-topology]] — SynRM motor overview
- [[pmasynrm-topology]] — PMaSynRM comparison
- [[torque-equation]] — Torque production fundamentals
- [[loss-equations]] — Loss models limiting sizing coefficient
- [[power-factor-equation]] — PF impact on inverter sizing
