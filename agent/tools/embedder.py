"""sentence-transformers wrapper — singleton embedder for all vector ops."""

from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
_embedder = None


def get_embedder() -> SentenceTransformer:
    """Get or create the shared embedding model instance."""
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer(MODEL_NAME)
    return _embedder


def embed_text(text: str) -> list[float]:
    """Embed a single text string. Returns normalized float vector."""
    return get_embedder().encode([text])[0].tolist()


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed multiple texts in batch. More efficient than embed_text per item."""
    return [vec.tolist() for vec in get_embedder().encode(texts)]
