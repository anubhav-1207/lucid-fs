# storage.py
#--------------------------------
from .metadata import update_metadata
from .events import log_event
from .hashing import hash_file
from pathlib import Path 

home_path = Path.home()
objects_path = home_path / ".lucidfs" / "objects"
objects_path.mkdir(parents=True, exist_ok=True)

def store_file(filename):
    hashed_object = hash_file(filename)
    object_path = objects_path / hashed_object

    if object_path.exists():
        """
        This means that the file has not been changed because object path is already exist.
        """
        return hashed_object

    with open(filename,"rb") as file:
        with open(object_path,"wb") as destination:
            while (chunk := file.read(64 * 1024)):
                destination.write(chunk) # write the new file into the object path
    
    return hashed_object

def add_file(filepath):
    hashed_object = store_file(filepath)
    update_metadata(filepath, hashed_object)
    log_event(filepath, hashed_object)

def read_object(file_hash):
    object_path = objects_path / file_hash
    with open(object_path, "rb") as f:
        return f.read()