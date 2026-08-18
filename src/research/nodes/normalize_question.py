"""Node 1: Normalize the research question — clarify scope and domain terms."""

from __future__ import annotations

from src.config import settings
from src.research.prompts.research_prompts import NORMALIZE_QUESTION
from src.research.schemas import NormalizedQuestion
from src.research.state import ResearchState


def normalize_question(state: ResearchState) -> dict:
    """Clarify the question and identify domain terms using an LLM call."""
    llm = settings.get_llm(settings.MODEL_RESEARCH)

    from langchain_core.messages import SystemMessage, HumanMessage

    try:
        response = llm.invoke([
            SystemMessage(content=NORMALIZE_QUESTION),
            HumanMessage(content=f"Research question: {state['question']}"),
        ])
        parsed = NormalizedQuestion.model_validate_json(response.content or "{}")
        return {
            "normalized_question": parsed.normalized_question,
            "domain_terms": parsed.domain_terms,
            "messages": [f"Normalized: {parsed.normalized_question}"],
        }
    except Exception as e:
        return {
            "normalized_question": state["question"],
            "domain_terms": [],
            "messages": [f"Normalization failed, using original question: {e}"],
        }
