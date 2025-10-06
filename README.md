# Med-bot
A RAG-based medical chatbot built with Google's Gemini API, Pinecone vector DB, and Langchain. It uses The Gale Encyclopedia of Medicine as its knowledge source to provide reliable health information.


This tool is useful for:
- Creating study guides  
- Summarizing complex documents  
- Generating FAQs from technical manuals  

The app provides a clean web interface to upload PDFs, view generated Q&A pairs, and export them as CSV for offline use.  

---

## Key Features
- PDF Upload – Drag-and-drop or file-picker interface for uploading PDF documents.  
- Automated Q&A Generation – Creates relevant questions and accurate answers from document content.  
- Web-Based Visualization – Displays Q&A pairs in a clean, easy-to-read card layout.  
- CSV Export – Download the full Q&A list as a CSV file.  
- RAG Pipeline – Uses a Retrieval-Augmented Generation (RAG) approach with FAISS vector store for context-aware answers.  

---

## Technology Stack
- Backend: Fast api 
- AI Framework: LangChain  
- LLM & Embeddings: Google Gemini API (`gemini-pro`, `text-embedding-004`)  
- Vector Store: FAISS  
- Frontend: HTML, Tailwind CSS, JavaScript  

---

## Setup and Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/viplavs2004/QA-Generator.git
cd QA-Generator


Step 2: Create a Virtual Environment
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt, generate one using:

pip freeze > requirements.txt

Step 4: Configure Environment Variables

Create a .env file in the root directory and add your Google API Key:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"


You can obtain an API key from Google AI Studio
.

Running the Application

Start the FastAPI server:

uvicorn app:app --reload


Open your browser and visit:
http://127.0.0.1:8000

Usage Guide

Open the Web App → Go to http://127.0.0.1:8000

Upload a PDF → Drag & drop or select a PDF file from your computer

Generate Q&A → Click “Generate Q&A” to process the document

View Results → Generated Q&A pairs will appear on the screen

Download CSV → Export results by clicking “Download CSV”