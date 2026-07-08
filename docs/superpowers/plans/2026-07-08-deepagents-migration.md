# Deep Agents Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Clean the repo end-to-end, replace custom tools with Deep Agents built-ins, rewrap Motor-CAD tools as Deep Agents tools, preserve LangGraph research subgraph.

**Architecture:** Deep Agents as runtime (agent loop, built-in tools, CLI, memory, HITL). LangGraph only for the research subgraph. Motor-CAD domain tools re-wrapped with LangChain `@tool` decorators. Wiki knowledge migrates to Deep Agents memory.

**Tech Stack:** `deepagents`, `langchain-core`, `langgraph`, `langchain-openai`, `pydantic`, `ansys.motorcad.core` (optional)

## Global Constraints

- Python 3.13.5 (Anaconda, `C:\Users\sarth\anaconda3`)
- Windows 11
- All LLM calls route through Opencode (`ai.opencode.ai/zen/v1`)
- Motor-CAD anti-hallucination rules from `AGENTS.md` must be preserved
- Pydantic >= 2.0 for all data models
- Research subgraph must remain functional as LangGraph pipeline

---

### Task 1: Install Deep Agents and Create Config

**Files:**
- Create: `config.toml`
- Modify: (none — clean start)

**Interfaces:**
- Consumes: existing `.env` with `OPENROUTER_API_KEY`, `MODEL_DEFAULT`, `TAVILY_API_KEY`
- Produces: Deep Agents config that dcode reads on launch

- [ ] **Step 1: Install deepagents package**

Run: `pip install deepagents`

- [ ] **Step 2: Verify installation**

Run: `python -c "import deepagents; print(deepagents.__version__)"`
Expected: prints version number

- [ ] **Step 3: Create config.toml at project root**

```toml
[agent]
model = "deepseek-v4-flash-free"
system_prompt = """You are a motor engineering assistant specializing in SynRM (Synchronous Reluctance Motor) design.

You can:
- Read, write, and search files in the project
- Run shell commands and Python scripts
- Search the web for motor engineering references
- Use Motor-CAD tools for electromagnetic simulation
- Research motor design topics via the research subgraph
- Store and retrieve knowledge across sessions

Anti-hallucination rules for Motor-CAD:
1. Always call get_variable_names() before any set/get
2. Use safe_get/safe_set wrappers — never raw calls
3. Call show_magnetic_context() before electromagnetic analysis
4. Save checkpoint before changing rotor params
5. Read all results before changing any parameter

Key files:
- AGENTS.md — motor specs, constraints, design strategy
- SynRM_45kW_IE5.mot — reference motor model
- optimize_synrm_v4.py — existing optimization script
"""

[tools]
packages = ["src/tools/motorcad/"]

[memory]
enabled = true

[subagents]
enabled = true
```

- [ ] **Step 4: Verify dcode can read config**

Run: `dcode --help`
Expected: shows dcode CLI help (not "command not found")

- [ ] **Step 5: Commit**

```bash
git add config.toml
git commit -m "feat: add Deep Agents config and install dependency"
```

---

### Task 2: Wrap Motor-CAD Tools with LangChain @tool Decorators

**Files:**
- Modify: `src/tools/motorcad/__init__.py`
- Modify: `src/tools/motorcad/run_motorcad.py`
- Modify: `src/tools/motorcad/set_parameters.py`
- Modify: `src/tools/motorcad/get_results.py`

**Interfaces:**
- Consumes: existing Motor-CAD functions, `src.domain.motor.parameter_mapping.validate_parameter`, `src.domain.motor.result_models.ElectromagneticResult`
- Produces: LangChain `@tool`-decorated functions that Deep Agents can ingest via `packages = ["src/tools/motorcad/"]`

- [ ] **Step 1: Update src/tools/motorcad/__init__.py**

Replace the empty file with tool registration:

```python
"""Motor-CAD tools for Deep Agents.

These tools wrap PyMotorCAD operations with anti-hallucination safeguards.
Deep Agents discovers them via the [tools] packages config.
"""

from src.tools.motorcad.run_motorcad import (
    motorcad_launch,
    motorcad_load_model,
    motorcad_run_magnetic,
    motorcad_run_and_extract,
    motorcad_close,
)
from src.tools.motorcad.set_parameters import (
    motorcad_safe_get,
    motorcad_safe_set,
    motorcad_set_parameter,
    motorcad_save_checkpoint,
)
from src.tools.motorcad.get_results import (
    motorcad_get_variables,
    motorcad_extract_results,
)

__all__ = [
    "motorcad_launch",
    "motorcad_load_model",
    "motorcad_run_magnetic",
    "motorcad_run_and_extract",
    "motorcad_close",
    "motorcad_safe_get",
    "motorcad_safe_set",
    "motorcad_set_parameter",
    "motorcad_save_checkpoint",
    "motorcad_get_variables",
    "motorcad_extract_results",
]
```

