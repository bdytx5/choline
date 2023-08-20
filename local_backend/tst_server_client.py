from flask import Flask, request
import requests
import threading
import time
from io import BytesIO

def server():
    app = Flask(__name__)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        uploaded_file = request.files['file']
        if uploaded_file.filename == 'abc':
            with open(uploaded_file.filename, 'wb') as file:
                payload = uploaded_file.read()
                print("Payload content:", payload.decode('utf-8'))  # Decode bytes to string for printing
            return 'File with ID "abc" uploaded successfully', 200
        return 'No file with the correct ID uploaded', 400

    app.run(port=8000)

def client():
    # Wait for the server to start
    time.sleep(2)

    url = "http://localhost:8000/upload"
    
    # Create a file-like object in memory with the content you want to send
    file_content = b"This is the content of the file with ID 'abc'."
    file_like_object = BytesIO(file_content)

    # Use the file-like object as the file to upload
    files = {'file': ('abc', file_like_object)}
    response = requests.post(url, files=files)

    print(response.text)

# Start the server in a separate thread
server_thread = threading.Thread(target=server)
server_thread.start()

# Start the client in the main thread
client()

# Wait for the server to finish
server_thread.join()