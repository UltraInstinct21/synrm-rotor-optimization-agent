"""Node 1: Normalize the research question — clarify scope and domain terms."""

from __future__ import annotations

from src.agent.event_stream import AsyncEventStream
from src.config import settings
from src.research.prompts.research_prompts import NORMALIZE_QUESTION
from src.research.schemas import NormalizedQuestion
from src.research.state import ResearchState


def normalize_question(state: ResearchState) -> dict:
    """Clarify the question and identify domain terms using an LLM call."""
    client = settings.get_llm_client()

    response = client.chat.completions.create(
        model=settings.MODEL_RESEARCH,
        messages=[
            {"role": "system", "content": NORMALIZE_QUESTION},
            {"role": "user", "content": f"Research question: {state['question']}"},
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "normalized",
                "schema": NormalizedQuestion.model_json_schema(),
            },
        },
    )

    parsed = NormalizedQuestion.model_validate_json(
        response.choices[0].message.content or "{}"
    )

    stream: AsyncEventStream | None = state.get("stream")
    if stream:
        stream.emit_sync(AsyncEventStream.text_chunk(
            "research", f"Normalized: {parsed.normalized_question}", "normalize"
        ))

    return {
        "normalized_question": parsed.normalized_question,
        "domain_terms": parsed.domain_terms,
        "messages": [f"Normalized: {parsed.normalized_question}"],
    }
