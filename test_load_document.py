from src.ingestion.document_loader import load_document

doc = load_document("data/raw/example.txt")
print(len(doc))