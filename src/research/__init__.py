"""Research subgraph — LangGraph Functional API research pipeline."""
from src.research.graph import run_research, run_research_stream
from src.research.state import ResearchState, make_initial_state
from src.research.schemas import (
    NormalizedQuestion,
    SourceSelection,
    SelectedSource,
    Extraction,
    Synthesis,
    ReportOutput,
    NORMALIZE_SCHEMA,
    SELECTION_SCHEMA,
    EXTRACTION_SCHEMA,
    SYNTHESIS_SCHEMA,
    REPORT_SCHEMA,
    SCHEMA_REGISTRY,
)

__all__ = [
    "run_research",
    "run_research_stream",
    "ResearchState",
    "make_initial_state",
    # Pydantic models
    "NormalizedQuestion",
    "SourceSelection",
    "SelectedSource",
    "Extraction",
    "Synthesis",
    "ReportOutput",
    # JSON Schema dicts
    "NORMALIZE_SCHEMA",
    "SELECTION_SCHEMA",
    "EXTRACTION_SCHEMA",
    "SYNTHESIS_SCHEMA",
    "REPORT_SCHEMA",
    "SCHEMA_REGISTRY",
]
