# CLAUDE.md — motor-deepagent

**Project Root:** `D:\SRM\Agent\`
**Updated:** 2026-07-08

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

Build a **terminal-first engineering assistant** that starts as a motor-design assistant with PyMotorCAD / experiment / optimization workflows and grows into a broader engineering platform.

### Architecture

```
User → dcode (Deep Agents runtime)
         ├── Built-in tools (read/write/grep/ls/execute/web_search/memory/skills)
         ├── Motor-CAD Tools (src/tools/motorcad/)
         ├── Research Subagent → LangGraph research subgraph
         └── Domain Models (src/domain/motor/)
```

**Principle:** Deep Agents for runtime + built-in capabilities. LangGraph only for the research subgraph where explicit graph structure helps.

### Key Files

| File | Purpose |
|------|---------|
| `config.toml` | Deep Agents configuration |
| `AGENTS.md` | Motor specs, constraints, design strategy |
| `src/tools/motorcad/` | Motor-CAD domain tools (Deep Agents compatible) |
| `src/tools/research/` | Research subgraph wrapper tool |
| `src/research/graph.py` | LangGraph research pipeline |
| `src/domain/motor/` | Parameter maps, result models, geometry models |
| `src/config/settings.py` | Project-wide paths and model config |
| `src/artifacts/` | Pydantic data contracts |
| `SynRM_45kW_IE5.mot` | Reference motor model |
| `optimize_synrm_v4.py` | Existing optimization script (reference) |

### Data Contracts

Subsystems exchange structured artifacts, not free-form text:

| Artifact | Producer | Consumer |
|----------|----------|----------|
| `ResearchReport` | Research Subgraph | Deep Agents memory |
| `CodeReport` | Deep Agents coding | Deep Agents memory |
| `ExperimentReport` | Experiment Runner | Deep Agents memory |

### LLM Model Selection

All LLM calls route through **Opencode** (`ai.opencode.ai/zen/v1`). Model per subsystem set via `.env`:

| Role | Env Var | Current |
|------|---------|---------|
| Default | `MODEL_DEFAULT` | `deepseek-v4-flash-free` |
| Research | `MODEL_RESEARCH` | `deepseek-v4-flash-free` |
| Synthesis | `MODEL_SYNTHESIS` | `deepseek-v4-flash-free` |

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
| `deepagents` | Agent runtime (built-in tools, memory, HITL, subagents) |
| `langgraph` | Research subgraph orchestration |
| `langchain-core` | Tool decorators, message types |
| `langchain-openai` | LLM client for Opencode API |
| `pydantic>=2.0` | Data contracts / structured output |

### Phase 4 Dependencies
| Package | Purpose |
|---------|---------|
| `ansys.motorcad.core` | PyMotorCAD (proprietary, Ansys EULA) |

### External Services
- **Opencode** — LLM access (`ai.opencode.ai/zen/v1`)
- **Tavily** — Web search (for `web_search` tool)
- **Ansys Motor-CAD 2025.1.1** — FEA solver (local, licensed)

---

## Quick Start

```bash
set OPENROUTER_API_KEY=sk-or-v1-...
set TAVILY_API_KEY=tvly-...
dcode                              # interactive REPL
dcode "inspect the motor parameters"   # single-shot
```

## Links

- Architecture spec: `AGENTS.md` (motor specs, constraints)
- Reference motor model: `SynRM_45kW_IE5.mot`
- Existing optimizer: `optimize_synrm_v4.py`
