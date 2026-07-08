---
type: concept
title: dq Theory (Direct-Quadrature Transformation)
tags:
  - dq-theory
  - park-transformation
  - field-oriented-control
  - synrm
  - pmsm
  - control-theory
---

# dq Theory (Direct-Quadrature Transformation)

## Definition

dq theory (also called Park transformation or field-oriented control theory) is a mathematical transformation that converts three-phase AC quantities (abc reference frame) into DC quantities in a rotating reference frame aligned with the rotor flux.

The transformation simplifies analysis and control of AC motors by making sinusoidal quantities appear as DC values in steady state.

## Reference Frames

### Stationary Reference Frame (abc or αβ)
- Fixed to stator
- Three-phase sinusoidal quantities
- Time-varying in steady state

### Rotating Reference Frame (dq0)
- Rotating at electrical speed ω
- Aligned with rotor flux (d-axis) or perpendicular (q-axis)
- DC quantities in steady state for balanced conditions

## Transformation Matrices

### abc → dq0 (Park Transformation)
```
[ i_d ]   [ cos(θ)    cos(θ-2π/3)  cos(θ+2π/3) ] [ i_a ]
[ i_q ] = [ -sin(θ)   -sin(θ-2π/3) -sin(θ+2π/3) ] [ i_b ]
[ i_0 ]   [ 1/2        1/2           1/2         ] [ i_c ]
```

Where θ = ∫ω dt + θ₀ is the rotor electrical angle.

### Inverse Transformation (dq0 → abc)
```
[ i_a ]   [ cos(θ)      -sin(θ)      1 ] [ i_d ]
[ i_b ] = [ cos(θ-2π/3) -sin(θ-2π/3) 1 ] [ i_q ]
[ i_c ]   [ cos(θ+2π/3) -sin(θ+2π/3) 1 ] [ i_0 ]
```

## Physical Meaning of Axes

### d-axis (Direct Axis)
- Aligned with rotor flux path
- **Minimum reluctance path** in SynRM
- Corresponds to maximum inductance (Ld)
- Flux-producing component

### q-axis (Quadrature Axis)
- Perpendicular to d-axis
- **Maximum reluctance path** in SynRM
- Corresponds to minimum inductance (Lq)
- Torque-producing component (with id)

### 0-axis (Zero Sequence)
- Represents homopolar component
- Zero in balanced three-phase systems
- Important for fault analysis

## Voltage Equations in dq Frame

For a synchronous motor in the dq reference frame:

```
v_d = R_s * i_d + d(Ld*i_d)/dt - ω * Lq * i_q
v_q = R_s * i_q + d(Lq*i_q)/dt + ω * Ld * i_d
```

Where:
- v_d, v_q: d and q axis voltages
- R_s: Stator resistance
- i_d, i_q: d and q axis currents
- Ld, Lq: d and q axis inductances
- ω: Electrical angular velocity

### Simplified Steady-State (dc quantities)
```
v_d = R_s * i_d - ω * Lq * i_q
v_q = R_s * i_q + ω * Ld * i_d
```

## Torque Equation

From [[torque-equation]], the electromagnetic torque in dq frame is:

```
T_e = (3/2)(P/2)(Ld - Lq) * i_d * i_q
```

Or alternatively:
```
T_e = (3/2)(P/2)(λ_d * i_q - λ_q * i_d)
```

Where:
- P: Number of poles
- λ_d, λ_q: d and q axis flux linkages

### Reluctance Torque Component
```
T_reluctance = (3/2)(P/2)(Ld - Lq) * i_d * i_q
```
This is the torque produced by the saliency (Ld ≠ Lq).

### Alignment Torque Component (for PM motors)
```
T_alignment = (3/2)(P/2) * λ_pm * i_q
```
Where λ_pm is the PM flux linkage.

## Inductances in dq Frame

From [[inductance-equations]]:

