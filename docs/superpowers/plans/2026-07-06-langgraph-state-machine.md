# LangGraph State Machine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace ad-hoc `run_request()` dispatch with a LangGraph `StateGraph` enabling HITL interrupts, streaming, and persistent state.

**Architecture:** LangGraph `StateGraph` with nodes for classify → route → execute → synthesize. Checkpointer for resumable sessions. Interrupts before motor writes.

**Tech Stack:** `langgraph>=0.4.0`, `langchain-core>=0.3.0`, existing OpenAI Agents SDK for subagent execution.

## Global Constraints

- Python >=3.13
- `langgraph>=0.4.0,<2.0.0`
- `langchain-core>=0.3.0,<1.0.0`
- Preserve existing `run_request()` API for backward compatibility
- All existing tests must pass after each task

---

## File Structure

| File | Purpose |
|------|---------|
| `src/agent/graph.py` | **NEW** — LangGraph StateGraph definition |
| `src/agent/state.py` | **NEW** — MotorState TypedDict |
| `src/agent/nodes.py` | **NEW** — Graph node functions |
| `src/agent/runtime.py` | **MODIFY** — Add `run_request_graph()` wrapper |
| `src/agent/checkpoint.py` | **NEW** — Checkpointer setup |
| `tests/test_graph.py` | **NEW** — Graph tests |

---

### Task 1: State Definition

**Files:**
- Create: `src/agent/state.py`
- Test: `tests/test_graph.py`

**Interfaces:**
- Produces: `MotorState` TypedDict

- [ ] **Step 1: Write the failing test**

```python
# tests/test_graph.py
"""Tests for LangGraph state machine."""

from __future__ import annotations


def test_motor_state_import():
    """MotorState can be imported and instantiated."""
    from src.agent.state import MotorState

    state: MotorState = {
        "messages": [],
        "category": "question",
        "delegations": {},
        "active_agent": "",
        "pending_changes": None,
        "last_checkpoint": None,
    }
    assert state["category"] == "question"
    assert state["delegations"] == {}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_graph.py::test_motor_state_import -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'src.agent.state'"

- [ ] **Step 3: Write minimal implementation**

```python
# src/agent/state.py
"""LangGraph state definition for motor-deepagent."""

from __future__ import annotations

from typing import Any, Literal, Optional, TypedDict

from langgraph.graph import add_messages
from typing_extensions import Annotated


class MotorState(TypedDict, total=False):
    """State channels for the motor-deepagent graph.

    Attributes:
        messages: Conversation history (reducer: append).
        category: Classified task type.
        delegations: Subsystem results keyed by agent name.
        active_agent: Current routing target.
        pending_changes: Motor parameter changes awaiting approval.
        last_checkpoint: Path to last Motor-CAD save state.
    """

    messages: Annotated[list, add_messages]
    category: str
    delegations: dict[str, Any]
    active_agent: str
    pending_changes: Optional[dict]
    last_checkpoint: Optional[str]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_graph.py::test_motor_state_import -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/agent/state.py tests/test_graph.py
git commit -m "feat: add MotorState TypedDict for LangGraph"
```

---

### Task 2: Graph Node Functions

**Files:**
- Create: `src/agent/nodes.py`
- Test: `tests/test_graph.py`

**Interfaces:**
- Consumes: `MotorState` from Task 1
- Produces: `classify_node()`, `route_node()`, `execute_code_node()`, `execute_wiki_node()`, `execute_research_node()`, `execute_experiment_node()`, `synthesize_node()`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_graph.py (append)

def test_classify_node():
    """classify_node sets category based on request."""
    from src.agent.nodes import classify_node

    state = {"messages": [{"role": "user", "content": "inspect the code"}]}
    result = classify_node(state)
    assert result["category"] == "repo_coding"


def test_route_node():
    """route_node returns correct next node name."""
    from src.agent.nodes import route_node

    state = {"category": "repo_coding"}
    assert route_node(state) == "execute_code"

    state = {"category": "wiki_maintenance"}
    assert route_node(state) == "execute_wiki"

    state = {"category": "research"}
    assert route_node(state) == "execute_research"

    state = {"category": "experiment"}
    assert route_node(state) == "execute_experiment"

    state = {"category": "question"}
    assert route_node(state) == "synthesize"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_graph.py::test_classify_node tests/test_graph.py::test_route_node -v`
Expected: FAIL with "ImportError"

- [ ] **Step 3: Write minimal implementation**

```python
# src/agent/nodes.py
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_graph.py::test_classify_node tests/test_graph.py::test_route_node -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/agent/nodes.py tests/test_graph.py
git commit -m "feat: add graph node functions for classify, route, execute, synthesize"
```

---

### Task 3: Checkpointer Setup

