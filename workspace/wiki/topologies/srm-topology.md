---
type: topology
title: Switched Reluctance Motor (SRM)
aliases: [SRM, Switched Reluctance]
tags: [topology, srm, reluctance, switched, no-magnet, simple]
motor_type: srm
topics: [operating-principle, rotor-design, torque-production, torque-ripple, control]
related_pages: [synrm-topology, torque-ripple, torque-equation]
confidence: verified
---

# Switched Reluctance Motor (SRM)

## Operating Principle

The SRM produces torque through **reluctance torque** with **sequential phase excitation**. Unlike the [[synrm-topology]], which uses a sinusoidally excited stator and synchronous operation, the SRM uses:

- **Concentrated stator windings** (one coil per pole)
- **Sequential phase energization** synchronized to rotor position
- **Asymmetric half-bridge converter** for independent phase control

When a phase is energized, the rotor poles are pulled toward alignment with the energized stator poles (minimum reluctance position). Torque is produced as the rotor moves toward the aligned position.

### Torque Production Mechanism

The instantaneous torque for a single phase is:

$$T = \frac{1}{2} i^2 \frac{dL(\theta)}{d\theta}$$

Where:
- $i$ = phase current
- $L(\theta)$ = phase inductance (function of rotor position)
- $\frac{dL}{d\theta}$ = inductance slope

**Key insight**: Torque is proportional to $i^2$ and $\frac{dL}{d\theta}$. Torque direction is independent of current polarity — only the inductance slope matters.

### Operating Regions

| Region | Inductance slope | Torque |
|---|---|---|
| Unaligned → Aligned | $\frac{dL}{d\theta} > 0$ | Motoring (positive torque) |
| Aligned → Unaligned | $\frac{dL}{d\theta} < 0$ | Generating (negative torque) |

## Rotor Construction

The SRM rotor is the **simplest of all motor types**:

- **No windings** — solid or laminated steel
- **No magnets** — pure reluctance rotor
- **No cage** — synchronous operation
- **Salient poles** — typically 8, 12, or 16 poles (for 6, 12, or 8 stator poles)

### Rotor Pole Configurations

| Stator poles | Rotor poles | Phases | Common use |
|---|---|---|---|
| 6 | 4 | 3 | Low-cost drives |
| 8 | 6 | 3 | Industrial drives |
| 12 | 8 | 3 | High-torque applications |
| 16 | 12 | 3 | Smooth torque applications |

### Rotor Geometry

- Simple salient pole shape
- No flux barriers (unlike [[synrm-topology]])
- Uniform air gap (constant except at pole tips)
- Mechanically very robust — can operate at very high speeds

## Stator Design

- **Concentrated windings**: One coil around each stator pole
- **No distributed winding**: Unlike SynRM or IPMSM
- **Independent phases**: Each phase is electrically isolated
- **No mutual coupling** (ideally) between phases

### Stator Winding Advantages

- Short end-windings → high copper utilization
- Simple manufacturing → low cost
- Independent phase control → fault tolerance
- No phase-to-phase insulation concerns

## Converter Topology

The SRM requires a **specialized converter** — it cannot use a standard 3-phase inverter:

### Asymmetric Half-Bridge

- Two switches per phase (one high-side, one low-side)
- Two diodes per phase for freewheeling
- Independent phase control
- Fault-tolerant: one phase failure doesn't disable others

### Converter Advantages

- No shoot-through risk (series switches)
- Simple gate drive requirements
- Fault tolerance per phase
- Regenerative braking capability

## Key Performance Characteristics

### Torque Ripple

**The most significant limitation of SRMs.** Torque ripple arises from:

- Discrete phase transitions (commutation)
- Current chopping during conduction
- Inductance profile nonlinearity
- Saturation effects at high currents

Typical torque ripple: 10–30% (can be reduced with advanced control)

See [[torque-ripple]] for detailed analysis.

### Acoustic Noise and Vibration

SRMs are inherently **noisier** than other motor types due to:

- Radial magnetic forces causing stator deformation
- Torque ripple exciting mechanical resonances
- Switching frequency harmonics
- Radial force pulsations at phase commutation

### Power Factor

- SRM power factor is **not well-defined** in the traditional sense
- The converter draws current independently of load angle
- Input power factor depends on converter control strategy
- Typically 0.8–0.9 with proper control

### Efficiency

