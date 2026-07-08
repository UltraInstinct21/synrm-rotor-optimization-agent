---
type: design_guideline
name: Pole Count Selection
aliases: [pole number, pole pairs]
motor_types: [SynRM, PMSM, IPMSM]
topics: [poles, frequency, torque]
source_pages: []
related_equations: ["equations/d2l_sizing"]
related_motorcad_variables: []
confidence: High confidence
---

# Pole Count Selection

## Typical Values for SynRM

| Poles | Frequency at 1500 rpm | Notes |
|-------|----------------------|-------|
| 2 | 25 Hz | Rare, low reluctance torque |
| 4 | 50 Hz | **Standard for SynRM** |
| 6 | 75 Hz | Higher frequency, more iron loss |
| 8 | 100 Hz | High iron loss |

## Tradeoffs

| More Poles | Fewer Poles |
|-----------|------------|
| Higher frequency → more iron loss | Lower frequency → less iron loss |
| Shorter flux path → shorter yoke | Longer flux path → wider yoke |
| Lower reluctance torque | **Higher reluctance torque** |
| Better for high-speed | Better for torque density |

## Design Considerations

- **4-pole is standard for SynRM** because reluctance torque decreases with pole count
- Higher poles increase electrical frequency → more iron loss
- Pole count affects yoke thickness (shorter flux path with more poles)
- Frequency affects inverter switching requirements

## MotorCAD Mapping

Pole count is a primary input:
- `MotorCAD variables Poles`
- Affects frequency, losses, and torque computation

## Related Pages

- [[design_guidelines/slot_selection]]
- [[equations/d2l_sizing]]
- [[concepts/iron_loss]]
- [[topologies/synrm]]
