from src.processing.chunk_formatter import format_chunks


chunks = ["hello world", "this is chunk two"]
formatted = format_chunks("example.txt", chunks)
print(formatted[0])
print(formatted[1])