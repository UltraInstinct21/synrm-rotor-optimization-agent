---
type: research_paper
title: "Design of Rotors for Synchronous Reluctance Motor: Analytical Treatment and Optimization"
authors: "Svetlana Orlova, Vladislav Pugachov, Anton Rassõlkin, Ants Kallaste, Toomas Vaimann"
year: "~2019"
venue: "Conference paper (likely RTUCON or IWED)"
doi: ""
motor_types: [SynRM]
topics: [rotor_topology_comparison, saliency_ratio, pole_coverage_optimization, magneto_isolated_poles, evolutionary_optimization, efficiency_mapping]
topologies: [salient_pole, transversally_laminated_anisotropy, magneto_isolated_poles, axially_laminated_anisotropy]
source_files: ["raw/papers/Design of Rotors for SRM Analytical Treatment and Optimization Acknowledgements.md"]
related_projects: [motor-deepagent]
related_experiments: []
equations_added: [synrm_electromagnetic_torque_voltage, torque_mmflux, pole_coverage_coefficient, motor_efficiency_definition]
concepts_updated: [SynRM_rotor_topologies, saliency_ratio, pole_coverage, magneto_isolated_poles, evolutionary_strategy_optimization]
motorcad_relevance: "High — pole coverage coefficient and rotor topology selection directly applicable to MotorCAD rotor geometry setup; magneto-isolated pole concept offers alternative topology for SynRM optimization"
confidence: Verified
---

# Design of Rotors for Synchronous Reluctance Motor: Analytical Treatment and Optimization

## Citation
Orlova, S., Pugachov, V., Rassõlkin, A., Kallaste, A., and Vaimann, T., "Design of Rotors for Synchronous Reluctance Motor: Analytical Treatment and Optimization," Institute of Physical Energetics / Tallinn University of Technology, ~2019. Supported by European Regional Development Fund (No. 1.1.1.2/VIAA/1/16/173) and Estonian Research Council grant PUT1260.

## Why This Paper Matters
Provides a systematic analytical comparison of four SynRM rotor topologies with experimental validation on a 10.5 kW machine. The key contribution is demonstrating that **magneto-isolated poles** (a relatively unexplored topology) can approach the performance of the established transversally laminated anisotropy (TLA) rotor after optimization. The [[pole_coverage_coefficient]] optimization methodology and the topology selection framework are directly applicable to [[SynRM_design]] and [[PyMotorCAD]] rotor geometry sweeps.

## Problem Statement
SynRM rotor design involves selecting among competing topologies — salient pole, axially laminated, transversally laminated, and magneto-isolated poles — each with different saliency, manufacturability, and torque characteristics. The paper aims to: (1) analytically compare these topologies' influence on d/q-axis inductance and saliency ratio; (2) numerically optimize the best candidates using an evolutionary strategy; and (3) experimentally validate the best design on a real test bench.

## Machine / Study Context
- **Machine type:** 3-phase [[SynRM]]
- **Stator core length:** 0.156 m
- **Stator inner diameter:** 0.136 m
- **Stator outer diameter:** 0.219 m
- **Number of slots:** 36
- **Air-gap height:** 0.5 mm
- **Rotor inner diameter:** 0.04 m
- **Rotor outer diameter:** 0.135 m
- **Frame:** 132 MA
- **Rated power:** 10.5 kW
- **Rated current:** 22 A
- **Rated speed:** 1500 rpm
- **Power factor (cosφ):** 0.6
- **Moment of inertia:** 0.048 kg·m²
- **FEA tool:** 2D finite element method

## Method / Theory

### Rotor Topology Taxonomy
Four rotor topologies are analyzed (Fig. 1 in paper):

| Type | Topology | Key Feature |
|------|----------|-------------|
| Type 1 | [[salient_pole_rotor]] | Simple but poor saliency, torque, PF |
| Type 2 | [[transversally_laminated_anisotropy]] | Most widely applied; punched laminations with thin ribs |
| Type 3 | [[magneto_isolated_poles]] | Iron cylinder divided by radial-axial gaps into sectors |
| N/A | [[axially_laminated_anisotropy]] | Best performance but difficult/expensive manufacturing — excluded from optimization |

### Saliency Principle
SynRM torque is proportional to the difference between d-axis and q-axis inductances. The [[saliency_ratio]] ξ = x_d/x_q determines torque capability — higher ξ means higher reluctance torque. For maximum torque, x_d must be maximized while x_q is minimized.

### Magneto-Isolated Pole Concept (Type 3)
The novel topology replaces radial poles with circumferential segments. The rotor is an iron cylinder divided by narrow radial-axial gaps into separate sectors (number equal to pole count). Key advantage: the air gap for magnetic flux along the transverse (q) axis is much larger than along the longitudinal (d) axis, naturally creating high saliency. When MMF components F_ad and F_aq are equal, flux Ф^d is considerably less than flux Ф^q, producing torque.

