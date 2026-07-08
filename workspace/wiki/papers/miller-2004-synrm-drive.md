---
type: research_paper
title: "High-Efficiency Synchronous Reluctance Motor Drive: Comparison with SRM, IM, and BLDC"
authors:
  - Miller et al.
year: 2004
venue: "IEEE Transactions on Industry Applications"
motor_types:
  - SynRM
  - SRM
  - IM
  - BLDC
tags:
  - segmental-rotor
  - drive-comparison
  - efficiency
  - torque-density
  - industrial-drive
  - ieee
source_file: "raw/papers/miller-2004-synrm-drive.pdf"
---

# High-Efficiency Synchronous Reluctance Motor Drive: Comparison with SRM, IM, and BLDC

## Citation

Miller et al., "High-Efficiency Synchronous Reluctance Motor Drive," *IEEE Transactions on Industry Applications*, 2004.

---

## Why This Paper Matters

This is a foundational paper by **T.J.E. Miller**, one of the most influential researchers in reluctance motor design. It provides a rigorous **head-to-head comparison** of SynRM against SRM, induction motor (IM), and BLDC across efficiency, torque density, power factor, and drive requirements. The paper demonstrates that SynRM, particularly with **segmental rotor construction**, can be competitive with established motor types for industrial drive applications.

---

## Problem Statement

At the time of this paper (2004), SynRM was not widely adopted despite theoretical advantages. The paper seeks to answer:
1. Can SynRM match or exceed IM efficiency?
2. Can SynRM compete with BLDC in torque density?
3. How does SynRM compare to SRM (another reluctance-based motor)?
4. What are the practical drive requirements for each motor type?

---

## Machine / Study Context

| Parameter | SynRM | SRM | IM | BLDC |
|---|---|---|---|---|
| Rotor type | Segmental / barrier | Salient pole | Squirrel cage | Permanent magnet |
| Magnets | None | None | None | NdFeB |
| Rotor copper loss | None | None | Yes | None |
| Stator copper loss | Yes | Yes | Yes | Yes |
| Iron loss | Yes | Yes | Yes | Yes |
| Drive type | 3-phase inverter | Asymmetric half-bridge | VFD | 6-step or PWM |

---

## Method / Theory

### SynRM Torque

$$T_{SynRM} = \frac{3}{2} p (L_d - L_q) i_d i_q$$

### SRM Torque

$$T_{SRM} = \frac{1}{2} i^2 \frac{dL}{d\theta}$$

SRM torque depends on the rate of change of inductance with rotor position. It is inherently pulsating because torque is produced only during inductance rise.

### IM Torque

$$T_{IM} = \frac{3}{2} p \frac{R_r}{s \omega_s} \frac{\psi_m^2}{(R_r/s)^2 + (X_r)^2}$$

IM torque depends on rotor resistance $R_r$ and slip $s$. Rotor copper loss is proportional to slip, limiting efficiency.

### BLDC Torque

$$T_{BLDC} = \frac{3}{2} p \psi_m i$$

BLDC torque is proportional to magnet flux and current. High torque density but requires rare-earth magnets.

### Efficiency Comparison

Efficiency for each motor:

$$\eta = \frac{P_{out}}{P_{out} + P_{loss}}$$

Loss breakdown:

| Loss Component | SynRM | SRM | IM | BLDC |
|---|---|---|---|---|
| Stator copper | Yes | Yes | Yes | Yes |
| Rotor copper | **No** | **No** | **Yes** | **No** |
| Iron (stator) | Yes | Yes | Yes | Yes |
| Iron (rotor) | Low | Low | Moderate | Low |
| Magnet (eddy current) | N/A | N/A | N/A | Small |
| Mechanical | Yes | Yes | Yes | Yes |

The absence of rotor copper loss is a key efficiency advantage for SynRM, SRM, and BLDC over IM.

---

## Segmental Rotor SynRM

### Concept

Instead of continuous laminations with flux barriers, the **segmental rotor** uses separate iron segments insulated from each other:

- Each segment is a piece of electrical steel
- Segments are held in place by a non-magnetic sleeve or epoxy
- Flux paths are forced through specific routes by the segment geometry
- **No bridges required** → no leakage flux → higher saliency

### Advantages

| Feature | Barrier Rotor | Segmental Rotor |
|---|---|---|
| Saliency ratio | 3–5 | 6–10 |
| Leakage flux (bridges) | Significant | Eliminated |
| Manufacturing | Stamping | Assembly of segments |
| Mechanical integrity | Excellent (continuous) | Moderate (segments + binder) |
| High-speed capability | Good | Limited (centrifugal on segments) |

