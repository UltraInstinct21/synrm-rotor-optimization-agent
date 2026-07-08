# DeepAgent ReAct Orchestrator Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** Refactor the motor-deepagent orchestrator from a keyword-routed StateGraph into a LangGraph ReAct agent where subagents are tools the LLM calls in a loop.

**Architecture:** Replace the current classify -> route -> execute_* -> synthesize StateGraph with a single ReAct agent loop (create_react_agent from langgraph.prebuilt). Each subsystem becomes a LangChain StructuredTool the orchestrator LLM selects via tool-calling.

**Tech Stack:** langgraph>=1.2, langgraph-prebuilt>=1.1, langchain-core>=1.4, pydantic>=2.0, langchain-openai>=1.3

## Global Constraints

- Python >= 3.13 (per pyproject.toml)
- langgraph>=0.4.0,<2.0.0 -- already satisfied
- langchain-core>=0.3.0 -- already satisfied
- Preserve backward compatibility: run_request_graph, run_request_graph_streamed
- All artifacts remain Pydantic models in src/artifacts/
- No new heavy dependencies

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| src/agent/tools.py | Create | LangChain StructuredTool wrappers for each subagent |
| src/agent/build_agent.py | Rewrite | Build ReAct agent via create_react_agent |
| src/agent/graph.py | Rewrite | Expose motor_graph as compiled ReAct agent |
| src/agent/runtime.py | Modify | Update run_request_graph / streaming |
| src/agent/prompts.py | Modify | Add ORCHESTRATOR_REACT system prompt |
| src/agent/subagents.py | Keep | Registry stays as config source |
| src/agent/nodes.py | Keep (deprecated) | Old nodes preserved, not used |
| src/agent/state.py | Keep | MotorState for backward compat |
| tests/test_graph.py | Modify | Update tests for new graph |
| tests/test_tools.py | Create | Tests for LangChain tool wrappers |
