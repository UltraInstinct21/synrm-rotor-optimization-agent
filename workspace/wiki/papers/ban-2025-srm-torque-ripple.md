---
type: research_paper
title: "Torque Ripple Reduction in Synchronous Reluctance Motors Using Skewing and Asymmetric Pole Techniques"
authors:
  - Ban et al.
year: 2025
venue: "2025"
motor_types:
  - SynRM
  - SRM
tags:
  - torque-ripple
  - skewing
  - asymmetric-poles
  - power-take-off
  - vibration
  - noise
source_file: "raw/papers/ban-2025-srm-torque-ripple.pdf"
---

# Torque Ripple Reduction in Synchronous Reluctance Motors Using Skewing and Asymmetric Pole Techniques

## Citation

Ban et al., "Torque Ripple Reduction in Synchronous Reluctance Motors Using Skewing and Asymmetric Pole Techniques," 2025.

---

## Why This Paper Matters

Torque ripple is one of the most critical performance limitations of SynRM, directly causing vibration, noise, and speed oscillation in drive systems. This paper addresses torque ripple reduction through two practical techniques: **continuous/step skewing** and **asymmetric pole design**. These methods are particularly relevant for EV powertrain applications where NVH (noise, vibration, harshness) requirements are stringent.

---

## Problem Statement

SynRM torque ripple originates from:
1. **Stator slotting harmonics**: Interaction between rotor flux and stator slot openings
2. **Rotor barrier harmonics**: Flux distribution discontinuities at barrier edges
3. **Saturation harmonics**: Localized saturation near bridges creates flux distortions
4. **MMF harmonics**: Winding distribution harmonics

Typical SynRM torque ripple: 8–15% (peak-to-peak / average). EV applications typically require <5%.

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | SynRM / SRM (comparative study) |
| Focus | Torque ripple reduction techniques |
| Application | Power take-off (PTO) and EV traction |
| Operating condition | Rated torque, rated speed |

---

## Method / Theory

### Torque Ripple Definition

$$TR = \frac{T_{max} - T_{min}}{T_{avg}} \times 100\%$$

where:
- $T_{max}$ = maximum torque over one electrical cycle
- $T_{min}$ = minimum torque over one electrical cycle
- $T_{avg}$ = average torque

### Torque Harmonic Analysis

The instantaneous torque can be decomposed into Fourier components:

$$T(\theta) = T_0 + \sum_{n=1}^{\infty} T_n \sin(n p \theta + \phi_n)$$

where:
- $T_0$ = average (DC) torque
- $T_n$ = amplitude of $n$-th torque harmonic
- $p$ = pole pair number
- $\phi_n$ = phase angle of $n$-th harmonic

The dominant ripple harmonics in SynRM are typically at $6p$ and $12p$ electrical frequency (for 3-phase machines).

### Continuous Skewing

Skewing distributes the torque along the axial length with a progressive angular shift:

$$T_{skewed} = \frac{1}{L_{stk}} \int_0^{L_{stk}} T(\theta + \alpha(z)) \, dz$$

For continuous skewing with skew angle $\alpha_s$:

$$\alpha(z) = \frac{\alpha_s}{L_{stk}} \cdot z$$

The effect on the $n$-th torque harmonic:

$$T_{n,skewed} = T_n \cdot \frac{\sin(n p \alpha_s / 2)}{n p \alpha_s / 2}$$

**Key result**: A skew angle equal to one stator slot pitch ($\alpha_s = 2\pi / Q_s$ where $Q_s$ = slot number) eliminates the slotting harmonic.

For 48-slot, 4-pole motor: $\alpha_s = 360° / 48 = 7.5°$ mechanical = 15° electrical.

### Step Skewing (Discrete Skew)

Step skewing divides the rotor into $N_s$ steps, each offset by $\Delta\alpha = \alpha_s / N_s$:

$$T_{step} = \frac{1}{N_s} \sum_{k=1}^{N_s} T\left(\theta + (k-1) \Delta\alpha\right)$$

The reduction of the $n$-th harmonic:

$$T_{n,step} = T_n \cdot \frac{\sin(n p \alpha_s / 2)}{N_s \sin(n p \alpha_s / (2 N_s))}$$

