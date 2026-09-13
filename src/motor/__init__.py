"""Motor-design domain package — machine-agnostic spec, validation, scoring, ledger, and sweep helpers.

The agent is a GENERAL motor design agent (SynRM, PMSM/IPM, IM, BLDC, ...).
The current project's targets, parameter bounds, and constraints come from the
active project folder (workspace/projects/<slug>/spec.json), never from
hardcoded values. An example template ships under workspace/specs/ for
reference only.
"""

from src.motor.spec import MachineSpec, load_active_spec, resolve_active_spec_path

__all__ = ["MachineSpec", "load_active_spec", "resolve_active_spec_path"]
