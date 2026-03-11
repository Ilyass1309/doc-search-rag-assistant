from src.processing.text_chunker import chunk_text
from src.ingestion.document_loader import load_document

doc = load_document("data/raw/example.txt")
print(f"Number of words in the document: {len(doc.split())}")
chunks = chunk_text(doc, chunk_size=100, overlap=20)
print(f"Number of chunks: {len(chunks)}")
for i in range(len(chunks)-1):
    last_20_words = chunks[i].split()[-20:]
    first_20_words = chunks[i+1].split()[:20]
    print(f"Chunk {i} last 20 words: {' '.join(last_20_words)}")
    print(f"Chunk {i+1} first 20 words: {' '.join(first_20_words)}")