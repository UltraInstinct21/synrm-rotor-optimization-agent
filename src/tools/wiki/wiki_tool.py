"""Wiki Agent Tool — enables Deep Agents to search, read, list, and update durable wiki knowledge in workspace/wiki."""

from __future__ import annotations

import json
from pathlib import Path

from langchain_core.tools import tool
from src.config.settings import WIKI_ROOT

WIKI_DIR = WIKI_ROOT


def _safe_wiki_path(page_path: str) -> Path | None:
    """Validate page_path to prevent path traversal outside WIKI_DIR."""
    try:
        clean = Path(page_path.strip())
        target = (WIKI_DIR / clean).resolve()
        wiki_res = WIKI_DIR.resolve()
        if wiki_res in target.parents or target == wiki_res:
            return target
    except Exception:
        pass
    return None


@tool
def wiki_tool(
    action: str,
    query: str = "",
    page_path: str = "",
    content: str = "",
) -> str:
    """Wiki Agent Tool to interact with durable project documentation in workspace/wiki.

    Args:
        action: The operation to perform. Supported: 'search', 'read', 'list', 'write'.
        query: Search term for 'search' action.
        page_path: Relative path to wiki page (e.g., 'project_overview.md' or 'architecture/orchestrator.md') for 'read' or 'write'.
        content: Markdown content to write when using 'write' action.

    Returns:
        JSON response with the outcome of the requested wiki action.
    """
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    if not action or not action.strip():
        return json.dumps({"status": "error", "error": "Action parameter required."})

    action_clean = action.strip().lower()

    if action_clean == "list":
        files = []
        try:
            for p in WIKI_DIR.glob("**/*"):
                if p.is_file() and p.suffix.lower() == ".md":
                    files.append(str(p.relative_to(WIKI_DIR)).replace("\\", "/"))
            return json.dumps({"status": "success", "action": "list", "wiki_pages": sorted(files)}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": f"Failed to list wiki pages: {e}"})

    elif action_clean == "search":
        if not query:
            return json.dumps({"status": "error", "error": "query parameter required for search action"})
        matches = []
        query_lower = query.lower()
        for p in WIKI_DIR.glob("**/*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
                rel_path = str(p.relative_to(WIKI_DIR)).replace("\\", "/")
                lines = text.splitlines()
                for line_no, line in enumerate(lines, 1):
                    if query_lower in line.lower():
                        matches.append({
                            "page": rel_path,
                            "line_number": line_no,
                            "content": line.strip()[:200]
                        })
            except Exception:
                continue
        return json.dumps({"status": "success", "action": "search", "query": query, "matches": matches[:50]}, indent=2)

    elif action_clean == "read":
        if not page_path:
            return json.dumps({"status": "error", "error": "page_path parameter required for read action"})
        target = _safe_wiki_path(page_path)
        if target is None or not target.exists() or not target.is_file():
            return json.dumps({"status": "error", "error": f"Wiki page not found or path invalid: {page_path}"})
        try:
            text = target.read_text(encoding="utf-8", errors="replace")
            return json.dumps({"status": "success", "action": "read", "page_path": page_path, "content": text}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": f"Failed to read wiki page: {e}"})

    elif action_clean in ("write", "update"):
        if not page_path or not content:
            return json.dumps({"status": "error", "error": "page_path and content parameters required for write action"})
        target = _safe_wiki_path(page_path)
        if target is None:
            return json.dumps({"status": "error", "error": f"Invalid or prohibited wiki path: {page_path}"})
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            rel_path = str(target.relative_to(WIKI_DIR)).replace("\\", "/")
            return json.dumps({"status": "success", "action": "write", "page_path": rel_path, "bytes_written": len(content)}, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": f"Failed to write wiki page: {e}"})

    else:
        return json.dumps({
            "status": "error",
            "error": f"Unknown action '{action}'. Supported actions: 'search', 'read', 'list', 'write'."
        })


__all__ = ["wiki_tool"]
