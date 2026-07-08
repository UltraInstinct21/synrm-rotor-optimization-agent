---
type: equation
name: Loss Models
aliases: [iron loss model, copper loss model]
motor_types: [SynRM, PMSM, IPMSM]
topics: [losses, efficiency, iron_loss, copper_loss]
source_pages: []
related_concepts: ["concepts/iron_loss", "concepts/copper_loss"]
related_motorcad_variables: []
confidence: Verified
verification_status: Verified
---

# Loss Models

## Iron Loss (Core Loss)

### Steinmetz Equation

$$P_{iron} = k_h f B_{max}^n + k_e f^2 B_{max}^2$$

Where:
- $k_h$ = hysteresis coefficient
- $k_e$ = eddy current coefficient
- $f$ = frequency
- $B_{max}$ = peak flux density
- $n$ = Steinmetz exponent (typically 1.6–2.0)

### Bertotti Separation Model

$$P_{iron} = k_h f B_{max}^n + k_e (f B_{max})^2 + k_{ex} |f B_{max}|^{1.5}$$

Adding the excess loss term for more accurate modeling.

## Copper Loss

$$P_{cu} = m I_s^2 R_s$$

With temperature dependence:

$$R_s(T) = R_{s,20} [1 + \alpha_{cu} (T - 20)]$$

Where $\alpha_{cu} \approx 0.00393$ /°C.

## Total Loss

$$P_{total} = P_{iron} + P_{cu} + P_{mech}$$

Where $P_{mech}$ includes windage and bearing losses (usually small at low speeds).

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $P_{iron}$ | Iron loss | W |
| $P_{cu}$ | Copper loss | W |
| $k_h$ | Hysteresis coefficient | W/(kg·Hz·T^n) |
| $k_e$ | Eddy current coefficient | W/(kg·Hz²·T²) |
| $k_{ex}$ | Excess loss coefficient | W/(kg·Hz^1.5·T^1.5) |
| $f$ | Electrical frequency | Hz |
| $B_{max}$ | Peak flux density | T |

## Assumptions

- Steinmetz equation is empirical, valid for sinusoidal excitation
- Separation model assumes independent loss mechanisms
- Copper loss assumes DC resistance (fundamental frequency only)

## Design Relevance

- Loss models drive efficiency optimization
- Iron loss dominates at high speed
- Copper loss dominates at high torque/low speed
- Thermal design must dissipate total losses

## MotorCAD Mapping

MotorCAD computes losses through FEA with material-specific loss coefficients. Outputs:
- Iron loss by region (teeth, yoke, rotor)
- Copper loss
- Total loss breakdown

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/iron_loss]]
- [[concepts/copper_loss]]
- [[design_guidelines/flux_density_limits]]
- [[design_guidelines/current_density_limits]]
- [[materials/]]
