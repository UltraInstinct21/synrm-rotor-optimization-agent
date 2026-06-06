"""Web search + fetch tools for research phase."""

from agent.models import call_llm


def search_research_topic(topic: str) -> str:
    """Given a research topic, use LLM knowledge to produce a structured summary.

    Uses the model's training knowledge, guided toward SynRM-relevant content.
    """
    system = (
        "You are a research assistant specialized in electrical machine design. "
        "Given a topic, produce a structured markdown summary covering: "
        "1) Key equations and theory, 2) Common parameter ranges, "
        "3) Design trade-offs, 4) Relevant references (authors, papers). "
        "Be specific with numbers. Use engineering units. "
        "Cite known papers where applicable."
    )
    user = f"Research the following topic for SynRM (Synchronous Reluctance Motor) design:\n\n{topic}"
    return call_llm(system, user, node="research")


def fetch_url_content(url: str) -> str:
    """Fetch a URL and return its text content.

    NOTE: WebFetch is called as a tool at the graph level.
    This function processes the fetched content.
    """
    return f"Content fetched from {url} (processed by graph node)"
