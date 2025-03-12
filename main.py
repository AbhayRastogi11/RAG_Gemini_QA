from app.pdf_processor import extract_text_from_pdf, chunk_text
from app.embedding import get_embedding
from app.vector_store import VectorStore
from app.mongo_store import store_in_mongo, get_all_documents
from app.qa_pipeline import load_vector_store, answer_query
import json
import os

DATA_PATH = "data/sample_ml_guide.pdf"
OUTPUT_PATH = "outputs/responses.json"

# Safely load JSON file (handles empty or corrupted file)
def safe_load_json(path):
    try:
        with open(path, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def main():
    # Step 1: Extract text from PDF
    print("🔍 Extracting text from PDF...")
    text = extract_text_from_pdf(DATA_PATH)

    # Step 2: Chunk the text
    print("✂️ Chunking into overlapping segments...")
    chunks = chunk_text(text)

    # Step 3: Generate embeddings
    print(f"🧠 Embedding {len(chunks)} chunks using Gemini Embedding API...")
    embeddings = [get_embedding(chunk) for chunk in chunks]

    # Step 4: Store in MongoDB
    print("💾 Storing chunks and embeddings in MongoDB...")
    store_in_mongo(chunks, embeddings)

    # Step 5: Load vector store from DB
    print("📦 Loading vector store...")
    vector_store = load_vector_store()

    print("\n✅ Setup complete! You can now ask questions based on the PDF.")

    # Step 6: User Q&A loop
    while True:
        query = input("\n🔎 Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        answer = answer_query(query, vector_store)
        print(f"\n💬 Answer: {answer}")

        # Step 7: Save response
        responses = safe_load_json(OUTPUT_PATH)
        responses.append({"question": query, "answer": answer})

        with open(OUTPUT_PATH, "w") as f:
            json.dump(responses, f, indent=2)

if __name__ == "__main__":
    main()