# First fastapi code
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, File, UploadFile, HTTPException
import mimetypes
import fitz

load_dotenv()
app = FastAPI()


@app.post("/ingestion")
def ingestion(file: UploadFile):
    allowed_types = ["application/pdf","text/markdown","text/plain"]
    MAX_FILE_SIZE = 15 * 1024 * 1024 # 15 MB

    # Check for file MIME_Type
    file_mime = mimetypes.guess_type(file.filename)[0]
    fname = file.filename
    print(f"file name ✅😒",fname)
    
    
    # Check if mime_type is acceptable
    if file_mime not in allowed_types:
        raise HTTPException(status_code=400,detail="Format Rejected ❌")

    # # File extention checks
    if not file.filename.endswith((".pdf",".md",".txt")):
        raise HTTPException(status_code=400,detail="File not Accepted")

    # Actual file claim
    file_context = file.file.read(5)
    if file_context != b"%PDF-":
        raise HTTPException(status_code=400,detail="This is not a PDF as claimed 👺")

    # File size checks
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400,detail="File size is too Big\n Please select a file lesser than 15 MB" )
     
    # Parser for PDF's
    parse_pdf = fitz.open(streaml=)
    return{
        "filename": file.filename,
        "MIME_Type": file_mime,
        "message": "File Accepted"
        }


# get question request
@app.get("/ask")
def ask(question: str):
    return{"answer": f"dummy:{question}"}
    
    
# home page message 
@app.get("/")
def home():
    return{"Hello" : "world"}