**Practical note**: 2–3 step skew is often sufficient for significant ripple reduction. More steps give diminishing returns.

### Asymmetric Pole Design

Asymmetric pole design uses different barrier geometry for adjacent poles within one electrical cycle:

$$\text{Pole}_1: \text{geometry}_A, \quad \text{Pole}_2: \text{geometry}_B$$

The torque ripple from each pole pair has different harmonic content, and the superposition partially cancels the dominant harmonics.

For a 4-pole motor with 2 asymmetric pole pairs:

$$T_{asym} = \frac{1}{2}\left[T_A(\theta) + T_B(\theta + \pi/p)\right]$$

If the dominant ripple harmonic of pole A is out of phase with pole B, cancellation occurs.

### Combined Skew + Asymmetric

The paper proposes combining both techniques:

$$T_{combined} = \frac{1}{N_s} \sum_{k=1}^{N_s} \frac{1}{2}\left[T_A(\theta_k) + T_B(\theta_k + \Delta\phi)\right]$$

where $\theta_k = \theta + (k-1)\Delta\alpha$ and $\Delta\phi$ is the angular offset between asymmetric poles.

---

## Results

### Continuous Skewing

| Skew Angle | Ripple Reduction | Torque Reduction |
|---|---|---|
| 5° mech | ~40% | ~3% |
| 7.5° mech (1 slot pitch) | ~70% | ~5% |
| 10° mech | ~80% | ~8% |

### Step Skewing (2-step)

| Step Angle | Ripple Reduction | Torque Reduction |
|---|---|---|
| 3.75° mech | ~55% | ~2% |
| 5° mech | ~65% | ~3% |
| 7.5° mech | ~75% | ~5% |

### Asymmetric Poles

| Configuration | Ripple Reduction | Torque Reduction |
|---|---|---|
| 2 asymmetric poles | ~30% | ~1% |
| 4 asymmetric poles | ~50% | ~2% |

### Combined (2-step skew + 2 asymmetric poles)

| Configuration | Ripple Reduction | Torque Reduction |
|---|---|---|
| Combined | ~85% | ~5% |

**Key finding**: Combining step skewing with asymmetric poles achieves >80% ripple reduction with <5% average torque loss.

---

## Design Insights

1. **Skew angle = 1 slot pitch is near-optimal**: It targets the dominant slotting harmonic while minimizing torque loss.
2. **Step skew is practical**: 2-step skew captures most of the benefit with simple manufacturing (two rotor segments).
3. **Asymmetric poles complement skewing**: They target different harmonic content, so the combination is synergistic.
4. **Torque reduction is the tradeoff**: Skewing always reduces average torque; the loss is proportional to $(n p \alpha_s / 2)^2$ for small angles.
5. **Manufacturing consideration**: Continuous skew requires skewed rotor lamination stamps; step skew uses straight stamps rotated during assembly.

---

## Limitations / Caveats

- Study assumes ideal current supply; inverter harmonics may interact with skew effects
- Mechanical balance of asymmetric rotors requires careful mass distribution analysis
- Skewing increases axial flux variation, which can affect sensorless control
- Step skew creates axial torque variation within each step, affecting local bearing loads
- Results are simulation-based; experimental validation recommended for production designs

---

## Propagation into Wiki

### Concepts to Update
- [[torque-ripple]] — comprehensive ripple reduction methods
- [[synrm-topology]] — ripple characteristics by topology

### Equations to Update
- [[torque-ripple-eq]] — TR definition and harmonic decomposition
- [[skewing-effect]] — continuous and step skew harmonic reduction

### Design Guidelines to Update
- [[torque-ripple-reduction]] — skew and asymmetric design rules
- [[manufacturing]] — skew implementation methods

### MotorCAD Pages to Update
- [[motorcad-outputs]] — torque ripple output interpretation
- [[motorcad-workflows]] — skew modeling in MotorCAD

---

## Related Pages

- [[torque-ripple]]
- [[synrm-topology]]
- [[flux-barriers]]
- [[dq-theory]]
- [[motorcad-outputs]]
- [[vibration]]
- [[noise]]
