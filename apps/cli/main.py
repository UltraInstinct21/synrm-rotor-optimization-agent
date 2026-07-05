"""CLI entry point — motor-deepagent terminal engineering assistant.

Usage:
    python -m apps.cli.main "your request here"
    python -m apps.cli.main          # interactive REPL
"""

from __future__ import annotations

import argparse
import asyncio
import sys

from apps.cli.chat import interactive_repl
from apps.cli.display import print_header, print_report
from src.agent.orchestration_helpers import classify_request
from src.agent.runtime import run_request
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
            "  ⚠️  OPENROUTER_API_KEY not set.  Set it in .env or as an env var.",
            file=sys.stderr,
        )
        sys.exit(1)

    print_header()

    if args.request:
        # Single-shot mode.
        result = asyncio.run(run_request(args.request, model=args.model))

        print(f"  Category: {result['category']}")
        if args.show_plan and result["plan"]:
            print(f"  Plan:")
            for step in result["plan"]:
                print(f"    • {step}")

        if "synthesis" in result and result["synthesis"]:
            print(f"\n  {result['synthesis']}")

        # Print delegation summaries.
        for subsystem, output in result.get("delegations", {}).items():
            if hasattr(output, "result"):
                status = output.result if isinstance(output.result, str) else "done"
            else:
                status = "done"
            print(f"  └─ {subsystem}: {status}")

    else:
        # Interactive REPL.
        asyncio.run(interactive_repl(model=args.model, show_plan=args.show_plan))


if __name__ == "__main__":
    main()
