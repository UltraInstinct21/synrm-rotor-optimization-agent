"""File-system tools for the agent: read, write, grep, ls.

Paths can be virtual paths (``/workspace/wiki/index.md``, ``/repo/src/``)
that resolve via the ``VirtualFileSystem`` in ``backend.py``.
"""

from __future__ import annotations

from pathlib import Path

from agents import function_tool, RunContextWrapper

from src.config import settings
from src.tools.filesys.backend import resolve

PROJECT_ROOT = settings.PROJECT_ROOT


def _check_safe(path: str) -> Path:
    """Resolve (virtual → real) and verify it's inside project root."""
    resolved = resolve(path).resolve()
    proj = PROJECT_ROOT.resolve()
    if not str(resolved).startswith(str(proj)):
        raise ValueError(f"Access denied: '{path}' resolves outside project root.")
    return resolved


@function_tool
async def read_file(ctx: RunContextWrapper, path: str, max_chars: int = 0) -> str:
    """Read the contents of a file.

    Accepts virtual paths (``/workspace/wiki/index.md``) and real paths.
    Only files inside the project root are accessible.

    Args:
        path:      Virtual or real path to the file.
        max_chars: Maximum characters to return (0 = full file).

    Returns:
        File contents.
    """
    full = _check_safe(path)
    if not full.is_file():
        return f"File not found: {path}"
    try:
        text = full.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        return f"Error reading {path}: {exc}"
    if max_chars and len(text) > max_chars:
        text = text[:max_chars] + f"\n... (truncated, {len(text)} total chars)"
    return text


@function_tool
async def write_file(ctx: RunContextWrapper, path: str, content: str) -> str:
    """Write content to a file (overwrites if exists).

    Accepts virtual paths.  Only files inside the project root are writable.

    Args:
        path:    Virtual or real path to the file.
        content: Text content to write.

    Returns:
        Confirmation.
    """
    full = _check_safe(path)
    full.parent.mkdir(parents=True, exist_ok=True)
    try:
        full.write_text(content, encoding="utf-8")
        return f"Wrote {len(content)} chars to {path}"
    except Exception as exc:
        return f"Error writing {path}: {exc}"


@function_tool
async def grep_files(
    ctx: RunContextWrapper, pattern: str, path: str = "", glob: str = "*"
) -> str:
    """Search for a text pattern in files within the project.

    Args:
        pattern: Text or regex pattern to search for.
        path:    Virtual or real path to search (default: project root).
        glob:    File glob pattern (e.g. ``"*.py"``, ``"*.md"``).

    Returns:
        Matching lines grouped by file.
    """
    root = _check_safe(path) if path else PROJECT_ROOT
    if not root.is_dir():
        return f"Directory not found: {path}"

    import re

    matches: list[str] = []
    files = list(root.rglob(glob))[:100]  # limit to 100 files
    for f in files:
        if not f.is_file():
            continue
        try:
            for i, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").split("\n"), 1):
                if re.search(pattern, line, re.IGNORECASE):
                    rel = f.relative_to(PROJECT_ROOT)
                    matches.append(f"  {rel}:{i}: {line.strip()[:200]}")
        except Exception:
            pass
    if not matches:
        return f"No matches for '{pattern}' in {root}."
    return f"Found {len(matches)} match(es):\n" + "\n".join(matches[:50])


@function_tool
async def list_directory(
    ctx: RunContextWrapper, path: str = "", pattern: str = "*", depth: int = 1
) -> str:
    """List files and directories.

    Args:
        path:    Virtual or real path to list (default: project root).
        pattern: Glob filter (e.g. ``"*.py"``, ``"**/*.md"``).
        depth:   How deep to recurse (1 = flat, 0 = unlimited).

    Returns:
        File/directory listing.
    """
    root = _check_safe(path) if path else PROJECT_ROOT
    if not root.is_dir():
        return f"Directory not found: {path}"

    lines: list[str] = []
    for f in sorted(root.rglob(pattern)) if depth == 0 else sorted(root.glob(pattern)):
        try:
            rel = f.relative_to(PROJECT_ROOT)
            marker = "/" if f.is_dir() else ""
            lines.append(f"  {rel}{marker}")
        except ValueError:
            pass
    if not lines:
        return f"Nothing found at {path}"
    return f"Contents of {root}:\n" + "\n".join(lines[:200])
