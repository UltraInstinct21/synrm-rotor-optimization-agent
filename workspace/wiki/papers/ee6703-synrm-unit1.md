---
type: textbook_unit
title: "EE6703 — Special Electrical Machines, Unit 1: Synchronous Reluctance Motor"
authors: ["EE6703 Course Material"]
year: "N/A"
venue: "University Textbook / Course Notes"
motor_types: ["SynRM"]
topics: ["construction", "operating principles", "torque equation", "inductance", "power factor", "phasor diagrams", "dq theory"]
tags: [synrm, textbook, construction, operating-principles, torque, inductance, power-factor, dq-theory]
source_file: "raw/textbooks/ee6703_unit1_synrm.pdf"
related_pages: ["[[synrm-topology]]", "[[dq-theory]]", "[[torque-equation]]"]
confidence: high
---

# EE6703 — Synchronous Reluctance Motor (Unit 1)

## Citation

EE6703 Special Electrical Machines, Unit 1: Synchronous Reluctance Motor. University course material.

**Motor type:** Synchronous Reluctance Motor (SynRM)
**Level:** Undergraduate / Postgraduate coursework
**Scope:** Fundamentals of SynRM construction, theory, and performance

---

## Overview

The Synchronous Reluctance Motor (SynRM) produces torque through the **reluctance variation** between the d-axis and q-axis rotor paths. Unlike PM motors, it requires no permanent magnets, making it cost-effective and suitable for high-temperature environments. This unit covers the foundational theory.

---

## Construction

### Stator

The SynRM stator is identical to an induction motor stator:

| Component | Description |
|---|---|
| Laminated core | Silicon steel laminations to reduce eddy currents |
| Distributed winding | Three-phase, sinusoidally distributed |
| Slot count | Typically 24, 36, or 48 slots |
| Winding type | Concentrated or distributed (distributed preferred for sinusoidal MMF) |
| Material | Silicon steel (M19, M27, 50C250, etc.) |

### Rotor

The rotor is the distinguishing feature of the SynRM:

| Component | Description |
|---|---|
| Laminated core | Silicon steel, no windings or magnets |
| Flux barriers | Air gaps or non-magnetic material inserted to create reluctance variation |
| Rotor type | Interior (most common), surface, or transverse |
| Barrier geometry | U-shape, step, or multi-layer |
| Pole count | 2, 4, 6, or more (4-pole most common for industrial) |

### Airgap

| Parameter | Typical Range |
|---|---|
| Mechanical airgap | 0.3–1.0 mm |
| Effect on performance | Smaller airgap → higher L_d, better torque, but tighter manufacturing tolerance |

---

## Operating Principle

### Reluctance Torque

The SynRM produces torque because the rotor has **different reluctances** along the d-axis and q-axis:

- **d-axis** — path of minimum reluctance (flux flows through iron and barriers easily)
- **q-axis** — path of maximum reluctance (flux must cross barriers, high reluctance)

When a stator MMF is applied, the rotor aligns to minimize the total reluctance of the magnetic circuit. This alignment produces **reluctance torque**:

$$T = \frac{1}{2} \cdot i^2 \cdot \frac{dL}{d\theta}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| T | Reluctance torque | Nm |
| i | Stator current | A |
| dL/dθ | Rate of change of inductance with rotor angle | H/rad |

### dq-Axis Model

The SynRM is modeled in the d-q reference frame:

$$v_d = R_s \cdot i_d + \frac{d\lambda_d}{dt} - \omega_e \cdot \lambda_q$$

$$v_q = R_s \cdot i_q + \frac{d\lambda_q}{dt} + \omega_e \cdot \lambda_d$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| v_d, v_q | d-axis and q-axis voltages | V |
| i_d, i_q | d-axis and q-axis currents | A |
| λ_d, λ_q | d-axis and q-axis flux linkages | Wb |
| R_s | Stator resistance | Ω |
| ω_e | Electrical angular velocity | rad/s |

Flux linkages:

$$\lambda_d = L_d \cdot i_d$$

$$\lambda_q = L_q \cdot i_q$$

Where L_d and L_q are the d-axis and q-axis inductances.

---

## Key Equations

### Torque Equation

$$T = \frac{3}{2} \cdot p \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| T | Electromagnetic torque | Nm |
| p | Number of pole pairs | — |
| L_d | d-axis inductance | H |
| L_q | q-axis inductance | H |
| i_d | d-axis current | A |
| i_q | q-axis current | A |

**Key insight:** Torque is proportional to (L_d - L_q), which is the **inductance difference** or **saliency**. Higher saliency → higher torque per ampere.

### Saliency Ratio

$$\xi = \frac{L_d}{L_q}$$

Typical values:
| Application | Typical ξ |
|---|---|
| Basic SynRM | 2–4 |
| Optimized SynRM | 4–8 |
| High-performance SynRM | 8–12 |
| PMaSynRM (with magnets) | 5–15 |

### Power Factor

$$PF = \cos(\phi) = \frac{P}{S} = \frac{T \cdot \omega_m}{\sqrt{3} \cdot V_{LL} \cdot I_L}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| PF | Power factor | — |
| φ | Angle between voltage and current | rad |
| P | Active power | W |
| S | Apparent power | VA |
| T | Torque | Nm |
| ω_m | Mechanical angular velocity | rad/s |
| V_LL | Line-line voltage | V |
| I_L | Line current | A |

