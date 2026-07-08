---
type: design_guideline
name: Mechanical Bridge Design
aliases: [bridge thickness, flux bridge]
motor_types: [SynRM]
topics: [rotor_design, mechanical, flux_leakage]
source_pages: []
related_equations: []
related_motorcad_variables: []
confidence: High confidence
---

# Mechanical Bridge Design

## Description

The mechanical bridge is the thin iron section connecting the outer rotor lamination to the inner section, providing structural integrity against centrifugal forces. It is a critical trade-off between mechanical strength and electromagnetic performance.

## Typical Ranges

| Parameter | Typical Range |
|-----------|--------------|
| Bridge thickness | 0.3–1.0 mm |
| Bridge angle | Aligned with flux barrier |

## Tradeoffs

| Thicker Bridge | Thinner Bridge |
|----------------|---------------|
| Better mechanical strength | More flux leakage |
| More flux leakage | Better saliency |
| Lower saliency | Higher mechanical risk |
| Safer | Higher performance |

## Design Considerations

- Bridge thickness is the most critical mechanical parameter
- Centrifugal stress at bridge: $\sigma \propto \rho \omega^2 r^2$
- Bridge must survive maximum speed + safety factor
- Flux leakage through bridge reduces effective $(L_d - L_q)$
- Saturation in bridge can help (reduces effective permeability)

## Mechanical Constraint

For a rotating rotor, the bridge stress can be estimated as:

$$\sigma_{max} = \rho \omega^2 r_{avg}^2 \frac{A_{outer}}{A_{bridge}}$$

Where:
- $A_{outer}$ = area of outer rotor section
- $A_{bridge}$ = bridge cross-section area

## MotorCAD Mapping

MotorCAD allows setting bridge thickness as a variable. Mechanical stress analysis can verify the design.

## Related Pages

- [[design_guidelines/rib_design]]
- [[design_guidelines/barrier_design]]
- [[concepts/saliency_ratio]]
- [[topologies/synrm]]
