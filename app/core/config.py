import os
from dotenv import load_dotenv

load_dotenv()

print("GOOGLE KEY FOUND:", bool(os.getenv("GOOGLE_API_KEY")))

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
  
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is missing")