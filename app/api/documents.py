from fastapi import APIRouter
from pathlib import Path


router = APIRouter()


UPLOAD_DIR = Path("app/data/uploads").resolve()


@router.get("/documents")
def get_documents():

    files = []

    for file in UPLOAD_DIR.iterdir():

        if file.is_file():

            files.append(file.name)


    return {
        "documents": files
    }