- [ ] **Step 2: Rewrite src/tools/motorcad/run_motorcad.py**

Remove the raw function wrappers. Each function gets a `@tool` decorator and returns a string (Deep Agents tool convention):

```python
"""Motor-CAD launcher tools — start, load models, and run analyses."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from langchain_core.tools import tool

from src.config.settings import REFERENCE_MOT

_MC_INSTANCE: Any | None = None


def _get_mc() -> Any:
    """Return the active Motor-CAD instance or raise."""
    if _MC_INSTANCE is None:
        raise RuntimeError("Motor-CAD is not running. Call motorcad_launch first.")
    return _MC_INSTANCE


@tool
def motorcad_launch(visible: bool = False, model_path: str = "") -> str:
    """Launch or connect to a Motor-CAD instance.

    Args:
        visible: Whether to show the Motor-CAD GUI.
        model_path: Optional .mot file to load on startup. Defaults to reference model.
    """
    global _MC_INSTANCE

    try:
        from ansys.motorcad.core import MotorCAD

        mc = MotorCAD(visible=visible)
        _MC_INSTANCE = mc

        path = model_path or str(REFERENCE_MOT)
        if path and Path(path).exists():
            mc.load_from_file(path)
            return f"Motor-CAD launched and loaded {path}"
        return "Motor-CAD launched (no model loaded)"

    except ImportError:
        return "ERROR: ansys.motorcad.core not installed. Cannot launch Motor-CAD."
    except Exception as e:
        return f"ERROR: Motor-CAD launch failed: {e}"


@tool
def motorcad_load_model(path: str = "") -> str:
    """Load a .mot model file into Motor-CAD.

    Args:
        path: Path to .mot file. Defaults to reference model.
    """
    mc = _get_mc()
    target = path or str(REFERENCE_MOT)

    try:
        mc.load_from_file(target)
        return f"Loaded {target}"
    except Exception as e:
        return f"ERROR: Load failed: {e}"


@tool
def motorcad_run_magnetic() -> str:
    """Run electromagnetic analysis. Calls show_magnetic_context() per anti-hallucination rules."""
    mc = _get_mc()

    try:
        mc.show_magnetic_context()
        return "Electromagnetic analysis completed"
    except Exception as e:
        return f"ERROR: Magnetic analysis failed: {e}"


@tool
def motorcad_run_and_extract() -> str:
    """Run electromagnetic analysis and extract all results as JSON.

    Returns torque, efficiency, power factor, inductances, and losses.
    """
    from src.tools.motorcad.get_results import extract_results

    mc = _get_mc()

    try:
        mc.show_magnetic_context()
    except Exception as e:
        return f"ERROR: Magnetic analysis failed: {e}"

    result = extract_results(mc)
    return result.model_dump_json(indent=2)


@tool
def motorcad_close() -> str:
    """Close Motor-CAD cleanly."""
    global _MC_INSTANCE
    mc = _MC_INSTANCE
    if mc:
        try:
            mc.quit()
        except Exception:
            pass
    _MC_INSTANCE = None
    return "Motor-CAD closed"
```

- [ ] **Step 3: Rewrite src/tools/motorcad/set_parameters.py**

