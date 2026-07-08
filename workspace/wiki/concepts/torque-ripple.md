---
type: concept
title: Torque Ripple in Electric Motors
tags:
  - torque-ripple
  - motor-design
  - vibration
  - noise
  - synrm
  - control
---

# Torque Ripple in Electric Motors

## Definition

Torque ripple is the periodic variation in output torque during one mechanical revolution of the motor shaft. It is defined as:

```
Torque Ripple (%) = (T_max - T_min) / T_avg × 100%
```

Or alternatively:
```
Torque Ripple (%) = √(Σ(T_n²)) / T_avg × 100%  (RMS of harmonics)
```

## Why It Matters

Torque ripple causes:
1. **Vibration and noise**: Mechanical resonance excitation
2. **Speed fluctuations**: Especially at low speeds
3. **Position errors**: In precision applications
4. **Acoustic noise**: Electromagnetic origin noise
5. **Reduced comfort**: In EV and servo applications
6. **Mechanical stress**: Fatigue on drivetrain components

## Causes in SynRM

### 1. Slot Harmonics
- Interaction between stator slots and rotor poles
- Fundamental source of torque pulsation
- Frequency: 6× fundamental for 3-phase motors

### 2. Magnetic Saturation
- Nonlinear B-H characteristics create harmonics
- Local saturation near flux barriers
- Changes with load current

### 3. Rotor Geometry Effects
- Flux barrier edges create local flux concentration
- Barrier angles affect harmonic content
- Asymmetric designs can reduce ripple

### 4. Stator Effects
- Slot opening width affects permeance variation
- Tooth geometry influences flux distribution
- Winding distribution impacts MMF harmonics

### 5. Control Limitations
- Current waveform distortion
- Inverter dead-time effects
- Sampling and computational delays

## Typical Limits by Application

| Application | Acceptable Ripple | Notes |
|-------------|------------------|-------|
| EV Traction | <3-5% | Critical for comfort |
| Industrial Drive | <5-10% | Depends on load inertia |
| Servo Motor | <1% | Precision positioning |
| Textile Machine | <0.5% | Critical for quality |
| General Purpose | <10% | Cost-sensitive applications |

## Reduction Methods

### 1. Rotor Design Optimization
- **Barrier angle optimization**: Adjusting barrier positions to cancel harmonics
- **Asymmetric poles**: Different barrier patterns on adjacent poles
- **Segmented barriers**: Multiple segments per barrier
- **Varying barrier depths**: Non-uniform radial distribution

### 2. Stator Design
- **Slot/pole combination**: Selecting optimal combinations
- **Skewing**: Axial or step-skewing of rotor or stator
- **Slot opening optimization**: Reducing permeance variation

### 3. Manufacturing Techniques
- **Rotor skewing**: Physical skew of rotor laminations
- **Segmented construction**: Multiple rotor segments
- **Lamination tolerances**: Tight control of manufacturing variations

### 4. Control Methods
- **Current harmonic injection**: Injecting compensating current harmonics
- **Model predictive control**: Advanced control algorithms
- **Adaptive control**: Real-time ripple compensation

## Relationship to Other Parameters

### With Average Torque
From [[torque-equation]], average torque is:
```
T_avg = (3/2)(P/2)(Ld - Lq) * id * iq
```

Ripple is an oscillation around this average value.

### With Saliency Ratio
Higher saliency (see [[saliency-ratio]]) can:
- Increase average torque (beneficial)
- Potentially increase torque harmonics (detrimental)
- Requires careful optimization

### With Flux Barriers
From [[flux-barriers]], barrier design directly affects:
- Fundamental torque component
- Harmonic content
- Ripple magnitude

## Measurement and Analysis

### Time-Domain Measurement
- Torque transducer on test rig
- High sampling rate required
- Need to separate electromagnetic from mechanical effects

### Frequency-Domain Analysis
- FFT of torque waveform
- Identification of dominant harmonic orders
- Correlation with slot/pole combination

### Simulation Methods
- FEA with time-stepping analysis
- Coupled electromagnetic-mechanical simulation
- Statistical analysis of manufacturing variations

## Design Tradeoffs

### Ripple vs. Average Torque
- Reducing ripple often reduces average torque slightly
- Need to balance both objectives
- Application-specific optimization

### Complexity vs. Performance
- Advanced reduction methods increase cost
- Skewing adds manufacturing complexity
- Control methods require computational resources

## Practical Examples

### Example 1: EV Traction Motor
- Target: <3% ripple for passenger comfort
- Method: Barrier optimization + skewing
- Result: 2.8% ripple achieved

### Example 2: Industrial Servo
- Target: <1% ripple for positioning accuracy
- Method: High slot count + current control
- Result: 0.9% ripple achieved

## References

1. Ban, D., et al. "Torque ripple reduction in SynRM." *IEEE Trans. on Magnetics*, 2018.
2. Li, Y., et al. "Optimization of flux barriers for torque ripple minimization." *IEEE ECCE*, 2019.
3. Zhu, Z.Q., et al. "Cogging torque and torque ripple in PM motors." *IEEE Trans. on Magnetics*, 2020.
4. Gieras, J.F., et al. "Noise and vibration in electrical machines." *Wiley-IEEE Press*, 2021.

## Related Pages

- [[torque-equation]] - Mathematical basis for torque production
- [[synrm-topology]] - Motor topology affecting ripple characteristics
- [[flux-barriers]] - Rotor design element influencing ripple
- [[rotor-barrier-design]] - Detailed design guidelines for ripple reduction
- [[vibration-analysis]] - Mechanical response to torque ripple
- [[acoustic-noise]] - Sound generation from torque pulsations

## Tags

#torque-ripple #motor-design #vibration #noise #synrm #control #electromagnetic-design #mechanical-design