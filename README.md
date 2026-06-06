# SynRM Multi-Agent Pipeline

LangGraph 4-phase state machine for automated SynRM motor design & optimization via PyMotorCAD FEA.

## Architecture

```
                    ┌──────────────────────────────────┐
                    │       LangGraph State Machine     │
                    │  (AgentState, MemorySaver,        │
                    │   phase_router conditional edges)  │
                    └──────┬──────┬──────┬──────┬───────┘
                           │      │      │      │
                    ┌──────┘      │      │      └────────┐
                    ▼             ▼      ▼               ▼
              ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
              │ RESEARCH │→│SYNTHESIS │→│CALCULATE │→│DESIGN    │
              │ Phase 1  │ │ Phase 2  │ │ Phase 3  │ │& OPTIM   │
              │          │ │          │ │          │ │ Phase 4  │
              └──────────┘ └──────────┘ └──────────┘ └──────────┘
                     │            │            │            │
                     ▼            ▼            ▼            ▼
              ┌───────────────────────────────────────────────────┐
              │                 Shared Knowledge Layer             │
              │  ┌──────────────┐  ┌──────────────┐  ┌─────────┐ │
              │  │  Obsidian    │  │  ChromaDB    │  │ .mot    │ │
              │  │  Wiki (.md)  │  │  (vectors)   │  │ Files   │ │
              │  └──────────────┘  └──────────────┘  └─────────┘ │
              └───────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.13 (Anaconda)
- Ansys Motor-CAD 2025.1.1 (for FEA)
- OpenRouter API key (free models)

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set API key (free-tier OpenRouter models)
set OPENROUTER_API_KEY=sk-or-v1-...
```

### Run Pipeline

```bash
python run_pipeline.py
```

Without API key: Calculate + Design phases run; Research + Synthesis gracefully degrade.
With API key: All 4 phases execute end-to-end.

## LangSmith Studio Visualization

Visualize and debug the pipeline graph in LangSmith Studio.

### Setup

```bash
# Copy env template and add your keys
cp .env.example .env
# Edit .env with your LangSmith API key
```

```bash
# Start the LangGraph dev server
langgraph dev
```

This reads `langgraph.json`, starts a local API server, and LangSmith Studio connects to it.

### What You See

| View | Shows |
|------|-------|
| Graph canvas | 4 phase nodes + routing edges |
| Tracing | Each pipeline run as a trace tree |
| State snapshots | `phase_status`, `winding_params`, etc. per step |
| Error visualization | Failed nodes highlighted with traceback |

### LangSmith Tracing (Standalone)

Without Studio, runs are automatically logged to LangSmith when env vars are set:

```bash
set LANGSMITH_TRACING=true
set LANGSMITH_API_KEY=lsv2_...
set LANGSMITH_PROJECT=synrm-agent
python run_pipeline.py
```

## Module Reference

### Graph (`agent/graph.py`)

| Function | Description |
|----------|-------------|
| `build_graph()` | Compile 4-node StateGraph with MemorySaver checkpointer |
| `initial_state(motor_spec)` | Create default AgentState for 45kW IE5 SynRM |
| `phase_router(state)` | Conditional edge: route done→next, failed→skip, running→stay |
| `safe_node_wrapper(func, state)` | try/except wrapper — marks phase failed with traceback |

### State (`agent/state.py`)

`AgentState` TypedDict fields:

| Field | Type | Populated By |
|-------|------|-------------|
| `messages` | `list[BaseMessage]` | LangGraph message history |
| `phase` | `str` | Current phase name |
| `phase_status` | `dict[str, PhaseStatus]` | All phases |
| `motor_spec` | `dict` | Initial state (45kW, 143Nm, 3000rpm, 4-pole, 580V) |
| `winding_params` | `dict` | Phase 3: Kw=0.9576, 24turns, 5.6A/mm², 0.589 fill |
| `barrier_params` | `dict` | Phase 3: airgap=0.5mm, saliency=7.0, barrier ratios |
| `derived_params` | `dict` | Phase 3: sizing, losses, thermal constraints |
| `mot_sections` | `dict[str, dict]` | Phase 4: 124 sections parsed from .mot |
| `pymotorcad_vars` | `list[str]` | Phase 4: discovered Motor-CAD variables |
| `optimization_results` | `list[dict]` | Phase 4 sub-node: LHS results |
| `wiki_*` | `list[str]` | Phases 1-2: paths to created wiki pages |

### Tool Layer (`agent/tools/`)

