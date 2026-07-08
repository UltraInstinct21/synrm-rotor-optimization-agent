---
type: research_paper
title: "Design and Analysis of Synchronous Reluctance Motor (SynRM) Using MATLAB Simulink"
authors: "Mohammed Ayad Alkhafaji, Yunus Uzun"
year: "2020"
venue: "IRSET-1-147 (journal/article)"
doi: ""
motor_types: [SynRM]
topics: [matlab_simulink_simulation, dq_model, SVPWM, vector_control, inverter_modelling]
topologies: [synchronous_reluctance]
source_files: ["raw/papers/IRSET-1-147.md"]
related_projects: [motor-deepagent]
related_experiments: []
equations_added: [synrm_dq_voltage, synrm_flux_linkage, synrm_current_dynamics, synrm_torque_dq, synrm_mechanical_dynamics, dq_transformation_matrix, svpwm_reference_voltage, svpwm_switching_times, svpwm_modulation_index]
concepts_updated: [SynRM_simulation, SVPWM_inverter, dq_transformation, SynRM_equivalent_circuit]
motorcad_relevance: "Medium — foundational d-q model and SVPWM equations are standard for motor drive simulation; parameters (Ld, Lq, Rs, J, B) are directly usable as MotorCAD input for drive-level validation"
confidence: Verified
---

# Design and Analysis of Synchronous Reluctance Motor (SynRM) Using MATLAB Simulink

## Citation
Alkhafaji, M.A. and Uzun, Y., "Design and Analysis of Synchronous Reluctance Motor (SynRM) Using MATLAB Simulink," IRSET-1-147, Aksaray University, Turkey.

## Why This Paper Matters
Provides a complete, self-contained d-q model of a cageless SynRM with SVPWM inverter drive, implemented entirely in MATLAB/Simulink. All simulation parameters are explicitly tabulated. The paper serves as a straightforward reference for the standard SynRM drive equations — useful as a baseline validation model for [[PyMotorCAD]] electromagnetic simulations and as a template for [[SynRM_simulation]] drive-level studies.

## Problem Statement
SynRM is gaining industrial importance due to its simple rotor construction (no windings, no permanent magnets), low manufacturing cost, and ruggedness. However, characterizing its dynamic performance under different load and frequency conditions requires simulation. This paper models the complete SynRM drive system — motor, d-q transformation, and SVPWM inverter — in Simulink and validates speed/torque response under no-load and loaded conditions.

## Machine / Study Context
- **Machine type:** 3-phase, 2-pole [[SynRM]] (cageless rotor)
- **Rated speed:** 3000 rpm (at 50 Hz synchronous speed)
- **Stator resistance Rs:** 0.0265 Ω
- **d-axis inductance Ld:** 6.0645 mH
- **q-axis inductance Lq:** 0.910 mH
- **Inertia J:** 0.245 kgm²
- **Viscous friction B:** 0.0000009 N.m.s
- **Pole pairs P:** 2 (note: paper states P=2 but describes 2-pole behavior at 3000 rpm — likely P is number of poles = 2, i.e. 1 pole pair)
- **Simulation tool:** MATLAB/Simulink
- **Inverter type:** Three-phase voltage-source inverter with 6 MOSFETs, SVPWM modulation
- **Operating conditions tested:** 25 Hz no-load, 50 Hz no-load, 25 Hz with 20 N.m load applied at 1.4 s

## Method / Theory

### SynRM d-q Equivalent Circuit
The SynRM model is derived from induction motor equations with rotor losses neglected. The stator has the same winding layout as an induction motor. The rotor is a laminated steel structure with flux barriers — no cage, no windings, no magnets. Torque is produced purely through reluctance difference (Ld ≠ Lq).

### Space Vector PWM (SVPWM)
The inverter converts DC bus voltage to three-phase AC using SVPWM. The reference voltage vector is derived from d-q transformed voltages. The SVPWM algorithm divides the voltage hexagon into six sectors and calculates switching times for each active and zero vector within one switching period.

### Drive System Architecture
The complete drive consists of three blocks: (1) SynRM motor model, (2) d-q transformation matrix, (3) SVPWM inverter. A feedback loop provides speed control by comparing reference speed with measured speed.

## Important Equations

### SynRM Voltage Equations (d-q frame)

**Eq. 1 — d-axis voltage:**
$$V_d = R_s I_d + \frac{d\lambda_d}{dt} - \omega_r \lambda_q$$

**Eq. 2 — q-axis voltage:**
$$V_q = R_s I_q + \frac{d\lambda_q}{dt} + \omega_r \lambda_d$$

| Variable | Description | Unit |
|----------|-------------|------|
| Vd, Vq | d-q axis stator voltages | V |
| Id, Iq | d-q axis stator currents | A |
| Rs | Stator resistance | Ω |
| λd, λq | d-q axis flux linkages | Wb |
| ωr | Rotor electrical angular speed | rad/s |

**Assumptions:** Steady-state and transient both valid; d-q frame aligned with rotor flux.

