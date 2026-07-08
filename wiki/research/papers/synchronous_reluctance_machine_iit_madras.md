---
type: research_paper
title: "Synchronous Reluctance Machine Design and Control"
authors: "Sushant Saxena"
year: "2022"
venue: "M.Tech Thesis, Department of Electrical Engineering, Indian Institute of Technology Madras"
doi: ""
motor_types: ["SynRM"]
topics: ["vector control", "MTPA", "field weakening", "finite element analysis", "saturation effects", "power factor", "saliency ratio", "cross-coupling"]
topologies: ["4-pole SynRM with flux barriers"]
source_files: ["raw/papers/SYNCHRONOUS RELUCTANCE MACHINE IIT MADRAS.md"]
related_projects: ["SynRM_45kW_IE5"]
related_experiments: []
equations_added: ["stator_flux_dq", "stator_voltage_dq", "torque_synrm", "mtpa_condition", "normalized_voltage", "power_factor_synrm", "field_weakening_limit", "saturation_torque"]
concepts_updated: ["MTPA", "saliency_ratio", "cross_saturation", "field_weakening"]
motorcad_relevance: "Directly applicable — provides mathematical framework for SynRM control, torque equations, saturation-aware MTPA lookup tables, and power factor optimization. FEA methodology (Ansys Maxwell) parallels [[PyMotorCAD]] workflows. Machine parameters (22kW, 4-pole, delta-connected) serve as reference for SynRM design studies."
confidence: Verified
---

# Synchronous Reluctance Machine Design and Control — IIT Madras (2022)

## Citation

> S. Saxena, "Synchronous Reluctance Machine Design and Control," M.Tech Project Report, Dept. of Electrical Engineering, Indian Institute of Technology Madras, June 2022. Supervised by Dr. Kamalesh Hatua.

## Why This Paper Matters

This thesis provides a complete derivation of SynRM modelling from first principles through to FEA-validated control strategies. The key contribution is demonstrating that **conventional MTPA (β=45°) is suboptimal under saturation** — FEA shows the MTPA point shifts to β≈65°, yielding a **17% increase in rated torque** (123 Nm → 144 Nm) for the same stator current. The normalized model makes results applicable to any SynRM via saliency ratio ζ alone.

## Problem Statement

Conventional SynRM control assumes constant Ld and Lq, leading to an MTPA operating point at β=45°. However, the highly anisotropic SynRM rotor saturates at currents far below rated value, invalidating this assumption. The thesis asks: **Can FEA-derived operating points improve drive utilization over conventional analytical MTPA?**

## Machine / Study Context

| Parameter | Value |
|-----------|-------|
| Rated Power | 22 kW |
| Phases | 3 |
| Connection | Delta |
| Number of Poles | 4 |
| Rated Speed | 1500 RPM |
| Rated Frequency | 50 Hz |
| Max Torque | 123 Nm |
| DC Bus Voltage | 500 V |
| Stator Resistance | 0.2 Ω/phase |
| Ld (d-axis inductance) | 48.18 mH |
| Lq (q-axis inductance) | 11.88 mH |
| Saliency Ratio ζ | ~4.06 |
| Inertia J | 0.5 kg·m² |
| Rotor Material | M36 grade steel |
| Winding Pitch | 1-14, 2-13, 3-12, 4-11 |
| Turns/phase | 80 |
| Slot Fill Factor | 41% |

FEA performed in Ansys Maxwell-2D using quarter-symmetry model, magnetostatic domain, current excitation.

## Method / Theory

1. **Derive d-q model** of SynRM from equivalent circuit → stator voltage equations + torque equation
2. **Design sensored vector control** with PI current/speed loops, decoupled via signal flow graph
3. **Normalize** machine equations to be machine-independent (dependent only on ζ)
4. **Study field weakening** using normalized model — derive constant-power speed limit
5. **Apply FEA** (Ansys Maxwell-2D) to compute Ld(Ls, β) and Lq(Ls, β) under saturation
6. **Compare** analytical vs FEA torque/power-factor to validate operating-point recommendations

## Important Equations

### Stator Flux in d-q Frame (Eq. 2.2)

**Normalized form:**
$$\vec{\Psi}_s^r = L_d i_d + j L_q i_q$$

**Original notation:** $\vec{\Psi}_s^r = \Psi_{sd} + j\Psi_{sq}$

