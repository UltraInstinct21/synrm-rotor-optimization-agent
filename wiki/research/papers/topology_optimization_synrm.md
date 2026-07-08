---
type: research_paper
title: "On the Use of Topology Optimization for Synchronous Reluctance Machines Design"
authors: "Oguz Korman, Mauro Di Nardo, Michele Degano, Chris Gerada"
year: 2022
venue: "Energies, 15(10), 3719"
doi: "10.3390/en15103719"
motor_types: ["Synchronous Reluctance (SynRel)"]
topics: ["topology optimization", "density method", "SIMP", "rotor design", "flux barriers", "torque ripple", "parametric optimization"]
topologies: ["SynRel", "flux barrier rotor"]
source_files: ["raw/papers/On the Use of Topology Optimization for Synchronous Reluctance Machines Design.md"]
related_projects: ["motor-deepagent"]
related_experiments: []
equations_added: ["permeability_interpolation_simp"]
concepts_updated: ["topology_optimization", "density_method", "SIMP", "penalization_coefficient", "adjoint_variable_method"]
motorcad_relevance: "Directly applicable — TO for SynRel rotor flux barrier design, refinement of parametrically-optimized geometries, sensitivity-based optimization with FEM"
confidence: Verified
---

# On the Use of Topology Optimization for Synchronous Reluctance Machines Design

## Citation

Korman, O.; Di Nardo, M.; Degano, M.; Gerada, C. On the Use of Topology Optimization for Synchronous Reluctance Machines Design. *Energies* **2022**, *15*, 3719. <https://doi.org/10.3390/en15103719>

## Why This Paper Matters

This paper provides a systematic investigation of **density-method (DM) topology optimization** applied to SynRel machine rotors — a relatively unexplored area at the time of publication. Unlike template-based parametric optimization (circular, fluid-shaped, straight-segmented barriers), TO removes shape constraints entirely, enabling exploration of geometries unreachable by parametric methods. The paper's key contribution is not a single optimized design, but rather a **detailed study of how optimization settings affect results**, making it a practical reference guide for anyone applying DM-based TO to SynRel machines. The finding that TO works best as a **refinement tool** on top of parametrically-optimized designs is particularly actionable for [[motorcad]] workflows.

## Problem Statement

SynRel machines offer cost-effective conversion without permanent magnets, but their rotor geometry is complex due to anisotropy requirements. Parametric optimization constrains the design space to predefined shapes (circular, fluid, straight-segmented barriers), limiting exploration. Topology optimization aims to find the **optimal material distribution** (iron vs. air) without imposed geometric templates. However, the interplay between optimization settings and SynRel-specific requirements (saliency, torque ripple, flux barrier coherence) is not well understood, requiring systematic investigation.

## Machine / Study Context

**Benchmark machine** — a SynRel machine designed for light traction applications:

| Parameter | Value |
|-----------|-------|
| Rated Speed | 2500 rpm |
| Maximum Speed | 10,000 rpm |
| DC Bus Voltage | 610 V |
| Stator Diameter | 245 mm |
| Rotor Diameter | 160 mm |
| Air Gap Length | 0.7 mm |
| Stack Length | 120 mm |
| Number of Slots | 36 |
| Number of Poles | 6 |
| Max Current Density | 10 A/mm² |
| Winding | Distributed single layer |
| Cooling | Water jacket, 3 L/min |
| Lamination | M290-50A (stator and rotor) |

The benchmark rotor was the result of a **parametric multi-objective optimization** (genetic algorithm maximizing average torque, minimizing torque ripple), yielding 100.8 Nm average torque with 7.3% ripple [[korman_parametric_flux_barrier_2022]]. FEM performed in **JMAG Designer** with mesh elements as design cells (iron/air only).

## Method / Theory

**Density Method (SIMP) Topology Optimization** applied to SynRel rotor design:

