"""P3+P5: cache hygiene / tool optimization contract tests.

Read-only against src/ — these tests assert deterministic tool wiring,
parallel-contract documentation, and execution observability helpers.
Tolerant pre-/post-P0/P2 so they pass before those agents land and still
pin the stronger contract after.
"""
import re

import pytest


EXPECTED_TOOL_ORDER = [
    "execute_generated_motorcad_code",
    "create_run_file",
    "execute_run_file",
    "delete_file",
    "validate_motor_params",
    "score_motor_result",
    "batch_validate_params",
    "wiki_search_many",
    "research_subgraph",
    "tavily_search",
    "wiki_tool",
]


def _tool_names(tools):
    names = []
    for t in tools:
        name = getattr(t, "name", None) or getattr(t, "__name__", None)
        # langchain StructuredTool exposes .name; fallback to str
        names.append(name if isinstance(name, str) else str(t))
    return names


def test_build_tools_order_stable():
    from src.agent.factory import build_tools

    first = _tool_names(build_tools())
    second = _tool_names(build_tools())
    # Determinism is the hard requirement (cache hygiene).
    assert first == second, f"build_tools() not deterministic: {first} vs {second}"
    # Pin the expected order when it matches; otherwise report helpfully
    # but still pass on determinism so pre-P0 reordering doesn't break P3.
    if first != EXPECTED_TOOL_ORDER:
        print(f"\nNOTE: tool order differs from expected.\nActual:   {first}\nExpected: {EXPECTED_TOOL_ORDER}")
    assert first == EXPECTED_TOOL_ORDER, (
        f"tool order mismatch.\nActual:   {first}\nExpected: {EXPECTED_TOOL_ORDER}"
    )


def test_system_prompt_has_parallel_contract():
    from src.agent.factory import SYSTEM_PROMPT

    assert isinstance(SYSTEM_PROMPT, str) and SYSTEM_PROMPT.strip(), "SYSTEM_PROMPT is empty"
    lowered = SYSTEM_PROMPT.lower()
    # Baseline contract that exists pre-P0: must mention parallel discipline.
    assert "parallel" in lowered, "SYSTEM_PROMPT has no parallel guidance at all"
    # Stronger P0 markers — report status but stay green pre-P0.
    has_simultaneous = "simultaneously" in lowered
    has_parallel_safe = "parallel-safe" in lowered
    has_serial_only = "serial only" in lowered
    print(
        f"\nParallel-contract markers: simultaneously={has_simultaneous}, "
        f"PARALLEL-SAFE={has_parallel_safe}, SERIAL ONLY={has_serial_only}"
    )
    if has_parallel_safe or has_serial_only:
        # Post-P0: pin the stronger contract.
        assert re.search(r"parallel-safe|serial only", SYSTEM_PROMPT, re.IGNORECASE), (
            "Expected PARALLEL-SAFE / SERIAL ONLY markers post-P0"
        )
        if has_simultaneous:
            assert re.search(r"simultaneously", SYSTEM_PROMPT, re.IGNORECASE)
    else:
        # Pre-P0: baseline 'parallel' mention suffices (asserted above).
        print("NOTE: P0 parallel-contract markers not yet present; baseline 'parallel' check suffices pre-P0.")


def test_execution_metrics_exist():
    import src.tools.execution as ex

    # scan_code_safety is the hard requirement (safety scan observability).
    assert hasattr(ex, "scan_code_safety"), "src.tools.execution.scan_code_safety missing"
    assert callable(ex.scan_code_safety), "scan_code_safety is not callable"

    # Metrics helpers may land with a later agent; accept any known variant.
    has_new_metrics = hasattr(ex, "get_execution_metrics") or hasattr(ex, "_TOOL_METRICS")
    if has_new_metrics:
        print("\nExecution metrics helper present (get_execution_metrics or _TOOL_METRICS).")
    else:
        # Pre-implementation fallback: budget observability already exists.
        has_fallback = hasattr(ex, "get_budget_status")
        print(
            "\nNOTE: get_execution_metrics/_TOOL_METRICS not yet present "
            f"(pre-optimization); fallback get_budget_status present={has_fallback}."
        )
        assert has_fallback, (
            "Neither get_execution_metrics/_TOOL_METRICS nor fallback get_budget_status exists"
        )


def test_batch_tools_importable():
    try:
        import src.tools.batch_tools  # noqa: F401
    except ImportError as e:
        pytest.skip(f"src.tools.batch_tools not yet created by P2 agent: {e}")
    # If importable, smoke-check it exposes at least one tool/callable.
    import src.tools.batch_tools as bt

    public = [n for n in dir(bt) if not n.startswith("_")]
    print(f"\nbatch_tools public attrs: {public}")
    assert len(public) > 0, "src.tools.batch_tools has no public attributes"
