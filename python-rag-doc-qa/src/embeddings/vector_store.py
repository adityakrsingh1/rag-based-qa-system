from typing import List, Any
import numpy as np
import faiss

class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.embeddings = []
    
    def add_embeddings(self, embeddings: List[np.ndarray]):
        self.embeddings.extend(embeddings)
        self.index.add(np.array(embeddings).astype('float32'))
    
    def search(self, query_embedding: np.ndarray, k: int = 5) -> List[int]:
        distances, indices = self.index.search(query_embedding.reshape(1, -1).astype('float32'), k)
        return indices[0].tolist()
    
    def get_embedding(self, index: int) -> Any:
        return self.embeddings[index] if index < len(self.embeddings) else None
    
    def __len__(self):
        return len(self.embeddings)