---
type: concept
name: Iron Loss
aliases: [core loss,铁损]
motor_types: [SynRM, PMSM, IPMSM]
topics: [losses, efficiency, iron]
source_pages: []
related_equations: ["equations/loss_models"]
related_motorcad_variables: []
confidence: Verified
---

# Iron Loss (Core Loss)

## Definition

Power dissipated in the magnetic core material due to time-varying magnetic fields, consisting of:

$$P_{iron} = P_{hysteresis} + P_{eddy} + P_{excess}$$

## Why It Matters

Iron loss is a major loss component in SynRM, especially at high speeds. It directly affects:
- Efficiency
- Thermal design
- Maximum-speed capability

## Physics

### Hysteresis Loss
Energy lost in each magnetization cycle due to domain wall movement:

$$P_h = k_h f B_{max}^n$$

Where $n$ ≈ 1.6–2.0 (Steinmetz exponent).

### Eddy Current Loss
Circulating currents induced in laminations:

$$P_e = k_e f^2 B_{max}^2 t^2$$

Where $t$ = lamination thickness.

### Excess Loss
Additional loss due to domain wall dynamics:

$$P_{ex} = k_{ex} f^{1.5} B_{max}^{1.5}$$

## Design Impact

- Higher speed → higher iron loss (frequency-dependent)
- Higher flux density → higher loss (nonlinear)
- Thinner laminations reduce eddy current loss
- Material selection matters (M19 vs M27 vs amorphous)

## MotorCAD Mapping

MotorCAD computes iron loss through electromagnetic simulation:
- Separates hysteresis and eddy components
- Provides loss maps by region (teeth, yoke, rotor)

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/copper_loss]]
- [[equations/loss_models]]
- [[design_guidelines/flux_density_limits]]
- [[materials/]]
