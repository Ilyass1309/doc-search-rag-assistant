from openai import OpenAI


client = OpenAI()


def generate_embeddings(formatted_chunks: list[dict]) -> list[dict]:
    if formatted_chunks == []:
        return []
    texts = []
    for chunk in formatted_chunks:
        if "text" not in chunk:
            raise ValueError("Each chunk must contain a 'text' key")
        if "text" == "":
            raise ValueError("Chunk text must not be empty")
        texts.append(chunk["text"])
        


