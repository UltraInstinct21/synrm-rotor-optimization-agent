"""LangGraph research pipeline using the Functional API (@entrypoint).

Nodes run sequentially with standard Python control flow::

    normalize -> collect_context -> source_selection -> read_extract
        -> [synthesize_claims if claims exist] -> build_report

Streaming events are emitted via ``AsyncEventStream`` (passed through state)
so the TUI can show real-time progress.
"""

from __future__ import annotations

from typing import Any, AsyncGenerator

from langgraph.func import entrypoint

from src.agent.event_stream import AsyncEventStream
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
    stream: AsyncEventStream | None = state.get("stream")

    # ── node: normalize_question ────────────────────────────────────
    if stream:
        stream.emit_sync(AsyncEventStream.node_start("research", "normalize"))
    _step(state, normalize_question)
    if stream:
        stream.emit_sync(AsyncEventStream.node_end("research", "normalize"))

    # ── node: collect_context ───────────────────────────────────────
    if stream:
        stream.emit_sync(AsyncEventStream.node_start("research", "collect_context"))
    _step(state, collect_context)
    if stream:
        stream.emit_sync(AsyncEventStream.node_end("research", "collect_context"))

    # ── node: source_selection ──────────────────────────────────────
    if stream:
        stream.emit_sync(AsyncEventStream.node_start("research", "source_selection"))
    _step(state, source_selection)
    if stream:
        stream.emit_sync(AsyncEventStream.node_end("research", "source_selection"))

    # ── node: read_extract ──────────────────────────────────────────
    if stream:
        stream.emit_sync(AsyncEventStream.node_start("research", "read_extract"))
    _step(state, read_extract)
    if stream:
        stream.emit_sync(AsyncEventStream.node_end("research", "read_extract"))

    # ── node: synthesize_claims (conditional) ───────────────────────
    if state.get("extracted_claims"):
        if stream:
            stream.emit_sync(AsyncEventStream.node_start("research", "synthesize"))
        _step(state, synthesize_claims)
        if stream:
            stream.emit_sync(AsyncEventStream.node_end("research", "synthesize"))

    # ── node: build_report ──────────────────────────────────────────
    if stream:
        stream.emit_sync(AsyncEventStream.node_start("research", "build_report"))
    _step(state, build_report)
    if stream:
        stream.emit_sync(AsyncEventStream.node_end("research", "build_report"))

    return state.get("report", {
        "question": state.get("question", ""),
        "summary": "Research pipeline completed but produced no report.",
        "confidence": "low",
    })


def _step(state: ResearchState, node_fn) -> None:
    """Apply a node's updates to state in-place."""
    state.update(node_fn(state))


# ── Public entry points ───────────────────────────────────────────────


async def run_research(question: str,
                       stream: AsyncEventStream | None = None) -> dict[str, Any]:
    """Run the research pipeline end-to-end.

    Pass an ``AsyncEventStream`` to receive live progress events.
    """
    state = make_initial_state(question, stream=stream)
    return await _research_pipeline.ainvoke(state)


async def run_research_stream(question: str) -> AsyncGenerator[dict[str, Any], None]:
    """Run research with LangGraph v3 event streaming.

    Yields ``.values`` (full state snapshots after each node) and finally
    the output dict.  Also emits progress events to the stream in state.
    """
    stream = AsyncEventStream()
    state = make_initial_state(question, stream=stream)

    # Fan out: consume both LangGraph events and custom stream events.
    lg_stream = await _research_pipeline.astream_events(state, version="v3")

    # ── State snapshots after each super-step ──────────────────────────
    async for snapshot in lg_stream.values:
        yield snapshot

    # ── Final output ───────────────────────────────────────────────────
    final = await lg_stream.output
    yield final
