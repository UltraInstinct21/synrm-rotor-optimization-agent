"""Data contracts between components."""

from src.artifacts.research_report import ResearchReport, Source
from src.artifacts.code_report import CodeReport
from src.artifacts.experiment_report import ExperimentReport

__all__ = [
    "ResearchReport",
    "Source",
    "CodeReport",
    "ExperimentReport",
]
