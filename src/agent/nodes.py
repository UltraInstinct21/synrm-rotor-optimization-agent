"""LangGraph node functions for motor-deepagent."""

from __future__ import annotations

from typing import Any, Literal

from src.agent.orchestration_helpers import classify_request
from src.agent.state import MotorState


def classify_node(state: MotorState) -> dict[str, str]:
    """Classify the user request by keyword matching."""
    messages = state.get("messages", [])
    last_msg = messages[-1] if messages else {}
    request = last_msg.get("content", "") if isinstance(last_msg, dict) else ""
    return {"category": classify_request(request)}


def route_node(
    state: MotorState,
) -> Literal["execute_code", "execute_wiki", "execute_research", "execute_experiment", "synthesize"]:
    """Route to the appropriate execution node based on category."""
    category = state.get("category", "question")
    routing = {
        "repo_coding": "execute_code",
        "wiki_maintenance": "execute_wiki",
        "research": "execute_research",
        "experiment": "execute_experiment",
    }
    return routing.get(category, "synthesize")


def execute_code_node(state: MotorState) -> dict[str, Any]:
    """Execute code-related task via RepoCodingAgent."""
    from src.agent.runtime import _run_subagent, _get_client
    from src.agent.subagents import REPO_CODING_AGENT
    from src.artifacts import CodeReport

    _get_client()
    messages = state.get("messages", [])
    request = messages[-1].get("content", "") if messages else ""

    import asyncio
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    output = loop.run_until_complete(
        _run_subagent(REPO_CODING_AGENT, request, output_type=CodeReport)
    )
    delegations = state.get("delegations", {})
    delegations["RepoCodingAgent"] = output
    return {"delegations": delegations}


def execute_wiki_node(state: MotorState) -> dict[str, Any]:
    """Execute wiki task via WikiManager."""
    from src.agent.runtime import _run_subagent, _get_client
    from src.agent.subagents import WIKI_MANAGER_AGENT

    _get_client()
    messages = state.get("messages", [])
    request = messages[-1].get("content", "") if messages else ""

    import asyncio
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    output = loop.run_until_complete(_run_subagent(WIKI_MANAGER_AGENT, request))
    delegations = state.get("delegations", {})
    delegations["WikiManager"] = output
    return {"delegations": delegations}


def execute_research_node(state: MotorState) -> dict[str, Any]:
    """Execute research task via ResearchSubgraph."""
    from src.agent.runtime import _run_research, _get_client

    _get_client()
    messages = state.get("messages", [])
    request = messages[-1].get("content", "") if messages else ""

    import asyncio
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    output = loop.run_until_complete(_run_research(request))
    delegations = state.get("delegations", {})
    delegations["ResearchSubgraph"] = output
    return {"delegations": delegations}


def execute_experiment_node(state: MotorState) -> dict[str, Any]:
    """Execute experiment task via ExperimentRunner."""
    from src.agent.runtime import _run_subagent, _get_client
    from src.agent.subagents import EXPERIMENT_RUNNER_AGENT
    from src.artifacts import ExperimentReport

    _get_client()
    messages = state.get("messages", [])
    request = messages[-1].get("content", "") if messages else ""

    import asyncio
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    output = loop.run_until_complete(
        _run_subagent(EXPERIMENT_RUNNER_AGENT, request, output_type=ExperimentReport)
    )
    delegations = state.get("delegations", {})
    delegations["ExperimentRunner"] = output
    return {"delegations": delegations}


def synthesize_node(state: MotorState) -> dict[str, str]:
    """Build human-readable synthesis from delegation results."""
    from src.agent.runtime import _synthesize

    result = {
        "category": state.get("category", ""),
        "delegations": state.get("delegations", {}),
    }
    return {"messages": [{"role": "assistant", "content": _synthesize(result)}]}
