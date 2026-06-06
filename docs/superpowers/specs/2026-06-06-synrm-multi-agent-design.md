# SynRM Multi-Agent Design Pipeline

**Date:** 2026-06-06
**Project:** D:\SRM\Agent\ — SynRM 45kW IE5 Rotor Optimization
**Status:** Implemented ✅ | 16/16 tasks complete | All 4 phases running

---

## 1. System Overview

A **LangGraph state machine** with 4 sequential phases. Each phase is a LangGraph node (potentially a mini-graph) that consumes from and writes to a shared knowledge layer. Phases run sequentially by default but support conditional skipping, retry, and failure recovery.

```
                    ┌──────────────────────────────────┐
                    │       LangGraph State Machine     │
                    │  (typed state, checkpointing)     │
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

### File Paths (from existing project)

| Item | Path |
|---|---|
| Project root | `D:\SRM\Agent\` |
| Working .mot | `D:\SRM\Agent\SynRM_45kW_IE5.mot` |
| Optimization script | `D:\SRM\Agent\optimize_synrm_v4.py` |
| Obsidian wiki | `D:\SRM\Motor _CAD\ScriptFiles\wiki\` |
| AGENTS.md spec | `D:\SRM\Agent\AGENTS.md` |
| Motor-CAD EXE | `C:\Ansys_Motor-CAD\2025_1_1\Motor-CAD_2025_1_1.exe` |

---

## 2. Shared State Schema (LangGraph)

```python
class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    phase: str                              # current phase name
    phase_status: dict[str, str]            # {phase: started|done|failed|skipped}
    error_log: list[dict]                   # [{phase, error, timestamp}]

    # Knowledge graph references
    wiki_entities_created: list[str]        # paths to new entity pages
    wiki_concepts_created: list[str]        # paths to new concept pages
    wiki_synthesis: list[str]               # paths to synthesis pages

    # Motor specification (from user)
    motor_spec: dict                        # {power, torque, speed, poles, ...}

    # Calculation outputs
    winding_params: dict                    # {kw, turns, fill, wire_dia, ...}
    barrier_params: dict                    # {L1_Dia, L2_Dia, L3_Dia, bridges...}
    derived_params: dict                    # {current_density, slot_fill, etc}

    # .mot file state
    mot_file_path: str                      # path to current .mot file
    mot_sections: dict                      # parsed .mot content by section
    pymotorcad_vars: list[str]              # discovered variable names

    # Optimization results
    optimization_results: list[dict]        # CSV-compatible result rows
    best_model_path: str                    # path to best .mot found
