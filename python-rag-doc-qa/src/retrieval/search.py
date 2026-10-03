from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from src.embeddings.vector_store import VectorStore

class SearchEngine:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def search(self, query: str, top_k: int = 5) -> List[str]:
        query_embedding = self.vector_store.embed_query(query)
        all_embeddings = self.vector_store.get_all_embeddings()
        
        similarities = cosine_similarity(query_embedding.reshape(1, -1), all_embeddings)
        top_indices = np.argsort(similarities[0])[-top_k:][::-1]
        
        return self.vector_store.get_documents_by_indices(top_indices)