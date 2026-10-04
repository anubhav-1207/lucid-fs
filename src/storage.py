# storage.py
#--------------------------------
from hashing import hash_file
from pathlib import Path 

home_path = Path.home()
objects_path = home_path / ".lucid-fs" / "objects"
objects_path.mkdir(parents=True, exist_ok=True)

def store_file(filename):
    hashed_object = hash_file(filename)
    object_path = objects_path / hashed_object

    
    if object_path.exists():
        """
        This means that the file has not been changed because object path is already exist.
        """
        return object_path

    with open(filename,"rb") as file:
        with open(object_path,"wb") as destination:
            while (chunk := file.read(64 * 1024)):
                destination.write(chunk) # write the new file into the object path
    
    return object_path