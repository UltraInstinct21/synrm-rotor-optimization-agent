---
type: concept
name: Copper Loss
aliases: [winding loss, I²R loss]
motor_types: [SynRM, PMSM, IPMSM]
topics: [losses, efficiency, winding]
source_pages: []
related_equations: ["equations/loss_models", "equations/current_density"]
related_motorcad_variables: []
confidence: Verified
---

# Copper Loss

## Definition

Power dissipated in the stator windings due to conductor resistance:

$$P_{cu} = m I_s^2 R_s$$

Where:
- $m$ = number of phases
- $I_s$ = RMS phase current
- $R_s$ = phase resistance

## Why It Matters

Copper loss is the dominant loss at low speeds/high torques. It determines:
- Efficiency at rated operating point
- Thermal limits
- Current density constraints

## Physics

Resistance depends on:
- Conductor length (stack length × turns)
- Conductor cross-section (wire gauge)
- Temperature (resistance increases ~0.4%/°C for copper)

$$R_s = \rho \frac{N_{ph} \cdot l_{turn}}{A_{cond} \cdot k_{fill}}$$

## Design Impact

- Higher current → copper loss ∝ $I^2$
- Thicker wire → lower resistance but lower slot fill
- Shorter stack → lower resistance but lower torque
- Temperature rise must be managed

Typical current density limits:
- Natural convection: 3–5 A/mm²
- Forced air: 5–8 A/mm²
- Liquid cooled: 8–15 A/mm²

## MotorCAD Mapping

MotorCAD computes winding resistance and copper loss. Key variables:
- Phase resistance
- Winding temperature
- Fill factor

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/iron_loss]]
- [[equations/loss_models]]
- [[equations/current_density]]
- [[design_guidelines/current_density_limits]]
