"""Node 3: Source selection — choose the top sources for deep reading."""

from __future__ import annotations

from langchain_core.messages import SystemMessage
from openai import OpenAI

from src.config import settings
from src.research.prompts.research_prompts import SOURCE_SELECTION
from src.research.state import ResearchState


def source_selection(state: ResearchState) -> dict:
    """Rank and select the top sources for deep reading."""
    sources = state.get("all_collected_sources", [])
    if not sources:
        return {
            "selected_sources": [],
            "messages": [SystemMessage(content="No sources found to select.")],
        }

    client = OpenAI(
        base_url=settings.OPENROUTER_BASE_URL,
        api_key=settings.OPENROUTER_API_KEY or "",
    )

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
                "schema": {
                    "type": "object",
                    "properties": {
                        "selected_sources": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {"type": "string"},
                                    "type": {"type": "string"},
                                    "path_or_url": {"type": "string"},
                                    "relevance": {"type": "string"},
                                },
                                "required": ["title", "type", "path_or_url"],
                            },
                        },
                    },
                    "required": ["selected_sources"],
                },
            },
        },
    )

    import json

    parsed = json.loads(response.choices[0].message.content or "{}")
    selected = parsed.get("selected_sources", sources[:3])

    return {
        "selected_sources": selected,
        "messages": [
            SystemMessage(content=f"Selected {len(selected)} sources for deep reading.")
        ],
    }
