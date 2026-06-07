"""Long-term memory store for SynRM pipeline — persists optimization results across runs.

Uses LangGraph's InMemoryStore for cross-session persistence. Stores best barrier
params per motor spec so future runs start with better initial guesses.
"""

from langgraph.store.memory import InMemoryStore
from datetime import datetime

NAMESPACE = ("synrm", "optimization_results")


def create_store() -> InMemoryStore:
    """Create a new in-memory store for cross-session persistence.

    Note: InMemoryStore is per-process. For true cross-session persistence
    across restarts, swap for a persistent BaseStore implementation.
    """
    return InMemoryStore()


def save_optimization_result(store, spec: dict, barrier_params: dict, results: list[dict]) -> dict | None:
    """Save best params for this motor spec to memory store.

    Returns the updated record, or None on failure (non-fatal).
    """
    try:
        key = _spec_key(spec)
        existing = store.get(NAMESPACE, key)
        data = existing.value if existing else {}

        best = min(results, key=lambda r: r.get("score", float("inf"))) if results else {}

        updated = {
            **data,
            "power_kw": spec.get("power_kw"),
            "speed_rpm": spec.get("speed_rpm"),
            "poles": spec.get("poles"),
            "best_params": barrier_params,
            "best_score": best.get("score"),
            "best_efficiency": best.get("MotorEfficiency"),
            "run_count": data.get("run_count", 0) + 1,
            "last_run": datetime.now().isoformat(),
        }
        store.put(NAMESPACE, key, updated)
        return updated
    except Exception as e:
        print(f"  [WARN] Memory save failed (non-fatal): {e}")
        return None


def load_best_params(store, spec: dict) -> dict | None:
    """Load remembered best params for a motor spec, if any.

    Returns the best_params dict, or None if no prior run exists or on error.
    """
    try:
        key = _spec_key(spec)
        item = store.get(NAMESPACE, key)
        if item and item.value.get("best_params"):
            return item.value["best_params"]
        return None
    except Exception as e:
        print(f"  [WARN] Memory load failed (non-fatal): {e}")
        return None


def _spec_key(spec: dict) -> str:
    return f"{spec.get('power_kw', 45)}kW_{spec.get('speed_rpm', 3000)}rpm_{spec.get('poles', 4)}p"