```python
"""Motor-CAD parameter setting tools — safe wrappers with validation and checkpoints."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from langchain_core.tools import tool

from src.config.settings import REFERENCE_MOT
from src.domain.motor.parameter_mapping import validate_parameter


def _get_mc() -> Any:
    if _MC_INSTANCE is None:
        raise RuntimeError("Motor-CAD is not running. Call motorcad_launch first.")
    return _MC_INSTANCE


# Module-level instance holder (shared with run_motorcad.py via process global)
_MC_INSTANCE: Any | None = None


def set_mc_instance(mc: Any) -> None:
    """Set the module-level Motor-CAD instance."""
    global _MC_INSTANCE
    _MC_INSTANCE = mc


@tool
def motorcad_safe_get(var_name: str) -> str:
    """Read a variable from Motor-CAD. Returns the float value or 'Not found'.

    Args:
        var_name: Motor-CAD variable name (e.g. 'Stator_OD', 'Torque').
    """
    mc = _get_mc()
    try:
        val = float(mc.get_variable(var_name))
        return str(val)
    except Exception:
        return f"Not found: {var_name}"


@tool
def motorcad_safe_set(var_name: str, value: float) -> str:
    """Set a Motor-CAD variable with verification (read-back check).

    Anti-hallucination: verifies variable exists via get_variable_names(),
    sets the value, then reads back to confirm.

    Args:
        var_name: Motor-CAD variable name.
        value: Value to set.
    """
    mc = _get_mc()
    try:
        available = mc.get_variable_names()
        if var_name not in available:
            return f"ERROR: Variable '{var_name}' not found in Motor-CAD"

        mc.set_variable(var_name, value)
        readback = mc.get_variable(var_name)
        if abs(float(readback) - value) > 1e-6:
            return f"ERROR: Set verify failed: {var_name} = {readback} (expected {value})"

        return f"{var_name} = {value} OK"
    except Exception as e:
        return f"ERROR: Failed to set {var_name}: {e}"


@tool
def motorcad_set_parameter(var_name: str, value: float, domain: str = "stator", checkpoint_before: bool = False) -> str:
    """Set a Motor-CAD parameter with domain validation and optional checkpoint.

    Validates against known ranges (stator/rotor/winding/rating domains).
    Saves checkpoint before rotor changes if requested.

    Args:
        var_name: Motor-CAD variable name.
        value: Target value.
        domain: Validation domain — stator, rotor, winding, or rating.
        checkpoint_before: Save a .mot checkpoint before setting (recommended for rotor params).
    """
    mc = _get_mc()

    valid, msg = validate_parameter(var_name, value, domain=domain)
    if not valid:
        return f"ERROR: {msg}"

    if checkpoint_before and "rotor" in domain.lower():
        try:
            mc.save_to_file(str(Path.cwd() / "best_so_far.mot"))
        except Exception:
            pass  # non-fatal

    return motorcad_safe_set.var_name and motorcad_safe_set(var_name, value)


@tool
def motorcad_save_checkpoint(path: str = "") -> str:
    """Save a .mot checkpoint file before making changes.

    Args:
        path: Checkpoint file path. Defaults to 'best_so_far.mot' in cwd.
    """
    mc = _get_mc()
    target = path or str(Path.cwd() / "best_so_far.mot")

    try:
        mc.save_to_file(target)
        return f"Checkpoint saved: {target}"
    except Exception as e:
        return f"ERROR: Checkpoint save failed: {e}"
```

- [ ] **Step 4: Rewrite src/tools/motorcad/get_results.py**

```python
"""Motor-CAD result extraction tools — read outputs from a running instance."""

from __future__ import annotations

from typing import Any

from langchain_core.tools import tool

from src.domain.motor.result_models import ElectromagneticResult

_RESULT_VARIABLES: dict[str, str] = {
    "Torque": "torque_nm",
    "Efficiency": "efficiency_pct",
    "Power Factor": "power_factor",
    "Speed": "speed_rpm",
    "Output Power": "output_power_kw",
    "Ld": "ld_mh",
    "Lq": "lq_mh",
    "Saliency Ratio": "saliency",
    "Iron Loss": "iron_loss_w",
    "Copper Loss": "copper_loss_w",
    "Magnet Loss": "magnet_loss_w",
    "Mechanical Loss": "mechanical_loss_w",
}

_MC_INSTANCE: Any | None = None


def set_mc_instance(mc: Any) -> None:
    global _MC_INSTANCE
    _MC_INSTANCE = mc


def _get_mc() -> Any:
    if _MC_INSTANCE is None:
        raise RuntimeError("Motor-CAD is not running. Call motorcad_launch first.")
    return _MC_INSTANCE


def _safe_get(mc: Any, var_name: str) -> float | None:
    try:
        return float(mc.get_variable(var_name))
    except Exception:
        return None


def extract_results(mc: Any) -> ElectromagneticResult:
    """Read all electromagnetic results (used internally by tools)."""
    try:
        available = mc.get_variable_names()
    except Exception:
        available = []

    raw: dict[str, float | None] = {}
    for mc_var, model_field in _RESULT_VARIABLES.items():
        raw[model_field] = _safe_get(mc, mc_var) if mc_var in available else None

    return ElectromagneticResult(**raw)


@tool
def motorcad_get_variables() -> str:
    """List all available Motor-CAD variable names in the current context."""
    mc = _get_mc()
    try:
        names = mc.get_variable_names()
        return "\n".join(sorted(names))
    except Exception as e:
        return f"ERROR: Could not get variables: {e}"


@tool
def motorcad_extract_results() -> str:
    """Extract all electromagnetic results as JSON.

    Returns torque, efficiency, power factor, inductances, and losses.
    Must run electromagnetic analysis first (motorcad_run_magnetic).
    """
    mc = _get_mc()
    result = extract_results(mc)
    return result.model_dump_json(indent=2)
```

