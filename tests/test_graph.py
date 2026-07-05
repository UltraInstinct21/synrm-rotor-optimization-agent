"""Tests for LangGraph state machine."""

from __future__ import annotations


def test_motor_state_import():
    """MotorState can be imported and instantiated."""
    from src.agent.state import MotorState

    state: MotorState = {
        "messages": [],
        "category": "question",
        "delegations": {},
        "active_agent": "",
        "pending_changes": None,
        "last_checkpoint": None,
    }
    assert state["category"] == "question"
    assert state["delegations"] == {}
