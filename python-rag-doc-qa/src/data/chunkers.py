from typing import List

def chunk_text(text: str, chunk_size: int, overlap: int) -> List[str]:
    """
    Splits the input text into smaller chunks with specified size and overlap.

    Args:
        text (str): The text to be chunked.
        chunk_size (int): The size of each chunk.
        overlap (int): The number of overlapping tokens between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def chunk_document(document: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """
    Processes a document and returns its chunks.

    Args:
        document (str): The document text to be chunked.
        chunk_size (int): The size of each chunk.
        overlap (int): The number of overlapping tokens between chunks.

    Returns:
        List[str]: A list of text chunks from the document.
    """
    return chunk_text(document, chunk_size, overlap)