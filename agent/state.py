"""LangGraph state definition for SynRM multi-agent pipeline."""

from typing import Annotated, TypedDict, Optional
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage


class PhaseStatus(TypedDict):
    """Status tracking for each pipeline phase."""
    status: str            # "pending" | "running" | "done" | "failed" | "skipped"
    error: Optional[str]   # error message if failed


class AgentState(TypedDict):
    """Shared state flowing through all pipeline phases."""
    messages: Annotated[list[BaseMessage], add_messages]
    phase: str                              # current phase name
    phase_status: dict[str, PhaseStatus]    # per-phase status

    # Knowledge graph references
    wiki_entities_created: list[str]
    wiki_concepts_created: list[str]
    wiki_synthesis: list[str]

    # Motor specification (from user)
    motor_spec: dict                        # {power, torque, speed, poles, ...}

    # Calculation outputs (populated by Phase 3)
    winding_params: dict                    # {kw, turns, fill, wire_dia, ...}
    barrier_params: dict                    # {L1_Dia, L2_Dia, bridges, webs...}
    derived_params: dict                    # {current_density, slot_fill, ...}

    # .mot file state (populated by Phase 4)
    mot_file_path: str
    mot_sections: dict[str, dict]           # {section_name: {param: value}}
    pymotorcad_vars: list[str]              # discovered variable names

    # Optimization results (populated by Phase 4)
    optimization_results: list[dict]
    best_model_path: str
