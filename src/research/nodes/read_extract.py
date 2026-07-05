"""Node 4: Read sources deeply and extract claims, equations, and notes."""

from __future__ import annotations

from pathlib import Path

from langchain_core.messages import SystemMessage
from openai import OpenAI

from src.config import settings
from src.research.prompts.research_prompts import READ_EXTRACT
from src.research.state import ResearchState


def read_extract(state: ResearchState) -> dict:
    """Read selected sources and extract structured findings."""
    sources = state.get("selected_sources", [])
    if not sources:
        return {
            "extracted_claims": [],
            "extracted_equations": [],
            "extracted_notes": ["No sources selected for reading."],
            "messages": [SystemMessage(content="No sources to read.")],
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
        # Use the snippets collected earlier.
        for src in sources:
            snippet = src.get("content_snippet", "")
            if snippet:
                full_texts.append(f"=== {src['title']} ===\n{snippet[:4000]}")

    source_text = "\n\n".join(full_texts)

    client = OpenAI(
        base_url=settings.OPENROUTER_BASE_URL,
        api_key=settings.OPENROUTER_API_KEY or "",
    )

    response = client.chat.completions.create(
        model=settings.MODEL_RESEARCH,
        messages=[
            {"role": "system", "content": READ_EXTRACT},
            {
                "role": "user",
                "content": (
                    f"Question: {state['normalized_question']}\n\n"
                    f"Sources:\n{source_text[:12000]}"
                ),
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "extraction",
                "schema": {
                    "type": "object",
                    "properties": {
                        "extracted_claims": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "extracted_equations": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "extracted_notes": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["extracted_claims", "extracted_equations", "extracted_notes"],
                },
            },
        },
    )

    import json

    parsed = json.loads(response.choices[0].message.content or "{}")

    return {
        "extracted_claims": parsed.get("extracted_claims", []),
        "extracted_equations": parsed.get("extracted_equations", []),
        "extracted_notes": parsed.get("extracted_notes", []),
        "messages": [
            SystemMessage(
                content=(
                    f"Extracted {len(parsed.get('extracted_claims', []))} claims, "
                    f"{len(parsed.get('extracted_equations', []))} equations."
                )
            ),
        ],
    }
