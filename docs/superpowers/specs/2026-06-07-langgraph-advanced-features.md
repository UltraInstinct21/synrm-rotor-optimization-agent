# LangGraph Advanced Features for SynRM Pipeline

**Date:** 2026-06-07
**Status:** Draft
**Goal:** Add streaming, map-reduce fan-out, human-in-the-loop, and long-term memory to the existing 4-phase SynRM pipeline.

---

## 1. Streaming

**What:** Stream graph execution events for real-time UX.

**Changes:**
- `run_pipeline.py`: Use `graph.stream(state, config, stream_mode="updates")` instead of `graph.invoke()`. Stream events to console with phase labels.
- No changes to `graph.py` — streaming is an invocation concern.

**Stream modes used:**
- `stream_mode="updates"` — emit per-node state diffs as each node completes
- Optional: `stream_mode="custom"` for LLM token events from research/synthesis nodes

**UX:**
```
[research]   Searching web for SynRM design principles... done
[synthesis]  Cross-referencing 12 entities, detecting gaps... done
[calculate]  Computing winding params... done
[design]     Parsing .mot... discovering variables... running optimization...
  iteration 1/10: T=98.2 Nm, E=94.1%
  iteration 2/10: T=101.5 Nm, E=94.5%
  ...
[design]     done → best model: SynRM_45kW_IE5_best.mot
```

---

## 2. Map-Reduce (Parallel Fan-Out)

**What:** Parallel sub-tasks within nodes using `Send()` API.

### 2a. Research — parallel sub-queries

Split the research query into 3 sub-topics, search each in parallel, merge results.

```
                      ┌─ sub_search("barrier rotor geometry")
Send("research") ─────┼─ sub_search("winding configuration") ── merged_results
                      └─ sub_search("magnetic material selection")
```

**Changes:**
- `agent/graph.py`: Replace single research node with a map-reduce sub-graph:
  - `research_mapper` — splits query into sub-topics, `Send()` to parallel searcher nodes
  - `research_reducer` — merges results, runs entity extraction
- `run_pipeline.py`: Must handle sub-graph streaming

### 2b. Optimization — parallel candidate evaluation

Send each LHS candidate to a separate evaluation node.

```
                        ┌─ eval_candidate(candidate_0)
                        ├─ eval_candidate(candidate_1)
Send("optimization") ───┼─ eval_candidate(candidate_2) ── collect → select best
                        ├─ ...
                        └─ eval_candidate(candidate_N)
```

**Changes:**
- `agent/graph.py`: Similar map-reduce sub-graph for optimization phase
- `agent/nodes/optimization.py`: Extract `evaluate_single(candidate) -> result` function
- LangGraph Node: `optimization_dispatcher` sends N `Send()` calls to `eval_candidate` node, then `optimization_collector` merges

### Scope note

Map-reduce is optional for MVP. Start with optimization fan-out (biggest speed gain), add research fan-out later.

---

## 3. Human-in-the-Loop (HITL)

**What:** Pause execution before critical actions, wait for user approval, resume.

**Interrupt points:**
1. **Before optimization** — show user the barrier params + candidate count, ask to proceed
2. **Before wiki write** — show synthesized content, ask to approve

**Changes:**
- `agent/graph.py`: Add `interrupt_before=["design"]` to `compile()`. No — use `interrupt_before=["optimization_approval"]` where `optimization_approval` is a new no-op node that just pauses.
- `run_pipeline.py`: After `stream()`, check for interrupts. Display approval prompt. Call `graph.invoke(Command(resume=answer), config)` to resume.

**Flow:**
```
1. Pipeline runs through research → synthesis → calculate
2. Hits "optimization_approval" node → pauses
3. User sees: "Run optimization with these params? L1_Dia=78, L2_Dia=92, bridges=1.2mm [y/N]"
4. User says "y" → pipeline resumes with Command(resume="proceed")
5. User says "n" → pipeline resumes with Command(resume="skip") → optimization skipped, design marked degraded
```

**Cleanup:** If user skips, set `phase_status.design = {status: "skipped"}` and route to END via existing router.

---

## 4. Long-Term Memory (Cross-Session Store)

**What:** `MemoryStore` from `langgraph.store` for persisting structured data across runs.

**Schema:**

```python
# memory namespaces:
# ( "synrm", "optimization_results" )  ← per-spec best params
# ( "synrm", "motor_specs" )           ← known motor spec → best params

# Item structure for optimization_results:
{
  "power_kw": 45,
  "speed_rpm": 3000,
  "poles": 4,
  "best_params": {"L1_Diameter": 78, "L2_Diameter": 92, ...},
  "best_efficiency": 96.2,
  "run_count": 12,
  "last_run": "2026-06-07T10:30:00",
}
```

**Changes:**
- `agent/graph.py`: Add `store=MemoryStore()` to `compile()`. Add `put()` after optimization completes, `get()` at design start to seed params.
- New file `agent/memory.py` — helper functions: `save_optimization_result(store, spec, params, results)`, `load_best_params(store, spec) -> dict | None`
- `run_pipeline.py`: Pass `store` in config

**Data flow:**
1. Design node starts → queries memory for best params matching this motor spec
2. If found → seeds `barrier_params` with remembered values (skips calculate defaults)
3. Optimization runs → stores results back to memory
4. Future runs start with better initial params → fewer iterations needed

---

## Integration Summary

### Files Changed

| File | Streaming | Map-Reduce | HITL | Memory |
|------|-----------|------------|------|--------|
| `agent/graph.py` | — | Sub-graphs for research + optimization | `interrupt_before`, approval node | `store=` param, memory queries |
| `agent/nodes/optimization.py` | — | `evaluate_single()` extracted | — | — |
| `agent/memory.py` (new) | — | — | — | Store helpers |
| `run_pipeline.py` | `stream()` loop | Sub-graph streaming | Interrupt handling, `Command(resume=...)` | Pass store config |

### Dependency Order

1. **Memory** first (independent, no deps) — create `agent/memory.py`
2. **Streaming** second (changes `run_pipeline.py` only)
3. **HITL** third (adds interrupt to graph + resume to run_pipeline)
4. **Map-Reduce** last (touches graph + nodes, biggest change)

### Error Handling

- Streaming: silent fallback to `invoke()` if stream fails (graceful degradation)
- Map-Reduce: failed parallel branches produce `null` in result array — filter with `.filter(Boolean)` before merge
- HITL: timeout on interrupt → auto-resume with "skip" after 5 min
- Memory: `MemoryStore` save failure is non-fatal (log warning, continue)

---

## Testing

- Streaming: compare output of `stream()` vs `invoke()` — same final state
- Map-Reduce: verify all Send() targets complete, merged result contains all candidates
- HITL: simulate resume with "proceed" and "skip", verify state transitions
- Memory: write + read round-trip, cross-session persistence
