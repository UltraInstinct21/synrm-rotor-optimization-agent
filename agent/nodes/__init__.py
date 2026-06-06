"""Pipeline node implementations — one function per phase."""
from agent.nodes.research import research_node
from agent.nodes.calculate import calculate_node
from agent.nodes.design import design_node

# Stubs for phases not yet implemented
from agent.state import AgentState


def synthesis_node(state: AgentState) -> AgentState:
    """Phase 2 — Synthesis (stub)."""
    state["phase"] = "synthesis"
    state["phase_status"]["synthesis"] = {"status": "done", "error": None}
    state["wiki_synthesis"] = state.get("wiki_synthesis", [])
    state["wiki_synthesis"].append("synthesis/stub")
    return state
