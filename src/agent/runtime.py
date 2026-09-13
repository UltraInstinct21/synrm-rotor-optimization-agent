"""Runtime entry point — backward-compat `run_request` for deepagents."""
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def run_request(query: str, thread_id: str = "default") -> dict:
    """Invoke the deepagents instance directly.

    Creates a fresh agent with all Motor-CAD and research tools and an
    in-memory checkpointer so `thread_id` isolates concurrent callers.
    For persistent cross-turn memory use the CLI (SqliteSaver) instead.
    """
    from src.agent.factory import build_agent
    try:
        from langgraph.checkpoint.memory import InMemorySaver

        from src.config import settings

        agent, _ = build_agent(checkpointer=InMemorySaver())
        config: dict = {"configurable": {"thread_id": thread_id}}
        _limit = settings.get_recursion_limit()
        if _limit is not None:
            config["recursion_limit"] = _limit
        return agent.invoke(
            {"messages": [("user", query)]},
            config=config,
        )
    except Exception as e:
        logger.error("Agent invocation failed: %s", e)
        return {
            "messages": [("assistant", f"Error: Agent invocation failed — {e}")],
            "error": str(e),
        }


__all__ = ["run_request"]