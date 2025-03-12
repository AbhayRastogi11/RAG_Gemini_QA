# 📄 RAG-Based Q&A System using Gemini API

A Retrieval-Augmented Generation (RAG) application built with Python that:
- Extracts text from PDF documents
- Chunks and embeds the content using Google's Gemini API
- Stores embeddings in MongoDB and FAISS
- Retrieves relevant context based on user queries
- Generates context-aware answers using Gemini's LLM

---

## 🔧 Features
- ✍️ PDF upload & text extraction using PyMuPDF
- 📓 Chunking with token overlap (~500 tokens)
- 🧠 Embedding using Gemini's Embedding API
- 🔍 Vector similarity search using FAISS
- 💾 MongoDB for persistent chunk storage
- 🔤 Contextual answer generation via Gemini LLM

---

## 🗂️ Project Structure
bash
rag-gemini-qa/
├── app/
│   ├── __init__.py
│   ├── pdf_processor.py         # PDF text extraction & chunking
│   ├── embedding.py             # Gemini embedding functions
│   ├── vector_store.py          # FAISS vector store setup & search
│   ├── mongo_store.py           # MongoDB integration
│   ├── qa_pipeline.py           # Retrieval + Gemini answer generation
├── data/
│   └── sample.pdf               # Example PDF input
├── outputs/
│   └── responses.json           # Stores generated Q&A pairs
├── main.py                      # Entry point for CLI
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (Git-ignored)
├── .gitignore                   # Ignored files & folders
└── README.md


---

## 🚪 Setup Instructions

### 1. Clone the Repository
bash
git clone https://github.com/yourusername/rag-gemini-qa.git
cd rag-gemini-qa


### 2. Create and Activate a Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows


### 3. Install Dependencies
bash
pip install -r requirements.txt


### 4. Configure Environment Variables
Create a .env file in the root folder with the following:
env
GEMINI_API_KEY=your_gemini_api_key_here
MONGO_URI=your_mongodb_connection_string_here


### 5. Add a Sample PDF
Place a test document in the data/ folder and name it sample.pdf.

### 6. Run the App
bash
python main.py

You will be prompted to ask questions based on the PDF content!

---

## 🎨 Example Questions to Ask
- What is machine learning?
- Explain supervised vs unsupervised learning
- What is the F1 score and when is it used?
- How is ML applied in healthcare?
- What causes overfitting in models?

---

## 🚀 Sample Output
bash
🔎 Ask a question (or type 'exit'): What is the F1 score?
💬 Answer: The F1 Score is the weighted average of Precision and Recall. It helps evaluate the balance between the two metrics...


---

## 📝 Dependencies
- PyMuPDF (fitz)
- google-generativeai
- pymongo
- python-dotenv
- faiss-cpu

Optional: To use ChromaDB instead of FAISS, install chromadb.

---

## 🚧 Future Improvements
- Streamlit Web UI
- PDF file upload interface
- ChromaDB backend support
- Deploy to Hugging Face Spaces or Replit

---