**Files:**
- Create: `src/agent/checkpoint.py`
- Test: `tests/test_graph.py`

**Interfaces:**
- Produces: `get_checkpointer()` function

- [ ] **Step 1: Write the failing test**

```python
# tests/test_graph.py (append)

def test_checkpointer_setup():
    """Checkpointer can be created."""
    from src.agent.checkpoint import get_checkpointer

    checkpointer = get_checkpointer()
    assert checkpointer is not None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_graph.py::test_checkpointer_setup -v`
Expected: FAIL with "ImportError"

- [ ] **Step 3: Write minimal implementation**

```python
# src/agent/checkpoint.py
"""Checkpointer setup for LangGraph state persistence."""

from __future__ import annotations

from langgraph.checkpoint.memory import MemorySaver


def get_checkpointer() -> MemorySaver:
    """Return an in-memory checkpointer for session persistence.

    In production, replace with SqliteSaver or PostgresSaver.
    """
    return MemorySaver()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_graph.py::test_checkpointer_setup -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/agent/checkpoint.py tests/test_graph.py
git commit -m "feat: add checkpointer setup for LangGraph persistence"
```

---

### Task 4: Graph Definition

**Files:**
- Create: `src/agent/graph.py`
- Test: `tests/test_graph.py`

**Interfaces:**
- Consumes: `MotorState`, node functions, checkpointer
- Produces: `build_graph()` function, `motor_graph` compiled graph

- [ ] **Step 1: Write the failing test**

```python
# tests/test_graph.py (append)

def test_graph_builds():
    """Graph can be built and compiled."""
    from src.agent.graph import build_graph

    graph = build_graph()
    assert graph is not None


def test_graph_has_nodes():
    """Graph has all required nodes."""
    from src.agent.graph import build_graph

    graph = build_graph()
    nodes = list(graph.nodes.keys())
    assert "classify" in nodes
    assert "route" in nodes
    assert "execute_code" in nodes
    assert "execute_wiki" in nodes
    assert "execute_research" in nodes
    assert "execute_experiment" in nodes
    assert "synthesize" in nodes
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_graph.py::test_graph_builds tests/test_graph.py::test_graph_has_nodes -v`
Expected: FAIL with "ImportError"

- [ ] **Step 3: Write minimal implementation**

```python
# src/agent/graph.py
"""LangGraph state machine for motor-deepagent."""

from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from src.agent.checkpoint import get_checkpointer
from src.agent.nodes import (
    classify_node,
    execute_code_node,
    execute_experiment_node,
    execute_research_node,
    execute_wiki_node,
    route_node,
    synthesize_node,
)
from src.agent.state import MotorState


def build_graph() -> StateGraph:
    """Build the motor-deepagent LangGraph.

    Returns compiled graph with checkpointer for state persistence.
    """
    builder = StateGraph(MotorState)

    # Add nodes
    builder.add_node("classify", classify_node)
    builder.add_node("route", route_node)
    builder.add_node("execute_code", execute_code_node)
    builder.add_node("execute_wiki", execute_wiki_node)
    builder.add_node("execute_research", execute_research_node)
    builder.add_node("execute_experiment", execute_experiment_node)
    builder.add_node("synthesize", synthesize_node)

    # Add edges
    builder.add_edge(START, "classify")
    builder.add_edge("classify", "route")

    # Conditional routing from route node
    builder.add_conditional_edges(
        "route",
        route_node,
        {
            "execute_code": "execute_code",
            "execute_wiki": "execute_wiki",
            "execute_research": "execute_research",
            "execute_experiment": "execute_experiment",
            "synthesize": "synthesize",
        },
    )

    # All execution nodes go to synthesize
    builder.add_edge("execute_code", "synthesize")
    builder.add_edge("execute_wiki", "synthesize")
    builder.add_edge("execute_research", "synthesize")
    builder.add_edge("execute_experiment", "synthesize")
    builder.add_edge("synthesize", END)

    # Compile with checkpointer
    checkpointer = get_checkpointer()
    return builder.compile(checkpointer=checkpointer)


# Pre-compiled graph for import
motor_graph = build_graph()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_graph.py::test_graph_builds tests/test_graph.py::test_graph_has_nodes -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/agent/graph.py tests/test_graph.py
git commit -m "feat: add LangGraph StateGraph definition with conditional routing"
```

---

### Task 5: Runtime Integration

**Files:**
- Modify: `src/agent/runtime.py`
- Test: `tests/test_graph.py`

**Interfaces:**
- Consumes: `motor_graph` from Task 4
- Produces: `run_request_graph()` function

- [ ] **Step 1: Write the failing test**

```python
# tests/test_graph.py (append)

def test_run_request_graph_import():
    """run_request_graph can be imported."""
    from src.agent.runtime import run_request_graph
    assert callable(run_request_graph)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_graph.py::test_run_request_graph_import -v`
