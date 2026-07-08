---
type: design_guideline
name: Current Density Limits
aliases: [J limits, thermal limits]
motor_types: [SynRM, PMSM, IPMSM]
topics: [thermal, current_density, cooling]
source_pages: []
related_equations: ["equations/current_density"]
related_motorcad_variables: []
confidence: High confidence
---

# Current Density Limits

## Typical Limits by Cooling Method

| Cooling Method | Current Density (A/mm²) | Temperature Rise |
|---------------|------------------------|-----------------|
| Natural convection (TEFC) | 3–5 | 80–100 K |
| Forced air | 5–8 | 60–80 K |
| Liquid cooled (water jacket) | 8–15 | 40–60 K |
| Direct oil spray | 15–25 | 30–50 K |

## Design Considerations

- Current density determines copper loss density ($J^2 \rho$)
- Thermal limit is the primary constraint on current density
- Insulation class limits maximum temperature:
  - Class F: 155°C
  - Class H: 180°C
  - Class N: 200°C
- Hot spot temperature > average winding temperature
- Thermal resistance from winding to coolant determines rise

## MotorCAD Mapping

MotorCAD thermal analysis computes temperature rise from current density. Key outputs:
- Winding temperature
- Hot spot location
- Thermal margins

## Related Pages

- [[equations/current_density]]
- [[concepts/copper_loss]]
- [[design_guidelines/slot_selection]]
- [[topologies/synrm]]
