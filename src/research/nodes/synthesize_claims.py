"""Node 5: Synthesize extracted claims — merge, identify conflicts, flag uncertainty."""

from __future__ import annotations

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

    llm = settings.get_llm(settings.MODEL_SYNTHESIS)

    from langchain_core.messages import SystemMessage, HumanMessage

    response = llm.invoke([
        SystemMessage(content=SYNTHESIZE_CLAIMS),
        HumanMessage(
            content=(
                f"Claims:\n{claims_text}\n\n"
                f"Equations:\n{eq_text}\n\n"
                f"Notes:\n{chr(10).join(notes)}"
            )
        ),
    ])

    parsed = Synthesis.model_validate_json(response.content or "{}")

    msg = (
        f"Synthesized {len(parsed.synthesized_claims)} claims, "
        f"{len(parsed.conflicts)} conflicts."
    )

    return {
        "synthesized_claims": parsed.synthesized_claims,
        "conflicts": parsed.conflicts,
        "messages": [msg],
    }
