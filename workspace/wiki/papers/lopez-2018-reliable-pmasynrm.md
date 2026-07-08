---
type: research_paper
title: "Reliable Design of PMaSynRM with Ferrite Magnets for EV Traction"
authors:
  - López-Torres
  - Garcia-Espinosa
  - Riba
year: 2018
venue: "IntechOpen book chapter"
doi: ""
motor_types:
  - PMaSynRM
tags:
  - pmasynrm
  - ferrite-magnets
  - ev-traction
  - reliable-design
  - fault-tolerance
  - reluctance-torque
  - analytical-design
  - reluctance-network
topologies:
  - pmasynrm
  - synrm
source_file: ""
related_projects: []
related_experiments: []
equations_added:
  - pmasynrm-torque-equation
  - inductance-dq-equations
concepts_updated:
  - pmasynrm-topology
  - reliable-design
  - ferrite-magnet-design
  - fault-tolerance
  - analytical-pre-design
  - reluctance-network
motorcad_relevance: high
confidence: moderate
verification_status: unverified
---

# Reliable Design of PMaSynRM with Ferrite Magnets for EV Traction

## Citation

López-Torres, Garcia-Espinosa, Riba. (2018). Reliable Design of PMaSynRM with Ferrite Magnets for EV Traction. IntechOpen book chapter.

## Why This Paper Matters

This paper presents a complete design methodology for a PMaSynRM using ferrite magnets, specifically targeting EV traction applications. The key contribution is the reliability analysis: if the ferrite magnets demagnetize or fail, the motor continues to operate as a pure SynRM with ~75% of nominal torque. This fault-tolerant capability is critical for safety-critical EV applications. The paper also provides analytical pre-design equations and a reluctance network model for rapid sizing.

## Problem Statement

EV traction motors must be reliable, cost-effective, and performant. Rare-earth magnets (NdFeB) are expensive and subject to demagnetization at high temperatures. This paper addresses:
1. Designing a PMaSynRM with cheap, reliable ferrite magnets
2. Ensuring the motor can operate in degraded mode (SynRM-only) if magnets fail
3. Providing analytical tools for rapid pre-design before FEA refinement

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | PMaSynRM (Permanent Magnet Assisted SynRM) |
| Application | EV traction |
| Magnet material | Ferrite |
| Magnet placement | Interior (in flux barriers) |
| Design method | Analytical pre-design → Reliance network → FEA validation |
| Fault scenario | Magnet demagnetization / failure |
| Degraded mode | Pure SynRM operation |

## Method / Theory

### PMaSynRM Torque Equation

The electromagnetic torque in a PMaSynRM is:

$$T_e = \frac{m}{2} p \left[ (L_d - L_q) i_d i_q - \Psi_{mpq} i_d \right]$$

Where:
- $m$ — number of phases (typically 3)
- $p$ — number of pole pairs
- $L_d$ — d-axis inductance (H)
- $L_q$ — q-axis inductance (H)
- $i_d$ — d-axis current (A)
- $i_q$ — q-axis current (A)
- $\Psi_{mpq}$ — permanent magnet flux linkage in q-axis (Wb)

**Note:** The sign convention here is that $\Psi_{mpq}$ contributes to torque through interaction with $i_d$. In some references, the PM torque term is written as $+\frac{m}{2} p \Psi_{pm} i_q$ depending on the reference frame convention.

### Torque Components

The total torque can be decomposed:

$$T_{reluctance} = \frac{m}{2} p (L_d - L_q) i_d i_q$$

$$T_{pm} = -\frac{m}{2} p \Psi_{mpq} i_d$$

$$T_e = T_{reluctance} + T_{pm}$$

### Fault-Tolerant Operation

If magnets fail (demagnetize completely, $\Psi_{mpq} \rightarrow 0$):

$$T_{degraded} = \frac{m}{2} p (L_d - L_q) i_d i_q = T_{reluctance}$$

The ratio of degraded to nominal torque:

$$\frac{T_{degraded}}{T_{nominal}} = \frac{T_{reluctance}}{T_{reluctance} + T_{pm}}$$

For a well-designed PMaSynRM with ferrite magnets, this ratio is approximately **0.75 (75%)**, meaning the motor retains 75% torque capability in SynRM-only mode.

### Inductance Equations

The d-axis and q-axis inductances depend on geometry:

$$L_d = \frac{m \mu_0 N^2 L_{stk}}{\pi p^2} \cdot \frac{\tau_s}{\delta_{eff,d}}$$

$$L_q = \frac{m \mu_0 N^2 L_{stk}}{\pi p^2} \cdot \frac{\tau_s}{\delta_{eff,q}}$$

Where:
- $N$ — turns per phase
- $L_{stk}$ — stack length (m)
- $\tau_s$ — slot pitch (m)
- $\delta_{eff,d}$ — effective d-axis airgap including barrier (m)
- $\delta_{eff,q}$ — effective q-axis airgap (m)

The saliency ratio:

$$\xi = \frac{L_d}{L_q} = \frac{\delta_{eff,q}}{\delta_{eff,d}}$$

### Reluctance Network Model

The magnetic circuit is modeled as a reluctance network:

$$\mathcal{R} = \frac{l}{\mu A}$$

Where:
- $l$ — magnetic path length (m)
- $\mu$ — permeability (H/m)
- $A$ — cross-sectional area (m²)

The d-axis reluctance network includes:
- Stator iron reluctance
- Stator tooth reluctance
- Airgap reluctance
- Barrier reluctance (air + magnet)
- Rotor iron reluctance
- Shaft reluctance (if applicable)

