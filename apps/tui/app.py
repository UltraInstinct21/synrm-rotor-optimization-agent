"""TUI for motor-deepagent — multi-tab interface wired to all subsystems.

Usage:
    python -m apps.tui.app
    python -m apps.tui.app --model <model-from-env>
"""

from __future__ import annotations

import asyncio
import sys
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from textual import work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import (
    Header,
    Footer,
    Input,
    RichLog,
    Static,
    TabbedContent,
    TabPane,
    Label,
    ListView,
    ListItem,
    Button,
    DataTable,
)
from textual.screen import Screen
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from rich.columns import Columns
from rich import box

from src.config import settings
from src.agent.runtime import run_request_graph_streamed, InteractiveSession
from src.agent.orchestration_helpers import classify_request
from src.agent.approvals import requires_approval, PermissionLevel
from src.agent.build_agent import build_orchestrator
from src.tools.wiki import list_pages, read_page, page_summary, apply_update_plan
from src.tools.execution import run_python_script
from src.execution.runner import run_experiment
from src.execution.result_summarizer import report_to_summary, summarize_log
from src.domain.motor.optimization.workflow import SweepConfig, run_sweep, compare_designs
from src.domain.motor.result_models import ComparisonResult, ElectromagneticResult
from src.artifacts import (
    CodeReport,
    ExperimentReport,
    ResearchReport,
    WikiUpdatePlan,
)
from src.research.graph import run_research

# ── Styles ──────────────────────────────────────────────────────────
TITLE_STYLE   = "bold #f8fafc on #050505"
HEADER_STYLE  = "bold #67e8f9"
SUCCESS_STYLE = "bold #4ade80"
WARN_STYLE    = "bold #fbbf24"
ERROR_STYLE   = "bold #fb7185"
INFO_STYLE    = "bold #60a5fa"
DIM_STYLE     = "dim #7a7f8f"
SECTION_STYLE = "bold #a78bfa"
CODE_STYLE    = "bold #e5e7eb"

# ── TUI App ─────────────────────────────────────────────────────────


