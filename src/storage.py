# storage.py
#--------------------------------
from .metadata import update_metadata, load_metadata
from .events import log_event
from .hashing import hash_file
from pathlib import Path 

home_path = Path.home()
objects_path = home_path / ".lucidfs" / "objects"
objects_path.mkdir(parents=True, exist_ok=True)

def store_file(filename):
    """Stores a file in the object_path, returning its hash."""
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
    """Adds a file to the storage, updating metadata and logging the event."""
    hashed_object = store_file(filepath)
    metadata = load_metadata()

    if metadata.get(filepath) == hashed_object:
        """
        This means that the file has not been changed because the hash of the file is already in the metadata.
        """
        return

    update_metadata(filepath, hashed_object)
    log_event(filepath, hashed_object)


def read_object(file_hash):
    """Reads the content of a stored object given its hash."""
    object_path = objects_path / file_hash
    with open(object_path, "rb") as f:
        return f.read()