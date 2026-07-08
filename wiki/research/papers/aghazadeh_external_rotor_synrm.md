---
type: research_paper
title: "Sizing and detailed design procedure of external rotor synchronous reluctance machine"
authors: "Hadi Aghazadeh, Ebrahim Afjei, Alireza Siadatan"
year: 2019
venue: "IET Electric Power Applications"
doi: "10.1049/iet-epa.2018.5802"
motor_types: ["External Rotor Synchronous Reluctance Machine (Ex-SynRM)"]
topics: ["sizing", "analytical design", "rotor geometry optimization", "torque ripple reduction", "insulation ratio", "FEA validation", "thermal analysis", "structural analysis", "prototype testing"]
topologies: ["external rotor", "distributed winding", "3-phase"]
source_files: ["raw/papers/IET Electric Power Appl - 2019 - Aghazadeh - Sizing and detailed design procedure of external rotor synchronous reluctance.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: ["Q = C₀(D²so × L) × ns", "Co = 11 × Bavg × ac × kw × 10⁻³", "ac = Iz × Z / (π × Dso)", "Bavg = p × φm / (π × Dso × L)", "τ = π × Dso / p", "kfill = Acu / Ass", "Q = Po / (η × p.f)", "Dso = p × L / π", "Eph = (√6/π) × kvo × Vo", "Iph = Pin / (3 × Eph × p.f × η)", "kd = sin(δ/2) / (qs × cos(δ/(2qs)))", "δ = π / (3 × qs)", "kw = kd × kc × ks", "Tph = Eph / (4.44 × fs × φm × Kw)", "φm = Bav × τ × L", "az = Iph / J", "Ass = (Zs × az) / Kfill", "bts = (p × φm) / (Bth × Ss × Li)", "Li = kst × L", "hcs = (φm/2) / (Bcmax × Li)", "Ass(hs) = ½ × (bs1 + bs2) × hs", "bs1(hs) = ((Dso - 2hs1 - 2hs2 - 2hs) × π) / Ss - bts", "bs2 = ((Dso - 2hs1 - 2hs2) × π) / Ss - bts", "a × h²s + b × hs + c = 0", "Tem = (3/2) × p × (Lmd - Lmq) × imd × imq", "kwq = la / ly", "ns - nr = ±4", "αi = ½ × (2i-1) × αm", "αm = (π/p - 2β) / (2nb + 1)", "Si+1/Si = fdi+1/fdi", "Wbi/Wb1 = (Δfi/Δf1)²", "Δfi = fqi+1 - fqi", "ly = ΣSi = ((Dro/2) - (Dso/2) - g) / (1 + kwq)", "la = ΣWbi = ((Dro/2) - (Dso/2) - g) / (1 + 1/kwq)"]
concepts_updated: ["insulation ratio in q-axis", "rotor slot pitch angle controller", "barrier end angle", "flux barrier shaping", "stator sizing procedure", "output coefficient", "specific magnetic loading", "specific electric loading"]
motorcad_relevance: "Directly applicable for [[SynRM]] motor design in [[PyMotorCAD]]. Provides complete sizing workflow from power rating to geometry. Equations (1)-(27) for stator sizing can be implemented as design tool. Rotor barrier shaping methodology (equations 28-37) with insulation ratio optimization is core to [[SynRM]] rotor design. Multi-objective optimization framework for average torque vs torque ripple is directly implementable. The external rotor topology is particularly relevant for [[e-bike]] and [[in-wheel motor]] applications."
confidence: Verified
---

# Sizing and detailed design procedure of external rotor synchronous reluctance machine

## Citation

Aghazadeh, H., Afjei, E., & Siadatan, A. (2019). Sizing and detailed design procedure of external rotor synchronous reluctance machine. *IET Electric Power Applications*, 13(7). DOI: [10.1049/iet-epa.2018.5802](https://doi.org/10.1049/iet-epa.2018.5802)

## Why This Paper Matters

This paper presents one of the few comprehensive analytical design procedures specifically for [[External Rotor SynRM]], filling a gap in literature where most Ex-SynRM studies focus on five-phase concentrated winding configurations. The key innovation is the **insulation ratio in the q-axis** ($k_{wq}$), a macroscopic parameter that collapses the multi-parameter rotor geometry optimization into a single-variable search, dramatically reducing FEA simulation time. The complete stator-to-rotor sizing workflow—from power rating to verified prototype—makes this directly implementable as a [[MotorCAD]] design procedure.

## Problem Statement

Designing an optimal synchronous reluctance machine requires navigating a vast combinatorial space of rotor barrier shapes and stator geometries. The research addresses three interconnected challenges:

1. **Dimensional coupling**: Stator geometry must be coordinated with rotor anisotropy for torque production, but analytical design procedures for external rotor Ex-SynRM are scarce
2. **Parameter explosion**: Rotor flux barrier design involves numerous geometric parameters that make optimization computationally expensive
3. **Torque ripple**: Barrier number and end-point positioning relative to stator slots critically affect torque quality, but the interaction is poorly understood for Ex-SynRM

## Machine / Study Context

| Parameter | Value |
|-----------|-------|
| Motor type | External rotor synchronous reluctance machine |
| Application | Electric bicycle (in-wheel direct drive) |
| Rated power | 250 W |
| Rated speed | 520 rpm |
| Number of pole pairs | 3 (6 poles) |
| Stator outer diameter | 120 mm |
| Stack length | 50 mm |
| Air gap | 0.4 mm |
| Stator slots | 36 ($q_s$ = 2 slots/pole/phase) |
| Rotor barriers per pole | 2 |
| Winding type | Distributed overlapping (full-pitch) |
| Connection | Delta |
| DC link voltage | 48 V |
| Lamination material | M-27 non-oriented steel (0.36 mm) |
| Prototype fabricated | Yes |

## Method / Theory

### Design Workflow

The paper follows a sequential design methodology:

1. **Sizing Phase** (Eqs. 1-8): Estimate motor volume from output power, speed, and magnetic/electric loadings
2. **Stator Design** (Eqs. 9-27): Calculate winding specifications and slot geometry using parallel-sided tooth / tapered slot topology
3. **Rotor Barrier Shaping** (Eqs. 28-37): Use MMF-based analytical method with insulation ratio to size barriers
4. **Optimization**: Multi-objective FEA optimization of rotor slot pitch angle controller β
5. **Validation**: Thermal, structural, and experimental verification

### Key Innovation: Insulation Ratio

The **insulation ratio in the q-axis** ($k_{wq}$) is defined as the ratio of total insulation layer thickness ($l_a$) to total iron segment thickness ($l_y$) along the q-axis:

$$k_{wq} = \frac{l_a}{l_y}$$

This single parameter controls the relative widths of flux barriers and iron segments, reducing the optimization problem from many geometric variables to one. The optimal value is found through limited FEA sensitivity analysis (optimal ≈ 0.6 for this geometry).

### Barrier Shaping Rules

The method assumes sinusoidal stator MMF distribution and derives barrier dimensions from two rules:

1. **Iron segment sizing**: Width proportional to average d-axis MMF over the segment
2. **Barrier sizing**: Width proportional to squared differential q-axis MMF (equal permeance assumption)

### Rotor Slot Pitch Angle Controller (β)

An additional parameter β positions the barrier end points relative to the q-axis. The relationship $\beta = \alpha_m$ (rotor slot pitch) produces lowest torque ripple by ensuring barrier ends do not align with stator slot openings.

## Important Equations (with normalized form, original notation, variables, units, assumptions)

### Sizing Equations

**Equation 1 — Output Power**
$$Q = C_o (D_{so}^2 \cdot L) \cdot n_s$$
- $Q$: Output power (W)
- $C_o$: Output coefficient
- $D_{so}$: Stator outer diameter (m)
- $L$: Stack length (m)
- $n_s$: Synchronous speed (rps)
- Assumption: Constant output coefficient for given loading conditions

**Equation 2 — Output Coefficient**
$$C_o = 11 \cdot B_{avg} \cdot ac \cdot k_w \cdot 10^{-3}$$
- $B_{avg}$: Specific magnetic loading (T)
- $ac$: Specific electric loading (A·turns/m)
- $k_w$: Winding factor

**Equation 3 — Specific Electric Loading**
$$ac = \frac{I_z \cdot Z}{\pi \cdot D_{so}}$$
- $I_z$: Current per conductor (A)
- $Z$: Total number of conductors

**Equation 4 — Specific Magnetic Loading**
$$B_{avg} = \frac{p \cdot \phi_m}{\pi \cdot D_{so} \cdot L} = \frac{\phi_m}{\tau \cdot L}$$
- $p$: Number of pole pairs
- $\phi_m$: Flux per pole (Wb)
- $\tau$: Pole pitch (m)

**Equation 5 — Pole Pitch**
$$\tau = \frac{\pi \cdot D_{so}}{p}$$

**Equation 6 — Slot Fill Factor**
$$k_{fill} = \frac{A_{cu}}{A_{ss}}$$
- $A_{cu}$: Total copper area (m²)
- $A_{ss}$: Stator slot area (m²)
- Typical range: 0.3-0.4 (distributed), up to 0.6 (concentrated)

**Equation 7 — kVA Rating**
$$Q = \frac{P_o}{\eta \cdot p.f}$$
- $P_o$: Rated power (kW)
- $\eta$: Efficiency
- $p.f$: Power factor

**Equation 8 — Stator Outer Diameter** (when $L/\tau = 1$)
$$D_{so} = \frac{p \cdot L}{\pi}$$

### Electrical Design Equations

**Equation 9 — Phase Voltage** (delta connection)
$$E_{ph} = \frac{\sqrt{6}}{\pi} \cdot k_{vo} \cdot V_o$$
- $k_{vo}$: Converter factor (0.8-1.0)
- $V_o$: DC link voltage (V)

**Equation 10 — Phase Current**
$$I_{ph} = \frac{P_{in}}{3 \cdot E_{ph} \cdot p.f \cdot \eta}$$

**Equation 11 — Distribution Factor**
$$k_d = \frac{\sin(\delta/2)}{q_s \cdot \cos(\delta/(2q_s))}$$
- $\delta$: Slot-pitch in electrical degrees
- $q_s$: Slots per pole per phase

**Equation 12 — Slot-Pitch (Electrical)**
$$\delta = \frac{\pi}{3 \cdot q_s}$$

**Equation 13 — Winding Factor**
$$k_w = k_d \cdot k_c \cdot k_s$$
- $k_c$: Chording factor (= 1 for full-pitch)
- $k_s$: Skew factor (= 1 for no skew)

**Equation 14 — Turns per Phase**
$$T_{ph} = \frac{E_{ph}}{4.44 \cdot f_s \cdot \phi_m \cdot K_w}$$
- $f_s$: Supply frequency (Hz)

**Equation 15 — Flux per Pole**
$$\phi_m = B_{av} \cdot \tau \cdot L$$

**Equation 16 — Conductor Cross-Section**
$$a_z = \frac{I_{ph}}{J}$$
- $J$: Current density (A/m²), typical 2-5 A/mm²

**Equation 17 — Slot Area**
$$A_{ss} = \frac{Z_s \cdot a_z}{K_{fill}}$$
- $Z_s$: Conductors per slot

### Stator Geometry Equations

**Equation 18 — Tooth Width**
$$b_{ts} = \frac{p \cdot \phi_m}{B_{th} \cdot S_s \cdot L_i}$$
- $B_{th}$: Tooth flux density (T), typically 1.7 T
- $S_s$: Number of stator slots
- $L_i$: Useful stator length (m)

**Equation 19 — Useful Stator Length**
$$L_i = k_{st} \cdot L$$
- $k_{st}$: Stacking factor (0.95)

**Equation 20 — Core Height**
$$h_{cs} = \frac{\phi_m/2}{B_{cmax} \cdot L_i}$$
- $B_{cmax}$: Maximum core flux density (T), typically 1.5 T

**Equation 21 — Tapered Slot Area**
$$A_{ss}(h_s) = \frac{1}{2}(b_{s1} + b_{s2}) \cdot h_s$$

**Equation 22 — Slot Width at Bottom**
$$b_{s1}(h_s) = \frac{(D_{so} - 2h_{s1} - 2h_{s2} - 2h_s) \cdot \pi}{S_s} - b_{ts}$$

**Equation 23 — Slot Width at Top**
$$b_{s2} = \frac{(D_{so} - 2h_{s1} - 2h_{s2}) \cdot \pi}{S_s} - b_{ts}$$

**Equation 24 — Quadratic for Slot Height**
$$a \cdot h_s^2 + b \cdot h_s + c = 0$$
where:
- $a = \pi/S_s$
- $b = -b_{s2}$
- $c = A_{ss}$

### Rotor Design Equations

**Equation 28 — Electromagnetic Torque**
$$T_{em} = \frac{3}{2} p (L_{md} - L_{mq}) i_{md} i_{mq} = \frac{3}{2} p (L_{md} - L_{mq}) I_m \sin(2\gamma)$$
- $L_{md}, L_{mq}$: d- and q-axis magnetizing inductances (H)
- $i_{md}, i_{mq}$: d- and q-axis currents (A)
- $I_m$: Stator current amplitude (A)
- $\gamma$: Current angle (°)
- Maximum torque at $\gamma = 45°$ (unsaturated), ~55° (saturated)

**Equation 29 — Insulation Ratio in q-axis**
$$k_{wq} = \frac{l_a}{l_y} = \frac{(D_{ro}/2) - (D_{so}/2) - g - \sum_{k=1}^{nb+1} S_k}{\sum_{k=1}^{nb+1} S_k}$$
- $l_a$: Total insulation layer thickness (m)
- $l_y$: Total iron segment thickness (m)
- $D_{ro}$: Rotor outer diameter (m)
- $g$: Air-gap length (m)
- $S_i$: Width of i-th iron segment (m)
- $n_b$: Number of barriers per pole
- Optimal value: ≈ 0.6

**Equation 30 — Stator-Rotor Slot Relationship**
$$n_s - n_r = \pm 4$$
- $n_s$: Stator slots per pole pair
- $n_r$: Rotor slots (barrier ends) per pole pair
- For 36 stator slots (12/pole pair): $n_r = 8$ → 2 barriers per pole

**Equation 31 — Barrier End Angle**
$$\alpha_i = \frac{1}{2}(2i-1) \cdot \alpha_m, \quad i = 1, ..., n_b$$

**Equation 32 — Rotor Slot Pitch**
$$\alpha_m = \frac{(\pi/p - 2\beta)}{(2n_b + 1)}$$
- $\beta$: Rotor slot pitch angle controller
- Optimal: $\beta = \alpha_m$ for minimum torque ripple

**Equation 33 — Iron Segment Sizing Rule**
$$\frac{S_{i+1}}{S_i} = \frac{f_{di+1}}{f_{di}}, \quad i = 1, ..., n_b$$
- $f_{di}$: Average d-axis MMF over i-th segment

**Equation 34 — Barrier Width Rule** (equal permeance)
$$\frac{W_{bi}}{W_{b1}} = \left(\frac{\Delta f_i}{\Delta f_1}\right)^2, \quad i = 2, ..., n_b$$
- $W_{bi}$: Width of i-th flux barrier in q-axis (m)
- $\Delta f_i$: Differential average q-axis MMF over i-th barrier

**Equation 35 — Differential MMF**
$$\Delta f_i = f_{qi+1} - f_{qi}$$

**Equation 36 — Total Iron Segments**
$$l_y = \sum_{i=1}^{nb+1} S_i = \frac{(D_{ro}/2) - (D_{so}/2) - g}{1 + k_{wq}}$$

**Equation 37 — Total Insulation Layers**
$$l_a = \sum_{i=1}^{nb} W_{bi} = \frac{(D_{ro}/2) - (D_{so}/2) - g}{1 + (1/k_{wq})}$$

## Key Design Insights

1. **Insulation ratio collapses parameter space**: The $k_{wq}$ parameter links all barrier and segment widths, reducing rotor optimization to a single-variable FEA sweep. For this geometry, optimal $k_{wq} \approx 0.6$.

2. **Rotor slot pitch controller β is critical for torque ripple**: Setting $\beta = \alpha_m$ positions barrier ends between stator slot openings, reducing torque ripple from 49.4% to 29.9%. Further optimization achieves 19.7% ripple with only 5% torque reduction.

3. **Barrier number must match stator slots**: The rule $n_s - n_r = \pm 4$ ensures proper MMF harmonic interaction. For 36 stator slots (12/pole pair), 2 barriers per pole (8 rotor "slots"/pole pair) is optimal.

4. **Distributed winding preferred over concentrated**: Distributed winding produces lower MMF harmonics, reducing torque ripple and core losses despite lower slot fill factor.

5. **Air gap trade-off**: Smaller air gap increases $L_d$ (higher torque) but also increases Carter's factor and torque ripple. 0.4 mm provides good compromise.

6. **External rotor advantages**: Wider stator slot area → higher torque density; rotor directly couples to wheel → eliminates gearbox; no rotor cage → cooler rotor.

7. **Saturation shifts optimal current angle**: Maximum torque occurs at $\gamma \approx 55°$ (not 45°) due to inductance variation with saturation.

8. **Power factor limitation**: Achieved PF of 0.64 is inherent to SynRM, requiring oversizing of inverter by ~1.56×.

## Optimization Setup (if applicable)

**Multi-objective optimization** with two objectives:
- Maximize average torque
- Minimize torque ripple

**Design variables**:
- Insulation ratio $k_{wq}$ (pre-optimized to 0.6 via sensitivity analysis)
- Rotor slot pitch angle controller β
- Air gap length g

**Optimization method**: FEA-based with weighted sum objective function (50% weight each)

**Pareto front results**:
- $\beta = 0.5\alpha_m$: 4.167 Nm, 49.4% ripple (high ripple)
- $\beta = \alpha_m$: 4.468 Nm, 29.9% ripple (good compromise)
- Optimal design: 4.242 Nm, 19.7% ripple (best ripple)

## Results (numerical)

### FEM Simulation Results

| Parameter | Value |
|-----------|-------|
| Average torque (optimal) | 4.242 Nm |
| Torque ripple (optimal) | 19.677% |
| Average torque (β = αm) | 4.468 Nm |
| Torque ripple (β = αm) | 29.858% |
| Air gap flux density THD (β = 0.5αm) | 32.33% |
| Air gap flux density THD (β = αm) | 28.53% |
| Optimal insulation ratio | 0.6 |
| Optimal air gap | 0.4 mm |

### Inductance Results (Locked Rotor Test)

| Parameter | Value |
|-----------|-------|
| $L_d$ (d-axis inductance) | 33.15 mH |
| $L_q$ (q-axis inductance) | 11.65 mH |
| Saliency ratio ($L_d/L_q$) | 2.85 |

### Experimental Results (250 W Prototype)

| Parameter | Value |
|-----------|-------|
| Average torque | 4.11 Nm |
| Torque ripple (experimental) | 4.2% |
| Efficiency | 81% |
| Power factor | 0.64 |
| Total losses | 57 W |
| Copper losses | 49 W (86% of total) |
| Core losses | 6.25 W |
| Friction & windage | 1.82 W |
| Max torque current angle | ~55° |

### Thermal & Structural Analysis

| Parameter | Value |
|-----------|-------|
| Ambient temperature | 20°C |
| Max stator tooth flux density | 1.66 T (at rated current) |
| Rotor max deformation | 0.7 µm |
| Rotor material | M-27 non-oriented steel |
| Thermal conductivity | 25 W/(m·°C) |
| Specific heat capacity | 490 J/(kg·°C) |
| Mass density | 7600 kg/m³ |

### Experimental vs FEM Comparison

- Average torque: 3% lower than FEM (due to 3D leakage from fabrication)
- Torque ripple: 4.2% vs 19.1% FEM (mechanical damping from housing/shaft)
- Inductance: Slight differences from measurement inaccuracy

## Limitations / Caveats

1. **Sinusoidal MMF assumption**: The barrier sizing method assumes ideal sinusoidal stator MMF, which doesn't capture harmonic effects that cause torque ripple
2. **2D FEA only**: 3D effects (end windings, axial leakage) not fully captured; prototype showed 3% torque reduction from 3D effects
3. **Single operating point**: Thermal analysis assumes steady-state at rated conditions; transient behavior not analyzed
4. **Low power factor**: 0.64 PF is inherent limitation of SynRM, requires oversized inverter
5. **Copper loss dominated**: 86% of losses are copper losses, suggesting thermal management is critical for continuous operation
6. **Fixed barrier number**: Method selects barrier number from slot relationship (Eq. 30) rather than optimizing it
7. **No field weakening analysis**: Design doesn't address constant power speed range capability
8. **Manufacturing sensitivity**: Small deviations in fabrication affect performance; 3D leakage not predictable from 2D model

## Propagation Into Wiki (list pages to update with [[wikilinks]])

- [[SynRM]] — Add external rotor variant, sizing procedure, insulation ratio concept
- [[External Rotor SynRM]] — New page or section with design methodology
- [[Motor Sizing]] — Add equations (1)-(8) for power-to-volume relationship
- [[Stator Design]] — Add tapered slot geometry calculations (equations 9-27)
- [[Rotor Barrier Design]] — Add insulation ratio method, barrier shaping rules (equations 28-37)
- [[Torque Ripple Reduction]] — Add rotor slot pitch controller β optimization
- [[Insulation Ratio]] — New concept page explaining kwq parameter
- [[E-bike Motor Design]] — Add Ex-SynRM as viable topology
- [[In-Wheel Motor]] — Add external rotor SynRM application
- [[FEA Validation]] — Add comparison methodology between analytical and experimental results

## Related Pages ([[wikilinks]])

- [[Synchronous Reluctance Machine]]
- [[Motor Design Methodology]]
- [[Magnetic Loading]]
- [[Electric Loading]]
- [[Winding Factor]]
- [[Saliency Ratio]]
- [[Flux Barrier Design]]
- [[MMF Distribution]]
- [[FEA Analysis]]
- [[Thermal Analysis]]
- [[Structural Analysis]]
- [[Prototype Testing]]
- [[Torque Ripple]]
- [[Power Factor Optimization]]
- [[Lamination Material Properties]]
