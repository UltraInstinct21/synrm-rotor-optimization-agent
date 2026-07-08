# Design Spec: Deep Agents Migration

**Date:** 2026-07-08
**Author:** motor-deepagent team
**Status:** Approved

---

## 1. Problem Statement

The motor-deepagent repo has accumulated ~30 custom tool functions (~2000+ lines) that duplicate capabilities already provided by LangChain Deep Agents (`deepagents` package). The codebase mixes two frameworks (OpenAI Agents SDK + LangGraph), has two competing architectures (StateGraph + ReAct agent), and subagent configs that are never wired to execution.

**Goal:** Clean the repo end-to-end. Use Deep Agents as the primary runtime, preserve the LangGraph research subgraph, and repackage Motor-CAD domain tools as Deep Agents tools.

---

## 2. Approach

**Approach B: Deep Agents + LangGraph Research**

- Deep Agents handles: agent loop, built-in tools (read/write/grep/ls/execute/web_search/memory/skills/subagents), CLI (`dcode`), HITL, tracing
- LangGraph handles: research subgraph (sequential pipeline with conditional branching)
- Motor-CAD tools: re-wrapped as Deep Agents-compatible tools
- Wiki system: migrated to Deep Agents memory storage

---

## 3. What Gets Deleted

### Entire directories (remove completely)

| Path | Lines | Reason |
|------|-------|--------|
| `src/tools/filesys/` | ~350 | Deep Agents has `read_file`, `write_file`, `grep`, `ls`, `glob` |
| `src/tools/shell/` | ~80 | Deep Agents has `execute` |
| `src/tools/search/` | ~120 | Deep Agents has `web_search` |
| `src/tools/memory/` | ~150 | Deep Agents has memory storage/retrieval |
| `src/tools/wiki/` | ~200 | Wiki → Deep Agents memory |
| `src/tools/execution/` | ~80 | Deep Agents has `execute` + `task` |
| `src/memory/` | ~100 | Deep Agents has memory built-in |
| `src/skills/` | ~200 | Deep Agents has its own skills system |
| `src/agent/graph.py` | ~150 | Dead StateGraph (never wired) |
| `src/agent/nodes.py` | ~200 | Dead graph nodes |
| `src/agent/runtime.py` | ~250 | Custom REPL (replaced by `dcode`) |
| `src/agent/subagents.py` | ~80 | SubagentConfig not wired |
| `src/agent/approvals.py` | ~60 | Deep Agents handles HITL |
| `src/agent/event_stream.py` | ~150 | Deep Agents has tracing |
| `src/agent/tools.py` | ~100 | Delegation tools replaced by Deep Agents `task` |
| `apps/cli/` | ~200 | Replaced by `dcode` CLI |
| `src/tools/__init__.py` | ~30 | Empty/imports of deleted modules |

**Total deleted:** ~2500 lines across 18 files/directories

### What stays

| Path | Reason |
|------|--------|
| `src/tools/motorcad/` | Domain-specific, re-wrap as Deep Agents tools |
| `src/domain/motor/` | Motor-CAD parameter maps, result models |
| `src/research/` | LangGraph research subgraph (preserved) |
| `src/config/settings.py` | Model config, paths, env loading |
| `src/artifacts/` | Pydantic data contracts |

---

## 4. New Architecture

```
dcode CLI (Deep Agents runtime)
  ├── Built-in tools (read_file, write_file, grep, ls, execute, web_search, task, memory, skills)
  ├── Motor-CAD Tool Package (src/tools/motorcad/)
  │     ├── safe_get, safe_set, set_parameter, save_checkpoint
  │     ├── launch_motorcad, load_model, run_magnetic, run_and_extract, close_motorcad
  │     └── get_available_variables, extract_results
  ├── Research Subagent (delegates to LangGraph graph)
  │     └── src/research/graph.py (normalize → collect_context → read_extract → synthesize → build_report)
  ├── Domain Models (src/domain/motor/)
  │     ├── parameter_mapping.py (STATOR_MAP, ROTOR_MAP, etc.)
  │     └── result_models.py (ElectromagneticResult, ComparisonResult)
  ├── Data Contracts (src/artifacts/)
  └── Config (src/config/settings.py)
```

### Data flow

1. User runs `dcode "optimize the SynRM motor"`
2. Deep Agents runtime loads config, built-in tools, Motor-CAD tools, research subagent
3. Agent classifies intent → routes to appropriate tool/subagent
4. Motor-CAD operations use domain tools (safe_get, safe_set, run_magnetic)
5. Research queries delegate to LangGraph subgraph via `task` tool
6. Results stored in Deep Agents memory
7. All operations traced via LangSmith

---

## 5. Motor-CAD Tool Package

### Location

`src/tools/motorcad/` — keep existing files, add `__init__.py` with tool registration.

### Tool wrapping

Each Motor-CAD function gets a LangChain `@tool` decorator so Deep Agents can ingest it:

```python
from langchain_core.tools import tool

@tool
def motorcad_safe_get(var_name: str) -> str:
    """Read a variable from Motor-CAD. Returns float value or None if not found."""
    # ... implementation
```

