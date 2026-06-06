"""Text chunking with configurable overlap for embedding."""

from typing import Iterator


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
    source_id: str = "",
) -> Iterator[dict]:
    """Split text into overlapping chunks.

    Yields dicts with keys: text, chunk_idx, source_id, char_start.
    """
    if not text:
        return

    start = 0
    idx = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        yield {
            "text": chunk,
            "chunk_idx": idx,
            "source_id": source_id,
            "char_start": start,
        }
        idx += 1
        if end >= len(text):
            break
        start = end - overlap


def chunk_texts(
    texts: list[str],
    chunk_size: int = 500,
    overlap: int = 50,
    source_ids: list[str] | None = None,
) -> list[dict]:
    """Chunk multiple texts, optionally with per-text source IDs."""
    results = []
    for i, text in enumerate(texts):
        sid = source_ids[i] if source_ids else f"source_{i}"
        results.extend(chunk_text(text, chunk_size, overlap, sid))
    return results
