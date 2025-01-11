import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Đường dẫn thư mục hiện tại
PROJECT_DIRECTORY = os.getcwd()

class UIFileHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type in ('created', 'modified') and event.src_path.endswith('.ui'):
            ui_file = event.src_path
            py_file = ui_file[:-3] + ".py"
            os.system(f"pyside6-uic {ui_file} -o {py_file}")
            print(f"Converted: {ui_file} -> {py_file}")

if __name__ == "__main__":
    event_handler = UIFileHandler()
    observer = Observer()
    observer.schedule(event_handler, PROJECT_DIRECTORY, recursive=True)
    observer.start()
    print(f"Watching directory: {PROJECT_DIRECTORY}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
