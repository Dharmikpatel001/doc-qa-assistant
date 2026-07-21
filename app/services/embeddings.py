from google import genai
from app.core.config import GEMINI_API_KEY

client = genai.Client(
    api_key=GEMINI_API_KEY 
)

def generate_embedding(text: str):
    """
    Generate an embedding vector for a single text chunk.
    """
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values

