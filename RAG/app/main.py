# First fastapi code
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, File, UploadFile
import mimetypes

load_dotenv()
app = FastAPI()


@app.post("/ingestion")
def ingestion(file: UploadFile):
    allowed_types = ["application/pdf","text/markdown","text/plain"]

    # Check for file MIME_Type
    file_mime = mimetypes.guess_type(file.filename)[0]
    
    # Check if mime_type is acceptable
    if file_mime in allowed_types:
        return{"Acceptted ✅"}
    else:
        return{"Rejected ❌"}

    # File extention checks
    if file.filename.endswith(".pdf",".md",".txt"):
        return{"File Format accepted"}
    else:
        return{"File fomart not accepted"}

    return{"filename": file.filename, "MIME_Type": file_mime}


# get question request
@app.get("/ask")
def ask(question: str):
    return{"answer": f"dummy:{question}"}
    
    
# home page message 
@app.get("/")
def home():
    return{"Hello" : "world"}