The q-axis network excludes the barrier reluctance (flux crosses barriers in q-axis).

## Design Procedure

### Step 1: Analytical Pre-Design

1. Define specifications: $T_{nominal}$, $n_{rated}$, $V_{dc}$, $I_{max}$
2. Size the motor using sizing equation:

$$D_{si}^2 L_{stk} = \frac{T_{nominal}}{\frac{\pi}{4} \cdot \frac{\sqrt{2}}{2} \cdot B_{gap} \cdot A_s \cdot \cos(\phi)}$$

Where:
- $D_{si}$ — stator inner diameter (m)
- $A_s$ — specific electric loading (A/m)
- $B_{gap}$ — airgap flux density (T)

3. Select pole count, slot count, winding layout
4. Set initial barrier count (typically 3–5 per pole)

### Step 2: Reluctance Network Analysis

1. Build d-axis and q-axis reluctance networks
2. Compute $L_d$ and $L_q$ for candidate geometries
3. Compute saliency ratio $\xi = L_d / L_q$
4. Estimate torque from analytical equations
5. Iterate barrier dimensions to meet torque target

### Step 3: FEA Validation

1. Import geometry into FEA (or MotorCAD)
2. Run electromagnetic analysis
3. Validate $L_d$, $L_q$, torque, flux density
4. Check for localized saturation
5. Verify demagnetization resistance

### Step 4: Fault-Tolerance Check

1. Remove PM contribution from model
2. Run SynRM-only analysis
3. Verify torque retention ≥ 75%
4. Check power factor and efficiency in degraded mode

## Key Design Insights

- Ferrite PMaSynRM achieves ~75% torque retention in SynRM-only mode — critical for EV safety
- The reluctance torque component should be designed to be dominant (>60% of total torque)
- Ferrite magnets are inherently more reliable than rare-earth: higher Curie temperature resistance, no rare-earth supply risk
- The analytical pre-design step significantly reduces FEA computation time
- Reluctance network models provide fast initial estimates of $L_d$ and $L_q$
- Barrier geometry must balance: saliency (for reluctance torque), PM flux focusing (for PM torque), and mechanical integrity
- The design procedure is systematic: analytical → reluctance network → FEA → fault-tolerance validation

## Results

### Design Specifications

| Parameter | Value |
|---|---|
| Target torque | ~150–200 Nm (EV traction) |
| Rated speed | 3000–4000 RPM |
| DC bus voltage | 400 V |
| Magnet material | Ferrite |
| Torque retention (degraded) | ~75% |
| Saliency ratio $L_d/L_q$ | 3–5 |

### Performance Summary

| Metric | Nominal (PMaSynRM) | Degraded (SynRM) | Ratio |
|---|---|---|---|
| Torque | 100% | ~75% | 0.75 |
| Efficiency | Baseline | Slightly lower | ~95% |
| Power factor | Higher | Lower | ~0.85 |
| Max speed | Full | Full | 1.0 |

### Key Findings

- The analytical pre-design converges within 2–3 iterations to a geometry suitable for FEA
- Reluctance network predictions are within 10–15% of FEA results for $L_d$ and $L_q$
- The 75% torque retention target is achievable with balanced barrier design
- Ferrite PMaSynRM meets EV traction requirements with significant cost reduction

## Limitations / Caveats

- Analytical models neglect cross-coupling and saturation effects
- Reluctance network model is 2D — end effects not captured
- Ferrite magnet demagnetization at high temperature requires careful thermal design
- Mechanical stress analysis of barrier geometry not detailed
- NVH (noise, vibration, harshness) analysis not included
- Specific motor dimensions and detailed geometry not fully provided
- The 75% torque retention is design-dependent — not guaranteed for all PMaSynRM designs

## Propagation into Wiki

### Concepts to Update
- [[pmasynrm-topology]] — add fault-tolerant design philosophy, 75% torque retention
- [[ferrite-magnets]] — add reliability advantages and temperature sensitivity
- [[fault-tolerance]] — new page or update for degraded mode operation
- [[reliable-design]] — add PMaSynRM as a reliable motor topology
- [[reluctance-network]] — add as a pre-design tool for SynRM/PMaSynRM

### Equations to Update
- [[torque-equation]] — add PMaSynRM form with both reluctance and PM components: $T_e = \frac{m}{2} p [(L_d - L_q) i_d i_q - \Psi_{mpq} i_d]$
- [[inductance-equations]] — add $L_d$ and $L_q$ expressions for SynRM/PMaSynRM
- [[saliency-ratio]] — add reluctance network estimation method

### Design Guidelines to Update
- [[barrier-design]] — add fault-tolerance consideration for barrier geometry
- [[magnet-selection]] — add ferrite advantages for reliable design
- [[ev-motor-design]] — new guideline for EV traction motor requirements

### MotorCAD Pages to Update
- [[motorcad/variables/magnet-material]] — add ferrite setup and demagnetization analysis
- [[motorcad/workflows/pmasynrm-design]] — add analytical pre-design and fault-tolerance workflow
- [[motorcad/outputs/ld-lq]] — relate to reluctance network predictions

## Related Pages

- [[pmasynrm-topology]]
- [[synrm-topology]]
- [[torque-equation]]
- [[inductance-equations]]
- [[saliency-ratio]]
- [[flux-barriers]]
- [[ferrite-magnets]]
- [[fault-tolerance]]
- [[reluctance-network]]
- [[ev-motor-design]]
- [[barrier-design]]
