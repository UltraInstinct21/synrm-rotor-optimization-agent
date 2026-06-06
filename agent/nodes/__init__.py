"""Pipeline node implementations — one function per phase."""
from agent.nodes.research import research_node

# Stubs for phases not yet implemented
from agent.state import AgentState


def synthesis_node(state: AgentState) -> AgentState:
    """Phase 2 — Synthesis (stub)."""
    state["phase"] = "synthesis"
    state["phase_status"]["synthesis"] = {"status": "done", "error": None}
    state["wiki_synthesis"] = state.get("wiki_synthesis", [])
    state["wiki_synthesis"].append("synthesis/stub")
    return state


def calculate_node(state: AgentState) -> AgentState:
    """Phase 3 — Calculation (stub)."""
    state["phase"] = "calculate"
    state["phase_status"]["calculate"] = {"status": "done", "error": None}
    state["winding_params"] = {
        "kw": 0.9576,
        "turns_per_slot": 24,
        "fill_factor": 0.45,
        "note": "stub — replace with real calculation",
    }
    return state


def design_node(state: AgentState) -> AgentState:
    """Phase 4 — Design (stub)."""
    state["phase"] = "design"
    state["phase_status"]["design"] = {"status": "done", "error": None}
    state["barrier_params"] = {
        "L1_Dia": 120.0,
        "L2_Dia": 85.0,
        "L3_Dia": 50.0,
        "note": "stub — replace with real parameters",
    }
    return state
