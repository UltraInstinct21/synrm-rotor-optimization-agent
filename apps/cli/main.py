"""CLI entry point — motor-deepagent terminal engineering assistant.

Usage:
    python -m apps.cli.main "your request here"
    python -m apps.cli.main          # interactive REPL
"""

from __future__ import annotations

import argparse
import sys

from apps.cli.chat import interactive_repl
from apps.cli.display import print_header, print_report
from src.agent.build_agent import build_orchestrator
from src.agent.orchestration_helpers import classify_request
from src.config.settings import OPENROUTER_API_KEY


def main() -> None:
    parser = argparse.ArgumentParser(
        description="motor-deepagent — terminal-first engineering assistant",
    )
    parser.add_argument(
        "request",
        nargs="?",
        help="Request to process.  Omit for interactive REPL.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="LLM model override (default: qwen/qwq-32b:free)",
    )
    parser.add_argument(
        "--show-plan",
        action="store_true",
        help="Print the orchestrator's plan before executing.",
    )

    args = parser.parse_args()

    if not OPENROUTER_API_KEY:
        print(
            "⚠️  OPENROUTER_API_KEY not set.  Set it in .env or as an env var.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Build the orchestrator config.
    orchestrator = build_orchestrator(model=args.model)

    print_header()

    if args.request:
        # Single-shot mode.
        category = classify_request(args.request)
        print(f"  Task category: {category}\n")

        if args.show_plan:
            print(f"  [Plan] Would delegate to appropriate subsystem.\n")

        # Invoke the orchestrator (stub — real agent call goes here).
        print_report(
            title="Orchestrator Response",
            sections=[
                ("Request", args.request),
                ("Category", category),
                ("Status", "Orchestrator built.  Agent SDK integration pending."),
            ],
        )
    else:
        # Interactive REPL.
        interactive_repl(model=args.model, show_plan=args.show_plan)


if __name__ == "__main__":
    main()
