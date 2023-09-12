import subprocess
import threading
import requests
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

@app.route('/chat')
def chat():
    return render_template_string(html_content)

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    prompt = data['prompt']
    payload = {
    'prompt': prompt,
    
    }

    
    try:
        response = requests.post("http://localhost:8080/predict", json=payload)
        
        api_response = response.text
        return api_response
    except Exception as e:
        return str(e)

def run_server():
    app.run(host='0.0.0.0', port=5000)

# HTML content and threading
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Chat with API</title>
    <script>
        async function sendMessage() {
            const message = document.getElementById("userInput").value;
            document.getElementById("chat").innerHTML += "<p><strong>You:</strong> " + message + "</p>";
            document.getElementById("loader").style.display = "block";
            
            const response = await fetch('/send_message', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ "prompt": message })
            });

            let data = await response.text();
            data = data.replace(/<\/?s>/g, '');  // Remove strikethrough tags
            document.getElementById("loader").style.display = "none";
            document.getElementById("chat").innerHTML += "<p><strong>API:</strong> " + data + "</p>";
        }
    </script>
</head>
<body>
    <div id="loader" style="display:none;">Loading...</div>
    <div id="chat"></div>
    <input id="userInput" type="text"/>
    <button onclick="sendMessage()">Send</button>
</body>
</html>
"""

if __name__ == "__main__":
    t = threading.Thread(target=run_server)
    t.start()
    print("Visit http://127.0.0.1:5000/chat to start chatting.")