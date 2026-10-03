from pydantic import BaseModel
from typing import List, Optional

class Document(BaseModel):
    id: str
    title: str
    content: str
    metadata: Optional[dict] = None

class Chunk(BaseModel):
    id: str
    document_id: str
    text: str
    embeddings: List[float]

class Query(BaseModel):
    question: str
    top_k: int = 5

class Answer(BaseModel):
    answer: str
    source_documents: List[Document]