1. **Design space discretization**: Mesh elements become optimization cells with material properties interpolated between iron and air via Equation (1).
2. **Gradient-based optimization**: Adjoint Variable Method (AVM) computes sensitivities efficiently — one function evaluation per sensitivity vector, regardless of variable count.
3. **Iron/air interpolation**: Controlled by penalization coefficient *n* that drives intermediate materials toward binary (air/iron) states.
4. **Symmetry**: Half-rotor (symmetric poles) used to reduce computation. Outer 0.5 mm frame added for feasibility.
5. **FEA coupling**: Each iteration requires a full electromagnetic FEA solve (torque at multiple rotor positions).

**Two-phase approach:**
- **Phase 1**: Empty design space — investigate mesh, initial density, penalization, objectives
- **Phase 2**: Existing optimized rotor as starting point — assess TO as refinement tool

## Important Equations

### Permeability Interpolation (SIMP Method) — Equation (1)

$$\mu_i = \mu_0 [1 + (\mu_r - 1)\rho_i^n]$$

| Variable | Description | Units |
|----------|-------------|-------|
| $\mu_i$ | Interpolated permeability of cell *i* | H/m |
| $\mu_0$ | Permeability of free space (air) | $4\pi \times 10^{-7}$ H/m |
| $\mu_r$ | Relative permeability of iron | dimensionless (~4000 for M290-50A) |
| $\rho_i$ | Normalized density of cell *i* (0 = air, 1 = iron) | dimensionless [0, 1] |
| $n$ | Penalization coefficient | dimensionless, positive integer |

**Assumptions:**
- Two-material system (iron + air only); no magnets or copper in design space
- $\rho_i = 0$ → cell is air; $\rho_i = 1$ → cell is iron; $0 < \rho_i < 1$ → intermediate ("gray") material
- Higher *n* → steeper interpolation → stronger drive toward binary material distribution
- For *n* = 1: linear interpolation (no penalization); for *n* > 1: penalization pushes intermediate densities toward air or iron

## Key Design Insights

1. **Mesh resolution tradeoff**: 0.25 mm mesh → 97.5 Nm in 4.4 h to knee; 2 mm mesh → 93.2 Nm in 9 min. **31 h difference for 4.5% torque gain.** Medium resolution (1 mm) offers best time/performance balance.

2. **Initial density has minor effect on final objective**: Starting from 0.2, 0.5, or 0.9 yielded 94.3, 95.2, 94.7 Nm respectively. Low starting density (more air) → significantly slower convergence due to low early sensitivities.

3. **Penalization coefficient is critical**: Higher *n* (≥2) → slower convergence AND worse final objective. Counterintuitively, higher penalization also produces **more** intermediate materials, not fewer. *n* = 1 recommended.

4. **Torque ripple optimization produces better structures**: Including torque ripple in the objective → more uniform material distribution and additional air barriers (three-barrier structure), despite higher computation (1000 iterations). Best result: 92.3 Nm, 4.6% ripple.

5. **TO as refinement tool**: Starting from the parametrically-optimized 3-barrier rotor → torque increased from 100.8 to 102.3 Nm (+1.5%), ripple reduced from 7.3% to 6.5%. The innermost barrier expanded toward the shaft, increasing air-to-iron ratio — a shape unreachable by parametric expressions without adding degrees of freedom.

6. **Manufacturing feasibility not guaranteed**: Without structural constraints, optimized rotors lack mechanical connections to the frame. Post-processing or feasibility constraints needed.

7. **Intermediate materials are not advantageous**: No design with gray-scale (intermediate density) materials outperformed binary (iron/air) designs. The intermediate materials are artifacts, not features.

## Optimization Setup

### Parameters Investigated

| Setting | Values Tested | Impact |
|---------|---------------|--------|
| Mesh max element length | 0.25, 0.5, 1, 2 mm | Computation time dominant; slight objective effect |
| Initial density | 0.2, 0.5, 0.9 | Minor effect on objective; low density → slow convergence |
| Penalization coefficient *n* | 1, 2, 3, 4, 5, 10, 20 | Strong effect; *n* = 1 best; higher → worse convergence and objective |
| Objective function | Avg torque only; avg torque + torque ripple | Ripple inclusion → better material distribution, more feasible structures |

### Software & Solver
- **FEA**: JMAG Designer
- **Optimization algorithm**: Gradient-based with AVM sensitivities
- **Design space**: Rotor mesh elements (iron/air interpolation)
- **Boundary conditions**: Symmetric poles, 0.5 mm outer frame, unchanged stator/winding/peak current

