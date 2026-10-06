# history.py
#-----------------------------
import json
from .events import events_path

def file_history(filepath):
    """Returns the history of a file with timestamp and hash."""
    with open(events_path, "r") as f:
        hashes = []
        for line in f:
            event = json.loads(line)

            if event['filepath'] == filepath:
                timestamp = event['timestamp']
                file_hash = event['file_hash']
                hashes.append((timestamp, file_hash))

    return hashes
