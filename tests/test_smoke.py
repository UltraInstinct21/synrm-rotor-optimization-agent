"""Smoke tests — verify all major components import and initialise correctly."""

from __future__ import annotations


def test_artifacts_import():
    from src.artifacts import ResearchReport, CodeReport, ExperimentReport, WikiUpdatePlan

    r = ResearchReport(question="test", summary="test")
    assert r.question == "test"
    assert r.confidence == "medium"


def test_config_import():
    from src.config.settings import PROJECT_ROOT, WIKI_ROOT, BACKEND_ROUTES

    assert PROJECT_ROOT.exists()
    assert "/workspace/" in BACKEND_ROUTES


def test_agent_builder():
    from src.agent.build_agent import build_orchestrator

    cfg = build_orchestrator()
    assert cfg["name"] == "motor-deepagent"
    assert len(cfg["handoffs"]) > 0


def test_subagents():
    from src.agent.subagents import REGISTRY

    assert "RepoCodingAgent" in REGISTRY
    assert "WikiManager" in REGISTRY
    assert "ResearchSubgraph" in REGISTRY
    assert "ExperimentRunner" in REGISTRY


def test_classify():
    from src.agent.orchestration_helpers import classify_request

    assert classify_request("inspect the optimizer code") == "repo_coding"
    assert classify_request("what pages exist in the wiki") == "wiki_maintenance"
    assert classify_request("what is a synrm") == "question"
    assert classify_request("read papers and update wiki") == "mixed"


def test_approvals():
    from src.agent.approvals import requires_approval, PermissionLevel

    assert requires_approval("read_code") == PermissionLevel.AUTO
    assert requires_approval("edit_code") == PermissionLevel.MANUAL


def test_wiki_tool():
    from src.tools.wiki import list_pages, page_summary

    pages = list_pages()
    assert len(pages) >= 8  # seed pages
    summary = page_summary(pages[0])
    assert "path" in summary
    assert "title" in summary


def test_research_state():
    from src.research import make_initial_state

    state = make_initial_state("How does stack length affect torque?")
    assert state["question"] == "How does stack length affect torque?"
    assert state["report_confidence"] == "medium"


def test_research_graph_imports():
    from src.research import run_research, ResearchState, make_initial_state

    assert callable(run_research)
    state = make_initial_state("test question")
    assert state["question"] == "test question"


def test_domain_models():
    from src.domain.motor import MotorDesign, ElectromagneticResult

    design = MotorDesign(name="Test")
    assert design.machine_type == "SynRM"
    assert design.stator.outer_diameter_mm == 250.0

    result = ElectromagneticResult(torque_nm=150.0, efficiency_pct=96.0)
    assert result.torque_nm == 150.0
    assert result.total_loss_w is None  # missing required fields


def test_parameter_mapping():
    from src.domain.motor import MotorDesign, design_to_motorcad_params

    design = MotorDesign()
    params = design_to_motorcad_params(design)
    assert "Stack_Length" in params
    assert "Rotor_OD" in params
    assert "Turns_Per_Coil" in params


def test_execution_imports():
    from src.execution import report_to_summary, summarize_log
    from src.artifacts import ExperimentReport

    report = ExperimentReport(
        experiment_id="test_001",
        workflow_name="test",
        key_metrics={"torque": 143.0, "efficiency": 96.5},
    )
    summary = report_to_summary(report)
    assert "test_001" in summary
    assert "143.0" in summary


def test_motorcad_wrappers():
    from src.tools.motorcad.get_results import _RESULT_VARIABLES
    from src.tools.motorcad.set_parameters import validate_parameter

    assert len(_RESULT_VARIABLES) >= 10
    valid, msg = validate_parameter("Stack_Length", 200.0, domain="stator")
    assert valid


def test_optimization():
    from src.domain.motor.optimization.workflow import SweepConfig, run_sweep

    config = SweepConfig(
        parameter_ranges={"stack_length_mm": (100, 300)},
        num_candidates=5,
    )
    report = run_sweep(config)
    assert report.result == "success"
    assert report.experiment_id.startswith("sweep_")


def test_tui_import():
    """Verify TUI module imports and initializes correctly."""
    from apps.tui import MotorDeepAgentTUI

    app = MotorDeepAgentTUI()
    assert app.model == "deepseek-v4-flash-free"
    assert app.active_tab == "chat"
    assert len(app.BINDINGS) == 9  # 4 generic + 5 tab bindings
