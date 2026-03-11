def chunk_text(text, chunk_size, overlap):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be less than chunk_size")
    if len(text) == 0:
        return []
    words = text.split()
    start = 0
    step = chunk_size - overlap
    chunks = []
    
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = ' '.join(words[start:end])
        chunks.append(chunk)
        start += step
    return chunks