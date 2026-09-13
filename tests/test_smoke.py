"""Smoke tests — verify all major components import and initialise correctly."""

from __future__ import annotations

import json


def test_artifacts_import():
    from src.artifacts import ResearchReport

    r = ResearchReport(question="test", summary="test")
    assert r.question == "test"
    assert r.confidence == "medium"


def test_config_import():
    from src.config.settings import PROJECT_ROOT, MODEL_DEFAULT, LLM_BASE_URL

    assert PROJECT_ROOT.exists()
    assert isinstance(MODEL_DEFAULT, str)


def test_agent_factory():
    """build_tools returns the streamlined custom tool list for DeepAgent.

    Todo tracking is deepagents' built-in write_todos (injected by middleware),
    so no custom todo tool may appear here. The shell `execute` tool is also
    excluded via the openai harness profile.
    """
    from src.agent.factory import build_tools

    tools = build_tools()
    names = {t.name for t in tools}
    assert "execute_generated_motorcad_code" in names
    assert "create_run_file" in names
    assert "execute_run_file" in names
    assert "validate_motor_params" in names
    assert "score_motor_result" in names
    assert "research_subgraph" in names
    assert "tavily_search" in names
    assert "wiki_tool" in names
    assert "delete_file" in names
    assert len(names) == 9
    assert "write_todos" not in names
    assert "update_todo_status" not in names


def test_wiki_tool():
    """Verify wiki_tool list and search capabilities."""
    from src.tools.wiki import wiki_tool

    res = wiki_tool.invoke({"action": "list"})
    data = json.loads(res)
    assert data["status"] == "success"
    assert "wiki_pages" in data

    res_search = wiki_tool.invoke({"action": "search", "query": "SynRM"})
    data_search = json.loads(res_search)
    assert data_search["status"] == "success"


def test_create_and_execute_run_file():
    """Verify create_run_file and execute_run_file work together."""
    from src.tools.execution import create_run_file, execute_run_file

    code = 'print("Hello from created run file!")\n'
    create_res = create_run_file.invoke({"filename": "test_run_script.py", "code_content": code})
    c_data = json.loads(create_res)
    assert c_data["status"] == "success"

    exec_res = execute_run_file.invoke({"filename": "test_run_script.py"})
    e_data = json.loads(exec_res)
    assert e_data["status"] == "success"
    assert "Hello from created run file!" in e_data["stdout"]


def test_research_state():
    from src.research.state import make_initial_state

    state = make_initial_state("How does stack length affect torque?")
    assert state["question"] == "How does stack length affect torque?"
    assert state["report_confidence"] == "medium"


def test_research_graph_imports():
    from src.research.graph import run_research
    from src.research.state import ResearchState, make_initial_state

    assert callable(run_research)
    state = make_initial_state("test question")
    assert state["question"] == "test question"


def test_research_schemas():
    from src.research.schemas import NormalizedQuestion

    n = NormalizedQuestion(normalized_question="test", domain_terms=["motor"])
    assert n.normalized_question == "test"
    assert "motor" in n.domain_terms



def test_sessions():
    from apps.cli.session import Session

    s = Session()
    assert s.id is not None
    s.add("user", "hello")
    assert len(s.messages) == 1


def test_interrupted_session_memory():
    from apps.cli.session import Session

    s = Session()
    s.add("user", "Start long sweep calculation")
    s.add("assistant", "Partial calculation results...\n\n[Response interrupted by user]")
    
    assert len(s.messages) == 2
    assert "interrupted" in s.messages[1]["content"]
    
    # Verify messages can be formatted cleanly for follow-up turns
    formatted = [(m["role"], m["content"]) for m in s.messages]
    assert len(formatted) == 2
    assert formatted[0] == ("user", "Start long sweep calculation")


def test_tavily_search_hitl():
    from src.tools.search import tavily_search, set_hitl_enabled, get_hitl_enabled

    set_hitl_enabled(False)
    assert not get_hitl_enabled()

    # Invoke without API key set -> should return clean json status error or missing key notice
    res = tavily_search.invoke({"query": "python latest release"})
    data = json.loads(res)
    assert "status" in data
    assert data["query"] == "python latest release"

    set_hitl_enabled(True)
    assert get_hitl_enabled()