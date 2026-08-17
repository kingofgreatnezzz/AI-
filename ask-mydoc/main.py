# First fastapi code
from fastapi import FastAPI
import os

app = FastAPI()

def load_docs(folder="doc"):
    doc = []
    for name in os.listdir(doc):
        if name.endswith((".txt", ".md")):
            with open(os.path.join(doc, name), encoding="utf-8") as f:
                doc.append({
                    "source": name,
                    "text": f.read()
                })
    return doc



@app.get("/ask")
def ask(question: str):
    return{"answer": f"dummy:{question}"}
    
    
@app.get("/")
def home():
    return{"Hello" : "world"}


docs = load_docs()
print(docs)