| Variable | Meaning | Unit |
|----------|---------|------|
| $\Psi_{sd}$ | d-axis stator flux linkage | Wb |
| $\Psi_{sq}$ | q-axis stator flux linkage | Wb |
| $L_d$ | Total d-axis inductance (Lls + Lmd) | H |
| $L_q$ | Total q-axis inductance (Lls + Lmq) | H |
| $i_d, i_q$ | d-axis and q-axis stator currents | A |

**Assumptions:** No rotor windings (SynRM), sinusoidal MMF distribution.

---

### Stator Voltage Equations (Eq. 2.5, 2.6)

**Normalized form:**
$$v_d = R_s i_d + \frac{d}{dt}(L_d i_d) - L_q i_q \omega$$
$$v_q = R_s i_q + \frac{d}{dt}(L_q i_q) + L_d i_d \omega$$

**Original notation:** Same as above.

| Variable | Meaning | Unit |
|----------|---------|------|
| $v_d, v_q$ | Stator voltage components in d-q | V |
| $R_s$ | Stator resistance | Ω |
| $\omega$ | Electrical rotor speed | rad/s |

**Assumptions:** Steady-state (derivative terms vanish), cross-coupling neglected.

---

### Developed Torque (Eq. 2.8)

**Normalized form:**
$$T = \frac{3}{2} \cdot \frac{P}{2} \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

or equivalently:
$$T = k_t \cdot i_d \cdot i_q$$

where $k_t = \frac{3}{2} \cdot \frac{P}{2} \cdot (L_d - L_q)$ (Eq. 2.9)

**Original notation:** $m_d = \frac{2}{3} \cdot \frac{P}{2} \cdot (L_{sd} - L_{sq}) \cdot i_{sq} \cdot i_{sd}$

| Variable | Meaning | Unit |
|----------|---------|------|
| $T$ or $m_d$ | Developed electromagnetic torque | Nm |
| $P$ | Number of poles | — |
| $k_t$ | Torque constant | Nm/A² |

**Assumptions:** Sinusoidal MMF, no saliency harmonics.

**Key insight:** Torque is proportional to the *difference* (Ld − Lq) and the *product* (id × iq). Both terms must be maximized for maximum torque.

---

### MTPA Condition (Eq. 2.11)

**Normalized form:**
$$i_d = i_q = \frac{I_s}{\sqrt{2}}$$

equivalently: β = 45°

**Original notation:** $i_{sq} = i_{sd} = \frac{I_s}{\sqrt{2}}$

| Variable | Meaning | Unit |
|----------|---------|------|
| $I_s$ | Stator current magnitude | A |
| β | Current angle (measured from d-axis) | degrees/rad |

**Derivation:** Set dT/diq = 0 with constraint id² + iq² = Is².

**Assumption:** Ld and Lq are constant (no saturation). **This breaks down under saturation** — FEA shows MTPA shifts to β > 45°.

---

### Normalized Torque (Eq. 2.26)

**Normalized form:**
$$\tau_n = i_n^2 \sin(2\beta)$$

| Variable | Meaning | Unit |
|----------|---------|------|
| $\tau_n$ | Normalized torque ($\tau / \tau_0$) | p.u. |
| $i_n$ | Normalized current ($I_s / i_0$) | p.u. |
| β | Current angle | degrees |

**Normalization base (Eq. 2.21):**
$$\tau_0 = \frac{3}{2} \cdot \frac{P}{2} \cdot (L_d - L_q) \cdot \frac{i_0^2}{2}$$

---

### Normalized Voltage (Eq. 2.24, 2.25, 2.27)

**Steady-state, constant β form (Eq. 2.27):**
$$v_n^2 = \frac{\tau_n \omega_n^2}{\zeta^2 + 1}\left(\tan\beta + \zeta^2 \cot\beta\right)$$

Rearranged for torque (Eq. 2.28):
$$\tau_n = \frac{1}{\omega_n^2} \cdot \frac{v_n^2(\zeta^2 + 1)}{\tan\beta + \zeta^2 \cot\beta}$$

| Variable | Meaning | Unit |
|----------|---------|------|
| $v_n$ | Normalized voltage ($v / v_0$) | p.u. |
| $\omega_n$ | Normalized speed ($\omega / \omega_0$) | p.u. |
| ζ | Saliency ratio ($L_d / L_q$) | — |
| β | Current angle | degrees |

---

