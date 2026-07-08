"""Node 6: Build the final ResearchReport from synthesized findings."""

from __future__ import annotations

from datetime import datetime

from src.config import settings
from src.research.prompts.research_prompts import BUILD_REPORT
from src.research.schemas import ReportOutput
from src.research.state import ResearchState


def build_report(state: ResearchState) -> dict:
    """Construct the ResearchReport dict from synthesized findings."""
    claims = state.get("synthesized_claims", [])
    conflicts = state.get("conflicts", [])
    equations = state.get("extracted_equations", [])
    sources = state.get("selected_sources", [])
    question = state.get("normalized_question", state["question"])

    if not claims:
        report = {
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
        }
        return {
            "report_summary": "Nothing was synthesized.",
            "report_confidence": "low",
            "report": report,
            "messages": ["Built empty report — no claims to report."],
        }

    claims_text = "\n".join(f"- {c}" for c in claims)
    conflicts_text = "\n".join(f"- {c}" for c in conflicts)
    eq_text = "\n".join(f"- {e}" for e in equations)

    llm = settings.get_llm(settings.MODEL_RESEARCH)

    from langchain_core.messages import SystemMessage, HumanMessage

    response = llm.invoke([
        SystemMessage(content=BUILD_REPORT),
        HumanMessage(
            content=(
                f"Question: {question}\n\n"
                f"Synthesized claims:\n{claims_text}\n\n"
                f"Conflicts:\n{conflicts_text}\n\n"
                f"Equations:\n{eq_text}\n\n"
                f"Sources: {len(sources)} selected."
            )
        ),
    ])

    parsed = ReportOutput.model_validate_json(response.content or "{}")

    report = {
        "question": question,
        "sources": [
            {"title": s.get("title", ""), "type": s.get("type", ""),
             "path_or_url": s.get("path_or_url", "")}
            for s in sources
        ],
        "summary": parsed.summary,
        "extracted_claims": claims,
        "equations_or_constraints": equations,
        "conflicts_or_uncertainties": conflicts,
        "recommended_wiki_updates": parsed.recommended_wiki_updates,
        "recommended_code_targets": parsed.recommended_code_targets,
        "confidence": parsed.confidence,
        "created_at": datetime.now().isoformat(),
    }

    msg = f"Built research report. Confidence: {parsed.confidence}"

    return {
        "report_summary": report["summary"],
        "report_confidence": report["confidence"],
        "report": report,
        "messages": [msg],
    }
