import unittest
from src.pipeline import RAGPipeline

class TestRAGPipeline(unittest.TestCase):

    def setUp(self):
        self.pipeline = RAGPipeline()

    def test_document_ingestion(self):
        # Test document ingestion functionality
        result = self.pipeline.ingest_documents('data/raw/sample_document.pdf')
        self.assertTrue(result)

    def test_embedding_generation(self):
        # Test embedding generation functionality
        text_chunks = ["This is a test chunk.", "This is another chunk."]
        embeddings = self.pipeline.generate_embeddings(text_chunks)
        self.assertEqual(len(embeddings), len(text_chunks))

    def test_similarity_search(self):
        # Test similarity search functionality
        query = "What is a test chunk?"
        results = self.pipeline.search(query)
        self.assertIsInstance(results, list)

    def test_answer_generation(self):
        # Test answer generation functionality
        context = "This is a test context for the LLM."
        answer = self.pipeline.generate_answer(context)
        self.assertIsInstance(answer, str)

if __name__ == '__main__':
    unittest.main()