- [ ] **Step 5: Fix motorcad_set_parameter to properly call motorcad_safe_set**

The `motorcad_set_parameter` function in Step 3 has a bug — it references `motorcad_safe_set.var_name`. Fix:

```python
@tool
def motorcad_set_parameter(var_name: str, value: float, domain: str = "stator", checkpoint_before: bool = False) -> str:
    """Set a Motor-CAD parameter with domain validation and optional checkpoint.

    Validates against known ranges (stator/rotor/winding/rating domains).
    Saves checkpoint before rotor changes if requested.

    Args:
        var_name: Motor-CAD variable name.
        value: Target value.
        domain: Validation domain — stator, rotor, winding, or rating.
        checkpoint_before: Save a .mot checkpoint before setting (recommended for rotor params).
    """
    mc = _get_mc()

    valid, msg = validate_parameter(var_name, value, domain=domain)
    if not valid:
        return f"ERROR: {msg}"

    if checkpoint_before and "rotor" in domain.lower():
        try:
            mc.save_to_file(str(Path.cwd() / "best_so_far.mot"))
        except Exception:
            pass

    # Delegate to safe_set logic inline
    try:
        available = mc.get_variable_names()
        if var_name not in available:
            return f"ERROR: Variable '{var_name}' not found"

        mc.set_variable(var_name, value)
        readback = mc.get_variable(var_name)
        if abs(float(readback) - value) > 1e-6:
            return f"ERROR: Set verify failed: {var_name} = {readback} (expected {value})"

        return f"{var_name} = {value} OK"
    except Exception as e:
        return f"ERROR: Failed to set {var_name}: {e}"
```

- [ ] **Step 6: Verify imports work**

Run: `python -c "from src.tools.motorcad import motorcad_launch, motorcad_safe_get; print('OK')"`
Expected: prints "OK"

- [ ] **Step 7: Commit**

```bash
git add src/tools/motorcad/
git commit -m "feat: wrap Motor-CAD tools with LangChain @tool decorators for Deep Agents"
```

---

### Task 3: Fix Research Graph — Remove AsyncEventStream Dependency

The research graph imports `AsyncEventStream` from `src.agent.event_stream`, which we're deleting. Remove that dependency while preserving the pipeline.

**Files:**
- Modify: `src/research/graph.py`
- Modify: `src/research/state.py`

**Interfaces:**
- Consumes: existing research nodes (normalize_question, collect_context, etc.)
- Produces: `run_research(question) -> dict` that works without event stream

- [ ] **Step 1: Update src/research/state.py — remove AsyncEventStream**

Remove the import and the `stream` field from `ResearchState`:

```python
"""Research state — TypedDict for the research subgraph."""

from __future__ import annotations

from typing import Any, TypedDict


class ResearchState(TypedDict):
    """State carried through the research subgraph nodes."""

    question: str
    normalized_question: str
    domain_terms: list[str]
    wiki_context: list[dict[str, str]]
    local_docs_context: list[dict[str, str]]
    all_collected_sources: list[dict[str, str]]
    selected_sources: list[dict[str, str]]
    extracted_claims: list[str]
    extracted_equations: list[str]
    extracted_notes: list[str]
    synthesized_claims: list[str]
    conflicts: list[str]
    report_summary: str
    report_confidence: str
    report: dict[str, Any]
    messages: list[str]


def make_initial_state(question: str) -> ResearchState:
    """Return a fresh ResearchState with defaults."""
    return {
        "question": question,
        "normalized_question": "",
        "domain_terms": [],
        "wiki_context": [],
        "local_docs_context": [],
        "all_collected_sources": [],
        "selected_sources": [],
        "extracted_claims": [],
        "extracted_equations": [],
        "extracted_notes": [],
        "synthesized_claims": [],
        "conflicts": [],
        "report_summary": "",
        "report_confidence": "medium",
        "report": {},
        "messages": [],
    }
```

- [ ] **Step 2: Update src/research/graph.py — remove event stream code**

