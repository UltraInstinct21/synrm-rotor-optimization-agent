---
type: research_paper
title: "EE6703 SEM Unit 1 — Synchronous Reluctance Motors"
authors: "Unknown (university course material)"
year: ""
venue: "EE6703 — Semester Course Unit (university lecture notes)"
doi: ""
motor_types: ["Synchronous Reluctance Motor", "Vernier Motor"]
topics:
  - "Construction and classification of SyRM"
  - "Torque derivation (salient-pole and reluctance-only)"
  - "d-q axis modeling"
  - "Phasor diagrams"
  - "Axial vs radial rotor topologies"
  - "Vernier motor principle"
  - "Performance characteristics"
topologies: ["Cage rotor", "Cageless rotor", "Axially laminated", "Radially laminated (flux barrier)", "Vernier"]
source_files: ["raw/papers/EE6703 SEM UNIT 1 - SYNCHRONOUS RELUCTANCE MOTORS.md"]
related_projects: []
related_experiments: []
equations_added:
  - "General torque equation (salient-pole synchronous machine)"
  - "SyRM reluctance torque equation"
  - "Voltage equation for SyRM"
  - "Stator flux linkage definition"
  - "Input power equation"
  - "Open-circuit air gap flux"
  - "Fundamental flux per pole (Fourier)"
  - "General torque equation (d-q frame)"
  - "Air gap permeance"
  - "Magnet potential difference"
concepts_updated: ["Reluctance torque", "Saliency ratio", "d-q axis modeling", "Vernier magnetic gearing"]
motorcad_relevance: "Core theory for [[SynRM]] rotor design — saliency ratio, flux barriers, torque angle limits directly inform [[motorcad_experiments]] setup"
confidence: Verified
---

# EE6703 SEM Unit 1 — Synchronous Reluctance Motors

## Citation

University course material: EE6703 Semester Course, Unit 1 — Synchronous Reluctance Motors. No formal authors, DOI, or journal listed. This is an instructional summary covering construction, torque theory, phasor diagrams, rotor topologies, and the Vernier motor.

## Why This Paper Matters

This is the foundational theory reference for [[SynRM]] design. It provides the complete torque derivation chain from [[salient_pole_synchronous_machine]] through to the reluctance-only torque equation that governs every [[motorcad_experiments|MotorCAD]] electromagnetic analysis. The rotor topology classification (axial vs radial, cage vs cageless, flux barrier) maps directly onto the rotor designs discussed in [[nagarkar_optimized_rotor_synrm]], [[torque_ripple_reduction_srm]], and the project's [[SynRM_45kW_IE5]] motor.

## Problem Statement

To present a unified treatment of synchronous reluctance motor theory: construction, d-q axis modeling, torque derivation, phasor diagrams, rotor classifications, performance characteristics, and the Vernier motor variant.

## Machine / Study Context

- **Motor types**: [[SynRM]] (cage and cageless variants), Vernier reluctance motor
- **Reference frames**: Stationary (a-b-c → d-q stationary), synchronous rotating (d-qe)
- **Assumptions in derivations**:
  - Stator resistance Rs neglected (for simplicity in phasor diagrams)
  - Stator and rotor steel infinitely permeable (in open-circuit EMF model)
  - Balanced 3-phase operation
  - Fringing neglected (air gap flux model)
  - Steady-state operation assumed for most equations

## Method / Theory

### Operating Principle

A ferromagnetic rotor with salient poles in a rotating magnetic field develops torque by the tendency to align with the field at minimum reluctance position. The rotor has no field winding and no permanent magnets. It starts as an [[induction_motor]] via a cage winding, then locks into synchronism via reluctance torque.

Key facts:
- Synchronous speed at steady state (slip = 0)
- Torque angle δ = 45° for maximum reluctance torque
- Saliency ratio Lds/Lqs governs torque density, power factor, efficiency

### d-q Axis Modeling

The three-phase stationary reference frame variables (as-bs-cs) are transformed to two-phase stationary (ds-qs) and then to synchronously rotating (d-qe). In the synchronous frame, all sinusoidal variables appear as DC quantities.

### Rotor Classification

