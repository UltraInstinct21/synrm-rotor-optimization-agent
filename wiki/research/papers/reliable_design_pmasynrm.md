---
type: research_paper
title: "Reliable Design of PMaSynRM"
authors: "Carlos López-Torres, Antoni Garcia-Espinosa, Jordi-Roger Riba"
year: 2018
venue: "IntechOpen Book Chapter"
doi: "10.5772/intechopen.76355"
motor_types: ["PMa-SynRM", "SynRM", "Ferrite PM"]
topics: ["pre-design", "analytical design", "rare-earth-free", "EV traction", "ferrite magnets", "electromagnetic design", "reluctance network", "mechanical stress"]
topologies: ["PMa-SynRM", "SynRM"]
source_files: ["raw/papers/Reliable_Design_of_PMaSynRM.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: [
  "eq:P_e", "eq:I_f", "eq:N_s", "eq:C_mec", "eq:X_form_factor", "eq:L_stk",
  "eq:g_airgap", "eq:z_q", "eq:N_ph_new", "eq:B_g_new",
  "eq:phi_t", "eq:tau_s", "eq:b_t", "eq:phi_g", "eq:tau_p",
  "eq:h_y", "eq:b_s", "eq:h_s", "eq:h_t", "eq:D_os",
  "eq:k_flux_barriers", "eq:alpha_barrier_angle",
  "eq:MMF_di", "eq:Si_ratio", "eq:L_s_segments", "eq:k_ins_q",
  "eq:MMF_qi", "eq:W_qi_ratio", "eq:R_barrier", "eq:phi_q_barrier",
  "eq:La_total_air", "eq:flux_minimization",
  "eq:W_di_ratio", "eq:L_ad_daxis",
  "eq:D_or", "eq:D_ir",
  "eq:MMF_winding", "eq:MMF_magnet", "eq:R_magnetic",
  "eq:MMF_KVL", "eq:flux_KCL",
  "eq:L_d_L_q", "eq:E_dq", "eq:torque", "eq:P_out",
  "eq:P_cu", "eq:P_fe", "eq:efficiency",
  "eq:F_centrifugal", "eq:W_r_radial_rib"
]
concepts_updated: [
  ["PMa-SynRM Design", "Complete analytical pre-design procedure for PMa-SynRM"],
  ["Ferrite Magnet Benefits", "Higher Curie temp, lower eddy current loss vs rare-earth"],
  ["Saliency Ratio Maximization", "Minimize air gap thickness for max saliency"],
  ["Rotor Flux Barrier Sizing", "Equal saturation across segments; barrier ratio from MMF delta"],
  ["Reluctance Network Model", "d/q-axis RN for inductance, flux linkage, torque calculation"],
  ["Mechanical Rib Sizing", "Centrifugal force and tensile strength determine rib width"]
]
motorcad_relevance: "High — provides complete analytical pre-design workflow directly applicable to [[SynRM]]/[[PMa-SynRM]] geometry setup in PyMotorCAD. Equations for slot/tooth/yoke sizing, rotor barrier placement, and magnet quantity can seed initial geometry before FEA optimization. The [[Reluctance Network Model]] (Eqs 46–54) enables fast torque/power-factor estimation without full FEA."
confidence: Verified
---

# Reliable Design of PMa-SynRM

## Citation

