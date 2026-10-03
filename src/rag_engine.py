import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from .utils import get_logger

logger = get_logger(__name__)

def load_rag_chain(index_path):
    """Loads the persisted FAISS index and constructs a RetrievalQA chain using Ollama."""
    logger.info(f"Loading FAISS index from {index_path}...")

    # Must use the same embedding model used during ingestion
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    try:
        vector_store = FAISS.load_local(
            index_path,
            embeddings,
            allow_dangerous_deserialization=True
        )
    except Exception as e:
        logger.error(f"Error loading vector store: {e}")
        raise e

    # Use Ollama for local LLM generation
    # Ensure Ollama is running and you have pulled the model (e.g., ollama pull llama3)
    llm = Ollama(model="llama3")

    # Custom Prompt to minimize hallucinations
    template = (
        "You are a helpful assistant. Use the following pieces of retrieved context to answer the question. "
        "If the answer is not contained within the context, state that you do not know. "
        "Do not make up an answer.\n\n"
        "Context: {context}\n\n"
        "Question: {question}\n\n"
        "Helpful Answer:"
    )
    QA_CHAIN_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template=template,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )

    logger.info("Local RAG chain constructed successfully.")
    return qa_chain