### Results

| Metric | Segmental SynRM | Barrier SynRM |
|---|---|---|
| Saliency ratio | 7–9 | 3–5 |
| Efficiency @ rated | 96.5% | 95.5% |
| Power factor | 0.75–0.80 | 0.80–0.85 |
| Torque density | High | Moderate |

---

## Comparative Results

### Efficiency

| Motor Type | Efficiency @ Rated | Efficiency @ 50% Load |
|---|---|---|
| Segmental SynRM | 96.5% | 95.0% |
| Barrier SynRM | 95.5% | 94.0% |
| SRM | 95.0% | 93.5% |
| IM (IE3) | 94.5% | 92.0% |
| BLDC | 96.0% | 94.5% |

**Key finding**: SynRM matches or exceeds IM efficiency across the load range, and is competitive with BLDC.

### Torque Density

| Motor Type | Relative Torque Density |
|---|---|
| BLDC | 1.00 (reference) |
| Segmental SynRM | 0.85–0.90 |
| SRM | 0.80–0.85 |
| Barrier SynRM | 0.75–0.80 |
| IM | 0.70–0.75 |

### Power Factor

| Motor Type | Power Factor |
|---|---|
| IM | 0.85–0.90 |
| BLDC | 0.90–0.95 |
| Barrier SynRM | 0.80–0.85 |
| SRM | 0.65–0.75 |
| Segmental SynRM | 0.75–0.80 |

**Key finding**: SynRM power factor is lower than IM and BLDC but can be improved with proper design (see [[suli-2025-synrm-pmasynrm-common-stator]] and [[bao-xia-2025-pmasynrm-ferrite]]).

### Drive Requirements

| Motor Type | Drive Complexity | Inverter Rating |
|---|---|---|
| SynRM | 3-phase, sensorless capable (saliency) | Standard |
| SRM | Asymmetric half-bridge (special) | Higher device count |
| IM | 3-phase VFD (standard) | Standard |
| BLDC | 6-step or 3-phase (simple) | Standard |

**SRM disadvantage**: Requires asymmetric half-bridge with one switch per phase, increasing component count and cost.

---

## Key Design Insights

1. **SynRM efficiency exceeds IE3 IM**: Rotor copper loss elimination is the primary driver.
2. **Segmental rotor offers highest saliency**: But manufacturing complexity limits practical adoption.
3. **SRM is simpler but less smooth**: Torque ripple and acoustic noise are worse than SynRM.
4. **BLDC has highest torque density**: But requires rare-earth magnets.
5. **SynRM is the best rare-earth-free option**: Among motors without permanent magnets, SynRM offers the best combination of efficiency and torque density.
6. **Power factor is SynRM's weakness**: Can be addressed with PM assistance (→ PMaSynRM).

---

## Limitations / Caveats

- Study is from 2004; modern lamination materials and manufacturing have improved all motor types
- IM efficiency has improved (IE4, IE5 motors now available)
- BLDC costs have decreased with magnet price fluctuations
- Segmental rotor manufacturing has not scaled to high-volume production
- Drive cost and complexity not fully quantified in monetary terms
- Only steady-state performance compared; dynamic response not analyzed

---

## Propagation into Wiki

### Concepts to Update
- [[synrm-topology]] — segmental rotor variant, comparison with other topologies
- [[srm-topology]] — torque production comparison
- [[im-topology]] — efficiency comparison
- [[bldc-topology]] — torque density comparison

### Equations to Update
- [[torque]] — SynRM, SRM, IM, BLDC torque equations
- [[efficiency]] — loss breakdown comparison

### Design Guidelines to Update
- [[motor-type-selection]] — comparison framework for motor type selection
- [[synrm-vs-im]] — efficiency and PF tradeoffs
- [[synrm-vs-pm]] — rare-earth-free vs. PM performance

### Topology Pages to Update
- [[synrm-topology]] — add segmental rotor description
- [[srm-topology]] — add comparison with SynRM

---

## Related Pages

- [[synrm-topology]]
- [[dq-theory]]
- [[srm-topology]]
- [[im-topology]]
- [[bldc-topology]]
- [[saliency-ratio]]
- [[power-factor]]
- [[efficiency]]
- [[flux-barriers]]
- [[segmental-rotor]]
