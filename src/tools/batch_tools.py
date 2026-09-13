"""Batch helpers — parallel-safe read-only fan-outs for validation and wiki search.

These tools perform no solves and no writes, so they are safe to batch
in a single turn instead of issuing N sequential tool calls.
"""

from __future__ import annotations

import json

from langchain_core.tools import tool


@tool
def batch_validate_params(candidates_json: str, spec_path: str = "") -> str:
    """Validate a batch of candidate geometry dicts against the active spec.

    PARALLEL-SAFE: batch this in one turn instead of N sequential calls.

    Read-only: calls validate_parameters/load_active_spec only, no solves,
    no writes. Capped at 20 candidates per call.

    Args:
        candidates_json: JSON list of {param_name: value} dicts, e.g.
            '[{"L1_Diameter": 100}, {"L1_Diameter": 999}]'.
        spec_path: Optional explicit spec file. Empty = active spec.

    Returns:
        JSON {status ok|error, results[{index, ok, errors}], spec}.
    """
    from src.motor.spec import load_active_spec
    from src.motor.validate import validate_parameters

    try:
        candidates = json.loads(candidates_json) if isinstance(candidates_json, str) else candidates_json
    except (json.JSONDecodeError, TypeError) as e:
        return json.dumps({"status": "error", "error": f"candidates_json is not valid JSON: {e}"}, indent=2)
    if not isinstance(candidates, list):
        return json.dumps({"status": "error", "error": "candidates_json must be a JSON list of param dicts"}, indent=2)
    if len(candidates) > 20:
        return json.dumps(
            {"status": "error", "error": f"Batch capped at 20 candidates, got {len(candidates)}. Split into smaller batches."},
            indent=2,
        )
    try:
        spec = load_active_spec(spec_path)
    except Exception as e:
        return json.dumps({"status": "error", "error": f"Cannot load machine spec: {e}"}, indent=2)
    results: list[dict] = []
    for i, params in enumerate(candidates):
        if not isinstance(params, dict):
            results.append({"index": i, "ok": False, "errors": [f"Candidate {i} is not a JSON object"]})
            continue
        try:
            verdict = validate_parameters(params, spec)
            results.append({
                "index": i,
                "ok": bool(verdict.get("ok", False)),
                "errors": verdict.get("errors", []),
            })
        except Exception as e:
            results.append({"index": i, "ok": False, "errors": [f"Validation failed: {e}"]})
    return json.dumps({"status": "ok", "results": results, "spec": spec.project}, indent=2)


@tool
def wiki_search_many(queries_json: str, scope: str = "indexed", limit_per_query: int = 10) -> str:
    """Search the wiki for several queries in one call.

    PARALLEL-SAFE: batch this in one turn instead of N sequential calls.

    Read-only: search action only, no writes. Max 5 queries per call.

    Args:
        queries_json: JSON list of query strings, e.g. '["Airgap", "PhaseAdvance"]'.
        scope: Search scope passed through to wiki_tool ('indexed' or 'all').
        limit_per_query: Max matches per query (clamped to 1..100).

    Returns:
        JSON {status ok|error, per_query[{query, status, matches|error}]}.
    """
    from src.tools.wiki.wiki_tool import wiki_tool

    try:
        queries = json.loads(queries_json) if isinstance(queries_json, str) else queries_json
    except (json.JSONDecodeError, TypeError) as e:
        return json.dumps({"status": "error", "error": f"queries_json is not valid JSON: {e}"}, indent=2)
    if not isinstance(queries, list):
        return json.dumps({"status": "error", "error": "queries_json must be a JSON list of query strings"}, indent=2)
    if len(queries) > 5:
        return json.dumps(
            {"status": "error", "error": f"Batch capped at 5 queries, got {len(queries)}. Split into smaller batches."},
            indent=2,
        )
    try:
        limit_i = max(1, min(int(limit_per_query), 100))
    except (TypeError, ValueError):
        limit_i = 10
    per_query: list[dict] = []
    for q in queries:
        if not isinstance(q, str) or not q.strip():
            per_query.append({"query": q, "status": "error", "error": "Query must be a non-empty string"})
            continue
        try:
            raw = wiki_tool.invoke({"action": "search", "query": q.strip(), "scope": scope, "limit": limit_i})
            payload = json.loads(raw) if isinstance(raw, str) else raw
            if isinstance(payload, dict) and payload.get("status") == "success":
                entry: dict = {"query": q.strip(), "status": "success", "matches": payload.get("matches", [])}
                for key in ("exact_parameter_match", "files_scanned", "files_matched", "truncated", "hint"):
                    if key in payload:
                        entry[key] = payload[key]
                per_query.append(entry)
            else:
                err = payload.get("error", "Unknown search error") if isinstance(payload, dict) else str(payload)
                per_query.append({"query": q.strip(), "status": "error", "error": err})
        except Exception as e:
            per_query.append({"query": q.strip(), "status": "error", "error": f"Search failed: {e}"})
    return json.dumps({"status": "ok", "per_query": per_query}, indent=2)


__all__ = ["batch_validate_params", "wiki_search_many"]
