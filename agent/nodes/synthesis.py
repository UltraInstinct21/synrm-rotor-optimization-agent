"""Phase 2 — Synthesis Node: cross-reference entities/concepts, detect gaps, derive insights."""

import os
from datetime import datetime

from agent.state import AgentState
from agent.tools.wiki import write_page, update_index
from agent.models import call_llm

WIKI_DIR = r"D:\SRM\Motor _CAD\ScriptFiles\wiki"


def _count_pages(subdir: str) -> int:
    """Count .md files in a wiki subdirectory."""
    d = os.path.join(WIKI_DIR, subdir)
    if not os.path.isdir(d):
        return 0
    return len([f for f in os.listdir(d) if f.endswith(".md")])


def _read_all_pages(subdir: str) -> str:
    """Read all .md files in a wiki subdirectory and return as concatenated text."""
    d = os.path.join(WIKI_DIR, subdir)
    if not os.path.isdir(d):
        return ""
    texts = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            fp = os.path.join(d, fn)
            with open(fp, "r", encoding="utf-8") as f:
                texts.append(f"=== {fn} ===\n{f.read()}")
    return "\n\n".join(texts)


def _log(state: AgentState, msg: str) -> None:
    phase = state.get("phase", "?")
    print(f"  [{phase:<12}] {msg}")


def synthesis_node(state: AgentState) -> AgentState:
    """Execute Phase 2: gap analysis, conflict resolution, insight generation."""
    state["phase"] = "synthesis"
    state["phase_status"]["synthesis"] = {"status": "running", "error": None}
    errors = []

    try:
        # 1. Gap Analysis: count pages in each category
        _log(state, "performing gap analysis...")
        entity_count = _count_pages("entities")
        concept_count = _count_pages("concepts")
        source_count = _count_pages("sources")
        synthesis_count = _count_pages("synthesis")

        gap_analysis = {
            "entities": entity_count,
            "concepts": concept_count,
            "sources": source_count,
            "synthesis": synthesis_count,
            "has_gaps": entity_count == 0 or concept_count == 0,
            "note": "",
        }

        if entity_count < 3:
            gap_analysis["note"] = "Low entity count — more research recommended"
        if concept_count < 3:
            gap_analysis["note"] += "; Low concept count" if gap_analysis["note"] else "Low concept count — more research recommended"

        # 2. Read existing pages to generate synthesis
        entities_text = _read_all_pages("entities")
        concepts_text = _read_all_pages("concepts")

        _log(state, f"found {entity_count} entities, {concept_count} concepts, {source_count} sources")

        if entities_text or concepts_text:
            # 3. Generate synthesis via LLM
            _log(state, "calling LLM for cross-reference synthesis (may take 30-60s)...")
            system_prompt = (
                "You are a synthesis engine for SynRM motor design knowledge. "
                "Given the existing wiki content, produce a condensed synthesis covering: "
                "1) Key design rules derived from literature, "
                "2) Parameter ranges and their trade-offs, "
                "3) Any contradictions found across sources and how to resolve them. "
                "Use specific numbers and cite sources."
            )
            user_prompt = (
                f"## Entities ({entity_count} pages)\n{entities_text[:3000]}\n\n"
                f"## Concepts ({concept_count} pages)\n{concepts_text[:3000]}\n\n"
                f"Motor spec: {state.get('motor_spec', {})}\n\n"
                "Generate a synthesis covering design rules, contradictions, and insights."
            )

            synthesis_content = call_llm(system_prompt, user_prompt, node="synthesis")

            _log(state, "LLM synthesis complete, writing wiki pages...")
            # 4. Write synthesis page
            path = write_page(
                title="SynRM Design Rules from Literature",
                page_type="synthesis",
                content=synthesis_content,
                tags=["synthesis", "design-rules", "literature-review"],
            )
            state["wiki_synthesis"] = [path]

            # Also write gap analysis
            gap_content = (
                f"## Gap Analysis\n\n"
                f"- Entities: {entity_count}\n"
                f"- Concepts: {concept_count}\n"
                f"- Sources: {source_count}\n"
                f"- Synthesis: {synthesis_count}\n\n"
                f"**Assessment:** {gap_analysis['note'] or 'Knowledge base has reasonable coverage.'}\n"
            )
            write_page(
                title="Knowledge Gaps",
                page_type="synthesis",
                content=gap_content,
                tags=["gaps", "coverage"],
            )

        # 5. Update wiki index
        update_index()

        state["phase_status"]["synthesis"] = {"status": "done", "error": None}

    except Exception as e:
        errors.append(str(e))
        state["phase_status"]["synthesis"] = {"status": "failed", "error": str(e)}
        # Graceful degradation: update index at least
        try:
            update_index()
        except Exception:
            pass

    if errors:
        state["error_log"] = state.get("error_log", [])
        state["error_log"].append({
            "phase": "synthesis",
            "error": str(errors),
            "timestamp": datetime.now().isoformat(),
        })

    return state
