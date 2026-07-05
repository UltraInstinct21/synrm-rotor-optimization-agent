"""Interactive REPL loop for motor-deepagent."""

from __future__ import annotations

from apps.cli.display import print_header, print_report, print_separator
from src.agent.orchestration_helpers import classify_request
from src.agent.runtime import InteractiveSession


async def interactive_repl(model: str | None = None, show_plan: bool = False) -> None:
    """Run an interactive terminal session using the real agent runtime."""
    session = InteractiveSession(model=model)

    print("  Type your request below, or :q to quit.\n")

    while True:
        try:
            raw = input("  >> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not raw:
            continue
        if raw in (":q", ":quit", ":exit"):
            break
        if raw == ":summary":
            print(f"  {session.summary()}")
            continue
        if raw == ":plan" and show_plan:
            _print_plan_examples()
            continue

        # Process through the real agent runtime.
        result = await session.process(raw)

        category = result["category"]
        print(f"    └─ category: {category}")

        if show_plan and result["plan"]:
            print(f"    └─ plan:")
            for step in result["plan"]:
                print(f"         • {step}")

        # Show delegation summaries.
        delegations = result.get("delegations", {})
        if delegations:
            for name, output in delegations.items():
                if hasattr(output, "result"):
                    status = output.result if isinstance(output.result, str) else "done"
                elif hasattr(output, "confidence"):
                    status = f"confidence={output.confidence}"
                else:
                    status = "done"
                print(f"    └─ {name}: {status}")

        # Show synthesis if present.
        if result.get("synthesis"):
            summary = result["synthesis"]
            if len(summary) > 300:
                summary = summary[:300] + "..."
            print(f"    └─ {summary}")

        print_separator()


def _print_plan_examples() -> None:
    print()
    print("  Example request patterns:")
    print('    "inspect the optimizer module structure"')
    print('    "read the codebase_map and update the wiki"')
    print('    "compare current-angle conventions across sources"')
    print('    "run the sweep script and summarize results"')
    print()
