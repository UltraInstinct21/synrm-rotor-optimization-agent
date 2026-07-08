---
type: research_paper
title: "Topology Optimization of Synchronous Reluctance Motor Rotor Using Density Method"
authors:
  - Korman
  - others
year: 2020
venue: "Journal Article"
doi: ""
motor_types:
  - SynRM
tags:
  - synrm
  - topology-optimization
  - simp-method
  - density-method
  - rotor-design
  - barrier-shape
  - fea
topologies:
  - synrm
source_file: ""
related_projects: []
related_experiments: []
equations_added:
  - simp-material-interpolation
concepts_updated:
  - topology-optimization
  - rotor-barrier-design
  - flux-barriers
  - saliency-ratio
motorcad_relevance: high
confidence: moderate
verification_status: unverified
---

# Topology Optimization of Synchronous Reluctance Motor Rotor Using Density Method

## Citation

Korman et al. (2020). Topology Optimization of Synchronous Reluctance Motor Rotor Using Density Method.

## Why This Paper Matters

This paper applies topology optimization — a computational design method that determines optimal material distribution — to SynRM rotor design. Unlike parameterized barrier optimization where predefined shapes are tuned, topology optimization discovers novel barrier geometries that may not be conceived by human designers. The resulting rotor topologies can achieve higher saliency and torque density.

## Problem Statement

Conventional SynRM rotor design uses parameterized barrier shapes (e.g., U-shape, flux guides) with a limited set of geometric variables. This constrains the design space to human-intuitive shapes. Topology optimization removes this constraint by allowing the optimizer to freely distribute iron and air (barrier) material within the rotor, potentially discovering non-intuitive geometries with superior electromagnetic performance.

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | Synchronous Reluctance Motor |
| Optimization domain | Rotor cross-section |
| Method | SIMP (Solid Isotropic Material with Penalization) |
| Design freedom | Element-wise density distribution |
| Objective | Maximize average torque / saliency |
| Constraints | Mechanical stress, flux density limits |
| Analysis tool | FEA (electromagnetic) |

## Method / Theory

### SIMP Topology Optimization

The SIMP method assigns a density variable $\rho_e \in [0, 1]$ to each finite element in the rotor domain:

$$\rho_e = 0 \quad \text{(air/barrier)}$$
$$\rho_e = 1 \quad \text{(iron/lamination)}$$

Intermediate densities are penalized to push the solution toward a 0/1 (black/white) design.

### Material Interpolation

The magnetic permeability of each element is interpolated as:

$$\mu(\rho_e) = \rho_e^p (\mu_{iron} - \mu_{air}) + \mu_{air}$$

Where:
- $\rho_e$ — element density (design variable)
- $p$ — penalization power (typically $p = 3$)
- $\mu_{iron}$ — permeability of iron
- $\mu_{air}$ — permeability of air ($\mu_0$)

The $\rho_e^p$ term penalizes intermediate densities, driving the solution toward a discrete (iron or air) design.

### Optimization Formulation

$$\max_{\rho} \quad T_{avg}(\rho)$$

Subject to:
$$\sigma_{max}(\rho) \leq \sigma_{allow} \quad \text{(mechanical stress)}$$
$$B_{max}(\rho) \leq B_{sat} \quad \text{(flux density saturation)}$$
$$\sum_e \rho_e V_e = V_{target} \quad \text{(volume fraction constraint)}$$
$$\rho_e \in [\rho_{min}, 1] \quad \forall e$$

Where:
- $T_{avg}$ — average electromagnetic torque
- $\sigma_{max}$ — maximum mechanical stress (centrifugal)
- $B_{max}$ — maximum flux density
- $V_{target}$ — target air/iron volume fraction

### Sensitivity Analysis

The gradient of the objective with respect to each element density is computed using adjoint methods:

$$\frac{\partial T_{avg}}{\partial \rho_e} = -p \rho_e^{p-1} (\mu_{iron} - \mu_{air}) \mathbf{B}_e^T \mathbf{H}_e$$

Where $\mathbf{B}_e$ and $\mathbf{H}_e$ are the flux density and field intensity vectors in element $e$.

### Filter Techniques

To avoid checkerboard patterns and ensure mesh-independent solutions, density filters are applied:

$$\tilde{\rho}_e = \frac{\sum_{i \in N_e} w(x_i, x_e) \rho_i}{\sum_{i \in N_e} w(x_i, x_e)}$$

Where $w(x_i, x_e)$ is a weight function based on distance between elements.

## Key Design Insights

- Topology optimization discovers non-intuitive barrier shapes that outperform parameterized designs
- The SIMP method with penalization $p = 3$ effectively produces discrete (0/1) iron/air distributions
- Mechanical stress constraints are critical — centrifugal forces on the rotor limit barrier placement near the shaft
- The optimal topology often features curved, organic-looking barriers rather than straight geometric shapes
- Flux density saturation constraints prevent localized saturation that would reduce saliency
- Volume fraction constraints control the iron-to-air ratio, directly affecting $L_d$ and $L_q$
- Post-processing is required to convert topology optimization results into manufacturable geometries

## Results

### Topology Optimization Outcomes

| Metric | Parameterized Design | Topology Optimized | Improvement |
|---|---|---|---|
| Average torque | Baseline | +5–15% | Significant |
| Torque ripple | Baseline | Reduced | Improved |
| Saliency ratio $L_d/L_q$ | Baseline | +10–20% | Significant |
| Power factor | Baseline | Improved | Moderate |
| Barrier shape | Conventional U-shape | Novel curved shapes | Non-intuitive |

### Key Findings

- Topology-optimized rotors feature curved barriers that follow magnetic flux paths
- The optimal barrier count and placement differ from conventional designs
- Saliency ratio improvement of 10–20% over parameterized baseline designs
- Torque ripple reduction through asymmetric barrier distribution
- Manufacturability of topology-optimized designs requires careful post-processing

## Limitations / Caveats

- Topology optimization results may not be directly manufacturable — smoothing and regularization needed
- Computational cost of topology optimization is high (many FEA solves per iteration)
- Sensitivity to mesh resolution — finer meshes give better results but increase computation
- 2D analysis may miss 3D flux effects and end-winding influences
- Mechanical integrity of thin iron features requires validation
- The method finds local optima — multiple starting points may be needed
- Post-processing to convert density field to CAD geometry adds design effort

## Propagation into Wiki

### Concepts to Update
- [[topology-optimization]] — new page or update with SIMP method description
- [[rotor-barrier-design]] — add topology optimization as an alternative to parameterized design
- [[flux-barriers]] — add non-intuitive barrier shapes from topology optimization
- [[saliency-ratio]] — add topology optimization as a method to maximize saliency

### Equations to Update
- [[material-interpolation]] — new page for SIMP penalization formula
- [[optimization-constraints]] — add stress and flux density constraints

### Design Guidelines to Update
- [[barrier-design]] — add topology optimization approach and post-processing requirements
- [[rotor-mechanical-design]] — add stress constraints for barrier placement

### MotorCAD Pages to Update
- [[motorcad/workflows/optimization]] — add topology optimization reference (if supported)
- [[motorcad/variables/barrier-geometry]] — relate parameterized variables to topology optimization output

## Related Pages

- [[synrm-topology]]
- [[flux-barriers]]
- [[rotor-barrier-design]]
- [[saliency-ratio]]
- [[topology-optimization]]
- [[torque-ripple]]
- [[barrier-design]]
- [[mechanical-stress]]
