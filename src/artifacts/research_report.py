"""ResearchReport artifact — structured output from the Research Subgraph."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Source(BaseModel):
    """A single source consulted during research."""

    title: str = Field(description="Source title")
    type_: str = Field(
        alias="type",
        description="Source type: paper | web | wiki | repo-doc | note",
    )
    path_or_url: str = Field(description="Path or URL to the source")

    model_config = ConfigDict(populate_by_name=True)


class ResearchReport(BaseModel):
    """Structured output from the LangGraph Research Subgraph.

    This is the primary artifact exchanged between the Research subsystem
    and the orchestrator.  It is *not* written directly to the wiki —
    the Wiki Manager decides what becomes durable knowledge.
    """

    question: str = Field(description="The original research question")
    sources: list[Source] = Field(
        default_factory=list,
        description="Sources consulted during research",
    )
    summary: str = Field(description="High-level synthesis of findings")
    extracted_claims: list[str] = Field(
        default_factory=list,
        description="Specific claims extracted from sources",
    )
    equations_or_constraints: list[str] = Field(
        default_factory=list,
        description="Relevant equations, formulas, or design constraints",
    )
    conflicts_or_uncertainties: list[str] = Field(
        default_factory=list,
        description="Disagreements between sources or unresolved questions",
    )
    recommended_wiki_updates: list[str] = Field(
        default_factory=list,
        description="Suggested wiki pages or sections to update",
    )
    recommended_code_targets: list[str] = Field(
        default_factory=list,
        description="Suggested code files or modules to modify",
    )
    confidence: str = Field(
        default="medium",
        description="Overall confidence: high | medium | low",
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary metadata (research graph version, duration, etc.)",
    )
    created_at: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="ISO-8601 timestamp of report creation",
    )
