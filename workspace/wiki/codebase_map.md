---
title: Codebase Map
created: 2026-07-05
---

# Codebase Map

## Module layout

| Path | Responsibility |
|------|---------------|
| `apps/cli/main.py` | Entry point — single-shot and REPL modes |
| `apps/cli/chat.py` | Interactive REPL loop |
| `apps/cli/display.py` | Terminal formatting utilities |
| `src/config/settings.py` | Project-wide paths, model config, backend routes |
| `src/agent/build_agent.py` | Orchestrator agent builder |
| `src/agent/prompts.py` | System prompts for all subsystems |
| `src/agent/subagents.py` | Subagent configurations |
| `src/agent/approvals.py` | Permission boundaries |
| `src/agent/orchestration_helpers.py` | Task classification, artifact handoff |
| `src/artifacts/` | Pydantic data contracts |
| `src/tools/wiki/update_wiki.py` | Wiki Manager — read, merge, update |
| `src/tools/execution/run_script.py` | Script execution with result capture |
| `src/skills/` | Skill definitions |
| `workspace/wiki/` | Durable project knowledge |

## Data flow

```
User request
  └→ Orchestrator classifies task
       ├→ Repo Coding Subagent → CodeReport
       ├→ Wiki Manager → wiki updates
       ├→ Research Subgraph → ResearchReport (Phase 2)
       └→ Experiment Runner → ExperimentReport (Phase 3)
  └→ Orchestrator synthesizes response
```

## Reference files

| File | Purpose |
|------|---------|
| `SynRM_45kW_IE5.mot` | Reference motor model |
| `optimize_synrm_v4.py` | Existing optimization script |
| `AGENTS.md` | Motor specs, constraints, strategy |
