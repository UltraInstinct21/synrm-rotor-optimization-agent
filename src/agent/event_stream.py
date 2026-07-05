"""Streaming event types and async event bus for live progress.

Provides:
- ``StreamEventType`` — enum of all event kinds.
- ``StreamEvent`` — dataclass carrying subsystem, node, message, data.
- ``AsyncEventStream`` — async generator + publisher bridge, used by
  sub-systems to emit events and by UI layers to consume them.

Usage (publisher side — research graph, orchestrator, etc.)::

    stream = AsyncEventStream()
    async with stream.publisher() as pub:
        pub.emit(StreamEvent(type=...))
        # ...do work...
        pub.emit(StreamEvent(type=...))

Usage (consumer side — TUI, CLI)::

    async for event in stream:
        # handle event
    # when publisher context exits, the stream terminates
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, AsyncIterator


class StreamEventType(Enum):
    """Types of events emitted during workflow execution."""

    # Orchestrator-level
    WORKFLOW_START = "workflow_start"
    WORKFLOW_END = "workflow_end"
    SUBSYSTEM_START = "subsystem_start"
    SUBSYSTEM_END = "subsystem_end"

    # Research graph node lifecycle
    NODE_START = "node_start"
    NODE_END = "node_end"
    NODE_PROGRESS = "node_progress"

    # LLM token streaming (future)
    LLM_TOKEN = "llm_token"

    # Numeric progress (sweep, experiment candidates)
    PROGRESS = "progress"

    # Text chunks (report synthesis, code results)
    TEXT_CHUNK = "text_chunk"

    # Errors
    ERROR = "error"


@dataclass
class StreamEvent:
    """A single streaming event from any subsystem.

    Attributes:
        type: Event type — dictates how the consumer renders it.
        subsystem: Which subsystem emitted it (``"research"``,
            ``"orchestrator"``, ``"coding"``, ``"wiki"``,
            ``"experiment"``, ``"sweep"``).
        node: Optional node / step name within the subsystem.
        message: Human-readable progress message (single line).
        data: Optional structured payload (dict, str, etc.).
        timestamp: Unix timestamp (set automatically on creation).
    """

    type: StreamEventType
    subsystem: str
    node: str | None = None
    message: str = ""
    data: Any = None
    timestamp: float = field(default_factory=time.time)


class AsyncEventStream:
    """Bidirectional async event stream.

    Publisher side calls ``emit()`` inside a ``publisher()`` context.
    Consumer side iterates ``async for event in stream``.
    When the publisher context exits the stream iterator stops.
    """

    def __init__(self, maxsize: int = 256) -> None:
        self._queue: asyncio.Queue[StreamEvent | None] = asyncio.Queue(maxsize)
        self._done: bool = False

    # ── Publisher side ──────────────────────────────────────────────

    async def emit(self, event: StreamEvent) -> None:
        """Push an event onto the stream (non-blocking with backpressure)."""
        if not self._done:
            await self._queue.put(event)

    def emit_sync(self, event: StreamEvent) -> None:
        """Synchronous variant — for use inside sync LangGraph nodes.

        Uses ``call_soon_threadsafe`` to bridge sync → async safely.
        """
        if not self._done:
            loop = asyncio.get_event_loop()
            loop.call_soon_threadsafe(self._queue.put_nowait, event)

    def done(self) -> None:
        """Signal end of stream."""
        if not self._done:
            self._done = True
            loop = asyncio.get_event_loop()
            loop.call_soon_threadsafe(self._queue.put_nowait, None)

    # ── Consumer side ───────────────────────────────────────────────

    def __aiter__(self) -> AsyncIterator[StreamEvent]:
        return self._aiterator()

    async def _aiterator(self) -> AsyncIterator[StreamEvent]:
        while True:
            item = await self._queue.get()
            if item is None:
                return
            yield item

    # ── Factory helpers ─────────────────────────────────────────────

    @staticmethod
    def node_start(subsystem: str, node: str, message: str = "") -> StreamEvent:
        return StreamEvent(
            type=StreamEventType.NODE_START,
            subsystem=subsystem,
            node=node,
            message=message or f"Starting {node}...",
        )

    @staticmethod
    def node_end(subsystem: str, node: str, message: str = "") -> StreamEvent:
        return StreamEvent(
            type=StreamEventType.NODE_END,
            subsystem=subsystem,
            node=node,
            message=message or f"Finished {node}.",
        )

    @staticmethod
    def progress(subsystem: str, current: int, total: int,
                 message: str = "") -> StreamEvent:
        return StreamEvent(
            type=StreamEventType.PROGRESS,
            subsystem=subsystem,
            message=message or f"{current}/{total}",
            data={"current": current, "total": total},
        )

    @staticmethod
    def text_chunk(subsystem: str, text: str, node: str | None = None) -> StreamEvent:
        return StreamEvent(
            type=StreamEventType.TEXT_CHUNK,
            subsystem=subsystem,
            node=node,
            message="",
            data=text,
        )

    @staticmethod
    def error(subsystem: str, message: str, node: str | None = None) -> StreamEvent:
        return StreamEvent(
            type=StreamEventType.ERROR,
            subsystem=subsystem,
            node=node,
            message=message,
        )

    @staticmethod
    def subsystem_start(subsystem: str, message: str = "") -> StreamEvent:
        return StreamEvent(
            type=StreamEventType.SUBSYSTEM_START,
            subsystem=subsystem,
            message=message or f"Starting {subsystem}...",
        )

    @staticmethod
    def subsystem_end(subsystem: str, message: str = "") -> StreamEvent:
        return StreamEvent(
            type=StreamEventType.SUBSYSTEM_END,
            subsystem=subsystem,
            message=message or f"Finished {subsystem}.",
        )
