import requests
from io import BytesIO

url = "http://localhost:8000/upload"

# Create a file-like object in memory with the content you want to send
file_content = b"This is the content of the file with ID 'abc'."
file_like_object = BytesIO(file_content)

# Use the file-like object as the file to upload
files = {'file': ('abc', file_like_object)}
response = requests.post(url, files=files)

print(response.text)