### Flux Linkage Equations

**Eq. 3 — d-axis flux linkage:**
$$\lambda_d = L_d I_d$$

**Eq. 4 — q-axis flux linkage:**
$$\lambda_q = L_q I_q$$

| Variable | Description | Unit |
|----------|-------------|------|
| Ld | d-axis self-inductance | H |
| Lq | q-axis self-inductance | H |

**Key distinction:** No mutual inductance terms — Ld and Lq are independent. No PM flux linkage term (λpm = 0). [[SynRM_literature_review]]

### Flux Linkage Rate of Change

**Eq. 5:**
$$\frac{d\lambda_d}{dt} = V_d - R_s I_d - \omega_r \lambda_q$$

**Eq. 6:**
$$\frac{d\lambda_q}{dt} = V_q - R_s I_q + \omega_r \lambda_d$$

### Current Dynamics

**Eq. 7 — d-axis current rate:**
$$\frac{dI_d}{dt} = \frac{1}{L_d}(V_d - R_s I_d + \omega_r L_q I_q)$$

**Eq. 8 — q-axis current rate:**
$$\frac{dI_q}{dt} = \frac{1}{L_q}(V_q - R_s I_q - \omega_r L_d I_d)$$

**Note:** Eq. 8 in the original paper has a typo using La instead of Lq; the correct form uses Lq. The sign of the cross-coupling term in Eq. 8 should be negative (−ωr Ld Id) for standard convention. [[dq_current_dynamics]]

### Electromagnetic Torque

**Eq. 9:**
$$T_e = \frac{3}{2} P (L_d - L_q) I_d I_q$$

| Variable | Description | Unit |
|----------|-------------|------|
| Te | Electromagnetic torque | N.m |
| P | Number of pole pairs | — |
| Ld − Lq | Reluctance difference | H |
| Id, Iq | d-q axis currents | A |

**Note:** The original paper shows 3/4 in Eq. 9 but this appears to be a typographical error; the standard form uses 3/2. The torque is purely reluctance torque — no PM contribution. [[SynRM_torque_expression]]

### Mechanical Dynamics

**Eq. 10:**
$$\frac{d\omega_r}{dt} = \frac{P}{J}(T_e - T_L)$$

**Eq. 11 — Full mechanical equation (Laplace form):**
$$T_e = \frac{3}{2}P(L_d - L_q)i_d i_q - (B\omega_r + J\frac{d\omega_r}{dt})$$

| Variable | Description | Unit |
|----------|-------------|------|
| J | Moment of inertia | kgm² |
| B | Viscous friction coefficient | N.m.s/rad |
| TL | Load torque | N.m |
| ωr | Rotor mechanical speed | rad/s |

### d-q Transformation Matrix (Clarke-like)

**Eq. 12:**
$$\begin{bmatrix} V_d \\ V_q \end{bmatrix} = \sqrt{\frac{2}{3}} \begin{bmatrix} 1 & -\frac{1}{2} & -\frac{1}{2} \\ 0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \end{bmatrix} \begin{bmatrix} V_a \\ V_b \\ V_c \end{bmatrix}$$

| Variable | Description | Unit |
|----------|-------------|------|
| Va, Vb, Vc | Three-phase stator voltages | V |
| Vd, Vq | Two-phase equivalent voltages | V |

**Assumptions:** Three-phase balanced, zero-sequence neglected, power-invariant transform. [[Park_transform]], [[Clarke_transform]]

### SVPWM Equations

**Eq. 13 — Reference voltage magnitude:**
$$\|V_{ref}\| = \sqrt{V_d^2 + V_q^2}$$

**Eq. 14 — Reference angle:**
$$\alpha = \tan^{-1}\left(\frac{V_d}{V_q}\right) = \omega_s t = 2\pi f_s t$$

**Eq. 15 — Vector synthesis:**
$$V_{ref} T_s = V_1 T_a + V_2 T_b + V_{0,7} T_o$$

**Eq. 16 — Switching period constraint:**
$$T_s = T_a + T_b + T_o$$

**Eq. 17 — Complex reference vector:**
$$V_{ref} = V_{ref} e^{j\alpha}$$

**Eq. 18 — Active and zero vectors:**
$$V_1 = \frac{2}{3}V_{dc}, \quad V_{0,7} = 0, \quad V_2 = \frac{2}{3}V_{dc} e^{j\pi/3}$$

**Eq. 19 — Real component (Re):**
$$V_{ref}\cos(\alpha) T_s = \frac{2}{3}V_{dc} T_a + \frac{1}{3}V_{dc} T_b$$

**Eq. 20 — Imaginary component (Im):**
$$V_{ref}\sin(\alpha) T_s = \frac{1}{\sqrt{3}}V_{dc} T_b$$

**Eq. 21 — Active vector time Ta (sector 1):**
$$T_a = \frac{\sqrt{3} T_s V_{ref}}{V_{dc}}\sin\left(\frac{\pi}{3} - \alpha\right) = T_s \cdot m_a \cdot \sin\left(\frac{\pi}{3} - \alpha\right)$$

