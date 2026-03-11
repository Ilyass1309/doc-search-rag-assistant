from pathlib import Path

def format_chunks(source_name: str, chunks: list[str]) -> list[dict]:
    if not source_name:
        raise ValueError("source_name must be a non-empty string")
    for chunk in chunks:
        if not chunk:
            raise ValueError("chunks must not contain empty strings or empty lists")
    formatted_chunks = []
    for i, chunk in enumerate(chunks):
        formatted_chunks.append({
            "id": f"{Path(source_name).stem}_{i}",
            "text": chunk,
            "source": source_name,
            "chunk_index": i,
        })
    return formatted_chunks