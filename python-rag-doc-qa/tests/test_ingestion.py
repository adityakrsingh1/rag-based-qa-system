import unittest
from src.data.loaders import load_documents
from src.data.extractors import extract_text
from src.data.chunkers import chunk_text
from src.data.preprocess import preprocess_text

class TestIngestion(unittest.TestCase):

    def setUp(self):
        self.raw_documents = load_documents('data/raw')
        self.processed_texts = [extract_text(doc) for doc in self.raw_documents]
        self.chunked_texts = [chunk_text(preprocess_text(text)) for text in self.processed_texts]

    def test_load_documents(self):
        self.assertGreater(len(self.raw_documents), 0, "No documents loaded.")

    def test_extract_text(self):
        for text in self.processed_texts:
            self.assertIsInstance(text, str, "Extracted text is not a string.")

    def test_chunk_text(self):
        for chunks in self.chunked_texts:
            self.assertGreater(len(chunks), 0, "No chunks created from text.")

    def test_preprocess_text(self):
        for text in self.processed_texts:
            preprocessed = preprocess_text(text)
            self.assertIsInstance(preprocessed, str, "Preprocessed text is not a string.")
            self.assertNotIn('\n', preprocessed, "Preprocessed text contains newlines.")

if __name__ == '__main__':
    unittest.main()