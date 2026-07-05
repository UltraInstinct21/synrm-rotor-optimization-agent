"""Interactive REPL loop for motor-deepagent."""

from __future__ import annotations

from apps.cli.display import print_header, print_report, print_separator
from src.agent.build_agent import build_orchestrator
from src.agent.orchestration_helpers import classify_request


def interactive_repl(model: str | None = None, show_plan: bool = False) -> None:
    """Run an interactive terminal session.

    The user types requests; the orchestrator classifies and (eventually)
    routes them to the appropriate subsystem.
    """
    print("  Type your request below, or :q to quit.\n")

    history: list[dict] = []

    while True:
        try:
            raw = input("  ⚡ ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not raw:
            continue
        if raw in (":q", ":quit", ":exit"):
            break

        category = classify_request(raw)
        history.append({"request": raw, "category": category})

        print(f"    └─ category: {category}")

        if show_plan:
            print(f"    └─ plan: inspect → delegate → synthesize")

        print_separator()

    # Session summary.
    if history:
        print()
        print_report(
            title="Session Summary",
            sections=[
                ("Requests", str(len(history))),
                ("Categories", ", ".join(set(h["category"] for h in history))),
            ],
        )
