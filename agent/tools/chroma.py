"""ChromaDB client — persistent collections for knowledge layer."""

import os
import chromadb
from chromadb.config import Settings
from chromadb.errors import NotFoundError as ChromaNotFoundError
from agent.tools.retry import retry

CHROMA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".chroma")

COLLECTIONS = {
    "sources": "Raw source text chunks from papers and web",
    "entities": "Entity page embeddings",
    "concepts": "Concept page embeddings",
    "synthesis": "Synthesis page embeddings",
    "pymotorcad_vars": "PyMotorCAD variable name lookups",
}

_client = None


def get_client() -> chromadb.PersistentClient:
    """Get or create the persistent ChromaDB client."""
    global _client
    if _client is None:
        os.makedirs(CHROMA_DIR, exist_ok=True)
        _client = chromadb.PersistentClient(
            path=CHROMA_DIR,
            settings=Settings(anonymized_telemetry=False),
        )
    return _client


def get_collection(name: str):
    """Get a collection by name, creating it with metadata if needed."""
    client = get_client()
    try:
        return client.get_collection(name)
    except ChromaNotFoundError:
        return client.create_collection(
            name=name,
            metadata={"description": COLLECTIONS.get(name, "")},
        )


def ensure_collections():
    """Ensure all standard collections exist."""
    for name in COLLECTIONS:
        get_collection(name)


@retry(max_attempts=2, delay=1.0)
def add_document(
    collection_name: str,
    doc_id: str,
    text: str,
    embedding: list[float],
    metadata: dict | None = None,
):
    """Add a single document + embedding to a collection."""
    col = get_collection(collection_name)
    col.add(
        ids=[doc_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[metadata or {}],
    )


def query_similar(
    collection_name: str,
    query_embedding: list[float],
    n_results: int = 5,
    filter_criteria: dict | None = None,
):
    """Query a collection by embedding similarity."""
    col = get_collection(collection_name)
    return col.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        where=filter_criteria,
    )
