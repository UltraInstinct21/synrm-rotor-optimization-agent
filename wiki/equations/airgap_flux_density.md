---
type: equation
name: Airgap Flux Density
aliases: [B_delta, airgap field]
motor_types: [SynRM, PMSM, IPMSM]
topics: [flux_density, airgap, magnetic_loading]
source_pages: []
related_concepts: ["concepts/magnetic_loading"]
related_motorcad_variables: []
confidence: Verified
verification_status: Verified
---

# Airgap Flux Density

## Statement

For a sinusoidal MMF distribution with Carter's coefficient:

$$B_\delta = \frac{\mu_0 F}{k_C \cdot g}$$

Where:
- $B_\delta$ = peak airgap flux density
- $\mu_0$ = permeability of free space ($4\pi \times 10^{-7}$ H/m)
- $F$ = peak MMF per pole
- $k_C$ = Carter's coefficient
- $g$ = mechanical airgap

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $B_\delta$ | Peak airgap flux density | T |
| $\mu_0$ | Vacuum permeability | H/m |
| $F$ | Peak MMF per pole | A·turns |
| $k_C$ | Carter's coefficient | — |
| $g$ | Mechanical airgap | m |

## Assumptions

- Sinusoidal MMF distribution
- Uniform airgap (cylindrical geometry)
- No saturation in iron (infinite permeability approximation)
- Carter's coefficient accounts for slotting effects

## Interpretation

The airgap flux density is determined by the MMF source and the airgap reluctance. In SynRM, the MMF comes entirely from stator current (no rotor excitation).

## Design Relevance

- Higher $B_\delta$ → higher torque density
- Limited by iron saturation and losses
- Airgap length affects $B_\delta$ and thus torque
- Barrier geometry in SynRM affects effective airgap seen by flux

## MotorCAD Mapping

MotorCAD computes airgap flux density through FEA. Output includes:
- Radial flux density waveform in airgap
- Harmonic content
- Peak and average values

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/magnetic_loading]]
- [[equations/carter_coefficient]]
- [[equations/d2l_sizing]]
- [[design_guidelines/airgap]]
- [[design_guidelines/flux_density_limits]]