| Module | Functions | Purpose |
|--------|-----------|---------|
| `chroma.py` | `get_collection`, `add_document`, `query_similar` | Persistent vector store (5 collections) |
| `embedder.py` | `embed_text`, `embed_texts` | sentence-transformers all-MiniLM-L6-v2 |
| `wiki.py` | `read_page`, `write_page`, `update_index` | Obsidian .md with YAML frontmatter |
| `chunker.py` | `chunk_text` | 500-char chunks, 50-char overlap |
| `pymotorcad.py` | `launch_motorcad`, `discover_variables`, `safe_get/set`, `evaluate_candidate_in_process` | Motor-CAD COM automation (AGENTS.md Rules 1-5) |
| `web_search.py` | `search_research_topic` | LLM-based research via OpenRouter |
| `retry.py` | `retry` decorator, `timeout_node` | Error hardening |

### Model Config (`agent/models.py`)

| Node | Model |
|------|-------|
| Research | `qwen/qwq-32b:free` |
| Synthesis | `nousresearch/hermes-3-llama-3.1-405b:free` |
| Calculate | `google/gemini-2.0-flash-exp:free` |
| Design | `qwen/qwq-32b:free` |
| Default | `qwen/qwq-32b:free` |

### Phase Nodes (`agent/nodes/`)

| Node | File | What It Does |
|------|------|-------------|
| Research | `research.py` | Web→chunk→embed→ChromaDB→LLM extract→wiki write |
| Synthesis | `synthesis.py` | Gap analysis, LLM insight generation, wiki write |
| Calculate | `calculate.py` | Sizing (143Nm), winding (24t, 5.6A/mm²), magnetic (0.5mm airgap, ξ=7.0), thermal (120°C) |
| Design | `design.py` | Parse .mot (124 sections), PyMotorCAD variable discovery, parameter setting |
| Optimization | `optimization.py` | LHS sampling, FEA evaluation via v4 script, simulated fallback |

## Error Handling

Each phase has 3-layer protection:

1. **Node-level try/except** — catches failures, sets `phase_status[phase]=failed`
2. `safe_node_wrapper` — wraps all node calls in `graph.py`, logs traceback
3. `@retry(max_attempts=2, delay=1.0)` — on ChromaDB `add_document` (exp backoff)

**Graceful degradation:**

| Failure | Behavior |
|---------|----------|
| No API key | Research/Synthesis fail → router skips to Calculate |
| No Motor-CAD | Design parses .mot without PyMotorCAD, Optimization uses simulated results |
| LLM timeout | Falls through to next phase with empty results |
| PyMotorCAD import error | evaluate_candidate_in_process returns error dict |

## Anti-Hallucination Rules (AGENTS.md)

All 5 rules enforced in `agent/tools/pymotorcad.py`:

1. **Discover before first use** — `discover_variables()` called before any set/get
2. **safe_get / safe_set wrappers** — no raw Motor-CAD calls
3. `show_magnetic_context()` — capture context before EMag solves
4. **Save before changing rotor params** — `save_backup()` creates timestamped `.mot.bak`
5. **Read results before changing** — `safe_get` reads current value before set

## File Map

```
D:\SRM\Agent\
├── run_pipeline.py          ← Entry point
├── agent/
│   ├── __init__.py
│   ├── state.py             ← AgentState TypedDict
│   ├── graph.py             ← LangGraph StateGraph + phase_router
│   ├── models.py            ← OpenRouter model config
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── research.py      ← Phase 1
│   │   ├── synthesis.py     ← Phase 2
│   │   ├── calculate.py     ← Phase 3
│   │   ├── design.py        ← Phase 4
│   │   └── optimization.py  ← Phase 4 sub-node
│   └── tools/
│       ├── chroma.py        ← ChromaDB vector store
│       ├── embedder.py      ← sentence-transformers
│       ├── wiki.py          ← Obsidian .md writer
│       ├── chunker.py       ← Text chunking
│       ├── pymotorcad.py    ← Motor-CAD automation
│       ├── web_search.py    ← Research via LLM
│       └── retry.py         ← Retry + timeout
├── optimize_synrm_v4.py     ← Existing reference
├── SynRM_45kW_IE5.mot       ← Working model
├── AGENTS.md                ← Project spec
├── requirements.txt
└── docs/superpowers/
    ├── specs/2026-06-06-synrm-multi-agent-design.md
    └── plans/2026-06-06-synrm-multi-agent-implementation.md
```

## Extended Spec

- Design: `docs/superpowers/specs/2026-06-06-synrm-multi-agent-design.md`
- Plan: `docs/superpowers/plans/2026-06-06-synrm-multi-agent-implementation.md`
