# CLAUDE.md — motor-deepagent

**Project Root:** `D:\SRM\Agent\`
**Updated:** 2026-07-05

---

## PART 1: WORKING RULES

### 1. Planning & Context

- **Think Before Coding:** Never guess. State assumptions explicitly and push back when a simpler approach exists.
- **Explore First, Plan, Then Code:** Do not write code right away. Ask questions, surface tradeoffs, and output a step-by-step plan before making changes.
- **Goal-Driven Execution:** Tell Claude what success looks like and let it iterate, rather than micromanaging every step.

### 2. Code Quality & Discipline

- **Simplicity First:** Write the minimum code required to solve the problem. Do not add speculative abstractions or error handling for impossible scenarios.
- **Match Existing Style:** Always adopt the codebase's existing conventions, even if they differ from Claude's defaults.
- **Surgical Changes:** Modify only what is required. Never refactor code that is not broken, and do not "improve" adjacent code unless requested.

### 3. Session Management

- **Manage Context Aggressively:** If a session goes wrong, do not try to fix the same mistake three times. Run `/compact` to clear the whiteboard, or start a fresh session.
- **Use Checkpoints:** Git commit frequently — after every working change. Use commits as rewinding checkpoints.
- **Pre-approve Actions:** Define which tools Claude can use. Risky operations (deleting files, running destructive commands) require confirmation.
- **Create Reusable Skills:** Document recurring workflows so Claude knows exactly how to handle specific tasks every time.

---

## PART 2: PROJECT — MOTOR-DEEPAGENT

### Goal

Build a **terminal-first engineering assistant** that starts as a repo/wiki/research coding agent and grows into a motor-design assistant with PyMotorCAD / experiment / optimization workflows.

### Architecture

```
User → DeepAgent Orchestrator
         ├── Repo Coding Subagent
         ├── Wiki Manager
         ├── LangGraph Research Subgraph  (Phase 2)
         └── Experiment / Execution Layer  (Phase 3-4)
```

**Principle:** DeepAgent for orchestration + built-in coding-agent capabilities. LangGraph only for structured multi-step workflows where explicit graph structure helps.

### Key Files

| File | Purpose |
|------|---------|
| `apps/cli/main.py` | CLI entry point (single-shot + REPL) |
| `src/agent/build_agent.py` | Orchestrator builder |
| `src/agent/prompts.py` | System prompts for all subsystems |
| `src/agent/subagents.py` | Subagent configurations |
| `src/agent/approvals.py` | Permission boundaries |
| `src/agent/orchestration_helpers.py` | Task classification, artifact handoff |
| `src/artifacts/` | Pydantic data contracts (ResearchReport, CodeReport, etc.) |
| `src/config/settings.py` | Project-wide paths and model config |
| `src/tools/wiki/update_wiki.py` | Wiki Manager |
| `src/tools/execution/run_script.py` | Script execution |
| `src/skills/` | Skill definitions |
| `workspace/wiki/` | Durable project knowledge base |
| `SynRM_45kW_IE5.mot` | Reference motor model |
| `optimize_synrm_v4.py` | Existing optimization script (reference) |
| `AGENTS.md` | Motor specs, constraints, strategy |

### Data Contracts

Subsystems exchange structured artifacts, not free-form text:

| Artifact | Producer | Consumer |
|----------|----------|----------|
| `ResearchReport` | Research Subgraph | Orchestrator → Wiki Manager |
| `CodeReport` | Repo Coding Subagent | Orchestrator → Wiki Manager |
| `ExperimentReport` | Experiment Runner | Orchestrator → Wiki Manager |
| `WikiUpdatePlan` | Orchestrator | Wiki Manager |

### Project Wiki (workspace/wiki/)

Persistent knowledge base for engineering knowledge:

```
workspace/wiki/
├── index.md               # master index with [[wikilinks]]
├── project_overview.md
├── codebase_map.md
├── known_issues.md
├── active_tasks.md
├── architecture/
│   └── orchestrator.md
├── motorcad/
│   ├── workflow.md
│   ├── parameters.md
│   ├── result_fields.md
│   └── experiments/
└── papers/
```

Legacy reference wiki (Obsidian): `D:\SRM\Motor _CAD\ScriptFiles\wiki\`

### LLM Model Selection

All LLM calls use **free open-source models** via OpenRouter:

| Role | Model |
|------|-------|
| Default | `qwen/qwq-32b:free` |
| Research | `qwen/qwq-32b:free` |
| Synthesis | `nousresearch/hermes-3-llama-3.1-405b:free` |
| Calculate | `google/gemini-2.0-flash-exp:free` |
| Design | `qwen/qwq-32b:free` |

### PyMotorCAD Anti-Hallucination Rules

From `AGENTS.md` — followed when motor-domain tools are active:

1. `mc.get_variable_names()` before any `set`/`get`
2. Use `safe_get`/`safe_set` wrappers — never raw calls
3. `show_magnetic_context()` before electromagnetic analysis
4. Save before changing rotor params (`best_so_far.mot`)
5. Read all results before changing any parameter

---

## PART 3: TECH STACK

### Python Environment
- Python 3.13.5 (Anaconda, `C:\Users\sarth\anaconda3`)
- Windows 11

### Core Dependencies
| Package | Purpose |
|---------|---------|
| `pydantic>=2.0` | Data contracts / structured output |
| `python-dotenv>=1.0` | Environment loading |

### Phase 2 Dependencies
| Package | Purpose |
|---------|---------|
| `langgraph>=0.4.0` | Research subgraph orchestration |
| `chromadb>=0.6.0` | Vector store for RAG |
| `sentence-transformers>=3.0.0` | Text embeddings |
| `openai>=1.50.0` | OpenRouter API client |
| `langchain-core>=0.3.0` | LangGraph message types |

### Phase 4 Dependencies
| Package | Purpose |
|---------|---------|
| `ansys.motorcad.core` | PyMotorCAD (proprietary, Ansys EULA) |
| `numpy>=2.0` | Numerical ops |

### External Services
- **OpenRouter** — Free-tier LLM access (`qwen/qwq-32b`, `gemini-2.0-flash-exp`, etc.)
- **Ansys Motor-CAD 2025.1.1** — FEA solver (local, licensed)

### File Patterns
- `.mot` — Motor-CAD model files (binary INI-like, 15k+ lines)
- `.md` — Wiki pages with YAML frontmatter + `[[wikilinks]]`
- `.py` — Agent code, tools, CLI

---

## Quick Start

```bash
set OPENROUTER_API_KEY=sk-or-v1-...
python -m apps.cli.main "inspect the repo module structure"
python -m apps.cli.main          # interactive REPL
```

## Links

- Architecture spec: `AGENTS.md` (motor specs, constraints)
- Reference motor model: `SynRM_45kW_IE5.mot`
- Existing optimizer: `optimize_synrm_v4.py`
- Project wiki: `workspace/wiki/`
- Legacy wiki: `D:\SRM\Motor _CAD\ScriptFiles\wiki\`
