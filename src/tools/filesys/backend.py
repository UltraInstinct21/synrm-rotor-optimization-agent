"""Virtual filesystem backend — maps virtual paths to real filesystem locations.

The ``BACKEND_ROUTES`` dict in ``settings.py`` defines the mapping::

    BACKEND_ROUTES = {
        "/workspace/": str(PROJECT_ROOT / "workspace"),
        "/repo/":      str(PROJECT_ROOT),
    }

The ``resolve()`` function translates a virtual path to an absolute ``Path``::

    resolve("/workspace/wiki/index.md")
    # → Path("D:/SRM/Agent/workspace/wiki/index.md")

If no virtual prefix matches, the path is resolved relative to the project root.
"""

from __future__ import annotations

from pathlib import Path

from src.config import settings


class VirtualFileSystem:
    """Resolve virtual paths against a set of route mappings.

    Usage::

        vfs = VirtualFileSystem()
        local = vfs.resolve("/workspace/wiki/index.md")
    """

    def __init__(self, routes: dict[str, str] | None = None) -> None:
        self._routes: dict[str, Path] = {}
        for prefix, real_path in (routes or settings.BACKEND_ROUTES).items():
            # Normalise: ensure prefix starts with / and ends with /
            normalised = f"/{prefix.strip('/')}/" if prefix.strip("/") else prefix
            self._routes[normalised] = Path(real_path).resolve()

    # ── Public API ───────────────────────────────────────────────────

    def resolve(self, virtual: str | Path) -> Path:
        """Translate a virtual path to an absolute filesystem ``Path``.

        If *virtual* is already an absolute path it is returned as-is.
        If no route matches, it's resolved relative to ``PROJECT_ROOT``.
        """
        p = Path(virtual)
        if p.is_absolute():
            return p

        virtual_str = str(virtual).replace("\\", "/")

        # Longest-prefix match.
        matched: str | None = None
        for prefix in sorted(self._routes, key=len, reverse=True):
            if virtual_str.startswith(prefix) or virtual_str.startswith(prefix.lstrip("/")):
                matched = prefix
                break

        if matched is not None:
            relative = virtual_str.removeprefix(matched).removeprefix(matched.lstrip("/"))
            return (self._routes[matched] / relative).resolve()

        # Fall through to project root.
        return (settings.PROJECT_ROOT / virtual_str).resolve()

    def list_routes(self) -> dict[str, str]:
        """Return the route mapping for display."""
        return {k: str(v) for k, v in self._routes.items()}

    def is_safe(self, path: Path) -> bool:
        """Check whether *path* falls inside any registered route."""
        resolved = path.resolve()
        return any(
            str(resolved).startswith(str(real.resolve()))
            for real in self._routes.values()
        )


# Module-level singleton for convenience.
_default: VirtualFileSystem | None = None


def get_vfs() -> VirtualFileSystem:
    global _default
    if _default is None:
        _default = VirtualFileSystem()
    return _default


def resolve(virtual: str | Path) -> Path:
    """Shortcut: resolve a virtual path via the default ``VirtualFileSystem``."""
    return get_vfs().resolve(virtual)
