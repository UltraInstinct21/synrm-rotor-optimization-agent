"""DeepAgent builder — constructs the orchestrator with subagent handoffs."""

from __future__ import annotations

import os
from pathlib import Path

from src.agent.prompts import ORCHESTRATOR_SYSTEM
from src.agent.subagents import REGISTRY, SubagentConfig
from src.config import settings


def build_orchestrator(
    model: str | None = None,
    additional_tools: list | None = None,
) -> dict:
    """Build the orchestrator agent configuration.

    Returns a dict that can be passed to the DeepAgent SDK's Agent constructor,
    or consumed by the CLI entry point.

    Parameters
    ----------
    model : str, optional
        Model override.  Defaults to ``settings.MODEL_DEFAULT``.
    additional_tools : list, optional
        Extra tools to attach to the orchestrator.

    Returns
    -------
    dict
        Agent configuration with instructions, model, tools, and handoffs.
    """
    model = model or settings.MODEL_DEFAULT

    # Collect subagent configs as handoff targets.
    handoffs = []
    for name, cfg in REGISTRY.items():
        handoffs.append(
            {
                "name": cfg.name,
                "instructions": cfg.instructions,
                "model": cfg.model or model,
            }
        )

    return {
        "name": "motor-deepagent",
        "instructions": ORCHESTRATOR_SYSTEM,
        "model": model,
        "tools": additional_tools or [],
        "handoffs": handoffs,
        "output_guardrails": {
            "enabled": True,
            "rules": [
                "Inspect code before editing — never guess file contents.",
                "Surface uncertainty instead of inventing plausible-sounding answers.",
                "Return structured artifacts for complex results.",
            ],
        },
    }


def build_coding_subagent(
    model: str | None = None,
) -> SubagentConfig:
    """Return the RepoCodingAgent config with optional model override."""
    cfg = REGISTRY["RepoCodingAgent"]
    if model:
        cfg.model = model
    return cfg


def build_wiki_manager(
    model: str | None = None,
    wiki_root: Path | None = None,
) -> SubagentConfig:
    """Return the WikiManager config.

    Parameters
    ----------
    model : str, optional
        Model override.
    wiki_root : Path, optional
        Wiki root path.  Defaults to ``settings.WIKI_ROOT``.
    """
    cfg = REGISTRY["WikiManager"]
    if model:
        cfg.model = model
    wiki_root = wiki_root or settings.WIKI_ROOT
    # Augment instructions with the actual wiki path.
    cfg.instructions += f"\n\nThe wiki lives at: {wiki_root}"
    return cfg


def build_research_subgraph(
    model: str | None = None,
) -> SubagentConfig:
    """Return the ResearchSubgraph config."""
    cfg = REGISTRY["ResearchSubgraph"]
    if model:
        cfg.model = model
    return cfg


def build_experiment_runner(
    model: str | None = None,
) -> SubagentConfig:
    """Return the ExperimentRunner config."""
    cfg = REGISTRY["ExperimentRunner"]
    if model:
        cfg.model = model
    return cfg
