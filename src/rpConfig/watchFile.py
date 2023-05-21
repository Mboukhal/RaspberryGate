import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class CustomEventHandler(FileSystemEventHandler):
    def __init__(self, file_path, observer):
        super().__init__()
        self.file_path = file_path
        self.observer = observer

    def on_created(self, event):
        if event.src_path == self.file_path:
            self.stop()

    def on_moved(self, event):
        if event.dest_path == self.file_path:
            self.stop()

    def stop(self):
        self.observer.stop()


def watchEnvServer(file_name):
    folder_path = '.'

    # Get the file's full path
    file_path = os.path.join(folder_path, file_name)

    observer = Observer()
    event_handler = CustomEventHandler(file_path, observer)
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()

    # Wait until the file is created or moved
    while not os.path.exists(file_path):
        time.sleep(0.1)

    # Stop the observer when the file is found
    observer.stop()
    observer.join()

    return True