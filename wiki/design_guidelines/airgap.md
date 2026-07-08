---
type: design_guideline
name: Airgap Selection
aliases: [mechanical airgap,气隙]
motor_types: [SynRM, PMSM, IPMSM]
topics: [geometry, airgap, manufacturing]
source_pages: []
related_equations: ["equations/airgap_flux_density", "equations/carter_coefficient"]
related_motorcad_variables: []
confidence: High confidence
---

# Airgap Selection

## Typical Ranges

| Application | Typical Airgap |
|-------------|---------------|
| Small motors (< 1 kW) | 0.2–0.5 mm |
| Medium motors (1–100 kW) | 0.5–1.0 mm |
| Large motors (> 100 kW) | 1.0–2.0 mm |
| High-speed | Larger (0.8–1.5 mm) |

Rule of thumb: $g \approx 0.001 \times D_{is}$ to $0.002 \times D_{is}$

## Tradeoffs

| Decreasing Airgap | Effect |
|-------------------|--------|
| Torque | Increases (higher flux density) |
| Inductance | Increases |
| Manufacturing tolerance | More critical |
| Bearing tolerance | More critical |
| Unbalanced magnetic pull | Increases |
| Assembly difficulty | Increases |

## Design Considerations

- Smaller airgap → higher torque but harder to manufacture
- Airgap affects Carter's coefficient ([[equations/carter_coefficient]])
- Mechanical tolerances must be much smaller than airgap
- In SynRM, airgap affects both $L_d$ and $L_q$
- Very small airgap risks rotor-stator contact

## MotorCAD Mapping

Airgap is a primary geometry variable:
- `MotorCAD variables Airgap`
- Directly affects electromagnetic simulation results

## Related Pages

- [[equations/airgap_flux_density]]
- [[equations/carter_coefficient]]
- [[design_guidelines/rotor_diameter]]
- [[design_guidelines/stack_length]]
- [[topologies/synrm]]
