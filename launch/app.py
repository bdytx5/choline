# import subprocess
# import threading
# import requests
# from flask import Flask, request, jsonify, render_template_string

# app = Flask(__name__)

# @app.route('/chat')
# def chat():
#     return render_template_string(html_content)

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     data = request.json
#     prompt = data['prompt']
#     payload = {
#     'prompt': prompt,
    
#     }

    
#     try:
#         response = requests.post("http://localhost:8080/predict", json=payload)
        
#         api_response = response.text
#         return api_response
#     except Exception as e:
#         return str(e)

# def run_server():
#     app.run(host='0.0.0.0', port=5000)

# # HTML content and threading
# html_content = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Chat with API</title>
#     <script>
#         async function sendMessage() {
#             const message = document.getElementById("userInput").value;
#             document.getElementById("chat").innerHTML += "<p><strong>You:</strong> " + message + "</p>";
#             document.getElementById("loader").style.display = "block";
            
#             const response = await fetch('/send_message', {
#                 method: 'POST',
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({ "prompt": message })
#             });

#             let data = await response.text();
#             data = data.replace(/<\/?s>/g, '');  // Remove strikethrough tags
#             document.getElementById("loader").style.display = "none";
#             document.getElementById("chat").innerHTML += "<p><strong>API:</strong> " + data + "</p>";
#         }
#     </script>
# </head>
# <body>
#     <div id="loader" style="display:none;">Loading...</div>
#     <div id="chat"></div>
#     <input id="userInput" type="text"/>
#     <button onclick="sendMessage()">Send</button>
# </body>
# </html>
# """

# if __name__ == "__main__":
#     t = threading.Thread(target=run_server)
#     t.start()
#     print("Visit http://127.0.0.1:5000/chat to start chatting.")

# import subprocess
# import threading
# import requests
# from flask import Flask, request, jsonify, render_template_string

# app = Flask(__name__)

# @app.route('/chat')
# def chat():
#     return render_template_string(html_content)

# @app.route('/send_message', methods=['POST'])
# def send_message():
#     data = request.json
#     prompt = data['prompt']
#     payload = {'prompt': prompt}
    
#     try:
#         response = requests.post("http://localhost:8080/predict", json=payload)
#         api_response = response.text
#         return api_response
#     except Exception as e:
#         return str(e)

# def run_server():
#     app.run(host='0.0.0.0', port=5000)

# html_content = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Chat with API</title>
#     <script>
#         function sendMessage(event) {
#             if (event.keyCode === 13) {
#                 const message = document.getElementById("userInput").value;
#                 document.getElementById("chat").innerHTML += "<p><strong>You:</strong> " + message + "</p>";
#                 document.getElementById("loader").style.display = "block";

#                 fetch('/send_message', {
#                     method: 'POST',
#                     headers: { 'Content-Type': 'application/json' },
#                     body: JSON.stringify({ "prompt": message })
#                 }).then(response => response.text()).then(data => {
#                     data = data.replace(/<\/?s>/g, '');  // Remove strikethrough tags
#                     document.getElementById("loader").style.display = "none";
#                     document.getElementById("chat").innerHTML += "<p><strong>API:</strong> " + data + "</p>";
#                     document.getElementById("userInput").value = '';
#                 });
#             }
#         }
#     </script>
# </head>
# <body>
#     <div id="loader" style="display:none;">Loading...</div>
#     <div id="chat"></div>
#     <textarea id="userInput" style="width: 100%; height: 50px; resize: both;" onkeydown="sendMessage(event)"></textarea>
# </body>
# </html>
# """

# if __name__ == "__main__":
#     t = threading.Thread(target=run_server)
#     t.start()
#     print("Visit http://127.0.0.1:5000/chat to start chatting.")

import subprocess
import threading
import requests
import sys
from flask import Flask, request, jsonify, render_template_string

# Check for --test and --port in the command line arguments
is_test = '--test' in sys.argv
port_index = sys.argv.index('--port') if '--port' in sys.argv else None
port = int(sys.argv[port_index + 1]) if port_index else 5000

# Decide the backend URL
backend_url = "http://localhost:8080/predict" if not is_test else f"http://127.0.0.1:{port}/predict"

app = Flask(__name__)

@app.route('/chat')
def chat():
    return render_template_string(html_content)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    prompt = data['prompt']
    payload = {'prompt': prompt}

    try:
        response = requests.post(backend_url, json=payload)
        api_response = response.text
        return api_response
    except Exception as e:
        return str(e)

def run_server():
    app.run(host='0.0.0.0', port=5000)

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Chat with API</title>
    <script>
        function sendMessage(event) {
            if (event.keyCode === 13 && event.shiftKey) {
                const message = document.getElementById('userInput').value;
                document.getElementById('chat').innerHTML += '<p><strong>You:</strong> ' + message + '</p>';
                document.getElementById('loader').style.display = 'block';

                fetch('/send_message', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 'prompt': message })
                }).then(response => response.text()).then(data => {
                    data = data.replace(/<\/?s>/g, '');  // Remove strikethrough tags
                    document.getElementById('loader').style.display = 'none';
                    document.getElementById('chat').innerHTML += '<p><strong>API:</strong> ' + data + '</p>';
                    document.getElementById('userInput').value = '';
                });
            }
        }
    </script>
</head>
<body>
    <div id='loader' style='display:none;'>Loading...</div>
    <div id='chat'></div>
    <textarea id='userInput' style='width: 100%; height: 50px; resize: both;' onkeydown='sendMessage(event)'></textarea>
    <p>Helper: To get a response, hit Shift+Enter</p>
</body>
</html>
"""

if __name__ == "__main__":
    t = threading.Thread(target=run_server)
    t.start()
    print(f"Visit http://127.0.0.1:{5000}/chat to start chatting.")