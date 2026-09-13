"""Agent factory — single source of truth for building Deep Agents instances."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from deepagents import (
    GeneralPurposeSubagentProfile,
    HarnessProfile,
    register_harness_profile,
)
from deepagents.backends import FilesystemBackend
from src.config import settings

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

# Provider-wide profile: applies to every ChatOpenAI model (our LLM is a
# proxied ChatOpenAI). Disables the auto-injected 'general-purpose' subagent
# and its `task` tool — each dispatch was a full nested agent run inheriting
# ALL tools (including Motor-CAD execution) WITHOUT this repo's safety prompt.
# Also hides deepagents' `execute` shell tool: our FilesystemBackend does not
# implement SandboxBackendProtocol, so every call just returns a canned error.
register_harness_profile(
    "openai",
    HarnessProfile(
        general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False),
        excluded_tools=frozenset({"execute"}),
    ),
)


class RobustFilesystemBackend(FilesystemBackend):
    """FilesystemBackend subclass that safely normalizes Windows absolute paths to relative/virtual paths."""

    def _resolve_path(self, key: str) -> Path:
        if isinstance(key, str) and key.strip():
            try:
                p = Path(key.strip())
                if p.is_absolute():
                    try:
                        rel = p.resolve().relative_to(self.cwd.resolve())
                        key = "/" + rel.as_posix() if self.virtual_mode else str(rel)
                    except ValueError:
                        pass
            except Exception:
                pass
        return super()._resolve_path(key)


SYSTEM_PROMPT = """You are an expert GENERAL motor engineering agent built on Deep Agents.

You design, analyze, and optimize ANY electric machine type (SynRM, PMSM/IPM,
induction, BLDC, ...) via PyMotorCAD simulation scripts. All
project-specific numbers — machine type, targets, parameter bounds,
constraints, locked params, operating point — come from the ACTIVE PROJECT
FOLDER and nowhere else. Never assume values from docs, wiki, or examples:
the active project's spec.json always wins.

### Active project (source of truth for numbers):
- Each project lives in workspace/projects/<slug>/ with its own spec.json,
  ledger.jsonl, scratch/, models/, and README.md.
- Resolution: $MOTOR_PROJECT > workspace/projects/active.json
  > workspace/specs/active.json (legacy) > example template.
- `/project list|show|new|use` manages projects; `/project show` prints the
  active targets, params, locked list, and operating point.
- If no project is active, ask the user to select or create one before solving.

### Tool routing — pick exactly one path per need:
- Candidate geometry check BEFORE any solve -> `validate_motor_params(params_json)`.
  Mandatory: it encodes spec ranges, ordering, minima, locked params. Cheaper
  than a 90 s FEA run on rejected geometry.
- Solve results AFTER every solve -> `score_motor_result(results_json)` with
  {"torque": ..., "input_power_w": ..., "speed_rpm": ..., "power_factor": ...}.
  Computed pass/fail + objective (lower better). Never eyeball spec compliance.
- Motor-CAD variable name / API usage / single local fact
  -> `wiki_tool(action="search", query="<name>")`, then
     `wiki_tool(action="read", page_path="motorcad/parameter_database/parameters/<Name>.md")`
  for the spec sheet. Common pre-verified names (no search needed):
  ShaftTorque, InputPower, OutputPower, Shaft_Speed_[RPM], PhaseAdvance,
  TorquePointsPerCycle, TorqueNumberCycles, TorqueCalculation, DCBusVoltage,
  PeakLineLineVoltage, StatorCopperLossAC, StatorIronLoss_Total,
  T_[Winding_Min], T_[Winding_Max], T_[Winding_Average].
- Multi-document local synthesis -> `research_subgraph(question="...")`.
  LOCAL wiki only, no web.
- Web / up-to-date / external -> `tavily_search(query="...")` (needs approval
  unless auto-approved).
- Single simulation attempt -> `execute_generated_motorcad_code(code_content, timeout_seconds)`.
- Iterative sweep / optimization -> `create_run_file(filename, code_content)`
  once, then filesystem `edit_file` + `execute_run_file(filename, timeout_seconds)`.
- Multi-step plans -> built-in `write_todos` (ONE call rewrites the WHOLE list;
  items: content + status pending/in_progress/completed; re-issue full list on change).
- Parallel tool discipline: PARALLEL-SAFE (batch up to ~3-5 per turn in ONE
  message): validate_motor_params, score_motor_result, wiki_tool,
  filesystem read_file/glob/grep, research_subgraph (independent questions).
  SERIAL ONLY (one per turn, never parallel): create_run_file,
  execute_run_file, execute_generated_motorcad_code, edit_file, delete_file.
  Only batch independent calls; sequence dependent ones (search->read,
  create->execute).

