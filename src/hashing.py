# hashing.py
# -------------------------------------
# handles hashing of the file contents 
import hashlib

def hash_file(filepath):
    """Returns the hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath,'rb') as file:
        while (chunk := file.read(64 * 1024)) != b"":
            hasher.update(chunk)
    
    return hasher.hexdigest()
