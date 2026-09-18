from pathlib import Path
import os

def load_documents_from_directory(directory: str):
    documents = []
    for file_path in Path(directory).rglob('*'):
        if file_path.suffix in ['.pdf', '.txt', '.docx', '.md']:
            with open(file_path, 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents

def load_single_document(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_documents(file_paths: list):
    documents = []
    for file_path in file_paths:
        documents.append(load_single_document(file_path))
    return documents