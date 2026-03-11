from src.processing.text_chunker import chunk_text
from src.ingestion.document_loader import load_document

doc = load_document("data/raw/example.txt")
print(f"Number of words in the document: {len(doc.split())}")
chunks = chunk_text(doc, chunk_size=100, overlap=20)
print(f"Number of chunks: {len(chunks)}")
for i in range(len(chunks)):
    print(f"indice {i}: len(chunk): {len(chunks[i].split())}")
    print(f"Chunk {i} preview: {' '.join(chunks[i].split()[:10])}...")