### Pole Coverage Coefficient Optimization
The influence of rotor tooth sizes on SynRM performance is captured by the [[pole_coverage_coefficient]]:
- **Type 1 (salient pole):** Maximum torque at α_τ = 0.5 (equal tooth and slot pitch angles)
- **Type 3 (magneto-isolated poles):** Maximum torque at α_τ = 0.85–0.9, with tooth height 0.035–0.040 m

### Optimization Method
An [[evolutionary_strategy]] was applied, operating with real-number vectors. The algorithm performs: mutation (adding normally distributed random variables with self-adapting parameters) → crossing to obtain descendants → selection of best individuals from parents+descendants without repetition. The stator was kept constant; only rotor geometry was optimized.

## Important Equations

### Eq. (1): SynRM Electromagnetic Torque (Voltage-Based)
$$T_{em} = \frac{m \cdot p \cdot U^2}{2 \cdot \omega} \cdot \left(\frac{1}{x_q} - \frac{1}{x_d}\right) \cdot \sin 2\gamma$$

**Variables:** m — number of phases; p — number of pole pairs; U — phase voltage [V]; ω — angular frequency of armature current [rad/s]; x_d — direct-axis synchronous reactance [Ω]; x_q — quadrature-axis synchronous reactance [Ω]; γ — load angle between supply voltage and fundamental no-load EMF [rad]
**Normalized form:** $\hat{T}_{em} \propto \left(\frac{1}{\xi_q} - \frac{1}{\xi_d}\right) \sin 2\gamma$ where ξ = x/x_base
**Assumptions:** Sinusoidal MMF distribution; steady-state; balanced 3-phase supply; no saturation coupling.

### Eq. (2): Electromagnetic Torque (MMF-Flux Form)
$$T_{em} = F_{ad}\Phi_q - F_{aq}\Phi_d$$

**Variables:** F_ad — d-axis component of stator MMF [A·turns]; F_aq — q-axis component of stator MMF [A·turns]; Φ_d — direct-axis magnetic flux [Wb]; Φ_q — quadrature-axis magnetic flux [Wb]
**Assumptions:** Fundamental harmonic only; interaction between MMF and flux components produces torque.
**Key insight:** For magneto-isolated poles, when F_ad ≈ F_aq, the air gap along q-axis is much larger than along d-axis, so Φ_q >> Φ_d, producing substantial torque even with modest MMF.

### Eq. (3): Pole Coverage Coefficient
$$\alpha_{\tau} = \frac{\alpha_{tooth}}{(\alpha_{tooth} + \alpha_{slot})} = \frac{\alpha_{tooth}}{\tau}$$

**Variables:** α_tooth — tooth pitch angle [rad]; α_slot — slot pitch angle [rad]; τ — pole pitch [rad]
**Assumptions:** Linear relationship between tooth/slot geometry and flux distribution; applicable across all three rotor types.

### Eq. (4): Motor Efficiency Definition
$$\eta_{motor} = \frac{P_{mech\ motor}}{P_{conv\ out\ total}}$$

**Variables:** P_mech,motor — motor shaft power [W]; P_conv,out,total — total output power of frequency converter [W]
**Assumptions:** Efficiency defined as ratio of mechanical output to electrical input from converter; drive losses ignored (shown to be negligible in earlier work [12]).

## Key Design Insights

1. **Saliency drives everything:** The maximum torque is directly proportional to (1/x_q − 1/x_d), so reducing q-axis permeance while maintaining d-axis permeance is the fundamental design lever.
2. **TLA rotor (Type 2) produces highest torque** among all three studied types — confirmed both numerically and by the torque-vs-angle comparison (Fig. 7).
3. **Magneto-isolated poles (Type 3) are competitive** after optimization: can approach TLA performance, with torque increase up to 25% over baseline salient pole designs.
4. **Salient pole rotors (Type 1) are inferior** for torque, power factor, and overall performance — not recommended for competitive SynRM designs.
5. **Pole coverage coefficient is the key optimization parameter:**
   - Type 1: α_τ_opt = 0.5 (symmetric tooth/slot)
   - Type 3: α_τ_opt = 0.85–0.9 (tooth-dominated)
