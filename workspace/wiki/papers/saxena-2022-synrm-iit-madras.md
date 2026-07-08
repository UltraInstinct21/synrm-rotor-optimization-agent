---
type: research_paper
title: "Design and Simulation of Synchronous Reluctance Motor with MTPA Control Strategy"
authors:
  - Sushant Saxena
  - Dr. Kamalesh Hatua (Supervisor)
year: 2022
venue: "M.Tech Project Report, IIT Madras"
motor_types:
  - SynRM
tags:
  - synrm
  - mtpa-control
  - dq-theory
  - power-factor
  - torque-optimization
  - fEA
  - hardware-implementation
  - saturation
source_file: saxena-2022-synrm-iit-madras.pdf
related_pages:
  - [[synrm-topology]]
  - [[dq-theory]]
  - [[mtpa-control]]
  - [[torque-equation]]
  - [[power-factor-equation]]
---

# Design and Simulation of SynRM with MTPA Control Strategy

## Citation

Sushant Saxena, "Design and Simulation of Synchronous Reluctance Motor with MTPA Control Strategy," M.Tech Project Report, Supervisor: Dr. Kamalesh Hatua, Indian Institute of Technology Madras, 2022.

---

## Problem Statement

This project investigates the design, simulation, and control of a Synchronous Reluctance Motor (SynRM) with focus on Maximum Torque Per Ampere (MTPA) control strategy. The study addresses torque optimization through current angle ($\beta$) control, explores the effects of magnetic saturation and cross-coupling on torque production, and validates the design with experimental hardware.

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor Type | SynRM |
| Rated Power | 22 kW |
| Phases | 3 |
| Connection | Delta |
| Pole Count | 4 |
| Rated Speed | 1500 RPM |
| Frequency | 50 Hz |
| Stator Resistance ($R_s$) | 0.2 Ω |
| d-axis Inductance ($L_d$) | 48.18 mH |
| q-axis Inductance ($L_q$) | 11.88 mH |
| Moment of Inertia ($J$) | 0.5 kg·m² |

### Derived Parameters

| Parameter | Value |
|---|---|
| Saliency Ratio ($\zeta = L_d/L_q$) | 4.06 |
| Inductance Difference ($L_d - L_q$) | 36.30 mH |

---

## Key Equations

### d-axis Flux Linkage

$$\psi_d = L_d \cdot i_d$$

### q-axis Flux Linkage

$$\psi_q = L_q \cdot i_q$$

### Electromagnetic Torque

$$T_e = \frac{3}{2} \cdot \frac{P}{2} \cdot (L_d - L_q) \cdot i_q \cdot i_d$$

Where:
- $T_e$ — electromagnetic torque [Nm]
- $P$ — pole pair number (= 2 for 4-pole)
- $L_d, L_q$ — d-axis and q-axis inductances [H]
- $i_d, i_q$ — d-axis and q-axis currents [A]

### Normalized Torque Expression

$$\tau_n = i_n^2 \cdot \sin(2\beta)$$

Where:
- $\tau_n$ — normalized torque
- $i_n$ — normalized current magnitude
- $\beta$ — current advance angle (electrical) [degrees]

The $\sin(2\beta)$ dependence shows that maximum torque in the linear (unsaturated) case occurs at $\beta = 45°$, where $\sin(2\beta) = 1$.

### Current Components

$$i_d = I_s \cdot \cos(\beta)$$
$$i_q = I_s \cdot \sin(\beta)$$

Where:
- $I_s$ — stator current magnitude [A]
- $\beta$ — current advance angle [degrees]

### MTPA Condition (Linear Model)

For the linear (unsaturated) model, the MTPA angle is:

$$\beta_{MTPA} = 45°$$

This gives:

$$i_d = i_q = \frac{I_s}{\sqrt{2}}$$

### Power Factor (Maximum)

$$PF_{max} = \frac{\zeta - 1}{\zeta + 1}$$

Where:
- $\zeta = L_d / L_q$ — saliency ratio

For this motor:
$$PF_{max} = \frac{4.06 - 1}{4.06 + 1} = \frac{3.06}{5.06} = 0.605$$

---

## MTPA Control Strategy

### Theoretical Basis

The MTPA strategy maximizes torque for a given stator current magnitude. In the linear model, this occurs at $\beta = 45°$ because the torque equation contains the $\sin(2\beta)$ term.

### Current Angle $\beta$ Optimization

The paper investigates the effect of varying $\beta$ from 45° to 90°:

