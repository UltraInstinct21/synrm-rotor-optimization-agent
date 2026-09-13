"""Node 1: Normalize the research question — clarify scope and domain terms."""

from __future__ import annotations

import json
import re

from src.config import settings
from src.research.prompts.research_prompts import NORMALIZE_QUESTION
from src.research.schemas import NormalizedQuestion
from src.research.state import ResearchState

_STOPWORDS = frozenset({
    "what", "whats", "how", "does", "do", "the", "a", "an", "and", "or",
    "for", "with", "about", "affect", "effect", "motor", "question",
})

_PARAM_LIKE = re.compile(r"^[A-Za-z][A-Za-z0-9_\[\]]*$")


def _keyword_fallback(question: str) -> list[str]:
    """Deterministic keyword fallback so collection never runs on zero terms."""
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_\-]+", question)
    terms: list[str] = []
    for tok in tokens:
        low = tok.lower()
        if len(tok) < 3 or low in _STOPWORDS:
            continue
        terms.append(tok)
        if len(terms) >= 8:
            break
    return terms


def _parse_normalized(content: str) -> tuple[str, list[str]] | None:
    """Robust JSON parse: strip fences, extract first {...} block, validate."""
    text = (content or "").strip()
    if not text:
        return None
    if "```" in text:
        text = "\n".join(l for l in text.splitlines() if not l.strip().startswith("```"))
    start, end = text.find("{"), text.rfind("}")
    candidate = text[start:end + 1] if start != -1 and end > start else text
    try:
        parsed = NormalizedQuestion.model_validate_json(candidate)
        return parsed.normalized_question, list(parsed.domain_terms)
    except Exception:
        pass
    try:
        raw = json.loads(candidate)
        return str(raw.get("normalized_question", "")), list(raw.get("domain_terms", []))
    except Exception:
        return None


def normalize_question(state: ResearchState) -> dict:
    """Clarify the question and identify domain terms using an LLM call."""
    llm = settings.get_llm(settings.MODEL_RESEARCH)

    from langchain_core.messages import SystemMessage, HumanMessage

    try:
        response = settings.invoke_with_fallback(llm, [
            SystemMessage(content=NORMALIZE_QUESTION),
            HumanMessage(content=f"Research question: {state['question']}"),
        ])
        result = _parse_normalized(response.content or "")
        if result and result[0].strip():
            norm, terms = result
            return {
                "normalized_question": norm.strip(),
                "domain_terms": [t for t in terms if t][:10],
                "messages": [f"Normalized: {norm.strip()}"],
            }
        raise ValueError("empty or unparseable normalizer output")
    except Exception as e:
        fallback_terms = _keyword_fallback(state.get("question", ""))
        return {
            "normalized_question": state["question"],
            "domain_terms": fallback_terms,
            "messages": [f"Normalization fallback (keywords={fallback_terms}): {e}"],
        }
