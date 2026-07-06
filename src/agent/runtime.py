"""Agent runtime — orchestrator loop using LangChain ChatOpenAI + Opencode.

Provides:
- ``run_request()`` — single user request → classification → delegation → synthesis.
- ``run_request_streamed()`` — streaming variant.
- ``InteractiveSession`` — REPL wrapper with history.
"""

from __future__ import annotations

import sys
from typing import Any, AsyncIterator

from langchain_core.messages import HumanMessage, SystemMessage

from src.agent.orchestration_helpers import classify_request
from src.agent.prompts import ORCHESTRATOR_SYSTEM
from src.artifacts import CodeReport, ExperimentReport, ResearchReport
from src.config import settings


# ── LLM helper ─────────────────────────────────────────────────────────


def _get_llm(model: str | None = None):
    """Return a ChatOpenAI instance via the settings factory."""
    return settings.get_llm(model)


# ── Subagent runners ───────────────────────────────────────────────────


async def _run_subagent(
    name: str,
    system_prompt: str,
    request: str,
    model: str | None = None,
) -> str:
    """Run a subsystem agent via ChatOpenAI (no tools)."""
    llm = _get_llm(model)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=request),
    ]
    response = await llm.ainvoke(messages)
    return response.content


async def _run_research(request: str) -> ResearchReport:
    """Delegate to the Research Subgraph (LangGraph)."""
    try:
        from src.research.graph import run_research

        return await run_research(request)
    except Exception as e:
        return ResearchReport(
            question=request,
            summary=f"Research subgraph error: {e}",
            confidence="low",
        )


# ── Streaming variant ─────────────────────────────────────────────────


async def run_request_streamed(
    request: str,
    model: str | None = None,
) -> AsyncIterator[dict[str, Any]]:
    """Yield streaming events for the orchestrator pipeline.

    Yields dicts with ``type`` (``"token"`` | ``"info"`` | ``"category"`` | ``"synthesis"``).
    """
    model = model or settings.MODEL_DEFAULT
    category = classify_request(request)
    yield {"type": "category", "data": category}

    if category == "repo_coding":
        yield {"type": "info", "label": "plan", "data": f"RepoCodingAgent: {request}"}
        output = await _run_subagent(
            "RepoCodingAgent",
            "You are a code assistant. Analyze and describe code changes.",
            request, model,
        )
        yield {"type": "info", "label": "RepoCodingAgent", "data": output[:200]}
        yield {"type": "synthesis", "data": output}

    elif category == "wiki_maintenance":
        yield {"type": "info", "label": "plan", "data": f"WikiManager: {request}"}
        output = await _run_subagent(
            "WikiManager",
            "You are a wiki manager. Maintain and update documentation.",
            request, model,
        )
        yield {"type": "info", "label": "WikiManager", "data": output[:200]}
        yield {"type": "synthesis", "data": output}

    elif category == "research":
        yield {"type": "info", "label": "plan", "data": f"ResearchSubgraph: {request}"}
        report = await _run_research(request)
        yield {"type": "info", "label": "ResearchSubgraph", "data": report.summary[:200]}
        yield {"type": "synthesis", "data": report.summary}

    elif category == "experiment":
        yield {"type": "info", "label": "plan", "data": f"ExperimentRunner: {request}"}
        output = await _run_subagent(
            "ExperimentRunner",
            "You are an experiment runner. Execute and analyze experiments.",
            request, model,
        )
        yield {"type": "info", "label": "ExperimentRunner", "data": output[:200]}
        yield {"type": "synthesis", "data": output}

    elif category == "mixed":
        parts = _decompose_mixed(request)
        for i, p in enumerate(parts):
            yield {"type": "info", "label": "plan", "data": f"Step {i+1}: {p}"}
            sub_cat = classify_request(p)
            if sub_cat == "repo_coding":
                output = await _run_subagent("RepoCodingAgent", "You are a code assistant.", p, model)
                yield {"type": "info", "label": f"step-{i+1}", "data": output[:200]}
            elif sub_cat == "research":
                report = await _run_research(p)
                yield {"type": "info", "label": f"step-{i+1}", "data": report.summary[:200]}

    else:
        # Question — stream from LLM directly.
        llm = _get_llm(model)
        messages = [
            SystemMessage(content=ORCHESTRATOR_SYSTEM),
            HumanMessage(content=request),
        ]
        async for chunk in llm.astream(messages):
            if chunk.content:
                yield {"type": "token", "data": chunk.content}

        # Final synthesis
        response = await llm.ainvoke(messages)
        yield {"type": "synthesis", "data": response.content}


