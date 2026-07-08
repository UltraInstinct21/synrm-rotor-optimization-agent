---
type: topology
title: Interior Permanent Magnet Synchronous Motor (IPMSM)
aliases: [IPMSM, IPM, Interior PM Motor]
tags: [topology, ipmsm, pm, synchronous, rare-earth, high-performance]
motor_type: ipmsm
topics: [operating-principle, rotor-design, torque-production, field-weakening, optimization]
related_pages: [pmasynrm-topology, synrm-topology, flux-barriers, dq-theory, torque-equation, power-factor]
confidence: verified
---

# Interior Permanent Magnet Synchronous Motor (IPMSM)

## Operating Principle

The IPMSM produces torque through **both PM torque and reluctance torque**:

$$T = \frac{3}{2} p \left[ \lambda_{PM} i_q + (L_d - L_q) i_d i_q \right]$$

- **PM torque** ($\lambda_{PM} i_q$): Interaction between PM flux and q-axis current
- **Reluctance torque** ($(L_d - L_q) i_d i_q$): Magnetic saliency from rotor geometry

In a well-designed IPMSM, PM torque typically contributes **70–90%** of total torque, with reluctance torque contributing **10–30%**. This is the key distinction from [[pmasynrm-topology]], where reluctance torque contributes more significantly.

### Field Weakening Capability

The IPMSM's primary advantage over [[pmasynrm-topology]] is superior **field weakening** capability:

- Negative d-axis current opposes PM flux
- Allows operation above base speed
- Wide constant-power speed range (CPSR)
- Reluctance torque continues to contribute in field-weakened region
- No demagnetization risk if properly designed

## Rotor Construction

The IPMSM rotor embeds permanent magnets **inside the rotor lamination stack**, below the rotor surface. This is fundamentally different from Surface PM (SPM) motors where magnets are mounted on the rotor surface.

### Magnet Configurations

| Configuration | Description | Saliency | Applications |
|---|---|---|---|
| Flat (rectangular) | Magnets in rectangular slots | Low-moderate | General purpose |
| V-shape | Two magnets per pole in V-arrangement | Moderate-high | EV traction |
| spoke-type | Magnets radiate outward | High | High-torque applications |
| multi-barrier | Multiple magnet layers | High | Premium EV motors |
| double-V | Two V-shapes per pole | Very high | High-performance EV |
| Delta | Triangular magnet arrangement | High | Research/prototype |

### V-Shape Configuration (Most Common for EV)

The V-shape is the **dominant configuration** for EV traction because it offers:

- Good saliency ratio (Ld ≠ Lq)
- High flux concentration
- Mechanical robustness
- Good field weakening performance
- Moderate manufacturing complexity

### Rotor Geometry Parameters

Key design variables for IPMSM rotor:

- Magnet width and thickness
- V-angle (angle between magnets in V-shape)
- Magnet depth (distance from air gap)
- Bridge thickness (mechanical retention)
- Barrier dimensions (between magnet and rotor surface)
- Magnet grade and grade selection

These parameters are often optimized using **Bezier curves** or **parameterized geometry** for smooth optimization.

### Flux Barriers in IPMSM

IPMSM rotors often include **flux barriers** (air pockets) in addition to magnet slots:

- Barriers around magnets reduce leakage flux
- Barriers between poles shape the flux path
- Barrier geometry affects saliency ratio
- Same design principles as [[flux-barriers]] in SynRM apply

## Stator Design

IPMSM typically uses **distributed windings** for sinusoidal MMF:

- 3-phase, distributed winding
- 48-slot or 36-slot common for 4-pole
- Short-pitched coils to reduce harmonics
- High slot fill factor for maximum torque

### Concentrated Windings (Emerging)

Some modern IPMSM designs use **concentrated windings**:
- Shorter end-windings
- Higher copper utilization
- Reduced manufacturing cost
- May increase torque ripple and harmonics

## Key Performance Characteristics

### Torque Density

IPMSM achieves the **highest torque density** of all motor types:

- High remanence NdFeB magnets provide strong air-gap flux
- Reluctance torque adds 10–30% to total torque
- Compact rotor with embedded magnets
- V-shape flux concentration amplifies air-gap flux

Typical torque density: 40–80 Nm/L (depending on size and cooling)

### Efficiency

IPMSM achieves **excellent efficiency** across a wide operating range:

- High efficiency at rated point (95–97%)
- Good partial-load efficiency
- Low losses at high speeds (reduced flux)
- IE5+ achievable with optimized design

Losses:
- Stator copper losses (dominant at low speed/high torque)
- Stator iron losses (dominant at high speed)
- Rotor magnet eddy current losses (small but non-zero)
- Mechanical losses (bearings, windage)

### Power Factor

IPMSM typically achieves **high power factor**:
- 0.85–0.95 at rated load
- PM flux provides magnetizing flux
- Reduced reactive current from inverter
- Better than [[synrm-topology]] and [[pmasynrm-topology]]

### Cogging Torque

A significant concern for IPMSM:
- Caused by PM flux interaction with stator slots
- Contributes to torque ripple and vibration
- Mitigation techniques: skewing, slot-pole combination optimization, magnet shaping

