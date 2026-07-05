"""LangGraph state definition for motor-deepagent."""

from __future__ import annotations

from typing import Any, Optional, TypedDict

from typing_extensions import Annotated

from langgraph.graph import add_messages


class MotorState(TypedDict, total=False):
    """State channels for the motor-deepagent graph.

    Attributes:
        messages: Conversation history (reducer: append).
        category: Classified task type.
        delegations: Subsystem results keyed by agent name.
        active_agent: Current routing target.
        pending_changes: Motor parameter changes awaiting approval.
        last_checkpoint: Path to last Motor-CAD save state.
    """

    messages: Annotated[list, add_messages]
    category: str
    delegations: dict[str, Any]
    active_agent: str
    pending_changes: Optional[dict]
    last_checkpoint: Optional[str]