### Tools to wrap

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `motorcad_launch` | Start/connect to Motor-CAD | `visible: bool = False` | Instance handle |
| `motorcad_load_model` | Load .mot file | `path: str` | Status |
| `motorcad_safe_get` | Read variable | `var_name: str` | Value or None |
| `motorcad_safe_set` | Set variable with verification | `var_name: str, value: float` | Success + message |
| `motorcad_set_parameter` | Set with domain validation | `var_name: str, value: float, domain: str` | Success + message |
| `motorcad_save_checkpoint` | Save .mot checkpoint | `path: str = "best_so_far.mot"` | Status |
| `motorcad_run_magnetic` | Run electromagnetic analysis | none | Status |
| `motorcad_run_and_extract` | Run + extract all results | none | ElectromagneticResult |
| `motorcad_get_variables` | List available variables | none | Variable list |
| `motorcad_close` | Quit Motor-CAD | none | Status |

### Anti-hallucination safeguards (preserved)

From `AGENTS.md`:
1. `get_variable_names()` before any `set`/`get`
2. `safe_get`/`safe_set` wrappers — never raw calls
3. `show_magnetic_context()` before electromagnetic analysis
4. Save before changing rotor params
5. Read all results before changing any parameter

---

## 6. Research Subagent

### Preservation

The LangGraph research subgraph at `src/research/` stays as-is. It's a well-structured sequential pipeline:

```
normalize_question → collect_context → source_selection → read_extract → synthesize_claims → build_report
```

### Deep Agents integration

A single wrapper tool that Deep Agents can call:

```python
@tool
def research_subgraph(question: str) -> str:
    """Research a motor engineering question. Returns a structured report with sources, claims, and equations."""
    from src.research.graph import run_research
    result = run_research(question)
    return json.dumps(result, indent=2)
```

This is registered as a Deep Agents tool. When the agent needs research, it calls this tool, which delegates to the LangGraph pipeline.

---

## 7. Configuration

### Deep Agents config (`config.toml`)

```toml
[agent]
model = "deepseek-v4-flash-free"
system_prompt = "You are a motor engineering assistant. You help with motor design, simulation, and optimization using PyMotorCAD. You can research topics, analyze motor parameters, and run electromagnetic simulations."

[tools]
packages = ["src/tools/motorcad/"]

[memory]
enabled = true

[subagents]
enabled = true
```

### Environment variables (`.env`)

```
OPENROUTER_API_KEY=sk-or-v1-...
MODEL_DEFAULT=deepseek-v4-flash-free
MODEL_RESEARCH=deepseek-v4-flash-free
TAVILY_API_KEY=...  # for web_search
```

---

## 8. Final File Structure

```
D:\SRM\Agent\
├── config.toml                    # Deep Agents config
├── .env                           # API keys
├── .gitignore
├── AGENTS.md                      # Motor specs, constraints
├── CLAUDE.md                      # Project instructions
├── README.md
├── SynRM_45kW_IE5.mot            # Reference motor model
├── optimize_synrm_v4.py          # Existing optimizer
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py           # Model config, paths
│   ├── domain/
│   │   ├── __init__.py
│   │   └── motor/
│   │       ├── __init__.py
│   │       ├── parameter_mapping.py
│   │       └── result_models.py
│   ├── research/
│   │   ├── __init__.py
│   │   ├── graph.py              # LangGraph research pipeline
│   │   ├── nodes.py              # Pipeline nodes
│   │   └── state.py              # ResearchState TypedDict
│   ├── tools/
│   │   ├── __init__.py
│   │   └── motorcad/
│   │       ├── __init__.py
│   │       ├── run_motorcad.py
│   │       ├── set_parameters.py
│   │       └── get_results.py
│   └── artifacts/
│       ├── __init__.py
│       └── models.py
├── workspace/
│   └── memory/                    # Deep Agents memory store
└── docs/
    └── superpowers/specs/
```

---

## 9. Migration Steps

1. **Install Deep Agents:** `pip install deepagents`
2. **Create `config.toml`** at project root
3. **Wrap Motor-CAD tools** with `@tool` decorators in `src/tools/motorcad/`
4. **Add research wrapper** tool that calls `run_research()`
5. **Delete dead code** (all paths listed in Section 3)
6. **Clean up imports** in remaining files
7. **Update `AGENTS.md`** to reflect new architecture
8. **Test:** Run `dcode "list the available Motor-CAD variables"` to verify tool loading
9. **Migrate wiki knowledge** to Deep Agents memory (if any critical knowledge exists)

---

## 10. Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Motor-CAD tools may not work in Deep Agents sandbox | Test with `dcode --auto-approve` first, then enable HITL |
| Research subgraph may have import issues after cleanup | Verify imports before deleting any files |
| Deep Agents memory may not match wiki structure | Migrate critical wiki pages to memory, keep wiki dir as fallback |
| Model routing (MODEL_DEFAULT vs MODEL_RESEARCH) | Configure in `config.toml` per-subagent if needed |

---

## 11. Success Criteria

- [ ] `dcode` launches and responds to basic queries
- [ ] Motor-CAD tools are discoverable and callable via `dcode`
- [ ] Research subgraph executes when delegated via `task` tool
- [ ] No duplicate tool implementations remain
- [ ] All dead code removed (~2500 lines)
- [ ] Single framework (Deep Agents) for runtime, LangGraph only for research
