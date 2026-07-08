---
type: concept
name: Magnetic Saturation
aliases: [saturation]
motor_types: [SynRM, PMSM, IPMSM]
topics: [flux_density, nonlinear, iron]
source_pages: []
related_equations: []
related_motorcad_variables: []
confidence: Verified
---

# Magnetic Saturation

## Definition

The phenomenon where increasing magnetic field intensity no longer produces proportional increases in flux density, as the magnetic domains in the iron become fully aligned.

## Why It Matters

Saturation in SynRM:
- Reduces $L_d$ more than $L_q$ → degrades saliency ratio
- Increases core losses
- Limits torque at high currents
- Causes nonlinear behavior that complicates control

## Physics

The B-H curve of electrical steel shows:
- Linear region: $B \propto H$ (constant permeability)
- Knee region: permeability begins to decrease
- Saturation region: $B$ increases slowly with $H$

For M19 steel:
- Linear up to ~1.5 T
- Knee at ~1.6–1.7 T
- Full saturation ~1.8–2.0 T

## Design Impact

In SynRM, saturation is most severe in:
- **Rotor bridges/ribs**: thin iron paths saturate easily, increasing $L_q$
- **Stator teeth**: high flux concentration
- **Rotor poles**: near barrier tips

Saturation reduces effective saliency:
- At light load: $\xi$ ≈ 6–8
- At rated load: $\xi$ ≈ 4–6
- At overload: $\xi$ ≈ 3–4

## MotorCAD Mapping

MotorCAD uses nonlinear B-H curves in FEA. Saturation effects appear in:
- Inductance vs. current curves
- Flux density distribution plots
- Torque vs. current characteristics

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/saliency_ratio]]
- [[concepts/magnetic_loading]]
- [[design_guidelines/flux_density_limits]]
- [[design_guidelines/rib_design]]
- [[design_guidelines/bridge_design]]
