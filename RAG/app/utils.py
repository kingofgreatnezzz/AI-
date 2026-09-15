import pymupdf

doc = pymupdf.open("../doc/ai_bulder.pdf")
for page in doc:
    print("---")
    print(page.get_text())

text = "C:\Users\TECHDEBIA\Documents\AI\RAG\doc"
print(text)

def cleaner(text=text):
    text = text.strip()
    text = text.replace("\r","")
    text = text.replace("\t","")
    # normalize other patterns ....
    return text

def chuncker(text, size=400, overlap=80):
    chunks = []
    # Iterate th rough 
    for i in range(0, len(text), size-overlap):
        print(i)
        piece = text[i:i+size]

        if piece.strip():
            chunks.append(piece)
            print(chunks)
    return chunks

        

    