| $\beta$ (deg) | Effect on Torque |
|---|---|
| 45° | Maximum in linear model ($\sin(90°) = 1$) |
| 45°–65° | Torque increases due to saturation effects |
| 65° | Optimum including saturation (17% improvement over 45°) |
| >65° | Torque decreases as $\sin(2\beta)$ term dominates |
| 90° | Zero torque ($\sin(180°) = 0$) |

### FEA Finding: Optimal Angle Shift

FEA simulation reveals that the optimal current angle shifts from 45° to approximately 65° due to magnetic saturation. This results in a **17% torque increase** compared to the linear MTPA prediction at 45°.

---

## Magnetic Saturation Effects

### Linear vs. Saturated Model

In the linear model, $L_d$ and $L_q$ are constant. In practice, both inductances decrease with increasing current due to iron saturation.

### Cross-Coupling Saturation

The study identifies cross-coupling saturation as a significant effect:
- d-axis flux path affects q-axis inductance and vice versa
- Cross-coupling adds approximately **17% more torque** beyond what the uncoupled model predicts
- This effect is particularly pronounced at high current densities

### Saturation Impact on MTPA

Saturation changes the optimal current angle:
- Linear model: $\beta_{MTPA} = 45°$
- Saturated model (FEA): $\beta_{MTPA} \approx 65°$
- The shift occurs because saturation reduces $L_d$ faster than $L_q$ at high currents, changing the torque-current relationship

---

## Simulation Results

### Torque vs. Current Angle

FEA simulations demonstrate:
1. At $\beta = 45°$ (linear MTPA): baseline torque
2. At $\beta = 65°$ (optimal with saturation): 17% higher torque
3. The improvement is attributed to better utilization of the saturated flux paths

### Inductance Variation

Both $L_d$ and $L_q$ vary with current:
- $L_d$ decreases significantly at high current (d-axis saturation)
- $L_q$ decreases less (q-axis has more iron path)
- The ratio $L_d/L_q$ changes with operating point

---

## Hardware Implementation

### Power Electronics

| Component | Specification |
|---|---|
| Inverter | IGBT-based |
| IGBT Module | SKM200GB12E4 |
| Voltage Rating | 1200 V |
| Current Rating | 200 A |

### Control Platform

| Component | Specification |
|---|---|
| DSP | TMS320F28335 |
| Manufacturer | Texas Instruments |
| Features | Floating-point, 150 MHz, PWM channels, ADC |

### Control Implementation
- Field-Oriented Control (FOC) implemented on DSP
- Current angle $\beta$ control for MTPA
- Speed and current control loops
- Sensorless or encoder-based rotor position feedback

---

## Design Insights

1. **Saturation Improves Torque**: Contrary to intuition, saturation can increase torque if the current angle is optimized. The 17% improvement at $\beta = 65°$ is significant.
2. **Cross-Coupling Matters**: Cross-coupling between d and q axes adds ~17% more torque. Ignoring cross-coupling leads to underestimation of motor capability.
3. **MTPA Angle Shift**: The optimal current angle shifts from 45° to 65° in practice. Control systems must account for this.
4. **Power Factor Limitation**: With $\zeta = 4.06$, the maximum achievable PF is ~0.605. Higher saliency ratios are needed for better PF.
5. **Hardware Validation**: The project demonstrates practical feasibility of SynRM drive systems with standard industrial components.

---

## Limitations

- Study limited to one motor geometry (22 kW, 4-pole)
- FEA simulations assume ideal conditions (no manufacturing tolerances)
- Thermal effects on inductance not fully characterized
- Experimental results limited to specific operating points
- Power factor of 0.605 is below typical industrial requirements (>0.85)

---

## Propagation into Wiki

### Concepts to Update
- [[synrm-topology]] — add MTPA control context
- [[dq-theory]] — add SynRM-specific d-q model
- [[mtpa-control]] — create if not exists; add SynRM MTPA derivation
- [[saturation-effects]] — create if not exists; add cross-coupling saturation

### Equations to Update
- [[torque-equation]] — add normalized form and MTPA derivation
- [[power-factor-equation]] — add saliency ratio relationship
- [[inductance-model]] — create if not exists; add saturation effects

### Design Guidelines to Update
- [[current-angle-selection]] — create if not exists; add MTPA optimization
- [[power-factor-improvement]] — add saliency ratio requirements

### MotorCAD Pages to Update
- [[motorcad/variables/inductance]] — note saturation behavior
- [[motorcad/workflows/mtpa-analysis]] — create if not exists

---

## Related Pages

- [[synrm-topology]]
- [[dq-theory]]
- [[mtpa-control]]
- [[torque-equation]]
- [[power-factor-equation]]
- [[saturation-effects]]
- [[inductance-model]]
