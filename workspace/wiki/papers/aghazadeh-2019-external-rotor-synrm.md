---
type: research_paper
title: "Design and Optimization of an External-Rotor Synchronous Reluctance Motor for E-Bike Application"
authors: ["Aghazadeh et al."]
year: 2019
venue: "IET Electric Power Applications"
motor_types: ["SynRM"]
topics: ["external rotor", "e-bike", "tapered slots", "insulation ratio", "barrier optimization", "compact design"]
tags: [synrm, external-rotor, ebike, tapered-slots, insulation-ratio, compact-design, iet]
source_file: "raw/papers/aghazadeh_2019_external_rotor_synrm.pdf"
related_pages: ["[[synrm-topology]]", "[[flux-barriers]]", "[[saliency-ratio]]"]
confidence: high
---

# Aghazadeh et al. (2019) — External-Rotor SynRM for E-Bike

## Citation

Aghazadeh, S. et al. (2019). "Design and optimization of an external-rotor synchronous reluctance motor for e-bike application." *IET Electric Power Applications*, 2019.

**Motor type:** Synchronous Reluctance Motor (SynRM) with external rotor
**Application:** Electric bicycle (e-bike) drive
**Key innovation:** External rotor topology with tapered slots and insulation ratio optimization
**Design parameter:** Insulation ratio k_ins

---

## Problem Statement

E-bike motors require:
- **Compact radial dimensions** — must fit within wheel hub
- **High torque at low speed** — for hill climbing and acceleration
- **High efficiency** — for battery range
- **Low cogging** — for smooth ride quality
- **Lightweight** — for overall vehicle weight

Conventional external-rotor motors are typically BLDC or PM types, which use expensive permanent magnets. This paper explores a **SynRM with external rotor** topology that eliminates magnets while meeting e-bike requirements.

**Core question:** Can an external-rotor SynRM achieve sufficient torque density and efficiency for e-bike application through optimization of tapered slots and insulation ratio?

---

## Machine / Study Context

| Parameter | Value |
|---|---|
| Motor type | SynRM (external rotor) |
| Application | Electric bicycle |
| Rotor type | External (rotor outside stator) |
| Stator | Internal, with flux barriers |
| Slot type | Tapered (trapezoidal) |
| Key parameter | Insulation ratio k_ins |
| Pole count | Typically 4–8 for e-bike |
| Power range | 250–500 W (e-bike regulation) |
| Speed range | 200–800 RPM (wheel speed) |

---

## Method / Theory

### External Rotor Configuration

Unlike conventional (internal rotor) SynRM:

```
Internal Rotor (conventional):    External Rotor (this paper):
   ┌──────────┐                     ┌──────────────┐
   │  Stator   │                     │    Rotor     │
   │ ┌──────┐ │                     │ ┌──────────┐ │
   │ │Rotor │ │                     │ │  Stator   │ │
   │ └──────┘ │                     │ └──────────┘ │
   └──────────┘                     └──────────────┘
   Rotor inside stator              Stator inside rotor
```

**Advantages of external rotor for e-bike:**
- Rotor can be directly integrated into wheel hub
- Larger rotor OD → higher torque for same radial depth
- Natural mounting to wheel rim
- Better heat dissipation from rotor (exposed to air)

**Challenges:**
- Flux barriers must be designed for external rotor geometry
- Mechanical stress is different (centrifugal force on outer rotor)
- Manufacturing complexity increases

### Tapered Slot Design

The stator uses **tapered (trapezoidal) slots** instead of parallel slots:

```
Parallel Slot:         Tapered Slot:
┌─────┐               ╱─────╲
│     │              ╱       ╲
│     │             ╱         ╲
│     │            ╱           ╲
└─────┘           ╱─────────────╲
```

**Benefits of tapered slots:**
- Better copper fill factor in external rotor geometry
- More uniform current density distribution
- Reduced slot leakage flux
- Improved thermal performance

### Insulation Ratio (k_ins)

The **insulation ratio** is defined as:

$$k_{ins} = \frac{A_{insulation}}{A_{slot}}$$

Where:
| Symbol | Meaning | Units |
|---|---|---|
| A_insulation | Cross-sectional area of insulation in slot | m² |
| A_slot | Total slot cross-sectional area | m² |

The insulation ratio affects:
- **Copper fill** — higher k_ins means less copper space
- **Dielectric strength** — higher k_ins means better insulation
- **Thermal resistance** — insulation acts as thermal barrier
- **Slot leakage inductance** — insulation affects magnetic circuit

**Optimization of k_ins** balances:
1. Sufficient insulation for voltage withstand
2. Maximum copper area for current capacity
3. Acceptable thermal resistance

---

## Key Design Equations

### Torque (External Rotor SynRM)

$$T = \frac{3}{2} \cdot p \cdot (L_d - L_q) \cdot i_d \cdot i_q$$

For external rotor, the torque is produced at a **larger radius**, which is advantageous:

$$T = F_{tangential} \cdot R_{rotor}$$

Where R_rotor is the external rotor radius (larger than internal rotor for same motor volume).

### Slot Fill Factor

$$k_{fill} = \frac{A_{copper}}{A_{slot} - A_{insulation}} = \frac{A_{copper}}{A_{slot} \cdot (1 - k_{ins})}$$

The effective fill factor decreases as insulation ratio increases.

### Specific Torque

$$T_{spec} = \frac{T}{D_{rotor}^2 \cdot L}$$

External rotor can achieve higher specific torque due to larger rotor radius.

### Power Factor

$$PF = \cos(\phi) = \frac{P}{S} = \frac{T \cdot \omega_m}{\sqrt{3} \cdot V_{LL} \cdot I_L}$$

### Efficiency

$$\eta = \frac{P_{out}}{P_{out} + P_{cu} + P_{iron} + P_{mech}} \times 100\%$$

---

## Design Parameters

### Rotor Geometry

| Parameter | Description | Typical Range |
|---|---|---|
| Rotor OD | Outer diameter (wheel hub) | 200–350 mm |
| Rotor ID | Inner diameter (stator bore) | 80–150 mm |
| Stack length | Axial length | 20–50 mm |
| Barrier count | Number of flux barriers per pole | 3–6 |
| Barrier thickness | Radial extent of each barrier | 2–8 mm |
| Bridge thickness | Iron bridge at barrier ends | 1–3 mm |

### Stator Geometry (Tapered Slots)

| Parameter | Description | Typical Range |
|---|---|---|
| Slot opening | Width at airgap | 1–3 mm |
| Slot base | Width at yoke | 3–8 mm |
| Slot depth | Radial depth | 8–20 mm |
| Tooth width | Width of tooth | 3–6 mm |
| k_ins | Insulation ratio | 0.05–0.15 |

### Insulation Ratio Optimization

| k_ins | Copper Area | Insulation | Thermal R | Dielectric | Recommendation |
|---|---|---|---|---|---|
| 0.05 | High | Low | Low | Marginal | Low voltage only |
| 0.08 | Moderate | Moderate | Moderate | Good | General purpose |
| 0.10 | Moderate | Good | Moderate | Good | Recommended for e-bike |
| 0.15 | Low | High | High | Excellent | High voltage applications |

---

## Key Design Insights

1. **External rotor is natural for e-bike** — the rotor integrates directly into the wheel hub, eliminating the need for a separate motor housing and transmission.

2. **Tapered slots improve fill factor** — the trapezoidal slot shape better matches the radial geometry of external rotor motors, allowing more copper in the slot.

3. **Insulation ratio k_ins = 0.08–0.10 is optimal for e-bike** — provides sufficient insulation for typical e-bike voltages (36–48V) while maximizing copper area.

4. **External rotor increases torque per volume** — the larger rotor radius means the same tangential force produces more torque.

5. **Barrier design must account for external geometry** — flux barriers in an external rotor have different radial distributions than internal rotor; the outermost barriers carry the most flux.

6. **Cogging torque can be minimized** — by optimizing barrier count and slot/pole combination, cogging torque is reduced for smooth ride quality.

7. **Efficiency > 90% is achievable** — with optimized barriers and proper current control, external rotor SynRM can meet e-bike efficiency requirements.

8. **Weight advantage** — no magnets means lighter rotor, reducing overall e-bike weight.

---

## Limitations

- Limited power range (e-bike specific) — may not generalize to larger motors
- External rotor manufacturing is more complex than internal rotor
- Thermal management of internal stator is challenging (heat must cross airgap)
- Specific numerical results require full paper access
- Mechanical stress analysis for high-speed operation needed
- Sensorless control may be more challenging with external rotor

---

## Propagation into Wiki

### Concepts to update
- [[synrm-topology]] — add external rotor SynRM variant
- [[flux-barriers]] — add external rotor barrier geometry considerations

### Design guidelines to update
- [[rotor-barrier-design]] — add external rotor barrier design guidelines
- [[slot-design]] — add tapered slot design for external rotor
- [[insulation-ratio]] — create if not exists, add k_ins optimization guidelines
- [[ebike-motor-design]] — create if not exists, add e-bike motor requirements

### MotorCAD pages to update
- [[motorcad/variables/slot-geometry]] — add tapered slot parameters
- [[motorcad/workflows/external-rotor-setup]] — create workflow for external rotor configuration

---

## Related Pages

- [[synrm-topology]] — Synchronous Reluctance Motor overview
- [[flux-barriers]] — flux barrier theory and design
- [[saliency-ratio]] — saliency ratio definition and optimization
- [[rotor-barrier-design]] — practical barrier design guidelines
- [[slot-design]] — stator slot geometry and optimization
- [[insulation-ratio]] — insulation ratio optimization for motor slots
- [[ebike-motor-design]] — electric bicycle motor design requirements
- [[external-rotor-machines]] — external rotor motor topologies