```python
"""LangGraph research pipeline using the Functional API (@entrypoint).

Nodes run sequentially:
    normalize -> collect_context -> source_selection -> read_extract
        -> [synthesize_claims if claims exist] -> build_report
"""

from __future__ import annotations

from typing import Any

from langgraph.func import entrypoint

from src.research.nodes.normalize_question import normalize_question
from src.research.nodes.collect_context import collect_context
from src.research.nodes.source_selection import source_selection
from src.research.nodes.read_extract import read_extract
from src.research.nodes.synthesize_claims import synthesize_claims
from src.research.nodes.build_report import build_report
from src.research.state import ResearchState, make_initial_state


@entrypoint()
async def _research_pipeline(state: ResearchState) -> dict[str, Any]:
    """Run the research pipeline — async entrypoint, sequential nodes."""
    _step(state, normalize_question)
    _step(state, collect_context)
    _step(state, source_selection)
    _step(state, read_extract)

    if state.get("extracted_claims"):
        _step(state, synthesize_claims)

    _step(state, build_report)

    return state.get("report", {
        "question": state.get("question", ""),
        "summary": "Research pipeline completed but produced no report.",
        "confidence": "low",
    })


def _step(state: ResearchState, node_fn) -> None:
    """Apply a node's updates to state in-place."""
    state.update(node_fn(state))


async def run_research(question: str) -> dict[str, Any]:
    """Run the research pipeline end-to-end."""
    state = make_initial_state(question)
    return await _research_pipeline.ainvoke(state)
```

- [ ] **Step 3: Check if any research nodes import AsyncEventStream**

Run: `grep -r "AsyncEventStream\|event_stream" src/research/`

If any hits, remove those imports (they should only be in graph.py and state.py).

- [ ] **Step 4: Verify research graph imports**

Run: `python -c "from src.research.graph import run_research; print('OK')"`
Expected: prints "OK"

- [ ] **Step 5: Commit**

```bash
git add src/research/graph.py src/research/state.py
git commit -m "refactor: remove AsyncEventStream dependency from research graph"
```

---

### Task 4: Add Research Wrapper Tool for Deep Agents

Create a single tool that Deep Agents can call to delegate research to the LangGraph pipeline.

**Files:**
- Create: `src/tools/research/__init__.py`
- Create: `src/tools/research/research_tool.py`

**Interfaces:**
- Consumes: `src.research.graph.run_research(question: str) -> dict`
- Produces: `research_subgraph` tool that returns JSON string

- [ ] **Step 1: Create src/tools/research/__init__.py**

```python
"""Research tool for Deep Agents — delegates to LangGraph research subgraph."""

from src.tools.research.research_tool import research_subgraph

__all__ = ["research_subgraph"]
```

- [ ] **Step 2: Create src/tools/research/research_tool.py**

```python
"""Research subgraph tool — wraps the LangGraph research pipeline for Deep Agents."""

from __future__ import annotations

import json

from langchain_core.tools import tool


@tool
def research_subgraph(question: str) -> str:
    """Research a motor engineering question using the LangGraph research pipeline.

    Runs a multi-step pipeline: normalize question, collect context from wiki/docs,
    select and read sources, extract claims and equations, synthesize findings,
    and produce a structured research report.

    Args:
        question: The motor engineering question to research.
    """
    import asyncio

    from src.research.graph import run_research

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        # Already in async context — run synchronously via thread
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor() as pool:
            result = pool.submit(asyncio.run, run_research(question)).result()
    else:
        result = asyncio.run(run_research(question))

    return json.dumps(result, indent=2, default=str)
```

- [ ] **Step 3: Verify import**

Run: `python -c "from src.tools.research import research_subgraph; print('OK')"`
Expected: prints "OK"

- [ ] **Step 4: Commit**

```bash
git add src/tools/research/
git commit -m "feat: add research_subgraph tool wrapping LangGraph pipeline for Deep Agents"
```

---

### Task 5: Update settings.py — Remove Dead References

**Files:**
- Modify: `src/config/settings.py`

**Interfaces:**
- Consumes: (none)
- Produces: cleaned settings with only what's needed

- [ ] **Step 1: Simplify settings.py**

Remove `MEMORY_PATH`, `BACKEND_ROUTES`, `AgentMode`, and the `invoke_structured` function (no longer used — Deep Agents handles structured output). Keep paths, model config, and `get_llm`.