López-Torres, C., Garcia-Espinosa, A., & Riba, J.-R. (2018). Reliable Design of PMaSynRM. In *IntechOpen*. [DOI: 10.5772/intechopen.76355](http://dx.doi.org/10.5772/intechopen.76355)

## Why This Paper Matters

This is a **complete analytical pre-design procedure** for PMa-SynRM machines, covering electromagnetic, thermal, and mechanical domains in a single iterative workflow. It provides ~59 equations that can directly seed [[PyMotorCAD]] geometry setup before [[Finite Element Analysis|FEA]] optimization. The approach is explicitly designed for **rare-earth-free EV traction motors** using [[Ferrite Magnets]], making it directly relevant to [[motor-deepagent]]'s SynRM optimization goals. The [[Reluctance Network Model]] (Eqs 46–54) is a fast analytical substitute for FEA during initial design sweeps.

## Problem Statement

EV traction motors require high reliability, power density, efficiency, and wide constant-power speed range — but rare-earth magnet supply/cost concerns drive demand for alternatives. Pure [[SynRM|SynRM]] topologies have low power factor and power density. [[PMa-SynRM|PMa-SynRM]] with ferrite magnets is a promising middle ground, but the **optimal design process** based on [[Finite Element Analysis|FEM]] is computationally expensive. An accurate analytical **pre-design** is needed to provide a good starting geometry that reduces optimization iterations.

## Machine / Study Context

- **Topology**: PMa-SynRM (permanent magnet assisted synchronous reluctance motor)
- **Application**: EV traction (high reliability, harsh thermal/mechanical conditions)
- **Magnet material**: Ferrite (not rare-earth) — higher Curie temperature, lower eddy current losses, but lower remanent flux density
- **Design domains**: Electromagnetic, thermal, mechanical — all considered simultaneously
- **Key advantage**: In demagnetization failure, machine degrades to pure SynRM providing ~75% rated torque (graceful degradation)

## Method / Theory

The procedure is a **multi-domain iterative analytical pre-design**:

1. **Electrical parameters** (Eqs 1–3): Estimate efficiency, power factor → compute electrical power, phase current, turns per phase
2. **Main dimensions** (Eqs 4–7): Use [[Mechanical Constant|C_mec]] to size air gap volume from reference motor data; form factor X relates diameter to length
3. **Stator geometry** (Eqs 8–21): Teeth, yoke, slots sized to limit magnetic saturation (teeth: 1.5–1.8 T; yoke: 1.4–1.6 T) and accommodate conductor current density
4. **Rotor geometry** (Eqs 22–45): Number of [[Flux Barriers]] chosen; barrier angles set; segment widths sized for **equal magnetic saturation** using [[Equivalent Magnetic Circuit|equivalent magnetic circuits]] in d- and q-axes; barrier widths sized to **minimize q-axis flux**
5. **[[Reluctance Network Model]]** (Eqs 46–54): d/q-axis reluctance networks solve for inductances L_d, L_q, and magnet flux linkage; computes torque, back EMF, power factor, efficiency
6. **Mechanical sizing** (Eqs 58–59): [[Radial Ribs]] sized for centrifugal force with safety factor > 2
7. **Iteration loop**: All estimated parameters (efficiency, power factor, B_g, etc.) are refined until convergence

## Important Equations

### Electrical Parameters

**Eq 1 — Electrical Power**
$$P_e = \frac{P_{mec}}{\eta}$$
- *Normalized form*: P_e = P_mec / η
- *Variables*: P_e [W] electrical power, P_mec [W] mechanical output power, η [—] estimated efficiency (~0.95 for SynRM)
- *Assumptions*: No additional losses beyond copper, iron, and mechanical

**Eq 2 — Phase Current**
$$I_f = \frac{P_e}{m U_f \cos(\varphi)}$$
- *Normalized form*: I_f = P_e / (m · U_f · cos(φ))
- *Variables*: I_f [A] RMS phase current, m [—] number of phases, U_f [V] RMS phase voltage, cos(φ) [—] estimated power factor (~0.7 for SynRM)

**Eq 3 — Number of Turns per Phase**
$$N_s = \frac{\sqrt{2} E}{\omega_e k_{w1} l_{eff} \tau_p \frac{D_{is}}{2} \alpha_i \hat{B}_g}$$
- *Variables*: E [V] back EMF (≈ 0.97 × U_f), ω_e [elec rad/s] electrical angular speed, k_w1 [—] fundamental winding factor, l_eff [m] effective stack length, τ_p [m] pole pitch, D_is [m] inner stator diameter, α_i [—] flux density average coefficient (2/π ≈ 0.64 for sinusoidal), B̂_g [T] peak air gap flux density

### Main Dimensions

**Eq 4 — [[Mechanical Constant|Mechanical Constant]]**
$$C_{mec} = \frac{P_{mec}}{D_{is}^2 l_{eff} n_{syn}}$$
- *Variables*: C_mec [W/(m³·Hz)] mechanical power constant, n_syn [Hz] rated electrical frequency
- *Reference values*: ~10 Nm/L for PMa-SynRM (from Bianchi et al.)

**Eq 5 — Form Factor**
$$X \approx \frac{\pi}{4\sqrt{p}}$$
- *Variables*: X [—] form factor (l_eff / D_is ratio), p [—] number of pole pairs
- *Purpose*: Relates bore diameter to effective length

**Eq 6 — Stack Length**
$$L_{stk} = l_{eff} - 2g$$
- *Variables*: L_stk [m] stack length (active part only, no end windings)

**Eq 7 — Air Gap (from SynRM/IM经验)**
$$g = \frac{0.18 + 0.006 P_{mec}^{0.4}}{1000}$$
- *Variables*: g [m] air gap length, P_mec [W]
- *Note*: Should be smaller than IM air gap to maximize [[Saliency Ratio]]

### Stator Geometry

**Eq 8 — Conductors per Slot**
$$z_q \approx \frac{2m N_{ph}}{Q_s}$$
- *Variables*: z_q [—] conductors per slot (must be integer), Q_s [—] number of slots
- *After rounding*: N_ph must be updated via Eq 9

**Eq 9 — Updated Turns per Phase**
$$N_{ph\_new} = \frac{z_q Q_s}{2m}$$

**Eq 10 — Updated Air Gap Flux Density**
$$\hat{B}_{g\_new} = \frac{\sqrt{2} E}{\omega_e k_{w1} l_{eff} \tau_p \frac{D_{is}}{2} \alpha_i N_{ph\_new}}$$

**Eq 11 — Tooth Flux**
$$\phi_t = \hat{B}_{g\_new} l_{eff} \tau_s \frac{D_{is}}{2}$$

**Eq 12 — Slot Pitch**
$$\tau_s = \frac{2\pi}{Q_s}$$

**Eq 13 — Tooth Width**
$$b_t = \frac{\phi_t}{k_{sf} \hat{B}_t L_{stk}}$$
- *Variables*: k_sf [—] stacking factor, B̂_t [T] max allowed tooth flux density (1.5–1.8 T)

**Eq 14 — Air Gap Flux (average)**
$$\phi_g = \frac{2}{\pi} \hat{B}_{g\_new} l_{eff} \tau_p \frac{D_{is}}{2}$$
- *Note*: 2/π converts peak sinusoidal to average

**Eq 16 — Pole Pitch**
$$\tau_p = \frac{2\pi}{2p}$$

**Eq 17 — Yoke Width**
$$h_y = \frac{\phi_g}{2 k_{sf} \hat{B}_y L_{stk}}$$
- *Variables*: B̂_y [T] max allowed yoke flux density (1.4–1.6 T, near knee of B-H curve)

**Eq 18 — Slot Width**
$$b_s = \tau_s \frac{D_{is}}{2} - b_t$$

**Eq 19 — Slot Height**
$$h_s = \frac{z_q I_{ph}}{J k_u b_s}$$
- *Variables*: J [A/m²] current density (depends on coolant), k_u [—] winding factor (~0.40)

**Eq 20 — Tooth Height**
$$h_t = h_s + h_{tip} + \Delta$$
- *Note*: h_tip ~ 1 mm, Δ ~ 0.5 mm (machine-dependent)

**Eq 21 — Outer Stator Diameter**
$$D_{os} = D_{is} + 2h_t + 2h_y$$

### Rotor Geometry

**Eq 22 — Number of Flux Barriers**
$$k = \frac{Q_s}{2p} \pm 2$$
- *Note*: Two possible values; choice depends on application/rotor size

**Eq 23 — Barrier Angle**
$$\alpha_i = \frac{\pi/p}{k+1}$$
- *Purpose*: Angle between barrier end points; reduces torque ripple

**Eq 24 — Segment Flux (d-axis, simplified)**
$$\phi_i = \frac{MMF_{di}}{\mathfrak{R}_g}$$
- *Assumption*: Air gap reluctance dominates; segment reluctances negligible

**Eq 25 — MMF per Segment (d-axis)**
$$MMF_{di} = \frac{\sin\left(\frac{2i-1}{2} p \alpha_i\right) - \sin\left(\frac{2i-3}{2} p \alpha_i\right)}{p \alpha_i}$$
- *Note*: Averaged from sinusoidal MMF distribution over each segment arc

**Eq 26 — Equal Saturation Condition (segment widths)**
$$\frac{S_i}{S_{i+1}} = \frac{MMF_i}{MMF_{i+1}}$$
- *Physical meaning*: All segments have same magnetic saturation level

**Eq 28 — Segment 1 Adaptation**
$$\frac{2S_1}{S_2} = \frac{MMF_1}{MMF_2}$$
- *Note*: Factor of 2 because flux splits across two poles at segment 1

**Eq 29 — Total Segment Length**
$$L_s = \sum_{i=1}^{n_b+1} S_i = \frac{h_{rotor}}{1 + k_{insq}}$$
- *Variables*: h_rotor = (D_or - D_ir)/2, k_insq [—] insulation ratio q-axis (~1.0)

**Eq 30 — Insulation Ratio q-axis**
$$k_{insq} = \frac{L_a}{L_s}$$
- *Variables*: L_a total air width q-axis, L_s total segment width q-axis

**Eq 31 — MMF per Segment (q-axis)**
$$MMF_{qi} = \frac{-\cos\left(\frac{2i-1}{2} p \alpha_i\right) + \cos\left(\frac{2i-3}{2} p \alpha_i\right)}{p \alpha_i}$$

**Eq 32 — Barrier Width Ratio (q-axis)**
$$\frac{W_{qi}}{W_{qi+1}} = \frac{\Delta MMF_i}{\Delta MMF_{i+1}}$$
- *Derived from*: Minimizing total q-axis flux (Eqs 33–40)

**Eq 34 — Barrier Reluctance**
$$\mathfrak{R}_{bi} = \frac{W_{qi}}{\mu_o l_{qi} L_{stk}}$$

**Eq 37 — Total Air Width (q-axis)**
$$L_a = \sum_{i=1}^{n_b} W_{qi} = \frac{h_{rotor}}{1 + 1/k_{insq}}$$

**Eq 39 — Flux Minimization Result**
$$\frac{\Delta MMF_1}{W_{q1}^2} l_{q1} = \frac{\Delta MMF_2}{W_{q2}^2} l_{q2}$$
- *Assumption*: Permeance l_q/W_q constant across barriers (Eq 40)

**Eq 41 — Alternative Barrier Ratio (from Vagati/Moghaddam)**
$$\frac{W_{qi}}{W_{qi+1}} = \frac{\Delta MMF_i^2}{\Delta MMF_{i+1}^2}$$
- *Note*: Different formulation from Eq 32; squared MMF ratio

**Eq 42 — d-axis Barrier Width Ratio**
$$\frac{W_{di}}{W_{di+1}} = \frac{W_{qi}}{W_{qi+1}}$$

**Eq 43 — Total d-axis Air Width**
$$L_{ad} = \sum_{i=1}^{n_b} W_{di} = L_s k_{insd}$$
- *Variables*: k_insd [—] insulation ratio d-axis (swept iteratively)

**Eq 44 — Outer Rotor Diameter**
$$D_{or} = D_{is} - 2g$$

**Eq 45 — Inner Rotor Diameter**
$$D_{ir} = D_{or} - 2h_{rotor}$$

### Reluctance Network Model

**Eq 46 — Winding MMF**
$$MMF_{winding} = \sum NI$$
- *Variables*: N conductors in coil, I rated current per phase

**Eq 47 — Magnet MMF**
$$MMF_{magnet} = H_c W_{qi}$$
- *Variables*: H_c [A/m] coercive force of ferrite, W_qi [m] magnet width (= barrier width)

**Eq 48 — Magnetic Reluctance**
$$\mathfrak{R} = \frac{l}{\mu_o \mu_r S}$$
- *Variables*: l [m] path length, S [m²] cross section, μ_r [—] relative permeability (1 for air, varies with saturation in steel)
- *Note*: Air gap reluctance multiplied by [[Carter's Coefficient]]

**Eq 49 — Kirchhoff's Voltage Law (magnetic)**
$$MMF = \sum \mathfrak{R} \phi$$

**Eq 50 — Kirchhoff's Current Law (magnetic)**
$$\sum \phi = 0$$

**Eq 51 — Inductances and Magnet Flux Linkage**
$$L_d = 2pN \frac{\phi_d}{I}$$
$$L_q = \frac{2pN\phi_q - \Psi_{mpq}}{I}$$
$$\Psi_{mpq} = 2pN\phi_q \quad \text{(where } I_q = 0\text{)}$$
- *Method*: Solve q-axis RN twice — once with magnets only (→ Ψ_mpq), once with full MMF

**Eq 52 — Back EMF**
$$E_d = -\omega_e L_q i_q - \omega_e \Psi_{mpq}$$
$$E_q = \omega_e L_d i_d$$

**Eq 53 — Electromagnetic Torque**
$$T = \frac{m}{2} p \left[(L_d - L_q) i_d i_q - \Psi_{mpq} i_d\right]$$
- *Variables*: m phases, p pole pairs, i_d/i_q [A] d/q currents (from MTPA)

**Eq 54 — Output Power**
$$P_{out} = \omega_e T$$

### Losses and Efficiency

**Eq 55 — Copper Losses**
$$P_{cu} = m R_s I_{rms}^2$$
- *Variables*: R_s [Ω] phase resistance (from stator geometry)

**Eq 56 — Iron Losses (Bertotti model)**
$$P_{fe} = k_h \frac{\omega_e}{2} \hat{B}^{n_i} + k_e \left(\frac{\omega_e}{2} \hat{B}\right)^2$$
- *Variables*: k_h [W/kg] hysteresis coefficient, k_e [W/kg] eddy current coefficient, n_i [—] Steinmetz exponent
- *Note*: Per-unit-mass; multiply by mass of yoke, teeth, and rotor (different saturation levels)

**Eq 57 — Efficiency**
$$\eta = \frac{P_{out}}{P_{out} + P_{cu} + P_{fe}}$$

### Mechanical Sizing

**Eq 58 — Centrifugal Force**
$$F_c = M \omega_m^2 R_G$$
- *Variables*: M [kg] mass supported by rib, ω_m [rad/s] mechanical speed, R_G [m] radius to center of gravity

**Eq 59 — Radial Rib Width**
$$W_r = \frac{k_s F_c}{\sigma_r L_{stk}}$$
- *Variables*: k_s [—] safety factor (>2), σ_r [Pa] tensile strength of lamination

## Key Design Insights

1. **Ferrite advantage for EVs**: Higher Curie temperature and lower eddy current losses than NdFeB → better reliability at high temperatures; supply chain resilience
2. **Equal saturation principle**: All rotor segments sized for the same B ensures no single segment is the bottleneck (Eqs 26, 28)
3. **Barrier sizing minimizes q-axis flux**: Direct minimization of total q-reluctance path (Eqs 32–40) — this maximizes saliency ratio
4. **Graceful degradation**: PMa-SynRM can operate as pure SynRM at ~75% torque if magnets demagnetize
5. **Innermost barrier priority**: Place magnets in innermost barrier first — outer barriers are more magnetically stressed, higher demagnetization risk
6. **Insulation ratios (k_insq, k_insd)** are key free parameters; k_insq ~ 1.0 is a good starting point, k_insd swept iteratively
7. **Two iterative loops** in rotor design: q-axis loop (sizes segments/barriers by h_rotor), d-axis loop (sizes barrier d-widths by k_insd)
8. **C_mec from reference motors**: The mechanical constant approach uses database of existing machines of same topology — Fig. 2 shows typical values vs efficiency

## Optimization Setup

This paper provides **pre-design** equations, not a formal optimization. However:

- **Free variables in pre-design**: k_insq, k_insd, h_rotor (via inner diameter), insulation ratios
- **Constraining loops**: Barrier minimum thickness (~3 mm for ferrite magnets), correct last-barrier angle (1.5α_m), mechanical strength check
- **Extension to optimization**: The [[Reluctance Network Model]] (Eqs 46–54) can replace FEA in fast optimization sweeps; reference [36] couples RN with genetic algorithm
- **For [[motor-deepagent]]**: These equations can initialize PyMotorCAD geometry before [[Finite Element Analysis|FEA]] refinement

## Results (numerical)

This is an **analytical methodology paper** — no specific numerical test results are presented for a single machine. The paper:

- Demonstrates the procedure with design examples showing the iterative convergence (Figures 9, 10)
- Shows that first iteration (i=1) may yield barrier widths below ferrite manufacturing minimum (0.5 mm vs required 3 mm)
- Final solution (i=n) yields inner rotor diameter of 75 mm vs 90 mm in first iteration — the rotor must be larger to accommodate minimum barrier thickness
- Compares mechanical constants across motor topologies (Fig. 2): PMa-SynRM achieves ~10 Nm/L at high efficiency
- References show benchmark machines achieving comparable performance to rare-earth PMSMs

## Limitations / Caveats

1. **No FEA validation in paper**: The analytical procedure is presented without direct comparison to FEM results for a specific machine
2. **Sinusoidal MMF assumption**: Rotor geometry calculated assuming sinusoidal MMF distribution — real windings introduce harmonics
3. **Simplified reluctance networks**: RN model neglects cross-coupling, saturation in q-axis steel, and 3D effects
4. **Carter's coefficient**: Only mentioned, not derived — accuracy depends on correct application
5. **Thermal domain**: Only considered in slot sizing (current density selection); no detailed thermal model presented
6. **Magnet demagnetization**: Only mentioned qualitatively; no quantitative demagnetization analysis
7. **k_insq and k_insd selection**: Largely trial-and-error; the paper acknowledges optimization is needed for optimal values
8. **Iron loss model**: Uses Bertotti separation — coefficients from manufacturer datasheets, which may not match actual operating conditions

## Propagation Into Wiki

- [[PMa-SynRM Design]] — add this as a reference pre-design procedure with equation list
- [[SynRM]] — update with PMa-SynRM hybrid concept and ferrite benefits
- [[Flux Barriers]] — add barrier sizing equations (Eqs 22–43), equal saturation principle
- [[Saliency Ratio]] — link to barrier design and air gap minimization
- [[Mechanical Constant]] — add C_mec values and reference data for SynRM/PMa-SynRM
- [[Ferrite Magnets]] — add Curie temperature, demagnetization considerations, barrier placement strategy
- [[Reluctance Network Model]] — add d/q-axis RN procedure (Eqs 46–54)
- [[Radial Ribs]] — add centrifugal force sizing (Eqs 58–59)
- [[PyMotorCAD Workflow]] — add as analytical pre-design reference before FEA
- [[Optimization Setup]] — link pre-design as initialization step

## Related Pages

- [[SynRM]]
- [[PMa-SynRM]]
- [[Ferrite Magnets]]
- [[Flux Barriers]]
- [[Saliency Ratio]]
- [[Reluctance Network Model]]
- [[Radial Ribs]]
- [[Mechanical Constant]]
- [[Finite Element Analysis]]
- [[PyMotorCAD Workflow]]
- [[motor-deepagent]]
- [[motorcad_parameters]]
