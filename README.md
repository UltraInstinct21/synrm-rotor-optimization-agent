# motor-deepagent ⚡

**Terminal-first engineering assistant** — repo/wiki/research/motor-design assistant.

Built as a **DeepAgent orchestrator** with specialized subagents:

- **Repo Coding Subagent** — inspect, patch, validate code
- **Wiki Manager** — durable project knowledge base
- **Research Subgraph** — multi-source research (Phase 2)
- **Experiment Runner** — script execution (Phase 3)
- **Motor-Domain Tools** — PyMotorCAD workflows (Phase 4)

## Quick start

```bash
set OPENROUTER_API_KEY=sk-or-v1-...
python -m apps.cli.main "inspect the repo and explain the module structure"
```

Interactive REPL:

```bash
python -m apps.cli.main
```

## Project structure

```
apps/cli/           # Terminal entry point
src/
  agent/            # Orchestrator + subagent definitions
  artifacts/        # Pydantic data contracts
  config/           # Settings
  skills/           # Skill definitions
  tools/            # Wiki, execution, motorcad tools
  research/         # LangGraph research subgraph
  execution/        # Experiment runner
  domain/motor/     # Motor-domain models
workspace/
  wiki/             # Durable knowledge base
  experiments/      # Experiment outputs
```

## Phases

| Phase | Status |
|-------|--------|
| 1 — Engineering wiki + repo coding agent | ✅ Active |
| 2 — Research subgraph | 🔜 Planned |
| 3 — Experiment/execution layer | 🔜 Planned |
| 4 — Motor-domain tools | 🔜 Planned |

## Dependencies

- Python 3.13+
- `pydantic` (data contracts)
- Optional: `langgraph`, `chromadb` (Phase 2)
- Optional: `ansys.motorcad.core` (Phase 4)

## License

MIT
