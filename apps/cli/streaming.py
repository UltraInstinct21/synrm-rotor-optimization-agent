"""Token streaming with markdown rendering, expanded tool details, and interrupt session memory (No-Emoji)."""

from __future__ import annotations

import asyncio
from typing import Any, Callable

from rich.console import Console, Group

from apps.cli.display import (
    format_todos_panel,
    render_markdown,
    render_thinking_start,
    render_thinking_stop,
    render_tool_start,
    render_tool_end,
)
from apps.cli.theme import render_assistant_header
from src.config import settings
from src.tools.todo_tools import set_active_session


async def _listen_keys(cli: Any, console: Console) -> None:
    """Listen for Ctrl+O keypresses mid-execution to dynamically toggle expanded view."""
    import sys
    if cli is None or not hasattr(cli, "expanded_view"):
        return

    is_win = sys.platform == "win32"
    try:
        if is_win:
            import msvcrt
            while True:
                await asyncio.sleep(0.1)
                if msvcrt.kbhit():
                    ch = msvcrt.getch()
                    if ch in (b"\x0f", b"o", b"O"):
                        cli.expanded_view = not cli.expanded_view
                        status_str = "ENABLED" if cli.expanded_view else "DISABLED"
                        console.print(f"\n  [cyan][INFO] Tool Call Details View toggled mid-execution: [bold]{status_str}[/bold] (Ctrl+O)[/cyan]\n")
        else:
            import select
            while True:
                await asyncio.sleep(0.1)
                dr, _, _ = select.select([sys.stdin], [], [], 0)
                if dr:
                    ch = sys.stdin.read(1)
                    if ch in ("\x0f", "o", "O"):
                        cli.expanded_view = not cli.expanded_view
                        status_str = "ENABLED" if cli.expanded_view else "DISABLED"
                        console.print(f"\n  [cyan][INFO] Tool Call Details View toggled mid-execution: [bold]{status_str}[/bold] (Ctrl+O)[/cyan]\n")
    except (asyncio.CancelledError, Exception):
        pass


def render_bottom_input_bar(
    session: Any,
    model_name: str = "default",
    expanded: bool = False,
    active_tool: str = "",
    width: int = 80,
) -> Any:
    """Render a persistent bottom chat input & status bar card for Rich Live."""
    from rich.table import Table
    from rich.text import Text
    from apps.cli.display import format_todos_panel

    todos = session.get_todos() if session else []
    todo_str = format_todos_panel(todos, width=width - 4) if todos else ""

    exp_str = "ON" if expanded else "OFF"
    msg_cnt = session.message_count if session else 0
    sess_id = session.id if session else "new"

    tool_status = f" Running [{active_tool}]..." if active_tool else " Generating response..."

    grid = Table.grid(expand=True)
    grid.add_column()
    if todo_str:
        grid.add_row(Text(todo_str, style="bold cyan"))

    status_line = f" Model: {model_name} | Session: {sess_id} ({msg_cnt} msgs) | Logs (Ctrl+O): {exp_str} | {tool_status}"
    if width < 75:
        status_line = f" Session: {sess_id} | Logs: {exp_str} | {tool_status}"

    grid.add_row(Text(status_line, style="bold white on blue"))
    grid.add_row(Text(f" motor [{sess_id}] > [Executing... press Ctrl+C to cancel]", style="bold bright_cyan"))

    return grid


def _build_live_renderable(
    session: Any,
    collected: list[str],
    model_name: str = "default",
    expanded: bool = False,
    active_tool: str = "",
    width: int = 80,
) -> Any:
    """Build a Rich renderable combining streamed text + bottom status bar."""
    bar = render_bottom_input_bar(session, model_name=model_name, expanded=expanded, active_tool=active_tool, width=width)
    text = "".join(collected)
    if text:
        md = render_markdown(text)
        return Group(md, bar)
    return bar


