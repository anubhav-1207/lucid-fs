# storage.py
#--------------------------------
from pathlib import Path 

home_path = Path.home()
objects_path = home_path / ".lucidfs" / "objects"
objects_path.mkdir(parents=True, exist_ok=True)

def store_file(filename):
    ...
