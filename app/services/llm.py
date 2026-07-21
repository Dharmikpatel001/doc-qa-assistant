from google import genai

from app.core.config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY
)

def generate_answer(context: str, question: str):

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the provided context.

Context:

{context}

Question:

{question}
"""
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    return response.text

def generate_general_answer(question):

    prompt = f"""
    Provide a clear, balanced, and general overview of {question}. 
    Include the key concepts, main perspectives, and practical examples in a structured 
    format
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return response.text