### Computation Costs
- 0.25 mm mesh: 300 iterations → several hours (knee at ~4.4 h)
- 2 mm mesh: 300 iterations → ~9 min (knee)
- Torque ripple study: 1000 iterations per run
- 31 h difference between finest and coarsest mesh for 4.5% torque improvement

## Results (numerical)

### Empty Design Space — Average Torque Optimization

| Mesh Length | Avg Torque (Nm) | Time to Knee | Notes |
|-------------|-----------------|--------------|-------|
| 0.25 mm | 97.5 | ~4.4 h | Most detailed |
| 0.5 mm | 97.2 | — | Good |
| 1 mm | 94.7 | — | Best tradeoff |
| 2 mm | 93.2 | ~9 min | Fastest |

### Empty Design Space — Initial Density Study (1 mm mesh)

| Initial Density | Avg Torque (Nm) | Notes |
|-----------------|-----------------|-------|
| 0.2 | 94.3 | More intermediate materials, slow convergence |
| 0.5 | 95.2 | More intermediate materials |
| 0.9 | 94.7 | Least intermediate materials |

### Empty Design Space — Penalization Study (1 mm mesh)

| *n* | Relative Performance | Convergence |
|-----|---------------------|-------------|
| 1 | Best (baseline) | Fast |
| 2 | Slightly worse | Slower |
| 3–20 | Substantially worse | Very slow; many intermediate materials |

### Torque Ripple Optimization

| Mesh | Avg Torque (Nm) | Torque Ripple | Notes |
|------|-----------------|---------------|-------|
| 2 mm | 92.3 | 4.6% | Better distribution |
| 1 mm | 92.1 | 6.3% | More intermediate materials |

### Non-Empty Design Space (Refinement)

| Metric | Before (Parametric) | After (TO Refinement) | Change |
|--------|--------------------|-----------------------|--------|
| Average Torque | 100.8 Nm | 102.3 Nm | +1.5% |
| Torque Ripple | 7.3% | 6.5% | −0.8 pp |

## Limitations / Caveats

1. **No structural/mechanical constraints**: Optimized rotors from empty space lack mechanical integrity (no bridges to frame). Additional feasibility constraints or post-processing required.
2. **Two-material only**: No magnets, copper, or stress-related multi-material TO explored. Real rotors may need bridges, ribs, or shaft connections.
3. **Single FEA solver**: Results dependent on JMAG-specific implementation; different solvers may yield different convergence behavior.
4. **No experimental validation**: All results are FEM-based; no prototype tested.
5. **Initial density generalizability caveat**: Authors note that the minor effect of starting density may not generalize to other problems.
6. **Computation time**: TO remains significantly slower than parametric optimization, especially for fine meshes and multi-objective problems.
7. **Refinement gain is small**: +1.5% torque improvement from TO refinement may not justify the additional computational cost in all cases.
8. **Penalization coefficient behavior**: The observation that higher *n* produces more intermediate materials is counterintuitive and may be problem-specific.

## Propagation Into Wiki

- [[topology_optimization]] — New concept page covering TO methods for motor design
- [[density_method_SIMP]] — Explanation of the density method / SIMP approach with Equation (1)
- [[optimization_settings_guide]] — Practical guide to TO settings (mesh, penalization, initial density, objectives)
- [[synrm_rotor_design]] — Update with TO as complementary tool to parametric optimization
- [[flux_barrier_design]] — Add TO-generated barrier shapes as additional topology reference
- [[torque_ripple_optimization]] — Note that torque ripple objectives improve material distribution quality
- [[parametric_vs_topology_optimization]] — Comparison of parametric and TO approaches
- [[motorcad_optimization]] — Potential workflow: parametric optimization → TO refinement

## Related Pages

- [[motorcad]]
- [[synrm_design]]
- [[finite_element_analysis]]
- [[torque_optimization]]
- [[rotor_topology]]
- [[korman_parametric_flux_barrier_2022]] — The parametric optimization study that produced the benchmark rotor
