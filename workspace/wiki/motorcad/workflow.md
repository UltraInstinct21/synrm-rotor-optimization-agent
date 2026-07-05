---
title: Motor-CAD Workflow
created: 2026-07-05
---

# Motor-CAD Workflow

## Summary

Motor-CAD is the FEA solver used for SynRM and PMaSynRM motor design. The workflow involves setting geometry/winding/rating parameters, running electromagnetic or thermal analysis, and extracting key performance metrics.

## Standard workflow

1. Load `.mot` model file.
2. Verify/set parameters (geometry, winding, rating, materials).
3. Save checkpoint before rotor modifications.
4. Run electromagnetic analysis (Magnetic context).
5. Extract results: torque, efficiency, power factor, Ld/Lq, saliency, losses.
6. Iterate if needed (geometry sweeps, optimization).

## Key files

| File | Purpose |
|------|---------|
| `SynRM_45kW_IE5.mot` | Reference 45kW IE5 SynRM model |
| `optimize_synrm_v4.py` | Multi-objective optimization script |

## Anti-hallucination rules

See `src/skills/motorcad-workflow/SKILL.md` for the full PyMotorCAD safety rules.

## Related

- [[motorcad/parameters]] — parameter reference
- [[motorcad/result_fields]] — result metric definitions