async def _astream(
    console: Console,
    agent: Any,
    query: str,
    session: Any,
    expanded: bool | Callable[[], bool] = False,
    cli: Any = None,
) -> None:
    """Async stream loop — collects tokens, renders tool details with timing metrics, handles interrupts with session memory."""
    from rich.live import Live

    set_active_session(session)
    collected: list[str] = []
    spinner = render_thinking_start(console)
    first_token = True
    tool_start_times: dict[str, float] = {}

    def get_is_expanded() -> bool:
        if callable(expanded):
            return expanded()
        elif cli is not None and hasattr(cli, "expanded_view"):
            return cli.expanded_view
        return bool(expanded)

    model_name = getattr(cli, "model_name", "default") if cli else "default"
    live = Live(
        _build_live_renderable(session, collected, model_name=model_name, expanded=get_is_expanded(), width=console.width),
        console=console,
        refresh_per_second=4,
        auto_refresh=True,
    )
    live.start()

    messages = [(m["role"], m["content"]) for m in session.messages]
    key_listener = asyncio.create_task(_listen_keys(cli, live.console))

    try:
        async for event in agent.astream_events(
            {"messages": messages},
            config={"recursion_limit": settings.RECURSION_LIMIT},
            version="v2",
        ):
            kind = event.get("event", "")

            if kind == "on_chat_model_stream":
                chunk = event["data"]["chunk"]
                if chunk.content:
                    if first_token:
                        render_thinking_stop(spinner)
                        first_token = False
                    collected.append(chunk.content)
                    live.update(_build_live_renderable(session, collected, model_name=model_name, expanded=get_is_expanded(), width=console.width))

            elif kind == "on_tool_start":
                if first_token:
                    render_thinking_stop(spinner)
                    first_token = False
                t_name = event.get("name", "tool")
                t_input = event.get("data", {}).get("input")
                t_id = event.get("run_id", t_name)
                is_exp = get_is_expanded()
                start_t = render_tool_start(live.console, t_name, tool_input=t_input, expanded=is_exp)
                tool_start_times[t_id] = start_t
                live.update(_build_live_renderable(session, collected, model_name=model_name, expanded=get_is_expanded(), active_tool=t_name, width=console.width))

            elif kind == "on_tool_end":
                t_name = event.get("name", "tool")
                t_output = event.get("data", {}).get("output")
                t_id = event.get("run_id", t_name)
                start_t = tool_start_times.pop(t_id, None)
                status = "error" if event.get("data", {}).get("error") else "done"
                is_exp = get_is_expanded()
                render_tool_end(
                    live.console,
                    t_name,
                    tool_output=t_output,
                    status=status,
                    expanded=is_exp,
                    start_time=start_t,
                )
                if t_name in ("write_todos", "update_todo_status") and session.get_todos():
                    todos_card = format_todos_panel(session.get_todos(), width=console.width - 4)
                    if todos_card:
                        live.console.print(f"  [bold cyan][TODO UPDATED mid-session][/bold cyan]\n{todos_card}\n")
                live.update(_build_live_renderable(session, collected, model_name=model_name, expanded=get_is_expanded(), width=console.width))

    except (KeyboardInterrupt, asyncio.CancelledError):
        if first_token:
            render_thinking_stop(spinner)
        console.print("\n  [yellow][INTERRUPTED] Query stopped by user.[/yellow]")
        partial = "".join(collected).strip()
        interrupted_msg = (
            f"{partial}\n\n[Response interrupted by user]"
            if partial
            else "[Response interrupted by user]"
        )
        if partial:
            render_assistant_header(console)
            console.print(render_markdown(partial))
            console.print("  [dim][MEM] Partial response saved to session memory.[/dim]")
        else:
            console.print("  [dim][MEM] Interrupted query saved to session memory.[/dim]")

        session.add("assistant", interrupted_msg)
        return
    except Exception:
        raise
    finally:
        key_listener.cancel()
        try:
            live.stop()
        except Exception:
            pass

    # Stop spinner if still showing (e.g. model returned without chunks)
    if first_token:
        render_thinking_stop(spinner)

    # Render the full response as properly formatted markdown
    full_response = "".join(collected)
    if full_response:
        console.print()
        render_assistant_header(console)
        console.print(render_markdown(full_response))
        session.add("assistant", full_response)


def _loop_exception_handler(loop: asyncio.AbstractEventLoop, context: dict[str, Any]) -> None:
    """Ignore Win32 handle cleanup exceptions from prompt_toolkit during event loop shutdown."""
    exception = context.get("exception")
    if isinstance(exception, RuntimeError) and "Executor shutdown has been called" in str(exception):
        return
    msg = context.get("message", "")
    if "Executor shutdown has been called" in msg or "add_win32_handle" in str(context):
        return
    loop.default_exception_handler(context)


async def _run_astream_with_handler(
    console: Console,
    agent: Any,
    query: str,
    session: Any,
    expanded: bool | Callable[[], bool] = False,
    cli: Any = None,
) -> None:
    """Async wrapper that sets custom loop exception handler before running _astream."""
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(_loop_exception_handler)
    await _astream(console, agent, query, session, expanded=expanded, cli=cli)


def stream_response(
    console: Console,
    agent: Any,
    query: str,
    session: Any,
    expanded: bool | Callable[[], bool] = False,
    cli: Any = None,
) -> None:
    """Sync wrapper — runs the async stream in the event loop with interrupt preservation."""
    set_active_session(session)
    messages = [(m["role"], m["content"]) for m in session.messages]

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    model_name = getattr(cli, "model_name", "default") if cli else "default"
    is_exp = cli.expanded_view if cli and hasattr(cli, "expanded_view") else (expanded() if callable(expanded) else bool(expanded))

    if loop and loop.is_running():
        try:
            from rich.live import Live
            with Live(
                render_bottom_input_bar(session, model_name=model_name, expanded=is_exp, width=console.width),
                console=console,
                refresh_per_second=4,
            ):
                result = agent.invoke(
                    {"messages": messages},
                    config={"recursion_limit": settings.RECURSION_LIMIT},
                )
            content = result["messages"][-1].content
            render_assistant_header(console)
            console.print(render_markdown(content))
            session.add("assistant", content)
        except KeyboardInterrupt:
            console.print("\n  [yellow][INTERRUPTED] Query stopped by user.[/yellow]")
            session.add("assistant", "[Response interrupted by user]")
        return

    try:
        asyncio.run(_run_astream_with_handler(console, agent, query, session, expanded=expanded, cli=cli))
    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    except (NotImplementedError, ValueError, Exception) as e:
        err_str = str(e)
        if "No generations found" in err_str or isinstance(e, (NotImplementedError, ValueError)):
            console.print("  [dim][INFO] Streaming endpoint returned empty chunk; running execution fallback...[/dim]\n")
            try:
                from rich.live import Live
                with Live(
                    render_bottom_input_bar(session, model_name=model_name, expanded=is_exp, width=console.width),
                    console=console,
                    refresh_per_second=4,
                ):
                    result = agent.invoke(
                        {"messages": messages},
                        config={"recursion_limit": settings.RECURSION_LIMIT},
                    )
                content = result["messages"][-1].content
                render_assistant_header(console)
                console.print(render_markdown(content))
                session.add("assistant", content)
            except KeyboardInterrupt:
                console.print("\n  [yellow][INTERRUPTED] Query stopped by user.[/yellow]")
                session.add("assistant", "[Response interrupted by user]")
        else:
            raise

