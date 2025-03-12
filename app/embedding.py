import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
embedding_model = genai.embed_content

def get_embedding(text, model="models/embedding-001"):
    response = embedding_model(
        model=model,
        content=text,
        task_type="retrieval_document"
    )
    return response["embedding"]