"""Project folders — each motor project is self-contained.

Layout per project::

    workspace/projects/<slug>/
    ├── spec.json       # targets, param bounds, constraints, locked list, operating point
    ├── ledger.jsonl    # scored CANDIDATE_RESULT log (append-only)
    ├── scratch/        # generated run scripts for this project
    ├── models/         # .mot files and backups (e.g. best_so_far.mot)
    └── README.md       # project notes

Active project resolution (first hit wins):
1. $MOTOR_PROJECT environment variable (a slug like ``my_motor``).
2. workspace/projects/active.json (``{"slug": ...}``, written by /project use).
3. Legacy workspace/specs/active.json — its ``slug`` field, if the matching
   project folder exists.
4. None (no project active — the CLI prompts to select/create one).

The example template under workspace/specs/synrm_45kw.json is reference-only:
it is copied as a starting point by create_project(), never treated as the
active project itself.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from pathlib import Path

_SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


def projects_root() -> Path:
    from src.config.settings import WORKSPACE_ROOT

    return WORKSPACE_ROOT / "projects"


def active_pointer_path() -> Path:
    return projects_root() / "active.json"


def sanitize_slug(raw: str) -> str:
    slug = (raw or "").strip().lower().replace(" ", "_")
    slug = re.sub(r"[^a-z0-9_-]", "", slug)
    return slug


def validate_slug(slug: str) -> str:
    slug = (slug or "").strip()
    if not slug or not _SLUG_RE.match(slug):
        raise ValueError(
            f"invalid project slug '{slug}': use lowercase letters, digits, '-' or '_'"
        )
    return slug


def project_dir(slug: str) -> Path:
    return projects_root() / validate_slug(slug)


def spec_path(slug: str) -> Path:
    return project_dir(slug) / "spec.json"


def ledger_path(slug: str) -> Path:
    return project_dir(slug) / "ledger.jsonl"


def scratch_dir(slug: str) -> Path:
    return project_dir(slug) / "scratch"


def models_dir(slug: str) -> Path:
    return project_dir(slug) / "models"


def get_active_slug() -> str | None:
    """Return the active project slug, or None when no project is selected."""
    env = os.getenv("MOTOR_PROJECT", "").strip()
    if env:
        return validate_slug(env)
    ptr = active_pointer_path()
    if ptr.exists():
        try:
            data = json.loads(ptr.read_text(encoding="utf-8"))
            slug = str(data.get("slug", "")).strip()
            if slug:
                return validate_slug(slug)
        except Exception:
            return None
    # Legacy fallback: specs/active.json carries a "slug" field.
    try:
        from src.config.settings import WORKSPACE_ROOT

        legacy = WORKSPACE_ROOT / "specs" / "active.json"
        if legacy.exists():
            data = json.loads(legacy.read_text(encoding="utf-8"))
            slug = str(data.get("slug", "")).strip()
            if slug and project_dir(slug).exists():
                return validate_slug(slug)
    except Exception:
        pass
    return None


def set_active_slug(slug: str) -> Path:
    """Persist the active project pointer; returns the pointer path."""
    slug = validate_slug(slug)
    if not project_dir(slug).exists():
        raise FileNotFoundError(f"project '{slug}' does not exist: {project_dir(slug)}")
    root = projects_root()
    root.mkdir(parents=True, exist_ok=True)
    ptr = active_pointer_path()
    ptr.write_text(json.dumps({"slug": slug}, indent=2) + "\n", encoding="utf-8")
    return ptr


def active_project_dir() -> Path | None:
    slug = get_active_slug()
    if not slug:
        return None
    d = project_dir(slug)
    return d if d.exists() else None


def active_spec_path() -> Path | None:
    d = active_project_dir()
    if d is None:
        return None
    p = d / "spec.json"
    return p if p.exists() else None


def active_scratch_dir() -> Path | None:
    d = active_project_dir()
    if d is None:
        return None
    return d / "scratch"


def active_ledger_path() -> Path | None:
    d = active_project_dir()
    if d is None:
        return None
    return d / "ledger.jsonl"


def list_projects() -> list[dict]:
    """List project folders that contain a spec.json, marking the active one."""
    root = projects_root()
    if not root.exists():
        return []
    active = get_active_slug()
    out: list[dict] = []
    for d in sorted(p for p in root.iterdir() if p.is_dir()):
        spec = d / "spec.json"
        if not spec.exists():
            continue
        try:
            data = json.loads(spec.read_text(encoding="utf-8"))
            out.append({
                "slug": d.name,
                "project": str(data.get("project", d.name)),
                "machine_type": str(data.get("machine_type", "generic")),
                "active": d.name == active,
                "path": str(d),
            })
        except Exception as e:
            out.append({"slug": d.name, "error": str(e), "active": False, "path": str(d)})
    return out


def _example_template_path() -> Path | None:
    from src.config.settings import WORKSPACE_ROOT

    cand = WORKSPACE_ROOT / "specs" / "synrm_45kw.json"
    return cand if cand.exists() else None


def create_project(
    slug: str,
    project: str = "",
    machine_type: str = "generic",
    description: str = "",
    model_file: str = "",
    template: str | Path | None = None,
) -> Path:
    """Create a new project folder and make it active.

    Copies the example template spec as a starting point (renaming project/slug
    fields), then the user edits spec.json bounds/targets for their machine.
    Creates scratch/, models/, README.md, and an empty ledger.jsonl.
    """
    slug = validate_slug(slug)
    dest = project_dir(slug)
    if dest.exists():
        raise FileExistsError(f"project '{slug}' already exists: {dest}")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "scratch").mkdir(parents=True, exist_ok=True)
    (dest / "models").mkdir(parents=True, exist_ok=True)

    template_path = Path(template) if template else _example_template_path()
    if template_path is not None and template_path.exists():
        data = json.loads(template_path.read_text(encoding="utf-8"))
    else:
        data = {
            "project": project or slug,
            "slug": slug,
            "machine_type": machine_type or "generic",
            "description": description,
            "operating_point": {},
            "targets": [],
            "params": {},
            "order_chains": [],
            "minimums": [],
            "maximums": [],
            "locked": [],
            "notes": "",
        }
    data["slug"] = slug
    if project:
        data["project"] = project
    if machine_type:
        data["machine_type"] = machine_type
    if description:
        data["description"] = description
    (dest / "spec.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    (dest / "ledger.jsonl").write_text("", encoding="utf-8")

    readme = (
        f"# {data.get('project', slug)}\n\n"
        f"Machine type: {data.get('machine_type', 'generic')}\n\n"
        f"{data.get('description', '')}\n\n".strip() + "\n\n"
        "## Files\n\n"
        "- `spec.json` — targets, param bounds, constraints, locked list, operating point (edit this for your machine).\n"
        "- `ledger.jsonl` — scored candidate log (written automatically).\n"
        "- `scratch/` — generated run scripts for this project.\n"
        "- `models/` — .mot files and backups (e.g. best_so_far.mot).\n"
    )
    (dest / "README.md").write_text(readme, encoding="utf-8")

    if model_file and str(model_file).strip():
        src = Path(str(model_file).strip())
        if src.exists() and src.is_file():
            try:
                shutil.copy2(src, dest / "models" / src.name)
            except Exception:
                pass

    set_active_slug(slug)
    return dest


def ensure_example_project() -> Path | None:
    """Migrate fresh checkouts: copy the example template into projects/ once.

    Only runs when no project folder exists yet, so existing users are never
    touched. Returns the created dir or None.
    """
    try:
        if projects_root().exists() and any(
            (p / "spec.json").exists() for p in projects_root().iterdir() if p.is_dir()
        ):
            return None
        template = _example_template_path()
        if template is None:
            return None
        data = json.loads(template.read_text(encoding="utf-8"))
        slug = str(data.get("slug", "synrm_45kw")).strip() or "synrm_45kw"
        if project_dir(slug).exists():
            return None
        return create_project(
            slug,
            project=str(data.get("project", slug)),
            machine_type=str(data.get("machine_type", "generic")),
            description=str(data.get("description", "")),
        )
    except Exception:
        return None


__all__ = [
    "active_ledger_path",
    "active_project_dir",
    "active_scratch_dir",
    "active_spec_path",
    "active_pointer_path",
    "create_project",
    "ensure_example_project",
    "get_active_slug",
    "ledger_path",
    "list_projects",
    "models_dir",
    "project_dir",
    "projects_root",
    "sanitize_slug",
    "scratch_dir",
    "set_active_slug",
    "spec_path",
    "validate_slug",
]
