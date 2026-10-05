# events.py
#---------------------------------------------
import json
from pathlib import Path
from datetime import datetime

home_path = Path.home()
events_path = home_path / ".lucidfs" / "events.jsonl"

def log_event(filepath,file_hash):
    """Log the event of adding a file to the metadata."""
    event = {}
    event['timestamp'] = datetime.now().isoformat()
    event['filepath'] = filepath
    event['file_hash'] = file_hash
    
    with open(events_path, "a") as f:
        f.write(json.dumps(event) + "\n")