"""Node 5: Synthesize extracted claims — merge, identify conflicts, flag uncertainty."""

from __future__ import annotations

from langchain_core.messages import SystemMessage
from openai import OpenAI

from src.config import settings
from src.research.prompts.research_prompts import SYNTHESIZE_CLAIMS
from src.research.state import ResearchState


def synthesize_claims(state: ResearchState) -> dict:
    """Merge extracted claims, identify conflicts, and flag uncertainties."""
    claims = state.get("extracted_claims", [])
    equations = state.get("extracted_equations", [])
    notes = state.get("extracted_notes", [])

    if not claims and not equations:
        return {
            "synthesized_claims": [],
            "conflicts": [],
            "messages": [SystemMessage(content="No claims to synthesize.")],
        }

    claims_text = "\n".join(f"- {c}" for c in claims)
    eq_text = "\n".join(f"- {e}" for e in equations)

    client = OpenAI(
        base_url=settings.OPENROUTER_BASE_URL,
        api_key=settings.OPENROUTER_API_KEY or "",
    )

    response = client.chat.completions.create(
        model=settings.MODEL_SYNTHESIS,
        messages=[
            {"role": "system", "content": SYNTHESIZE_CLAIMS},
            {
                "role": "user",
                "content": (
                    f"Claims:\n{claims_text}\n\n"
                    f"Equations:\n{eq_text}\n\n"
                    f"Notes:\n{chr(10).join(notes)}"
                ),
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "synthesis",
                "schema": {
                    "type": "object",
                    "properties": {
                        "synthesized_claims": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "conflicts": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["synthesized_claims", "conflicts"],
                },
            },
        },
    )

    import json

    parsed = json.loads(response.choices[0].message.content or "{}")

    return {
        "synthesized_claims": parsed.get("synthesized_claims", claims),
        "conflicts": parsed.get("conflicts", []),
        "messages": [
            SystemMessage(
                content=(
                    f"Synthesized {len(parsed.get('synthesized_claims', []))} claims, "
                    f"{len(parsed.get('conflicts', []))} conflicts."
                )
            ),
        ],
    }
