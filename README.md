Submitted on: 11/09/2026 Last Edited: 03/10/2026 -> Edited:(README.md)
# 📚 RAG-Based Document QA System (Local Edition)

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows you to chat with your PDF documents. This version is designed to run **completely locally** on your machine, ensuring your data stays private and the system remains free to use.

## 🌟 Features
- **Privacy-First**: No data leaves your machine. No API keys required.
- **Local Embeddings**: Uses HuggingFace's `all-MiniLM-L6-v2` for fast, efficient local vectorization.
- **Local LLM**: Powered by **Ollama (Llama 3)** for natural language generation.
- **Anti-Hallucination**: Strictly configured to answer only based on the provided document context.
- **Persistent Storage**: Uses FAISS to save indexed documents locally, so you don't have to re-process PDFs every time.

---

## 🛠️ Installation & Setup

### 1. Install Ollama (Required)
The system uses Ollama to run the LLM locally.
1. Download and install Ollama from [ollama.com](https://ollama.com/).
2. Open your terminal and download the Llama 3 model:
   ```bash
   ollama pull llama3
   ```

### 2. Setup Python Environment
Clone this repository (or enter the folder) and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Prepare Your Documents
Place all the PDF files you want to query into the `data/` directory:
```text
rag-doc-qa/
└── data/
    ├── document1.pdf
    └── document2.pdf
```

---

## 🚀 Usage

### Step 1: Index Your Documents
Before asking questions, you must "index" your PDFs. This parses the text, splits it into chunks, and creates a local vector database.
```bash
python -m src.main --index
```
*This will create a folder called `indices/` where the processed data is stored.*

### Step 2: Query Your Documents
Once indexing is complete, you can start a chat session:
```bash
python -m src.main --query
```
You can now ask questions. The system will retrieve the most relevant parts of your PDFs and use them to generate a factual answer.

---

## 🏗️ Technical Architecture

### The Pipeline
1. **Ingestion**: `PyPDFLoader` $\rightarrow$ `RecursiveCharacterTextSplitter` $\rightarrow$ `HuggingFaceEmbeddings` $\rightarrow$ `FAISS`.
2. **Retrieval**: User Query $\rightarrow$ Embedding $\rightarrow$ FAISS Similarity Search $\rightarrow$ Top-k Context Chunks.
3. **Generation**: User Query + Context $\rightarrow$ `Ollama (Llama 3)` $\rightarrow$ Final Answer.

### Project Structure
- `src/ingestion.py`: Handles PDF parsing and vector store creation.
- `src/rag_engine.py`: Manages the retrieval and the LLM chain.
- `src/main.py`: The CLI entry point for indexing and querying.
- `src/utils.py`: Logging and utility functions.

## 🛡️ Hallucination Guard
To prevent the model from making things up, we use a strict system prompt:
> *"Use the following pieces of retrieved context to answer the question. If the answer is not contained within the context, state that you do not know. Do not make up an answer."*