Expected: FAIL (function doesn't exist yet)

- [ ] **Step 3: Add function to runtime.py**

Add at end of `src/agent/runtime.py`:

```python
# ── LangGraph integration ────────────────────────────────────────────


async def run_request_graph(
    request: str,
    thread_id: str = "default",
) -> dict[str, Any]:
    """Process a request through the LangGraph state machine.

    Parameters
    ----------
    request : str
        The user's natural-language request.
    thread_id : str
        Thread ID for checkpointer persistence.

    Returns
    -------
    dict
        Final state with messages, category, delegations.
    """
    from src.agent.graph import motor_graph

    config = {"configurable": {"thread_id": thread_id}}

    # Invoke graph
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_graph.py::test_run_request_graph_import -v`
Expected: PASS

- [ ] **Step 5: Run full test suite**

Run: `pytest tests/ -v`
Expected: All tests pass

- [ ] **Step 6: Commit**

```bash
git add src/agent/runtime.py tests/test_graph.py
git commit -m "feat: add run_request_graph() LangGraph integration"
```

---

### Task 6: Backward Compatibility Test

**Files:**
- Test: `tests/test_graph.py`

**Interfaces:**
- Consumes: `run_request()` from runtime.py

- [ ] **Step 1: Write the failing test**

```python
# tests/test_graph.py (append)

def test_original_run_request_still_works():
    """Original run_request() API is preserved."""
    from src.agent.runtime import run_request
    assert callable(run_request)
```

- [ ] **Step 2: Run test to verify it passes**

Run: `pytest tests/test_graph.py::test_original_run_request_still_works -v`
Expected: PASS

- [ ] **Step 3: Commit**

```bash
git add tests/test_graph.py
git commit -m "test: verify backward compatibility with run_request()"
```

---

### Task 7: Full Graph Integration Test

**Files:**
- Test: `tests/test_graph.py`

**Interfaces:**
- Consumes: `motor_graph`

- [ ] **Step 1: Write the integration test**

```python
# tests/test_graph.py (append)

def test_graph_invoke_question():
    """Graph can invoke on a simple question."""
    from src.agent.graph import motor_graph

    config = {"configurable": {"thread_id": "test-question-1"}}
    result = motor_graph.invoke(
        {"messages": [{"role": "user", "content": "hello"}]},
        config=config,
    )
    assert "category" in result
    assert result["category"] == "question"
    assert "messages" in result
    assert len(result["messages"]) >= 1
```

- [ ] **Step 2: Run test to verify it passes**

Run: `pytest tests/test_graph.py::test_graph_invoke_question -v`
Expected: PASS (may be slow due to LLM call)

- [ ] **Step 3: Commit**

```bash
git add tests/test_graph.py
git commit -m "test: add full graph integration test"
```

---

### Task 8: Cleanup & Documentation

**Files:**
- Modify: `src/agent/graph.py` (docstring only)

- [ ] **Step 1: Update module docstring**

```python
# src/agent/graph.py (update docstring at top)

"""LangGraph state machine for motor-deepagent.

Provides:
- ``build_graph()`` — builds the StateGraph with all nodes and edges.
- ``motor_graph`` — pre-compiled graph instance ready for invocation.
- ``run_request_graph()`` in runtime.py — async wrapper for graph invocation.

Graph Flow:
    classify → route → execute_* → synthesize → END

State:
    MotorState with messages, category, delegations, pending_changes.
"""
```

- [ ] **Step 2: Run full test suite**

Run: `pytest tests/ -v`
Expected: All tests pass

- [ ] **Step 3: Commit**

```bash
git add src/agent/graph.py
git commit -m "docs: update graph module docstring"
```

---

## Summary

| Task | Description | Files Changed |
|------|-------------|---------------|
| 1 | State Definition | `src/agent/state.py`, `tests/test_graph.py` |
| 2 | Graph Node Functions | `src/agent/nodes.py`, `tests/test_graph.py` |
| 3 | Checkpointer Setup | `src/agent/checkpoint.py`, `tests/test_graph.py` |
| 4 | Graph Definition | `src/agent/graph.py`, `tests/test_graph.py` |
| 5 | Runtime Integration | `src/agent/runtime.py`, `tests/test_graph.py` |
| 6 | Backward Compatibility | `tests/test_graph.py` |
| 7 | Full Integration Test | `tests/test_graph.py` |
| 8 | Cleanup & Documentation | `src/agent/graph.py` |

**Total new files:** 4 (`state.py`, `nodes.py`, `checkpoint.py`, `graph.py`)
**Total modified files:** 2 (`runtime.py`, `tests/test_graph.py`)
