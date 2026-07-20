from pathlib import Path
from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.ingestion import extract_text
from app.services.chunking import split_text
from app.services.embeddings import generate_embedding
from app.services.vectorestore import add_document

router = APIRouter()

UPLOAD_DIR = Path("app/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENTIONS = {".pdf", ".txt", ".json", ".docx"}

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    extension =  Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENTIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type."
        )
    
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)

    chunks = split_text(text)

    embeddings = []

    for chunk in chunks:
        vector = generate_embedding(chunk)
        embeddings.append(vector)

    add_document(
        chunks,
        embeddings,
        file.filename
    )

    return{
        "message": "File uploaded successfully",
        "filename": file.filename,
        "file_type": extension,
        "characters": len(text),
        "total_chunks": len(chunks),
        "preview": text[:500]
    }