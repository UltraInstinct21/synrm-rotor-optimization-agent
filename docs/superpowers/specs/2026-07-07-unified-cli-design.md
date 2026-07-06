# Motor-DeepAgent Unified CLI Design

**Date:** 2026-07-07
**Status:** Approved
**Replaces:** `apps/cli/` (basic REPL) and `apps/tui/` (Textual TUI)

---

## Goal

Build a Claude Code / OpenCode style terminal CLI that replaces the existing TUI and basic REPL. Single unified interface with live streaming, slash commands, and all subsystems (chat, wiki, motor, research, run, memory) accessible from one prompt.

## Architecture

**Approach:** Command Module Pattern — core REPL loop dispatches to separate command handler modules.

**Framework:** Rich (rendering) + prompt_toolkit (input/prompt)

### File Structure

```
apps/cli/
├── __init__.py
├── app.py              # REPL loop, prompt_toolkit setup, command dispatch
├── commands/
│   ├── __init__.py     # register_all() — imports & registers all command groups
│   ├── chat.py         # Default handler (no /prefix) — agent chat via graph
│   ├── wiki.py         # /wiki list|read|search|update
│   ├── motor.py        # /motor status|launch|load|run|extract|set|sweep|close
│   ├── research.py     # /research <query>
│   ├── run.py          # /run <script>|sweep
│   ├── memory.py       # /memory store|search|list|forget
│   └── system.py       # /help, /clear, /compact, /model, /status, /quit
├── rendering.py        # Rich console, panels, markdown, tables, code blocks
├── streaming.py        # Token stream handler, spinner, live display
└── session.py          # Session state, persistence, conversation history
```

### Entry Point

```
python -m apps.cli              # REPL mode
python -m apps.cli "request"    # Single-shot mode (backwards compatible)
```

## Core REPL (app.py)

### Layout

```
┌──────────────────────────────────────────────────────────┐
│  motor-deepagent v0.1.0                    model: flash  │
├──────────────────────────────────────────────────────────┤
│  > optimize the rotor barriers for max torque            │
│                                                          │
│  ┌─ classify ─────────────────────────────────────────┐  │
│  │ 📂 experiment                                       │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌─ execute_experiment ───────────────────────────────┐  │
│  │ Running optimization sweep across 12 parameters...  │  │
│  │ ████████████████████████░░░░░░ 72%  [3m 22s]       │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  ┌─ synthesis ────────────────────────────────────────┐  │
│  │ Best result: 148.2 Nm torque, 96.3% efficiency,    │  │
│  │ PF 0.87. Barrier L1=92mm, L2=138mm, L3=178mm.      │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  > _                                                     │
├──────────────────────────────────────────────────────────┤
│  /help  /wiki  /motor  /research  /clear  Ctrl-C exit    │
└──────────────────────────────────────────────────────────┘
```

### Input Behavior

- **Enter** sends the message
- **Shift+Enter** inserts newline (multi-line input)
- **Up/Down arrows** cycle through command history
- **Tab** autocomplete for slash commands
- **Ctrl-C** cancels current generation (not exit)
- **Ctrl-D** or `/quit` exits

### Command Dispatch

```python
# Pseudocode for dispatch logic
def dispatch(user_input: str):
    if user_input.startswith("/"):
        cmd, *args = user_input.split(maxsplit=1)
        handler = commands.get(cmd.lower())
        if handler:
            handler.run(args[0] if args else "")
        else:
            render_error(f"Unknown command: {cmd}. Type /help for available commands.")
    else:
        # Default: chat with agent
        commands["chat"].run(user_input)
```

## Streaming Output (streaming.py + rendering.py)

### Phase Panels

Each phase of graph execution gets a Rich `Panel` with colored border:

| Phase | Border Color | Content |
|-------|-------------|---------|
| classify | cyan | Detected category with icon |
| execute_* | yellow | Progress bar, step count, elapsed time |
| synthesize | green | Final answer (markdown rendered) |
| error | red | Error message with abbreviated traceback |

### Streaming Behavior

1. **Thinking state:** Animated spinner with phase label (`"Classifying..."`, `"Running code agent..."`)
2. **Token streaming:** Live typewriter effect via Rich `Live` display
3. **Progress bars:** For long operations (sweeps, experiments) via `rich.progress`
4. **Markdown rendering:** Code blocks with syntax highlighting, tables, lists
5. **Error rendering:** Red panel with short error message, expandable traceback

### API Path

```
User input
  → run_request_graph_streamed(request, thread_id)
  → yields {"type": "category", "data": "experiment"}
      → render classify panel
  → yields {"type": "info", "data": "...", "label": "execute_experiment"}
      → render execute panel with progress
  → yields {"type": "synthesis", "data": "..."}
      → render synthesis panel (markdown)
```

Reuses existing `run_request_graph_streamed()` from `src/agent/runtime.py`.

## Command Modules

### commands/chat.py — Default Handler

No `/` prefix. Sends input through `run_request_graph_streamed()`. Renders streaming output with phase panels. Maintains conversation context via `thread_id` from session.

### commands/wiki.py — `/wiki`

