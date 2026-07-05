"""Terminal display utilities — header, separators, report rendering.

Uses only ASCII characters for Windows cp1252 compatibility.
"""

from __future__ import annotations

import shutil

_TERM_WIDTH = shutil.get_terminal_size(fallback=(80, 24)).columns


def print_header() -> None:
    """Render the motor-deepagent header (ASCII-safe)."""
    print()
    print("=" * _TERM_WIDTH)
    print("  motor-deepagent >> terminal engineering assistant")
    print("=" * _TERM_WIDTH)
    print()


def print_separator(char: str = "-") -> None:
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
    print(f"  == {title} ==")
    for label, content in sections:
        for line in content.split("\n"):
            if label:
                print(f"  {label}: {line}")
                label = ""
            else:
                print(f"  {line}")
    print()
