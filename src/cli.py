import typer
from .watcher import watch as watch_directory
from .history import file_history
from .diff import diff as generate_diff
from .metadata import load_metadata
from .storage import objects_path
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
    metadata = load_metadata()
    print(f"Tracked files: {len(metadata)}")

    for filepath in metadata:
        print(filepath)
    objects = list(objects_path.iterdir())
    print(f"Stored objects: {len(objects)}")
    
    if events_path.exists():
        with open(events_path, "r") as f:
            events = sum(1 for _ in f)
    else:
        events = 0
    print(f"Events: {events}")

if __name__ == "__main__":
    app()