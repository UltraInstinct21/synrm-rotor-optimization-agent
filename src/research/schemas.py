"""Shared Pydantic models and JSON schemas for structured LLM output.

All nodes that call the LLM with ``response_format="json_schema"`` share
their schema definitions here, so they're visible and testable in one place.

Each logical output has a Pydantic model (for validation) and a matching
``json_schema`` dict (for the wire call).  Use the model when you want
Pydantic-validated data; use the dict when you need the raw JSON Schema
object for the API.
"""

from __future__ import annotations

from pydantic import BaseModel


# ── Normalize question ────────────────────────────────────────────────


class NormalizedQuestion(BaseModel):
    """Output of the ``normalize_question`` node."""

    normalized_question: str
    domain_terms: list[str]


NORMALIZE_SCHEMA: dict = NormalizedQuestion.model_json_schema()


# ── Source selection ──────────────────────────────────────────────────


class SelectedSource(BaseModel):
    """A single source chosen for deep reading."""

    title: str
    type: str
    path_or_url: str
    relevance: str | None = None


class SourceSelection(BaseModel):
    """Output of the ``source_selection`` node."""

    selected_sources: list[SelectedSource]


SELECTION_SCHEMA: dict = SourceSelection.model_json_schema()


# ── Read / extract ────────────────────────────────────────────────────


class Extraction(BaseModel):
    """Output of the ``read_extract`` node."""

    extracted_claims: list[str]
    extracted_equations: list[str]
    extracted_notes: list[str]


EXTRACTION_SCHEMA: dict = Extraction.model_json_schema()


# ── Synthesize claims ─────────────────────────────────────────────────


class Synthesis(BaseModel):
    """Output of the ``synthesize_claims`` node."""

    synthesized_claims: list[str]
    conflicts: list[str]


SYNTHESIS_SCHEMA: dict = Synthesis.model_json_schema()


# ── Build report ──────────────────────────────────────────────────────


class ReportOutput(BaseModel):
    """Output of the ``build_report`` node (the LLM-produced portion)."""

    summary: str
    confidence: str  # "high" | "medium" | "low"
    recommended_wiki_updates: list[str]
    recommended_code_targets: list[str]


REPORT_SCHEMA: dict = ReportOutput.model_json_schema()


# ── Map: schema name → (model, schema-dict) ───────────────────────────

SCHEMA_REGISTRY: dict[str, tuple[type[BaseModel], dict]] = {
    "normalize": (NormalizedQuestion, NORMALIZE_SCHEMA),
    "selection": (SourceSelection, SELECTION_SCHEMA),
    "extraction": (Extraction, EXTRACTION_SCHEMA),
    "synthesis": (Synthesis, SYNTHESIS_SCHEMA),
    "report": (ReportOutput, REPORT_SCHEMA),
}
