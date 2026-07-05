"""LangGraph state machine for motor-deepagent."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from src.agent.checkpoint import get_checkpointer
from src.agent.nodes import (
    classify_node,
    execute_code_node,
    execute_experiment_node,
    execute_research_node,
    execute_wiki_node,
    route_node,
    synthesize_node,
)
from src.agent.state import MotorState


def build_graph() -> StateGraph:
    """Build the motor-deepagent LangGraph.

    Returns compiled graph with checkpointer for state persistence.
    """
    builder = StateGraph(MotorState)

    # Add nodes
    builder.add_node("classify", classify_node)
    builder.add_node("execute_code", execute_code_node)
    builder.add_node("execute_wiki", execute_wiki_node)
    builder.add_node("execute_research", execute_research_node)
    builder.add_node("execute_experiment", execute_experiment_node)
    builder.add_node("synthesize", synthesize_node)

    # Add edges — classify routes directly via conditional edges
    builder.add_edge(START, "classify")
    builder.add_conditional_edges(
        "classify",
        route_node,
        {
            "execute_code": "execute_code",
            "execute_wiki": "execute_wiki",
            "execute_research": "execute_research",
            "execute_experiment": "execute_experiment",
            "synthesize": "synthesize",
        },
    )

    # All execution nodes go to synthesize
    builder.add_edge("execute_code", "synthesize")
    builder.add_edge("execute_wiki", "synthesize")
    builder.add_edge("execute_research", "synthesize")
    builder.add_edge("execute_experiment", "synthesize")
    builder.add_edge("synthesize", END)

    # Compile with checkpointer
    checkpointer = get_checkpointer()
    return builder.compile(checkpointer=checkpointer)


# Pre-compiled graph for import
motor_graph = build_graph()
