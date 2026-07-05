"""Node 3: Source selection — choose the top sources for deep reading."""

from __future__ import annotations

from src.agent.event_stream import AsyncEventStream
from src.config import settings
from src.research.prompts.research_prompts import SOURCE_SELECTION
from src.research.schemas import SourceSelection
from src.research.state import ResearchState


def source_selection(state: ResearchState) -> dict:
    """Rank and select the top sources for deep reading."""
    sources = state.get("all_collected_sources", [])
    if not sources:
        return {
            "selected_sources": [],
            "messages": ["No sources found to select."],
        }

    client = settings.get_llm_client()

    sources_text = "\n".join(
        f"- {s['title']} ({s['type']}): {s.get('path_or_url', '')}"
        for s in sources[:10]
    )

    response = client.chat.completions.create(
        model=settings.MODEL_RESEARCH,
        messages=[
            {"role": "system", "content": SOURCE_SELECTION},
            {
                "role": "user",
                "content": (
                    f"Question: {state['normalized_question']}\n\n"
                    f"Candidate sources:\n{sources_text}"
                ),
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "selection",
                "schema": SourceSelection.model_json_schema(),
            },
        },
    )

    parsed = SourceSelection.model_validate_json(
        response.choices[0].message.content or "{}"
    )
    selected = [s.model_dump() for s in parsed.selected_sources] or sources[:3]

    msg = f"Selected {len(selected)} sources for deep reading."
    stream: AsyncEventStream | None = state.get("stream")
    if stream:
        stream.emit_sync(AsyncEventStream.text_chunk("research", msg, "source_selection"))

    return {
        "selected_sources": selected,
        "messages": [msg],
    }
