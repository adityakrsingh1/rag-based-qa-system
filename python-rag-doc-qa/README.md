# Retrieval-Augmented Generation (RAG) Document Q&A System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) based document question and answer system. It processes various document formats, extracts text, chunks it, generates embeddings, stores them in a vector database, performs similarity searches, and generates answers using a language model.

## Architecture
The system is structured into several components:
- **Document Processing**: Ingests and processes documents from various formats.
- **Embedding Generation**: Converts text chunks into embeddings for efficient retrieval.
- **Vector Database**: Stores embeddings and allows for similarity searches.
- **Retrieval and Reranking**: Retrieves relevant chunks based on user queries and reranks them for relevance.
- **Answer Generation**: Uses a language model to generate answers based on retrieved context.

## Technologies Used
- Python
- Libraries for document processing (e.g., PyPDF2, python-docx)
- Embedding models (e.g., Sentence Transformers)
- Vector databases (e.g., FAISS, Weaviate)
- Language models (e.g., OpenAI's GPT)

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-rag-doc-qa
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Copy `.env.example` to `.env` and fill in the required values.

## Usage
1. Place your documents in the `data/raw` directory.
2. Run the application:
   ```
   python main.py
   ```

3. Follow the prompts to ask questions based on the processed documents.

## Testing
To run the tests, use:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.