"""motor-deepagent launcher — creates a Deep Agents instance with Motor-CAD tools."""

from src.config import settings
from deepagents import create_deep_agent
from src.tools.motorcad import (
    motorcad_launch,
    motorcad_load_model,
    motorcad_run_magnetic,
    motorcad_run_and_extract,
    motorcad_close,
    motorcad_safe_get,
    motorcad_safe_set,
    motorcad_set_parameter,
    motorcad_save_checkpoint,
    motorcad_get_variables,
    motorcad_extract_results,
)
from src.tools.research import research_subgraph

SYSTEM_PROMPT = """You are a motor engineering assistant built on Deep Agents.

You have access to Motor-CAD tools for motor design and a research subagent for literature review.

PyMotorCAD Anti-Hallucination Rules:
1. Always use mc.get_variable_names() before any set/get
2. Use safe_get/safe_set wrappers — never raw calls
3. show_magnetic_context() before electromagnetic analysis
4. Save before changing rotor params (best_so_far.mot)
5. Read all results before changing any parameter
"""

TOOLS = [
    motorcad_launch,
    motorcad_load_model,
    motorcad_run_magnetic,
    motorcad_run_and_extract,
    motorcad_close,
    motorcad_safe_get,
    motorcad_safe_set,
    motorcad_set_parameter,
    motorcad_save_checkpoint,
    motorcad_get_variables,
    motorcad_extract_results,
    research_subgraph,
]

if __name__ == "__main__":
    import sys

    llm = settings.get_llm()

    agent = create_deep_agent(
        model=llm,
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT,
    )

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        result = agent.invoke({"messages": [("user", query)]})
        print(result["messages"][-1].content)
    else:
        print("motor-deepagent ready. Usage: python run.py 'your question'")
        print("Tools loaded:", len(TOOLS))
