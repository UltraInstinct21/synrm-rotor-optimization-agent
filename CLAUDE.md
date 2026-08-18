# CLAUDE.md — motor-deepagent

**Project Root:** `D:\SRM\Agent\`  
**Codename:** `motor-deepagent`  
**Goal:** Terminal-first engineering assistant for SynRM motor design, PyMotorCAD script generation & execution (run files), wiki management, and structured research.

---

## 1. System Architecture & Split

The system combines **DeepAgents** for orchestration/runtime capabilities with **LangGraph** for structured research workflows, backed by **durable wiki knowledge**.

```text
User / Terminal CLI (apps/cli/main.py)
  ↓
DeepAgent Orchestrator (deepagents runtime)
  ├── Run Files Creation & Execution (create_run_file, execute_run_file, execute_generated_motorcad_code)
  ├── Research Subagent Tool (src/tools/research/research_tool.py)
  └── Wiki Agent Tool (src/tools/wiki/wiki_tool.py)
        ↓
      LangGraph Research Subgraph (src/research/graph.py @entrypoint)
        ├── normalize_question
        ├── collect_context
        ├── source_selection
        ├── read_extract
        ├── synthesize_claims
        └── build_report → ResearchReport
```

### Core Separation of Responsibilities
- **DeepAgent Orchestrator:** Creates PyMotorCAD Python script run files, executes them, manages user interaction, planning/todos, subagent routing, context summarization, and built-in file/tool execution.
- **Run Files Tools:** Allows DeepAgent to construct syntactically correct PyMotorCAD scripts and run them safely in sandboxed subprocesses.
- **LangGraph Subgraph:** Owns explicit multi-step research pipelines (`normalize` → `collect` → `select` → `extract` → `synthesize` → `report`).
- **Wiki Agent Tool:** Curates and queries durable project knowledge under `wiki/` (`search`, `read`, `list`, `write`).

---

## 2. DeepAgent Tools & Subsystems

1. **Run File Tools (`create_run_file`, `execute_run_file`, `execute_generated_motorcad_code`):**
   - Create Python scripts using PyMotorCAD (`ansys.motorcad.core.MotorCAD`) for simulation, parameter sweeps, and optimization.
   - Execute generated run files in sandboxed subprocess environment.
2. **Research Tool (`research_subgraph`):**
   - Literature review and engineering domain research pipeline.
3. **Wiki Tool (`wiki_tool`):**
   - Search, read, list, and update wiki documentation in `wiki/`.

---

## 3. Directory Map

| Path | Description |
|------|-------------|
| [`apps/cli/`](file:///D:/SRM/Agent/apps/cli/) | Rich terminal CLI harness (`main.py`, `app.py`, REPL) |
| [`src/agent/`](file:///D:/SRM/Agent/src/agent/) | DeepAgent factory (`factory.py`), graph, state, runtime |
| [`src/tools/execution.py`](file:///D:/SRM/Agent/src/tools/execution.py) | Run file creation and sandboxed code execution tools |
| [`src/tools/research/`](file:///D:/SRM/Agent/src/tools/research/) | `@tool` wrapper for LangGraph research subgraph |
| [`src/tools/wiki/`](file:///D:/SRM/Agent/src/tools/wiki/) | Wiki agent `@tool` for searching, reading, listing, updating wiki |
| [`src/domain/motor/`](file:///D:/SRM/Agent/src/domain/motor/) | Motor parameters, geometry models, result definitions |
| [`src/artifacts/`](file:///D:/SRM/Agent/src/artifacts/) | Pydantic data schemas for inter-component handoff |
| [`wiki/`](file:///D:/SRM/Agent/wiki/) | Durable project knowledge (`project_overview.md`, `codebase_map.md`, `active_tasks.md`, `known_issues.md`) |
| [`AGENTS.md`](file:///D:/SRM/Agent/AGENTS.md) | Motor specification, optimization variables, and anti-hallucination rules |
| [`config.toml`](file:///D:/SRM/Agent/config.toml) | DeepAgents runtime configuration |
| [`pyproject.toml`](file:///D:/SRM/Agent/pyproject.toml) | Dependencies (`deepagents`, `langgraph`, `langchain-core`, `pydantic`) |

---

## 4. PyMotorCAD Scripting Rules

From [`AGENTS.md`](file:///D:/SRM/Agent/AGENTS.md) — strictly mandatory when generating PyMotorCAD run files:

1. **Parameter Database Search:** Search unknown or unverified variable names in `workspace/wiki/motorcad/parameter_database/` (`index.md`, `categories/*.md`, `parameters/<Name>.md`) using `wiki_tool`.
2. **Discovery Fallback:** Call `mc.get_variable_names()` before any `get`/`set` call if parameter string remains uncertain.
3. **Safe Wrappers:** Include `safe_get` / `safe_set` helper functions in generated scripts.
4. **Context Check:** Always invoke `mc.show_magnetic_context()` before running EMag calculations.
5. **Model Backup:** Save `best_so_far.mot` before mutating rotor parameters.
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