```

---

## 3. Phase 1 — Research Node

### Purpose
Ingest web sources, papers, and user-provided documents. Extract structured entities, concepts, and relationships. Write to Obsidian wiki + ChromaDB.

### Sub-nodes

**3.1 WebSearch Agent**
- Takes user query or research topic
- Calls WebSearch API (OpenRouter model)
- Returns markdown summaries with sources

**3.2 Source Ingest Agent**
- Accepts: PDF paths, URLs, raw text, .md files
- Extracts content, normalizes format
- Stores raw `.md` in `wiki/sources/`

**3.3 Chunking + Embedding**
- Split source text into ~500-char chunks with 50-char overlap
- Embed with `sentence-transformers/all-MiniLM-L6-v2`
- Index into ChromaDB collection `sources` with metadata:
  - `source_id`, `section`, `tags`, `chunk_idx`

**3.4 Entity/Concept Extraction**
- LLM call with `StructuredOutput` returns schema:
  ```python
  class ExtractedEntity(BaseModel):
      title: str
      type: Literal["entity", "concept", "source"]
      content: str
      relations: list[str]          # [[wikilinks]] to existing pages
      tags: list[str]
  ```
- Pre-check ChromaDB for duplicates via similarity > 0.85
- If new, write to `wiki/{type}s/{slug}.md` in YAML frontmatter format

**3.5 Wiki Writer**
- Generates markdown matching existing format:
  ```markdown
  ---
  title: "Entity Name"
  type: entity
  created: "2026-06-06"
  source_count: N
  tags: [tag1, tag2]
  aliases: ["alt name"]
  ---
  # Entity Name
  
  ## Definition
  ...
  
  ## Relations
  - [[Related Entity]] — relationship description
  ```
- Updates `wiki/index.md` with new page count

### Error handling
- Failed source ingest → log, skip, continue
- Duplicate content → skip write, log "already exists"

### Input / Output
- **Input:** User query, URL, file path
- **Output:** Updated `wiki/{entities,concepts,sources}/`, updated ChromaDB

---

## 4. Phase 2 — Synthesis Node

### Purpose
Cross-reference all ingested entities and concepts. Detect gaps, resolve contradictions, derive project-specific insights. Write to `wiki/synthesis/`.

### Sub-nodes

**4.1 Gap Analysis Agent**
- Queries ChromaDB across all collections
- Identifies topics where wiki has concepts but no entity (or vice versa)
- Checks coverage against AGENTS.md project spec
- Returns: `missing_topics: list[str]`

**4.2 Conflict Resolver Agent**
- Finds entity/concept pairs with contradictory information
- Resolves using project target spec as ground truth (from AGENTS.md)
- Example: "Orlova airgap=0.5mm vs Bao airgap=0.3mm — project uses 0.5mm, so 0.5mm is canonical"
- Writes resolution to `wiki/synthesis/conflicts.md`

**4.3 Derived Insight Generator**
- Reads all entities/concepts for a given project topic
- Produces condensed synthesis pages
- Example: `wiki/synthesis/synrm-design-rules.md` containing:
  - Barrier spacing ratios from literature
  - Recommended bridge thickness ranges for IE5
  - MTPA angle shift vs saturation relationship

### ChromaDB queries
- `synthesis` collection seeded with synthesis pages
- RAG retrieval across all collections for insight generation

### Input / Output
- **Input:** All wiki pages, ChromaDB indices, AGENTS.md
- **Output:** `wiki/synthesis/` pages, updated ChromaDB `synthesis` collection

---

## 5. Phase 3 — Calculation Node

### Purpose
Take motor ratings (power, speed, torque, voltage) and derive all necessary parameters for .mot file creation. Uses literature-backed formulas and the synthesize knowledge.

### Sub-nodes

**5.1 Fundamental Sizing**
- Given: power, speed, target efficiency
- Calculate: rated torque, estimated losses, thermal budget
- Validate against IE5 thresholds from wiki entity

**5.2 Winding Calculation**
- Read winding derivation from wiki (existing design guide)
- Calculate: effective turns, conductor size, slot fill
- Check slot geometry from .mot file
- Write to `wiki/synthesis/winding.md`

**5.3 Magnetic Circuit Parameters**
- Airgap selection (from project spec: 0.5mm)
- Barrier spacing ratios (from synthesis rules)
- Ld/Lq saliency targets (from literature in wiki)
- Write to `wiki/synthesis/magnetic-params.md`

**5.4 Thermal Constraints**
- Current density limits (from winding temp targets)
- Cooling requirements
- Thermal coupling settings (matching optimize_synrm_v4.py)

### Error handling
- Out-of-range results → clamp with warning
- Missing data → fallback to conservative estimates, log gap
- All calculations stored as structured YAML for audit

### Input / Output
- **Input:** motor_spec dict, wiki synthesis pages
- **Output:** winding_params, barrier_params, wiki/synthesis/*.md

---

## 6. Phase 4 — Design & Optimization Node

### Purpose
Create, read, modify, and optimize .mot files via PyMotorCAD. The heaviest phase, matching the existing `optimize_synrm_v4.py` workflow.

### Sub-nodes

**6.1 .mot File Explorer**
- Load `.mot` file via PyMotorCAD or parse as INI
- Get all section → parameter mappings
- Cache section-parameter relationships in ChromaDB for RAG
- Discover variable names via `mc.get_variable_names()`

**6.2 Variable Discovery Agent**
- Matches PyMotorCAD variable names to wiki parameter names
- Builds a lookup table for agents: `{wiki_name → pymotorcad_variable}`
- Follows AGENTS.md Rule 1: always discover before first use
- Stores in ChromaDB `pymotorcad_vars` collection

**6.3 Parameter Setting Agent**
- Takes calculation outputs from Phase 3
- Calls `mc.set_variable()` / `mc.set_array_variable()`
- Validates with `check_constraints()` from optimize_synrm_v4.py
- Saves backups before changes (AGENTS.md Rule 4)

**6.4 Optimization Engine**
- Spawns child processes matching the script's multiprocessing pattern
- Allocates 1 Motor-CAD instance per evaluation
- Implements Ibrahim et al. strategy:
  1. Latin Hypercube Sampling of barrier geometry
  2. Pareto selection (torque vs torque ripple)
  3. Saliency ratio (Ld-Lq) evaluation on top-5
  4. PhaseAdvance sweep
  5. Optional PM-assisted study
- Logs all results to CSV
- Saves best model to `best_so_far.mot`

**6.5 Result Logger**
- Writes optimization history to `wiki/synthesis/optimization-log.md`
- Updates CSV with all result fields (matching CSV_FIELDS from script)
- Generates summary: best params, comparison to baseline

### Process isolation
- Each FEA evaluation in its own `multiprocessing.Process` with timeout
- Timeout kills hung solves (matching `run_candidate_with_timeout`)
- Non-blocking: main graph continues while evaluations run

### Input / Output
- **Input:** barrier_params, winding_params, motor_spec
- **Output:** optimized .mot file, CSV results, wiki/synthesis/optimization-log.md

---

## 7. Knowledge Layer Detail

### 7.1 Obsidian Wiki Structure

```
wiki/
├── index.md              # master index with counts
├── log.md                # activity log
├── entities/
│   ├── synrm.md          # motor entity
│   ├── ie5-efficiency-class.md
│   ├── gamak-electric-motors.md
│   └── ...               # 8 entities
├── concepts/
│   ├── saliency-ratio.md
│   ├── rotor-flux-barrier-optimization.md
│   ├── mtpa.md
│   └── ...               # 8 concepts
├── sources/
│   ├── 2026-06-05_common-stator-suli.md
│   ├── 2026-06-05_45kw-ie5-design-guide.md
│   └── ...               # 4 sources
├── synthesis/            # ← populated by agents
│   ├── conflicts.md
│   ├── winding.md
│   ├── magnetic-params.md
│   └── optimization-log.md
└── queries/              # ← populated by agent queries to wiki
```

### 7.2 ChromaDB Collections

| Collection | Content | Chunk size | Used by |
|---|---|---|---|
| `sources` | Raw source chunks | 500 char | Research phase |
| `entities` | Entity page embeddings | page-level | Research, Synthesis |
| `concepts` | Concept page embeddings | page-level | Research, Synthesis, Calculate |
| `synthesis` | Synthesis page embeddings | page-level | Calculate, Design |
| `pymotorcad_vars` | Variable name lookup | per-variable | Design phase |

### 7.3 ChromaDB Query Patterns

```python
# Research: find entities related to a query
related = chroma_collection.query(
    query_texts=[topic],
    n_results=5,
    filter={"type": "entity"}
)