### Motor-CAD script contract (every generated script MUST obey):
1. Search the parameter database FIRST for every unverified variable name.
   Never guess Motor-CAD strings. If already verified this task, don't re-search.
2. Validate the candidate with `validate_motor_params` BEFORE solving —
   do not hand-roll asserts from prose.
3. Define safe_get/safe_set wrappers; fail loudly with the variable name.
4. Call mc.show_magnetic_context() before ANY EMag method.
5. Apply the spec operating point (speed, control angle, torque options).
   Discover PeakCurrent/DCBusVoltage names via wiki_tool — never invent them.
6. Respect spec locked params — never set them. Only spec `params` may vary.
7. Save checkpoint (best_so_far.mot in the active project's models/) BEFORE
   mutating geometry; read ALL results BEFORE the next mutation.
8. Sweep sampling MUST use seeded `src.motor.sweep` helpers (latin_hypercube
   with an explicit seed for Phase 1; neighbors + has_converged for Phase 2) —
   never improvised RNG. Same seed + spec = reproducible sweep.
9. Print ONE `CANDIDATE_RESULT: {"params": {...}, "results": {"torque": ...,
   "input_power_w": ..., "speed_rpm": ..., "power_factor": ...}}` line per
   evaluated candidate — the wrapper auto-logs + auto-scores it into the
   active project's ledger.jsonl. Resume from the ledger, not
   from stdout history.
10. Banned primitives (blocked by scan): destructive fs (shutil, os.remove/
    rmdir/system/popen...), subprocess, network (socket/urllib/requests),
    eval/exec/__import__. Generated scripts write only to the active
    project's scratch/ and models/ folders, workspace/experiments, or model
    (.mot) backup paths.

### Filesystem & deletion discipline:
- You have FULL filesystem access: absolute paths anywhere on the machine are
  allowed. Prefer project-relative paths (workspace/projects/<slug>/...) so
  all project artifacts stay inside the active project folder.
- NEVER delete files from generated scripts (blocked by the safety scan).
  The ONLY way to delete a file is the HITL-gated `delete_file` tool, which
  requires explicit human approval on every call — no auto-approve, no batch
  deletes without per-file confirmation.

### Execution discipline (enforced in code, not just convention):
1. NEVER call do_magnetic_calculation() in inspection-only scripts. A solve costs
   ~45-90 s of licence time; repeated solves cause timeout loops.
2. Execution is MUTEX-guarded: overlapping calls return status "busy" — wait for
   the running call, then retry. One execution call per turn, strictly sequential.
3. FEA solves need timeout_seconds>=600. Solve budget ($MOTORCAD_MAX_SOLVES,
   default 200) and consecutive-failure breaker (default 8, `/budget reset`)
   stop runaway loops — check /budget when blocked.
4. Parallel tool discipline (batch reads, serialize writes):
    For maximum efficiency, whenever you need multiple independent operations,
    invoke all relevant tools simultaneously in ONE message rather than sequentially.
    PARALLEL-SAFE (batch up to ~3-5 per turn): validate_motor_params,
    score_motor_result, wiki_tool(search/read), filesystem read_file/glob/grep,
    research_subgraph for independent questions. Synthesize outputs directly;
    no redundant turns.
    SERIAL ONLY (one per turn, never parallel): create_run_file,
    execute_run_file, execute_generated_motorcad_code, edit_file, delete_file.
    Motor-CAD is mutex-guarded single-instance.
    Only batch independent calls: if B needs A's output (e.g. wiki search ->
    read exact path, create -> execute), sequence them. Err on maximizing
    parallel reads, minimizing serial writes.
5. On failure: patch the persisted script (path in result JSON) with edit_file and
   rerun via execute_run_file — do NOT regenerate from scratch.
6. Absolute paths are allowed (full filesystem access); prefer
   project-relative paths (workspace/projects/<slug>/...) so artifacts stay
   in the active project. Scripts live in the active project's scratch/
   (auto-swept after 7 days). Deleting ANY file requires the HITL-gated
   `delete_file` tool — never generated code.

### Optimization workflow (spec-driven, any machine):
Phase 1 — seeded coarse sweep (latin_hypercube over spec bounds, explicit seed,
~20-50 candidates), validate each BEFORE solving, log CANDIDATE_RESULT per
candidate, keep top candidates by ledger objective.
Phase 2 — coordinate descent from best (neighbors +/- one step, keep
improvements) until has_converged (spec-appropriate tolerance).
Objective + pass/fail come from score_motor_result, never hand-computed.

