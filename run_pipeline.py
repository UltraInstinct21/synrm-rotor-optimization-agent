"""Entry point — run the full SynRM design pipeline with streaming progress + HITL."""

import sys
from pathlib import Path

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).parent))

from langgraph.types import Command
from agent.graph import build_graph, initial_state

# Phase-specific running messages shown as each node begins execution.
_PHASE_MSG = {
    "research": "Researching SynRM motor theory",
    "synthesis": "Synthesizing knowledge across sources",
    "calculate": "Computing motor winding and barrier parameters",
    "design": "Exploring .mot and discovering design variables",
}


def _fmt_event(phase: str, update: dict) -> str | None:
    """Build a single progress line from a node's state diff update.

    Returns a formatted string like:
        [research]   Researching SynRM motor theory... done — 5 entities extracted

    Returns None when the update carries no meaningful phase_status info
    (e.g. an empty intermediate event that should be skipped).
    """
    if not isinstance(update, dict):
        return None  # skip non-dict events (internal LangGraph tuples, etc.)
    ps = update.get("phase_status", {})
    raw = ps.get(phase, {})
    if isinstance(raw, dict):
        status = raw.get("status", "?")
        error = raw.get("error", "")
    else:
        status = str(raw)
        error = ""

    if status in ("?", ""):
        return None  # skip uninformative events

    msg = _PHASE_MSG.get(phase, "Running")

    if status == "done":
        detail = ""
        if phase == "calculate":
            wp = update.get("winding_params", {})
            bp = update.get("barrier_params", {})
            detail = f" — {len(wp)} winding params, {len(bp)} barrier params"
        elif phase == "research":
            ec = update.get("wiki_entities_created", [])
            detail = f" — {len(ec)} entities extracted" if ec else ""
        elif phase == "synthesis":
            cc = update.get("wiki_concepts_created", [])
            detail = f" — {len(cc)} concepts synthesized" if cc else ""
        elif phase == "design":
            best = update.get("best_model_path", "")
            ec = update.get("wiki_entities_created", [])
            bits = []
            if ec:
                bits.append(f"{len(ec)} entities")
            if best:
                bits.append(f"best: {Path(best).name}")
            detail = " — " + ", ".join(bits) if bits else ""
        return f"  [{phase:<12}] {msg}... {status}{detail}"

    if status == "failed":
        err_short = (error[:77] + "...") if len(error) > 80 else error
        return f"  [{phase:<12}] {msg}... FAILED: {err_short}"

    if status == "skipped":
        return f"  [{phase:<12}] {msg}... skipped"

    return f"  [{phase:<12}] {msg}... {status}"


def main():
    """Build and stream the SynRM pipeline, displaying real-time progress."""
    print("=" * 60)
    print("SynRM Multi-Agent Pipeline — LangGraph State Machine")
    print("=" * 60)

    # Build graph
    print("\n[1/4] Building graph...")
    app = build_graph(hitl=True)

    # Create initial state
    print("[2/4] Creating initial state (45kW IE5 SynRM)...")
    state = initial_state()

    print(f"[3/4] Motor specs: {state['motor_spec']}")
    print(f"[4/4] Starting pipeline...\n")

    # Config with required thread_id for checkpointer
    config = {"configurable": {"thread_id": "synrm-pipeline-1"}}

    # Run pipeline with streaming — stream_mode="updates" emits per-node state diffs
    for event in app.stream(state, config, stream_mode="updates"):
        for node_name, update in event.items():
            line = _fmt_event(node_name, update)
            if line:
                print(line)

    # Check for interrupt (human-in-the-loop approval gate)
    snapshot = app.get_state(config)
    if snapshot.next:
        print("\n" + "=" * 60)
        print("  HUMAN-IN-THE-LOOP: Optimization Approval Required")
        print("=" * 60)

        current_state = snapshot.values
        bp = current_state.get("barrier_params", {})
        print("\n  Barrier parameters ready for optimization:")
        for k, v in list(bp.items())[:12]:
            print(f"    {k} = {v}")
        if len(bp) > 12:
            print(f"    ... and {len(bp) - 12} more")

        answer = input("\n  Run optimization with these params? [Y/n]: ").strip().lower()

        if answer in ("", "y", "yes"):
            print("\n  Resuming: proceeding with optimization...")
            for event in app.stream(
                Command(update={"approval": {"proceed": True}}, resume=True),
                config,
                stream_mode="updates",
            ):
                for node_name, update in event.items():
                    line = _fmt_event(node_name, update)
                    if line:
                        print(line)
        else:
            print("\n  Resuming: skipping optimization...")
            for event in app.stream(
                Command(
                    update={
                        "approval": {"proceed": False},
                        "phase": "design",
                        "phase_status": {
                            "design": {
                                "status": "skipped",
                                "error": "User skipped optimization at approval gate",
                            }
                        },
                    },
                    resume=True,
                ),
                config,
                stream_mode="updates",
            ):
                for node_name, update in event.items():
                    line = _fmt_event(node_name, update)
                    if line:
                        print(line)

    # Print final state summary
    final_state = app.get_state(config)
    print("\n" + "=" * 60)
    print("Pipeline complete. Final state:")
    print(f"  Phase status: {final_state.values.get('phase_status', {})}")
    print(f"  Entities created: {len(final_state.values.get('wiki_entities_created', []))}")
    print(f"  Concepts created: {len(final_state.values.get('wiki_concepts_created', []))}")
    print(f"  Winding params: {final_state.values.get('winding_params', {})}")
    print(f"  Barrier params: {len(final_state.values.get('barrier_params', {}))} keys")
    print("=" * 60)


if __name__ == "__main__":
    main()
