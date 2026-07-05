"""ExperimentReport artifact — structured output from the Execution layer."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ExperimentReport(BaseModel):
    """Structured output after running an experiment or script.

    Carries inputs, outputs, key metrics, and suggestions for wiki logging.
    """

    experiment_id: str = Field(description="Unique identifier for this run")
    workflow_name: str = Field(description="Name of the workflow or script run")
    inputs: dict[str, Any] = Field(
        default_factory=lambda: {
            "parameters": {},
            "config_files": [],
            "notes": "",
        },
        description="Input parameters, config files, and notes",
    )
    outputs: dict[str, Any] = Field(
        default_factory=lambda: {
            "files": [],
            "logs": [],
        },
        description="Output files and log paths",
    )
    key_metrics: dict[str, float | None] = Field(
        default_factory=lambda: {
            "torque": None,
            "efficiency": None,
            "power_factor": None,
        },
        description="Extracted numeric metrics from the run",
    )
    result: str = Field(
        default="success",
        description="Outcome: success | partial | failed",
    )
    notes_for_wiki: list[str] = Field(
        default_factory=list,
        description="Key findings that should be recorded in the wiki",
    )
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Arbitrary metadata",
    )
    created_at: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="ISO-8601 timestamp",
    )
