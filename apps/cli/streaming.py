"""Streaming output — process events from run_request_graph_streamed."""

from __future__ import annotations

from typing import Any

from apps.cli.rendering import Renderer


class StreamHandler:
    """Processes streaming events from the agent graph and renders them."""

    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer
        self._current_label: str = ""

    async def handle_stream(self, stream) -> str:
        """Consume an async event stream and render each event.

        Parameters
        ----------
        stream : AsyncIterator[dict]
            From run_request_graph_streamed() or run_request_streamed().

        Returns
        -------
        str : The final synthesis text.
        """
        synthesis = ""
        async for event in stream:
            etype = event.get("type", "")

            if etype == "category":
                self.renderer.panel_classify(event["data"])

            elif etype == "info":
                label = event.get("label", "info")
                data = event.get("data", "")
                self.renderer.panel_execute(label, data)

            elif etype == "token":
                # Token streaming — handled separately by the REPL
                pass

            elif etype == "synthesis":
                synthesis = event.get("data", "")

            elif etype == "error":
                self.renderer.panel_error(event.get("data", "Unknown error"))

        if synthesis:
            self.renderer.panel_synthesis(synthesis)

        return synthesis

    def render_tokens(self, tokens: list[str]) -> str:
        """Join collected tokens into a single string."""
        return "".join(tokens)