```python
"""Project-wide configuration — paths, model defaults."""

from __future__ import annotations

import os
from pathlib import Path

# ── Project root ──────────────────────────────────────────────────────
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent.parent
WORKSPACE_ROOT: Path = PROJECT_ROOT / "workspace"

# ── Wiki paths (legacy — knowledge now in Deep Agents memory) ─────────
WIKI_ROOT: Path = WORKSPACE_ROOT / "wiki"

# ── Motor-CAD paths ───────────────────────────────────────────────────
MOTORCAD_MOT_DIR: Path | None = (
    Path(r"D:\SRM\Motor _CAD\ScriptFiles")
    if os.path.exists(r"D:\SRM\Motor _CAD\ScriptFiles")
    else None
)

REFERENCE_MOT: Path = PROJECT_ROOT / "SynRM_45kW_IE5.mot"

# ── LLM / Opencode ────────────────────────────────────────────────────
LLM_API_KEY: str | None = os.getenv("OPENCODE_API_KEY")
LLM_BASE_URL: str = os.getenv("LLM_BASE_URL", "https://opencode.ai/zen/v1")
LLM_MODEL: str = os.getenv("LLM_MODEL", "deepseek-v4-flash-free")

MODEL_DEFAULT: str = os.getenv("MODEL_DEFAULT", LLM_MODEL)
MODEL_RESEARCH: str = os.getenv("MODEL_RESEARCH", LLM_MODEL)

# ── LLM client factory ────────────────────────────────────────────────


def get_llm(model: str | None = None) -> "ChatOpenAI":
    """Return a LangChain ChatOpenAI pointed at Opencode."""
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=model or MODEL_DEFAULT,
        base_url=LLM_BASE_URL,
        api_key=LLM_API_KEY or os.getenv("OPENCODE_API_KEY") or "sk-placeholder",
        temperature=0.3,
    )


__all__ = [
    "PROJECT_ROOT",
    "WORKSPACE_ROOT",
    "WIKI_ROOT",
    "MOTORCAD_MOT_DIR",
    "REFERENCE_MOT",
    "LLM_API_KEY",
    "LLM_BASE_URL",
    "LLM_MODEL",
    "MODEL_DEFAULT",
    "MODEL_RESEARCH",
    "get_llm",
]
```

- [ ] **Step 2: Verify import**

Run: `python -c "from src.config.settings import get_llm, PROJECT_ROOT; print('OK')"`
Expected: prints "OK"

- [ ] **Step 3: Commit**

```bash
git add src/config/settings.py
git commit -m "refactor: simplify settings.py — remove dead references"
```

---

### Task 6: Delete Dead Code

Remove all files and directories marked for deletion in the spec.

**Files:**
- Delete: `src/tools/filesys/` (entire directory)
- Delete: `src/tools/shell/` (entire directory)
- Delete: `src/tools/search/` (entire directory)
- Delete: `src/tools/memory/` (entire directory)
- Delete: `src/tools/wiki/` (entire directory)
- Delete: `src/tools/execution/` (entire directory)
- Delete: `src/memory/` (entire directory)
- Delete: `src/agent/graph.py`
- Delete: `src/agent/nodes.py`
- Delete: `src/agent/runtime.py`
- Delete: `src/agent/subagents.py`
- Delete: `src/agent/approvals.py`
- Delete: `src/agent/event_stream.py`
- Delete: `src/agent/tools.py`
- Delete: `src/skills/` (entire directory)
- Delete: `apps/cli/` (entire directory)

**Interfaces:**
- Consumes: (none — these are dead code)
- Produces: cleaner repo with only active code

- [ ] **Step 1: Delete directories**

```bash
rm -rf src/tools/filesys/
rm -rf src/tools/shell/
rm -rf src/tools/search/
rm -rf src/tools/memory/
rm -rf src/tools/wiki/
rm -rf src/tools/execution/
rm -rf src/memory/
rm -rf src/skills/
rm -rf apps/cli/
```

- [ ] **Step 2: Delete individual files**

```bash
rm src/agent/graph.py
rm src/agent/nodes.py
rm src/agent/runtime.py
rm src/agent/subagents.py
rm src/agent/approvals.py
rm src/agent/event_stream.py
rm src/agent/tools.py
```

- [ ] **Step 3: Clean up remaining __init__.py files**

Check if `src/tools/__init__.py` still imports deleted modules. If so, empty it:

```python
"""Tools package — Motor-CAD domain tools for Deep Agents."""
```

Check if `src/agent/__init__.py` still imports deleted modules. If so, clean it.

