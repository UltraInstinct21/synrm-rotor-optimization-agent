"""Data contracts between components.

Every subsystem exchanges structured artifacts rather than free-form text.
"""

from src.artifacts.research_report import ResearchReport, Source
from src.artifacts.code_report import CodeReport
from src.artifacts.experiment_report import ExperimentReport
from src.artifacts.wiki_update_plan import WikiUpdatePlan, NewSection, SectionEdit

__all__ = [
    "ResearchReport",
    "Source",
    "CodeReport",
    "ExperimentReport",
    "WikiUpdatePlan",
    "NewSection",
    "SectionEdit",
]
