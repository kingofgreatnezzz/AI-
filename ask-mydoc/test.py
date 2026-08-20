import os
text="hello world"

# Chuncking will take a size, overlap 
def chunk(text, size=4, overlap=1):
    chunks = []
    # Iterate through the text by size
    for i in range(0 ,len(text), size - overlap):
        print(f"iteration ->",i)
        piece = text[i:i + size]
        print(f"Piece ->",piece)

        if piece.strip():
            chunks.append(piece)
            print(f"chuncks",chunks)
    return chunks

chunk(text=text)




# # go to a folder ,pick all file adn print thier content
# folder = "doc"

# for file in os.listdir(folder):
#     path = os.path.join(folder, file)
    
#     if os.path.isfile(path):
#         print(f"\n -- {file} ---")

#     with open(path, "r") as f:
#         print(f.read())



# files = os.listdir(".")
# for file in files:
#     print(file)


# def load_docs(folder="doc"):
#     for f in folder:
#         with open(f, "r") as file:
#             content =  file.read()
#         print(f"\n--- {file} ---")
#         print(content)