**Eq. 22 — Active vector time Tb (sector 1):**
$$T_b = \frac{\sqrt{3} T_s V_{ref}}{V_{dc}}\sin(\alpha) = T_s \cdot m_a \cdot \sin(\alpha)$$

**Eq. 23 — Zero vector time:**
$$T_o = T_s - T_a - T_b$$

**Eq. 24 — Modulation index:**
$$m_a = \frac{\sqrt{3} V_{ref}}{V_{dc}}, \quad 0 \leq \alpha \leq 60°$$

**Eq. 25 — Generalized Ta (sector n):**
$$T_a = \frac{\sqrt{3} T_s V_{ref}}{V_{dc}}\sin\left(\frac{n\pi}{3} - \alpha\right)$$

**Eq. 26 — Generalized Tb (sector n):**
$$T_b = \frac{\sqrt{3} T_s V_{ref}}{V_{dc}}\sin\left(\alpha - \frac{(n-1)\pi}{3}\right)$$

| Variable | Description | Unit |
|----------|-------------|------|
| Vdc | DC bus voltage | V |
| Ts | Switching period | s |
| Ta, Tb | Active vector switching times | s |
| To | Zero vector switching time | s |
| ma | Modulation index | — |
| α | Reference voltage angle | rad |
| n | Sector number (1–6) | — |

**Assumptions:** Voltage source constant during one switching cycle; six-sector SVPWM; balanced three-phase output. [[SVPWM_inverter]], [[PWM_techniques]]

## Key Design Insights
1. **Ld/Lq ratio is the core performance driver:** Ld = 6.0645 mH, Lq = 0.910 mH gives Ld/Lq ≈ 6.66, which is a high saliency ratio indicating good torque-producing capability.
2. **Cageless operation viable with SVPWM + FOC:** The paper confirms that modern SVPWM inverters eliminate the need for a rotor cage, simplifying construction.
3. **Speed control via frequency:** Motor speed is directly proportional to supply frequency; at 50 Hz with 2 pole pairs, synchronous speed = 1500 rpm (paper states 3000 rpm which suggests P=1 interpretation, or there is a discrepancy).
4. **Load causes speed droop without control:** When 20 N.m load is applied at 25 Hz without feedback control, speed drops significantly — demonstrating the need for closed-loop control.

## Optimization Setup
Not applicable — this is a simulation/characterization study, not an optimization study.

## Results (Numerical)
- **Efficiency:** 94.8% (measured in simulation)
- **No-load speed at 25 Hz:** Settles to synchronous speed (~1500 rpm)
- **No-load speed at 50 Hz:** Settles to synchronous speed (~3000 rpm)
- **Loaded speed at 25 Hz (20 N.m at 1.4 s):** Speed drops from synchronous — no feedback control applied
- **No-load torque:** Near zero (small oscillations due to PWM switching)
- **Loaded torque:** Rises to match 20 N.m load after transient
- **d-axis and q-axis currents:** Id is dominant (high inductance path), Iq is small — consistent with reluctance torque production

## Limitations / Caveats
1. **No rotor saturation modelling:** Ld and Lq are treated as constants — real SynRM inductances vary with current (magnetic saturation). [[Iron_saturation]]
2. **No iron loss modelling:** Core losses are neglected; the paper states "neglecting rotor losses from IM equations" but also does not model stator iron losses.
3. **No cogging torque or torque ripple analysis:** The paper does not quantify torque ripple, which is a critical SynRM performance metric. [[torque_ripple_reduction]]
4. **Typographical inconsistencies:** Eq. 9 shows 3/4 coefficient (should be 3/2); Eq. 8 uses La instead of Lq; pole pairs stated as P=2 but described behavior suggests P=1.
5. **No speed controller:** The simulation runs open-loop — no PI or other speed controller is implemented, limiting practical relevance.
6. **Very low viscous friction (B ≈ 0):** The given B value is essentially zero, which may not represent real bearing and windage losses.
7. **No experimental validation:** Results are purely simulation-based with no hardware comparison.

## Propagation Into Wiki
- Update [[SynRM_simulation]] — add this paper as a Simulink-based reference implementation
- Update [[SynRM_dq_model]] — add parameter table and confirmed equations
- Update [[SVPWM_inverter]] — add full SVPWM timing equations (Eqs. 13–26)
- Update [[motorcad_parameter_reference]] — add Ld, Lq, Rs, J, B values as simulation baseline
- Update [[drive_simulation_workflow]] — add Simulink block diagram structure as reference

## Related Pages
- [[SynRM]]
- [[SynRM_dq_model]]
- [[SVPWM_inverter]]
- [[PWM_techniques]]
- [[Park_transform]]
- [[Clarke_transform]]
- [[PyMotorCAD]]
- [[SynRM_optimization]]
- [[torque_ripple_reduction]]
- [[Iron_saturation]]
- [[motor-deepagent]]
