import pytest
from src.retrieval.search import Search
from src.embeddings.vector_store import VectorStore

@pytest.fixture
def setup_vector_store():
    vector_store = VectorStore()
    yield vector_store
    vector_store.clear()

def test_similarity_search(setup_vector_store):
    setup_vector_store.add_embedding("What is Retrieval-Augmented Generation?", [0.1, 0.2, 0.3])
    setup_vector_store.add_embedding("How does it work?", [0.1, 0.2, 0.4])
    
    search = Search(vector_store=setup_vector_store)
    results = search.similarity_search("Explain Retrieval-Augmented Generation.")
    
    assert len(results) > 0
    assert "What is Retrieval-Augmented Generation?" in results

def test_empty_search(setup_vector_store):
    search = Search(vector_store=setup_vector_store)
    results = search.similarity_search("Non-existent query.")
    
    assert len(results) == 0

def test_reranking_functionality(setup_vector_store):
    setup_vector_store.add_embedding("First document", [0.1, 0.2, 0.3])
    setup_vector_store.add_embedding("Second document", [0.1, 0.2, 0.4])
    
    search = Search(vector_store=setup_vector_store)
    results = search.similarity_search("First document")
    
    reranked_results = search.rerank(results)
    
    assert reranked_results[0] == "First document"  # Assuming reranking keeps the first document as the most relevant