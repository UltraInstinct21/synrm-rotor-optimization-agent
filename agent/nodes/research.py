"""Phase 1 — Research Node: web ingest, chunking, embedding, entity extraction, wiki writing."""

from datetime import datetime

from agent.state import AgentState
from agent.tools.chunker import chunk_text
from agent.tools.embedder import embed_texts
from agent.tools.chroma import add_document, query_similar
from agent.tools.wiki import write_page, update_index
from agent.tools.web_search import search_research_topic
from agent.models import call_llm_structured
from pydantic import BaseModel
from typing import Literal


class ExtractedEntity(BaseModel):
    """Schema for LLM entity/concept extraction."""
    title: str
    type: Literal["entity", "concept"]
    content: str
    relations: list[str] = []
    tags: list[str] = []


def research_node(state: AgentState) -> AgentState:
    """Execute Phase 1: research, chunk, embed, extract, wiki-write."""
    state["phase"] = "research"

    # Mark as running
    state["phase_status"]["research"] = {"status": "running", "error": None}
    errors = []

    try:
        # 1. Research the motor topic from motor_spec
        topic = (
            f"SynRM {state['motor_spec'].get('power_kw', 45)}kW IE5 rotor design: "
            f"{state['motor_spec'].get('poles', 4)}-pole, "
            f"barrier optimization, efficiency >= {state['motor_spec'].get('target_efficiency', 96)}%"
        )
        research_text = search_research_topic(topic)

        # 2. Chunk the research text
        source_id = f"research-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        chunks = list(chunk_text(research_text, source_id=source_id))

        # 3. Embed all chunks
        texts = [c["text"] for c in chunks]
        embeddings = embed_texts(texts)

        # 4. Add to ChromaDB
        for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
            doc_id = f"{source_id}-chunk-{i}"
            add_document(
                "sources",
                doc_id,
                chunk["text"],
                emb,
                metadata={
                    "source_id": source_id,
                    "chunk_idx": i,
                    "section": "research",
                    "tags": "synrm,barrier,optimization",
                },
            )

        # 5. Extract entities/concepts via LLM
        system_prompt = (
            "You are a knowledge extraction assistant for SynRM motor design. "
            "Extract entities (specific named things: researchers, motors, companies) "
            "and concepts (abstract ideas: formulas, techniques, phenomena) from the text. "
            "Each extraction should have a clear title, full content description, "
            "related wikilinks ([[Title]]), and relevant tags."
        )
        extraction_result = call_llm_structured(
            system_prompt,
            f"Extract entities and concepts from this research text:\n\n{research_text[:4000]}",
            ExtractedEntity,
            node="research",
        )

        # 6. Write extracted items to wiki (skip duplicates via simple slug check)
        entities_created = []
        concepts_created = []

        if extraction_result:
            page_type = extraction_result.type
            title = extraction_result.title
            # Write the page — wiki.write_page handles path creation
            path = write_page(
                title=title,
                page_type=page_type,
                content=extraction_result.content,
                tags=extraction_result.tags,
                relations=extraction_result.relations,
            )
            if page_type == "entity":
                entities_created.append(path)
            else:
                concepts_created.append(path)

        # 7. Update wiki index
        update_index()

        # Mark done
        state["phase_status"]["research"] = {"status": "done", "error": None}
        state["wiki_entities_created"] = entities_created
        state["wiki_concepts_created"] = concepts_created

    except Exception as e:
        errors.append(str(e))
        state["phase_status"]["research"] = {"status": "failed", "error": str(e)}
        # Graceful degradation: continue with what we have

    if errors:
        state["error_log"] = state.get("error_log", [])
        state["error_log"].append({
            "phase": "research",
            "error": str(errors),
            "timestamp": datetime.now().isoformat(),
        })

    return state
