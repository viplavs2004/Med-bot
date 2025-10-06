# 1. Imports
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # <-- ADD THIS IMPORT
from dotenv import load_dotenv
import os

from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *

# 2. FastAPI App Initialization
app = FastAPI()

# --- ADD THIS LINE TO SERVE STATIC FILES (CSS, JS, Images) ---
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup for HTML templates (This should point to your "templates" folder)
templates = Jinja2Templates(directory="templates")


# 3. Environment Variable Loading
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


# 4. LangChain and Pinecone Setup
embeddings = download_hugging_face_embeddings()
index_name = "med-bot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.4, max_output_tokens=500)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


# 5. API Routes

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


@app.post("/get")
async def chat(msg: str = Form(...)):
    input_text = msg
    print(f"Received message: {input_text}")
    response = rag_chain.invoke({"input": input_text})
    answer = response.get("answer", "Sorry, I couldn't find an answer.")
    print(f"Response: {answer}")
    return {"answer": answer}


# 6. Running the App
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

