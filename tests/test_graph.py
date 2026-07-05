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


def test_classify_node():
    """classify_node sets category based on request."""
    from src.agent.nodes import classify_node

    state = {"messages": [{"role": "user", "content": "inspect the code"}]}
    result = classify_node(state)
    assert result["category"] == "repo_coding"


def test_route_node():
    """route_node returns correct next node name."""
    from src.agent.nodes import route_node

    state = {"category": "repo_coding"}
    assert route_node(state) == "execute_code"

    state = {"category": "wiki_maintenance"}
    assert route_node(state) == "execute_wiki"

    state = {"category": "research"}
    assert route_node(state) == "execute_research"

    state = {"category": "experiment"}
    assert route_node(state) == "execute_experiment"

    state = {"category": "question"}
    assert route_node(state) == "synthesize"


def test_checkpointer_setup():
    """Checkpointer can be created."""
    from src.agent.checkpoint import get_checkpointer

    checkpointer = get_checkpointer()
    assert checkpointer is not None


def test_graph_builds():
    """Graph can be built and compiled."""
    from src.agent.graph import build_graph

    graph = build_graph()
    assert graph is not None


def test_graph_has_nodes():
    """Graph has all required nodes."""
    from src.agent.graph import build_graph

    graph = build_graph()
    nodes = list(graph.nodes.keys())
    assert "classify" in nodes
    assert "route" in nodes
    assert "execute_code" in nodes
    assert "execute_wiki" in nodes
    assert "execute_research" in nodes
    assert "execute_experiment" in nodes
    assert "synthesize" in nodes
