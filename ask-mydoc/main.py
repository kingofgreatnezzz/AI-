# First fastapi code
from fastapi import FastAPI
import os

app = FastAPI()



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



@app.get("/ask")
def ask(question: str):
    return{"answer": f"dummy:{question}"}
    
    
@app.get("/")
def home():
    return{"Hello" : "world"}


#docs = load_docs()
#print(docs)


# Chuncking will take a size, overlap 
def chunk(text, size=400, overlap=80):
    chunks = []
    # Iterate through the text by size
    for i in range(0 ,len(text), size - overlap):
        print(i)
        piece = text[i:i + size]

        if piece.strip():
            chunks.append(piece)
            print(chunks)
            




# def load_docs(folder="doc"):
#     for file in os.listdir(folder):
#         path = os.path.join(folder, file)
#         #print(path)
#     # if os.path.isfile(path):
#     #     return True
#     # else:
#     #     return False







