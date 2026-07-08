---
title: Orchestrator Architecture
created: 2026-07-05
---

# Orchestrator Architecture

## Design

The orchestrator is a **DeepAgent** that owns the user interaction loop and delegates specialized work.

```
User
  ↓
DeepAgent Orchestrator
  ├─ Repo Coding Subagent
  ├─ Wiki Manager
  ├─ LangGraph Research Subgraph  (Phase 2)
  └─ Experiment / Execution Layer  (Phase 3)
```

## Why this split

- **Context management** — no single agent tries to do everything.
- **Clear responsibility boundaries** — each subsystem has a narrow contract.
- **Observability** — you can see which subsystem produced which result.
- **Extensibility** — motor-domain workflows slot into the execution layer.

## Orchestrator responsibilities

- Classify the task (repo, wiki, research, experiment, mixed).
- Build a high-level plan.
- Delegate to the correct subsystem with enough context.
- Merge structured artifacts into a final response.

## Orchestrator non-responsibilities

- Deep paper reading — that belongs in the Research Subgraph.
- Large wiki edits — that belongs in the Wiki Manager.
- All repo exploration — that belongs in the Repo Coding Subagent.
- Motor-CAD logic — that belongs in the domain execution layer.
