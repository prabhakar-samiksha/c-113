import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="C:/Users/Lenovo/Downloads"
class Fileeventhandler(FileSystemEventHandler):
    def on_created(self,event):
      print(f"hii,{event.src_path}has created")
    def on_deleted(self,event):
        print(f"oops someone deleted{event.src_path}")
    def on_modified(self,event):
        print(f"hey,there{event.src_path}has been modified")
    def on_move(self,event):
        print(f"someone moved{event.src_path}to{event.dest_path}")
    
eventhandler=Fileeventhandler()
observer=Observer()
observer.schedule(eventhandler,from_dir,recursive=True)
observer.start()
try:
    while True :
        time.sleep(2)
        print("running")

       

except KeyboardInterrupt:
    print("stop")
    observer.stop()


        
