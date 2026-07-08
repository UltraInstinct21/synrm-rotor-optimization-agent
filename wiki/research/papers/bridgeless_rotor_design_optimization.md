---
type: research_paper
title: "Design and Optimization of a Bridgeless Rotor for Synchronous Reluctance Machines"
authors: "Arash Allahyari, Ilya Petrov, Juha J. Pyrhönen, Lassi Aarniovuori, Pia Lindh, Miika Parviainen"
year: "2024"
venue: "IEEE Access"
doi: "10.1109/ACCESS.2024.3398798"
motor_types: ["Synchronous Reluctance Machine (SynRM)"]
topics: ["bridgeless rotor", "high power", "high speed", "multi-objective optimization", "torque ripple", "power factor"]
topologies: ["bridgeless rotor", "transversally laminated rotor", "flux guide tooth tips"]
source_files: ["raw/papers/Design_and_Optimization_of_a_Bridgeless_Rotor_for_Synchronous_Reluctance_Machines.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: []
concepts_updated: ["bridgeless rotor", "flux guide tooth tips", "backplate construction", "dual phase material"]
motorcad_relevance: "High — demonstrates rotor bridge elimination as the key performance lever for SynRM. Directly applicable to the 45kW SynRM reference model in this project. The bridgeless concept explains why radial bridge thickness is the dominant factor limiting saliency in conventional designs."
confidence: Verified
---

# Design and Optimization of a Bridgeless Rotor for Synchronous Reluctance Machines

## Citation

Allahyari, A., Petrov, I., Pyrhönen, J. J., Aarniovuori, L., Lindh, P., & Parviainen, M. (2024). Design and optimization of a bridgeless rotor for synchronous reluctance machines. *IEEE Access*, 12, 61678–61693. DOI: [10.1109/ACCESS.2024.3398798](https://doi.org/10.1109/ACCESS.2024.3398798)

## Why This Paper Matters

This paper proposes eliminating radial and tangential bridges from SynRM rotors — the single biggest performance bottleneck in conventional high-power, high-speed designs. Instead of bridges, separate flux guides are attached to non-magnetic backplates stacked axially on the shaft. The result: 22–27% more torque and ~30% higher power factor compared to an optimized conventional SynRM at the same current density. For this project's [[SynRM_45kW_IE5]] model, the paper explains *why* thick bridges hurt saliency and how to think about eliminating them.

## Problem Statement

Conventional transversally laminated SynRM rotors require radial and tangential iron bridges for mechanical integrity. These bridges:
- Create unintended flux paths that increase L_q
- Reduce saliency (L_d/L_q) and (L_d − L_q)
- Deteriorate average torque and power factor
- Get worse at high power (larger rotor diameter) and high speed (thicker bridges needed)

The thicker the bridges become, the more they cancel the reluctance torque benefit. At 10,000 rpm and 250 kW, conventional SynRM designs reach severe limitations.

## Machine / Study Context

| Parameter | Value |
|-----------|-------|
| Power rating | 250 kW |
| Max speed | 10,000 rpm |
| Base speed | 4,000 rpm |
| Poles / slots | 6 / 36 |
| Stator OD | 375 mm |
| Stack length | 210 mm |
| Airgap | 0.8 mm |
| Terminal voltage | 500 V (line-line, rms) |
| Stator steel | M270-35A |
| Rotor steel | S355 |
| Cooling | Water jacket |
| Winding | 5/6 short pitch, 6 parallel paths, 18 turns/phase |

## Method / Theory

### Bridgeless Rotor Concept

Instead of iron bridges connecting flux barriers, separate flux guide (FG) modules are laser-welded to non-magnetic backplates (austenitic stainless steel 316L, 0.2 mm thick). Modules are stacked axially on the shaft. This eliminates all iron paths in the q-axis, dramatically increasing saliency.

### Flux Guide Tooth Tips (FGTT)

A novel geometry is added to the tips of flux guides near the airgap — analogous to semi-closed rotor slots in induction machines. FGTT:
- Smoothens reluctance variations → reduces torque ripple
- Decreases effective airgap → increases average torque
- Achieved without mechanical compromise (no bridges needed)

### Multi-Objective Optimization

23 total geometry variables (5 per flux guide × 3 + 2 FGTT + 6 stator), optimized using multi-objective genetic algorithm in MATLAB via PyAEDT connecting to Ansys Maxwell. Objectives: maximize average torque, minimize torque ripple. Single operating point: J = 6 A/mm², current vector angle = 60°, n = 4000 rpm.

### Conventional SynRM Baseline

Same dimensions and optimization method applied to a conventional 3-barrier transversally laminated SynRM. Mechanical stress analysis first determines minimum bridge thicknesses (b1 ≥ 8 mm, b2 ≥ 4 mm, tangential ≥ 2 mm at 10,000 rpm).

## Important Equations

The paper is primarily FEA-driven and does not present new analytical equations. Key relationships used:

### Saliency Ratio

$$\xi = \frac{L_d}{L_q}$$

- **Variables:** L_d = d-axis inductance, L_q = q-axis inductance
- **Units:** dimensionless
- **Assumptions:** At saturation levels typical of rated operation
- **Relevance:** Higher saliency → higher torque and PF. Bridges increase L_q, reducing ξ.

### Average Torque (Reluctance Torque)

$$T_{avg} = \frac{3}{2} p (L_d - L_q) I_s^2 \sin(2\gamma)$$

- **Variables:** p = pole pairs, L_d, L_q = dq inductances, I_s = stator current magnitude, γ = current vector angle from d-axis
- **Units:** N·m
- **Assumptions:** Sinusoidal MMF, no saturation effects (actual behavior deviates due to saturation)
- **Relevance:** Max torque at γ = 45° in theory; in practice rated torque at γ = 55–65° due to saturation

### Torque Ripple

$$TR = \frac{T_{max} - T_{min}}{T_{avg}} \times 100\%$$

- **Variables:** T_max, T_min = peak-to-peak torque extrema over one electrical period
- **Units:** percentage
- **Assumptions:** Over one complete electrical cycle at steady state

### Rotor Iron Space Factor (with backplates)

$$k_{rotor} = \frac{l_{lam}}{l_{lam} + 2 \cdot t_{backplate}} = \frac{3}{3.4} \approx 0.88$$

- **Variables:** l lam = lamination stack length (3 mm), t backplate = backplate thickness (0.2 mm each)
- **Units:** dimensionless
- **Assumptions:** Two backplates per lamination module
- **Relevance:** Backplates reduce rotor iron volume, decreasing d-axis permeance and ~4% average torque

## Key Design Insights

1. **Bridge thickness is the dominant bottleneck.** At 10,000 rpm with 220 mm rotor diameter, minimum bridge thicknesses of 8/4/2 mm are required — these destroy saliency.
2. **Bridgeless rotor delivers 26% more torque** at same current density (560 Nm vs 445 Nm in optimization, 22–27% in 2.5D FEA with backplates and skew).
3. **Power factor improves by ~30%** (0.64 vs 0.49 at nominal current). PF > 0.6 over most operating points for BLR vs max 0.52 for conventional.
4. **Power output at max speed: 2.4× higher** for BLR (157 kW vs 65 kW at 10,000 rpm).
5. **Efficiency maps are significantly wider** above 0.95 for BLR. Rotor iron losses are 50% lower in BLR at peak current (saturated bridges in conventional SynRM increase core loss).
6. **Flux guide tooth tips** reduce torque ripple significantly and increase average torque — use them.
7. **3 flux guides (FG)** chosen for manufacturing simplicity; more FGs showed marginal improvement but increase welding operations.
8. **Rotor skew**: 6 slices, 5° total angle reduces torque ripple from ~6.5% to 2.4% with only ~1% torque penalty.
9. **Backplate effect**: ~4% torque reduction from rotor space factor of 0.88 vs 0.97. Must be accounted for in design.
10. **Rotor iron loss reduction**: Eliminated bridges (which saturate heavily) means dramatically lower rotor core losses — a significant advantage at high current density.

## Optimization Setup

### BLRSynRM Variables (23 total)

**Rotor per flux guide (5 × 3 = 15):**
| Variable | Description |
|----------|-------------|
| x1 | Distance of FG from shaft center [mm] |
| x2 | Height of FG at shaft center [mm] |
| x3 | Height of FG at arm [mm] |
| x4 | Width of FG middle body [mm] |
| x5 | Angle of FG arm from q-axis [deg] |

**Flux guide tooth tips (2):**
| Variable | Description |
|----------|-------------|
| x6 | Width of FG tooth tips [mm] |
| x7 | Height of FG tooth tips [mm] |

**Stator (6):**
| Variable | Description |
|----------|-------------|
| x8 | Stator inner diameter [mm] |
| x9 | Width of stator teeth under tooth tips [mm] |
| x10 | Slot body height [mm] |
| x11 | Width of stator teeth at yoke [mm] |
| x12 | Yoke height [mm] (auto-calculated from OD) |
| x13 | Slot opening width [mm] |
| x14 | Stator tooth tip root height [mm] |

### Conventional SynRM Variables (21 total)
- 15 rotor variables (3 barriers × 5 variables each)
- 6 stator variables

### Operating Point
- Current density: J = 6 A/mm² (nominal), up to 12 A/mm² (overload)
- Current vector angle: γ = 60° from d-axis
- Speed: n = 4000 rpm
- Rationale: Max theoretical torque at 45°, but saturation pushes optimal angle to 55–65°

### Algorithm
- Multi-objective genetic algorithm (MATLAB)
- FEA coupling via PyAEDT → Ansys Maxwell
- Pareto front: maximize average torque, minimize torque ripple
- Selection criterion: max torque with ripple < 10%

## Results (numerical)

### BLRSynRM Selected Design Geometry

| Variable | FG1 | FG2 | FG3 |
|----------|-----|-----|-----|
| x1 [mm] | 34.8 | 70.4 | 87.2 |
| x2 [mm] | 11.8 | 8.3 | 8.3 |
| x3 [mm] | 14.5 | 9.6 | 9.9 |
| x4 [mm] | 38.9 | 23.5 | 16.6 |
| x5 [deg] | 34.1 | 24.3 | 15.7 |
| FGTT width (x6) | 1.6 mm | 1.6 mm | 1.6 mm |
| FGTT height (x7) | 1.3 mm | 1.3 mm | 1.3 mm |

### Performance Comparison (6 A/mm², 60°)

| Metric | BLRSynRM (with backplates + skew) | Conventional SynRM (with skew) | Improvement |
|--------|-----------------------------------|--------------------------------|-------------|
| Average torque | 528.9 Nm | 432.8 Nm | **+22%** |
| Torque ripple | 3.1% | 1.8% | — |
| Power factor | 0.64 | 0.49 | **+31%** |

### Performance Comparison (12 A/mm², 60° — overload)

| Metric | BLRSynRM | Conventional SynRM | Improvement |
|--------|----------|-------------------|-------------|
| Average torque | 984.1 Nm | 774.5 Nm | **+27%** |
| Torque ripple | 6.1% | 5.5% | — |
| Power factor | 0.49 | 0.38 | **+29%** |

### Power Output

| Metric | BLRSynRM | Conventional SynRM |
|--------|----------|-------------------|
| Peak power | ~440 kW | ~300 kW (+47%) |
| Power at 10,000 rpm | 157 kW | 65 kW (2.4× higher) |

### Backplate and Skew Effects (BLRSynRM)

| Configuration | Torque (Nm) | Ripple (%) | PF |
|---------------|-------------|------------|-----|
| 2D FEA (no backplates, no skew) | 557.2 | 6.5 | 0.65 |
| 2D FEA (rotor SF=0.88, no skew) | 535.7 | 6.2 | 0.64 |
| 3D FEA (4mm FG + 0.5mm BP, no skew) | 532.4 | 7.6 | 0.61 |
| 2.5D FEA (SF=0.97, 6-slice skew) | 551.1 | 2.4 | 0.65 |
| 2.5D FEA (SF=0.88, 6-slice skew) | 528.9 | 3.1 | 0.64 |

### Mechanical Integrity
- Backplate: 0.2 mm austenitic stainless steel 316L (yield strength 290 MPa)
- Flux guide lamination: 3 mm S355 steel, 1 mm sheets
- Module: 2 × 0.2 mm backplates + 3 mm lamination = 3.4 mm total
- Stress analysis at 12,000 rpm (20% above max speed): well within acceptable range

## Limitations / Caveats

1. **Manufacturability is acknowledged as challenging.** Laser welding flux guides to backplates and stacking modules is more complex than stamping conventional laminations. The paper notes manufacture is "actively under development."
2. **Glue-based assembly is not viable** for high-power/high-speed applications due to thermal degradation of adhesive properties.
3. **3D FEA is computationally prohibitive** (>40 hours for one electrical period). 2D FEA with space factor correction (SF = 0.88) is the practical approach, but introduces approximation.
4. **Efficiency maps are optimistic** — PWM harmonic losses, mechanical losses, AC winding losses, and rotor eddy current losses are not included.
5. **Rotor eddy current losses from galvanic contacts** between laminations through backplates are not fully characterized.
6. **Conventional SynRM PF degrades severely at overload** (0.38 at 12 A/mm²), making it impractical for traction requiring high power inverter ratings.
7. **SynRM power drops significantly above base speed** — careful base speed selection is critical for the application.
8. **Comparison excludes SRMs** because their dedicated high-power converters (~400 kW) are impractical, while SynRM converters are commercially available.
9. **No experimental validation** — all results are FEA-based. Physical prototype manufacturing status is mentioned but no measurements are presented.

## Propagation Into Wiki

Pages that should reference this paper's findings:

- [[SynRM_45kW_IE5]] — Apply bridgeless rotor concept to reference motor design
- [[motorcad/workflow]] — Note bridge thickness as primary saliency limiter
- [[motorcad/parameters]] — Document flux guide geometry variables and backplate effect on space factor
- [[codebase_map]] — Reference optimization approach (genetic algorithm, multi-objective)
- [[architecture/orchestrator]] — Consider BLR optimization as a workflow template
- [[active_tasks]] — Add bridgeless rotor feasibility study as potential task

## Related Pages

- [[motorcad/parameters]] — Rotor geometry variables, bridge dimensions, saliency relationship
- [[motorcad/workflow]] — Design and optimization workflow for SynRM rotors
- [[known_issues]] — Bridge-induced saliency degradation as fundamental SynRM limitation
- [[project_overview]] — SynRM design goals for the motor-deepagent project
- [[motorcad/result_fields]] — Ld, Lq, saliency, torque, power factor as key optimization outputs
