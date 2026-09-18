from typing import List
import pdfplumber
import docx
import os

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_txt(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def extract_text_from_markdown(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def extract_text(file_path: str) -> str:
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext == '.txt':
        return extract_text_from_txt(file_path)
    elif ext == '.md':
        return extract_text_from_markdown(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def extract_texts_from_files(file_paths: List[str]) -> List[str]:
    extracted_texts = []
    for file_path in file_paths:
        try:
            text = extract_text(file_path)
            extracted_texts.append(text)
        except Exception as e:
            print(f"Error extracting text from {file_path}: {e}")
    return extracted_texts