"""Node 4: Read sources deeply and extract claims, equations, and notes."""

from __future__ import annotations

from pathlib import Path

from src.config import settings
from src.research.prompts.research_prompts import READ_EXTRACT
from src.research.schemas import Extraction
from src.research.state import ResearchState


def read_extract(state: ResearchState) -> dict:
    """Read selected sources and extract structured findings."""
    sources = state.get("selected_sources", [])
    if not sources:
        return {
            "extracted_claims": [],
            "extracted_equations": [],
            "extracted_notes": ["No sources selected for reading."],
            "messages": ["No sources to read."],
        }

    # Read full content of selected wiki sources.
    full_texts = []
    for src in sources:
        path = src.get("path_or_url", "")
        try:
            p = Path(path)
            if p.exists():
                text = p.read_text(encoding="utf-8", errors="ignore")
                full_texts.append(f"=== {src['title']} ===\n{text[:4000]}")
        except Exception:
            full_texts.append(f"=== {src['title']} ===\n(Could not read)")

    if not full_texts:
        for src in sources:
            snippet = src.get("content_snippet", "")
            if snippet:
                full_texts.append(f"=== {src['title']} ===\n{snippet[:4000]}")

    source_text = "\n\n".join(full_texts)

    llm = settings.get_llm(settings.MODEL_RESEARCH)

    from langchain_core.messages import SystemMessage, HumanMessage

    response = llm.invoke([
        SystemMessage(content=READ_EXTRACT),
        HumanMessage(
            content=(
                f"Question: {state['normalized_question']}\n\n"
                f"Sources:\n{source_text[:12000]}"
            )
        ),
    ])

    parsed = Extraction.model_validate_json(response.content or "{}")

    msg = f"Extracted {len(parsed.extracted_claims)} claims, {len(parsed.extracted_equations)} equations."

    return {
        "extracted_claims": parsed.extracted_claims,
        "extracted_equations": parsed.extracted_equations,
        "extracted_notes": parsed.extracted_notes,
        "messages": [msg],
    }
