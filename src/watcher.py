# watcher.py
#----------------------------------------------
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .storage import add_file

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self,event):

        if event.is_directory:
            return
        
        print(event.src_path)
        add_file(event.src_path)

def watch(directory):    
    observer = Observer()
    handler = ChangeHandler()
    observer.schedule(handler, directory, recursive=True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()