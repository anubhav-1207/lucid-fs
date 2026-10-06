# cli.py
#----------------------------------------------------
# handles the main CLI of LucidFS and commands of CLI
#-----------------------------------------------------
import typer
from .watcher import watch as watch_directory
from .history import file_history
from .diff import diff as generate_diff
from .metadata import load_metadata
from .storage import objects_path, read_object
from .events import events_path

app = typer.Typer()

@app.callback()
def main():
    ...

@app.command()
def watch(directory: str):
    
    watch_directory(directory)

@app.command()
def history(file_path: str):
    history = file_history(file_path)
    for entry in history:
        print(entry)

@app.command()
def diff(directory: str):
    differences = generate_diff(directory)
    print(differences)

@app.command()
def status():
    print("LucidFS Status:")
    metadata = load_metadata()
    print(f"- Tracked files: {len(metadata)}")

    objects = list(objects_path.iterdir())
    print(f"- Stored objects: {len(objects)}")
    
    if events_path.exists():
        with open(events_path, "r") as f:
            events = sum(1 for _ in f)
    else:
        events = 0
    print(f"- Events: {events}")

    print("- Tracked:")
    for filepath in metadata:
        print(f"\t{filepath}")

@app.command()
def restore(filepath: str, version: str):
    content = read_object(version)
    versions = file_history(filepath)

    if not versions:
        print("! - No versions found for this file.")
        return

    if version not in [entry[1] for entry in versions]:
        print("! - Version not found for this file.")
        return
    
    with open(filepath,'wb') as file:
        file.write(content)
        print(f"- Restored file: {filepath} to version: {version[0:8]}.....")

if __name__ == "__main__":
    app()