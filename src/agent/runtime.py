"""Agent runtime — orchestrator loop using OpenAI Agents SDK + Opencode.

Provides:
- ``create_orchestrator()`` — builds the top-level agent with subagent handoffs.
- ``run_request()`` — single user request → classification → delegation → synthesis.
- ``InteractiveSession`` — REPL wrapper with conversation history.
"""

from __future__ import annotations

import os
import sys
from typing import Any

from openai import OpenAI
from agents import Agent, Runner, handoff, set_default_openai_client

from src.agent.build_agent import build_coding_subagent, build_wiki_manager
from src.agent.orchestration_helpers import classify_request
from src.agent.prompts import ORCHESTRATOR_SYSTEM
from src.artifacts import CodeReport, ExperimentReport, ResearchReport, WikiUpdatePlan
from src.config import settings

# ── Wire Opencode as the OpenAI provider ──────────────────────────────

_llm_client: OpenAI | None = None


def _get_client() -> OpenAI:
    global _llm_client
    if _llm_client is not None:
        return _llm_client
    api_key = settings.LLM_API_KEY or os.getenv("OPENCODE_API_KEY")
    if not api_key:
        print(
            "  ⚠️  OPENCODE_API_KEY not set.  Set in .env or environment.",
            file=sys.stderr,
        )
        api_key = "sk-placeholder"
    _llm_client = OpenAI(
        base_url=settings.LLM_BASE_URL,
        api_key=api_key,
    )
    set_default_openai_client(_llm_client)
    return _llm_client


# ── Subagent tools ────────────────────────────────────────────────────


async def _run_coding(request: str) -> CodeReport:
    """Delegate to the Repo Coding Subagent."""
    from src.agent.subagents import REPO_CODING_AGENT as cfg

    agent = Agent(
        name=cfg.name,
        instructions=cfg.instructions,
        model=cfg.model or settings.MODEL_DEFAULT,
        output_type=CodeReport,
    )
    result = await Runner.run(agent, request)
    return result.final_output


async def _run_wiki(request: str) -> str:
    """Delegate to the Wiki Manager."""
    from src.agent.subagents import WIKI_MANAGER_AGENT as cfg

    agent = Agent(
        name=cfg.name,
        instructions=cfg.instructions,
        model=cfg.model or settings.MODEL_DEFAULT,
    )
    result = await Runner.run(agent, request)
    return result.final_output


async def _run_research(request: str) -> ResearchReport:
    """Delegate to the Research Subgraph (Phase 2 — LangGraph)."""
    try:
        from src.research.graph import run_research

        report = await run_research(request)
        return report
    except ImportError:
        return ResearchReport(
            question=request,
            summary="Research subgraph not available yet. Install langgraph and configure research nodes.",
            confidence="low",
        )


async def _run_experiment(request: str) -> ExperimentReport:
    """Delegate to the Experiment Runner."""
    from src.agent.subagents import EXPERIMENT_RUNNER_AGENT as cfg

    agent = Agent(
        name=cfg.name,
        instructions=cfg.instructions,
        model=cfg.model or settings.MODEL_DEFAULT,
        output_type=ExperimentReport,
    )
    result = await Runner.run(agent, request)
    return result.final_output


# ── Orchestrator dispatch ─────────────────────────────────────────────


async def run_request(request: str, model: str | None = None) -> dict[str, Any]:
    """Process a single user request through the orchestrator.

    Returns a dict with keys: request, category, plan, results, synthesis.
    """
    _get_client()
    model = model or settings.MODEL_DEFAULT
    category = classify_request(request)

    result: dict[str, Any] = {
        "request": request,
        "category": category,
        "plan": [],
        "delegations": {},
        "synthesis": "",
    }

    # ── Build plan ────────────────────────────────────────────────────
    if category == "repo_coding":
        result["plan"] = [f"RepoCodingAgent: {request}"]
        result["delegations"]["RepoCodingAgent"] = await _run_coding(request)

    elif category == "wiki_maintenance":
        result["plan"] = [f"WikiManager: {request}"]
        result["delegations"]["WikiManager"] = await _run_wiki(request)

    elif category == "research":
        result["plan"] = [f"ResearchSubgraph: {request}"]
        result["delegations"]["ResearchSubgraph"] = await _run_research(request)

    elif category == "experiment":
        result["plan"] = [f"ExperimentRunner: {request}"]
        result["delegations"]["ExperimentRunner"] = await _run_experiment(request)

    elif category == "mixed":
        # Mixed: use the orchestrator agent to plan and route.
        parts = _decompose_mixed(request)
        result["plan"] = [f"Step {i+1}: {p}" for i, p in enumerate(parts)]
        for step in parts:
            sub_cat = classify_request(step)
            if sub_cat == "repo_coding":
                result["delegations"][f"coding:{step[:40]}"] = await _run_coding(step)
            elif sub_cat == "wiki_maintenance":
                result["delegations"][f"wiki:{step[:40]}"] = await _run_wiki(step)
            elif sub_cat == "research":
                result["delegations"][f"research:{step[:40]}"] = await _run_research(step)
            elif sub_cat == "experiment":
                result["delegations"][f"experiment:{step[:40]}"] = await _run_experiment(step)

    else:
        # Simple question — route to the orchestrator LLM directly.
        agent = Agent(
            name="motor-deepagent",
            instructions=ORCHESTRATOR_SYSTEM,
            model=model,
        )
        response = await Runner.run(agent, request)
        result["synthesis"] = response.final_output

    # ── Synthesize final response ─────────────────────────────────────
    if not result["synthesis"]:
        result["synthesis"] = _synthesize(result)

    return result


def _decompose_mixed(request: str) -> list[str]:
    """Split a mixed request into sub-tasks."""
    lines = request.strip().split("\n")
    # If the user gave a numbered or bullet list, treat each as a step.
    steps = []
    for line in lines:
        stripped = line.strip().lstrip("-*1234567890. ")
        if stripped:
            steps.append(stripped)
    return steps if len(steps) > 1 else [request]


def _synthesize(result: dict[str, Any]) -> str:
    """Build a human-readable synthesis from delegation results."""
    parts = []
    for subsystem, output in result.get("delegations", {}).items():
        if isinstance(output, CodeReport):
            parts.append(
                f"Code changes: {output.files_changed} ({output.result})"
            )
        elif isinstance(output, ResearchReport):
            parts.append(f"Research: {output.summary[:200]}")
        elif isinstance(output, ExperimentReport):
            parts.append(f"Experiment: {output.experiment_id} ({output.result})")
        else:
            parts.append(f"{subsystem}: completed")

    if not parts:
        return f"Request classified as '{result['category']}'. No subsystems invoked."

    return "\n".join(parts)


# ── Interactive session ───────────────────────────────────────────────


class InteractiveSession:
    """REPL session with conversation tracking."""

    def __init__(self, model: str | None = None) -> None:
        self.model = model or settings.MODEL_DEFAULT
        self.history: list[dict[str, Any]] = []

    async def process(self, request: str) -> dict[str, Any]:
        result = await run_request(request, model=self.model)
        self.history.append(result)
        return result

    def summary(self) -> str:
        if not self.history:
            return "No requests processed."
        cats = ", ".join(set(h["category"] for h in self.history))
        return f"{len(self.history)} requests [{cats}]"