### Power Factor (Eq. 2.34)

**Normalized form:**
$$\cos\phi = \frac{\zeta - 1}{\sqrt{\frac{\zeta^2}{\tan^2\beta} + \tan^2\beta + \zeta^2 + 1}}$$

**Maximum power factor condition (Eq. 2.35):**
$$\tan\beta = \sqrt{\zeta}$$

$$pf_{max} = \frac{\zeta - 1}{\zeta + 1}$$

For this machine (ζ ≈ 4.06): pf_max ≈ 0.603

| Variable | Meaning | Unit |
|----------|---------|------|
| φ | Angle between voltage and current | degrees |
| ζ | Saliency ratio | — |
| β | Current angle | degrees |

**Key insight:** Power factor depends *only* on ζ and β. Higher saliency ratio → higher maximum power factor.

---

### Field Weakening Speed Limit (Eq. 2.31)

**Normalized form:**
$$\omega_n < \frac{\zeta^2 + 1}{2\zeta}$$

For this machine: ω_n,max = 2.1511 → 3226.6 RPM

| Variable | Meaning | Unit |
|----------|---------|------|
| $\omega_n$ | Normalized speed | p.u. |
| ζ | Saliency ratio | — |

**Derivation:** Requires real solution to Eq. 2.30: discriminant ≥ 0.

---

### Current Angle in Field Weakening (Eq. 2.30)

$$\tan\beta = \frac{\frac{\zeta^2+1}{\omega_n} \pm \sqrt{\left(\frac{\zeta^2+1}{\omega_n}\right)^2 - 4\zeta^2}}{2}$$

---

### Saturation-Aware Torque (Eq. 3.1)

**Normalized form:**
$$T = \frac{3}{2} \cdot \frac{P}{2} \cdot \left[L_d(I_s, \beta) - L_q(I_s, \beta)\right] \cdot \frac{I_s^2 \sin(2\beta)}{2}$$

| Variable | Meaning | Unit |
|----------|---------|------|
| $L_d(I_s, \beta)$ | d-axis inductance as function of current magnitude and angle | H |
| $L_q(I_s, \beta)$ | q-axis inductance as function of current magnitude and angle | H |

**Key difference from Eq. 2.8:** Inductances are now functions of operating point, not constants.

---

### Current Loop PI Gains (Eq. 2.12–2.14)

$$\tau_{pc} = \frac{L_d}{R_s}$$
$$k_{pc} = \frac{L_d}{\tau_{bc}^*}$$
$$k_{ic} = \frac{k_{pc}}{\tau_{pc}}$$

| Variable | Meaning | Unit |
|----------|---------|------|
| $\tau_{pc}$ | Current controller time constant | s |
| $\tau_{bc}^*$ | Desired current loop bandwidth | s |
| $k_{pc}, k_{ic}$ | PI proportional and integral gains | — |

---

### Speed Loop PI Gains (Eq. 2.16–2.18)

$$\tau_{p\omega} = \frac{J}{B}$$
$$k_{p\omega} = \frac{J}{k_t \tau_{b\omega}^*}$$
$$k_{i\omega} = \frac{k_{p\omega}}{\tau_{p\omega}}$$

| Variable | Meaning | Unit |
|----------|---------|------|
| $J$ | Rotor inertia | kg·m² |
| $B$ | Frictional coefficient | Nm·s/rad |
| $\tau_{b\omega}^*$ | Desired speed loop bandwidth | s |

---

### dq-to-abc Transformation (Eq. 3.2)

$$\begin{bmatrix} d \\ q \end{bmatrix} = \begin{bmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{bmatrix} \begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix} \begin{bmatrix} a \\ b \\ c \end{bmatrix}$$

Used in FEA to convert abc flux linkages (from Maxwell) to dq frame for inductance estimation.

---

### Power Factor from Flux Linkages (used in Ch. 3)

$$PF = \cos\left(\arctan\frac{i_d}{i_q} + \arctan\frac{\psi_q}{\psi_d}\right)$$

This form avoids assuming constant inductances — suitable for FEA post-processing.

## Key Design Insights

1. **Saturation shifts MTPA:** Under saturation, the optimal β shifts from 45° (analytical) to ~60–65° (FEA). At β≈60°, saliency ratio converges across current levels — this is a robust operating point.

