---
type: concept
name: Magnetic Loading
aliases: [airgap flux density]
motor_types: [SynRM, PMSM, IPMSM]
topics: [flux_density, airgap, sizing]
source_pages: []
related_equations: ["equations/airgap_flux_density", "equations/d2l_sizing"]
related_motorcad_variables: []
confidence: Verified
---

# Magnetic Loading

## Definition

The average airgap flux density over one pole pitch, denoted $B_{avg}$ or $B_\delta$.

$$B_{avg} = \frac{1}{\tau_p} \int_0^{\tau_p} B(\theta) d\theta$$

## Why It Matters

Magnetic loading directly scales torque output. Higher magnetic loading → higher torque for the same machine volume.

## Physics

In SynRM, the airgap flux density is limited by:
- Saturation of stator teeth and yoke
- Rotor iron saturation (especially near bridges/ribs)
- Iron loss (increases with flux density)

Typical values for SynRM:
- Airgap peak: 0.8–1.2 T
- Stator teeth: 1.5–1.8 T (M19 steel)
- Stator yoke: 1.4–1.6 T
- Rotor: 1.2–1.5 T

## Design Impact

- Higher $B_{avg}$ → higher torque density
- Limited by material saturation and losses
- Barrier geometry affects flux distribution
- Bridge/rib saturation limits effective magnetic loading

## MotorCAD Mapping

MotorCAD computes flux density distribution through FEA. Key outputs:
- Airgap flux density waveform
- Tooth and yoke flux densities
- Saturation maps

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/electric_loading]]
- [[concepts/saturation]]
- [[equations/airgap_flux_density]]
- [[equations/d2l_sizing]]
- [[design_guidelines/flux_density_limits]]