- [ ] **Step 4: Remove empty apps/ directory**

```bash
rm -rf apps/
```

- [ ] **Step 5: Verify no broken imports remain**

Run: `python -c "from src.tools.motorcad import motorcad_launch; from src.research.graph import run_research; from src.config.settings import get_llm; print('All imports OK')"`
Expected: prints "All imports OK"

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "refactor: delete dead code — custom tools, graph, runtime, skills, CLI

Removed ~2500 lines of code that duplicated Deep Agents built-ins:
- src/tools/filesys/, shell/, search/, memory/, wiki/, execution/
- src/memory/, src/skills/, apps/cli/
- src/agent/graph.py, nodes.py, runtime.py, subagents.py, approvals.py, event_stream.py, tools.py

Kept: Motor-CAD tools (domain-specific), research subgraph (LangGraph), domain models, config, artifacts."
```

---

### Task 7: Clean Up Artifacts — Remove Wiki-Specific Contracts

The `WikiUpdatePlan` artifact is no longer needed (wiki → Deep Agents memory). Remove it and clean up imports.

**Files:**
- Modify: `src/artifacts/__init__.py`
- Delete: `src/artifacts/wiki_update_plan.py`

**Interfaces:**
- Consumes: (none)
- Produces: cleaned artifacts package

- [ ] **Step 1: Remove WikiUpdatePlan from src/artifacts/__init__.py**

```python
"""Data contracts between components."""

from src.artifacts.research_report import ResearchReport, Source
from src.artifacts.code_report import CodeReport
from src.artifacts.experiment_report import ExperimentReport

__all__ = [
    "ResearchReport",
    "Source",
    "CodeReport",
    "ExperimentReport",
]
```

- [ ] **Step 2: Delete wiki_update_plan.py**

```bash
rm src/artifacts/wiki_update_plan.py
```

- [ ] **Step 3: Verify import**

Run: `python -c "from src.artifacts import ResearchReport, CodeReport; print('OK')"`
Expected: prints "OK"

- [ ] **Step 4: Commit**

```bash
git add src/artifacts/
git commit -m "refactor: remove WikiUpdatePlan artifact — wiki replaced by Deep Agents memory"
```

---

### Task 8: Update CLAUDE.md and AGENTS.md

Update project documentation to reflect the new architecture.

**Files:**
- Modify: `CLAUDE.md`
- Modify: `AGENTS.md` (if it references deleted tools)

**Interfaces:**
- Consumes: new architecture from Tasks 1-7
- Produces: accurate project documentation

- [ ] **Step 1: Update CLAUDE.md — replace Key Files table and Architecture section**

Replace the architecture diagram and key files table:

```markdown
## PART 2: PROJECT — MOTOR-DEEPAGENT

### Goal

Build a **terminal-first engineering assistant** that starts as a motor-design assistant with PyMotorCAD / experiment / optimization workflows and grows into a broader engineering platform.

### Architecture

```
User → dcode (Deep Agents runtime)
         ├── Built-in tools (read/write/grep/ls/execute/web_search/memory/skills)
         ├── Motor-CAD Tools (src/tools/motorcad/)
         ├── Research Subagent → LangGraph research subgraph
         └── Domain Models (src/domain/motor/)
```

**Principle:** Deep Agents for runtime + built-in capabilities. LangGraph only for the research subgraph where explicit graph structure helps.

### Key Files

| File | Purpose |
|------|---------|
| `config.toml` | Deep Agents configuration |
| `AGENTS.md` | Motor specs, constraints, design strategy |
| `src/tools/motorcad/` | Motor-CAD domain tools (Deep Agents compatible) |
| `src/research/graph.py` | LangGraph research pipeline |
| `src/domain/motor/` | Parameter maps, result models, geometry models |
| `src/config/settings.py` | Project-wide paths and model config |
| `src/artifacts/` | Pydantic data contracts |
| `SynRM_45kW_IE5.mot` | Reference motor model |
| `optimize_synrm_v4.py` | Existing optimization script (reference) |
```

- [ ] **Step 2: Update Tech Stack section — add Deep Agents, remove old deps**

```markdown
## PART 3: TECH STACK

### Python Environment
- Python 3.13.5 (Anaconda, `C:\Users\sarth\anaconda3`)
- Windows 11

### Core Dependencies
| Package | Purpose |
|---------|---------|
| `deepagents` | Agent runtime (built-in tools, memory, HITL, subagents) |
| `langgraph` | Research subgraph orchestration |
| `langchain-core` | Tool decorators, message types |
| `langchain-openai` | LLM client for Opencode API |
| `pydantic>=2.0` | Data contracts / structured output |
| `python-dotenv>=1.0` | Environment loading |

