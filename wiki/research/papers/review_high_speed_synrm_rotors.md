---
type: research_paper
title: "Review and Enhancements of Rotor Designs for High Speed Synchronous Reluctance Machines"
authors: "Ludwig Hausmann, Markus Heim, Marcel Waldhof, Julian Fischer, Jürgen Fleischer, Wilken Wößner, Max Oliveira Flammer, Nejila Parspour"
year: ""
venue: ""
doi: ""
motor_types: ["Synchronous Reluctance Machine (SynRM)"]
topics: ["High Speed Rotor Design", "Fiber Reinforced Plastics", "Structural Analysis", "Electromagnetic Analysis", "Manufacturing"]
topologies: ["Transversally Laminated Rotor", "Axially Laminated Rotor", "Fiber Reinforced Support Structure"]
source_files: ["raw/papers/Review and Enhancements of Rotor Designs for High Speed Synchronous Reluctance Machines.md"]
related_projects: []
related_experiments: []
equations_added: ["torque_proportionality"]
concepts_updated: ["saliency_ratio", "inductance_ratio", "power_factor", "field_weakening"]
motorcad_relevance: "Direct relevance for high-speed SynRM design, rotor structural optimization, and fiber reinforced support concepts"
confidence: Verified
---

# Review and Enhancements of Rotor Designs for High Speed Synchronous Reluctance Machines

## Citation

Hausmann, L., Heim, M., Waldhof, M., Fischer, J., Fleischer, J., Wößner, W., Flammer, M. O., & Parspour, N. (n.d.). *Review and Enhancements of Rotor Designs for High Speed Synchronous Reluctance Machines*. KIT and University of Stuttgart.

## Why This Paper Matters

This paper provides a comprehensive taxonomy of existing high-speed SynRM rotor designs and introduces a novel fiber-reinforced support structure concept. It addresses the fundamental limitation preventing SynRM adoption in traction applications: mechanical restrictions on maximum rotor speed. The work bridges electromagnetic performance with structural integrity and manufacturing feasibility—critical for practical implementation. The morphological box classification serves as a valuable design reference for exploring rotor topology options.

## Problem Statement

SynRM offers a rare-earth-free alternative to PMSM for traction drives, but suffers from:
- Low power factor compared to PMSM
- Poor torque and power density
- Early power drop in field weakening range

**Root cause:** Mechanical restrictions on rotor lamination stack limit maximum permissible operating speed, preventing SynRM from reaching power densities competitive with PMSM for traction applications.

**Goal:** Increase maximum operation speed of SynRM by optimizing structural design while maintaining electromagnetic performance and suitability for series production.

## Machine / Study Context

**Application:** Electric vehicle traction drives (general, not specific platform)

**Machine Geometry (TABLE II):**
| Parameter | Value |
|-----------|-------|
| Outer stator diameter | 250 mm |
| Bore diameter | 130 mm |
| Active length | 180 mm |
| Air-gap | 0.5 mm |
| Number of slots | 36 |
| Number of poles | 4 |
| Slots per pole per phase | q = 3 |
| Nominal current | 42 A |
| DC-Link Voltage | 650 V |
| Base speed | ≈ 5000 rpm |

**Design Constraints:**
- Standard electrical sheets for flux conduction
- Fiber reinforced structural struts for mechanical support
- Must withstand centrifugal forces at high speed
- Must maintain electromagnetic performance comparable to conventional design

## Method / Theory

### Literature Review & Classification
Systematic analysis of existing rotor concepts using morphological box classification based on:
1. Material composition (mono vs. multi-material)
2. Material of support structure (metal, polymers, fiber reinforced plastic)
3. Assembly process (pressing, filling, winding, etc.)
4. Type of closure for radial load (form-fit, force-fit, material closure)
5. Arrangement of support structure (axial, radial, tangential)
6. Additional end plates (applied vs. not applied)

### Novel Rotor Concept
- **Standard electrical sheets** for flux conduction
- **Continuous fiber reinforced structural struts** inserted within rotor core
- **Bone-shaped struts** created by double loop connection around two support wires
- **Form-fit transmission** between flux conducting sections
- **Press-fit assembly** into sheet metal stack