- **Competitive with induction motors** at rated load
- No rotor copper losses
- Low copper losses (concentrated windings)
- Iron losses can be significant at high speeds
- Efficiency drops at light loads due to fixed excitation

### Speed Range

- Very wide speed range achievable (10:1 or more)
- No back-EMF limitation (no magnets)
- Field weakening is inherent — reduce current pulse width
- High-speed operation straightforward

## Advantages

| Advantage | Explanation |
|---|---|
| Very simple construction | Rotor: laminated steel only |
| Low cost | No magnets, no windings on rotor, simple stator |
| Very robust | No magnets to crack, no windings to fail |
| High speed capability | No magnet retention, simple rotor |
| Wide speed range | 10:1 or more with simple control |
| Fault tolerant | Independent phases, no mutual coupling |
| High temperature operation | No magnets to demagnetize |
| Simple manufacturing | Concentrated windings, simple rotor |
| No rare-earth materials | All steel and copper |
| Good starting torque | High torque at low speeds |

## Disadvantages

| Disadvantage | Explanation |
|---|---|
| High torque ripple | Discrete phase transitions, inductance profile |
| Acoustic noise | Radial forces, torque ripple |
| Vibration | Stator deformation from radial forces |
| Position sensor required | Accurate rotor position needed for commutation |
| Specialized converter | Cannot use standard 3-phase inverter |
| Lower torque density | Reluctance torque only, lower utilization |
| Current pulsations | High peak currents during conduction |
| Complex control | Current control, commutation optimization |
| Lower PF than IPMSM | Converter input characteristics |

## Applications

### Primary Applications

- **Aerospace actuators** — fault tolerance, high speed, robustness
- **Automotive starter/generators** — wide speed range, high starting torque
- **Appliance drives** — low cost, simple construction
- **Mining equipment** — robustness, no sparking risk

### Niche Applications

- **Vacuum cleaners** — high speed, low cost
- **Washing machines** — variable speed, robust
- **Power tools** — simple, cheap, high torque
- **Traction (emerging)** — with advanced torque ripple control

### Not Ideal For

- Applications requiring very smooth torque (use [[synrm-topology]] or [[ipmsm-topology]])
- High-precision servo (use [[ipmsm-topology]])
- Applications with strict noise requirements

## Control Strategies

### Current Chopping Control (CCC)

- Used at low speeds
- Hysteresis current control within each phase
- High torque ripple but simple

### Angle Position Control (APC)

- Used at medium to high speeds
- Fixed turn-on/turn-off angles
- Current controlled by back-EMF

### Single Pulse Control

- Used at high speeds
- One current pulse per phase per cycle
- Maximum power operation

### Torque Ripple Minimization

- Instantaneous torque control
- Torque sharing functions
- Active damping techniques
- Advanced current profiling

## Comparison with Other Reluctance Motors

| Feature | SRM | [[synrm-topology]] |
|---|---|---|
| Stator winding | Concentrated | Distributed |
| Excitation | Sequential DC pulses | Sinusoidal AC |
| Converter | Asymmetric half-bridge | Standard 3-phase inverter |
| Torque ripple | High (10–30%) | Moderate (5–15%) |
| Noise | High | Low-moderate |
| Rotor structure | Salient poles | Flux barriers |
| Position sensor | Required | Not required (synchronous) |
| Control complexity | High | Moderate |

## Key Equations

- Torque: $T = \frac{1}{2} i^2 \frac{dL}{d\theta}$
- Inductance profile: $L(\theta)$ varies from $L_{min}$ (unaligned) to $L_{max}$ (aligned)
- Torque ripple: [[torque-ripple]]
- Compare reluctance torque with [[synrm-topology]]

## Research References

### Key Papers

- **Ban et al.** — Torque ripple reduction techniques for SRM
- **Miller et al.** — Comprehensive comparison of SRM with other motor types

### Design Topics

- Torque ripple minimization
- Acoustic noise reduction
- Advanced converter topologies
- Sensorless control methods
- High-speed design considerations

## Related Pages

- [[synrm-topology]] — Synchronous reluctance motor (sinusoidal excitation)
- [[torque-ripple]] — Torque ripple analysis and mitigation
- [[torque-equation]] — General torque equations
- [[ipmsm-topology]] — Interior PM motor (for comparison)
- [[pmasynrm-topology]] — PM-assisted SynRM

## Tags

#topology #srm #reluctance #switched #no-magnet #simple #fault-tolerant #high-speed #torque-ripple