class MotorDeepAgentTUI(App):
    """Multi-tab terminal UI for motor-deepagent.

    Tabs: Chat | Wiki | Research | Run | Motor
    """

    CSS = """
Screen {
    background: #000000;
}

#sidebar {
    width: 22;
    dock: left;
    background: #050505;
    border-right: solid #1f1f1f;
    padding: 0;
}

#sidebar-title {
    padding: 1 1;
    text-align: center;
    background: #0b0b0b;
    color: #fb7185;
    text-style: bold;
}

#sidebar-tabs {
    height: auto;
    margin: 0;
}

#sidebar-buttons {
    width: 100%;
    height: auto;
}

#sidebar-buttons Button {
    width: 100%;
    height: 3;
    background: #050505;
    color: #9ca3af;
    border: none;
    text-align: left;
    padding: 0 1;
}

#sidebar-buttons Button:hover {
    background: #111111;
    color: #f3f4f6;
}

#sidebar-buttons Button.-primary,
#sidebar-buttons Button.variant-primary {
    background: #111111;
    color: #67e8f9;
    text-style: bold;
    border-left: thick #fb7185;
}

#main-content {
    width: 1fr;
    height: 1fr;
}

#status-connection {
    width: 100%;
    height: auto;
    padding: 0 1;
    background: #0b0b0b;
    color: #9ca3af;
    border-bottom: solid #1a1a1a;
}

#output-area {
    width: 100%;
    height: 1fr;
    background: #000000;
    border-bottom: solid #1a1a1a;
}

#output-area:focus-within {
    border-bottom: solid #fb7185;
}

RichLog {
    background: #000000;
    color: #e5e7eb;
    padding: 0 1;
}

#streaming-output {
    background: #000000;
    color: #67e8f9;
    padding: 0 1;
}

.hidden {
    display: none;
}

#input-container {
    width: 100%;
    height: 3;
    background: #050505;
    border-top: solid #1a1a1a;
    padding: 0 1;
}

#prompt-label {
    width: 4;
    height: 3;
    content-align: left middle;
    color: #fb7185;
    text-style: bold;
}

#cmd-input {
    width: 1fr;
    height: 3;
    background: #050505;
    color: #e5e7eb;
    border: none;
}

#cmd-input:focus {
    background: #0b0b0b;
}

#cmd-input .input-cursor {
    color: #67e8f9;
}

#cmd-input .input-placeholder {
    color: #6b7280;
}

#status-bar {
    width: 100%;
    height: 1;
    background: #0b0b0b;
    color: #6b7280;
    padding: 0 1;
    border-top: solid #1a1a1a;
}

#status-text {
    width: 1fr;
    height: 1;
    color: #9ca3af;
}

#stats-text {
    width: auto;
    height: 1;
    color: #6b7280;
}

#model-text {
    width: auto;
    height: 1;
    color: #6b7280;
}

DataTable {
    background: #000000;
    color: #e5e7eb;
    border: none;
}

DataTable > .datatable--header {
    background: #0b0b0b;
    color: #67e8f9;
    text-style: bold;
}

DataTable > .datatable--cursor {
    background: #111111;
    color: #ffffff;
}

ListView {
    background: #000000;
    border: none;
}

ListItem {
    background: #000000;
    color: #e5e7eb;
    padding: 0 1;
}

ListItem:hover {
    background: #111111;
    color: #ffffff;
}

Button {
    background: #111111;
    color: #e5e7eb;
    border: none;
    padding: 0 2;
    margin: 0 1;
}

Button:hover {
    background: #1a1a1a;
    color: #67e8f9;
}

#detail-panel {
    width: 100%;
    height: 1fr;
    background: #000000;
    border-top: solid #1a1a1a;
}

#detail-panel RichLog {
    height: 100%;
}
    """
    # ── Bindings ──────────────────────────────────────────────────
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
        Binding("ctrl+l", "clear_output", "Clear"),
        Binding("ctrl+w", "focus_input", "Input"),
        Binding("f1", "tab_chat", "Chat", priority=True),
        Binding("f2", "tab_wiki", "Wiki", priority=True),
        Binding("f3", "tab_research", "Research", priority=True),
        Binding("f4", "tab_run", "Run", priority=True),
        Binding("f5", "tab_motor", "Motor", priority=True),
        Binding("f6", "refresh_wiki", "Refresh"),
    ]

    # ── Lifecycle ─────────────────────────────────────────────────

    def __init__(self, model: str | None = None) -> None:
        super().__init__()
        self.model = model or settings.MODEL_DEFAULT
        self.session = InteractiveSession(model=self.model)
        self.active_tab = "chat"
        self._busy = False

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            # Sidebar
            with Vertical(id="sidebar"):
                yield Label(" NAVIGATION ", id="sidebar-title")
                with Vertical(id="sidebar-buttons"):
                    yield Button(" F1  Chat     ", id="btn-chat", variant="default")
                    yield Button(" F2  Wiki     ", id="btn-wiki", variant="default")
                    yield Button(" F3  Research ", id="btn-research", variant="default")
                    yield Button(" F4  Run      ", id="btn-run", variant="default")
                    yield Button(" F5  Motor    ", id="btn-motor", variant="default")

            # Main area
            with Vertical(id="main-content"):
                # Connection status
                yield Static(self._connection_info(), id="status-connection")
                # Output area
                yield RichLog(id="output-area", highlight=True, markup=True, max_lines=5000)
                # Streaming response (hidden by default, shown during graph progress)
                yield Static("", id="streaming-output", classes="hidden")
                # Input
                with Horizontal(id="input-container"):
                    yield Static(" >> ", id="prompt-label")
                    yield Input(
                        placeholder="Type a command or request...",
                        id="cmd-input",
                    )
                # Status bar
                with Horizontal(id="status-bar"):
                    yield Static("Ready", id="status-text")
                    yield Static(self.model, id="model-text")
                    yield Static("0 requests", id="stats-text")

    def on_mount(self) -> None:
        """Set up initial state."""
        self.title = "motor-deepagent"
        self.sub_title = f"Model: {self.model}"
        self._highlight_active_tab()
        self._log_init()
        self.query_one("#cmd-input", Input).focus()

    # ── Sidebar ───────────────────────────────────────────────────

    def _highlight_active_tab(self) -> None:
        """Highlight the active tab button."""
        tab_map = {
            "chat": "btn-chat",
            "wiki": "btn-wiki",
            "research": "btn-research",
            "run": "btn-run",
            "motor": "btn-motor",
        }
        for key, btn_id in tab_map.items():
            btn = self.query_one(f"#{btn_id}", Button)
            btn.variant = "primary" if key == self.active_tab else "default"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle sidebar button clicks."""
        tab_map = {
            "btn-chat": "chat",
            "btn-wiki": "wiki",
            "btn-research": "research",
            "btn-run": "run",
            "btn-motor": "motor",
        }
        tab = tab_map.get(event.button.id or "")
        if tab:
            self._set_active_tab(tab)

    def _set_active_tab(self, tab: str) -> None:
        """Switch active tab."""
        self.active_tab = tab
        self._highlight_active_tab()
        self._set_placeholder(tab)
        self.query_one("#cmd-input", Input).focus()

    def _set_placeholder(self, tab: str) -> None:
        """Set the input placeholder based on active tab."""
        placeholders = {
            "chat": "Ask anything: inspect code, update wiki, research, run experiments...",
            "wiki": "Wiki command: list, read <page>, search <term>, update <page>...",
            "research": "Research query: e.g. compare torque density across topologies...",
            "run": "Run: script <path>, sweep <param>=<min>-<max>...",
            "motor": "Motor-CAD: launch, load <model>, run_mag, extract, sweep...",
        }
        self.query_one("#cmd-input", Input).placeholder = placeholders.get(
            tab, "Enter command..."
        )

    # ── Logging ───────────────────────────────────────────────────

    def _log(self, message: str, style: str = "") -> None:
        """Append a line to the output log."""
        log = self.query_one("#output-area", RichLog)
        if style:
            log.write(Text(message, style=style))
        else:
            log.write(message)

    def _log_init(self) -> None:
        """Write startup banner."""
        width = 60
        sep = "=" * width
        self._log(sep, HEADER_STYLE)
        self._log("  motor-deepagent >> terminal engineering assistant", HEADER_STYLE)
        self._log(f"  Model: {self.model}", INFO_STYLE)
        self._log(f"  Modes: Chat | Wiki | Research | Run | Motor", DIM_STYLE)
        self._log(sep, DIM_STYLE)
        self._log("")

    def _log_request(self, request: str) -> None:
        """Log a user request."""
        self._log(f"\n  >> {request}", "bold #e94560")

    def _log_response(self, text: str) -> None:
        """Log a response."""
        for line in text.strip().split("\n"):
            self._log(f"     {line}")

    def _log_result(self, label: str, value: str, style: str = INFO_STYLE) -> None:
        """Log a labelled result line."""
        self._log(f"     {label}: {value}", style)

    def _log_error(self, msg: str) -> None:
        """Log an error."""
        self._log(f"  !! {msg}", ERROR_STYLE)

    def _log_divider(self) -> None:
        self._log(f"  {'-' * 56}", DIM_STYLE)

    def _connection_info(self) -> str:
        """Return connection/API status line."""
        key_ok = bool(settings.LLM_API_KEY or "OPENCODE_API_KEY" in __import__("os").environ)
        status = "connected" if key_ok else "no API key"
        color = "green" if key_ok else "red"
        return (
            f"[{color}]●[/] API: opencode.ai/zen/v1  "
            f"| Model: {self.model}  "
            f"| Mode: auto  "
            f"| Status: {status}"
        )

    # ── Input handling ────────────────────────────────────────────

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Process input based on active tab."""
        if self._busy:
            self._log("  Busy — wait for current operation.", WARN_STYLE)
            event.input.value = ""
            return

        cmd = event.value.strip()
        event.input.value = ""
        if not cmd:
            return

        self._log_request(cmd)

        if cmd in (":q", ":quit", ":exit"):
            self.exit()
            return
        if cmd in (":clear", ":cls"):
            self.query_one("#output-area", RichLog).clear()
            self._log_init()
            return
        if cmd == ":help":
            self._show_help()
            return
        if cmd == ":stats":
            self._show_stats()
            return

        # Dispatch by tab
        handlers = {
            "chat": self._handle_chat,
            "wiki": self._handle_wiki,
            "research": self._handle_research,
            "run": self._handle_run,
            "motor": self._handle_motor,
        }
        handler = handlers.get(self.active_tab, self._handle_chat)
        self._busy = True
        self.query_one("#status-text", Static).update("Working...")
        handler(cmd)

    # ── Tab actions ───────────────────────────────────────────────

    def action_tab_chat(self) -> None:
        self._set_active_tab("chat")

    def action_tab_wiki(self) -> None:
        self._set_active_tab("wiki")

    def action_tab_research(self) -> None:
        self._set_active_tab("research")

    def action_tab_run(self) -> None:
        self._set_active_tab("run")

    def action_tab_motor(self) -> None:
        self._set_active_tab("motor")

    # ── Help / Stats ─────────────────────────────────────────────

    def _show_help(self) -> None:
        self._log("  Commands:", TITLE_STYLE)
        self._log("    :q, :quit, :exit   Quit", DIM_STYLE)
        self._log("    :clear, :cls       Clear output", DIM_STYLE)
        self._log("    :help              Show this help", DIM_STYLE)
        self._log("    :stats             Show session stats", DIM_STYLE)
        self._log("")
        self._log("  Tabs:", TITLE_STYLE)
        self._log("    1 Chat     2 Wiki   3 Research   4 Run   5 Motor", DIM_STYLE)
        self._log("")
        self._log("  Wiki tab commands:", TITLE_STYLE)
        self._log("    list                      List all wiki pages", DIM_STYLE)
        self._log("    read <page>               Read a wiki page", DIM_STYLE)
        self._log("    search <term>            Search wiki content", DIM_STYLE)
        self._log("")
        self._log("  Run tab commands:", TITLE_STYLE)
        self._log("    script <path> [args]      Run a Python script", DIM_STYLE)
        self._log("    sweep <p>=<lo>-<hi>...    Run parameter sweep", DIM_STYLE)
        self._log("")
        self._log("  Motor tab commands:", TITLE_STYLE)
        self._log("    launch [path]             Launch Motor-CAD", DIM_STYLE)
        self._log("    load <path>               Load .mot model", DIM_STYLE)
        self._log("    run_mag                   Run magnetic analysis", DIM_STYLE)
        self._log("    extract                   Extract results", DIM_STYLE)
        self._log("    close                     Close Motor-CAD", DIM_STYLE)
        self._log_divider()

    def _show_stats(self) -> None:
        """Show session statistics."""
        h = self.session.history
        if not h:
            self._log("  No requests processed yet.", DIM_STYLE)
            return
        cats = {}
        for entry in h:
            c = entry.get("category", "unknown")
            cats[c] = cats.get(c, 0) + 1
        self._log("  Session Statistics:", TITLE_STYLE)
        self._log(f"    Total requests: {len(h)}", INFO_STYLE)
        for cat, count in sorted(cats.items()):
            self._log(f"    {cat}: {count}", DIM_STYLE)
        self._log_divider()

    # ── Tab: Chat ─────────────────────────────────────────────────

    @work(thread=False)
    async def _handle_chat(self, cmd: str) -> None:
        """Process via run_request_graph_streamed() — live graph progress."""
        streaming = self.query_one("#streaming-output", Static)
        buffer = ""
        flush_delay = 0.05
        last_flush = time.monotonic()

        def _flush():
            nonlocal buffer, last_flush
            if not buffer:
                return
            streaming.update(Text(f"  {buffer}", INFO_STYLE))
            streaming.remove_class("hidden")
            last_flush = time.monotonic()

        def _finalize(text: str):
            if text:
                self._log_response(text)
            streaming.update("")
            streaming.add_class("hidden")

        try:
            async for event in run_request_graph_streamed(cmd):
                etype = event.get("type")

                if etype == "category":
                    _flush()
                    self._log_result("category", event["data"])

                elif etype == "info":
                    _flush()
                    label = event.get("label", "")
                    data = event.get("data", "")
                    self._log(f"    └─ {label}: {data}", INFO_STYLE)

                elif etype == "synthesis":
                    _finalize(event["data"])

            if buffer:
                _finalize(buffer)

        except Exception as e:
            _finalize(buffer)
            self._log_error(f"Chat error: {e}")
        finally:
            self._busy = False
            self._update_stats()
            self.query_one("#status-text", Static).update("Ready")

    # ── Tab: Wiki ─────────────────────────────────────────────────

    @work(thread=False)
    async def _handle_wiki(self, cmd: str) -> None:
        """Handle wiki commands."""
        try:
            parts = cmd.split(maxsplit=1)
            verb = parts[0].lower() if parts else ""
            arg = parts[1] if len(parts) > 1 else ""

            if verb == "list":
                pages = list_pages()
                if not pages:
                    self._log("  No wiki pages found.", WARN_STYLE)
                else:
                    self._log(f"  Wiki pages ({len(pages)}):", TITLE_STYLE)
                    for p in pages:
                        summary = page_summary(p)
                        self._log(
                            f"    {summary['path']:40s} {summary['size_bytes']:>6} bytes",
                            DIM_STYLE,
                        )

            elif verb == "read":
                if not arg:
                    self._log("  Usage: read <page-path>", WARN_STYLE)
                else:
                    # Try to find the page
                    pages = list_pages()
                    target = next((p for p in pages if arg in str(p)), None)
                    if not target:
                        self._log(f"  Page matching '{arg}' not found.", ERROR_STYLE)
                    else:
                        content = read_page(target)
                        if content:
                            summary = page_summary(target)
                            self._log(
                                f"  {summary['title']} ({summary['path']})",
                                TITLE_STYLE,
                            )
                            self._log(f"  {content[:3000]}", "white")
                            if len(content) > 3000:
                                self._log("  ... (truncated)", DIM_STYLE)
                        else:
                            self._log(f"  Could not read page.", ERROR_STYLE)

            elif verb == "search":
                if not arg:
                    self._log("  Usage: search <term>", WARN_STYLE)
                else:
                    pages = list_pages()
                    found = 0
                    for p in pages:
                        content = read_page(p)
                        if content and arg.lower() in content.lower():
                            summary = page_summary(p)
                            self._log(f"    {summary['path']}", INFO_STYLE)
                            found += 1
                    self._log(f"  Found in {found} page(s).", DIM_STYLE)

            elif verb == "refresh":
                self._log("  Wiki index refreshed.", DIM_STYLE)

            else:
                # Free-form wiki request via the Wiki Manager agent
                self._log_result("WikiManager", f"processing: {cmd}")
                from src.agent.runtime import _run_wiki
                result = await _run_wiki(cmd)
                if result:
                    self._log_response(str(result)[:2000])
                else:
                    self._log("  No response from Wiki Manager.", WARN_STYLE)

        except Exception as e:
            self._log_error(f"Wiki error: {e}")
        finally:
            self._busy = False
            self.query_one("#status-text", Static).update("Ready")

    # ── Tab: Research ─────────────────────────────────────────────

    @work(thread=False)
    async def _handle_research(self, cmd: str) -> None:
        """Run a research query."""
        try:
            self._log("  Running research subgraph...", INFO_STYLE)
            report = await run_research(cmd)

            if isinstance(report, dict):
                self._log_result("question", report.get("question", cmd))
                self._log_result("confidence", report.get("confidence", "medium"))
                summary = report.get("summary", "")
                if summary:
                    self._log_response(summary[:2000])

                claims = report.get("extracted_claims", [])
                if claims:
                    self._log(f"  Claims ({len(claims)}):", TITLE_STYLE)
                    for c in claims[:5]:
                        self._log(f"    - {c[:200]}", DIM_STYLE)

                equations = report.get("equations_or_constraints", [])
                if equations:
                    self._log(f"  Equations ({len(equations)}):", TITLE_STYLE)
                    for e in equations[:3]:
                        self._log(f"    {e[:150]}", CODE_STYLE)

                conflicts = report.get("conflicts_or_uncertainties", [])
                if conflicts:
                    self._log(f"  Conflicts ({len(conflicts)}):", WARN_STYLE)
                    for c in conflicts[:3]:
                        self._log(f"    - {c[:200]}", WARN_STYLE)

                sources = report.get("sources", [])
                if sources:
                    self._log(f"  Sources ({len(sources)}):", TITLE_STYLE)
                    for s in sources[:5]:
                        self._log(
                            f"    {s.get('title', '?')} ({s.get('type', '?')})",
                            DIM_STYLE,
                        )

                updates = report.get("recommended_wiki_updates", [])
                if updates:
                    self._log(f"  Recommended wiki updates:", TITLE_STYLE)
                    for u in updates:
                        self._log(f"    - {u}", DIM_STYLE)

            elif isinstance(report, ResearchReport):
                self._log_result("confidence", report.confidence)
                self._log_response(report.summary[:2000])
            else:
                self._log_response(str(report)[:2000])

        except Exception as e:
            self._log_error(f"Research error: {e}")
        finally:
            self._busy = False
            self.query_one("#status-text", Static).update("Ready")

    # ── Tab: Run ──────────────────────────────────────────────────

    @work(thread=False)
    async def _handle_run(self, cmd: str) -> None:
        """Handle run/tab commands."""
        try:
            parts = cmd.split()
            verb = parts[0].lower() if parts else ""

            if verb == "script" and len(parts) >= 2:
                script_path = Path(parts[1])
                if not script_path.exists():
                    # Try relative to project root
                    script_path = settings.PROJECT_ROOT / parts[1]
                if not script_path.exists():
                    self._log(f"  Script not found: {parts[1]}", ERROR_STYLE)
                else:
                    args = parts[2:] if len(parts) > 2 else None
                    self._log(f"  Running: {script_path} ...", INFO_STYLE)
                    report = await run_experiment(
                        script_path=str(script_path),
                        args=args,
                        log_to_wiki=True,
                    )
                    self._log_result("experiment_id", report.experiment_id)
                    self._log_result("result", report.result,
                                     SUCCESS_STYLE if report.result == "success" else ERROR_STYLE)
                    self._log_result("workflow", report.workflow_name)

                    if report.outputs:
                        logs = report.outputs.get("logs", [])
                        if logs:
                            for log_line in logs[:10]:
                                self._log(f"    {log_line[:200]}", DIM_STYLE)

                    if report.key_metrics:
                        self._log("  Key metrics:", TITLE_STYLE)
                        for k, v in report.key_metrics.items():
                            if v is not None:
                                self._log(f"    {k}: {v}", INFO_STYLE)

                    if report.notes_for_wiki:
                        self._log("  Notes:", DIM_STYLE)
                        for note in report.notes_for_wiki:
                            self._log(f"    {note}", DIM_STYLE)

            elif verb == "sweep":
                # Parse sweep params: sweep stack_length=100-300 turns=4-12
                params = {}
                fixed = {}
                for p in parts[1:]:
                    if "=" in p and "-" in p:
                        key, rest = p.split("=", 1)
                        lo, hi = rest.split("-", 1)
                        params[key] = (float(lo), float(hi))
                    elif "=" in p:
                        key, val = p.split("=", 1)
                        fixed[key] = float(val)

                if not params:
                    self._log("  Usage: sweep <param>=<lo>-<hi> [<param>=<val>...]", WARN_STYLE)
                    self._log("  Example: sweep stack_length=100-300 turns=4-12", DIM_STYLE)
                else:
                    config = SweepConfig(
                        parameter_ranges=params,
                        fixed_params=fixed,
                        num_candidates=10,
                    )
                    self._log(f"  Running sweep: {params}", INFO_STYLE)
                    report = run_sweep(config)
                    self._log_result("sweep_id", report.experiment_id)
                    self._log_result("result", report.result,
                                     SUCCESS_STYLE if report.result == "success" else ERROR_STYLE)
                    if report.key_metrics:
                        self._log("  Best results:", TITLE_STYLE)
                        for k, v in report.key_metrics.items():
                            if v is not None:
                                self._log(f"    {k}: {v}", SUCCESS_STYLE)
                    if report.outputs:
                        files = report.outputs.get("files", [])
                        if files:
                            self._log(f"  Output: {files[0]}", DIM_STYLE)

            elif verb == "list":
                # List available scripts in project
                scripts = list(settings.PROJECT_ROOT.rglob("*.py"))
                self._log(f"  Python scripts ({len(scripts)}):", TITLE_STYLE)
                for s in scripts[:20]:
                    rel = s.relative_to(settings.PROJECT_ROOT)
                    self._log(f"    {rel}", DIM_STYLE)

            else:
                self._log("  Commands: script <path> [args], sweep <p>=<lo>-<hi>..., list", WARN_STYLE)

        except Exception as e:
            self._log_error(f"Run error: {e}")
        finally:
            self._busy = False
            self.query_one("#status-text", Static).update("Ready")

    # ── Tab: Motor ────────────────────────────────────────────────

    _mc_instance: Any = None

    @work(thread=False)
    async def _handle_motor(self, cmd: str) -> None:
        """Handle Motor-CAD and optimization commands."""
        try:
            parts = cmd.split()
            verb = parts[0].lower() if parts else ""

            if verb == "launch":
                model_path = parts[1] if len(parts) > 1 else None
                if model_path and not Path(model_path).exists():
                    # Try reference model
                    model_path = str(settings.REFERENCE_MOT)
                self._log("  Launching Motor-CAD...", INFO_STYLE)
                from src.tools.motorcad.run_motorcad import launch_motorcad as lm
                mc = lm(visible=False, model_path=model_path)
                if mc:
                    type(self)._mc_instance = mc
                    self._log("  Motor-CAD instance ready.", SUCCESS_STYLE)
                    self._log_result("loaded model",
                                     model_path or "default")
                else:
                    self._log("  Motor-CAD launch failed (is ansys.motorcad.core installed?)",
                              ERROR_STYLE)

            elif verb == "load":
                if len(parts) < 2:
                    self._log("  Usage: load <path>", WARN_STYLE)
                else:
                    from src.tools.motorcad.run_motorcad import load_model
                    ok = load_model(self._mc_instance, parts[1])
                    self._log(f"  Load model: {'ok' if ok else 'failed'}",
                              SUCCESS_STYLE if ok else ERROR_STYLE)

            elif verb == "run_mag":
                from src.tools.motorcad.run_motorcad import run_magnetic
                ok = run_magnetic(self._mc_instance)
                if ok:
                    self._log("  Magnetic analysis complete.", SUCCESS_STYLE)
                else:
                    self._log("  Magnetic analysis failed.", ERROR_STYLE)

            elif verb == "extract":
                from src.tools.motorcad.run_motorcad import run_and_extract
                result = run_and_extract(self._mc_instance)
                if result:
                    self._log("  Electromagnetic Results:", TITLE_STYLE)
                    for field, val in result.model_dump().items():
                        if val is not None:
                            display = field.replace("_", " ").title()
                            self._log(f"    {display}: {val}", INFO_STYLE)
                else:
                    self._log("  Extraction failed.", ERROR_STYLE)

            elif verb == "sweep":
                # Parse: sweep stack_length=100-300 turns=4-12
                params = {}
                fixed = {}
                for p in parts[1:]:
                    if "=" in p and "-" in p:
                        key, rest = p.split("=", 1)
                        lo, hi = rest.split("-", 1)
                        params[key] = (float(lo), float(hi))
                    elif "=" in p:
                        key, val = p.split("=", 1)
                        fixed[key] = float(val)
                if not params:
                    self._log("  Usage: sweep <param>=<lo>-<hi> [fixed=val...]", WARN_STYLE)
                else:
                    config = SweepConfig(
                        parameter_ranges=params,
                        fixed_params=fixed,
                        num_candidates=10,
                    )
                    self._log(f"  Running motor sweep: {params}", INFO_STYLE)
                    report = run_sweep(config)
                    self._log_result("sweep_id", report.experiment_id)
                    self._log_result("result", report.result,
                                     SUCCESS_STYLE if report.result == "success" else ERROR_STYLE)
                    if report.key_metrics:
                        for k, v in report.key_metrics.items():
                            if v is not None:
                                self._log(f"    Best {k}: {v}", SUCCESS_STYLE)
                    if report.outputs:
                        files = report.outputs.get("files", [])
                        if files:
                            self._log(f"    CSV: {files[0]}", DIM_STYLE)

            elif verb == "close":
                from src.tools.motorcad.run_motorcad import close_motorcad as cm
                cm(self._mc_instance)
                type(self)._mc_instance = None
                self._log("  Motor-CAD closed.", DIM_STYLE)

            elif verb == "status":
                mc = self._mc_instance
                if mc:
                    self._log("  Motor-CAD: Running", SUCCESS_STYLE)
                else:
                    self._log("  Motor-CAD: Not launched", WARN_STYLE)
                    self._log("  Type 'launch' to start.", DIM_STYLE)

            elif verb == "compare":
                # Compare designs from a sweep CSV
                self._log("  Compare: pass sweep results via sweep command first.", WARN_STYLE)

            else:
                self._log("  Motor commands:", TITLE_STYLE)
                self._log("    launch [model]    Launch Motor-CAD", DIM_STYLE)
                self._log("    load <path>       Load .mot model", DIM_STYLE)
                self._log("    run_mag           Run magnetic analysis", DIM_STYLE)
                self._log("    extract           Extract all results", DIM_STYLE)
                self._log("    sweep <p>=<r>...  Run parameter sweep", DIM_STYLE)
                self._log("    close             Close Motor-CAD", DIM_STYLE)
                self._log("    status            Show Motor-CAD status", DIM_STYLE)

        except Exception as e:
            self._log_error(f"Motor error: {e}")
        finally:
            self._busy = False
            self.query_one("#status-text", Static).update("Ready")

    # ── Utilities ─────────────────────────────────────────────────

    def _update_stats(self) -> None:
        """Update the stats display in the status bar."""
        n = len(self.session.history)
        self.query_one("#stats-text", Static).update(f"{n} requests")
        cats = set()
        for h in self.session.history:
            cats.add(h.get("category", "?"))
        if cats:
            cats_str = ", ".join(sorted(cats))

    def clear_output(self) -> None:
        """Clear the output area."""
        self.query_one("#output-area", RichLog).clear()
        self._log_init()
        self.query_one("#cmd-input", Input).focus()

    def focus_input(self) -> None:
        """Focus the command input."""
        self.query_one("#cmd-input", Input).focus()

    async def action_refresh_wiki(self) -> None:
        """Refresh wiki index (F5)."""
        pages = list_pages()
        self._log(f"  Wiki refreshed: {len(pages)} pages.", INFO_STYLE)

    def on_input_focus(self) -> None:
        """Handle input focus."""
        pass


# ── Entry point ────────────────────────────────────────────────────


def load_env() -> None:
    """Load .env from project root."""
    env_path = Path(__file__).resolve().parent.parent.parent / ".env"
    load_dotenv(env_path, override=False)


def main() -> None:
    """Launch the TUI."""
    load_env()

    import argparse

    parser = argparse.ArgumentParser(description="motor-deepagent TUI")
    parser.add_argument("--model", default=None, help="Model override")
    args = parser.parse_args()

    app = MotorDeepAgentTUI(model=args.model)
    app.run()


if __name__ == "__main__":
    main()
