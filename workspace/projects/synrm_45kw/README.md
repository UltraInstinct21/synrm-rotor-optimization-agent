# 45kW SynRM rotor optimization

Machine type: SynRM

Optimize rotor flux-barrier geometry of a 45 kW SynRM. Stator is locked; only rotor barrier parameters may vary.

## Files

- `spec.json` — targets, param bounds, constraints, locked list, operating point (edit this for your machine).
- `ledger.jsonl` — scored candidate log (written automatically).
- `scratch/` — generated run scripts for this project.
- `models/` — .mot files and backups (e.g. best_so_far.mot).
