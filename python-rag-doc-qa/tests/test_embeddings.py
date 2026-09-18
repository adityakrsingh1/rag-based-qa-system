import unittest
from src.embeddings.embedder import Embedder

class TestEmbedder(unittest.TestCase):

    def setUp(self):
        self.embedder = Embedder()

    def test_embedding_generation(self):
        text = "This is a test sentence."
        embedding = self.embedder.generate_embedding(text)
        self.assertIsNotNone(embedding)
        self.assertEqual(len(embedding), self.embedder.embedding_dimension)

    def test_embedding_shape(self):
        text = "Another test sentence."
        embedding = self.embedder.generate_embedding(text)
        self.assertEqual(len(embedding), self.embedder.embedding_dimension)

if __name__ == '__main__':
    unittest.main()