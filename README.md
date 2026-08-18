# motor-deepagent

**Terminal-first AI engineering agent for Synchronous Reluctance Motor (SynRM) design — PyMotorCAD simulation, rotor barrier optimization, structured research, and wiki management.**

Built on **LangChain DeepAgents**, **LangGraph**, **PyMotorCAD (`ansys.motorcad.core`)**, **Tavily**, **Rich**, and **Prompt Toolkit**.

> **Current mission:** Optimize the rotor flux-barrier geometry of a 45 kW SynRM to meet IE5 efficiency (≥ 96.0 %), 143 Nm rated torque at 3000 RPM, and power factor ≥ 0.85 — all without touching the locked stator geometry.

---

## System Architecture

```text
                     ┌─────────────────────────────────────────┐
                     │    User / Terminal CLI (apps/cli/)      │
                     │    - Rich Markdown & Live Token Stream  │
                     │    - Ctrl+O Expanded Tool Details View  │
                     │    - Ctrl+C Session Memory Interrupts   │
                     │    - Dynamic Task Status & Toolbar      │
                     │    - Slash Commands (/hitl /model …)    │
                     └────────────────────┬────────────────────┘
                                          │
                                          ▼
                     ┌─────────────────────────────────────────┐
                     │   DeepAgent Orchestrator (factory.py)   │
                     │   - System Prompt & Anti-Hallucination  │
                     │   - Tool Routing & Memory Checkpointing │
                     │   - config.toml & Settings Manager      │
                     └────┬──────────┬──────────┬─────────────┘
                          │          │          │
          ┌───────────────┴──┐  ┌────┴──────┐  ┌┴──────────────────────┐
          │ PyMotorCAD       │  │ Research  │  │ Native Filesystem +   │
          │ Execution Tool   │  │ Subgraph  │  │ Wiki/Search Tools     │
          │ (execution.py)   │  │(LangGraph │  │ (wiki/, search/,      │
          │                  │  │ pipeline) │  │  todo_tools.py)       │
          │ - Sandboxed 1-   │  │           │  │                       │
          │   Turn Scripts   │  │ normalize │  │ - Parameter DB lookup │
          │ - Path Guards    │  │ → collect │  │ - Tavily Web Search   │
          │ - Auto Cleanup   │  │ → synth.  │  │ - TODO tracking       │
          └──────────────────┘  └───────────┘  └───────────────────────┘
```

---

## Key Features

### 1. PyMotorCAD Script Creation & Sandboxed Execution
- **Unified 1-Turn Code Execution**: `execute_generated_motorcad_code` creates, sandboxes, executes, and auto-cleans Python simulation scripts in a single agent turn.
- **Security & Path Traversal Guards**: Scripts cannot escape `workspace/scratch/` via relative or absolute path manipulation.
- **Resource Protection**: Subprocess timeouts clamped strictly between 1 and 3600 s.
- **Anti-Hallucination Safeguards**: System prompt enforces parameter-database lookup before any `set_variable` / `get_variable` call, dynamic name discovery, explicit context switches (`show_magnetic_context()`), and checkpoint backups before each candidate.

### 2. Native Filesystem Integration & Parameter Database
- **DeepAgents Built-in Tools**: `grep`, `read_file`, `write_file`, `edit_file`, `ls`, `glob` — no redundant custom wrappers.
- **Parameter Database** (`workspace/wiki/motorcad/parameter_database/`): 13 000+ indexed Motor-CAD parameters across 140 categories. The agent searches this before writing any script, eliminating silent wrong-variable errors.

### 3. Async Research Subgraph
- **2-Stage LangGraph Pipeline**: `normalize_question` → `collect_context` → `synthesize_research_report`.
- **Context Explosion Protection**: Strict relevance filtering + 1 MB per-file cap on wiki reads.
- **Exposed as async tool** (`research_subgraph`) — non-blocking relative to the main orchestrator.

### 4. Human-In-The-Loop Web Search & Session TODO Tracking
- **Tavily Web Search**: General knowledge, IEEE standards, and technical benchmarks.
- **Thread-Safe HITL Mode**: `/hitl` toggles interactive approval prompts before any external web query.
- **Mid-Session TODO Tracking**: `write_todos` + `update_todo_status` render a live status card above the CLI prompt.

---

## Project: 45 kW SynRM Rotor Optimization

### Target Specification

| Parameter | Target | Tolerance |
|---|---|---|
| Output Power | 45 kW | ±2% |
| Rated Torque | 143 Nm @ 3000 RPM | ±2% |
| Rated Speed | 3000 RPM | exact |
| Max Speed | 6000 RPM | must not degrade |
| Efficiency Class | IE5 (≥ 96.0%) | must meet or exceed |
| Power Factor | ≥ 0.85 | — |
| Control Angle | 45° (fixed) | — |
| Service Factor | 1.2 | must sustain |

### Optimization Variables (12 rotor barrier parameters)

