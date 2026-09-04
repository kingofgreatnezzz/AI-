# First fastapi code
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, File, UploadFile, HTTPException
import mimetypes
import pymupdf

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

    # # File Extention checks
    if not file.filename.endswith((".pdf",".md",".txt")):
        raise HTTPException(status_code=400,detail="File not Accepted")

    # File size checks
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400,detail="File size is too Big\n Please select a file lesser than 15 MB" )
     
    if file_context == "application/pdf":
        # Actual file claim
        file.file.seek(0)
        file_context = file.file.read(5)

        if file_context != b"%PDF-":
        raise HTTPException(status_code=400,detail="This is not a PDF as claimed 👺")

        file.file.seek(0)
        actual_file = file.file.read()
        parse_pdf = pymupdf.open(stream=actual_file, filetype="pdf")
        text = " "
        for texts in parse_pdf:
            text += texts.get_text()

    # Read TXT MD File
    elif file_mime in ["text/markdown","text/plain"]:
        file.file.seek(0)
        text = file.file.read().decode("utf-8")
     
    return{
        "filename": file.filename,
        "MIME_Type": file_mime,
        "message": "File Accepted ✅😒",
       # "text": text
        }


# get question request
@app.get("/ask")
def ask(question: str):
    return{"answer": f"dummy:{question}"}
    
    
# home page message 
@app.get("/")
def home():
    return{"Hello" : "world"}
















