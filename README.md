# Medical Chatbot with RAG and LLM

This project is a sophisticated, AI-powered medical chatbot that answers user questions based on a specialized knowledge source—the **"Gale Encyclopedia of Medicine."**  
It uses a **Retrieval-Augmented Generation (RAG)** architecture to provide accurate, context-aware responses, preventing the language model from hallucinating and ensuring the answers are grounded in the provided medical text.

The application is built with a **FastAPI** backend and a user-friendly **HTML/CSS/JavaScript** frontend.

---

## Core Technologies

- **Backend Framework:** FastAPI  
- **LLM Framework:** LangChain  
- **Language Model (LLM):** Google Gemini Pro  
- **Vector Database:** Pinecone (Free Tier)  
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2` (Hugging Face)  
- **Deployment:** Uvicorn ASGI Server  

---

## Setup and Installation Guide

Follow these steps to set up and run the project locally on your machine.


### **Step 1: Prerequisites**

- Python 3.9 or higher  
- A free Pinecone API key  
- A Google Gemini API key  



### **Step 2: Clone the Repository**

Open your terminal and clone the project repository:

```bash
git clone https://github.com/viplavs2004/Med-bot
cd med-bot
```



### **Step 3: Set Up a Virtual Environment**

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create the virtual environment
python -m venv med-bot-env

# Activate the environment
# On Windows:
.\med-bot-env\Scripts\activate

# On macOS/Linux:
source med-bot-env/bin/activate
```



### **Step 4: Install Dependencies**

Install all the required Python packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```



### **Step 5: Configure Environment Variables**

You need to provide your secret API keys.

Create a new file named `.env` in the root directory of the project.

Copy and paste the following content into the `.env` file, replacing the placeholder values with your actual keys.

```bash
# .env file

# Pinecone API Key
PINECONE_API_KEY="YOUR_PINECONE_API_KEY"

# Google Gemini API Key
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```

### **Step 6: Prepare and Load Your Data into Pinecone**

Before you can run the chatbot, you must process the source PDF and load it into your Pinecone index.

- **Check the Source PDF:**  
  The *"Gale Encyclopedia of Medicine"* is already included in the `Data/` directory.  
  If you wish to use a different edition or another medical PDF, simply replace the file in this directory.

- **Run the Indexing Script:**  
  Execute the `store_index.py` script from your terminal.  
  This will automatically create the Pinecone index, process your PDF, and upload the data.

```bash
python store_index.py
```

> **Note:** This process may take a few minutes depending on the size of your document. Wait for it to complete before proceeding.


## Running the Application

Once the setup is complete, you can start the web server by running the `app.py` file directly.  
This works because the file includes a script to start the Uvicorn server programmatically.

```bash
python app.py
```

After starting the server, open your web browser and go to:
```bash
http://127.0.0.1:8080
```
You should see the **medical chatbot interface**, ready to answer your questions!

---

## 🖼️ Application Screenshot  

![Medical Chatbot Screenshot](https://github.com/viplavs2004/Med-bot/blob/main/med-bot-frontend.PNG)
