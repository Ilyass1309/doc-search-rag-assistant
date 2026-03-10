from pathlib import Path

def load_document(file_path):
    file_path = Path(file_path)
    if(not file_path.exists()):
        raise  FileNotFoundError(f"File {file_path} does not exist")
    if(file_path.is_dir()):
        raise  ValueError(f"{file_path} is a directory, not a file")
    if(file_path.suffix != '.txt'):
        raise  ValueError("Only .txt files are supported")
    
    with file_path.open(encoding="utf-8") as f:
        content = f.read()
    return content
