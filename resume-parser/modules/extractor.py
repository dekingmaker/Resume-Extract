import os 

import  fitz 
from docx import Dcoument


def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:

        text += page.get_text()

    return text



def extract_text_from_doc(file_path):
    doc = Dcoument(file_path)
    text = ""
    for page in doc:
        text += page.join([p.text for p in doc.paragraphs])
        return text



def extract_text(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")