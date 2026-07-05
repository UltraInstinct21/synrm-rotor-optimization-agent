# Design: LangGraph State Machine for motor-deepagent

**Date:** 2026-07-06
**Status:** Approved
**Author:** Claude (brainstorming session)

---

## 1. Overview

Replace the ad-hoc `run_request()` dispatch with a proper LangGraph `StateGraph` — explicit nodes, edges, and conditional routing. This enables:

- **Human-in-the-loop interrupts** before Motor-CAD parameter changes
- **Real-time streaming** of tokens and progress
- **Persistent state** via checkpointers for resumable experiments

---

## 2. Graph Architecture

```
User Request
     │
     ▼
┌─────────────┐
│  classify   │ ← keyword heuristic + LLM refinement
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   route     │ ← conditional edges per category
└──────┬──────┘
       │
  ┌────┼────┬────────┐
  ▼    ▼    ▼        ▼
┌────┐┌────┐┌──────┐┌─────────┐
│code││wiki││research││experiment│
└─┬──┘└─┬──┘└──┬───┘└────┬────┘
  │     │      │          │
  └─────┴──────┴──────────┘
              │
              ▼
       ┌─────────────┐
       │  synthesize  │
       └──────┬──────┘
              │
              ▼
         Final Output
```

### State Channels

```python
class MotorState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    category: str
    delegations: dict[str, Any]
    active_agent: str
    pending_changes: Optional[dict]  # For HITL approval
    last_checkpoint: Optional[str]   # Motor-CAD save state
```

---

## 3. Human-in-the-Loop Interrupts

### When to Interrupt

| Action | Trigger | Decision Types |
|--------|---------|----------------|
| Motor parameter write | `set_parameters()` called | approve / reject / edit |
| `.mot` file save | Before `save_checkpoint()` | approve / reject |
| Wiki page overwrite | `write_file()` on wiki/*.md | approve / reject |
| Shell execution | `run_shell()` with destructive cmds | approve / reject |

### Implementation

```python
from langgraph.types import interrupt, Command

def execute_motor_change(state: MotorState) -> Command[Literal["proceed", "cancel"]]:
    """Interrupt before motor parameter changes for human approval."""
    decision = interrupt({
        "question": "Approve motor parameter change?",
        "parameters": state["pending_changes"],
        "checkpoint": state["last_checkpoint"],
    })
    
    if decision:
        return Command(goto="proceed")
    else:
        return Command(goto="cancel")
```

### TUI Integration

- Interrupt fires → TUI shows approval card with parameter diff
- User presses `Y`/`N` or edits values before approving
- Resume via `Command(resume=True)` or `Command(resume={"edited_params": ...})`

---

## 4. Streaming & Progress

### What Streams

1. **Token-by-token** — LLM responses appear in real-time
2. **Tool calls** — Show which tool is being called and its args
3. **Subagent progress** — Stream internal steps when delegating
4. **Motor-CAD status** — Show FEA simulation progress if available

### Implementation

```python
# In TUI, wrap graph invocation with stream_events
for chunk in graph.stream_events(
    {"messages": [HumanMessage(content=request)]},
    config=config,
    version="v3",
):
    if chunk["type"] == "messages":
        token, metadata = chunk["data"]
        if isinstance(token, AIMessageChunk):
            yield token.text  # Stream to TUI chat pane
    elif chunk["type"] == "updates":
        for source, update in chunk["data"].items():
            if source == "__interrupt__":
                yield InterruptCard(update)  # Show approval UI
            elif "motor_cad" in str(update):
                yield ProgressUpdate(update)  # Show simulation status
```

### TUI Changes

- Chat pane shows streaming tokens with cursor
- Status bar shows "Researching..." / "Running FEA..." / "Awaiting approval..."
- New "Progress" tab for multi-step operations (optional)

---

## 5. Memory & Persistence

### Short-Term (Per-Thread)

- `InMemorySaver` checkpointer for conversation continuity
- Enables resuming interrupted experiments
- Thread ID tied to session

### Long-Term (Cross-Thread)

- `InMemoryStore` for motor knowledge (papers, experiment history)
- Namespaces: `(project_id, "motor_knowledge")`, `(project_id, "experiments")`
- Semantic search via embeddings for "find similar past experiments"

### Implementation

```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = InMemorySaver()
store = InMemoryStore()

graph = builder.compile(checkpointer=checkpointer, store=store)
```

---

## 6. Migration Path

### Phase1: Core Graph (Week1)

- [ ] Create `src/agent/graph.py` with `StateGraph` definition
- [ ] Implement `classify`, `route`, `synthesize` nodes
- [ ] Wrap existing subagent runners as graph nodes
- [ ] Add `InMemorySaver` checkpointer

### Phase2: HITL Interrupts (Week2)

- [ ] Add `interrupt()` calls before motor writes
- [ ] Create `InterruptCard` TUI widget
- [ ] Wire resume logic in `InteractiveSession`

### Phase3: Streaming (Week3)

- [ ] Replace `Runner.run()` with `graph.stream_events()`
- [ ] Update TUI to consume stream chunks
- [ ] Add progress indicators

### Phase4: Long-Term Memory (Week4)

- [ ] Add `InMotorStore` for experiment history
- [ ] Create embedding index for motor papers
- [ ] Add "find similar" tool

---

## 7. Dependencies

```toml
# Add to pyproject.toml
langgraph = ">=0.4.0"
langchain-core = ">=0.3.0"
langchain-openai = ">=0.2.0"  # For embeddings (if using OpenAI-compatible)
```

---

## 8. Success Criteria

- [ ] All existing tests pass after migration
- [ ] Streaming works in TUI (tokens appear in real-time)
- [ ] HITL interrupts fire before motor writes
- [ ] Interrupted experiments can be resumed
- [ ] Long-term memory stores experiment results

---

## 9. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| LangGraph API changes | High | Pin versions, wrap with adapter |
| Streaming performance | Medium | Buffer tokens, batch updates |
| Checkpointer memory usage | Low | Use `InMemorySaver` (clears on restart) |
| HITL UX confusion | Medium | Clear approval cards, help text |
