from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["rag_db"]
collection = db["documents"]

def store_in_mongo(chunks, embeddings):
    docs = []
    for chunk, emb in zip(chunks, embeddings):
        docs.append({"chunk": chunk, "embedding": emb})
    collection.insert_many(docs)

def get_all_documents():
    return list(collection.find({}, {"_id": 0}))