6. **Tooth relative height matters for Type 3:** Below 0.15 relative height, pole saturation decreases and torque drops. Above this threshold, tooth height has minor effect on torque but affects specific torque (torque per volume).
7. **Manufacturing tradeoff:** Axially laminated rotors theoretically offer best performance but are too expensive/complex. TLA rotors balance performance and manufacturability — hence their commercial dominance.
8. **Efficiency map:** The 10.5 kW SynRM (Type 2 rotor) shows >90% efficiency in the 900–1800 rpm, 30–50 Nm region — confirming SynRM viability for variable-speed drive applications.
9. **Motor-drive system efficiency ≈ motor efficiency:** Drive losses are negligible for SynRM, simplifying system-level optimization.
10. **Torque increase potential:** TLA rotor can achieve up to 40% torque increase (x_d >> x_q), while magneto-isolated poles achieve up to 25% (x_q >> x_d) over reference designs.

## Optimization Setup (if applicable)

| Parameter | Value |
|-----------|-------|
| Optimizer | Evolutionary Strategy (real-number vectors) |
| Method | Mutation (self-adapting normal distribution) → crossing → selection without repetition |
| Design space | Type 1: α_τ sweep; Type 3: α_τ + tooth height |
| Fixed stator | Same for all three rotor types |
| FEA tool | 2D finite element method |
| Evaluation metric | Electromagnetic torque vs. rotation angle |

## Results (numerical)

### Torque Comparison (Fig. 7)
- **Type 2 (TLA):** Highest torque — best performance
- **Type 3 (magneto-isolated poles):** Comparable after optimization, up to 25% torque increase over baseline
- **Type 1 (salient pole):** Lowest torque

### Optimization Outcomes
| Rotor Type | Optimal α_τ | Optimal Tooth Height | Torque Increase |
|------------|-------------|---------------------|-----------------|
| Type 1 (salient pole) | 0.5 | N/A | Baseline |
| Type 2 (TLA) | N/A (accepted as optimum) | N/A | Up to 40% |
| Type 3 (magneto-isolated) | 0.85–0.9 | 0.035–0.040 m | Up to 25% |

### Experimental Validation (Type 2 Rotor)
- **Region of >90% efficiency:** 900–1800 rpm, 30–50 Nm
- **Test equipment:** ABB ACS880 (30 kW drive), ABB ACS800 (37 kW load motor), NCTE 4000-0250 torque transducer, Dewetron DAQ with Oxygen software
- **Control:** Direct Torque Control (DTC)
- **Sampling frequency:** 10 kHz

## Limitations / Caveats

1. **No direct torque comparison across all three types under identical conditions** — Type 2 was accepted as optimal without full optimization sweep (unlike Types 1 and 3). [[Unverified]] whether Type 3 with further optimization could match or exceed Type 2.
2. **No power factor comparison** reported across rotor types — only torque is compared numerically.
3. **No efficiency comparison across rotor types** — efficiency map only measured for Type 2.
4. **Evolutionary strategy details sparse** — population size, convergence criteria, and number of generations not reported. [[Unverified]] optimality of results.
5. **Single operating point for FEA** — no torque-speed envelope characterization for Types 1 and 3.
6. **Experimental validation only for Type 2** — magneto-isolated pole rotor was not manufactured or tested (mentioned as future work).
7. **No cogging torque, torque ripple, or NVH analysis** reported.
8. **Axially laminated rotor excluded** due to manufacturing difficulty — performance potential unquantified in this study.
9. **Stator is fixed** — rotor-only optimization may miss better overall machine designs.
10. **No thermal analysis** or temperature-dependent material properties considered.

## Propagation Into Wiki
- [[SynRM_rotor_topologies]] — add four-type comparison framework with pros/cons
- [[saliency_ratio]] — add voltage-based torque equation and design implications
- [[pole_coverage_coefficient]] — new concept: optimization parameter for rotor tooth sizing
- [[magneto_isolated_poles]] — new concept: promising alternative topology, 25% torque gain potential
- [[evolutionary_strategy_optimization]] — add methodology for rotor geometry optimization
- [[SynRM_efficiency_mapping]] — add experimental efficiency map data for 10.5 kW machine
- [[SynRM_equations]] — add Eqs. (1)-(2) torque expressions
- [[rotor_design_selection]] — add topology selection decision framework
- [[motorcad_rotor_sweep]] — map pole coverage coefficient to MotorCAD rotor editor parameters

## Related Pages ([[wikilinks]])
- [[SynRM]]
- [[SynRM_design]]
- [[saliency_ratio]]
- [[flux_barrier_geometry]]
- [[transversally_laminated_anisotropy]]
- [[magneto_isolated_poles]]
- [[salient_pole_rotor]]
- [[axially_laminated_anisotropy]]
- [[pole_coverage_coefficient]]
- [[SynRM_optimization]]
- [[evolutionary_strategy_optimization]]
- [[SynRM_efficiency_mapping]]
- [[PyMotorCAD]]
- [[motorcad_rotor_sweep]]
- [[rare_earth_free_machines]]
- [[FEA_workflow]]
- [[Direct_Torque_Control]]
