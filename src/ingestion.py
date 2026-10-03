import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from .utils import get_logger

logger = get_logger(__name__)

def load_pdfs(data_dir):
    """Loads all PDF files from the specified directory."""
    documents = []
    if not os.path.exists(data_dir):
        logger.error(f"Data directory {data_dir} does not exist.")
        return documents

    for file in os.listdir(data_dir):
        if file.endswith(".pdf"):
            file_path = os.path.join(data_dir, file)
            logger.info(f"Loading PDF: {file}")
            try:
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
            except Exception as e:
                logger.error(f"Error loading {file}: {e}")

    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Splits documents into smaller chunks."""
    logger.info(f"Splitting {len(documents)} documents into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    logger.info(f"Created {len(chunks)} chunks.")
    return chunks

def create_vector_store(chunks, index_path):
    """Creates a FAISS vector store and saves it locally using HuggingFace embeddings."""
    logger.info("Creating vector store and generating embeddings using HuggingFace...")
    # Using a high-quality, lightweight embedding model that runs locally on CPU
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)

    vector_store.save_local(index_path)
    logger.info(f"Vector store saved to {index_path}")
    return vector_store
