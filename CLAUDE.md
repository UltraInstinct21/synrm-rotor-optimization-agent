# CLAUDE.md — motor-deepagent

**Project Root:** `D:\SRM\Agent\`
**Codename:** `motor-deepagent`
**Goal:** Terminal-first engineering assistant for general motor design, PyMotorCAD script generation & execution (run files), wiki management, and structured research. Project-specific numbers always come from the active project folder (`workspace/projects/<slug>/spec.json`), never from these docs.

---

## 1. System Architecture & Split

The system combines **DeepAgents** for orchestration/runtime capabilities with **LangGraph** for structured research workflows, backed by **durable wiki knowledge**.

```text
User / Terminal CLI (apps/cli/main.py)
  ↓
DeepAgent Orchestrator (deepagents runtime)
  ├── Run Files Creation & Execution (execute_generated_motorcad_code, execute_run_file)
  ├── Research Subagent Tool (src/tools/research/research_tool.py)
  ├── Web Search Tool (src/tools/search — tavily_search, HITL-gated)
  ├── Wiki Agent Tool (src/tools/wiki/wiki_tool.py)
  └── Built-in deepagents tools (write_todos, read_file, write_file, edit_file, ls, glob, grep)
        ↓
      LangGraph Research Subgraph (src/research/graph.py @entrypoint)
        ├── normalize_question
        ├── collect_context
        └── synthesize_research_report → ResearchReport
```

### Core Separation of Responsibilities
- **DeepAgent Orchestrator:** Creates PyMotorCAD Python script run files, executes them, manages user interaction, planning/todos, subagent routing, context summarization, and built-in file/tool execution.
- **Run Files Tools:** Allows DeepAgent to construct syntactically correct PyMotorCAD scripts and run them safely in sandboxed subprocesses.
- **LangGraph Subgraph:** Owns the explicit 3-step research pipeline (`normalize` → `collect` → `synthesize` → `report`).
- **Wiki Agent Tool:** Curates and queries durable project knowledge under `workspace/wiki/` (`search`, `read`, `list`, `write`).

---

## 2. DeepAgent Tools & Subsystems

1. **Run File Tools (`execute_run_file`, `execute_generated_motorcad_code`; `create_run_file` is internal):**
   - Create Python scripts using PyMotorCAD (`ansys.motorcad.core.MotorCAD`) for simulation, parameter sweeps, and optimization.
   - Execute generated run files in sandboxed subprocesses. Failed scripts stay on disk so the agent can patch them with `edit_file` and rerun via `execute_run_file`.
2. **Research Tool (`research_subgraph`):**
   - Literature review and engineering domain research pipeline.
3. **Wiki Tool (`wiki_tool`):**
   - Search, read, list, and update wiki documentation in `workspace/wiki/`.

---

## 3. Directory Map

| Path | Description |
|------|-------------|
| [`apps/cli/`](file:///D:/SRM/Agent/apps/cli/) | Rich terminal CLI harness (`main.py`, `app.py`, REPL) |
| [`src/agent/`](file:///D:/SRM/Agent/src/agent/) | DeepAgent factory (`factory.py`), graph, state, runtime |
| [`src/tools/execution.py`](file:///D:/SRM/Agent/src/tools/execution.py) | Run file creation and sandboxed code execution tools |
| [`src/tools/research/`](file:///D:/SRM/Agent/src/tools/research/) | `@tool` wrapper for LangGraph research subgraph |
| [`src/tools/wiki/`](file:///D:/SRM/Agent/src/tools/wiki/) | Wiki agent `@tool` for searching, reading, listing, updating wiki |
| [`src/motor/`](file:///D:/SRM/Agent/src/motor/) | Motor params, scoring, validation, sweep, ledger (`spec.py`, `validate.py`, `scoring.py`, `sweep.py`, `ledger.py`) |
| [`src/tools/motor/`](file:///D:/SRM/Agent/src/tools/motor/) | Motor-CAD validate/score `@tool` wrappers (`motor_tools.py`) |
| [`src/artifacts/`](file:///D:/SRM/Agent/src/artifacts/) | Pydantic data schemas for inter-component handoff |
| [`workspace/projects/`](file:///D:/SRM/Agent/workspace/projects/) | Canonical per-project folders (`<slug>/spec.json`, `ledger.jsonl`, `scratch/`, `models/`) |
| [`workspace/specs/`](file:///D:/SRM/Agent/workspace/specs/) | Example machine spec template (reference only) |
| [`workspace/wiki/`](file:///D:/SRM/Agent/workspace/wiki/) | Durable project knowledge (`project_overview.md`, `active_tasks.md`, `motorcad/`, `papers/`, `design_guidelines/`, ...) |
| [`AGENTS.md`](file:///D:/SRM/Agent/AGENTS.md) | General agent contract: active project folders, anti-hallucination rules |
| [`config.toml`](file:///D:/SRM/Agent/config.toml) | DeepAgents runtime configuration |
| [`pyproject.toml`](file:///D:/SRM/Agent/pyproject.toml) | Dependencies (`deepagents`, `langgraph`, `langchain-core`, `pydantic`) |

---

## 4. PyMotorCAD Scripting Rules

From [`AGENTS.md`](file:///D:/SRM/Agent/AGENTS.md) — strictly mandatory when generating PyMotorCAD run files:

1. **Parameter Database Search:** Search unknown or unverified variable names in `workspace/wiki/motorcad/parameter_database/` (`index.md`, `categories/*.md`, `parameters/<Name>.md`) using `wiki_tool`.
2. **Discovery Fallback:** Call `mc.get_variable_names()` before any `get`/`set` call if parameter string remains uncertain.
3. **Safe Wrappers:** Include `safe_get` / `safe_set` helper functions in generated scripts.
4. **Context Check:** Always invoke `mc.show_magnetic_context()` before running EMag calculations.
5. **Model Backup:** Save `best_so_far.mot` into the active project's `models/` before mutating geometry.
6. **Atomic Result Reading:** Read all required outputs (`ShaftTorque`, `InputPower`, loss breakdown) *immediately* after calculation.

### Motor-CAD Wiki Navigation Map (`workspace/wiki/motorcad/`)
- `parameter_database/`: 13,004 indexed parameters, 140 categories, parameter spec sheets.
- `pymotorcad-*.md`: Detailed API function & code documentation (`calculations-api.md`, `geometry-*.md`, `emag-example.md`, `thermal-*.md`, `lab-api.md`, `graphs-api.md`, `errors.md`).

---

## 5. Development & CLI Commands

```bash
# Launch interactive terminal CLI
python -m apps.cli.main
# or installed entrypoint:
motor

# Run tests
pytest
```
