---
type: research_paper
title: "High-Speed Synchronous Reluctance Motor Rotor with Glass Fiber Reinforced Bone-Shaped Struts"
authors:
  - Hausmann
  - Heim
  - Waldhof
  - Fischer
  - Fleischer
  - Wößner
  - Flammer
  - Parspour
year: 2020
venue: IEEE Conference
motor_types:
  - SynRM
tags:
  - high-speed
  - rotor-structural
  - fiber-reinforcement
  - flux-barriers
  - mechanical-stress
  - synrm
source_file: hausmann-2020-high-speed-synrm.pdf
related_pages:
  - [[synrm-topology]]
  - [[flux-barriers]]
  - [[rotor-bridge-design]]
---

# High-Speed SynRM Rotor with Glass Fiber Reinforced Bone-Shaped Struts

## Citation

Hausmann, Heim, Waldhof, Fischer, Fleischer, Wößner, Flammer, and Parspour, "High-Speed Synchronous Reluctance Motor Rotor with Glass Fiber Reinforced Bone-Shaped Struts," IEEE Conference, 2020.

---

## Problem Statement

Synchronous Reluctance Motors (SynRMs) offer advantages such as no permanent magnets, low cost, and high robustness. However, achieving high mechanical integrity at high rotational speeds is a major challenge. The rotor flux barriers significantly weaken the mechanical structure, and conventional rib designs fail at speeds above ~18,000 rpm for the studied geometry. This paper proposes a novel rotor reinforcement method using glass fiber reinforced bone-shaped structural struts to survive extreme centrifugal stresses.

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor Type | SynRM (Interior U-shape) |
| Stator OD | 250 mm |
| Stator Bore | 130 mm |
| Active Length | 180 mm |
| Pole Count | 4 |
| Slot Count | 36 |
| Speed Range | Up to 20,000 rpm |

The study focuses on a high-speed SynRM for applications requiring rotational speeds well above standard industrial ranges.

---

## Key Equations

### Reluctance Torque

$$T = \frac{3}{2} \cdot \frac{P}{2} \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

Where:
- $T$ — electromagnetic torque [Nm]
- $P$ — pole pair number
- $L_d$ — d-axis inductance [H]
- $L_q$ — q-axis inductance [H]
- $i_d, i_q$ — d-axis and q-axis currents [A]

The torque is proportional to the inductance difference $(L_d - L_q)$, which is the fundamental torque production mechanism of SynRMs. Maximizing this difference while maintaining structural integrity is the core design challenge.

---

## Rotor Concepts Reviewed

The paper surveys multiple rotor structural concepts for high-speed SynRMs:

### Conventional Ribs
- Thin iron bridges at flux barrier edges
- Provides minimal mechanical connection between rotor segments
- Fails at approximately 18,000–20,000 rpm for this geometry
- Stress concentration at rib tips is the primary failure mode

### Segmented Core
- Rotor laminations segmented into independent blocks
- Improved mechanical robustness over continuous laminations
- Manufacturing complexity increases significantly

### Two-Metal Alloys
- Rotor fabricated from two materials with different mechanical properties
- Allows selective reinforcement
- Cost and manufacturing challenges limit practical adoption

### Bolted Rotor
- Mechanical fasteners hold rotor segments together
- Effective but introduces additional mass and assembly complexity
- Bolt holes create new stress concentration points

### Fiber Sleeve
- Carbon or glass fiber sleeve shrunk-fit over the rotor
- Provides compressive pre-stress to counteract centrifugal forces
- Well-established for IPM rotors but requires careful thermal matching

### Epoxy Resin
- Structural adhesive fills flux barriers
- Low density and moderate strength
- Limited by thermal degradation and creep at high temperatures

### 3D Printing
- Additive manufacturing enables complex geometries
- Material properties may not match laminated steel
- Emerging technology, not yet validated for high-speed production

---

## Novel Concept: Glass Fiber Reinforced Bone-Shaped Struts

### Design Description

The proposed concept introduces bone-shaped struts made from glass fiber reinforced polymer (GFRP) inserted into the flux barrier regions. The struts mechanically connect the inner and outer rotor segments across the barriers.

### Key Features
- **Bone-shaped geometry**: Wider at the ends (for load distribution) and narrower in the middle (to allow flux passage)
- **Glass fiber reinforcement**: Provides high tensile strength and stiffness
- **Minimal flux interference**: Geometry optimized to reduce flux path obstruction
- **Mechanical continuity**: Maintains structural integrity across flux barriers at high speed

### Manufacturing Considerations
- Struts can be manufactured separately and inserted during rotor assembly
- Glass fiber provides good strength-to-weight ratio
- Compatible with existing lamination stacking processes

---

## FEA Results

### Structural Performance

| Rotor Concept | Maximum Speed Survived |
|---|---|
| Conventional ribs | < 20,000 rpm (failure) |
| Glass fiber reinforced bone-shaped struts | ≥ 20,000 rpm (survival) |

The conventional rib design fails at approximately 20,000 rpm due to excessive centrifugal stress exceeding material yield strength. The bone-shaped strut concept successfully survives the target speed with acceptable stress margins.

### Electromagnetic Performance

| Parameter | Value |
|---|---|
| Torque | 32.26 Nm |
| $L_d$ | 8.77 mH |
| $L_q$ | 1.53 mH |
| Saliency Ratio ($L_d/L_q$) | 5.73 |
| Power Factor | 0.66 |

The electromagnetic performance remains acceptable despite the structural modifications. The saliency ratio of 5.73 indicates good reluctance torque capability. The power factor of 0.66 is typical for SynRMs without permanent magnets.

---

## Design Insights

1. **Structural-Electromagnetic Tradeoff**: Flux barriers weaken the rotor mechanically. Reinforcement must balance structural integrity with flux path preservation.
2. **Bone-Shaped Geometry**: The wider ends provide mechanical load distribution while the narrow middle section minimizes flux obstruction.
3. **Fiber Reinforcement Viability**: Glass fiber reinforced polymer provides sufficient strength for high-speed SynRM rotors at a reasonable cost.
4. **Speed Capability**: The proposed concept extends the safe operating speed from ~18,000 rpm to ≥ 20,000 rpm for the studied geometry.
5. **Manufacturing Feasibility**: The strut approach is compatible with existing lamination-based manufacturing processes.

---

## Limitations

- Study limited to 250 mm OD / 130 mm bore geometry
- Only glass fiber was evaluated (carbon fiber not compared)
- Long-term thermal cycling effects on GFRP not addressed
- Manufacturing cost analysis not provided
- No experimental validation — FEA only

---

## Propagation into Wiki

### Concepts to Update
- [[flux-barriers]] — add structural reinforcement aspect
- [[rotor-bridge-design]] — add fiber-reinforced strut alternative
- [[synrm-topology]] — add high-speed design considerations

### Equations to Update
- [[torque-equation]] — reference this paper for reluctance torque context

### Design Guidelines to Update
- [[rotor-speed-limits]] — create if not exists; add strut-based speed extension
- [[flux-barrier-reinforcement]] — create if not exists

### MotorCAD Pages to Update
- [[motorcad/variables/rotor-geometry]] — note high-speed structural constraints

---

## Related Pages

- [[synrm-topology]]
- [[flux-barriers]]
- [[rotor-bridge-design]]
- [[torque-equation]]
- [[high-speed-motor-design]]
