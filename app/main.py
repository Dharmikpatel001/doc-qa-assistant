from fastapi import FastAPI
from app.api.upload import router as upload_router  
from app.api.chat import router as chat_router
from app.api.documents import router as document_router

app = FastAPI(
    title="Doc QA assistant",
    version="1.0.0",
    description="Ask questions about uploaded documents using Gemini and RAG."
)

app.include_router(upload_router)

app.include_router(chat_router)

app.include_router(document_router)

@app.get("/")
def home():
    return {
        "message":"Welcome to Doc QA Assistant"
    }
