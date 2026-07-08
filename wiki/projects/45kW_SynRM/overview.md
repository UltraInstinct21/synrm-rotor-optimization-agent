---
type: project
name: 45kW SynRM Design
aliases: [45kW SynRM, SynRM 45kW]
status: Active
motor_types: [SynRM]
rating: 45 kW
source_files: []
related_experiments: []
related_decisions: []
related_failures: []
confidence: Verified
---

# 45kW SynRM Design Project

## Specifications

| Parameter | Value |
|-----------|-------|
| Rated power | 45 kW |
| Motor type | Synchronous Reluctance Motor |
| Cooling | TBD |
| Application | Industrial drive |

## Project Goals

1. Design a high-efficiency SynRM meeting 45kW rating
2. Optimize rotor geometry for maximum torque and minimum ripple
3. Verify design through MotorCAD simulation
4. Document design decisions and lessons learned

## Status

- MotorCAD model: `SynRM_45kW_IE5.mot`
- Optimization script: `optimize_synrm_v4.py`

## Related Pages

- [[topologies/synrm]]
- [[design_guidelines/barrier_design]]
- [[motorcad/workflows/index]]
