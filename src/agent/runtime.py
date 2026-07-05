"""Agent runtime — orchestrator loop using OpenAI Agents SDK + Opencode.

Provides:
- ``create_orchestrator()`` — builds the top-level agent with subagent handoffs.
- ``run_request()`` — single user request → classification → delegation → synthesis.
- ``InteractiveSession`` — REPL wrapper with optional SQLite conversation memory.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

from openai import OpenAI, AsyncOpenAI
from agents import (
    Agent,
    MultiProvider,
    Runner,
    handoff,
    RunConfig,
    set_default_openai_client,
)
from agents.memory import SQLiteSession, Session

from src.agent.build_agent import build_coding_subagent, build_wiki_manager
from src.agent.orchestration_helpers import classify_request
from src.agent.prompts import ORCHESTRATOR_SYSTEM
from src.artifacts import CodeReport, ExperimentReport, ResearchReport, WikiUpdatePlan
from src.config import settings

# ── Wire Opencode as the OpenAI provider ──────────────────────────────

_llm_client: OpenAI | None = None
_multi_provider: MultiProvider | None = None
SESSION_DB_PATH: Path = settings.PROJECT_ROOT / ".session" / "conversations.db"


def _get_client() -> OpenAI:
    """Return (and cache) the Opencode-compatible OpenAI client."""
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


def get_model_provider() -> MultiProvider:
    """Return a ``MultiProvider`` that routes all model calls through Opencode.

    This lets us use model-parameter prefixes (``deepseek-v4-flash-free`` as a
    bare name resolves via the default ``OpenAIProvider`` whose base URL points
    at Opencode).
    """
    global _multi_provider
    if _multi_provider is not None:
        return _multi_provider
    client = _get_client()
    _multi_provider = MultiProvider(
        openai_client=AsyncOpenAI(
            base_url=settings.LLM_BASE_URL,
            api_key=(settings.LLM_API_KEY or os.getenv("OPENCODE_API_KEY") or "sk-placeholder"),
        ),
        openai_use_responses=False,  # use ChatCompletions, not Responses
    )
    return _multi_provider


# ── SQLite conversation session ──────────────────────────────────────


def get_session(session_id: str = "default") -> Session | None:
    """Return a SQLite-backed session for conversation persistence.

    Returns ``None`` if ``aiosqlite`` is not installed (graceful fallback).
    """
    try:
        SESSION_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
        return SQLiteSession(
            session_id=session_id,
            db_path=str(SESSION_DB_PATH),
        )
    except Exception:
        return None


# ── Subagent tools ────────────────────────────────────────────────────


async def _run_coding(request: str, model: str | None = None) -> CodeReport:
    """Delegate to the Repo Coding Subagent."""
    from src.agent.subagents import REPO_CODING_AGENT as cfg

    agent = Agent(
        name=cfg.name,
        instructions=cfg.instructions,
        model=model or cfg.model or settings.MODEL_DEFAULT,
        output_type=CodeReport,
    )
    result = await Runner.run(agent, request)
    return result.final_output


async def _run_wiki(request: str, model: str | None = None) -> str:
    """Delegate to the Wiki Manager."""
    from src.agent.subagents import WIKI_MANAGER_AGENT as cfg

    agent = Agent(
        name=cfg.name,
        instructions=cfg.instructions,
        model=model or cfg.model or settings.MODEL_DEFAULT,
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


async def _run_experiment(request: str, model: str | None = None) -> ExperimentReport:
    """Delegate to the Experiment Runner."""
    from src.agent.subagents import EXPERIMENT_RUNNER_AGENT as cfg

    agent = Agent(
        name=cfg.name,
        instructions=cfg.instructions,
        model=model or cfg.model or settings.MODEL_DEFAULT,
        output_type=ExperimentReport,
    )
    result = await Runner.run(agent, request)
    return result.final_output


# ── Orchestrator dispatch ─────────────────────────────────────────────


async def run_request(
    request: str,
    model: str | None = None,
    session: Session | None = None,
) -> dict[str, Any]:
    """Process a single user request through the orchestrator.

    Parameters
    ----------
    request : str
        The user's natural-language request.
    model : str, optional
        Model override.
    session : Session, optional
        Optional SQLite (or other) session for conversation memory.

    Returns
    -------
    dict
        Keys: ``request``, ``category``, ``plan``, ``delegations``, ``synthesis``.
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

    # Build RunConfig with model provider and optional session.
    run_config = RunConfig(
        model_provider=get_model_provider(),
        session=session,
        workflow_name="motor-deepagent",
        group_id="motor-deepagent-session",
    )

    # ── Build plan ────────────────────────────────────────────────────
    if category == "repo_coding":
        result["plan"] = [f"RepoCodingAgent: {request}"]
        result["delegations"]["RepoCodingAgent"] = await _run_coding(request, model)

    elif category == "wiki_maintenance":
        result["plan"] = [f"WikiManager: {request}"]
        result["delegations"]["WikiManager"] = await _run_wiki(request, model)

    elif category == "research":
        result["plan"] = [f"ResearchSubgraph: {request}"]
        result["delegations"]["ResearchSubgraph"] = await _run_research(request)

    elif category == "experiment":
        result["plan"] = [f"ExperimentRunner: {request}"]
        result["delegations"]["ExperimentRunner"] = await _run_experiment(request, model)

    elif category == "mixed":
        parts = _decompose_mixed(request)
        result["plan"] = [f"Step {i+1}: {p}" for i, p in enumerate(parts)]
        for step in parts:
            sub_cat = classify_request(step)
            if sub_cat == "repo_coding":
                result["delegations"][f"coding:{step[:40]}"] = await _run_coding(step, model)
            elif sub_cat == "wiki_maintenance":
                result["delegations"][f"wiki:{step[:40]}"] = await _run_wiki(step, model)
            elif sub_cat == "research":
                result["delegations"][f"research:{step[:40]}"] = await _run_research(step)
            elif sub_cat == "experiment":
                result["delegations"][f"experiment:{step[:40]}"] = await _run_experiment(step, model)

    else:
        # Simple question — route to the orchestrator LLM directly.
        agent = Agent(
            name="motor-deepagent",
            instructions=ORCHESTRATOR_SYSTEM,
            model=model,
        )
        response = await Runner.run(agent, request, run_config=run_config)
        result["synthesis"] = response.final_output

    # ── Synthesize final response ─────────────────────────────────────
    if not result["synthesis"]:
        result["synthesis"] = _synthesize(result)

    return result


def _decompose_mixed(request: str) -> list[str]:
    """Split a mixed request into sub-tasks."""
    lines = request.strip().split("\n")
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


# ── Interactive session with memory ───────────────────────────────────


class InteractiveSession:
    """REPL session with optional SQLite conversation persistence.

    Usage::

        session = InteractiveSession()
        result = await session.process("hello")
        print(session.history)
    """

    def __init__(
        self,
        model: str | None = None,
        use_memory: bool = True,
    ) -> None:
        self.model = model or settings.MODEL_DEFAULT
        self.history: list[dict[str, Any]] = []
        self._session: Session | None = get_session() if use_memory else None

    @property
    def memory(self) -> Session | None:
        """The underlying SQLite session (or ``None`` if disabled)."""
        return self._session

    async def process(self, request: str) -> dict[str, Any]:
        """Process a request, tracking it in history and optional memory."""
        result = await run_request(
            request,
            model=self.model,
            session=self._session,
        )
        self.history.append(result)
        return result

    def summary(self) -> str:
        if not self.history:
            return "No requests processed."
        cats = ", ".join(set(h["category"] for h in self.history))
        return f"{len(self.history)} requests [{cats}]"
