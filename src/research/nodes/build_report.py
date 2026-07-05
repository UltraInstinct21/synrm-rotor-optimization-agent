"""Node 6: Build the final ResearchReport from synthesized findings."""

from __future__ import annotations

from datetime import datetime

from langchain_core.messages import SystemMessage
from openai import OpenAI

from src.config import settings
from src.research.prompts.research_prompts import BUILD_REPORT
from src.research.state import ResearchState


def build_report(state: ResearchState) -> dict:
    """Construct the ResearchReport dict from synthesized findings."""
    claims = state.get("synthesized_claims", [])
    conflicts = state.get("conflicts", [])
    equations = state.get("extracted_equations", [])
    sources = state.get("selected_sources", [])
    question = state.get("normalized_question", state["question"])

    if not claims:
        return {
            "report_summary": "Nothing was synthesized.",
            "report_confidence": "low",
            "report": {
                "question": question,
                "sources": sources,
                "summary": "Nothing was synthesized.",
                "extracted_claims": [],
                "equations_or_constraints": [],
                "conflicts_or_uncertainties": [],
                "recommended_wiki_updates": [],
                "recommended_code_targets": [],
                "confidence": "low",
                "created_at": datetime.now().isoformat(),
            },
            "messages": [SystemMessage(content="Built empty report — no claims to report.")],
        }

    claims_text = "\n".join(f"- {c}" for c in claims)
    conflicts_text = "\n".join(f"- {c}" for c in conflicts)
    eq_text = "\n".join(f"- {e}" for e in equations)

    client = OpenAI(
        base_url=settings.OPENROUTER_BASE_URL,
        api_key=settings.OPENROUTER_API_KEY or "",
    )

    response = client.chat.completions.create(
        model=settings.MODEL_RESEARCH,
        messages=[
            {"role": "system", "content": BUILD_REPORT},
            {
                "role": "user",
                "content": (
                    f"Question: {question}\n\n"
                    f"Synthesized claims:\n{claims_text}\n\n"
                    f"Conflicts:\n{conflicts_text}\n\n"
                    f"Equations:\n{eq_text}\n\n"
                    f"Sources: {len(sources)} selected."
                ),
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "report",
                "schema": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string"},
                        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
                        "recommended_wiki_updates": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "recommended_code_targets": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["summary", "confidence", "recommended_wiki_updates", "recommended_code_targets"],
                },
            },
        },
    )

    import json

    parsed = json.loads(response.choices[0].message.content or "{}")

    report = {
        "question": question,
        "sources": [
            {"title": s.get("title", ""), "type": s.get("type", ""), "path_or_url": s.get("path_or_url", "")}
            for s in sources
        ],
        "summary": parsed.get("summary", ""),
        "extracted_claims": claims,
        "equations_or_constraints": equations,
        "conflicts_or_uncertainties": conflicts,
        "recommended_wiki_updates": parsed.get("recommended_wiki_updates", []),
        "recommended_code_targets": parsed.get("recommended_code_targets", []),
        "confidence": parsed.get("confidence", "medium"),
        "created_at": datetime.now().isoformat(),
    }

    return {
        "report_summary": report["summary"],
        "report_confidence": report["confidence"],
        "report": report,
        "messages": [SystemMessage(content=f"Built research report. Confidence: {report['confidence']}")],
    }
