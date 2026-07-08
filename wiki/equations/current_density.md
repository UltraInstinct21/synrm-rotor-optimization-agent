---
type: equation
name: Current Density
aliases: [J, current density formulation]
motor_types: [SynRM, PMSM, IPMSM]
topics: [current_density, thermal, winding]
source_pages: []
related_concepts: ["concepts/electric_loading"]
related_motorcad_variables: []
confidence: Verified
verification_status: Verified
---

# Current Density

## Statement

$$J = \frac{I_s}{A_{cond}} = \frac{N_{ph} I_s}{A_{slot} \cdot k_{fill}}$$

Where:
- $J$ = current density (A/mm²)
- $I_s$ = RMS phase current
- $A_{cond}$ = total conductor cross-section per slot
- $A_{slot}$ = slot area
- $k_{fill}$ = slot fill factor

## Normalized Notation

| Symbol | Meaning | Units |
|--------|---------|-------|
| $J$ | Current density | A/mm² |
| $I_s$ | RMS phase current | A |
| $A_{cond}$ | Conductor cross-section | mm² |
| $A_{slot}$ | Slot area | mm² |
| $k_{fill}$ | Slot fill factor | — |
| $N_{ph}$ | Series turns per phase | — |

## Assumptions

- Uniform current distribution in conductors
- DC resistance only (no skin/proximity effects at fundamental)
- Fill factor accounts for insulation and packing

## Interpretation

Current density determines the thermal loading of the machine. It must be kept within limits determined by:
- Cooling method
- Insulation class
- Allowable temperature rise

## Design Relevance

| Cooling Method | Typical J Limit |
|---------------|----------------|
| Natural convection | 3–5 A/mm² |
| Forced air | 5–8 A/mm² |
| Liquid cooled | 8–15 A/mm² |
| Direct oil cooling | 15–25 A/mm² |

Higher J → smaller machine but more heat → requires better cooling.

## MotorCAD Mapping

MotorCAD computes current density from winding and current settings. Thermal analysis uses J for heat generation.

## Sources

- [[references/boldea]]
- [[references/pyrhonen]]

## Related Pages

- [[concepts/electric_loading]]
- [[concepts/copper_loss]]
- [[design_guidelines/current_density_limits]]
- [[design_guidelines/slot_selection]]
