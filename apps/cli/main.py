"""motor-deepagent CLI — entry point."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env", override=False)


def _build_agent():
    """Build the Deep Agents instance with Motor-CAD tools."""
    from src.agent.factory import build_agent

    return build_agent()


def main() -> None:
    from apps.cli.app import MotorCLI

    cli = MotorCLI()
    if len(sys.argv) > 1:
        cli.single_shot(" ".join(sys.argv[1:]))
    else:
        cli.run()


if __name__ == "__main__":
    main()
