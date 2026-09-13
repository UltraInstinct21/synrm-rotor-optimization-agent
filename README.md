# motor-deepagent

**Terminal-first AI engineering agent for general electric motor design — PyMotorCAD simulation, spec-driven optimization, structured research, and wiki management.**

Built on **LangChain DeepAgents**, **LangGraph**, **PyMotorCAD (`ansys.motorcad.core`)**, **Tavily**, **Rich**, and **Prompt Toolkit**.

> The agent is machine-general (SynRM, PMSM/IPM, induction, BLDC, …). The current
> project's targets, bounds, and constraints come from the active project folder
> (`$MOTOR_PROJECT` → `workspace/projects/active.json` → legacy `workspace/specs/active.json`).
> Create one with `/project new <slug>` and switch with `/project use <slug>`.
> An example template (`synrm_45kw`) ships under `workspace/specs/` for reference only.

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

### 1. PyMotorCAD Script Creation & Guarded Execution
- **Unified 1-Turn Code Execution**: `execute_generated_motorcad_code` creates, scans, executes, and auto-logs Python simulation scripts in a single agent turn.
- **Safety Scan**: generated code is statically scanned (strings/comments stripped) — destructive filesystem ops, process spawning, network/exfiltration, and dynamic exec are blocked before anything runs.
- **Mutex**: Motor-CAD is single-instance; overlapping calls fail fast with `busy` instead of corrupting a solve.
- **Solve Budget + Breaker**: FEA solves consume a per-session budget (default 200); N consecutive failures trip a circuit breaker (`/budget`, `/budget reset`).
- **Experiment Ledger**: scripts print `CANDIDATE_RESULT: {...}` per candidate; the wrapper auto-logs + auto-scores into the active project's `workspace/projects/<slug>/ledger.jsonl` (`MOTOR_LEDGER_DIR` override supported).
- **Opt-in Approval**: `MOTORCAD_REQUIRE_APPROVAL=1` gates every run behind HITL approval.
- **Resource Protection**: Subprocess timeouts clamped 60–3600 s (FEA solves need ≥ 600 s).

### 1b. Spec-Driven Motor Design (`src/motor/`, `workspace/projects/`)
- **Machine Specs**: targets, parameter bounds, ordering/min/max constraints, locked params, and operating point live in JSON (`workspace/projects/<slug>/spec.json`) — new machines need a new project folder, no code. `workspace/specs/` holds the example template only.
- **`validate_motor_params`**: single source of truth for geometry checks, called before every solve.
- **`score_motor_result`**: computed spec compliance (objective + pass/fail), called after every solve.
- **Seeded Sweeps**: `src.motor.sweep` (`latin_hypercube`, `neighbors`, `has_converged`, `clamp`) makes Phase-1/Phase-2 reproducible.

### 2. Native Filesystem Integration & Parameter Database
- **DeepAgents Built-in Tools**: `grep`, `read_file`, `write_file`, `edit_file`, `ls`, `glob` — no redundant custom wrappers.
- **Parameter Database** (`workspace/wiki/motorcad/parameter_database/`): 13 000+ indexed Motor-CAD parameters across 140 categories. The agent searches this before writing any script, eliminating silent wrong-variable errors.

### 3. Async Research Subgraph
- **2-Stage LangGraph Pipeline**: `normalize_question` → `collect_context` → `synthesize_research_report`.
- **Context Explosion Protection**: Strict relevance filtering + 1 MB per-file cap on wiki reads.
- **LLM Fallback**: research calls retry on cheap provider models before failing.
- **Exposed as async tool** (`research_subgraph`) — non-blocking relative to the main orchestrator.

