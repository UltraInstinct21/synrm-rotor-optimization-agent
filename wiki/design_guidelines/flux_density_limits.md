---
type: design_guideline
name: Flux Density Limits
aliases: [B limits, saturation limits]
motor_types: [SynRM, PMSM, IPMSM]
topics: [saturation, flux_density, materials]
source_pages: []
related_equations: ["equations/airgap_flux_density"]
related_motorcad_variables: []
confidence: High confidence
---

# Flux Density Limits

## Typical Limits for M19 Steel

| Region | Maximum $B$ (T) | Design Target (T) |
|--------|----------------|-------------------|
| Stator teeth | 1.8 | 1.5–1.7 |
| Stator yoke | 1.7 | 1.4–1.6 |
| Rotor iron | 1.6 | 1.2–1.5 |
| Rotor bridges | >2.0 (saturated) | >1.8 (intentional) |
| Airgap | 1.2 | 0.8–1.0 |

## Design Considerations

- Operating above knee point → rapid permeability drop
- Bridges intentionally saturate to limit flux leakage
- Teeth are usually the first to saturate
- Rotor saturation degrades saliency ratio
- Higher-grade steel (M27, M36) allows higher flux densities

## Material Comparison

| Material | Saturation (T) | Loss at 1.5T, 60Hz (W/kg) |
|----------|---------------|--------------------------|
| M19 | 2.03 | 1.30 |
| M27 | 2.03 | 0.97 |
| M36 | 2.03 | 0.80 |
| M43 | 2.03 | 0.60 |

## MotorCAD Mapping

MotorCAD uses B-H curves for each material. Saturation effects appear in:
- Inductance vs. current
- Flux density maps
- Torque vs. current

## Related Pages

- [[concepts/saturation]]
- [[concepts/magnetic_loading]]
- [[equations/airgap_flux_density]]
- [[materials/]]
- [[topologies/synrm]]