def _format_output_summary(name: str, output: Any) -> str:
    """Return a one-line summary of a subagent's output."""
    if isinstance(output, CodeReport):
        return f"{output.files_changed or 0} files changed, result: {output.result}"
    elif isinstance(output, ResearchReport):
        return f"confidence={output.confidence}, {output.summary[:120]}"
    elif isinstance(output, ExperimentReport):
        return f"id={output.experiment_id}, result={output.result}"
    return str(output)[:200] if output else "completed"


# ── Decompose ──────────────────────────────────────────────────────────


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
            parts.append(f"Code changes: {output.files_changed} ({output.result})")
        elif isinstance(output, ResearchReport):
            parts.append(f"Research: {output.summary[:200]}")
        elif isinstance(output, ExperimentReport):
            parts.append(f"Experiment: {output.experiment_id} ({output.result})")
        else:
            parts.append(f"{subsystem}: {str(output)[:200]}")

    if not parts:
        return f"Request classified as '{result['category']}'. No subsystems invoked."

    return "\n".join(parts)


# ── Interactive session ────────────────────────────────────────────────


class InteractiveSession:
    """REPL session with history tracking."""

    def __init__(self, model: str | None = None) -> None:
        self.model = model or settings.MODEL_DEFAULT
        self.history: list[dict[str, Any]] = []

    async def process(self, request: str) -> dict[str, Any]:
        """Process a request, tracking it in history."""
        category = classify_request(request)
        result: dict[str, Any] = {
            "request": request,
            "category": category,
            "synthesis": "",
        }

        if category == "repo_coding":
            result["synthesis"] = await _run_subagent(
                "RepoCodingAgent", "You are a code assistant.", request, self.model
            )
        elif category == "wiki_maintenance":
            result["synthesis"] = await _run_subagent(
                "WikiManager", "You are a wiki manager.", request, self.model
            )
        elif category == "research":
            report = await _run_research(request)
            result["synthesis"] = report.summary
        elif category == "experiment":
            result["synthesis"] = await _run_subagent(
                "ExperimentRunner", "You are an experiment runner.", request, self.model
            )
        else:
            llm = _get_llm(self.model)
            response = await llm.ainvoke([
                SystemMessage(content=ORCHESTRATOR_SYSTEM),
                HumanMessage(content=request),
            ])
            result["synthesis"] = response.content

        self.history.append(result)
        return result

    def summary(self) -> str:
        if not self.history:
            return "No requests processed."
        cats = ", ".join(set(h["category"] for h in self.history))
        return f"{len(self.history)} requests [{cats}]"


# ── LangGraph integration ──────────────────────────────────────────────


async def run_request_graph(
    request: str,
    thread_id: str = "default",
) -> dict[str, Any]:
    """Process a request through the LangGraph state machine."""
    from src.agent.graph import motor_graph_local as motor_graph

    config = {"configurable": {"thread_id": thread_id}}
    result = await motor_graph.ainvoke(
        {"messages": [{"role": "user", "content": request}]},
        config=config,
    )

    return {
        "request": request,
        "category": result.get("category", ""),
        "delegations": result.get("delegations", {}),
        "synthesis": _extract_synthesis(result),
        "messages": result.get("messages", []),
    }


def _extract_synthesis(result: dict) -> str:
    """Extract synthesis text from graph result."""
    messages = result.get("messages", [])
    for msg in reversed(messages):
        if isinstance(msg, dict) and msg.get("role") == "assistant":
            return msg.get("content", "")
        if hasattr(msg, "content") and hasattr(msg, "type"):
            if msg.type == "ai":
                return msg.content
    return ""


async def run_request_graph_streamed(
    request: str,
    thread_id: str = "default",
) -> AsyncIterator[dict[str, Any]]:
    """Like :func:`run_request_graph` but yields streaming events."""
    from src.agent.graph import motor_graph_local as motor_graph

    config = {"configurable": {"thread_id": thread_id}}

    async for event in motor_graph.astream(
        {"messages": [{"role": "user", "content": request}]},
        config=config,
        stream_mode="updates",
    ):
        for node_name, update in event.items():
            if node_name == "classify" and "category" in update:
                yield {"type": "category", "data": update["category"]}

            elif node_name.startswith("execute_") and "delegations" in update:
                delegations = update["delegations"]
                for agent_name, output in delegations.items():
                    summary = _format_output_summary(agent_name, output)
                    yield {"type": "info", "label": agent_name, "data": summary}

            elif node_name == "synthesize" and "messages" in update:
                for msg in update["messages"]:
                    content = ""
                    if isinstance(msg, dict):
                        content = msg.get("content", "")
                    elif hasattr(msg, "content"):
                        content = msg.content
                    if content:
                        yield {"type": "synthesis", "data": content}
