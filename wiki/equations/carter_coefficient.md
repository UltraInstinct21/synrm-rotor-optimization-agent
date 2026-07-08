---
type: equation
name: Carter's Coefficient
aliases: [Carter factor, slotting correction]
motor_types: [SynRM, PMSM, IPMSM]
topics: [airgap, slotting, correction_factor]
source_pages: []
related_concepts: ["concepts/magnetic_loading"]
related_motorcad_variables: []
confidence: Verified
verification_status: Verified
---

# Carter's Coefficient

## Statement

$$k_C = \frac{\tau_s}{\tau_s - \frac{b_o^2}{5g + b_o}}$$

Where:
- $\tau_s$ = slot pitch
- $b_o$ = slot opening width
- $g$ = mechanical airgap

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $k_C$ | Carter's coefficient | — |
| $\tau_s$ | Slot pitch | m |
| $b_o$ | Slot opening | m |
| $g$ | Mechanical airgap | m |

## Assumptions

- Uniform airgap
- Straight (non-parallel) slot walls
- No saturation in tooth tips
- Approximate correction for slotting effects

## Interpretation

Carter's coefficient accounts for the increase in effective airgap due to slot openings. It is always > 1.

Typical values: 1.0–1.3 depending on slot opening to airgap ratio.

## Design Relevance

- Larger slot openings → higher $k_C$ → larger effective airgap → lower flux density
- Smaller airgap amplifies the effect of slot openings
- Affects torque calculation accuracy

## MotorCAD Mapping

MotorCAD accounts for slotting effects in FEA automatically. Carter's coefficient is used in analytical pre-design.

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[equations/airgap_flux_density]]
- [[design_guidelines/airgap]]
- [[design_guidelines/slot_selection]]
