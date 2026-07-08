---
type: design_guideline
name: Rib Design
aliases: [inter-barrier rib, flux rib]
motor_types: [SynRM]
topics: [rotor_design, mechanical, flux_leakage]
source_pages: []
related_equations: []
related_motorcad_variables: []
confidence: High confidence
---

# Rib Design

## Description

Ribs are the thin iron sections between adjacent flux barriers. They provide mechanical connection between rotor segments but create flux leakage paths that reduce saliency.

## Typical Ranges

| Parameter | Typical Range |
|-----------|--------------|
| Rib thickness | 0.3–0.8 mm |
| Rib count | One per barrier pair |

## Tradeoffs

| Thicker Ribs | Thinner Ribs |
|-------------|-------------|
| Better mechanical integrity | More flux leakage |
| More flux leakage | Better saliency |
| Lower saliency | Higher mechanical risk |
| Easier manufacturing | Harder to manufacture |

## Design Considerations

- Ribs saturate easily due to small cross-section
- Saturation actually helps reduce effective flux leakage
- Rib stress depends on rotor speed and geometry
- Multiple barriers → multiple ribs → cumulative leakage effect
- Rib dimensions interact with barrier dimensions

## MotorCAD Mapping

MotorCAD allows setting rib thickness. Saturation effects are captured in FEA.

## Related Pages

- [[design_guidelines/bridge_design]]
- [[design_guidelines/barrier_design]]
- [[concepts/saliency_ratio]]
- [[concepts/saturation]]
- [[topologies/synrm]]
