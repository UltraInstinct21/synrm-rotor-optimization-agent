---
type: research_paper
title: "Fast synthesis of permanent magnet assisted synchronous reluctance motors"
authors: "Nicola Bianchi, Hanafy Mahmoud, Silverio Bolognani"
year: "2016"
venue: "IET Electric Power Applications"
doi: "10.1049/iet-epa.2015.0240"
motor_types: ["Synchronous Reluctance", "PM-Assisted Synchronous Reluctance"]
topics: ["analytical design procedure", "rotor geometry synthesis", "flux barrier sizing", "PM demagnetisation", "torque density estimation", "iron rib mechanical design"]
topologies: ["multi-barrier SynRM", "ferrite PM-assisted SynRM"]
source_files: ["raw/papers/IET Electric Power Appl - 2016 - Bianchi - Fast synthesis of permanent magnet assisted synchronous reluctance motors.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: ["eq_bianchi_torque_density", "eq_bianchi_barrier_spacing", "eq_bianchi_kair", "eq_bianchi_iron_path_width", "eq_bianchi_barrier_profile", "eq_bianchi_island_area", "eq_bianchi_rib_force", "eq_bianchi_rib_thickness", "eq_bianchi_pm_effective_flux", "eq_bianchi_pm_width_lost", "eq_bianchi_avg_airgap_flux_density", "eq_bianchi_airgap_flux", "eq_bianchi_airgap_flux_network", "eq_bianchi reluctances", "eq_bianchi_pm_effective_width", "eq_bianchi_pm_total_width", "eq_bianchi_barrier_flux", "eq_bianchi_barrier_stress", "eq_bianchi_stator_mmf_avg", "eq_bianchi_barrier_stress_equal_spacing", "eq_bianchi_demagnetisation_current"]
concepts_updated: ["pmasynrm_synthesis", "flux_barrier_design", "rotor_rib_sizing", "pm_width_selection", "pm_demagnetisation_check"]
motorcad_relevance: "Directly applicable — provides analytical starting-point equations for SynRM/PMA-SynRM rotor geometry that feed into Motor-CAD parametric models. Every equation maps to Motor-CAD rotor geometry parameters."
confidence: Verified
---

# Fast Synthesis of Permanent Magnet Assisted Synchronous Reluctance Motors

## Citation

Bianchi, N., Mahmoud, H., & Bolognani, S. (2016). Fast synthesis of permanent magnet assisted synchronous reluctance motors. *IET Electric Power Applications*, 10(6), 468–479. DOI: [10.1049/iet-epa.2015.0240](https://doi.org/10.1049/iet-epa.2015.0240)

Special Issue: Permanent-Magnet Synchronous Reluctance Machines and their Applications.

## Why This Paper Matters

This paper provides a complete, purely analytical design procedure for sizing both a synchronous reluctance motor (SynRM) and a PM-assisted SynRM (PMA-SynRM) from rated torque and speed requirements. Unlike FEA-driven iterative design, this gives a rapid first-pass geometry — suitable as a starting point for [[optimize_synrm_v4.py]]-style optimisation or as a quick comparison baseline between motor topologies. The procedure covers stator sizing, rotor flux-barrier geometry, iron rib mechanical sizing, PM width selection, and PM demagnetisation checking — all closed-form equations that map directly to [[motorcad_workflow|Motor-CAD]] parametric inputs.

## Problem Statement

There is a gap in practical design knowledge for SynRM/PMA-SynRM machines: given application requirements (torque, speed), how to determine the motor geometry rapidly and analytically, without relying on time-consuming FEA iterations. The paper fills this gap with a step-by-step analytical procedure.

## Machine / Study Context

- **Motor types**: Synchronous Reluctance (SynRM) and Ferrite PM-Assisted SynRM (PMA-SynRM)
- **Typical torque range**: 5–50 N·m (for the torque density factor)
- **Application focus**: Industrial drives, sensorless control applications
- **Stator**: Selected from existing commercial lamination geometries (e.g. MEC 132), 3 slots/pole/phase distributed winding, 4-pole
- **Rotor**: 3 flux barriers per pole (typical range: 2–4 barriers)
- **PM material**: Ferrite (B_rem ≈ 0.35 T) — chosen to avoid rare-earth cost
- **Design example**: T_N = 12.5 N·m, n_N = 5000 rpm, D_e = 200 mm, L_stk = 40 mm

## Method / Theory

The procedure has 8 steps:

1. **Stator sizing** — Torque density factor k_TV relates rated torque to outer volume
2. **Flux barrier end selection** — Equi-spaced equivalent rotor slots, linked to stator slot count
3. **Flux barrier geometry** — k_air coefficient controls saturation balance between rotor and stator; iron path widths computed from d-axis flux density distribution
4. **Barrier profiles** — Based on magnetic field potential lines (analytical curves)
5. **Iron rib sizing** — Mechanical analysis: centrifugal + magnetic force on rotor islands, safety factor 2–3× on tensile strength
6. **PM width selection** — Magnetic network at no load; effective PM width after accounting for rib saturation losses
7. **PM thickness / demagnetisation check** — Magnetic network with stator MMF; ensures PM operating point stays above knee point
8. **FEA verification** — The analytical result is verified and then refined numerically

## Important Equations

### Eq. 1 — Torque Density Factor

$$k_{\rm TV} = \frac{T_n}{D_e^2 \, L_{\rm stk}} \simeq 10 \;\mathrm{N \cdot m / l}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $T_n$ | Rated torque | N·m |
| $D_e$ | Outer stator diameter | m |
| $L_{\rm stk}$ | Stack length | m |
| $k_{\rm TV}$ | Torque density factor | N·m/l |

**Assumptions**: Valid for torque range 5–50 N·m. Range 8–12 N·m/l depending on cooling. Small motors have larger $D_e/D_i$ ratio → higher k_TV.

---

### Eq. 2 — Flux Barrier End Spacing Rule

$$n_r = n_s \pm 4$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $n_s$ | Stator slots per pole pair ($Q_s/p$) | — |
| $n_r$ | Equivalent rotor slots per pole pair | — |

**Assumptions**: Based on Vagati's design rule (Ref [26]). Barrier ends equi-spaced along rotor periphery. Good starting point; not always the absolute minimum ripple solution.

---

### Eq. 3 — Air-Gap Coefficient

$$k_{\rm air} = \frac{\sum_i t_{b_i}}{(D_r - D_{\rm sh})/2}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $t_{b_i}$ | Thickness of $i$-th flux barrier | m |
| $D_r$ | External rotor diameter | m |
| $D_{\rm sh}$ | Shaft diameter | m |

**Assumptions**: $k_{\rm air}$ should be close to stator $k_{\rm air,s} = (p_s - w_t)/p_s$ for balanced saturation. Slightly higher than stator value limits iron losses. Too high → decreased torque and power. Typical value in example: 0.45.

---

### Eq. 4 — Iron Path Width (d-axis flux distribution)

$$w_{r_{pi}} = (1 - k_{\rm air}) \left[\frac{D_r - D_{\rm sh}}{2}\right] \frac{\frac{1}{\theta_{b_{i+1}}^e - \theta_{b_i}^e} \int_{\theta_{b_i}^e}^{\theta_{b_{i+1}}^e} \sin\theta^e \, d\theta^e}{\frac{1}{\pi/2} \int_0^{\pi/2} \sin\theta^e \, d\theta^e}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $\theta_{b_i}^e$ | Electrical angle of $i$-th flux barrier end | rad (electrical) |

**Assumptions**: Iron path width proportional to average flux density in that path. Superscript 'e' denotes electrical angles.

---

### Eqs. 5 & 6 — Flux Barrier Profile (Potential Lines)

$$c = \sin(p\theta) \frac{(2r/D_{\rm sh})^{2p} - 1}{(2r/D_{\rm sh})^p}$$

$$r = \frac{D_{\rm sh}}{2} \left[\frac{c + \sqrt{c^2 + 4\sin^2(p\theta)}}{2\sin(p\theta)}\right]^{1/p}, \quad 0 \le \theta \le \frac{\pi}{p}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $r$ | Radius of point on potential line | m |
| $\theta$ | Angle of point on potential line | rad |
| $p$ | Number of pole pairs | — |
| $c$ | Constant defining specific potential line | — |
| $D_{\rm sh}$ | Shaft diameter | m |

**Assumptions**: Barrier profile follows magnetic field potential lines of the rotor. Each barrier defined by three potential lines (central line + two border lines offset by barrier thickness). Based on analytical solutions from Binns & Lawrenson (Ref [29]).

---

### Eq. 7 — Rotor Island Cross-Section Area

$$S_{\rm isl} = \frac{R_r^2}{2}\left[2\theta_b - \sin(2\theta_b)\right]$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $R_r$ | Outer rotor radius ($D_r/2$) | m |
| $\theta_b$ | Half-angle of flux barrier | rad |
| $S_{\rm isl}$ | Cross-section area of rotor island | m² |

---

### Eq. 8 — Total Force on Rotor Rib

$$F_r = \theta_b D_r L_{\rm stk} \left\{\frac{B^2}{2\mu_0} + \frac{\gamma D_r^2 \omega_m^2 \cos\theta_b}{4}\left[1 - \frac{\sin(2\theta_b)}{2\theta_b}\right]\right\}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $F_r$ | Total force on rib | N |
| $B$ | Air-gap flux density (1–1.2 T assumed) | T |
| $\mu_0$ | Permeability of free space ($4\pi \times 10^{-7}$) | H/m |
| $\gamma$ | Mass density of lamination (~7800) | kg/m³ |
| $\omega_m$ | Rotor mechanical speed | rad/s |
| $D_r$ | Outer rotor diameter | m |
| $L_{\rm stk}$ | Stack length | m |
| $R_c$ | Radius of centre of gravity of island ≈ $D_r \cos\theta_b / 2$ | m |

**Assumptions**: Magnetic pressure $B^2/(2\mu_0)$ with B = 1–1.2 T overestimates magnetic force (conservative). Circular flux barrier geometry. $R_c$ approximation slightly underestimates for rectangular barriers.

---

### Eq. 9 — Iron Rib Thickness

$$\sum t_r = \frac{F_r}{\sigma_r \, L_{\rm orb}}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $\sigma_r$ | Allowable rib stress (150–200 N/mm²) | Pa |
| $L_{\rm orb}$ | Rib length (perpendicular to force direction) | m |

**Assumptions**: Tensile strength of non-oriented steel 400–500 N/mm². Safety factor 2–3× applied → allowable stress 150–200 N/mm². Minimum practical rib thickness = lamination thickness (e.g. 0.4 mm for 0.35 mm lamination).

---

### Eq. 10 — Effective PM Remanence Flux

$$\phi'_{\rm rem} = \phi_{\rm rem} - \phi_{\rm sat} = B_{\rm rem} \, w'_m \, L_{\rm stk}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $\phi_{\rm rem}$ | Total remanence flux of PM ($B_{\rm rem} w_m L_{\rm stk}$) | Wb |
| $\phi_{\rm sat}$ | Flux lost saturating iron ribs | Wb |
| $w'_m$ | Effective PM width (useful for air-gap flux) | m |
| $B_{\rm rem}$ | PM remanence (≈0.35 T for ferrite) | T |

---

### Eq. 11 — PM Width Lost to Rib Saturation

$$\Delta w_m = \frac{B_{\rm sat}}{B_{\rm rem}} \, t_r$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $B_{\rm sat}$ | Saturation flux density in iron ribs (1.8–2 T) | T |
| $t_r$ | Total iron rib thickness | m |
| $\Delta w_m$ | PM width consumed by rib saturation | m |

**Assumptions**: For ferrite ($B_{\rm rem} \approx 0.35$ T): $\Delta w_m \approx 0.6 \, t_r$.

---

### Eq. 12 — Average Air-Gap Flux Density per Barrier

$$B_{g_{i_{\rm avg}}} = \hat{B}_g \frac{\sin(\theta_{b_i}^e) - \sin(\theta_{b_{i-1}}^e)}{\theta_{b_i}^e - \theta_{b_{i-1}}^e}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $\hat{B}_g$ | Peak air-gap flux density at no load (≤0.1 T for ferrite) | T |
| $\theta_{b_i}^e$ | Electrical angle of $i$-th barrier end | rad |

**Assumptions**: Staircase flux distribution approximated as sinusoidal. Ferrite PM → $\hat{B}_g \le 0.1$ T.

---

### Eq. 13 — Air-Gap Flux per Barrier Region

$$\phi_{g_i} = B_{g_{i_{\rm avg}}} (l_{b_i} - l_{b_{i-1}}) L_{\rm stk}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $l_{b_i}$ | Length of $i$-th flux barrier ≈ $\theta_{b_i} D_r$ | m |

---

### Eq. 14 — Air-Gap Flux from Magnetic Network

$$\phi_{g_i} = \frac{\phi'_{\rm rem_i} \, R_{m_i}}{R_{g_i} + R_{m_i}}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $R_{g_i}$ | Reluctance of air-gap portion in front of $i$-th barrier | A·m/Wb |
| $R_{m_i}$ | Reluctance of $i$-th PM | A·m/Wb |

---

### Eq. 15 — Reluctances

$$R_{g_i} = \frac{g}{\mu_0 (l_{b_i} - l_{b_{i-1}}) L_{\rm stk}}, \quad R_{m_i} = \frac{t_{b_i}}{\mu_0 \, l_{m_i} \, L_{\rm stk}}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $g$ | Air-gap length | m |
| $t_{b_i}$ | Thickness of $i$-th flux barrier (= PM thickness in barrier) | m |
| $l_{m_i}$ | Length of PM in $i$-th barrier | m |

---

### Eq. 16 — PM Effective Width (Iterative)

$$w'_{m_i} = \left[\frac{B_{\rm rem} \, t_{b_i}}{B_{\rm rem} \, t_{b_i} - B_{{\rm avg}_i} \, g}\right] \left[w'_{m_{i-1}} + (l_{b_i} - l_{b_{i-1}}) \frac{B_{{\rm avg}_i}}{B_{\rm rem}}\right]$$

**Assumptions**: Solved iteratively from innermost barrier outward. Magnetic network simplified with three assumptions (Fig. 6–7).

---

### Eq. 17 — Total PM Width

$$w_{m_i} = w'_{m_i} + \Delta w_{m_i}$$

---

### Eq. 18 — Barrier Flux Under Stator MMF

$$\phi_{b_i} = \frac{U_{s_i} - U_{s_{i+1}}}{R_{b_i}}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $U_{s_i}$ | Average stator magnetic potential in front of $i$-th barrier | A |
| $R_{b_i}$ | Reluctance of $i$-th flux barrier | A·m/Wb |

**Assumptions**: Air-gap reluctances $R_{g_i}$ neglected (overestimates stress → conservative).

---

### Eq. 19 — PM Stress (Flux Density in Barrier)

$$B_{b_i} = \frac{\mu_0}{t_{b_i}}(U_{s_i} - U_{s_{i+1}})$$

---

### Eq. 20 — Average Stator MMF per Barrier

$$U_{s_i} = \hat{U}_s \frac{\sin(\theta_{b_i}^e) - \sin(\theta_{b_{i-1}}^e)}{\theta_{b_i}^e - \theta_{b_{i-1}}^e}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $\hat{U}_s$ | Peak stator MMF | A |

---

### Eq. 21 — PM Stress with Equal Spacing

$$B_{b_i} = \frac{\mu_0 \, \hat{U}_s}{t_{b_i}} \left[\frac{2\sin(k_i \, \Delta\theta_b^e) [1 - \cos(\Delta\theta_b^e)]}{\Delta\theta_b^e}\right]$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $\Delta\theta_b^e$ | Electrical angle between equivalent rotor slots = $2\pi/n_r$ | rad |
| $k_i$ | Geometry constant (0.5, 1.5, 2.5 if $n_r/2$ even; 1, 2, 3 if $n_r/2$ odd) | — |

---

### Eq. 22 — Maximum Demagnetisation Current

$$I_{\rm demg} = I_n \frac{B_{mo_i} - B_{\rm knee}}{B_{mo_i} - B_{bn_i}}$$

| Symbol | Meaning | Units |
|--------|---------|-------|
| $I_{\rm demg}$ | Maximum current causing irreversible demagnetisation | A |
| $I_n$ | Rated current | A |
| $B_{mo_i}$ | No-load flux density in $i$-th PM | T |
| $B_{bn_i}$ | Stress on $i$-th barrier at rated current | T |
| $B_{\rm knee}$ | Knee point flux density (≈0.1 T for ferrite) | T |

**Assumptions**: Worst case — stator current flux completely opposes PM flux. Superposition applied on REL motor (PMs removed).

---

## Key Design Insights

1. **k_TV ≈ 10 N·m/l** is a robust first-pass sizing factor for SynRM/PMA-SynRM in the 5–50 N·m range. Literature values span 6–13 N·m/l depending on cooling and size.

2. **k_air ≈ 0.45** balances rotor and stator saturation. Slightly higher than stator k_air,s reduces iron losses without degrading PF/efficiency significantly.

3. **Barrier end rule** $n_r = n_s \pm 4$ with equi-spaced ends is a good analytical starting point, not necessarily the ripple minimum. FEA refinement recommended.

4. **Rib sizing** is mechanical: centrifugal + magnetic forces with safety factor 2–3×. Minimum practical thickness = lamination gauge (≈0.4 mm). Inner ribs of shortest barrier can sometimes be omitted.

5. **PM width** is determined by air-gap flux requirements at no load. A significant portion of PM flux is consumed saturating iron ribs ($\Delta w_m \approx 0.6 t_r$ for ferrite).

6. **Demagnetisation check** ensures PM operating point stays above knee point ($B_{\rm knee} \approx 0.1$ T for ferrite) under worst-case stator MMF. Example showed 290% overload margin.

7. **Barrier thickness is the key demagnetisation lever**: increasing $t_{b_i}$ reduces PM stress $B_{b_i}$ (Eq. 21), but too thick → reduced torque and saliency. Trade-off is explicit in the equations.

## Optimization Setup (if applicable)

The paper is not itself an optimisation paper, but provides the analytical starting point for FEA-based optimisation:

- **Design variables**: Flux barrier ends ($\theta_{b_i}^e$), barrier thicknesses ($t_{b_i}$), PM widths ($w_{m_i}$), iron rib thicknesses
- **Objectives**: Average torque maximisation, torque ripple minimisation
- **Constraints**: Demagnetisation margin ($I_{\rm demg} \ge 2 \times I_n$), mechanical rib stress ($\sigma_r \le 150$–200 N/mm²), minimum rib thickness ≥ lamination gauge
- **Example result**: Analytical procedure yields 12.47 N·m average torque with 26% ripple; subsequent FEA optimisation of barrier positions reduced ripple

## Results (numerical)

Design example: T_N = 12.5 N·m, n_N = 5000 rpm, D_e = 200 mm, L_stk = 40 mm, MEC 132 lamination (36 slots, D_i = 125 mm).

| Parameter | Value |
|-----------|-------|
| Flux barrier ends (elec.) | 25.71°, 51.42°, 77.13° |
| Barrier thicknesses | t_b1 = 3 mm, t_b2 = 6 mm, t_b3 = 10 mm |
| Barrier lengths | l_b1 = 28 mm, l_b2 = 56 mm, l_b3 = 84 mm |
| Iron rib thicknesses | t_r1 = 0.8 mm, t_r2 = 1.6 mm, t_r3 = 1.6 mm |
| PM widths | w_m1 = 13 mm, w_m2 = 25 mm, w_m3 = 29 mm |
| PM stress (barrier) | B_b1 = 0.107 T, B_b2 = 0.094 T, B_b3 = 0.069 T |
| PM operating points | B_m1 = 0.200 T, B_m2 = 0.213 T, B_m3 = 0.238 T |
| Demagnetisation current | 290% of rated current |
| Current density (J_s) | 6 A/mm² (continuous duty) |
| Electrical loading (K_s) | 33,500 A/m |
| FEA average torque | 12.47 N·m |
| FEA torque ripple | ~26% (before optimisation) |

## Limitations / Caveats

- **Torque density factor** is empirically derived and depends on cooling, size, and manufacturing. Values outside 5–50 N·m range need recalibration.
- **Equi-spaced barrier ends** are a starting point, not optimal for ripple. Paper acknowledges FEA optimisation is needed.
- **Sinusoidal MMF assumption** ignores slotting harmonics and saturation effects on MMF waveform.
- **Neglecting $R_{g_i}$** in the demagnetisation analysis overestimates PM stress (conservative, but may lead to over-designed PM thickness).
- **Ferrite-specific**: Many numerical assumptions (B_rem = 0.35 T, B_knee ≈ 0.1 T, $\hat{B}_g \le 0.1$ T) are tailored to ferrite PMs. Rare-earth PMs would shift these values significantly.
- **26% torque ripple** before FEA optimisation is high for many applications — the analytical procedure gives geometry, not performance guarantees.
- **Unverified**: The specific lamination data (MEC 132) and commercial availability — marked as from the paper's example, not independently verified.

## Propagation Into Wiki

- [[motorcad_workflow]] — Update with Bianchi's analytical sizing procedure as pre-Motor-CAD input generation
- [[motorcad_parameters]] — Map flux barrier geometry equations to Motor-CAD rotor parametric inputs (barrier positions, thicknesses, PM dimensions)
- [[optimize_synrm_v4]] — Reference as analytical starting point for optimization; k_TV provides initial volume estimate
- [[known_issues]] — Note that torque ripple from analytical procedure (26%) requires FEA refinement
- [[active_tasks]] — If implementing automated SynRM sizing, these equations form the analytical front-end

## Related Pages

- [[motorcad_workflow]]
- [[motorcad_parameters]]
- [[optimize_synrm_v4]]
- [[project_overview]]