| Category | Type | Application |
|----------|------|-------------|
| Cage rotor (line start) | Flux barrier, distributed anisotropy | Constant voltage/frequency |
| Cageless rotor | Conventional lam, axial lam | Variable speed drives |
| Axial air gap | Axially laminated, high Ld/Lq | High PF, high efficiency |
| Radial air gap | Flux barrier punched lam | Low torque ripple, lower losses |
| Vernier | Slotted iron, magnetic gearing | High torque, low speed direct drive |

## Important Equations

### 1. Input Power — Salient Pole Synchronous Machine

$$P_{in} = \frac{3V_s^2 (X_{ds} - X_{qs})}{2 X_{ds} X_{qs}} \sin 2\delta + \frac{3 V_s V_f \sin \delta}{X_{ds}}$$

| Variable | Meaning | Unit |
|----------|---------|------|
| Pin | Input power (3-phase) | W |
| Vs | Phase voltage (rms) | V |
| Vf | Excitation (speed) emf | V |
| Xds | d-axis synchronous reactance | Ω |
| Xqs | q-axis synchronous reactance | Ω |
| δ | Torque angle (electrical) | rad or deg |

**Assumptions**: Rs neglected, balanced 3-phase, steady state.

The first term is the **reluctance torque component**; the second is the **field torque component**.

### 2. Torque Equation — Salient Pole Synchronous Machine

$$T_e = 3 \left(\frac{P}{2}\right) \left[\frac{V_s V_f \sin \delta}{\omega_e X_{ds}} + \frac{V_s^2 (X_{ds} - X_{qs})}{2 \omega_e X_{ds} X_{qs}} \sin 2\delta \right]$$

Or equivalently in terms of flux linkages:

$$T_e = 3 \left(\frac{P}{2}\right) \left[\frac{\psi_s \psi_f}{L_{ds}} \sin \delta + \frac{\psi_s^2 (L_{ds} - L_{qs})}{2 L_{ds} L_{qs}} \sin 2\delta \right]$$

| Variable | Meaning | Unit |
|----------|---------|------|
| Te | Developed electromagnetic torque | N·m |
| P | Number of poles | — |
| ωe | Electrical angular velocity | rad/s |
| ψs | Stator flux linkage magnitude | Wb |
| ψf | Field flux linkage | Wb |
| Lds | d-axis inductance (sync frame) | H |
| Lqs | q-axis inductance (sync frame) | H |

### 3. SyRM Torque Equation (Vf = 0, no field winding)

$$\boxed{T_e = 3 \left(\frac{P}{2}\right) \frac{\psi_s^2 (L_{ds} - L_{qs})}{2 L_{ds} L_{qs}} \sin 2\delta}$$

This is the **reluctance torque** only. Maximum at δ = 45°.

| Variable | Meaning | Unit |
|----------|---------|------|
| Te | Reluctance torque | N·m |
| ψs | Stator flux linkage | Wb |
| Lds, Lqs | d-axis and q-axis inductances | H |
| δ | Torque angle | rad |

**Assumptions**: No field excitation (Vf = 0), Rs neglected, steady state.

### 4. Stator Flux Linkage

$$\psi_s = \left| \frac{V_s}{\omega_e} \right| \angle \left(-\frac{\pi}{2}\right)$$

If V/ω ratio is held constant (V/f constant control), ψs is constant and torque is independent of frequency.

### 5. Voltage Equation (SyRM, Rs neglected)

$$V_s = \sqrt{\frac{2 P_{in} X_{ds} X_{qs}}{3(X_{ds} - X_{qs})}}$$

Or from phasor diagram:

$$V_s \cos \delta = V_f - I_{ds} X_{ds}$$
$$V_s \sin \delta = I_{qs} X_{qs}$$

### 6. Current Components

$$I_{ds} = \frac{V_s \cos \delta - V_f}{X_{ds}}, \qquad I_{qs} = \frac{V_s \sin \delta}{X_{qs}}$$

For SyRM (Vf = 0):

$$I_{ds} = \frac{V_s \cos \delta}{X_{ds}}, \qquad I_{qs} = \frac{V_s \sin \delta}{X_{qs}}$$

