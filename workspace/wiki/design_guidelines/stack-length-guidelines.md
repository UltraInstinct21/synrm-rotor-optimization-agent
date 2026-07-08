---
type: design_guideline
title: Stack Length Guidelines
aliases: [stack-length, axial-length, l-d-ratio]
tags: [synrm, sizing, stack-length, thermal, manufacturing, design-guideline]
motor_types: [synrm, pmasynrm, ipmsm, spm, induction]
topics: [stack-length, sizing, l-d-ratio, thermal-management, manufacturing]
related_pages: [sizing-equation, synrm-topology, thermal-limits]
source_files: []
confidence: high
---

# Stack Length Guidelines

## Purpose

Stack length (L) is a primary sizing parameter that, together with rotor diameter (D), determines the motor's torque capability, thermal behavior, efficiency, and manufacturability. This page provides guidelines for selecting stack length, the L/D ratio, and the tradeoffs involved.

---

## Fundamental Relation

### Torque vs. stack length

For a given rotor diameter and airgap flux density, torque scales approximately linearly with stack length:

$$T \propto B_{gap} \cdot A \cdot D^2 \cdot L$$

Where:
- B_gap = airgap flux density (T)
- A = specific electric loading (A/m)
- D = rotor diameter (m)
- L = stack length (m)

### Design implication

- Doubling stack length approximately doubles torque (with the same D, B, A).
- Alternatively, for the same torque, a longer stack allows a smaller D, which may reduce material cost or allow a smaller frame.

---

## Form Factor (X)

### Definition

The form factor X relates rotor diameter D and stack length L:

$$X = \frac{\pi}{4\sqrt{p}} \cdot \frac{L}{D}$$

Where:
- X = form factor
- p = number of pole pairs
- L = stack length (m)
- D = rotor diameter (m)

### Typical values

| Application | X | L/D |
|---|---|---|
| Small motors (<5 kW) | 0.3–0.6 | 0.5–1.0 |
| Medium motors (5–50 kW) | 0.5–1.0 | 0.8–1.5 |
| Large motors (>50 kW) | 0.8–1.5 | 1.0–2.0 |
| High-speed motors | 0.3–0.6 | 0.3–0.8 |
| Low-speed, high-torque | 1.0–2.0 | 1.5–3.0 |

### Selection guidance

- **Short stack (L/D < 0.5)**: Better cooling, easier manufacturing, lower deflection, but lower torque density per unit volume.
- **Medium stack (L/D = 0.5–1.5)**: Most common industrial range, good balance.
- **Long stack (L/D > 1.5)**: Higher torque density, but harder to cool, more deflection, more complex mechanical design.

---

## Typical L/D Ratio for SynRM

| Power range | Recommended L/D | Notes |
|---|---|---|
| 0.5–5 kW | 0.5–1.0 | Small frame, manufacturing dominated |
| 5–45 kW | 0.8–1.5 | Industrial sweet spot |
| 45–200 kW | 1.0–2.0 | Larger frame, thermal design important |
| >200 kW | 1.5–3.0 | Custom design, thermal management critical |

---

## Thermal Considerations

### Heat generation

- Total copper loss ∝ I²R ∝ L (longer stack → more winding → more loss).
- Total iron loss ∝ L (longer stack → more lamination volume → more loss).
- **Total losses scale linearly with L** (approximately).

### Heat removal

- Primary cooling path is radial (through stator teeth and frame).
- Axial heat conduction is limited (lamination stacking direction has low thermal conductivity).
- **Longer stack → heat must travel farther axially to reach end-windings → higher peak temperature.**

### Thermal design rule

$$T_{hotspot} \propto \frac{L^2}{k_{axial}}$$

Where:
- T_hotspot = peak winding temperature above coolant
- k_axial = effective axial thermal conductivity

### Practical implications

- For L > 150 mm, consider **additional cooling features** (e.g., axial cooling channels, spray cooling).
- For L > 250 mm, **thermal management becomes a primary design constraint**.
- CFD or thermal FEA should be used for stacks longer than 200 mm.

---

## Manufacturing Considerations

### Lamination pressing

- Longer stacks require higher pressing force during assembly.
- Lamination deflection during pressing increases with L².
- **Practical pressing limit**: ~300 mm for standard equipment; >300 mm requires specialized fixtures.

### Lamination alignment

- Longer stacks are harder to align during stacking.
- Stacking errors accumulate → rotor eccentricity increases.
- **Tolerance**: ±0.05 mm radial alignment for stacks up to 200 mm; tighter tolerance needed for longer stacks.

### Machining

- Rotor shaft and OD machining: longer stacks require more rigid fixturing to avoid runout.
- Balancing: longer rotors are harder to balance (more bearing span, more modes).

### Cost implication

- Stack length increases material cost linearly.
- Manufacturing complexity increases non-linearly for L > 200 mm.
- There is usually an **optimal L/D ratio** that minimizes total cost for a given torque requirement.

---

## Mechanical Considerations

### Deflection

- Rotor deflection under magnetic pull and gravity increases with L³ (beam theory).
- **Minimum bearing span** should be at least 0.3× L to limit deflection.
- For L > 200 mm, intermediate bearings or a stiffer shaft may be needed.

### Critical speed

- First critical speed of the rotor decreases with L.
- For high-speed applications, shorter stacks are preferred to keep critical speed above operating range.

### Vibration

- Longer stacks have more vibration modes.
- Modal analysis should be performed for L > 150 mm.

---

## Effect on Electromagnetic Performance

### Torque ripple

- Stack length does not directly affect torque ripple percentage.
- However, longer stacks may have more manufacturing variation → slight increase in unbalanced magnetic pull.

### Cogging torque

- Cogging torque magnitude increases with L (more magnet/teeth interacting).
- Cogging torque percentage (relative to average torque) is approximately constant.

### Efficiency

- Longer stacks generally improve efficiency slightly because the fixed losses (core loss per unit volume) are amortized over more active material.
- This effect is small and usually secondary to thermal and mechanical constraints.

---

## Design Decision Framework

```
1. Determine torque requirement
2. Select rotor diameter (based on speed, voltage, frame size)
3. Calculate required L from sizing equation
4. Check L/D ratio against typical range
5. Check thermal limits (FEA or analytical)
6. Check mechanical limits (deflection, critical speed)
7. Check manufacturing limits (pressing, alignment)
8. Iterate if constraints are violated
```

### Common iterations

- If L/D is too high → increase D, reduce L (need larger frame).
- If L/D is too low → reduce D, increase L (may need higher current density).
- If thermal limit is exceeded → reduce current density, add cooling, or reduce L.
- If mechanical deflection is too high → increase shaft diameter, reduce L, or add bearings.

---

## References

- Pyrhönen, J. — rotational electrical machines (sizing theory)
- Boldea, I. — reluctance synchronous motors (design methodology)
- Gieras, J. — permanent magnet motor technology (form factor discussion)

---

## Related Pages

- [[sizing-equation]] — fundamental torque-volume relationship
- [[synrm-topology]] — overall SynRM design considerations
- [[thermal-limits]] — winding temperature limits and cooling methods
- [[airgap-guidelines]] — airgap selection and its interaction with stack length
