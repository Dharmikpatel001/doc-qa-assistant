from pathlib import Path
from pypdf import PdfReader
import json
from docx import Document

    
def extract_pdf(file_path: Path) -> str:
    
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def extract_txt(file_path: Path) -> str:
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
    
def extract_json(file_path: Path) -> str:

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return json.dumps(data, indent=4)


def extract_docx(file_path: Path) -> str:

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text

def extract_text(file_path: Path) -> str:

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_pdf(file_path)

    elif extension == ".txt":
        return extract_txt(file_path)

    elif extension == ".json":
        return extract_json(file_path)

    elif extension == ".docx":
        return extract_docx(file_path)

    raise ValueError(f"Unsupported file type: {extension}")

