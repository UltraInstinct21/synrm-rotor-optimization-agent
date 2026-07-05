"""Agent tools for long-term memory access."""

from __future__ import annotations

from agents import function_tool, RunContextWrapper

from src.memory.long_term import FileMemory

# Singleton shared by all memory tool calls.
_memory: FileMemory | None = None


def _get_memory() -> FileMemory:
    global _memory
    if _memory is None:
        from src.config import settings

        _memory = FileMemory(settings.MEMORY_PATH)
    return _memory


@function_tool
async def store_memory(
    ctx: RunContextWrapper,
    namespace: str,
    content: str,
    key: str = "",
) -> str:
    """Store a fact or piece of information in long-term memory.

    Memory persists across sessions.  Use namespaces to organise:
    ``"user/preferences"``, ``"project/facts"``, ``"motor/params"``.

    Args:
        namespace:  Slash-separated path like ``"user/preferences"``.
        content:    The fact or value to remember.
        key:        Optional unique key.  Auto-generated if omitted.

    Returns:
        Confirmation with the stored key.
    """
    ns = tuple(namespace.split("/"))
    mem = _get_memory()
    actual_key = mem.put(ns, key or None, {"text": content})
    return f"Stored under namespace='{namespace}' key='{actual_key}'"


@function_tool
async def search_memory(ctx: RunContextWrapper, query: str, namespace: str = "") -> str:
    """Search long-term memory for relevant facts.

    Args:
        query:     Search text — finds substring matches in stored content.
        namespace: Optional namespace prefix to narrow the search
                   (e.g. ``"user"``, ``"project/facts"``).

    Returns:
        Formatted list of matching memories.
    """
    mem = _get_memory()
    ns = tuple(namespace.split("/")) if namespace else ()
    results = mem.search(ns, query=query, limit=10)
    if not results:
        return f"No memories found for '{query}'."
    lines = []
    for r in results:
        ns_str = "/".join(r["namespace"])
        lines.append(f"  [{ns_str}] {r['key']}: {r['value'].get('text', r['value'])}")
    return f"Found {len(results)} memory(s):\n" + "\n".join(lines)


@function_tool
async def list_memories(ctx: RunContextWrapper, namespace: str = "") -> str:
    """List all memory namespaces, optionally under a prefix.

    Args:
        namespace: Optional prefix (e.g. ``"user"`` lists all user namespaces).

    Returns:
        List of namespaces and their item counts.
    """
    mem = _get_memory()
    ns = tuple(namespace.split("/")) if namespace else ()
    namespaces = mem.list_namespaces(prefix=ns)
    if not namespaces:
        return "No memory namespaces found."
    lines = []
    for n in namespaces:
        items = mem.search(n, limit=100)  # count items in namespace
        count = len(items)
        lines.append(f"  {'/'.join(n)} ({count} item(s))")
    return "Memory namespaces:\n" + "\n".join(lines)


@function_tool
async def forget_memory(ctx: RunContextWrapper, key: str, namespace: str = "") -> str:
    """Remove a specific memory by key.

    Use ``search_memory`` first to find the key you want to delete.

    Args:
        key:       The unique key of the memory to remove.
        namespace: Namespace the memory lives in (e.g. ``"user/preferences"``).

    Returns:
        Confirmation message.
    """
    mem = _get_memory()
    ns = tuple(namespace.split("/")) if namespace else ()
    if mem.delete(ns, key):
        return f"Deleted memory key='{key}' from '{namespace}'."
    return f"Memory key='{key}' not found in '{namespace}'."
