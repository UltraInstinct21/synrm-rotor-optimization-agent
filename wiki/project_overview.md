---
title: Project Overview
created: 2026-07-05
---

# Project Overview

## Summary

**motor-deepagent** is a terminal-first engineering assistant that starts as a repo/wiki/research coding agent and grows into a motor-design assistant with PyMotorCAD / experiment / optimization workflows.

## Project structure

```
motor-deepagent/
├── apps/cli/           # Terminal entry point
├── src/
│   ├── agent/          # Orchestrator + subagent definitions
│   ├── artifacts/      # Data contracts (ResearchReport, CodeReport, etc.)
│   ├── config/         # Project settings
│   ├── skills/         # Skill definitions
│   ├── tools/          # Wiki, execution, motorcad tools
│   ├── research/       # LangGraph research subgraph (Phase 2)
│   ├── execution/      # Experiment runner
│   └── domain/motor/   # Motor-domain models (Phase 4)
├── workspace/
│   ├── wiki/           # Durable knowledge base
│   └── experiments/    # Experiment outputs
└── tests/
```

## Architecture

See [[architecture/orchestrator]] for the component architecture.

## Key principles

- **DeepAgent for orchestration** — built-in planning, tools, subagent delegation
- **LangGraph for structured workflows** — explicit state transitions, branching, retries
- **Wiki-first knowledge** — durable project memory with structured pages
- **Structured artifacts** — subsystems exchange typed data contracts, not free-form text

## Phases

| Phase | Focus | Status |
|-------|-------|--------|
| 1 | Engineering wiki + repo coding agent | ✅ Active |
| 2 | Research subgraph | 🔜 Planned |
| 3 | Experiment / execution layer | 🔜 Planned |
| 4 | Motor-domain tools (PyMotorCAD) | 🔜 Planned |
