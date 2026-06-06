"""Entry point — run the full SynRM design pipeline."""

import sys
from pathlib import Path

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).parent))

from agent.graph import build_graph, initial_state


def main():
    """Build and invoke the pipeline with default motor specs."""
    print("=" * 60)
    print("SynRM Multi-Agent Pipeline — LangGraph State Machine")
    print("=" * 60)

    # Build graph
    print("\n[1/4] Building graph...")
    app = build_graph()

    # Create initial state
    print("[2/4] Creating initial state (45kW IE5 SynRM)...")
    state = initial_state()

    print(f"[3/4] Motor specs: {state['motor_spec']}")
    print(f"[4/4] Starting pipeline...\n")

    # Config with required thread_id for checkpointer
    config = {"configurable": {"thread_id": "synrm-pipeline-1"}}

    # Run pipeline
    for event in app.stream(state, config):
        for node_name, node_state in event.items():
            phase = node_state.get("phase", "")
            ps = node_state.get("phase_status", {}).get(phase, {})
            s = ps.get("status", "?") if isinstance(ps, dict) else str(ps)
            print(f"  -> [{phase}] status={s}")

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