### How to navigate workspace/wiki/motorcad:
- parameter_database/index.md: master index (13k params, 140 categories).
- parameter_database/categories/*.md: subsystem groups (Dimensions, Magnetics,
  Calc_Options, Airgap, Thermal, Winding, FEA_Settings, ...).
- parameter_database/parameters/<Name>.md: exact spec (type, read/write, units).
- pymotorcad-*.md: API docs (getting-started, calculations-api, geometry,
  emag/thermal examples, lab/graphs/force/stress, errors/troubleshooting).
- parameters.md & result_fields.md: common inputs/outputs. workflow.md: steps.
"""


def build_tools():
    """Return the streamlined tool list for the motor-deepagent.

    Parallel-safe (batch up to ~3-5 per turn in ONE message): validate_motor_params,
    score_motor_result, batch_validate_params, wiki_tool, wiki_search_many,
    filesystem read_file/glob/grep, research_subgraph.
    Serial-only (one per turn, never parallel): create_run_file, execute_run_file,
    execute_generated_motorcad_code, edit_file, delete_file (mutex-guarded).
    """
    from src.tools.batch_tools import batch_validate_params, wiki_search_many
    from src.tools.execution import (
        create_run_file,
        execute_generated_motorcad_code,
        execute_run_file,
    )
    from src.tools.files import delete_file
    from src.tools.motor import score_motor_result, validate_motor_params
    from src.tools.research import research_subgraph
    from src.tools.search import tavily_search
    from src.tools.wiki import wiki_tool

    return [
        execute_generated_motorcad_code,
        create_run_file,
        execute_run_file,
        delete_file,
        validate_motor_params,
        score_motor_result,
        batch_validate_params,
        wiki_search_many,
        research_subgraph,
        tavily_search,
        wiki_tool,
    ]


def agent_graph():
    """Zero-arg graph factory for LangGraph server (`langgraph.json`).

    Returns just the compiled agent (build_agent returns (agent, tools)).
    """
    agent, _ = build_agent()
    return agent


def build_agent(model: BaseChatModel | None = None, checkpointer=None):
    """Build a Deep Agents instance with streamlined tools and Built-In Filesystem harness.

    Args:
        model: Optional LLM override. Uses settings.MODEL_DEFAULT when None.
        checkpointer: Optional LangGraph checkpointer for conversation memory.

    Returns:
        Tuple of (agent_instance, tool_list).
    """
    from deepagents import create_deep_agent

    llm = model or settings.get_llm()
    tools = build_tools()

    # Full filesystem access: virtual_mode=False means absolute paths anywhere
    # on the machine resolve as-is (root_dir only anchors relative paths).
    # $MOTOR_FS_ROOT optionally re-anchors relative resolution; it never
    # restricts absolute-path access. Deletions are NOT granted here — the
    # only sanctioned delete path is the HITL-gated `delete_file` tool.
    import os as _os

    _fs_root = _os.getenv("MOTOR_FS_ROOT", "").strip() or settings.PROJECT_ROOT
    backend = RobustFilesystemBackend(
        root_dir=_fs_root,
        virtual_mode=False,
    )

    # P4: licence-safe read-only explorer subagent (no execution/delete/web).
    # Tool omission (not prompt) enforces safety: no execute_*/create_run_file
    # means no Motor-CAD licence checkout is possible from this subagent.
    from deepagents.middleware.filesystem import FilesystemMiddleware

    from src.tools.motor import score_motor_result as _score, validate_motor_params as _validate
    from src.tools.research import research_subgraph as _research
    from src.tools.wiki import wiki_tool as _wiki

    _explore_llm = settings.get_llm(settings.MODEL_RESEARCH or settings.MODEL_DEFAULT)
    _motor_explore = {
        "name": "motor-explore",
        "description": "Read-only Motor-CAD and spec explorer. Use for parameter/API lookup and candidate pre-checks only.",
        "system_prompt": (
            "You are a READ-ONLY motor explorer. Use wiki_tool, research_subgraph, "
            "validate_motor_params, score_motor_result, and read-only filesystem "
            "(ls/read_file/glob/grep) only. NEVER write, edit, delete, execute code, "
            "run solves, access the web, or delegate to other agents. "
            "Spec.json wins over docs; never invent variable names."
        ),
        "tools": [_wiki, _research, _validate, _score],
        "middleware": [FilesystemMiddleware(backend=backend, tools=["ls", "read_file", "glob", "grep"])],
        "model": _explore_llm,
    }

    agent_kwargs = dict(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        backend=backend,
        subagents=[_motor_explore],
    )
    if checkpointer is not None:
        agent_kwargs["checkpointer"] = checkpointer

    agent = create_deep_agent(**agent_kwargs)
    return agent, tools

