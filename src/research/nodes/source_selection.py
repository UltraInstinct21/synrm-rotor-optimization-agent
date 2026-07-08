"""Node 3: Source selection — choose the top sources for deep reading."""

from __future__ import annotations

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

    llm = settings.get_llm(settings.MODEL_RESEARCH)

    from langchain_core.messages import SystemMessage, HumanMessage

    sources_text = "\n".join(
        f"- {s['title']} ({s['type']}): {s.get('path_or_url', '')}"
        for s in sources[:10]
    )

    response = llm.invoke([
        SystemMessage(content=SOURCE_SELECTION),
        HumanMessage(
            content=(
                f"Question: {state['normalized_question']}\n\n"
                f"Candidate sources:\n{sources_text}"
            )
        ),
    ])

    parsed = SourceSelection.model_validate_json(response.content or "{}")
    selected = [s.model_dump() for s in parsed.selected_sources] or sources[:3]

    msg = f"Selected {len(selected)} sources for deep reading."

    return {
        "selected_sources": selected,
        "messages": [msg],
    }
