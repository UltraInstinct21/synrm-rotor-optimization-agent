---
type: research_paper
title: "An Overview of High-efficiency Synchronous Reluctance Machines"
authors: "Xuan Li, Yawei Wang, Yuhang Cheng, Dawei Li, Ronghai Qu"
year: 2023
venue: "Chinese Society for Electrical Engineering / CESTEMS"
doi: "10.30941/CESTEMS.2023.00030"
motor_types: [SynRM, PMaSynRM]
topics: [efficiency, torque_density, torque_ripple, high_speed, flux_barrier, optimization, control]
topologies: [transversely_laminated_rotor, axially_laminated_rotor, outer_rotor, segmented_rotor, solid_rotor]
source_files: ["raw/papers/An Overview of High-efficiency Synchronous.md"]
related_projects: [projects/45kW_SynRM]
related_experiments: []
equations_added: [equations/torque_synrm, equations/saliency_ratio_eq]
concepts_updated: [concepts/saliency_ratio, concepts/reluctance_torque, concepts/torque_ripple, concepts/power_factor]
motorcad_relevance: "Provides the theoretical foundation for rotor barrier optimization, winding selection, and efficiency classification. All barrier shape studies and torque/efficiency tradeoffs map directly to MotorCAD rotor geometry parameters."
confidence: Verified
---

# An Overview of High-efficiency Synchronous Reluctance Machines

## Citation

