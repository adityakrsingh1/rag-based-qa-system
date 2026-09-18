from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, texts):
        return self.model.encode(texts, convert_to_tensor=True)

    def save_embeddings(self, embeddings, file_path):
        # Implement saving logic here (e.g., to a file or database)
        pass

    def load_embeddings(self, file_path):
        # Implement loading logic here (e.g., from a file or database)
        pass