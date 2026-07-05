"""WikiUpdatePlan artifact — structured plan for Wiki Manager updates."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class NewSection(BaseModel):
    """A new section to be added to a wiki page."""

    page: str = Field(description="Target page path (relative to wiki root)")
    heading: str = Field(description="Section heading")
    content_summary: str = Field(
        description="Short description of the content to add",
    )


class SectionEdit(BaseModel):
    """An edit to an existing wiki section."""

    page: str = Field(description="Target page path")
    heading: str = Field(description="Section heading to modify")
    change_summary: str = Field(description="What should be changed and why")


class WikiUpdatePlan(BaseModel):
    """Structured plan produced by the orchestrator for the Wiki Manager.

    The Wiki Manager should review this plan, apply the changes, and
    report back what was actually done.
    """

    target_pages: list[str] = Field(
        description="Full list of pages that will be read or modified",
    )
    new_sections: list[NewSection] = Field(
        default_factory=list,
        description="New sections or pages to create",
    )
    edits_to_existing_sections: list[SectionEdit] = Field(
        default_factory=list,
        description="Modifications to existing content",
    )
    source_links: list[str] = Field(
        default_factory=list,
        description="URLs or file paths that inform this update",
    )
    confidence: str = Field(
        default="medium",
        description="How confident we are in the new knowledge: high | medium | low",
    )
    open_questions: list[str] = Field(
        default_factory=list,
        description="Unresolved questions that should be recorded alongside the update",
    )
    created_at: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="ISO-8601 timestamp",
    )