Li, X., Wang, Y., Cheng, Y., Li, D., & Qu, R. (2023). An Overview of High-efficiency Synchronous Reluctance Machines. *Chinese Society for Electrical Engineering*. DOI: [10.30941/CESTEMS.2023.00030](https://doi.org/10.30941/CESTEMS.2023.00030)

## Why This Paper Matters

This is the **single most comprehensive survey** of SynRM design covering every lever available to a motor designer: rotor barrier geometry, winding configuration, material selection, airgap tuning, and control strategies. For a [[projects/45kW_SynRM/overview|45kW SynRM project]], it serves as a decision map — every major design variable and its documented effect on torque, efficiency, and power factor is catalogued with numerical results from 86 references. It also establishes the efficiency classification context (IE4/IE5) that anchors our target specifications.

## Problem Statement

SynRMs offer high torque density, high reliability, and low cost, but suffer from **low power factor** and **torque ripple**. The paper surveys methods to simultaneously maximize average torque, minimize torque ripple, and achieve high efficiency (IE4/IE5 class) while managing the inherent power-factor limitation.

## Machine / Study Context

This is a **literature review** — no single experimental machine. It synthesizes results from dozens of machines ranging from fractional-horsepower appliances to 50 kW EV drives. Key application contexts covered:

- **Industrial variable-speed drives** (ABB, Siemens, REEL products)
- **Electric vehicles** (wide speed range, torque ripple critical)
- **Water pumps and fans** (VSD efficiency classification)
- **Flywheel energy storage** (zero no-load loss advantage)
- **High-speed applications** (>20,000 rpm)

## Method / Theory

The paper is structured around six sections covering:

1. **History**: From Kostko (1923) through axially laminated (1970s) to modern transversely laminated rotors
2. **Operating principle**: [[concepts/dq_theory|d-q axis]] modeling of reluctance torque generation
3. **Torque improvement**: Rotor barrier shape optimization, asymmetric arrangements, control strategies
4. **High-speed design**: Rotor mechanical reinforcement, material selection for high-frequency losses
5. **Efficiency improvement**: Rotor optimization, [[design_guidelines/slot_selection|winding configuration]], [[design_guidelines/airgap|airgap]] tuning, [[concepts/iron_loss|material selection]], [[concepts/copper_loss|control strategies]]
6. **Industrial status**: ABB (IE4), Siemens (+3% over IE3), Okuma (+4-9% over IM)

## Important Equations

### Equation 1: d-axis Voltage (Transient)

$$v_d = R_s i_d + L_d \frac{di_d}{dt} - \omega L_q i_q$$

| Variable | Description | Unit |
|----------|-------------|------|
| $v_d$ | d-axis voltage | V |
| $R_s$ | Stator resistance | Ω |
| $i_d$ | d-axis current | A |
| $L_d$ | d-axis inductance | H |
| $L_q$ | q-axis inductance | H |
| $\omega$ | Electrical angular velocity | rad/s |
| $i_q$ | q-axis current | A |

**Assumptions:** Symmetrical 3-phase, sinusoidal MMF, no saturation coupling between axes (the paper notes cross-saturation is a significant real-world correction).

### Equation 2: q-axis Voltage (Transient)

$$v_q = R_s i_q + L_q \frac{di_q}{dt} + \omega L_d i_d$$

Same variables as Equation 1. Note the paper lists Eq. 1 twice (likely a typo); the q-axis equation is the standard complement.

### Equation 3: Steady-State d-axis Voltage

$$V_d = R_s I_d - \omega L_q I_q$$

### Equation 4: Steady-State q-axis Voltage

$$V_q = R_s I_q + \omega L_d I_d$$

### Equation 5: Electromagnetic Torque

$$T = \frac{3}{2} p (L_d - L_q) i_d i_q = \frac{3}{2} p (\xi - 1) L_q i_d i_q$$

| Variable | Description | Unit |
|----------|-------------|------|
| $T$ | Electromagnetic torque | N·m |
| $p$ | Number of pole pairs | - |
| $L_d$ | d-axis inductance | H |
| $L_q$ | q-axis inductance | H |
| $i_d$ | d-axis current | A |
| $i_q$ | q-axis current | A |
| $\xi$ | Saliency ratio ($L_d/L_q$) | - |

**Normalized form:** $T_{norm} = (\xi - 1) L_q i_d i_q$ (per pole-pair torque). Torque scales linearly with $(\xi - 1)$, making [[concepts/saliency_ratio|saliency ratio]] the primary design target. **Key insight for optimization:** At fixed current magnitude, maximum torque per ampere (MTPA) occurs at $\alpha_i^e = 45°$ when $L_d$ and $L_q$ are constant, but magnetic saturation shifts this angle.

### Equation 6: Saliency Ratio

$$\xi = \frac{L_d}{L_q}$$

| Variable | Description | Unit |
|----------|-------------|------|
| $\xi$ | Saliency ratio | - |
| $L_d$ | d-axis inductance | H |
| $L_q$ | q-axis inductance | H |

Typical values: $\xi = 3\text{–}10$ for practical transversely laminated SynRMs. The paper shows power factor rises steeply with $\xi$ (Fig. 6).

### Equation 7: Power Factor (General Definition)

$$\cos\varphi = \frac{\omega_m T}{\frac{1}{2} m V I}$$

| Variable | Description | Unit |
|----------|-------------|------|
| $\cos\varphi$ | Power factor | - |
| $\omega_m$ | Mechanical angular speed | rad/s |
| $T$ | Torque | N·m |
| $V$ | Peak voltage | V |
| $I$ | Peak current | A |
| $m$ | Phase number | - |

### Equation 8: Power Factor (Derived, SynRM-specific)

$$\cos\varphi = (\xi - 1) \sqrt{\frac{\sin 2\alpha_i^e}{2\left(\xi^2 \cot \alpha_i^e + \tan \alpha_i^e\right)}}$$

| Variable | Description | Unit |
|----------|-------------|------|
| $\xi$ | Saliency ratio | - |
| $\alpha_i^e$ | Current phase angle (angle between current vector and q-axis) | rad or ° |

**Key relationship:** Power factor is fundamentally limited by $\xi$. At $\xi = 5$ and optimal $\alpha_i^e$, PF ≈ 0.6–0.7. Achieving PF > 0.8 typically requires $\xi > 8$ or [[topologies/pmasynrm|PM-assisted]] magnetization. **This equation is critical for [[projects/45kW_SynRM/overview|45kW design]]** — it defines the minimum saliency ratio needed to meet system PF requirements.

## Key Design Insights

### Rotor Barrier Design
- **Barrier shape**: Fluid, rectangular, circular, U-shaped, and hyperbolic shapes all studied. C-type barriers give 2.3% higher torque than U-type due to less saturation at bends.
- **Barrier count**: More barriers = higher parameters to optimize; diminishing returns beyond ~4 layers. See [[design_guidelines/barrier_design]].
- **Asymmetric barriers**: Reduce torque ripple without sacrificing average torque (key for [[concepts/torque_ripple|ripple reduction]]).
- **Segmented rotors**: Allow per-lamination harmonic cancellation — a powerful ripple reduction technique.
- **Zukovski barriers**: Central ribs for mechanical integrity at high speed; barrier shape compensates torque loss.

### Winding Configuration
- **FSCW** (fractional-slot concentrated windings): Higher torque density but lower PF and higher ripple due to rich MMF harmonics.
- **Toroidal windings**: Eliminate even space harmonics while keeping FSCW advantages; wider slot-pole selection.
- **Dual winding with series/parallel switching**: Extends speed range and improves efficiency for wound-field SynRM.

### Airgap
- Larger airgap reduces rotor eddy-current losses and stator losses from spatial harmonics.
- But requires higher current for same torque → higher copper losses.
- **Tradeoff**: Airgap must be optimized per application, not minimized blindly. See [[design_guidelines/airgap]].

### Material Selection
- Steel grade has **9% efficiency impact** (NO20 vs M600-100A at same geometry).
- **CoFe**: Better at low speed (higher $B_{sat}$). **SiFe**: Better at high speed (lower iron loss).
- Tradeoffs between silicon content, saturation, and loss must be evaluated at the operating point.

### Control Strategies
- **MTPA** (Maximum Torque Per Ampere): Standard for torque maximization.
- **MPPT** (Minimum Power Per Torque): Identical to max-efficiency operation; achieved via signal injection without motor parameter dependency.
- **Loss minimization controllers**: Account for cross-saturation; optimize d-q current split dynamically.
- **Neural network / fuzzy control**: Handle nonlinear relationships; achieve high efficiency even in transient states.

## Optimization Setup (if applicable)

This paper surveys optimization approaches rather than presenting one:

| Method | Reference | Objective | Notes |
|--------|-----------|-----------|-------|
| Stochastic optimization + FEA | [57] | Torque density, losses, ripple | Automated procedure, MOGA |
| Two-step MOGA | [58] | Pareto front (torque vs ripple) | Time-efficient multi-objective |
| Multi-objective GA | [59] | Max torque, min ripple | IE5 achieved; IE4 manufacturable |
| MMFD (Modified Method of Feasible Direction) | [60] | Drive system efficiency | 92.2% weighted efficiency for 5.5 kW |
| Nelder-Mead | [65] | Torque/volume ratio | Handles non-smooth/noisy objectives |
| Multi-objective DE (Differential Evolution) | [86] | High-speed rotor at 20,000 rpm | Barrier geometry speed-dependent |
| Taguchi method | [44] | Outer rotor optimization | Simpler, fewer runs |

**For [[projects/45kW_SynRM/overview|our optimization]]**: The Nelder-Mead and MOGA approaches are most directly applicable. The paper confirms that barrier geometry parameters (width ratio, number of barriers, iron segment thickness) are the primary design variables.

## Results (Numerical)

| Metric | Value | Source |
|--------|-------|--------|
| Efficiency improvement (steel grade) | 9% (NO20 vs M600-100A) | [72] |
| SynRM vs IE3 IM (drive system) | SynRM superior at matched power level | [60] |
| 5.5 kW RSM weighted efficiency | 92.2% (IE4) | [60] |
| New SynRM at 90% rated speed | 90.7% efficiency (IE5) | [65] |
| C-type vs U-type torque advantage | +2.3% | [39] |
| Solid rotor improvement (drilled + jacket) | +10% average torque vs classical | [43] |
| Siemens SynRM | +14% over IE1, +3% over IE3 | [24] |
| Okuma PMaSynRM | +4–9% over IM | [23] |
| ABB SynRM | IE4 class (4-pole, <200 kW) | [21] |

## Limitations / Caveats

1. **Literature review only** — no original experimental validation; numerical results are aggregated from cited works with different test conditions.
2. **Power factor remains low** — the paper acknowledges this as the primary limitation. No breakthrough beyond PM-assisted topologies is presented.
3. **High-speed SynRM is "almost unexplored"** — the Section V coverage is thin; design guidance for >20 kHz operation is limited.
4. **Control results are simulation-heavy** — many control strategies lack experimental validation at scale.
5. **Cross-saturation effects** are noted as significant but not systematically quantified across the surveyed designs.
6. **Manufacturing complexity** of advanced topologies (asymmetric, segmented, toroidal) is mentioned but not cost-analyzed.

## Propagation Into Wiki

- [[concepts/saliency_ratio]] — Update with Eq. 6 and the PF-ξ relationship from Eq. 8; add design implications
- [[concepts/reluctance_torque]] — Update with torque equation (Eq. 5) and MTPA angle considerations
- [[concepts/torque_ripple]] — Add barrier-based mitigation methods (asymmetric, segmented, auxiliary slots)
- [[concepts/power_factor]] — Update with derived PF equation (Eq. 8) and the ξ-PF curve
- [[design_guidelines/barrier_design]] — Add barrier shape comparison (C vs U), number-of-barriers tradeoff, Zukovski barriers for high-speed
- [[design_guidelines/airgap]] — Document the airgap tradeoff (loss reduction vs copper loss increase)
- [[design_guidelines/slot_selection]] — FSCW vs toroidal winding tradeoffs
- [[heuristics/torque_ripple_reduction]] — Add asymmetric barriers, segmented rotors, auxiliary slots
- [[heuristics/saliency_improvement]] — Add barrier count and shape optimization results
- [[equations/torque_synrm]] — Link to Eq. 5 with variable definitions
- [[equations/saliency_ratio_eq]] — Link to Eq. 6
- [[topologies/synrm]] — Update with industrial status (ABB, Siemens, Okuma) and efficiency classification context

## Related Pages

- [[topologies/synrm]]
- [[topologies/pmasynrm]]
- [[concepts/saliency_ratio]]
- [[concepts/reluctance_torque]]
- [[concepts/torque_ripple]]
- [[concepts/power_factor]]
- [[design_guidelines/barrier_design]]
- [[design_guidelines/airgap]]
- [[design_guidelines/slot_selection]]
- [[equations/torque_synrm]]
- [[equations/saliency_ratio_eq]]
- [[heuristics/torque_ripple_reduction]]
- [[heuristics/saliency_improvement]]
- [[optimization/nsga2]]
- [[projects/45kW_SynRM/overview]]
- [[research/papers/synrm_barrier_review_2025]]
- [[research/papers/topology_optimization_synrm]]
- [[research/papers/review_high_speed_synrm]]
