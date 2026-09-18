from data.loaders import load_documents
from data.extractors import extract_text
from data.chunkers import chunk_text
from data.preprocess import preprocess_text
from embeddings.embedder import generate_embeddings
from embeddings.vector_store import VectorStore
from retrieval.search import perform_similarity_search
from llm.client import generate_answer

class RAGPipeline:
    def __init__(self, vector_store_path):
        self.vector_store = VectorStore(vector_store_path)

    def run(self, document_paths, query):
        documents = load_documents(document_paths)
        extracted_texts = extract_text(documents)
        chunks = chunk_text(extracted_texts)
        preprocessed_chunks = [preprocess_text(chunk) for chunk in chunks]
        embeddings = generate_embeddings(preprocessed_chunks)
        self.vector_store.store_embeddings(embeddings)

        relevant_chunks = perform_similarity_search(query, self.vector_store)
        answer = generate_answer(relevant_chunks, query)

        return answer