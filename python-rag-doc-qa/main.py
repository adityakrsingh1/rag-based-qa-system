import os
from src.config import Config
from src.pipeline import RAGPipeline

def main():
    # Load configuration
    config = Config()

    # Initialize the RAG pipeline
    rag_pipeline = RAGPipeline(config)

    # Run the pipeline
    rag_pipeline.run()

if __name__ == "__main__":
    main()