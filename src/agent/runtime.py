"""Runtime entry point — backward-compat `run_request` for deepagents."""
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def run_request(query: str, thread_id: str = "default") -> dict:
    """Invoke the deepagents instance directly.

    Creates a fresh agent with all Motor-CAD and research tools.
    """
    from src.agent.factory import build_agent
    try:
        from src.config import settings

        agent, _ = build_agent()
        return agent.invoke(
            {"messages": [("user", query)]},
            config={
                "configurable": {"thread_id": thread_id},
                "recursion_limit": settings.RECURSION_LIMIT,
            },
        )
    except Exception as e:
        logger.error("Agent invocation failed: %s", e)
        return {
            "messages": [("assistant", f"Error: Agent invocation failed — {e}")],
            "error": str(e),
        }


__all__ = ["run_request"]