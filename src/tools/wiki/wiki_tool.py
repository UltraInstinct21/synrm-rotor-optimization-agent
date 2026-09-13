"""Wiki Agent Tool — enables Deep Agents to search, read, list, and update durable wiki knowledge in workspace/wiki.

Routing: use `search` for a single local fact (esp. Motor-CAD variable names
— mandatory before any set/get of an unverified name). Use `read` on
`motorcad/parameter_database/parameters/<Name>.md` for the exact spec sheet
once search names the parameter. For multi-doc synthesis use
`research_subgraph`; for web info use `tavily_search`.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path

from langchain_core.tools import tool
from src.config.settings import WIKI_ROOT

WIKI_DIR = WIKI_ROOT

# The parameter_database/parameters/ tree holds ~13k per-parameter detail
# sheets (64 MB). Category sheets in parameter_database/categories/ already
# name every parameter, so default search skips the detail sheets.
_SEARCH_SKIP_DIRS = {"parameters"}
_LIST_CAP_DEFAULT = 200
_MAX_SEARCH_FILE_BYTES = 2 * 1024 * 1024
_MAX_READ_CHARS = 12000
_PARAM_NAME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_\[\]]*$")


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


def _iter_wiki_files(scope: str = "indexed"):
    """Yield wiki .md files. scope='indexed' skips parameter detail sheets."""
    for root, dirs, files in os.walk(WIKI_DIR):
        if scope != "all":
            dirs[:] = [d for d in dirs if d not in _SEARCH_SKIP_DIRS]
        for name in files:
            if name.lower().endswith(".md"):
                yield Path(root) / name


def _exact_parameter_sheet(query: str) -> Path | None:
    """Fast path: if query looks like an exact Motor-CAD name, resolve its spec sheet directly."""
    name = query.strip().strip("\"'`")
    if not name or not _PARAM_NAME_RE.match(name) or len(name) > 80:
        return None
    candidate = WIKI_DIR / "motorcad" / "parameter_database" / "parameters" / f"{name}.md"
    try:
        if candidate.is_file():
            return candidate
    except OSError:
        pass
    return None


def _score_file(text_lower: str, title_lower: str, query_lower: str, terms: list[str]) -> tuple[int, int]:
    """Rank: exact-query hits in title > exact-query hits in body > term hits."""
    title_hits = text_lower.count(query_lower) if query_lower else 0
    in_title = 1 if query_lower and query_lower in title_lower else 0
    term_hits = sum(text_lower.count(t) for t in terms if t)
    return (in_title, title_hits * 3 + term_hits)


@tool
def wiki_tool(
    action: str,
    query: str = "",
    page_path: str = "",
    content: str = "",
    scope: str = "indexed",
    offset: int = 0,
    limit: int = 200,
    max_chars: int = 12000,
) -> str:
    """Wiki Agent Tool to interact with durable project documentation in workspace/wiki.

    Args:
        action: The operation to perform. Supported: 'search', 'read', 'list', 'write'.
        query: Search term for 'search' action. If it exactly matches a
            Motor-CAD parameter name, its spec sheet is returned directly
            without a full scan.
        page_path: Relative path to wiki page (e.g., 'project_overview.md' or
            'motorcad/parameter_database/parameters/<Name>.md') for 'read' or 'write'.
        content: Markdown content to write when using 'write' action.
        scope: Search scope for 'search'. 'indexed' (default) searches category sheets
            and all normal wiki pages but skips the ~13k per-parameter detail sheets in
            motorcad/parameter_database/parameters/ — category sheets already name every
            parameter, then use read on parameters/<Name>.md for its spec sheet.
            'all' includes every file (slow full scan).
        offset: Pagination offset for 'list' (page start) or 'read' (char start).
        limit: Max entries for 'list' (default 200) / max matches for 'search' (default 50).
        max_chars: Max chars returned by 'read' (default 12000; longer pages truncated).

    Returns:
        JSON response with the outcome of the requested wiki action.
    """
    WIKI_DIR.mkdir(parents=True, exist_ok=True)
    if not action or not action.strip():
        return json.dumps({"status": "error", "error": "Action parameter required."})

    action_clean = action.strip().lower()

    if action_clean == "list":
        try:
            try:
                offset_i = max(0, int(offset))
            except (TypeError, ValueError):
                offset_i = 0
            try:
                limit_i = max(1, min(int(limit), 1000))
            except (TypeError, ValueError):
                limit_i = _LIST_CAP_DEFAULT
            files = sorted(
                str(p.relative_to(WIKI_DIR)).replace("\\", "/")
                for p in _iter_wiki_files("all")
            )
            page = files[offset_i:offset_i + limit_i]
            payload = {
                "status": "success",
                "action": "list",
                "wiki_pages": page,
                "total_count": len(files),
                "offset": offset_i,
            }
            if offset_i + limit_i < len(files):
                payload["truncated"] = True
                payload["next_offset"] = offset_i + limit_i
            return json.dumps(payload, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": f"Failed to list wiki pages: {e}"})

    elif action_clean == "search":
        if not query or not query.strip():
            return json.dumps({"status": "error", "error": "query parameter required for search action"})
        # Fast path: exact Motor-CAD parameter name -> spec sheet, no scan.
        exact = _exact_parameter_sheet(query)
        if exact is not None:
            try:
                text = exact.read_text(encoding="utf-8", errors="replace")
                rel = str(exact.relative_to(WIKI_DIR)).replace("\\", "/")
                return json.dumps({
                    "status": "success",
                    "action": "search",
                    "query": query.strip(),
                    "scope": scope,
                    "exact_parameter_match": rel,
                    "matches": [{"page": rel, "line_number": 1, "content": text[:500]}],
                    "hint": f"Full spec via wiki_tool(action='read', page_path='{rel}')",
                }, indent=2)
            except Exception:
                pass
        try:
            limit_i = max(1, min(int(limit), 100))
        except (TypeError, ValueError):
            limit_i = 50
        matches: list[dict] = []
        files_scanned = 0
        query_clean = query.strip()
        query_lower = query_clean.lower()
        # Extra terms improve ranking for multi-word queries.
        terms = [t.lower() for t in re.split(r"\s+", query_lower) if len(t) > 2]
        scored_files: list[tuple[tuple[int, int], Path, str]] = []
        for p in _iter_wiki_files(scope):
            try:
                if p.stat().st_size > _MAX_SEARCH_FILE_BYTES:
                    continue
                files_scanned += 1
                text = p.read_text(encoding="utf-8", errors="replace")
                text_lower = text.lower()
                if query_lower not in text_lower and not any(t in text_lower for t in terms):
                    continue
                title_lower = p.stem.replace("_", " ").lower()
                scored_files.append((_score_file(text_lower, title_lower, query_lower, terms), p, text))
            except Exception:
                continue
        # Rank: title matches first, then hit density. Cap file reads for context.
        scored_files.sort(key=lambda item: (item[0][0], item[0][1]), reverse=True)
        truncated = False
        for _, p, text in scored_files:
            rel_path = str(p.relative_to(WIKI_DIR)).replace("\\", "/")
            lines = text.splitlines()
            for line_no, line in enumerate(lines, 1):
                if query_lower in line.lower() or any(t in line.lower() for t in terms):
                    if len(matches) >= limit_i:
                        truncated = True
                        break
                    matches.append({
                        "page": rel_path,
                        "line_number": line_no,
                        "content": line.strip()[:300],
                    })
            if len(matches) >= limit_i:
                truncated = True
                break
        # Auto-fallback: indexed scope found nothing and query looks like a
        # parameter — retry the full scan once before giving up.
        if not matches and scope != "all" and _PARAM_NAME_RE.match(query_clean):
            return wiki_tool.invoke({
                "action": "search", "query": query_clean, "scope": "all",
                "limit": limit_i,
            })
        return json.dumps({
            "status": "success",
            "action": "search",
            "query": query_clean,
            "scope": scope,
            "files_scanned": files_scanned,
            "files_matched": len(scored_files),
            "matches": matches,
            "truncated": truncated,
        }, indent=2)

    elif action_clean == "read":
        if not page_path:
            return json.dumps({"status": "error", "error": "page_path parameter required for read action"})
        target = _safe_wiki_path(page_path)
        if target is None or not target.exists() or not target.is_file():
            return json.dumps({"status": "error", "error": f"Wiki page not found or path invalid: {page_path}"})
        try:
            try:
                offset_i = max(0, int(offset))
            except (TypeError, ValueError):
                offset_i = 0
            try:
                max_chars_i = max(500, min(int(max_chars), 100000))
            except (TypeError, ValueError):
                max_chars_i = _MAX_READ_CHARS
            text = target.read_text(encoding="utf-8", errors="replace")
            total = len(text)
            chunk = text[offset_i:offset_i + max_chars_i]
            payload = {"status": "success", "action": "read", "page_path": page_path,
                       "content": chunk, "total_chars": total, "offset": offset_i}
            if offset_i + max_chars_i < total:
                payload["truncated"] = True
                payload["next_offset"] = offset_i + max_chars_i
            return json.dumps(payload, indent=2)
        except Exception as e:
            return json.dumps({"status": "error", "error": f"Failed to read wiki page: {e}"})

    elif action_clean in ("write", "update"):
        if not page_path or not content:
            return json.dumps({"status": "error", "error": "page_path and content parameters required for write action"})
        if len(content) > 200_000:
            return json.dumps({"status": "error", "error": "content exceeds 200,000 chars. Split into smaller pages."})
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