### d-axis Inductance
```
Ld = λ_d / i_d  (at i_q = 0)
```
Represents flux linkage per ampere along d-axis.

### q-axis Inductance
```
Lq = λ_q / i_q  (at i_d = 0)
```
Represents flux linkage per ampere along q-axis.

### Saliency Ratio
```
ζ = Ld / Lq
```
From [[saliency-ratio]], this directly affects torque and power factor.

## Application in Control

### Field-Oriented Control (FOC)
dq theory enables FOC by:
1. Measuring phase currents
2. Transforming to dq using measured rotor position
3. Controlling i_d and i_q independently
4. Transforming back to abc for inverter control

### MTPA Strategy
From [[mtpa-control]], maximum torque per ampere occurs at specific i_d/i_q ratio depending on motor parameters.

### Flux Weakening
For high-speed operation, i_d is made negative to reduce airgap flux, enabling operation above base speed.

## Advantages of dq Theory

1. **Simplification**: AC quantities become DC in steady state
2. **Decoupling**: Flux and torque control separated
3. **Intuitive control**: Similar to DC motor control
4. **Performance**: Enables high-performance drives
5. **Analysis**: Simplifies motor design equations

## Limitations and Considerations

### Parameter Sensitivity
- Control performance depends on accurate Ld, Lq values
- Saturation changes inductances with current
- Temperature affects PM strength

### Transient Behavior
- dq transformation assumes sinusoidal distribution
- May not capture all harmonics accurately
- Requires accurate position estimation

### Non-ideal Effects
- Inverter dead-time introduces errors
- Sampling delays affect control bandwidth
- Parameter variation with operating point

## Implementation in Code

```python
import numpy as np

def park_transform(i_a, i_b, i_c, theta):
    """abc to dq0 transformation"""
    i_d = (i_a * np.cos(theta) + 
           i_b * np.cos(theta - 2*np.pi/3) + 
           i_c * np.cos(theta + 2*np.pi/3))
    
    i_q = (-i_a * np.sin(theta) - 
           i_b * np.sin(theta - 2*np.pi/3) - 
           i_c * np.sin(theta + 2*np.pi/3))
    
    i_0 = (i_a + i_b + i_c) / 3
    
    return i_d, i_q, i_0

def inverse_park(i_d, i_q, i_0, theta):
    """dq0 to abc transformation"""
    i_a = i_d * np.cos(theta) - i_q * np.sin(theta) + i_0
    i_b = (i_d * np.cos(theta - 2*np.pi/3) - 
           i_q * np.sin(theta - 2*np.pi/3) + i_0)
    i_c = (i_d * np.cos(theta + 2*np.pi/3) - 
           i_q * np.sin(theta + 2*np.pi/3) + i_0)
    
    return i_a, i_b, i_c
```

## References

1. Saxena, N., et al. "dq modeling of SynRM for high-performance control." *IEEE Trans. on Industry Applications*, 2019.
2. Alkhafaji, M., et al. "Field-oriented control of SynRM." *IEEE ECCE*, 2020.
3. EE6703 course materials. "Electric Drives." University lectures.
4. Vas, P. "Sensorless Vector and Direct Torque Control." *Oxford University Press*, 1998.
5. Krishnan, R. "Permanent Magnet Synchronous and Brushless DC Motor Drives." *CRC Press*, 2010.

## Related Pages

- [[torque-equation]] - Torque expression in dq frame
- [[inductance-equations]] - Detailed inductance definitions
- [[mtpa-control]] - Optimal current angle strategy
- [[flux-barriers]] - Physical basis for Ld/Lq difference
- [[saliency-ratio]] - Key parameter in dq model
- [[synrm-topology]] - Motor topology using dq theory
- [[field-oriented-control]] - Implementation of dq theory in drives
- [[power-factor-equation]] - PF relationship in dq frame

## Tags

#dq-theory #park-transformation #field-oriented-control #synrm #pmsm #control-theory #electromagnetic-design #motor-control