```
/wiki list              → Rich table of all wiki pages (path, title, size)
/wiki read <page>       → Syntax-highlighted markdown display
/wiki search <query>    → Highlighted search results with context
/wiki update <page>     → Triggers wiki update flow (prompts for content)
```

Reuses: `src/tools/wiki/update_wiki.py` (`list_pages`, `read_page`, `page_summary`, `apply_update_plan`)

### commands/motor.py — `/motor`

```
/motor status                → connection status, loaded model, last analysis
/motor launch                → launch Motor-CAD (shows spinner)
/motor load <model.mot>      → load model file (validates path)
/motor run                   → run magnetic analysis (shows progress)
/motor extract               → extract results → Rich table with all metrics
/motor set <var> <value>     → set parameter with validation + readback
/motor sweep <var>=lo-hi     → parameter sweep with progress bar
                                  Live-updating Rich table showing iteration, params, torque, efficiency.
                                  Final summary with best result highlighted.
/motor close                 → disconnect cleanly
```

Reuses: `src/tools/motorcad/` (`run_motorcad`, `get_results`, `set_parameters`)
State: persistent `mc` instance across commands via session.

### commands/research.py — `/research`

```
/research <query>     → run research subgraph, streaming progress + results
```

Reuses: `src/research/graph.py` (`run_research`)

### commands/run.py — `/run`

```
/run <script.py>           → execute Python script, show output
/run sweep p1=10-20 p2=5   → parameter sweep with progress
```

Reuses: `src/tools/execution/run_script.py` (`run_python_script`)

### commands/memory.py — `/memory`

```
/memory store <key> <value>   → store fact
/memory search <query>        → search memories with highlights
/memory list                  → list all namespaces + counts
/memory forget <key>          → delete with confirmation
```

Reuses: `src/tools/memory/memory_tools.py`

### commands/system.py — System

```
/help    → Rich table of all commands with descriptions
/clear   → clear terminal, preserve session
/compact → LLM summarizes conversation, keeps recent N messages
/model   → show current model, prompt to switch
/status  → session stats: requests, tokens, uptime, model
/quit    → clean exit (save session, close motor if open)
```

## Session Management (session.py)

### State

```python
@dataclass
class Session:
    conversation_id: str        # UUID per session
    thread_id: str              # LangGraph thread for state
    model: str                  # Current LLM model name
    motor_instance: Any         # Persistent Motor-CAD connection (or None)
    stats: SessionStats         # request_count, total_tokens, start_time
    history: list[Message]      # Conversation messages
```

### Persistence

- **Session file:** `.motor-deepagent/session.json` — conversation_id, model, last_active, stats
- **History:** `.motor-deepagent/history/{conversation_id}.jsonl` — one JSON object per message
- **On startup:** prompt to resume last session or start fresh

### Context Management

- Messages stored in memory during session
- `/compact` summarizes older messages via LLM, keeps recent N
- Auto-compact when context exceeds threshold (configurable)

## Reused Components

| Component | Source | Reused As |
|-----------|--------|-----------|
| LangGraph streaming | `src/agent/runtime.py` | `run_request_graph_streamed()` |
| Wiki tools | `src/tools/wiki/` | Direct function calls |
| Motor-CAD tools | `src/tools/motorcad/` | Direct function calls |
| Research graph | `src/research/graph.py` | `run_research()` |
| Script execution | `src/tools/execution/` | `run_python_script()` |
| Memory tools | `src/tools/memory/` | Direct function calls |
| Filesystem tools | `src/tools/filesys/` | Available to agent subagents |
| Event stream | `src/agent/event_stream.py` | For progress updates |

## Replaced Components

| Old | New | Notes |
|-----|-----|-------|
| `apps/cli/main.py` | `apps/cli/app.py` | Complete rewrite |
| `apps/cli/chat.py` | `apps/cli/commands/chat.py` | Integrated into command system |
| `apps/cli/display.py` | `apps/cli/rendering.py` | Rich-based rendering |
| `apps/tui/app.py` | `apps/cli/commands/*.py` | All 5 tabs become slash commands |

## Error Handling

- **Unknown command:** Red error message with suggestion to type `/help`
- **Missing args:** Usage hint with example (e.g., `Usage: /wiki read <page>`)
- **Motor-CAD not connected:** Clear message to run `/motor launch` first
- **LLM errors:** Retry once, then show error panel with raw message
- **KeyboardInterrupt:** Cancel current generation, return to prompt
- **Session corruption:** Fall back to fresh session, log warning

## Testing

- Unit tests for each command module (mock tools/runtime)
- Integration test for REPL dispatch loop
- Test streaming output rendering with mock events
- Test session persistence (save/load/compact)

## Success Criteria

1. `python -m apps.cli` launches interactive REPL with Rich rendering
2. Live streaming of agent responses with phase panels
3. All `/wiki`, `/motor`, `/research`, `/run`, `/memory` commands work
4. `/help` shows complete command reference
5. Session persists across restarts
6. Motor-CAD connection maintained across `/motor` commands
7. `/compact` reduces conversation context
8. Clean error messages for all failure modes
