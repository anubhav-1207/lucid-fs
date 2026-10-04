# hashing.py
# ----------------------
import hashlib

def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath,'rb') as file:
        while (chunk := file.read(64 * 1024)) != b"":
            hasher.update(chunk)
    
    return hasher.hexdigest()