### 3b. Multi-Provider LLM Layer
- **Direct static-key client** (no session/OAuth flows): `LLM_PROVIDER=zen` (paid tier), `openrouter` (free `:free` models via API), `nim` (free NVIDIA NIM key), or `groq` (free tier). One-var switch — `LLM_BASE_URL` follows the provider unless explicitly customized.
- **Server-side gates are respected, not bypassed**: Zen free-tier models refuse direct API calls by design ("can only be used in OpenCode") — free usage goes through providers whose free tiers are API-accessible (NIM, OpenRouter, Groq), same approach as free-claude-code's provider routing.
- **Live catalogue per provider**: `/model` lists whatever the active base URL serves.

### 4. Human-In-The-Loop Web Search & Session TODO Tracking
- **Tavily Web Search**: General knowledge, IEEE standards, and technical benchmarks.
- **Thread-Safe HITL Mode**: `/hitl` toggles interactive approval prompts before any external web query.
- **Mid-Session TODO Tracking**: `write_todos` + `update_todo_status` render a live status card above the CLI prompt.

---

## Project folders

Each motor project is self-contained:

```
workspace/projects/<slug>/
├── spec.json       # targets, param bounds, constraints, locked list, operating point
├── ledger.jsonl    # scored CANDIDATE_RESULT log (append-only)
├── scratch/        # generated run scripts for this project
├── models/         # .mot files and backups (e.g. best_so_far.mot)
└── README.md       # project notes
```

Create/select on launch (`/project new <slug>`, `/project use <slug>`).
An example template ships under `workspace/specs/` for reference.

---

## Repository Layout

```
motor-deepagent/
├── apps/cli/           # Terminal UI — Rich renderer, prompt-toolkit REPL, slash commands
├── src/
│   ├── agent/          # DeepAgent factory & runtime (factory.py, runtime.py)
│   ├── motor/          # Machine-agnostic domain: spec, validate, scoring, ledger, sweep
│   ├── tools/
│   │   ├── execution.py      # Guarded PyMotorCAD code execution (scan, mutex, budget, ledger)
│   │   ├── motor/            # validate_motor_params + score_motor_result
│   │   ├── search/           # Tavily web search (HITL-aware)
│   │   ├── wiki/             # Wiki read/write helpers
│   │   └── todo_tools.py     # Session TODO tracking tools (if present)
│   ├── research/       # 3-node LangGraph research subgraph (LLM fallback enabled)
│   └── config/         # Settings, Zen model discovery, preflight checks
├── workspace/
│   ├── projects/<slug>/  # Canonical per-project spec, ledger, scratch/, models/
│   ├── specs/          # Example machine spec template (reference only)
│   ├── wiki/           # Living knowledge base — motor theory, PyMotorCAD docs
│   │   └── motorcad/parameter_database/  # 13 000+ indexed parameters
│   ├── scratch/        # (gitignored) legacy per-session scripts
│   └── experiments/    # (gitignored) legacy per-project ledger data
├── tests/              # pytest suite — CLI, execution guards, motor domain, wiki, research
├── AGENTS.md           # General agent contract (project numbers live in project folders)
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
# LLM provider (one-var switch: zen | openrouter | nim | groq)
OPENCODE_API_KEY=oc-...
LLM_PROVIDER=zen
LLM_MODEL=nemotron-3-ultra-free

# Tavily Web Search
TAVILY_API_KEY=tvly-your-tavily-key-here

# Active project folder + Motor-CAD
MOTOR_PROJECT=my_motor
MOTORCAD_EXE=C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe
```

### 3. Motor-CAD Requirement
Ansys Motor-CAD must be installed (`MOTORCAD_EXE`, default `C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe`). The agent auto-launches it via PyMotorCAD when executing simulation scripts. `.mot` model files live in each project's `models/` folder and are never committed.

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
| `/model [id\|number\|prefix\|list\|refresh]` | List Opencode Zen models (auto-fetched live) or switch the active LLM model |
| `/project [list\|show\|new\|use]` | Manage project folders (each has its own spec/results/scripts) |
| `/spec [list\|show\|use]` | Manage machine specs (legacy view over project spec files) |
| `/budget [reset]` | Show Motor-CAD solve budget and breaker state |
| `/preflight` | Re-run startup environment checks |
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
