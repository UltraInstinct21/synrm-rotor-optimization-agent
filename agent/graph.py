"""LangGraph state machine — 4-phase pipeline for SynRM design.

Features:
  - Linear pipeline: research → synthesis → calculate → design → END
  - Streaming-ready: stream_mode="updates" emits per-node state diffs
  - Human-in-the-loop: interrupt before optimization approval gate
  - Long-term memory: MemoryStore cross-session parameter persistence
  - Map-reduce: parallel candidate evaluation within optimization sub-node
"""

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from agent.state import AgentState, PhaseStatus

# Phase order — defines the linear pipeline sequence.
# "optimization_approval" is the human-in-the-loop gate before design.
PHASE_ORDER = ["research", "synthesis", "calculate", "optimization_approval", "design"]


def get_next_phase(current: str) -> str | None:
    """Return the next phase after current, or None if last."""
    try:
        idx = PHASE_ORDER.index(current)
        if idx + 1 < len(PHASE_ORDER):
            return PHASE_ORDER[idx + 1]
        return None
    except ValueError:
        return PHASE_ORDER[0]


def safe_node_wrapper(node_func, state: AgentState, phase_name: str = "") -> dict:
    """Wrap a node execution in try/except, marking phase as failed on error.

    phase_name is explicit so failure routing is deterministic even if
    state["phase"] hasn't been set yet (import error, early crash).
    """
    try:
        result = node_func(state)
        return result
    except Exception as e:
        import traceback
        error_msg = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
        name = phase_name or state.get("phase", "?")
        print(f"  [ERROR] Phase {name} failed: {error_msg}")
        return {
            "phase_status": {
                **state.get("phase_status", {}),
                name: PhaseStatus(status="failed", error=error_msg),
            }
        }


def phase_router(state: AgentState) -> str:
    """Route to next phase based on phase_status.

    Normal transitions:
      done/failed/skipped  → advance to next phase (or END)
      running/pending      → retry current (self-loop)

    Any unhandled status string is treated as failed and routes forward,
    preventing infinite self-loops from corrupt/typo'd status values.
    """
    status = state.get("phase_status", {})

    if not status:
        return PHASE_ORDER[0]

    current = state.get("phase", PHASE_ORDER[0])

    try:
        PHASE_ORDER.index(current)
    except ValueError:
        return PHASE_ORDER[0]

    current_status = status.get(current, {}).get("status", "")

    # Terminal statuses → advance
    if current_status in ("done", "failed", "skipped"):
        next_ph = get_next_phase(current)
        return next_ph if next_ph else END

    # Unknown/corrupt non-empty status → treat as failed, advance
    if current_status and current_status not in ("running", "pending"):
        next_ph = get_next_phase(current)
        return next_ph if next_ph else END

    # Still running or initial → stay
    return current


def _make_node_wrapper(phase_name: str, func_name: str):
    """Factory: create a node wrapper with import safety + deterministic phase name.

    Imports `agent.nodes` inside a try/except so an ImportError is caught
    and mapped to a failed phase status (safe_node_wrapper alone can't catch
    import failures since they happen before the call).
    """
    def wrapper(state: AgentState) -> AgentState:
        try:
            from agent import nodes
            node_func = getattr(nodes, func_name)
        except (ImportError, AttributeError) as e:
            return {
                "phase_status": {
                    **state.get("phase_status", {}),
                    phase_name: PhaseStatus(
                        status="failed",
                        error=f"Node import failed: {e}",
                    ),
                }
            }
        return safe_node_wrapper(node_func, state, phase_name)
    return wrapper


research_node_wrapper = _make_node_wrapper("research", "research_node")
synthesis_node_wrapper = _make_node_wrapper("synthesis", "synthesis_node")
calculate_node_wrapper = _make_node_wrapper("calculate", "calculate_node")
design_node_wrapper = _make_node_wrapper("design", "design_node")


def optimization_approval_node(state: AgentState) -> AgentState:
    """No-op approval gate. Pauses before design/optimization when HITL enabled.

    The graph interrupts before this node. The user resumes via
    Command(update={"approval": {"proceed": bool}}) in run_pipeline.py.
    The approval_router then decides whether to proceed to design or route to END.
    """
    return state


def approval_router(state: AgentState) -> str:
    """Route from approval gate: proceed to design, or skip to END."""
    approval = state.get("approval", {})
    if approval.get("proceed", True):
        return "design"
    return END


def build_graph(hitl: bool = True, store=None) -> StateGraph:
    """Build and compile the LangGraph pipeline.

    Args:
        hitl: If True, enables human-in-the-loop interrupt before the design
              phase to ask for user approval before running optimization.
              Set to False for fully automatic runs (no pause).
        store: Optional MemoryStore for cross-session persistence.
               When provided, the design node saves/loads optimization
               results to/from the store automatically.
    """
    builder = StateGraph(AgentState)

    # Add all phase nodes
    builder.add_node("research", research_node_wrapper)
    builder.add_node("synthesis", synthesis_node_wrapper)
    builder.add_node("calculate", calculate_node_wrapper)
    builder.add_node("optimization_approval", optimization_approval_node)
    builder.add_node("design", design_node_wrapper)

    # Per-node conditional edges — only valid transitions are mapped.
    # This enforces linear pipeline order.
    # optimization_approval uses its own router (phase_router handles the rest)
    builder.add_conditional_edges(START, phase_router, {"research": "research"})
    builder.add_conditional_edges("research", phase_router, {"research": "research", "synthesis": "synthesis", END: END})
    builder.add_conditional_edges("synthesis", phase_router, {"synthesis": "synthesis", "calculate": "calculate", END: END})
    builder.add_conditional_edges("calculate", phase_router, {"calculate": "calculate", "optimization_approval": "optimization_approval", END: END})
    builder.add_conditional_edges("optimization_approval", approval_router, {"design": "design", END: END})
    builder.add_conditional_edges("design", phase_router, {"design": "design", END: END})

    # Compile with checkpointer and optional store
    checkpointer = MemorySaver()
    compile_kwargs = {"checkpointer": checkpointer}
    if hitl:
        compile_kwargs["interrupt_before"] = ["optimization_approval"]
    if store:
        compile_kwargs["store"] = store
    return builder.compile(**compile_kwargs)


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
