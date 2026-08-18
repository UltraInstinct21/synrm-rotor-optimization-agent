"""MotorCLI — chat-style interactive session orchestrator (Glitch-Free Dynamic Redraw)."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from apps.cli.commands import COMMANDS, dispatch
from apps.cli.display import render_error, render_user_message
from apps.cli.session import Session, SessionStore
from apps.cli.streaming import stream_response
from apps.cli.theme import get_console, render_banner

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

SESSION_DIR = Path.home() / ".motor-deepagent" / "sessions"


class MotorCLI:
    """Chat-style CLI orchestrator."""

    def __init__(self) -> None:
        self.console = get_console()
        self.session_store = SessionStore(SESSION_DIR)
        self.current_session: Session = self.session_store.new()
        self.model_name: str = "default"
        self._agent = None
        self.tools: list = []
        self.expanded_view: bool = False
        self._prompt_session = None

    def _ensure_agent(self):  # noqa: ANN202
        """Lazy-build the agent on first use for instantaneous CLI startup with error recovery."""
        if self._agent is None:
            try:
                from apps.cli.main import _build_agent

                self._agent, self.tools = _build_agent()
            except Exception as e:
                render_error(self.console, e)
                raise RuntimeError(f"Failed to initialize Agent runtime: {e}") from e
        return self._agent

    def _get_prompt_session(self):
        """Lazy-create PromptSession with auto-completer and clean dynamic status toolbar."""
        if self._prompt_session is None:
            from prompt_toolkit import PromptSession
            from prompt_toolkit.completion import Completer, Completion
            from prompt_toolkit.history import FileHistory
            from prompt_toolkit.key_binding import KeyBindings
            from prompt_toolkit.styles import Style

            class SlashCompleter(Completer):
                def __init__(self, commands: dict[str, dict]) -> None:
                    self.commands = commands

                def get_completions(self, document, complete_event):
                    text = document.text_before_cursor
                    if not text.startswith("/"):
                        return
                    word = text.lstrip("/")
                    for name in sorted(self.commands):
                        if name.startswith(word):
                            yield Completion(
                                f"/{name}",
                                start_position=-len(text),
                                display_meta=self.commands[name]["help"],
                            )

            kb = KeyBindings()

            @kb.add("c-o")
            def _toggle_expanded_kb(event):
                """Toggle detailed tool call view seamlessly without stdout line collisions."""
                self.expanded_view = not self.expanded_view
                event.app.invalidate()

            def _get_toolbar():
                from apps.cli.display import format_todos_panel
                exp = "ON" if self.expanded_view else "OFF"
                msg_cnt = self.current_session.message_count
                term_w = self.console.width

                todos = self.current_session.get_todos()
                todo_str = format_todos_panel(todos, width=term_w - 4) if todos else ""

                if term_w < 75:
                    status_text = f" Model: {self.model_name} | Session: {self.current_session.id} | Logs: {exp} "
                else:
                    status_text = f" Model: {self.model_name} | Session: {self.current_session.id} ({msg_cnt} msgs) | Logs (Ctrl+O): {exp} | Type /help "

                if todo_str:
                    return [
                        ("class:todo_panel", f"{todo_str}\n"),
                        ("class:toolbar", status_text),
                    ]
                return [("class:toolbar", status_text)]

            prompt_style = Style.from_dict({
                "prompt": "ansibrightcyan bold",
                "toolbar": "bg:#1E293B #94A3B8 bold",
                "todo_panel": "#38BDF8 bold",
            })

            self._prompt_session = PromptSession(
                history=FileHistory(str(SESSION_DIR / ".input_history")),
                completer=SlashCompleter(COMMANDS),
                key_bindings=kb,
                bottom_toolbar=_get_toolbar,
                style=prompt_style,
                refresh_interval=0.5,
            )
        return self._prompt_session

    def _read_multiline(self) -> str | None:
        """Read input with multi-line support cleanly."""
        prompt_sess = self._get_prompt_session()
        try:
            first = prompt_sess.prompt([("class:prompt", f"motor [{self.current_session.id}] > ")])
        except KeyboardInterrupt:
            self.console.print("  [dim]Input cancelled. Ready for next query.[/dim]")
            return ""
        except EOFError:
            return None

        first = first.rstrip("\n")

        # Multi-line: line ends with backslash
        if first.endswith("\\"):
            lines = [first[:-1]]  # strip backslash
            while True:
                try:
                    line = prompt_sess.prompt([("class:prompt", "... ")])
                except KeyboardInterrupt:
                    self.console.print("  [dim]Multi-line input cancelled.[/dim]")
                    return ""
                except EOFError:
                    return None
                line = line.rstrip("\n")
                if not line:
                    break
                lines.append(line)
            return "\n".join(lines)

        return first

    def single_shot(self, query: str) -> None:
        """Process a single query and print the result."""
        try:
            agent = self._ensure_agent()
            self.current_session.add("user", query)
            stream_response(self.console, agent, query, self.current_session, expanded=self.expanded_view, cli=self)
        except KeyboardInterrupt:
            self.console.print("\n  [dim][INTERRUPTED] Session memory preserved.[/dim]\n")
        except Exception as e:
            render_error(self.console, e)
            self.current_session.add("assistant", f"[Execution error encountered: {e}]")

    def run(self) -> None:
        """Interactive REPL loop."""
        from src.tools.search import get_hitl_enabled

        # Render clean welcome banner immediately
        render_banner(
            self.console,
            session_id=self.current_session.id,
            model_name=self.model_name,
            hitl_enabled=get_hitl_enabled(),
            tool_count=6,
            expanded_view=self.expanded_view,
        )

        while True:
            query = self._read_multiline()
            if query is None:
                self.console.print("\n  [bold bright_cyan]Goodbye![/bold bright_cyan]\n")
                break

            query = query.strip()
            if not query:
                continue

            # Slash commands
            if query.startswith("/"):
                if dispatch(self, query) is False:
                    break
                continue

            # Ensure agent build before executing query
            try:
                agent = self._ensure_agent()
            except Exception:
                self.console.print("  [dim]Agent initialization failed. Please fix configuration and retry.[/dim]\n")
                continue

            # Regular query stream
            try:
                render_user_message(self.console, query)
                self.current_session.add("user", query)
                stream_response(self.console, agent, query, self.current_session, expanded=self.expanded_view, cli=self)
                self.console.print()
            except KeyboardInterrupt:
                self.console.print("\n  [dim][INTERRUPTED] Session memory preserved. Ready for follow-up query.[/dim]\n")
            except Exception as e:
                render_error(self.console, e)
                self.current_session.add("assistant", f"[Execution error encountered: {e}]")

    def rebuild_agent(self, model: BaseChatModel | None = None) -> None:  # noqa: ARG002
        """Force agent rebuild. Call after model switch."""
        self._agent = None
        self._ensure_agent()