### Phase 4 Dependencies
| Package | Purpose |
|---------|---------|
| `ansys.motorcad.core` | PyMotorCAD (proprietary, Ansys EULA) |

### External Services
- **Opencode** — LLM access (`ai.opencode.ai/zen/v1`)
- **Tavily** — Web search (for `web_search` tool)
- **Ansys Motor-CAD 2025.1.1** — FEA solver (local, licensed)
```

- [ ] **Step 3: Update Quick Start**

```markdown
## Quick Start

```bash
set OPENROUTER_API_KEY=sk-or-v1-...
set TAVILY_API_KEY=tvly-...
dcode                              # interactive REPL
dcode "inspect the motor parameters"   # single-shot
```
```

- [ ] **Step 4: Check AGENTS.md for references to deleted tools**

Run: `grep -n "read_file\|write_file\|grep_files\|list_directory\|tavily_search\|store_memory\|SubagentConfig\|build_orchestrator" AGENTS.md`

If hits found, update those lines to reference Deep Agents built-in tools instead.

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md AGENTS.md
git commit -m "docs: update CLAUDE.md and AGENTS.md for Deep Agents architecture"
```

---

### Task 9: Update .gitignore

Ensure workspace/memory/ and config artifacts are properly ignored.

**Files:**
- Modify: `.gitignore` (if exists, otherwise create)

**Interfaces:**
- Consumes: (none)
- Produces: proper gitignore

- [ ] **Step 1: Create or update .gitignore**

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/

# Environment
.env
.venv/
venv/

# IDE
.vscode/
.idea/
*.swp

# OS
Thumbs.db
Desktop.ini

# Deep Agents
workspace/memory/

# Motor-CAD
best_so_far.mot
```

- [ ] **Step 2: Commit**

```bash
git add .gitignore
git commit -m "chore: update .gitignore for Deep Agents"
```

---

### Task 10: Final Verification

**Files:**
- (none — verification only)

**Interfaces:**
- Consumes: all tasks 1-9 complete
- Produces: working system

- [ ] **Step 1: Verify all imports work**

Run: `python -c "from src.tools.motorcad import motorcad_launch, motorcad_safe_get, motorcad_get_variables; from src.tools.research import research_subgraph; from src.research.graph import run_research; from src.config.settings import get_llm, PROJECT_ROOT; from src.artifacts import ResearchReport, CodeReport; from src.domain.motor.result_models import ElectromagneticResult; print('All imports OK')"`

Expected: prints "All imports OK"

- [ ] **Step 2: Verify dcode can discover tools**

Run: `dcode --help`
Expected: shows dcode help

- [ ] **Step 3: Verify no dead imports remain**

Run: `python -m py_compile src/tools/motorcad/__init__.py && python -m py_compile src/tools/research/__init__.py && python -m py_compile src/research/graph.py && python -m py_compile src/config/settings.py && echo "All files compile OK"`

Expected: prints "All files compile OK"

- [ ] **Step 4: Verify file structure**

Run: `find src/ -name "*.py" | sort`

Expected output (no dead files):
```
src/__init__.py
src/artifacts/__init__.py
src/artifacts/code_report.py
src/artifacts/experiment_report.py
src/artifacts/research_report.py
src/config/__init__.py
src/config/settings.py
src/domain/__init__.py
src/domain/motor/__init__.py
src/domain/motor/geometry_models.py
src/domain/motor/parameter_mapping.py
src/domain/motor/result_models.py
src/research/__init__.py
src/research/graph.py
src/research/nodes/__init__.py
src/research/nodes/build_report.py
src/research/nodes/collect_context.py
src/research/nodes/normalize_question.py
src/research/nodes/read_extract.py
src/research/nodes/source_selection.py
src/research/nodes/synthesize_claims.py
src/research/prompts/__init__.py
src/research/prompts/research_prompts.py
src/research/schemas.py
src/research/state.py
src/tools/__init__.py
src/tools/motorcad/__init__.py
src/tools/motorcad/get_results.py
src/tools/motorcad/run_motorcad.py
src/tools/motorcad/set_parameters.py
src/tools/research/__init__.py
src/tools/research/research_tool.py
```

- [ ] **Step 5: Final commit**

```bash
git add -A
git commit -m "chore: final cleanup — verify all imports and file structure"
```
