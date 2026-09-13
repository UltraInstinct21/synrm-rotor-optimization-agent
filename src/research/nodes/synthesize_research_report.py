"""Synthesized Research Report Node — single-pass synthesis from collected context."""

from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from src.config import settings
from src.research.prompts.research_prompts import (
    SYNTHESIZE_REPORT_SYSTEM,
    SYNTHESIZE_REPORT_TEMPLATE,
)
from src.research.schemas import ReportOutput
from src.research.state import ResearchState


def _parse_report(content: str) -> dict[str, Any] | None:
    """Parse synthesis JSON robustly (strip fences, extract {...}, validate)."""
    text = (content or "").strip()
    if not text:
        return None
    if "```" in text:
        text = "\n".join(l for l in text.splitlines() if not l.strip().startswith("```"))
    start, end = text.find("{"), text.rfind("}")
    candidate = text[start:end + 1] if start != -1 and end > start else text
    try:
        validated = ReportOutput.model_validate_json(candidate)
        return validated.model_dump()
    except Exception:
        pass
    try:
        return json.loads(candidate)
    except Exception:
        return None


def synthesize_research_report(state: ResearchState) -> dict[str, Any]:
    """Single-pass synthesis of research report from collected context.
    
    Consolidates selection, extraction, claim synthesis, and report generation
    into 1 efficient LLM call instead of 4 separate sequential calls.
    """
    question = state.get("normalized_question") or state.get("question", "")
    sources = state.get("all_collected_sources", [])

    if not sources:
        report = {
            "question": question,
            "sources": [],
            "summary": f"No relevant documentation found in wiki for '{question}'.",
            "extracted_claims": [],
            "equations_or_constraints": [],
            "conflicts_or_uncertainties": [],
            "recommended_wiki_updates": [],
            "recommended_code_targets": [],
            "confidence": "low",
            "created_at": datetime.now().isoformat(),
        }
        return {
            "report_summary": report["summary"],
            "report_confidence": "low",
            "report": report,
            "messages": ["Empty report — no sources collected."],
        }

    # Format collected sources for single-pass prompt
    snippets = []
    for s in sources[:8]:  # Top 8 candidate sources
        title = s.get("title", "Doc")
        path = s.get("path_or_url", "")
        content = s.get("content_snippet", "")[:1500]
        snippets.append(f"### Source: {title} ({path})\n{content}")

    context_str = "\n\n".join(snippets)

    prompt = SYNTHESIZE_REPORT_TEMPLATE.format(question=question, context_str=context_str)

    llm = settings.get_llm(settings.MODEL_RESEARCH)

    from langchain_core.messages import SystemMessage, HumanMessage

    try:
        response = settings.invoke_with_fallback(llm, [
            SystemMessage(content=SYNTHESIZE_REPORT_SYSTEM),
            HumanMessage(content=prompt),
        ])
        parsed = _parse_report(response.content or "") or {}
        if not parsed.get("summary"):
            raise ValueError("empty synthesis output")
    except Exception as e:
        parsed = {
            "summary": f"Failed to parse research synthesis: {e}",
            "extracted_claims": [],
            "equations_or_constraints": [],
            "conflicts_or_uncertainties": [],
            "recommended_wiki_updates": [],
            "recommended_code_targets": [],
            "confidence": "low",
        }

    report = {
        "question": question,
        "sources": [
            {"title": s.get("title", ""), "type": s.get("type", "wiki"), "path_or_url": s.get("path_or_url", "")}
            for s in sources[:8]
        ],
        "summary": parsed.get("summary", ""),
        "extracted_claims": parsed.get("extracted_claims", []),
        "equations_or_constraints": parsed.get("equations_or_constraints", []),
        "conflicts_or_uncertainties": parsed.get("conflicts_or_uncertainties", []),
        "recommended_wiki_updates": parsed.get("recommended_wiki_updates", []),
        "recommended_code_targets": parsed.get("recommended_code_targets", []),
        "confidence": parsed.get("confidence", "medium"),
        "created_at": datetime.now().isoformat(),
    }

    return {
        "report_summary": report["summary"],
        "report_confidence": report["confidence"],
        "report": report,
        "messages": [f"Single-pass research report generated ({len(report['extracted_claims'])} claims extracted)."],
    }
