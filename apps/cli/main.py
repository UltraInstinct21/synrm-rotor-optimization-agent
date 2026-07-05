"""CLI entry point — motor-deepagent terminal engineering assistant.

Usage:
    python -m apps.cli.main "your request here"
    python -m apps.cli.main          # interactive REPL
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv

from apps.cli.chat import interactive_repl
from apps.cli.display import print_header, print_report
from src.agent.orchestration_helpers import classify_request
from src.agent.runtime import run_request
from src.config import settings
from src.config.settings import LLM_API_KEY


def main() -> None:
    # Load .env from project root
    env_path = Path(__file__).resolve().parent.parent.parent / ".env"
    load_dotenv(env_path, override=False)

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
        help=f"LLM model override (default: {settings.MODEL_DEFAULT})",
    )
    parser.add_argument(
        "--show-plan",
        action="store_true",
        help="Print the orchestrator's plan before executing.",
    )

    args = parser.parse_args()

    if not LLM_API_KEY:
        print(
            "  ⚠️  OPENCODE_API_KEY not set.  Set it in .env or as an env var.",
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
