"""LangGraph state machine — 4-phase pipeline for SynRM design."""

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from agent.state import AgentState


def phase_router(state: AgentState) -> str:
    """Route to the next phase based on current phase_status."""
    status = state.get("phase_status", {})

    # If no phase started yet, start with research
    if not status:
        return "research"

    # Check completed phases in order
    order = ["research", "synthesis", "calculate", "design"]
    current = state.get("phase", "research")

    # Find current index and route to next
    try:
        idx = order.index(current)
    except ValueError:
        return "research"

    # If current phase done, move to next
    current_status = status.get(current, {}).get("status", "")
    if current_status == "done":
        if idx + 1 < len(order):
            return order[idx + 1]
        return END  # all phases done

    # If current phase failed, check if we can skip
    if current_status == "failed":
        # Try to move to next phase
        if idx + 1 < len(order):
            return order[idx + 1]
        return END

    # Continue current phase
    return current


def research_node_wrapper(state: AgentState) -> AgentState:
    """Wrapper for Phase 1 — Research node."""
    from agent import nodes

    return nodes.research_node(state)


def synthesis_node_wrapper(state: AgentState) -> AgentState:
    """Wrapper for Phase 2 — Synthesis node."""
    from agent import nodes

    return nodes.synthesis_node(state)


def calculate_node_wrapper(state: AgentState) -> AgentState:
    """Wrapper for Phase 3 — Calculation node."""
    from agent import nodes

    return nodes.calculate_node(state)


def design_node_wrapper(state: AgentState) -> AgentState:
    """Wrapper for Phase 4 — Design & Optimization node."""
    from agent import nodes

    return nodes.design_node(state)


def build_graph() -> StateGraph:
    """Build and compile the 4-phase LangGraph pipeline."""
    builder = StateGraph(AgentState)

    # Add all phase nodes
    builder.add_node("research", research_node_wrapper)
    builder.add_node("synthesis", synthesis_node_wrapper)
    builder.add_node("calculate", calculate_node_wrapper)
    builder.add_node("design", design_node_wrapper)

    # Conditional edges: START -> router -> phases -> END
    builder.add_conditional_edges(START, phase_router)
    builder.add_conditional_edges("research", phase_router)
    builder.add_conditional_edges("synthesis", phase_router)
    builder.add_conditional_edges("calculate", phase_router)
    builder.add_conditional_edges("design", phase_router)

    # Compile with checkpointer
    checkpointer = MemorySaver()
    return builder.compile(checkpointer=checkpointer)


def initial_state(motor_spec: dict | None = None) -> AgentState:
    """Create a default initial state for the pipeline."""
    return {
        "messages": [],
        "phase": "research",
        "phase_status": {},
        "error_log": [],
        "wiki_entities_created": [],
        "wiki_concepts_created": [],
        "wiki_synthesis": [],
        "motor_spec": motor_spec
        or {
            "power_kw": 45,
            "torque_nm": 143,
            "speed_rpm": 3000,
            "poles": 4,
            "voltage_v": 580,
            "target_efficiency": 96.0,
            "target_pf": 0.85,
        },
        "winding_params": {},
        "barrier_params": {},
        "derived_params": {},
        "mot_file_path": "D:/SRM/Agent/SynRM_45kW_IE5.mot",
        "mot_sections": {},
        "pymotorcad_vars": [],
        "optimization_results": [],
        "best_model_path": "",
    }