### 7. General Torque Equation (d-q frame, current form)

$$T_e = \frac{3}{2} \left(\frac{P}{2}\right) (L_{ds} - L_{qs}) \, i_{qs} \, i_{ds}$$

Or equivalently:

$$T_e = \frac{3}{2} \left(\frac{P}{2}\right) \left(\psi_{ds} \, i_{qs} - \psi_{qs} \, i_{ds}\right)$$

| Variable | Meaning | Unit |
|----------|---------|------|
| ids | d-axis stator current | A |
| iqs | q-axis stator current | A |
| ψds | d-axis flux linkage | Wb |
| ψqs | q-axis flux linkage | Wb |

**This is the most practical form for MotorCAD simulations and FOC control.**

### 8. Synchronous Reactance Relations

$$X_{ds} = \omega_e L_{ds}, \qquad X_{qs} = \omega_e L_{qs}$$

### 9. Power-Torque Relation

$$P_{in} = \frac{2}{P} \omega_e T_e$$

### 10. Open-Circuit Air Gap Flux Density (per-pole model)

$$B_g = \frac{\mu_0}{g'} (u_1 - u_0) = \frac{\mu_0 u_1}{g'}$$

where u1 is the magnetic potential at the pole piece, u0 = 0 (assigned), and g' is the effective air gap.

### 11. Air Gap Permeance

