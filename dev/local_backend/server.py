
#### listens for calls from the client, and provisions storage
####### also recieves vast instance information 
########### 



# # THIS SERVER SENDS A PATH TO THE CLIENT, SO THEY CAN START UPLOADING DATA TO A CHOLINE SERVER 
# # THIS WILL ALSO START UP A LISTENER, LISTENING AT THE PATH THAT WILL READ FILES THAT ARE BEING 
# # SENT TO THIS LOCATION 

# # THE FIRST FILE THAT NEEDS TO BE READ IS A FILE CALLED "CHOLINE_{RUNID}.txt"
# # this file will contain the information that has the location (a vastai instance ssh)
# # where the files will be sent to (the listener uses rsysnc)


# from flask import Flask, request
# import os
# import time

# app = Flask(__name__)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     username = request.form.get('username')
#     if username:
#         run_id = str(int(time.time()))
#         folder_path = os.path.expanduser(f"~/.choline/{run_id}")
#         os.makedirs(folder_path, exist_ok=True)
#         return f"Directory created successfully: {folder_path}", 200
#     return 'No username provided', 400

# if __name__ == '__main__':
#     app.run(port=8000)


# from flask import Flask, request
# import os
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import subprocess

# class MyHandler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.src_path.endswith(f"CHOLINE_{run_id}.txt"):
#             with open(event.src_path, 'r') as file:
#                 vast_instance_info = file.read().strip()
#                 print(f"Received Vast.ai instance information: {vast_instance_info}")

#                 # Make sure the destination directory exists
#                 os.makedirs(vast_instance_info, exist_ok=True)

#                 # Construct the rsync command to transfer files to the Vast.ai instance simulation
#                 command = f'rsync -av {folder_path}/ {vast_instance_info}/'

#                 # Execute the command
#                 result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#                 # Print the result
#                 if result.returncode == 0:
#                     print("Files transferred successfully")
#                 else:
#                     print(f"An error occurred: {result.stderr.decode()}")

# app = Flask(__name__)
# run_id = None
# folder_path = None

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     global run_id, folder_path
#     username = request.form.get('username')
#     if username:
#         run_id = str(int(time.time()))
#         folder_path = os.path.expanduser(f"~/.choline/{run_id}")
#         os.makedirs(folder_path, exist_ok=True)

#         observer = Observer()
#         event_handler = MyHandler()
#         observer.schedule(event_handler, path=folder_path, recursive=False)
#         observer.start()

#         return f"Directory created successfully: {folder_path}", 200
#     return 'No username provided', 400

# if __name__ == '__main__':
#     app.run(port=8000)


from flask import Flask, request
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from collections import deque
import threading

class PayloadDispatchListener(FileSystemEventHandler):
    def __init__(self):
        self.files_count = {}
        self.total_files = 0
        self.upload_queue = deque()

    def on_modified(self, event):
        if event.src_path.endswith(f"CHOLINE_{run_id}.txt"):
            with open(event.src_path, 'r') as file:
                self.vast_instance_info, self.total_files = file.read().strip().split('\n')
                self.total_files = int(self.total_files)
                print(f"Received Vast.ai instance information: {self.vast_instance_info}")

        elif not event.src_path.endswith('/') and os.path.isfile(event.src_path):
            self.files_count[event.src_path] = self.files_count.get(event.src_path, 0) + 1

            # If the file is seen for the second time, add to the upload queue
            if self.files_count[event.src_path] == 2:
                self.upload_queue.append(event.src_path)
                # You can start uploading the file here if you want immediate action


    def upload_files(self):
        while True:
            if self.upload_queue and self.vast_instance_info:
                file_path = self.upload_queue.popleft()

                # Construct the rsync command to synchronize this file
                command = f'rsync -av {file_path} {self.vast_instance_info}/'

                # Execute the command
                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                # Print the result
                if result.returncode == 0:
                    print(f"File {file_path} synchronized successfully")
                else:
                    print(f"An error occurred while synchronizing {file_path}: {result.stderr.decode()}")

                # Check if all files have been uploaded
                if len(self.upload_queue) == 0 and len(self.files_count) == self.total_files:
                    print("All files uploaded successfully")
                    break 

            time.sleep(0.3) # prevents "busy waiting" ? 

app = Flask(__name__)
run_id = None
folder_path = None

@app.route('/upload', methods=['POST'])
def upload_file():
    global run_id, folder_path
    username = request.form.get('username')
    if username:
        run_id = str(int(time.time()))
        folder_path = os.path.expanduser(f"~/.choline/{run_id}")
        os.makedirs(folder_path, exist_ok=True)

        observer = Observer()
        event_handler = PayloadDispatchListener()
        observer.schedule(event_handler, path=folder_path, recursive=False)
        observer.start()

        # Start a thread to process the upload queue
        upload_thread = threading.Thread(target=event_handler.upload_files)
        upload_thread.start()

        return f"Directory created successfully: {folder_path}", 200
    return 'No username provided', 400

if __name__ == '__main__':
    app.run(port=8000)
