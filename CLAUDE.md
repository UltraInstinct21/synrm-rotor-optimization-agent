# CLAUDE.md — SynRM Multi-Agent Pipeline Project

**Project Root:** `D:\SRM\Agent\`
**Updated:** 2026-06-06

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
- **Provide Verification Criteria:** Claude performs best when given test cases or exact target outputs.

### 3. Session Management

- **Manage Context Aggressively:** If a session goes wrong, do not try to fix the same mistake three times. Run `/compact` to clear the whiteboard, or start a fresh session.
- **Use Checkpoints:** Git commit frequently — after every working change. Use commits as rewinding checkpoints.
- **Pre-approve Actions:** Define which tools Claude can use. Risky operations (deleting files, running destructive commands) require confirmation.
- **Create Reusable Skills:** Document recurring workflows so Claude knows exactly how to handle specific tasks (like code reviews) every time.
- **Define Your Tech Stack:** Explicitly list dependencies, file structures, and ignored patterns (see Part 3).

---

## PART 2: PROJECT — SYNRM MULTI-AGENT PIPELINE

### Goal

Build a multi-agent LangGraph pipeline that:
1. **Researches** SynRM motor design theory (web + user resources)
2. **Synthesizes** knowledge into an Obsidian-style wiki
3. **Calculates** motor parameters from ratings (power, speed, torque)
4. **Designs & Optimizes** .mot files via PyMotorCAD FEA

### Architecture

LangGraph state machine with 4 phases — each phase is a graph node with typed state (`AgentState`). Shared knowledge layer via ChromaDB (vectors) + Obsidian `wiki/` (markdown files).

```
User → Research → Synthesis → Calculate → Design & Optimize → .mot file
                                                      │
                                                      ▼
                                              PyMotorCAD FEA
```

### Key Files

| File | Purpose |
|------|---------|
| `run_pipeline.py` | Entry point — runs full pipeline |
| `agent/graph.py` | LangGraph StateGraph + phase routing |
| `agent/state.py` | `AgentState` TypedDict |
| `agent/models.py` | LLM client config (OpenRouter, free models) |
| `agent/nodes/research.py` | Phase 1: source ingest → entity extraction |
| `agent/nodes/synthesis.py` | Phase 2: gap/conflict/insight |
| `agent/nodes/calculate.py` | Phase 3: sizing, winding, magnetic params |
| `agent/nodes/design.py` | Phase 4: .mot explorer + variable discovery |
| `agent/nodes/optimization.py` | Phase 4 sub-node: LHS/Pareto/PA sweep |
| `agent/tools/chroma.py` | ChromaDB client + collection manager |
| `agent/tools/wiki.py` | Obsidian .md reader/writer |
| `agent/tools/embedder.py` | sentence-transformers wrapper |
| `agent/tools/chunker.py` | Text chunking with overlap |
| `agent/tools/pymotorcad.py` | PyMotorCAD subprocess launcher |
| `agent/tools/retry.py` | Retry + timeout decorators |
| `optimize_synrm_v4.py` | Existing PyMotorCAD optimization script (reference) |
| `SynRM_45kW_IE5.mot` | Working model file |
| `AGENTS.md` | Project spec — specs, constraints, strategy |

### LLM Wiki Knowledge Base

The project uses an Obsidian-style wiki at `D:\SRM\Motor _CAD\ScriptFiles\wiki\` as its persistent knowledge layer. See `D:\SRM\Motor _CAD\ScriptFiles\CLAUDE.md` Part 1 for the full wiki schema (INGEST, QUERY, LINT workflows, YAML frontmatter, wikilink conventions).

**Wiki structure:**
```
wiki/
├── index.md           # master index — all pages listed
├── log.md             # append-only activity log
├── entities/          # motor types, materials, researchers, companies
├── concepts/          # design principles, equations, tradeoffs
├── sources/           # ingested papers, design guides, web content
├── synthesis/         # cross-cutting analyses, calculations, logs
└── queries/           # answered questions
```

### LLM Model Selection

All LLM calls use **free open-source models** via OpenRouter:

| Node | Model | Notes |
|------|-------|-------|
| Default | `qwen/qwq-32b:free` | Strong reasoning, free tier |
| Research | `qwen/qwq-32b:free` | Fast research summaries |
| Synthesis | `nousresearch/hermes-3-llama-3.1-405b:free` | Deep cross-referencing |
| Calculate | `google/gemini-2.0-flash-exp:free` | Numerical precision |
| Design | `qwen/qwq-32b:free` | High-stakes geometry decisions |

### PyMotorCAD Anti-Hallucination Rules

From `AGENTS.md` — followed by all design/optimization code:

1. **Discover before first use** — `mc.get_variable_names()` before any `set/get`
2. **Use safe_get / safe_set wrappers** — never raw calls
3. **show_magnetic_context() before EMag**
4. **Save before changing rotor params** — `best_so_far.mot` checkpoint
5. **Read all results before changing any parameter**

---

## PART 3: TECH STACK

### Python Environment
- Python 3.13.5 (Anaconda, `C:\Users\sarth\anaconda3`)
- Windows 11

### Core Dependencies
| Package | Purpose | License |
|---------|---------|---------|
| `langgraph>=0.4.0` | State machine orchestration | MIT |
| `chromadb>=0.6.0` | Vector store for RAG | Apache 2.0 |
| `sentence-transformers>=3.0.0` | Text embeddings | Apache 2.0 |
| `openai>=1.50.0` | OpenRouter API client | MIT |
| `langchain-core>=0.3.0` | LangGraph message types | MIT |
| `numpy>=2.0.0` | Numerical ops | BSD |
| `pydantic>=2.0.0` | Structured output schemas | MIT |
| `ansys.motorcad.core` | PyMotorCAD (proprietary) | Ansys EULA |

### External Services
- **OpenRouter** — Free-tier LLM access (`qwen/qwq-32b`, `gemini-2.0-flash-exp`, etc.)
- **Ansys Motor-CAD 2025.1.1** — FEA solver (local, licensed)
- **Obsidian** — Knowledge graph visualization (optional, local)

### File Patterns
- `.mot` — Motor-CAD model files (binary INI-like, 15k+ lines)
- `.csv` — Optimization result logs
- `.md` — Wiki pages with YAML frontmatter + `[[wikilinks]]`
- `.py` — Agent nodes, tools, pipeline scripts

### Git Ignore
```
.chroma/
__pycache__/
*.pyc
.env
optimization_results*.csv
best_so_far*.mot
*.bak
```

---

## Links

- Design spec: `docs/superpowers/specs/2026-06-06-synrm-multi-agent-design.md`
- Implementation plan: `docs/superpowers/plans/2026-06-06-synrm-multi-agent-implementation.md`
- Existing wiki: `D:\SRM\Motor _CAD\ScriptFiles\CLAUDE.md` (wiki schema, Part 1)
- Optimization reference: `D:\SRM\Agent\AGENTS.md` (motor specs, constraints)
- Existing optimization: `D:\SRM\Agent\optimize_synrm_v4.py`
