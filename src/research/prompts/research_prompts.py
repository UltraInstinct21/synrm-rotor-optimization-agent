"""Prompts for nodes in the research subgraph."""

NORMALIZE_QUESTION = """\
You are a research question normalizer for electric motor engineering
(SynRM, induction, PMSM, Motor-CAD simulation).

Given a raw engineering question:
1. Clarify the scope — what exactly is being asked (one sentence).
2. Identify domain terms — 3-8 key motor-design terms (e.g. "flux barrier",
   "saliency ratio", "power factor"). Prefer exact
   Motor-CAD parameter names when the question mentions geometry.
3. Suggest likely source types is NOT needed — output JSON only.

Output STRICTLY valid JSON, no markdown fences, matching:
{"normalized_question": "<clarified question>", "domain_terms": ["term1", "term2"]}

Example:
Q: "how do L1/L2 barriers affect torque?"
-> {"normalized_question": "How do L1 and L2 rotor flux-barrier geometries affect SynRM shaft torque?", "domain_terms": ["flux barrier", "L1_Diameter", "L2_Diameter", "shaft torque", "saliency ratio"]}
"""

SYNTHESIZE_REPORT_SYSTEM = (
    "You are an expert motor engineering research synthesizer. "
    "Output strictly valid JSON matching the requested structure — no markdown fences, no commentary."
)

SYNTHESIZE_REPORT_TEMPLATE = """You are a motor engineering research assistant. Analyze the provided source snippets and synthesize a comprehensive technical answer.

Question: {question}

Source Context:
{context_str}

Respond with a JSON object containing:
- "summary": Clear, direct answer to the user's question based on context. Cite source titles in parentheses where used.
- "extracted_claims": List of key technical claims/facts extracted (each one sentence).
- "equations_or_constraints": List of design equations or geometric constraints mentioned (e.g. L1_Diameter < L2_Diameter).
- "conflicts_or_uncertainties": Any conflicting statements or missing details.
- "recommended_wiki_updates": Suggested updates to wiki pages if needed.
- "recommended_code_targets": Suggested PyMotorCAD parameters or python run files to modify.
- "confidence": "high", "medium", or "low".
"""