2. **Saturation improves torque and power factor:** Paradoxically, a saturated SynRM produces *more* torque at *better* power factor than the unsaturated prediction, because Ld increases with β (reduced d-axis saturation) while Lq remains roughly constant (already saturated). This enables **overloading** — 17% torque boost at rated current.

3. **Cross-coupling introduces a scaling error but not a shape error:** Analytical torque curves match FEA torque curve shape exactly, differing only by a scaling factor from cross-coupling. For control purposes (MTPA lookup tables), shape is sufficient.

4. **Torque ripple is inherent:** Two components — low-frequency from winding distribution, high-frequency from slotting (period = slot pitch = 7.5° mechanical for 48-slot machine). Does not affect MTPA selection.

5. **Saliency ratio limits field-weakening range:** Constant-power speed range is bounded by ω_n,max = (ζ²+1)/(2ζ). For ζ≈4.06, this gives ~2.15× base speed.

6. **Power factor is the real inverter-usage limiter:** Lower PF means higher current for same power, stressing the inverter. Operating at higher β under saturation improves PF, effectively increasing inverter utilization.

## Optimization Setup (if applicable)

No formal optimization algorithm is used. The "optimization" is an exhaustive FEA sweep:

- **Variables:** Current magnitude Is, current angle β
- **Objective:** Maximize torque at given Is, maximize power factor
- **Method:** Magnetostatic FEA in Ansys Maxwell-2D, 1/4 model, current excitation, sweep β from 0° to 90° at multiple Is levels
- **Output:** Lookup tables of Ld(Is,β), Lq(Is,β), T(Is,β), PF(Is,β)
- **Recommended:** Replace MTPA gain block with 2D lookup table directly generating id* and iq* from torque reference

**No MotorCAD comparison was performed.** FEA was done entirely in Ansys Maxwell-2D.

## Results (numerical)

| Metric | Analytical (Ch. 2) | FEA (Ch. 3) |
|--------|-------------------|-------------|
| MTPA angle (β) | 45° | ~65° at rated current |
| Rated torque | 123 Nm | 144 Nm (at β=65°) |
| Torque improvement | — | +17% |
| Field weakening speed limit | ωn = 2.1511 (3226.6 RPM) | Same (analytical bound) |
| Current loop bandwidth | 10 ms | — |
| Speed loop bandwidth | 1 s | — |
| SPWM switching frequency | 10 kHz | — |
| PI gains (speed) | kp=10.33, ki=0.206 | — |
| PI gains (d-axis current) | kp=4.818, ki=20 | — |
| PI gains (q-axis current) | kp=1.188, ki=20 | — |

Simulation: Reference speed 400 RPM step at t=0.5s, load torque step to 10 Nm at t=1.5s. First-order speed response confirmed. Current peaks at 15A during load transient.

## Limitations / Caveats

- **No hardware validation** — SynRM was unavailable at time of writing; only simulation + FEA
- **Cross-coupling effect ignored** in analytical torque estimation — introduces scaling error (underestimate of torque)
- **2D FEA only** — axial effects not captured
- **Magnetostatic FEA** — no iron loss or eddy current modelling
- **Constant saliency ratio assumed** in normalized model — breaks down under heavy saturation
- **No thermal modelling** — saturation effects are temperature-dependent (B-H curve changes)
- **Single machine studied** — results for ζ≈4.06 may not generalize to low-saliency designs
- **MotorCAD not used** — comparison with Ansys Maxwell results would be valuable for cross-validation

## Propagation Into Wiki

- [[motorcad/parameters]] — Add 22kW SynRM reference parameters (Ld, Lq, Rs, saliency ratio)
- [[motorcad/workflow]] — Note FEA methodology for inductance estimation (flux linkage → dq transform → Ld/Lq)
- [[motorcad/result_fields]] — Add torque, power factor, flux linkage as key output fields
- [[motorcad/experiments/]] — Potential: saturation-aware MTPA lookup table validation
- [[known_issues]] — Cross-coupling effect causes ~17% torque estimation error when using constant-inductance model
- [[architecture/orchestrator]] — SynRM control subagent could use lookup-table approach for MTPA

## Related Pages

- [[SynRM_45kW_IE5]] — Reference motor model in project
- [[motorcad/workflow]] — PyMotorCAD modelling workflow
- [[motorcad/parameters]] — Motor parameter database
- [[motorcad/result_fields]] — Result field definitions
- [[known_issues]] — Cross-saturation modelling gap
