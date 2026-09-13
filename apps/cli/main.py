"""motor-deepagent CLI — entry point."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env", override=False)


def _build_checkpointer():
    """Return a LangGraph checkpointer so tool results persist across turns.

    SqliteSaver (durable, survives CLI restarts) when langgraph-checkpoint-sqlite
    is installed; otherwise the in-memory saver. No new dependencies are added.
    """
    import sqlite3

    try:
        from langgraph.checkpoint.sqlite import SqliteSaver

        session_dir = PROJECT_ROOT / ".session"
        session_dir.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(session_dir / "checkpoints.db"), check_same_thread=False)
        return SqliteSaver(conn)
    except ImportError:
        from langgraph.checkpoint.memory import InMemorySaver

        return InMemorySaver()


def _build_agent(model=None):
    """Build the Deep Agents instance with Motor-CAD tools."""
    from src.agent.factory import build_agent

    return build_agent(model=model, checkpointer=_build_checkpointer())


def main() -> None:
    from apps.cli.app import MotorCLI

    cli = MotorCLI()
    if len(sys.argv) > 1:
        cli.single_shot(" ".join(sys.argv[1:]))
    else:
        cli.run()


if __name__ == "__main__":
    main()
