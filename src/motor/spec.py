"""Machine spec — active project definition for the general motor design agent.

Resolution order for the active spec:
1. Explicit path passed by the caller.
2. Active project folder: $MOTOR_PROJECT > workspace/projects/active.json
   (spec at workspace/projects/<slug>/spec.json).
3. $MOTOR_SPEC environment variable (legacy spec-file override).
4. workspace/specs/active.json (legacy, written by `/spec use <name>`).
5. Example template: workspace/specs/synrm_45kw.json (reference only — used
   only so fresh checkouts have something loadable until `/project new` runs).
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path


def specs_dir() -> Path:
    from src.config.settings import WORKSPACE_ROOT

    return WORKSPACE_ROOT / "specs"


def bundled_default_path() -> Path:
    return specs_dir() / "synrm_45kw.json"


def resolve_active_spec_path(explicit: str = "") -> Path:
    if explicit and explicit.strip():
        return Path(explicit.strip())
    try:
        from src.config.projects import active_spec_path as _project_spec_path

        _p = _project_spec_path()
        if _p is not None:
            return _p
    except Exception:
        pass
    env = os.getenv("MOTOR_SPEC", "").strip()
    if env:
        return Path(env)
    active = specs_dir() / "active.json"
    if active.exists():
        return active
    return bundled_default_path()


@dataclass
class MachineSpec:
    """Validated machine project definition (machine-agnostic)."""

    project: str = "unnamed"
    slug: str = "unnamed"
    machine_type: str = "generic"
    description: str = ""
    operating_point: dict = field(default_factory=dict)
    targets: list[dict] = field(default_factory=list)
    params: dict[str, dict] = field(default_factory=dict)
    order_chains: list[list[str]] = field(default_factory=list)
    minimums: list[dict] = field(default_factory=list)
    maximums: list[dict] = field(default_factory=list)
    locked: list[str] = field(default_factory=list)
    notes: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "MachineSpec":
        if not isinstance(data, dict):
            raise ValueError("spec must be a JSON object")
        spec = cls(
            project=str(data.get("project", "unnamed")),
            slug=str(data.get("slug", "unnamed")),
            machine_type=str(data.get("machine_type", "generic")),
            description=str(data.get("description", "")),
            operating_point=dict(data.get("operating_point", {}) or {}),
            targets=list(data.get("targets", []) or []),
            params=dict(data.get("params", {}) or {}),
            order_chains=[list(c) for c in (data.get("order_chains", []) or [])],
            minimums=list(data.get("minimums", []) or []),
            maximums=list(data.get("maximums", []) or []),
            locked=list(data.get("locked", []) or []),
            notes=str(data.get("notes", "")),
        )
        spec.validate_schema()
        return spec

    def validate_schema(self) -> None:
        if not self.params:
            raise ValueError(f"spec '{self.project}': 'params' must be non-empty")
        for name, bounds in self.params.items():
            if "min" not in bounds or "max" not in bounds:
                raise ValueError(f"spec '{self.project}': param '{name}' needs min and max")
            if bounds["min"] >= bounds["max"]:
                raise ValueError(f"spec '{self.project}': param '{name}' has min >= max")
        for target in self.targets:
            if "key" not in target or ("tol_pct" not in target and "min" not in target):
                raise ValueError(f"spec '{self.project}': each target needs key + tol_pct|min: {target}")

    def summary(self) -> dict:
        return {
            "project": self.project,
            "slug": self.slug,
            "machine_type": self.machine_type,
            "n_params": len(self.params),
            "n_targets": len(self.targets),
            "locked_count": len(self.locked),
        }


def load_spec(path: str | Path) -> MachineSpec:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"machine spec not found: {p}")
    return MachineSpec.from_dict(json.loads(p.read_text(encoding="utf-8")))


def load_active_spec(explicit: str = "") -> MachineSpec:
    return load_spec(resolve_active_spec_path(explicit))


def list_specs() -> list[dict]:
    """List available spec files plus which one is active."""
    d = specs_dir()
    if not d.exists():
        return []
    active = resolve_active_spec_path()
    out = []
    for p in sorted(d.glob("*.json")):
        if p.name == "active.json":
            continue
        try:
            spec = load_spec(p)
            out.append({"name": p.stem, "project": spec.project,
                        "machine_type": spec.machine_type,
                        "active": p.resolve() == active.resolve()})
        except Exception as e:
            out.append({"name": p.stem, "error": str(e), "active": False})
    return out


__all__ = [
    "MachineSpec",
    "bundled_default_path",
    "list_specs",
    "load_active_spec",
    "load_spec",
    "resolve_active_spec_path",
    "specs_dir",
]