### Simulation Methods
- **Structural Analysis:** Abaqus FEA (centrifugal load, thermal load)
- **Electromagnetic Analysis:** COMSOL Multiphysics (non-linear stationary FEA)
- **Torque-Speed Map:** Hybrid numerical-analytical model with MTPA, MA, MTPV algorithms

### Material Properties (TABLE III)

**Electric Sheet (TKES M270-35A):**
| Property | Value |
|----------|-------|
| Density ρe | 7.65 g/cm³ |
| Young's modulus E | 185,000 N/mm² |
| Poisson ratio ν | 0.3 |
| Yield strength Rp0.2 | 390 N/mm² |
| Tensile strength Rm | 550 N/mm² |
| Thermal expansion α | 12×10⁻⁶/K |

**Unidirectional Glass Fiber Composite:**
| Property | Value |
|----------|-------|
| Density ρg | 1.9 g/cm³ |
| Longitudinal modulus E11 | 40,000 N/mm² |
| Transversal modulus E22 | 11,000 N/mm² |
| In-plane shear modulus G12 | 4,300 N/mm² |
| Major Poisson ratio ν12 | 0.28 |
| Minor Poisson ratio ν23 | 0.07 |
| Longitudinal thermal expansion α1 | 4.5×10⁻⁶/K |
| Transversal thermal expansion α2, α3 | 50×10⁻⁶/K |

## Important Equations (with normalized form, original notation, variables, units, assumptions)

### Torque Proportionality (Equation 1)

**Original Notation:**
$$T \propto L_d - L_q \tag{1}$$

**Normalized Form:**
$$T = \frac{3}{2} p \left[ \lambda_d i_q - \lambda_q i_d \right] = \frac{3}{2} p \left[ L_d i_d i_q - L_q i_q i_d \right] = \frac{3}{2} p (L_d - L_q) i_d i_q$$

**Variables:**
- $T$ — Torque [Nm]
- $L_d$ — d-axis inductance [H] (or [mH] in paper)
- $L_q$ — q-axis inductance [H] (or [mH] in paper)
- $p$ — Number of pole pairs
- $\lambda_d$, $\lambda_q$ — d-axis and q-axis flux linkages [Wb]
- $i_d$, $i_q$ — d-axis and q-axis currents [A]

**Units:** Torque in Nm, inductances in mH, currents in A

**Assumptions:**
- Sinusoidal winding distribution
- Negligible saturation effects (linear magnetic circuit)
- No permanent magnet excitation (SynRM specific)

**Significance:** Torque is directly proportional to the difference between d-axis and q-axis inductances. Maximizing $(L_d - L_q)$ maximizes torque production.

### Inductance Ratio

**Notation:**
$$x = \frac{L_d}{L_q}$$

**Variables:**
- $x$ — Inductance ratio (field-oriented)
- $L_d$ — d-axis inductance [mH]
- $L_q$ — q-axis inductance [mH]

**Significance:** The ratio $x$ has a large impact on constant power range behavior in field weakening operation. Higher $x$ enables wider constant power range, beneficial for EV traction.

## Key Design Insights

### Existing Concepts Analysis
1. **Topology optimization of ribs** offers simple structure but limited output power (max 37,500 rpm ceiling observed)
2. **Thinner laminations** reduce iron losses but increase production effort and tooling wear
3. **Air-gap sensitivity** — geometric errors or retaining sleeves significantly impact efficiency
4. **Thermal management** remains under-investigated, especially for multi-material rotors with different thermal expansion coefficients

### Novel Fiber Reinforced Concept
1. **Bone-shaped struts** enable form-fit force transmission without compromising electromagnetic path
2. **Continuous fiber reinforcement** provides superior strength-to-weight ratio vs. metallic ribs
3. **Modular assembly** — struts press-fitted into sheet stack, enabling independent optimization of mechanical and electromagnetic properties
4. **Design flexibility** — rib substitution allows electromagnetic tuning while maintaining structural integrity

### Electromagnetic Trade-offs
- Additional electrical steel for bone holders decreases q-axis magnetic resistance
- Higher $L_q$ reduces average torque by ~4% vs. conventional design
- Substituted ribs can improve inductance ratio, enhancing field weakening performance