## Advantages

| Advantage | Explanation |
|---|---|
| Highest torque density | Strong PM flux + reluctance torque |
| Excellent efficiency | 95–97% at rated, IE5+ |
| Wide field weakening range | CPSR 3:1 or more |
| High power factor | 0.85–0.95, reduces inverter sizing |
| High speed capability | Magnets protected inside rotor |
| Good partial-load efficiency | Important for variable-speed drives |
| Mature technology | Well-understood, widely manufactured |
| High starting torque | Immediate full torque from standstill |

## Disadvantages

| Disadvantage | Explanation |
|---|---|
| Rare-earth magnets | NdFeB cost and supply chain risk |
| Complex rotor | Multiple magnet layers, precise geometry |
| Cogging torque | PM-slot interaction causes vibration |
| Demagnetization risk | At high temperature or fault currents |
| High manufacturing cost | Magnet insertion, bonding, rotor assembly |
| Magnet eddy currents | Losses from harmonics, requires segmentation |
| Thermal sensitivity | Magnet properties degrade with temperature |
| Finite field weakening | Limited by demagnetization constraint |

## Rotor Geometry Optimization

### Bezier Curve Optimization

Modern IPMSM design uses **Bezier curves** to parameterize magnet and barrier shapes:

- Smooth geometry representation
- Fewer design variables
- Better optimization convergence
- Avoids sharp corners that cause flux concentration

### Multi-Objective Optimization

IPMSM rotor optimization typically balances:
- Torque (maximize)
- Torque ripple (minimize)
- Cogging torque (minimize)
- Efficiency (maximize)
- Field weakening range (maximize)
- Mechanical integrity (constraint)
- Manufacturing feasibility (constraint)

### Key Design Trade-offs

| Trade-off | Description |
|---|---|
| Torque vs. ripple | Higher torque often increases ripple |
| Saliency vs. flux | More barriers increase saliency but reduce flux |
| Magnet volume vs. cost | More magnet = more torque but higher cost |
| Bridge thickness vs. saliency | Thicker bridges reduce saliency but improve strength |
| Magnet depth vs. field weakening | Deeper magnets improve CPSR but reduce torque |

## Applications

### Primary Applications

- **Electric vehicle traction** — dominant motor type for EVs
- **Industrial servo drives** — high torque density and precision
- **HVAC compressors** — high efficiency at variable speed
- **Industrial pumps and fans** — IE5 efficiency

### EV Traction Specifically

IPMSM is the **standard choice** for EV traction because:
- Highest torque density → compact packaging
- Wide CPSR → single-speed transmission possible
- High efficiency → maximum range
- Good field weakening → high-speed cruising
- Proven reliability in automotive applications

### Comparison with Alternatives

| Application | Best topology | Reason |
|---|---|---|
| EV traction (performance) | IPMSM | Highest torque density, CPSR |
| EV traction (cost) | [[pmasynrm-topology]] | No rare-earth option |
| Industrial drive (cost) | [[synrm-topology]] | Lowest cost |
| High-reliability | [[srm-topology]] | Fault tolerance |
| High-precision servo | IPMSM | Smooth torque, high bandwidth |

## Thermal Considerations

### Magnet Temperature

- NdFeB remanence decreases ~0.1%/°C
- Coercivity decreases ~0.5–0.6%/°C
- Maximum operating temperature depends on grade (120–200°C)
- Thermal demagnetization must be checked under worst-case conditions

### Cooling Methods

- Water jacket cooling (most common for EV)
- Oil spray cooling
- Direct oil cooling (emerging)
- Air cooling (low-cost applications)

## Research References

### Key Design Topics

- V-shape magnet optimization
- Bezier curve parameterization for rotor geometry
- Multi-objective optimization (torque, ripple, efficiency, CPSR)
- Demagnetization withstand capability
- Manufacturing processes for magnet insertion

### Comparison with PMaSynRM

- IPMSM uses higher-grade magnets (NdFeB) → higher torque density
- [[pmasynrm-topology]] can use ferrite → lower cost, no rare earth
- IPMSM reluctance contribution is smaller percentage of total torque
- PMaSynRM has higher reluctance torque percentage

## Key Equations

- Torque: [[torque-equation]]
- dq model: [[dq-theory]]
- Saliency ratio: [[saliency-ratio]]
- Power factor: [[power-factor]]
- PM flux linkage: depends on magnet grade, volume, and rotor geometry

## Related Pages

- [[pmasynrm-topology]] — PM-assisted SynRM (lower PM contribution)
- [[synrm-topology]] — Pure reluctance motor (no magnets)
- [[flux-barriers]] — Flux barrier design principles
- [[dq-theory]] — dq reference frame theory
- [[torque-equation]] — Torque production equations
- [[power-factor]] — Power factor analysis
- [[saliency-ratio]] — Saliency ratio definition
- [[torque-ripple]] — Torque ripple analysis

## Tags

#topology #ipmsm #pm #synchronous #rare-earth #ndfeb #ev-traction #high-performance #field-weakening #v-shape
