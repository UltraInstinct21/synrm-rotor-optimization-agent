"""Result summarizer — extract human-readable summaries from experiment outputs."""

from __future__ import annotations

import re
from pathlib import Path

from src.artifacts import ExperimentReport


def summarize_log(log_path: str | Path) -> dict[str, float | str | None]:
    """Parse a structured log file for key metrics.

    Looks for patterns like:
      EXIT_CODE: 0
      torque = 143.2
      efficiency = 96.5
      power_factor = 0.78

    Returns a dict of extracted values.
    """
    path = Path(log_path)
    if not path.exists():
        return {"error": f"File not found: {path}"}

    text = path.read_text(encoding="utf-8", errors="ignore")
    metrics: dict[str, float | str | None] = {}

    # Extract exit code.
    exit_match = re.search(r"EXIT_CODE:\s*(\d+)", text)
    metrics["exit_code"] = int(exit_match.group(1)) if exit_match else None

    # Extract numeric patterns (name = number).
    num_pattern = re.compile(
        r"(torque|efficiency|power_factor|power\s*factor|saliency|"
        r"ld|lq|iron_loss|copper_loss|speed|output_power)\s*[=:]\s*([\d.]+)",
        re.IGNORECASE,
    )
    for match in num_pattern.finditer(text):
        key = match.group(1).lower().replace(" ", "_")
        metrics[key] = float(match.group(2))

    # Extract CSV-like rows if present.
    csv_lines = [l for l in text.split("\n") if re.search(r"[\d]+\.[\d]+", l) and "," in l]
    if csv_lines and "torque" not in metrics:
        # Try to parse headers from a CSV line.
        for line in csv_lines:
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 2:
                try:
                    metrics[f"col_{parts[0]}"] = float(parts[1])
                except ValueError:
                    pass

    return metrics


def report_to_summary(report: ExperimentReport) -> str:
    """Produce a one-paragraph summary of an ExperimentReport."""
    parts = [
        f"Experiment '{report.experiment_id}' ({report.workflow_name}) "
        f"completed with result '{report.result}'."
    ]

    metrics = report.key_metrics or {}
    metric_strs = []
    if metrics.get("torque") is not None:
        metric_strs.append(f"torque={metrics['torque']} Nm")
    if metrics.get("efficiency") is not None:
        metric_strs.append(f"efficiency={metrics['efficiency']}%")
    if metrics.get("power_factor") is not None:
        metric_strs.append(f"PF={metrics['power_factor']}")

    if metric_strs:
        parts.append(f"Key metrics: {', '.join(metric_strs)}")

    if report.notes_for_wiki:
        parts.append(f"Notes: {'; '.join(report.notes_for_wiki)}")

    return " ".join(parts)
