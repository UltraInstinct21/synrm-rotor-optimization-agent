"""Terminal display utilities — header, separators, report rendering."""

from __future__ import annotations

import shutil

# ── Characters ────────────────────────────────────────────────────────
_TERM_WIDTH = shutil.get_terminal_size(fallback=80).columns


def print_header() -> None:
    """Render the motor-deepagent header."""
    print()
    print("=" * _TERM_WIDTH)
    title = "motor-deepagent  ⚡  terminal engineering assistant"
    print(f"  {title}")
    print("=" * _TERM_WIDTH)
    print()


def print_separator(char: str = "─") -> None:
    """Print a horizontal rule."""
    print(f"  {char * min(_TERM_WIDTH - 2, 60)}")


def print_report(title: str, sections: list[tuple[str, str]]) -> None:
    """Print a named report with labelled sections.

    Parameters
    ----------
    title : str
        Report title.
    sections : list of (label, content) tuples
        Each section is rendered as ``label: content``.
    """
    print()
    print(f"  ┌─ {title}")
    print(f"  │")
    for label, content in sections:
        # Word-wrap long content.
        for line in content.split("\n"):
            print(f"  ├  {label}: {line}" if label else f"  │  {line}")
            label = ""  # only show label on first line
    print(f"  └─")
    print()