**SynRM power factor limitation:** The SynRM inherently has a lower power factor than PM motors because the magnetizing current is entirely supplied by the stator. Typical PF ranges from 0.5–0.85 depending on design.

### Power Factor from dq Currents

$$PF = \cos\left(\arctan\left(\frac{v_q \cdot i_q + v_d \cdot i_d}{v_d \cdot i_q - v_q \cdot i_d}\right)\right)$$

Or more practically, for maximum torque per ampere (MTPA) operation:

$$PF = \frac{L_d \cdot i_d^2 + L_q \cdot i_q^2}{\sqrt{(L_d \cdot i_d)^2 + (L_q \cdot i_q)^2} \cdot \sqrt{i_d^2 + i_q^2}}$$

### Inductance Definitions

**d-axis inductance:**

$$L_d = \frac{\lambda_d}{i_d} = \frac{N^2 \cdot k_w^2}{R_d}$$

**q-axis inductance:**

$$L_q = \frac{\lambda_q}{i_q} = \frac{N^2 \cdot k_w^2}{R_q}$$

Where R_d and R_q are the total reluctances along each axis.

### Torque Angle

The torque angle δ is defined as the angle between the rotor d-axis and the stator MMF vector:

$$T = \frac{3 \cdot p \cdot V^2}{2 \cdot \omega_e} \cdot \left(\frac{1}{X_q} - \frac{1}{X_d}\right) \cdot \sin(2\delta)$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| δ | Torque angle (between MMF and rotor d-axis) | rad |
| X_d, X_q | d-axis and q-axis reactances | Ω |

Maximum torque occurs at δ = 45° (electrical).

---

## Phasor Diagram

### Steady-State Phasor Relationship

For a SynRM with no PM flux:

$$\vec{V} = R_s \cdot \vec{I} + jX_d \cdot \vec{I_d} + jX_q \cdot \vec{I_q}$$

Where:
- **V** = terminal voltage
- **I** = stator current
- **I_d** = d-axis current component
- **I_q** = q-axis current component

### Current Angle for MTPA

For maximum torque per ampere, the optimal current angle γ (angle between current and d-axis) is:

$$\gamma_{MTPA} = \arctan\left(\sqrt{\frac{L_d}{L_q}}\right) = \arctan(\sqrt{\xi})$$

For ξ = 4: γ_MTPA ≈ 63.4°
For ξ = 9: γ_MTPA ≈ 71.6°

---

## Losses in SynRM

| Loss Type | Source | Typical % of Rated Power |
|---|---|---|
| Stator copper loss | I²R in stator windings | 3–8% |
| Stator iron loss | Eddy current + hysteresis in stator laminations | 2–5% |
| Rotor iron loss | Eddy currents in rotor (smaller than stator) | 0.5–2% |
| Mechanical loss | Bearing friction, windage | 0.5–2% |
| Stray load loss | Harmonics, leakage flux | 0.5–1% |

**Efficiency:**

$$\eta = \frac{P_{out}}{P_{out} + P_{copper} + P_{iron} + P_{mech} + P_{stray}} \times 100\%$$

---

## Advantages and Disadvantages

### Advantages
- No permanent magnets → lower cost, no demagnetization risk
- Robust rotor construction → suitable for high speed
- Good thermal performance → no magnet temperature limitations
- Simple manufacturing → standard lamination stamping
- Wide speed range → field weakening is natural

### Disadvantages
- Lower power factor than PM motors → requires larger inverter
- Lower torque density than PM motors
- Torque ripple can be significant → requires careful barrier design
- Power factor degrades at light load
- Requires rotor position sensor for vector control

---

## Comparison with Other Motor Types

| Parameter | SynRM | IPMSM | Induction Motor |
|---|---|---|---|
| Torque density | Moderate | High | Moderate |
| Power factor | 0.5–0.85 | 0.8–0.95 | 0.8–0.9 |
| Efficiency | 90–96% | 92–98% | 85–95% |
| Cost | Low | High (magnets) | Low |
| Speed range | Wide | Wide | Moderate |
| Rotor robustness | Excellent | Good | Good |
| Thermal limit | Stator only | Stator + magnets | Stator + rotor |

---

## Propagation into Wiki

### Concepts to update
- [[synrm-topology]] — add construction and operating principle details
- [[dq-theory]] — add SynRM-specific dq model
- [[power-factor]] — add SynRM power factor characteristics

### Equations to update
- [[torque-equation]] — add reluctance torque derivation
- [[inductance-equations]] — add L_d and L_q definitions from reluctance
- [[saliency-ratio]] — add saliency definition and typical ranges

### Design guidelines to update
- [[current-density-limits]] — add SynRM current density considerations
- [[airgap-selection]] — add airgap effect on L_d

---

## Related Pages

- [[synrm-topology]] — Synchronous Reluctance Motor overview
- [[dq-theory]] — d-q reference frame theory
- [[torque-equation]] — torque production equations
- [[inductance-equations]] — inductance definitions and calculations
- [[saliency-ratio]] — saliency ratio and its optimization
- [[power-factor]] — power factor in electric motors
- [[flux-barriers]] — flux barrier design for SynRM rotors
