"""Synthesized Research Report Node — single-pass synthesis from collected context."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from src.config import settings
from src.research.state import ResearchState


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

    prompt = f"""You are a motor engineering research assistant. Analyze the provided source snippets and synthesize a comprehensive technical answer.

Question: {question}

Source Context:
{context_str}

Respond with a JSON object containing:
- "summary": Clear, direct answer to the user's question based on context.
- "extracted_claims": List of key technical claims/facts extracted.
- "equations_or_constraints": List of design equations or geometric constraints mentioned.
- "conflicts_or_uncertainties": Any conflicting statements or missing details.
- "recommended_wiki_updates": Suggested updates to wiki pages if needed.
- "recommended_code_targets": Suggested PyMotorCAD parameters or python run files to modify.
- "confidence": "high", "medium", or "low".
"""

    llm = settings.get_llm(settings.MODEL_RESEARCH)

    from langchain_core.messages import SystemMessage, HumanMessage
    import json

    try:
        response = llm.invoke([
            SystemMessage(content="You are an expert motor engineering research synthesizer. Output strictly valid JSON matching the requested structure."),
            HumanMessage(content=prompt),
        ])
        content_text = response.content or "{}"
        # Strip markdown code blocks if present
        if "```" in content_text:
            lines = content_text.splitlines()
            content_text = "\n".join(l for l in lines if not l.strip().startswith("```"))
        
        parsed = json.loads(content_text.strip())
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
