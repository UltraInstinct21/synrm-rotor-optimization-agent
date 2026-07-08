---
type: design_guideline
name: Stack Length Selection
aliases: [active length, lamination stack]
motor_types: [SynRM, PMSM, IPMSM]
topics: [sizing, geometry, tradeoffs]
source_pages: []
related_equations: ["equations/d2l_sizing"]
related_motorcad_variables: []
confidence: High confidence
---

# Stack Length Selection

## Typical Ranges

| Application | Typical $L_{sk}/D_{is}$ |
|-------------|-------------------------|
| High-speed | 0.3–0.5 |
| General purpose | 0.5–1.0 |
| High-torque | 1.0–2.0 |

## Tradeoffs

| Increasing Stack Length | Effect |
|------------------------|--------|
| Torque | Increases linearly |
| Copper loss | Increases (longer conductors) |
| Iron loss | Increases proportionally |
| Rotor dynamics | More critical (longer rotor) |
| Deflection | Increases (∝ $L^3$) |
| Cost | Increases |
| Manufacturability | Harder for very long stacks |

## Design Considerations

- Torque scales linearly with $L_{sk}$ (from [[equations/d2l_sizing]])
- Rotor lateral stiffness decreases with length
- Critical speed may limit maximum length
- Cooling becomes harder for longer stacks
-端部 winding length becomes relatively smaller → better copper utilization

## MotorCAD Mapping

Stack length is a primary geometry variable in MotorCAD:
- `MotorCAD variables Stator_Lam_Length` or equivalent
- Directly affects torque output in simulation

## Related Pages

- [[equations/d2l_sizing]]
- [[design_guidelines/rotor_diameter]]
- [[concepts/magnetic_loading]]
- [[concepts/electric_loading]]
- [[topologies/synrm]]
