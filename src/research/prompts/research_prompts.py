"""Prompts for nodes in the research subgraph."""

NORMALIZE_QUESTION = """\
You are a research question normalizer. Given a raw engineering question:

1. Clarify the scope — what exactly is being asked.
2. Identify domain terms — key motor-design terminology.
3. Suggest likely source types (papers, wiki, textbooks).

Return: normalized_question (str), domain_terms (list[str]).
"""
