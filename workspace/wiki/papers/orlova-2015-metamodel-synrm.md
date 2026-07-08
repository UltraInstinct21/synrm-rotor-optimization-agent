---
type: research_paper
title: "Metamodel-Based Optimization of Synchronous Reluctance Motor Using Local Polynomial Approximation"
authors:
  - Orlova
  - others
year: 2015
venue: "Journal Article"
doi: ""
motor_types:
  - SynRM
tags:
  - synrm
  - metamodel
  - surrogate-optimization
  - local-polynomial
  - rotor-design
  - barrier-geometry
  - computation-efficiency
topologies:
  - synrm
source_file: ""
related_projects: []
related_experiments: []
equations_added:
  - metamodel-approximation
concepts_updated:
  - surrogate-based-optimization
  - rotor-barrier-design
  - flux-barriers
motorcad_relevance: high
confidence: moderate
verification_status: unverified
---

# Metamodel-Based Optimization of Synchronous Reluctance Motor Using Local Polynomial Approximation

## Citation

Orlova et al. (2015). Metamodel-Based Optimization of Synchronous Reluctance Motor Using Local Polynomial Approximation.

## Why This Paper Matters

This paper addresses a critical bottleneck in SynRM design: the computational cost of FEA-based optimization. By using metamodel (surrogate) optimization with local polynomial approximation, the authors demonstrate significant reduction in computation time while maintaining design quality. This approach is directly applicable to MotorCAD-based optimization workflows where each EMag calculation takes 60–90 seconds.

## Problem Statement

Optimizing SynRM rotor barrier geometry requires many FEA evaluations. Each evaluation is computationally expensive (minutes to hours per design point). Full factorial or grid-based optimization is impractical for high-dimensional design spaces. The paper proposes a metamodel-based approach to reduce the number of direct FEA evaluations while still finding near-optimal designs.

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | Synchronous Reluctance Motor |
| Stator | W21 frame (standard industrial) |
| Rotor type | Multi-barrier interior |
| Optimization variables | Barrier geometry parameters |
| Objective | Maximize torque / minimize torque ripple |
| Constraints | Mechanical integrity, flux density limits |
| Method | Metamodel (surrogate) optimization |

## Method / Theory

### Metamodel Optimization Framework

The optimization replaces expensive FEA evaluations with a cheap mathematical model (metamodel) that approximates the FEA response surface:

$$\hat{f}(\mathbf{x}) \approx f_{FEA}(\mathbf{x})$$

Where:
- $\hat{f}(\mathbf{x})$ — metamodel prediction
- $f_{FEA}(\mathbf{x})$ — actual FEA evaluation
- $\mathbf{x}$ — design variable vector

### Local Polynomial Approximation

The metamodel uses local polynomial fitting. For each query point, a polynomial is fitted using nearby sample points:

$$\hat{f}(\mathbf{x}) = \sum_{i=1}^{N} w_i(\mathbf{x}) f(\mathbf{x}_i)$$

Where:
- $w_i(\mathbf{x})$ — weight function depending on distance from query point $\mathbf{x}$ to sample point $\mathbf{x}_i$
- $f(\mathbf{x}_i)$ — FEA evaluation at sample point $i$
- $N$ — number of sample points in the local neighborhood

### Optimization Algorithm

```
1. Initial sampling: Generate N₀ design points (Latin Hypercube or similar)
2. FEA evaluation: Run FEA for all N₀ points
3. Metamodel construction: Build local polynomial approximation
4. Metamodel optimization: Find optimum of metamodel (cheap)
5. Verification: Run FEA at metamodel optimum
6. Update: Add new point to sample set, refine metamodel
7. Convergence check: Repeat 4–6 until convergence
```

### Design Variables

The barrier geometry is parameterized by:

| Variable | Description | Typical Range |
|---|---|---|
| Barrier angle | Angular position of each barrier layer | 10–80° |
| Barrier thickness | Width of each air/magnet barrier | 1–10 mm |
| Bridge thickness | Mechanical bridge at barrier ends | 0.5–3 mm |
| Web thickness | Iron web between barriers | 2–15 mm |
| Barrier count | Number of barrier layers per pole | 2–6 |

### Objective Function

$$\min_{\mathbf{x}} \quad J(\mathbf{x}) = w_1 \cdot \frac{T_{avg}}{T_{target}} + w_2 \cdot \frac{TR}{TR_{max}} + w_3 \cdot \frac{PF_{min}}{PF(\mathbf{x})}$$

Where:
- $T_{avg}$ — average torque
- $TR$ — torque ripple
- $PF$ — power factor
- $w_1, w_2, w_3$ — weighting factors

## Key Design Insights

- Metamodel optimization reduces FEA evaluations by 70–90% compared to direct optimization
- Local polynomial approximation adapts better to nonlinear FEA response surfaces than global polynomial surrogates
- Latin Hypercube sampling provides efficient initial space-filling designs
- The approach is particularly valuable for SynRM barrier optimization where the response surface is highly nonlinear
- Sequential refinement (adding points near the optimum) improves metamodel accuracy where it matters most
- W21 stator frame is a common industrial standard used for benchmarking

## Results

| Metric | Direct FEA Optimization | Metamodel Optimization |
|---|---|---|
| Number of FEA evaluations | 200–500 | 30–80 |
| Computation time | Very high | Reduced by 70–90% |
| Solution quality | Optimal | Near-optimal (within 2–5%) |
| Convergence | Guaranteed | Relies on metamodel accuracy |

### Key Findings

- Optimized barrier geometry achieves higher torque density than baseline design
- Torque ripple is reduced through barrier angle optimization
- The metamodel approach finds designs within 2–5% of the true FEA optimum
- Computation time is reduced from days to hours for a complete optimization run

## Limitations / Caveats

- Metamodel accuracy depends on sample density and distribution
- Highly nonlinear regions (e.g., near saturation) may require more sample points
- The approach assumes a smooth response surface — discontinuities from geometry changes can cause issues
- Specific W21 stator dimensions and rotor parameters not fully detailed in the summary
- Multi-objective tradeoffs require careful weight selection
- 2D FEA assumptions may not capture 3D effects

## Propagation into Wiki

### Concepts to Update
- [[surrogate-based-optimization]] — add metamodel framework and local polynomial method
- [[rotor-barrier-design]] — add optimization variable definitions and ranges
- [[flux-barriers]] — add barrier parameterization for optimization
- [[design-of-experiments]] — add Latin Hypercube sampling for initial design

### Equations to Update
- [[optimization-objective]] — add multi-objective SynRM formulation
- [[metamodel-approximation]] — new page for surrogate model theory

### Design Guidelines to Update
- [[barrier-design]] — add optimization-oriented barrier parameterization
- [[optimization-strategy]] — add metamodel approach for MotorCAD workflows

### MotorCAD Pages to Update
- [[motorcad/workflows/parameter-sweep]] — relate to metamodel sampling strategy
- [[motorcad/workflows/optimization]] — add surrogate-based optimization approach

## Related Pages

- [[synrm-topology]]
- [[flux-barriers]]
- [[rotor-barrier-design]]
- [[surrogate-based-optimization]]
- [[design-of-experiments]]
- [[barrier-design]]
- [[torque-ripple]]
- [[saliency-ratio]]
