# First fastapi code
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, File, UploadFile


load_dotenv()
app = FastAPI()

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

# Choose a model
model = SentenceTransformer("all-MiniLM-L6-v2")
print("-------------Model Loaded🔫--------------")

# Turn Chunks to embeddings
vectors = model.encode(chucker)
#print(f"\n----{vectors[0]}----〽️")

# Testing question
question = "what is python"
question_vector = model.encode(question)
#print(f"Ques Vec 🚀🚀🚀🚀---- {question_vector}")



# Step 5
# Similarity search b/w chuncks vectors & Question Vector.🤖
from sentence_transformers.util import semantic_search
hits = semantic_search(question_vector, vectors, top_k=3)
print(f"\n---- 📃{hits}")

# Getting the actual text in the corpus_id 
best_chunk_id = hits[0][0]["corpus_id"] # best result in of the semanitc search

best_chunk = chucker[best_chunk_id]

prompt = f"""Answer using ONLY the context below
Context: 
{best_chunk}
Question:
{question}
"""
print(prompt)
print(f"\n --Best Chunk:--\n", {best_chunk})

# QUERY PIPELINE (READ HEAVY)----6 & 7---
# The Generation part of Retrieval-Augmented Generation🚀. 💬 Answer


# setup the OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", 
    api_key=os.getenv("OPENROUTER_API_KEY"))


# call the LLM using the 'prompt' you built above!
print("\n⌛ sending to NVIDIA LLM...")
try:
    response = client.chat.completions.create(
        # model="meta-llama/llama-3.1-8b-instruct:free",
        model="openrouter/free",
        messages=[
            {
                "role":"user",
                "content": prompt
            }
        ]
    )
    final_answer = response.choices[0].message.content
except Exception as e:
    # catches ANY error (404. downtime, timeout)
    print(f"\n ❌Error:{e}")
    


