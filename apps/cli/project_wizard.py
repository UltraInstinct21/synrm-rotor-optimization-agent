"""Per-project selection/creation wizard run once on CLI launch."""

from __future__ import annotations


def _say(console, msg: str) -> None:
    """Print to console if available, else plain print. Never raises."""
    try:
        if console is not None and hasattr(console, "print"):
            try:
                console.print(msg)
                return
            except Exception:
                pass
        print(msg)
    except Exception:
        pass


def ensure_project_on_launch(console) -> str | None:
    """Ensure a project is selected on CLI launch.

    - Runs one-time example migration (silent).
    - Fast path: active slug with loadable spec -> return silently.
    - Otherwise prompt via plain input(): numbered select, 'new', or Enter.
    - Never raises; EOF/KeyboardInterrupt -> current active slug or None.
    """
    from src.config.projects import (
        create_project,
        ensure_example_project,
        get_active_slug,
        list_projects,
        sanitize_slug,
        set_active_slug,
        validate_slug,
    )

    # (a) one-time migration, silent.
    try:
        ensure_example_project()
    except Exception:
        pass

    def _current_active() -> str | None:
        try:
            return get_active_slug()
        except Exception:
            return None

    # (b) fast path: active slug whose spec loads -> no output, no prompt.
    active = _current_active()
    if active:
        try:
            from src.motor.spec import load_active_spec

            load_active_spec()
            return active
        except Exception:
            pass

    # (c) interactive prompt.
    try:
        try:
            projects = list_projects()
        except Exception:
            projects = []

        if projects:
            _say(console, "Projects:")
            for i, p in enumerate(projects, 1):
                slug = str(p.get("slug", "?"))
                proj = str(p.get("project", slug))
                mtype = str(p.get("machine_type", "generic"))
                marker = " [active]" if p.get("active") else ""
                _say(console, f"  {i}. {slug} ({proj}, {mtype}){marker}")
        else:
            _say(console, "No projects found.")

        while True:
            try:
                choice = input("Select project [number], 'new' to create, or Enter to continue: ")
            except (EOFError, KeyboardInterrupt):
                return _current_active() or active
            except StopIteration:
                return _current_active() or active

            text = (choice or "").strip()
            if not text:
                return _current_active() or active
            low = text.lower()
            if low == "new":
                created = _create_flow(console, create_project, sanitize_slug, validate_slug)
                if created:
                    return created
                return _current_active() or active
            if text.isdigit():
                idx = int(text) - 1
                if 0 <= idx < len(projects):
                    slug = str(projects[idx].get("slug", "")).strip()
                    try:
                        set_active_slug(slug)
                        _say(console, f"Active project -> {slug}")
                        return slug
                    except Exception as e:
                        _say(console, f"Failed to select project '{slug}': {e}")
                        return _current_active() or active
                _say(console, f"Invalid selection '{text}'. Enter a number 1-{len(projects)}, 'new', or Enter.")
                continue
            # Treat bare slug as a select attempt.
            slug = text
            try:
                set_active_slug(slug)
                _say(console, f"Active project -> {slug}")
                return slug
            except FileNotFoundError:
                _say(console, f"Project '{slug}' not found.")
                continue
            except Exception as e:
                _say(console, f"Failed to select project '{slug}': {e}")
                continue
    except (EOFError, KeyboardInterrupt):
        try:
            return _current_active() or active
        except Exception:
            return None
    except Exception:
        try:
            return _current_active() or active
        except Exception:
            return None


def _create_flow(console, create_project, sanitize_slug, validate_slug) -> str | None:
    """Run the creation prompts. Returns new slug or None."""
    # Slug (sanitized/validated, re-prompt on invalid).
    slug = ""
    while True:
        try:
            raw = input("Project slug: ")
        except (EOFError, KeyboardInterrupt, StopIteration):
            return None
        cleaned = sanitize_slug(raw or "")
        try:
            if not cleaned:
                raise ValueError(f"invalid project slug '{raw}'")
            slug = validate_slug(cleaned)
            break
        except Exception as e:
            _say(console, f"Invalid slug: {e}. Use lowercase letters, digits, '-' or '_'.")
            continue

    try:
        try:
            display = input(f"Display name [{slug}]: ")
        except (EOFError, KeyboardInterrupt, StopIteration):
            display = slug
        display = (display or "").strip() or slug

        try:
            mtype = input("Machine type [generic]: ")
        except (EOFError, KeyboardInterrupt, StopIteration):
            mtype = "generic"
        mtype = (mtype or "").strip() or "generic"

        try:
            desc = input("Description (optional): ")
        except (EOFError, KeyboardInterrupt, StopIteration):
            desc = ""
        desc = (desc or "").strip()

        try:
            model_file = input(".mot model file path (optional): ")
        except (EOFError, KeyboardInterrupt, StopIteration):
            model_file = ""
        model_file = (model_file or "").strip()
    except (EOFError, KeyboardInterrupt):
        return None

    try:
        dest = create_project(
            slug,
            project=display,
            machine_type=mtype,
            description=desc,
            model_file=model_file,
        )
        _say(console, f"Created project '{slug}' at {dest}")
        return slug
    except Exception as e:
        _say(console, f"Failed to create project '{slug}': {e}")
        return None
