import argparse
import os
from .utils import check_api_key, get_logger
from .ingestion import load_pdfs, split_documents, create_vector_store
from .rag_engine import load_rag_chain

logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="RAG-Based Document QA System")
    parser.add_argument(
        "--index",
        action="store_true",
        help="Index documents in the data folder"
    )
    parser.add_argument(
        "--query",
        action="store_true",
        help="Query the indexed documents"
    )

    args = parser.parse_args()

    try:
        check_api_key()
    except ValueError as e:
        logger.error(e)
        return

    data_dir = "rag-doc-qa/data"
    index_path = "rag-doc-qa/indices/faiss_index"

    if args.index:
        logger.info("Starting indexing pipeline...")
        docs = load_pdfs(data_dir)
        if not docs:
            logger.error("No PDFs found in the data directory.")
            return

        chunks = split_documents(docs)
        create_vector_store(chunks, index_path)
        logger.info("Indexing complete!")

    elif args.query:
        if not os.path.exists(index_path):
            logger.error("Index not found. Please run with --index first.")
            return

        logger.info("Starting query pipeline...")
        qa_chain = load_rag_chain(index_path)

        print("\n--- RAG Document QA System ---")
        print("Type 'exit' or 'quit' to stop.\n")

        while True:
            query = input("Question: ")
            if query.lower() in ["exit", "quit"]:
                break

            if not query.strip():
                continue

            try:
                response = qa_chain.invoke({"query": query})
                print(f"\nAnswer: {response['result']}\n")
            except Exception as e:
                logger.error(f"Error during query: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
