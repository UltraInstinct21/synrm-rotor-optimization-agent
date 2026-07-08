---
type: research_paper
title: "Modeling and Simulation of Synchronous Reluctance Motor Using MATLAB/Simulink"
authors:
  - Alkhafaji
  - Uzun
year: 2024
venue: "Journal Article"
doi: ""
motor_types:
  - SynRM
tags:
  - synrm
  - matlab
  - simulink
  - svpwm
  - dq-control
  - current-control
  - simulation
  - power-electronics
topologies:
  - synrm
source_file: ""
related_projects: []
related_experiments: []
equations_added:
  - dq-voltage-equations
  - torque-equation-synrm
concepts_updated:
  - dq-theory
  - svpwm
  - mtpa-control
motorcad_relevance: moderate
confidence: moderate
verification_status: unverified
---

# Modeling and Simulation of Synchronous Reluctance Motor Using MATLAB/Simulink

## Citation

Alkhafaji, Uzun. (2024). Modeling and Simulation of Synchronous Reluctance Motor Using MATLAB/Simulink.

## Why This Paper Matters

This paper provides a complete MATLAB/Simulink model of a SynRM drive system, including Space Vector PWM (SVPWM) generation and d-q axis current control. It serves as a reference for building simulation-based SynRM drive workflows and validates analytical SynRM models against dynamic simulation results.

## Problem Statement

SynRM drives require accurate dynamic models for controller design and performance prediction. This paper addresses the development of a Simulink-based SynRM model with SVPWM inverter and current regulation, enabling virtual prototyping before hardware implementation.

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | Synchronous Reluctance Motor (SynRM) |
| Control method | Field-oriented control (FOC) with d-q axes |
| PWM scheme | Space Vector PWM (SVPWM) |
| Inverter | Three-phase voltage source inverter |
| Operating mode | Speed control with inner current loops |
| Simulation tool | MATLAB/Simulink |

## Method / Theory

### dq-Axis Voltage Equations

The SynRM voltage equations in the synchronous d-q reference frame are:

$$v_d = R_s i_d + \frac{d\lambda_d}{dt} - \omega_e \lambda_q$$

$$v_q = R_s i_q + \frac{d\lambda_q}{dt} + \omega_e \lambda_d$$

Where:
- $v_d, v_q$ — d-axis and q-axis stator voltages (V)
- $i_d, i_q$ — d-axis and q-axis stator currents (A)
- $R_s$ — stator resistance (Ω)
- $\lambda_d, \lambda_q$ — d-axis and q-axis flux linkages (Wb)
- $\omega_e$ — electrical angular velocity (rad/s)

### Flux Linkage Relations

For a SynRM (no permanent magnets):

$$\lambda_d = L_d i_d$$

$$\lambda_q = L_q i_q$$

Where:
- $L_d$ — d-axis inductance (H)
- $L_q$ — q-axis inductance (H)

### Electromagnetic Torque

$$T_e = \frac{3}{2} p (L_d - L_q) i_d i_q$$

Where:
- $T_e$ — electromagnetic torque (Nm)
- $p$ — number of pole pairs
- $L_d - L_q$ — inductance difference (saliency) (H)

### Space Vector PWM

SVPWM computes the inverter switching states to synthesize the reference voltage vector. The algorithm:

1. Determine the sector of the reference voltage vector $\vec{V}_{ref}$
2. Calculate active vector dwell times $T_1$ and $T_2$
3. Determine zero vector dwell times $T_0 = T_s - T_1 - T_2$
4. Generate switching patterns for the three inverter legs

The modulation index is:

$$m = \frac{|\vec{V}_{ref}|}{\frac{2}{3}V_{dc}}$$

Where $V_{dc}$ is the DC bus voltage.

### Current Control Loop

The current controller uses PI regulators in the d-q frame:

$$v_d^* = (K_{p} + \frac{K_{i}}{s})(i_d^* - i_d) - \omega_e L_q i_q$$

$$v_q^* = (K_{p} + \frac{K_{i}}{s})(i_q^* - i_q) + \omega_e L_d i_d$$

Cross-coupling terms are feedforward-compensated for improved dynamic response.

## Key Design Insights

- SynRM torque is proportional to the inductance difference $(L_d - L_q)$ and the product $i_d i_q$
- Maximum torque per ampere (MTPA) occurs when $|i_d| = |i_q|$ for a given current magnitude in a SynRM
- SVPWM provides ~15% higher DC bus utilization compared to sinusoidal PWM
- The d-axis current primarily controls flux, while the q-axis current controls torque
- Current loop bandwidth must be significantly higher than the speed loop for stable FOC

## Simulation Setup

### Model Structure

```
Speed Reference → Speed PI Controller → iq* Reference
                                          ↓
id* Reference → Current PI Controllers → SVPWM → Inverter → SynRM
                                          ↑
                        Current Feedback (abc → dq transform)
```

### Key Simulation Parameters

| Parameter | Typical Value |
|---|---|
| Switching frequency | 10 kHz |
| Current loop bandwidth | ~1 kHz |
| Speed loop bandwidth | ~100 Hz |
| DC bus voltage | 300–600 V |
| Simulation step | 1–10 μs |

## Results

- The Simulink model validates analytical torque calculations
- SVPWM-based drive achieves sinusoidal phase currents with low THD
- Current controllers maintain accurate tracking of $i_d^*$ and $i_q^*$ references
- Dynamic response to speed and torque step changes is well-characterized

## Limitations / Caveats

- Model assumes constant $L_d$ and $L_q$ (no magnetic saturation modeling)
- No core loss or iron loss modeling included
- Temperature effects on winding resistance not considered
- Mechanical load model is simplified
- Parameters are not explicitly provided for a specific motor rating

## Propagation into Wiki

### Concepts to Update
- [[dq-theory]] — add Simulink model description and SVPWM details
- [[svpwm-modulation]] — new page or update if exists
- [[mtpa-control]] — add MTPA condition for SynRM: $|i_d| = |i_q|$

### Equations to Update
- [[torque-equation]] — add dq-frame SynRM torque expression
- [[voltage-equations]] — new page for dq-frame voltage model
- [[inductance-equations]] — add flux linkage relations for SynRM

### Design Guidelines to Update
- [[current-density-limits]] — add controller design considerations

### MotorCAD Pages to Update
- [[motorcad/variables/phase-advance]] — relate current angle to $i_d/i_q$ ratio

## Related Pages

- [[synrm-topology]]
- [[dq-theory]]
- [[mtpa-control]]
- [[torque-equation]]
- [[flux-barriers]]
- [[inductance-equations]]
