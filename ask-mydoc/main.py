# First fastapi code
from fastapi import FastAPI
import os

app = FastAPI()

# get question request
@app.get("/ask")
def ask(question: str):
    return{"answer": f"dummy:{question}"}
    
# home page message 
@app.get("/")
def home():
    return{"Hello" : "world"}


# My documents (load all documents so it's visible)
def load_docs(folder="doc"):
    docs = []
    for name in os.listdir(folder):
        if name.endswith((".txt",".md")):
            # Open the files
            with open(os.path.join(folder,name), encoding="utf-8") as f:
                # return{
                #     "source": {name},
                #     "text": f.read()
                # }
                docs.append({
                    "source":{name},
                    "text" : f.read()
                })
        
    return docs


# Chuncking will take a file, size, overlap 
# Reason for Embeddings and Retrieval 

def chunk(text, size=400, overlap=80):
    chunks = []
    # Iterate through the text by size
    for i in range(0 ,len(text), size - overlap):
        print(i)
        piece = text[i:i + size]

        if piece.strip():
            chunks.append(piece)
            print(chunks)
    return chunks

# Test for Chuncking
docs = load_docs()

# call the chunk function to chunk a file
chucker = chunk(docs[0]["text"], size=100, overlap=20)

# Print the source of the doc selected
source = docs[0]["source"]
print(f"\n----[source]-----{source}\n \n ---[Chuncked]---\n{chucker}")

# get the postion/ number of each chunks
for i, piece in enumerate(chucker):
    # print(f"\n ---chunk {i + 1} ----$")
    print(f"\n --- Chuck 🧩 {i +1 }--- ",piece)

# Documents loading and Chuncking done ✅


# Step 4 Embeddings 🧠
from sentence_transformers import SentenceTransformer








