"""Node 5: Synthesize extracted claims — merge, identify conflicts, flag uncertainty."""

from __future__ import annotations

from src.agent.event_stream import AsyncEventStream
from src.config import settings
from src.research.prompts.research_prompts import SYNTHESIZE_CLAIMS
from src.research.schemas import Synthesis
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
            "messages": ["No claims to synthesize."],
        }

    claims_text = "\n".join(f"- {c}" for c in claims)
    eq_text = "\n".join(f"- {e}" for e in equations)

    client = settings.get_llm_client()

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
                "schema": Synthesis.model_json_schema(),
            },
        },
    )

    parsed = Synthesis.model_validate_json(
        response.choices[0].message.content or "{}"
    )

    msg = (
        f"Synthesized {len(parsed.synthesized_claims)} claims, "
        f"{len(parsed.conflicts)} conflicts."
    )
    stream: AsyncEventStream | None = state.get("stream")
    if stream:
        stream.emit_sync(AsyncEventStream.text_chunk("research", msg, "synthesize"))

    return {
        "synthesized_claims": parsed.synthesized_claims,
        "conflicts": parsed.conflicts,
        "messages": [msg],
    }
