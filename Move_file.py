import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

src_path = "C:/Users/HP/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")
    
    def on_moved(self, event):
        print(f"Someone moved {event.src_path}")
    def on_modified(self, event):
        print(f"{event.src_path} has been changed")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler,src_path)

observer.start()
try:
    while True:
            time.sleep(2)
            print("running...")
except KeyboardInterrupt:
        print("stopped!")
        observer.stop




