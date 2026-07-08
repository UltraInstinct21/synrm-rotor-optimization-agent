---
type: design_guideline
name: Slot/Pole Combination Selection
aliases: [slot count, pole count, slot-pole]
motor_types: [SynRM, PMSM, IPMSM]
topics: [winding, slots, poles]
source_pages: []
related_equations: []
related_motorcad_variables: []
confidence: High confidence
---

# Slot/Pole Combination Selection

## Typical Combinations for SynRM

| Poles | Slots | Slot/Pole | Winding Factor | Notes |
|-------|-------|-----------|----------------|-------|
| 4 | 36 | 9 | 0.960 | Common, good performance |
| 4 | 48 | 12 | 0.958 | Higher slot count |
| 2 | 24 | 12 | 0.966 | Fewer poles |
| 6 | 36 | 6 | 0.960 | Higher pole count |
| 8 | 48 | 6 | 0.960 | High pole count |

## Selection Criteria

1. **Winding factor**: Higher → better MMF utilization
2. **Cogging torque**: GCD of slots and poles affects cogging
3. **Manufacturing**: Fewer slots → simpler winding
4. **Harmonic content**: Affects losses and torque ripple
5. **Slot opening**: Affects airgap flux distribution

## Design Impact

- 4-pole is standard for SynRM (higher poles reduce reluctance torque)
- 36-slot or 48-slot common for 4-pole
- Fractional slot/pole combinations can reduce cogging
- Slot opening affects Carter's coefficient ([[equations/carter_coefficient]])

## MotorCAD Mapping

MotorCAD requires slot count and pole count as inputs. Winding pattern is defined separately.

## Related Pages

- [[concepts/electric_loading]]
- [[equations/carter_coefficient]]
- [[design_guidelines/pole_selection]]
- [[topologies/synrm]]
