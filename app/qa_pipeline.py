from app.embedding import get_embedding
from app.vector_store import VectorStore
from app.mongo_store import get_all_documents
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_vector_store():
    docs = get_all_documents()
    if not docs:
        raise ValueError("No documents found in MongoDB.")

    embeddings = [doc["embedding"] for doc in docs]
    chunks = [doc["chunk"] for doc in docs]

    store = VectorStore(dim=len(embeddings[0]))
    store.add_embeddings(embeddings, chunks)
    return store

def answer_query(question, vector_store):
    query_emb = get_embedding(question)
    top_chunks = vector_store.search(query_emb, top_k=3)
   
    prompt = "Use the following context to answer the question:\n\n"
    prompt += "\n\n".join(top_chunks)
    prompt += f"\n\nQuestion: {question}\nAnswer:"

    model = genai.GenerativeModel('models/gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text