# Calculate: retrieve synthesis rules for calculation
rules = chroma_collection.query(
    query_texts=[f"winding calculation {motor_spec}"],
    n_results=3,
    filter={"collection": "synthesis"}
)

# Design: find Motor-CAD variable names
var_lookup = chroma_collection.query(
    query_texts=[f"parameter: {wiki_param_name}"],
    n_results=1,
    filter={"collection": "pymotorcad_vars"}
)
```

---

## 8. Model Layer — OpenRouter

Default model assignments per node:

| Node | Model | Rationale |
|---|---|---|
| All (default) | `openrouter/qwen-qwq-32b` | Fast, cheap, strong reasoning |
| Research extract | `openrouter/qwen-qwq-32b` | High throughput |
| Synthesis | `openrouter/anthropic/claude-sonnet-4-5` | Deep cross-referencing |
| Calculate | `openrouter/google/gemini-2.5-pro` | Numerical precision |
| Design critical | `openrouter/anthropic/claude-opus-4` | High-stakes geometry decisions |
| Optimization | N/A | Spawns PyMotorCAD directly |

The `openai` library with OpenRouter base URL is used for all LLM calls, making model switching a config change.

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Per-node model selection
MODEL_CONFIG = {
    "research":  "openrouter/qwen-qwq-32b",
    "synthesis": "openrouter/anthropic/claude-sonnet-4-5",
    "calculate": "openrouter/google/gemini-2.5-pro",
    "design":    "openrouter/anthropic/claude-opus-4",
}
```

---

## 9. Error Handling & Resilience

### Per-node strategy
```
1. Timeout wrapper (default 120s per LLM call, 300s per FEA solve)
2. Retry with exponential backoff (max 2 retries for transient failures)
3. Fallback path if all retries exhausted:
   - Skip node, mark phase_status[phase] = "failed"
   - Use conservative defaults for missing data
   - Log to error_log dict in state
4. Checkpoint state before each phase node (LangGraph checkpoint)
```

### Graceful degradation
- If research fails → use existing wiki content
- If calculation fails → use AGENTS.md parameter defaults
- If optimization fails → return baseline model with warning
- If PyMotorCAD unavailable → run in "design-only" mode (no FEA)

### State persistence
- LangGraph `MemorySaver` checkpoints state after each phase
- `best_so_far.mot` always holds the last valid design
- CSV log is append-only, never overwritten

---

## 10. Implementation Sequence

### Build order (matching decomposition from brainstorming):

1. **Agent scaffold** — LangGraph state machine, phase stubs, ChromaDB setup
2. **Phase 1: Research** — Web ingest, chunking, entity extraction, wiki writing
3. **Phase 3: Calculation** — Sizing, winding, magnetic parameter derivation
4. **Phase 4: Design** — .mot explorer, variable discovery, parameter setting
5. **Phase 4: Optimization** — LHS, Pareto, PA sweep (wrapping script)
6. **Phase 2: Synthesis** — Gap analysis, conflict resolution
7. **Integration** — Full pipeline run, error handling hardening

---

## 11. Existing Assets That Map Directly

| Existing file | Used in |
|---|---|
| `optimize_synrm_v4.py` (LHS → Nelder-Mead → PA → verify) | Phase 4 reference implementation |
| `AGENTS.md` (specs, constraints, anti-hallucination rules) | All phases — ground truth |
| `wiki/` (22 entity/concept/source pages) | Phase 1 output + Phase 2 input |
| Prototype LangGraph agent (rewrite → route → retrieve → agent) | Phase 4 .mot RAG pattern |
| `SynRM_45kW_IE5.mot` | Phase 4 input model |
