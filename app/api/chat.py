from fastapi import APIRouter
from app.models.request import ChatRequest

from app.services.embeddings import generate_embedding
from app.services.vectorestore import search_documents
from app.services.llm import generate_answer, generate_general_answer

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    question = request.question 

    query_embedding = generate_embedding(question)

    results = search_documents(query_embedding)

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    sources = results["metadatas"][0]

    distances = results["distances"][0]

    best_distance = distances[0]

    SIMILARITY_THRESHOLD = 0.5

    if best_distance > SIMILARITY_THRESHOLD:

        answer = generate_general_answer(question)

        return {
            "question": question,
            "answer": answer,
            "sources": []
        }

    else:
        
        answer = generate_answer(
            context,
            question
        )

        return {
            "question": question,   
            "answer": answer,
            "sources": sources
        }