$$P_g = \frac{1}{R_g} = \frac{\mu_0 A_g}{g'}$$

where:

$$A_g = \alpha \frac{\pi}{P} r_1 l$$

| Variable | Meaning | Unit |
|----------|---------|------|
| α | Pole arc / pole pitch ratio | — |
| r1 | Stator base radius | m |
| l | Stack length | m |
| g' | Effective air gap | m |

### 12. Fundamental Flux Per Pole (Fourier)

$$\phi_{M1} = \phi_g \frac{8}{\pi^2 \alpha} \sin\left(\frac{\alpha \pi}{2}\right)$$

where:

$$B_{M1} = k_1 B_g, \qquad k_1 = \frac{4}{\pi} \sin\left(\frac{\alpha \pi}{2}\right)$$

### 13. Induced EMF (per phase)

$$E_{ph} = \frac{2\pi}{\sqrt{2}} K_{w1} N_{ph} \phi_{M1} f$$

or:

$$\tilde{E}_{ph} = j E_q = j \omega \tilde{\psi}_{M1} = \frac{1}{\sqrt{2}} K_{w1} N_{ph} \phi_{M1}$$

| Variable | Meaning | Unit |
|----------|---------|------|
| E_ph | RMS induced EMF per phase | V |
| Kw1 | Winding factor | — |
| N_ph | Series turns per phase | — |
| ϕM1 | Fundamental flux per pole | Wb |
| f | Supply frequency | Hz |

### 14. Leakage Flux in Link Sections

$$\frac{1}{2}\phi_y = B_S \, y \, l$$

### 15. Magnet Magnetic Potential Difference

$$u_1 = \frac{\phi_r - \phi_y}{P_m + P_g}$$

where ϕr = Br × Am (remanent flux).

### 16. Magnet Effective Width and Permeance

$$W'_m = W_m + h/2$$
$$A'_m = W'_m \, l$$
$$P_m = \frac{\mu_{rec} \mu_0 A'_m}{l_m}$$

### 17. Air Gap Flux

$$\phi_g = u_1 P_g = \frac{\phi_r - \phi_y}{1 + P_m + R_g} = B_g A_g$$

## Key Design Insights

1. **Saliency ratio Lds/Lqs is the single most important design parameter.** Higher ratio → higher torque density, better power factor, better efficiency. Modern anisotropic construction can achieve ratios far beyond the traditional 3-5 range.

2. **Torque angle δ = 45° gives maximum reluctance torque** (from sin 2δ term). Stability limit is at this angle; exceeding it causes pull-out.

3. **Reluctance torque ∝ (Lds − Lqs) / (Lds × Lqs)** — maximizing Lds−Lqs alone is not enough; the product in the denominator matters too.

4. **Power factor ∝ saliency ratio.** With high Lds/Lqs, PF of 0.8+ is achievable (vs ~0.5 for low-saliency designs).

5. **Open slot stator**: easier automated winding but significant torque pulsations from harmonics. **Semi-closed slots**: better performance, lower harmonics.

6. **Axial lamination rotors** achieve higher Ld/Lq (ratio up to 20, efficiency ~94%) but are mechanically more complex. **Radial (flux barrier) rotors** are simpler to manufacture but have lower saliency.

7. **Cogging** can be minimized by skewing rotor bars and avoiding rotor slot counts that are exact multiples of pole count.

8. **Vernier motor**: "magnetic gearing effect" — small rotor displacement → large permeance axis displacement. N1 = N2 + P for stator/rotor slot relationship. High torque at low speed (~200 rpm).

9. **No rotor electrical losses at synchronism** — the cage winding carries no current in steady state.

10. **SyRM rated power ~1/3 of equivalent induction motor** (same frame), though this can be improved to ~1/2 with optimized design.

## Optimization Setup (if applicable)

This paper is theoretical/foundational. No explicit optimization is performed, but the equations establish the objective function for SyRM rotor optimization:

- **Objective**: Maximize torque per ampere → maximize (Lds − Lqs) / (Lds × Lqs)
- **Constraint**: Structural integrity at high speed (flux barriers weaken rotor)
- **Trade-off**: Axial lam (high saliency, complex) vs radial lam (lower saliency, simpler)
- **Key design variables**: Barrier number, barrier thickness/position ratio, pole arc/pole pitch ratio α, stack length

## Results (numerical)

- Axial lam, 2-pole, 2-phase, Ld/Lq = 20 → max efficiency **94%**
- High saliency SyRM → power factor **0.8** achievable
- SyRM pull-out torque at δ = 45°
- Starting torque: **300–400%** of full load (as induction motor)
- Beyond pull-out torque, operates as single-phase induction motor up to **500%** rated output
- Vernier motor typical speed ~**200 rpm** with high torque-to-inertia ratio
- Example Vernier: 0.312 Nm at 300 rpm with 15V controller; max speed 8400 rpm at 38V → 274.5 W electromagnetic power at air gap

## Limitations / Caveats

1. **Stator resistance neglected** in all phasor diagrams and torque derivations — affects low-speed accuracy and copper loss calculation.
2. **No saturation modeling** — the d-q inductances Lds, Lqs are treated as constant; cross-saturation effects between d and q axes are mentioned but not quantified.
3. **No thermal analysis** — temperature effects on inductance and losses not covered.
4. **No torque ripple analysis** — the sin2δ torque waveform implies significant ripple in simple designs; flux barrier optimization for ripple reduction is not treated here.
5. **Steady-state only** — no dynamic/transient modeling.
6. **Course material quality** — some equations contain typographical errors (e.g., repeated terms, inconsistent subscripts in the derivation chain). The final boxed SyRM torque equation is consistent across multiple derivations and is reliable.
7. **No FEA validation** — purely analytical treatment.

## Propagation Into Wiki

Pages to update with findings from this source:

- [[motorcad_parameters]] — add Lds/Lqs saliency ratio as primary design metric
- [[motorcad_experiments]] — reference torque equation as baseline for electromagnetic analysis
- [[motorcad_workflow]] — note d-q frame current decomposition for FOC setup
- [[known_issues]] — note that torque ripple requires flux barrier optimization beyond this theory
- [[codebase_map]] — reference source paper in research papers index
- [[motorcad_result_fields]] — map Te, Pin, δ to result field names

## Related Pages ([[wikilinks]])

- [[SynRM]] — overall synchronous reluctance motor project
- [[SynRM_45kW_IE5]] — reference motor model
- [[motorcad_parameters]] — MotorCAD variable definitions
- [[motorcad_experiments]] — experiment designs using these equations
- [[motorcad_workflow]] — simulation workflow
- [[nagarkar_optimized_rotor_synrm]] — optimized rotor geometry research
- [[torque_ripple_reduction_srm]] — torque ripple reduction methods
- [[induction_motor]] — comparison baseline for SyRM
- [[research_index]] — research papers index