### Manufacturing Considerations
1. **Continuous fiber option** — semi-finished fiber product entwined around austenite steel wires, similar to pultrusion process
2. **Long-fiber integral structure** — injection molding or impact extrusion for cost-effective mass production
3. **Form-fit assembly** — negative shapes in sheet stack ensure reliable force transmission

## Optimization Setup (if applicable)

### Structural Optimization Parameters
- **Speed range:** 15,000 rpm (baseline) to 20,000 rpm (overspeed)
- **Thermal load:** 150 K temperature difference
- **Failure criterion:** Maximum equivalent stress < yield strength (390 N/mm²)

### Electromagnetic Optimization Parameters
- **DC-Link Voltage:** 650 V
- **Nominal Current:** 42 A
- **Base Speed:** ~5000 rpm
- **Optimization objectives:** Maximize torque, maximize inductance ratio, maintain power factor
- **Control strategies:** MTPA, MA, MTPV algorithms

### Design Variables (Future Work)
- Rib thickness and position
- Support structure geometry (bone shape optimization)
- Fiber material selection (glass, basalt, carbon)
- Preload during assembly
- Axial end plate configuration
- Lateral air-gap filling with adhesive resins

## Results (numerical)

### Structural Analysis

**At 15,000 rpm + 150 K thermal load:**
- **Conventional design:** Max radial expansion near air-gap = 170 μm
- **Novel design:** Max radial expansion near air-gap = 161 μm (5.3% reduction)
- **Stress levels:** Both designs show similar maximum equivalent stresses in electrical steel

**At 20,000 rpm (overspeed) + 150 K thermal load:**
- **Conventional design:** Maximum tensile strength of electrical steel EXCEEDED (plastic strain concentration, failure)
- **Novel design:** Maximum equivalent stress < 410 MPa (below yield strength, survived)
- **Fiber composite:** Only moderately stressed in novel design

### Electromagnetic Analysis (TABLE IV)

| Parameter | Unit | Initial Rotor (IR) | Novel Rotor (NR) | Abs. Deviation |
|-----------|------|---------------------|-------------------|----------------|
| Torque | Nm | 36.54 | 32.26 (35.93) | 0.96 (0.98) |
| d-Inductance | mH | 8.87 | 8.77 (8.76) | 0.99 (0.99) |
| q-Inductance | mH | 1.37 | 1.53 (1.39) | 1.15 (1.01) |
| Power Factor | - | 0.68 | 0.66 (0.68) | 0.97 (1.00) |
| Base Speed | rpm | 5477 | 5488 (5532) | 1.00 (1.01) |

**Key Findings:**
- Novel rotor torque = 88% of initial (with bone holders)
- With rib substitution: Torque = 98% of initial
- Inductance ratio improved with rib substitution
- Power factor maintained at 0.68 with optimized design
- Base speed increased slightly in novel design

## Limitations / Caveats

1. **Generic topology** — study based on generic rotor, not oriented toward specific performance class or application
2. **Simulation only** — no prototype fabrication or experimental validation (planned as future work)
3. **Glass fiber limitation** — conservative material choice; carbon/basalt fibers would improve performance
4. **Thermal expansion mismatch** — not fully analyzed for long-term reliability
5. **Manufacturing feasibility** — continuous fiber option requires further process development
6. **Cost analysis** — not included; fiber reinforced concept may have higher material cost than conventional ribs
7. **No burst testing** — structural validation pending experimental verification
8. **Cooling strategy** — not investigated in detail
9. **Rotor balancing** — consistency during operation not addressed

## Propagation Into Wiki (list pages to update with [[wikilinks]])

- [[motorcad/parameters]] — Add high-speed SynRM design parameters and constraints
- [[motorcad/workflow]] — Reference fiber reinforced rotor concept as advanced design option
- [[architecture/orchestrator]] — Update with SynRM topology optimization capabilities
- [[known_issues]] — Document mechanical limitations of conventional SynRM rotors
- [[codebase_map]] — Add references to rotor design optimization tools

## Related Pages ([[wikilinks]])

- [[motorcad/workflow]]
- [[motorcad/parameters]]
- [[motorcad/result_fields]]
- [[architecture/orchestrator]]
- [[known_issues]]
- [[active_tasks]]
