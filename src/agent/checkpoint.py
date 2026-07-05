"""Checkpointer setup for LangGraph state persistence."""

from __future__ import annotations

from langgraph.checkpoint.memory import MemorySaver


def get_checkpointer() -> MemorySaver:
    """Return an in-memory checkpointer for session persistence.

    In production, replace with SqliteSaver or PostgresSaver.
    """
    return MemorySaver()
