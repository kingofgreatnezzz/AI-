import pymupdf

doc = pymupdf.open("../doc/ai_bulder.pdf")

for page in doc:
    print("---")
    print(page.get_text())