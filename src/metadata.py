# metadata.py 
#------------------------------------------
import json
from pathlib import Path

home_path = Path.home()
metadata_path = home_path / ".lucidfs" / "files.json"

def load_metadata():
    """Load metadata from the JSON file."""
    if metadata_path.exists():
        with open(metadata_path, "r") as f:
            metadata = json.load(f)
        return metadata
    
    else:
        return {}

def save_metadata(metadata):
    """Save metadata to the JSON file."""
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

def update_metadata(filepath,hashed_object):
    """Update metadata with the new file and its hashed object."""
    metadata = load_metadata()
    metadata[filepath] = hashed_object
    save_metadata(metadata)