| Variable | Baseline | Search Range |
|---|---|---|
| `L1_Diameter` | 100 mm | 90–115 mm |
| `L1_Bridge_Thickness` | 4 mm | 1–6 mm |
| `L1_Web_Thickness` | 17 mm | 5–30 mm |
| `L1_Outer_Angle_Offset` | −10° | −20–0° |
| `L1_Outer_Thickness` | 4 mm | 2–8 mm |
| `L1_Inner_Thickness` | 5 mm | 2–8 mm |
| `L2_Diameter` | 130 mm | 120–150 mm |
| `L2_Bridge_Thickness` | 5 mm | 1–6 mm |
| `L2_Web_Thickness` | 50 mm | 20–70 mm |
| `L3_Diameter` | 160 mm | 145–175 mm |
| `L3_Bridge_Thickness` | 5 mm | 1–6 mm |
| `L3_Web_Thickness` | 82 mm | 50–100 mm |

### Stator — locked, not modified

340 mm OD · 215 mm bore · 48 slots · 50C250 lamination · Parallel Tooth

### Optimization Strategy
1. **Phase 1 (Coarse Sweep)** — Latin Hypercube / grid over ~20–50 candidates, log `ShaftTorque` + `Efficiency`.
2. **Phase 2 (Gradient Refinement)** — Coordinate descent from the best Phase 1 candidate until Δtorque < 0.5 Nm.

---

## Repository Layout

```
motor-deepagent/
├── apps/cli/           # Terminal UI — Rich renderer, prompt-toolkit REPL, slash commands
├── src/
│   ├── agent/          # DeepAgent factory & runtime (factory.py, runtime.py)
│   ├── tools/
│   │   ├── execution.py      # Sandboxed PyMotorCAD code execution tool
│   │   ├── search/           # Tavily web search (HITL-aware)
│   │   ├── wiki/             # Wiki read/write helpers
│   │   └── todo_tools.py     # Session TODO tracking tools
│   ├── research/       # 3-node LangGraph research subgraph
│   └── config/         # Settings & config.toml loader
├── workspace/
│   ├── wiki/           # Living knowledge base — motor theory, PyMotorCAD docs
│   │   └── motorcad/parameter_database/  # 13 000+ indexed parameters
│   ├── scratch/        # (gitignored) per-session generated scripts
│   └── experiments/    # (gitignored) optimization run data
├── tests/              # pytest suite — CLI, execution sandbox, wiki, research
├── AGENTS.md           # Codex/agent rules — variable names, constraints, file paths
├── config.toml         # Runtime config (model, paths, HITL default)
├── langgraph.json      # LangGraph server config
└── pyproject.toml      # Package build & dependencies
```

---

## Tech Stack

| Layer | Libraries |
|---|---|
| Agent Runtime | [`deepagents`](https://github.com/langchain-ai/deepagents), [`langgraph`](https://github.com/langchain-ai/langgraph), [`langchain-core`](https://github.com/langchain-ai/langchain), [`langchain-openai`](https://github.com/langchain-ai/langchain) |
| Motor Simulation | [`ansys.motorcad.core`](https://motorcad.docs.pyansys.com/) (PyMotorCAD), `numpy` |
| Web Search | `tavily-python` |
| CLI & UI | `rich ≥ 13.0`, `prompt_toolkit ≥ 3.0` |
| Testing | `pytest`, `pytest-cov` |

---

## Installation & Configuration

### 1. Clone & Install
```bash
git clone https://github.com/your-username/motor-deepagent.git
cd motor-deepagent

# Editable install with CLI entrypoint
pip install -e .

# Motor-CAD integration (requires Ansys Motor-CAD licence)
pip install -e ".[motorcad]"
```

### 2. Configure Environment Variables
Copy `.env.example` → `.env` and fill in your keys:

```env
# LLM Provider
OPENAI_API_KEY=your-openai-key-here

# Tavily Web Search
TAVILY_API_KEY=tvly-your-tavily-key-here

# Optional overrides
MOTORCAD_SCRIPT_DIR=D:\SRM\Motor _CAD\ScriptFiles
```

### 3. Motor-CAD Requirement
Ansys Motor-CAD v2025.1.1 must be installed. The agent auto-launches it via PyMotorCAD when executing simulation scripts.

---

## Usage

### Launch the REPL
```bash
motor
```

### Slash Commands

| Command | Description |
|---|---|
| `/help` | Show all commands organized by category |
| `/todo` | Manage session TODO tasks (`list`, `add <task>`, `done <id>`, `clear`) |
| `/expanded` | Toggle expanded tool call details (inputs & outputs) |
| `/hitl [on/off]` | Toggle Human-In-The-Loop web search approval |
| `/model [name]` | View or switch active LLM model |
| `/tools` | List all tools available to the agent |
| `/session` | Manage sessions (`list`, `new`, `load <id>`, `export [path]`) |
| `/clear` | Clear terminal screen |
| `/exit` | Save session and exit |

---

## Running Tests

```bash
python -m pytest tests/ -v
```

---

## License

MIT
