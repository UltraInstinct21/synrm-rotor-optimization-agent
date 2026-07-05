"""CodeReport artifact — structured output from the Repo Coding Subagent."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class CodeReport(BaseModel):
    """Structured output from the Repo Coding Subagent.

    Describes what code was inspected, changed, and what follow-up is needed.
    """

    goal: str = Field(description="The original goal of the code task")
    files_inspected: list[str] = Field(
        default_factory=list,
        description="Files read or searched during the task",
    )
    files_changed: list[str] = Field(
        default_factory=list,
        description="Files that were modified or created",
    )
    diff_summary: str = Field(
        default="",
        description="Human-readable summary of what changed and why",
    )
    tests_run: list[str] = Field(
        default_factory=list,
        description="Tests executed (paths or names)",
    )
    result: str = Field(
        default="success",
        description="Outcome: success | partial | failed",
    )
    follow_up_needed: list[str] = Field(
        default_factory=list,
        description="Actions still needed after this change",
    )
    wiki_update_candidates: list[str] = Field(
        default_factory=list,
        description="Wiki pages that may need updating based on this code change",
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary metadata",
    )
    created_at: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="ISO-8601 timestamp",
    )
