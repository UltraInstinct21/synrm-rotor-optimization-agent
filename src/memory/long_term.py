"""File-backed long-term memory — namespace/key/value JSON store.

Follows LangGraph ``BaseStore`` pattern (put / get / search / delete)
but persists to a single JSON file for zero-dependency portability.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Any


class FileMemory:
    """Namespace-key-value store backed by a JSON file.

    Each item has ``value`` (a dict), ``created_at``, and ``updated_at``.

    Thread-safe (single-process).  Not designed for multi-process access.

    Usage::

        mem = FileMemory(Path("workspace/memory/store.json"))
        mem.put(("user", "memories"), "k1", {"text": "likes pizza"})
        item = mem.get(("user", "memories"), "k1")
        items = mem.search(("user",))
    """

    def __init__(self, path: Path) -> None:
        self._path = path
        self._lock = Lock()
        path.parent.mkdir(parents=True, exist_ok=True)
        self._data: dict[str, dict[str, dict[str, Any]]] = self._load()

    # ── public API ─────────────────────────────────────────────────────

    def put(
        self,
        namespace: tuple[str, ...],
        key: str | None = None,
        value: dict[str, Any] | None = None,
    ) -> str:
        """Store or overwrite an item.  Returns the item key."""
        key = key or str(uuid.uuid4())
        ns_str = self._ns(namespace)
        now = _now()
        with self._lock:
            ns = self._data.setdefault(ns_str, {})
            existing = ns.get(key, {})
            ns[key] = {
                "value": value or {},
                "created_at": existing.get("created_at", now),
                "updated_at": now,
            }
            self._save()
        return key

    def get(
        self, namespace: tuple[str, ...], key: str
    ) -> dict[str, Any] | None:
        """Retrieve a single item, or ``None`` if missing."""
        ns_str = self._ns(namespace)
        with self._lock:
            ns = self._data.get(ns_str, {})
            return ns.get(key)

    def search(
        self,
        namespace_prefix: tuple[str, ...],
        *,
        query: str | None = None,
        limit: int = 10,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        """Search items under a namespace prefix.

        Parameters
        ----------
        namespace_prefix :
            Tuple prefix to match namespaces against (e.g. ``("user",)``
            matches ``("user", "memories")``, ``("user", "prefs")``, etc.).
        query :
            Optional text filter — case-insensitive substring match against
            ``str(value)`` of each item.
        limit :
            Max results to return.
        offset :
            Number of results to skip (for pagination).

        Returns
        -------
        list[dict]
            Each entry has keys ``key``, ``value``, ``namespace``,
            ``created_at``, ``updated_at``.
        """
        prefix_str = self._ns(namespace_prefix)
        results: list[dict[str, Any]] = []
        with self._lock:
            for ns_str, items in self._data.items():
                if not ns_str.startswith(prefix_str):
                    continue
                namespace = tuple(ns_str.split("::"))
                for k, item in items.items():
                    if query is not None and query.lower() not in str(
                        item.get("value", {})
                    ).lower():
                        continue
                    results.append(
                        {
                            "key": k,
                            "value": item["value"],
                            "namespace": list(namespace),
                            "created_at": item["created_at"],
                            "updated_at": item["updated_at"],
                        }
                    )
            results.sort(key=lambda r: r["updated_at"], reverse=True)
            return results[offset : offset + limit]

    def delete(self, namespace: tuple[str, ...], key: str) -> bool:
        """Delete an item.  Returns ``True`` if it existed."""
        ns_str = self._ns(namespace)
        with self._lock:
            ns = self._data.get(ns_str, {})
            existed = key in ns
            if existed:
                del ns[key]
                if not ns:
                    del self._data[ns_str]
                self._save()
        return existed

    def list_namespaces(
        self,
        *,
        prefix: tuple[str, ...] | None = None,
        max_depth: int | None = None,
    ) -> list[tuple[str, ...]]:
        """List stored namespaces with an optional prefix filter."""
        prefix_str = self._ns(prefix) if prefix else ""
        namespaces: set[str] = set()
        with self._lock:
            for ns_str in self._data:
                if ns_str.startswith(prefix_str):
                    parts = ns_str.split("::")
                    if max_depth is not None:
                        parts = parts[:max_depth]
                    if prefix:
                        # Keep at least the prefix length
                        min_len = len(prefix)
                        while len(parts) < min_len:
                            parts.append("")
                        parts = parts[:max(len(prefix), len(parts))]
                    namespaces.add("::".join(parts))
        result = []
        for ns in sorted(namespaces):
            t = tuple(ns.split("::"))
            if t and t[-1] == "":
                t = t[:-1]
            result.append(t)
        return result

    def clear(self) -> None:
        """Wipe all stored memories."""
        with self._lock:
            self._data.clear()
            self._save()

    @property
    def path(self) -> Path:
        return self._path

    # ── internal ──────────────────────────────────────────────────────

    @staticmethod
    def _ns(t: tuple[str, ...]) -> str:
        return "::".join(t)

    def _load(self) -> dict[str, dict[str, dict[str, Any]]]:
        if not self._path.exists():
            return {}
        try:
            raw = self._path.read_text(encoding="utf-8")
            return json.loads(raw) if raw.strip() else {}
        except (json.JSONDecodeError, OSError):
            return {}

    def _save(self) -> None:
        self._path.write_text(
            json.dumps(self._data, indent=2, default=str),
            encoding="utf-8",
        )


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()
