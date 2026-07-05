"""Experiment logger — write structured experiment records to the wiki."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from src.artifacts import ExperimentReport
from src.config import settings


def log_experiment_to_wiki(report: ExperimentReport, wiki_root: Path | None = None) -> Path:
    """Write an ExperimentReport as a wiki page under motorcad/experiments/.

    Returns the path to the created page.
    """
    root = wiki_root or settings.WIKI_ROOT
    exp_dir = root / "motorcad" / "experiments"
    exp_dir.mkdir(parents=True, exist_ok=True)

    slug = report.experiment_id.replace(" ", "_").lower()
    page_path = exp_dir / f"{slug}.md"

    lines = [
        "---",
        f"title: Experiment {report.experiment_id}",
        f"created: {report.created_at}",
        "---",
        "",
        f"# Experiment: {report.experiment_id}",
        "",
        f"**Workflow:** {report.workflow_name}",
        f"**Result:** {report.result}",
        "",
        "## Inputs",
    ]

    inputs = report.inputs or {}
    if inputs.get("parameters"):
        lines.append("")
        lines.append("| Parameter | Value |")
        lines.append("|-----------|-------|")
        for k, v in inputs["parameters"].items():
            lines.append(f"| {k} | {v} |")

    if inputs.get("config_files"):
        lines.append("\n**Config files:**")
        for f in inputs["config_files"]:
            lines.append(f"- {f}")

    lines.extend([
        "",
        "## Outputs",
    ])

    outputs = report.outputs or {}
    if outputs.get("files"):
        lines.append("")
        for f in outputs["files"]:
            lines.append(f"- {f}")

    metrics = report.key_metrics or {}
    if any(v is not None for v in metrics.values()):
        lines.extend([
            "",
            "## Key Metrics",
            "",
            "| Metric | Value |",
            "|--------|-------|",
        ])
        for k, v in metrics.items():
            if v is not None:
                lines.append(f"| {k} | {v} |")

    if report.notes_for_wiki:
        lines.extend([
            "",
            "## Notes",
            "",
        ])
        for note in report.notes_for_wiki:
            lines.append(f"- {note}")

    lines.append("")
    page_path.write_text("\n".join(lines), encoding="utf-8")
    return page_path
