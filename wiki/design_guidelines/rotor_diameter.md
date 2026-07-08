---
type: design_guideline
name: Rotor Diameter Selection
aliases: [rotor OD, rotor size]
motor_types: [SynRM, PMSM, IPMSM]
topics: [sizing, geometry, mechanical]
source_pages: []
related_equations: ["equations/d2l_sizing"]
related_motorcad_variables: []
confidence: High confidence
---

# Rotor Diameter Selection

## Typical Ranges

| Application | Typical $D_{is}/D_o$ |
|-------------|---------------------|
| High-speed | 0.55–0.65 |
| General purpose | 0.50–0.60 |
| High-torque | 0.45–0.55 |

## Tradeoffs

| Increasing Rotor Diameter | Effect |
|--------------------------|--------|
| Torque | Increases ($\propto D^2$) |
| Speed | Decreases (higher tip speed) |
| Centrifugal stress | Increases ($\propto D^2 n^2$) |
| Rotor barriers | More space for barriers |
| Mechanical integrity | More critical |
| Airgap | Typically proportioned |

## Design Considerations

- Torque scales with $D_{is}^2$ (from [[equations/d2l_sizing]])
- Rotor tip speed must remain below mechanical limits (~100–150 m/s for laminated rotors)
- Larger rotor → more room for flux barriers → better saliency
- Smaller rotor → better for high-speed applications
- Bridge/rib stress increases with diameter

## MotorCAD Mapping

Rotor diameter is a primary geometry variable:
- `MotorCAD variables Rotor_Diameter`
- Affects barrier geometry and mechanical stress analysis

## Related Pages

- [[equations/d2l_sizing]]
- [[design_guidelines/stack_length]]
- [[design_guidelines/barrier_design]]
- [[design_guidelines/bridge_design]]
- [[topologies/synrm]]
