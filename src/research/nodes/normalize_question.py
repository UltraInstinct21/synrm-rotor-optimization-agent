"""Node 1: Normalize the research question — clarify scope and domain terms."""

from __future__ import annotations

from langchain_core.messages import HumanMessage, SystemMessage

from src.research.state import ResearchState
from src.research.prompts.research_prompts import NORMALIZE_QUESTION
from src.config import settings


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
                "schema": {
                    "type": "object",
                    "properties": {
                        "normalized_question": {"type": "string"},
                        "domain_terms": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["normalized_question", "domain_terms"],
                },
            },
        },
    )

    import json

    parsed = json.loads(response.choices[0].message.content or "{}")

    return {
        "normalized_question": parsed.get(
            "normalized_question", state["question"]
        ),
        "domain_terms": parsed.get("domain_terms", []),
        "messages": [
            SystemMessage(content=f"Normalized: {parsed.get('normalized_question', '')}"),
        ],
    }
