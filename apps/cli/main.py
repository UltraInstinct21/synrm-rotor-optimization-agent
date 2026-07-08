"""motor-deepagent CLI — terminal-first engineering assistant."""

from __future__ import annotations

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env", override=False)


def _build_agent():
    """Build the Deep Agents instance with Motor-CAD tools."""
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

    llm = settings.get_llm()

    return create_deep_agent(
        model=llm,
        tools=[
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
        ],
        system_prompt=(
            "You are a motor engineering assistant built on Deep Agents.\n\n"
            "You have access to Motor-CAD tools for motor design and a research "
            "subagent for literature review.\n\n"
            "PyMotorCAD Anti-Hallucination Rules:\n"
            "1. Always use mc.get_variable_names() before any set/get\n"
            "2. Use safe_get/safe_set wrappers — never raw calls\n"
            "3. show_magnetic_context() before electromagnetic analysis\n"
            "4. Save before changing rotor params (best_so_far.mot)\n"
            "5. Read all results before changing any parameter"
        ),
    )


def _single_shot(query: str) -> None:
    """Process a single query and print the result."""
    agent = _build_agent()
    result = agent.invoke({"messages": [("user", query)]})
    print(result["messages"][-1].content)


def _repl() -> None:
    """Interactive REPL with prompt_toolkit."""
    try:
        from prompt_toolkit import PromptSession
        from prompt_toolkit.history import InMemoryHistory
    except ImportError:
        print("Installing prompt_toolkit...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "prompt_toolkit"])
        from prompt_toolkit import PromptSession
        from prompt_toolkit.history import InMemoryHistory

    agent = _build_agent()
    session = PromptSession(history=InMemoryHistory())

    print("motor-deepagent ready. Type your question or 'exit' to quit.\n")

    while True:
        try:
            query = session.prompt("motor> ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        query = query.strip()
        if not query:
            continue
        if query.lower() in ("exit", "quit", "q"):
            print("Bye!")
            break

        try:
            result = agent.invoke({"messages": [("user", query)]})
            print(result["messages"][-1].content)
        except Exception as e:
            print(f"Error: {e}")


def main() -> None:
    if len(sys.argv) > 1:
        _single_shot(" ".join(sys.argv[1:]))
    else:
        _repl()


if __name__ == "__main__":
    main()
