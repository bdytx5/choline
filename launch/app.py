from flask import Flask, request, render_template_string
import requests
import threading
import sys
from collections import deque

# Check for --test and --port in the command line arguments
is_test = '--test' in sys.argv
port_index = sys.argv.index('--port') if '--port' in sys.argv else None
port = int(sys.argv[port_index + 1]) if port_index else 5000

# Decide the backend URL
backend_url = "http://localhost:8080/predict" if not is_test else f"http://127.0.0.1:{port}/predict"

# Cache to hold previous chat messages and responses
chat_cache = deque(maxlen=100)

# Number of tokens per word
tokens_per_word = 2

app = Flask(__name__)

@app.route('/chat')
def chat():
    return render_template_string(html_content)

@app.route('/clear_chat', methods=['POST'])
def clear_chat():
    global chat_cache
    chat_cache.clear()
    return 'Cleared'

@app.route('/send_message', methods=['POST'])
def send_message():
    global chat_cache
    
    data = request.json
    new_prompt = f"User: {data['prompt']}\n"
    
    chat_cache.append(new_prompt)

    tokens = sum(len(word.split()) for sentence in chat_cache for word in sentence.split()) * tokens_per_word

    full_prompt = ''.join(chat_cache)

    payload = {'prompt': full_prompt}

    try:
        response = requests.post(backend_url, json=payload)
        api_response = f"Bot: {response.json()['response']}\n"
        
        chat_cache.append(api_response)

        return api_response.strip()
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
            if (event.shiftKey && event.keyCode === 13) {
                const message = document.getElementById('userInput').value;
                document.getElementById('chat').innerHTML += '<p><strong>You:</strong> ' + message + '</p>';
                document.getElementById('loader').style.display = 'block';

                fetch('/send_message', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 'prompt': message })
                }).then(response => response.text()).then(data => {
                    data = data.replace(/<\/?s>/g, '');
                    document.getElementById('loader').style.display = 'none';
                    document.getElementById('chat').innerHTML += '<p><strong>API:</strong> ' + data + '</p>';
                    document.getElementById('userInput').value = '';
                });
            }
        }

        function clearChat() {
            fetch('/clear_chat', {
                method: 'POST'
            }).then(() => {
                document.getElementById('chat').innerHTML = '';
            });
        }
    </script>
</head>
<body>
    <div id='loader' style='display:none;'>Loading...</div>
    <div id='chat' style='padding-bottom: 50px;'></div>
    <textarea id='userInput' style='width: 100%; height: 50px; resize: both;' onkeydown='sendMessage(event)'></textarea>
    <p>To get a response, hit Shift+Enter.</p>
    <button onclick='clearChat()'>Clear Chat</button>
</body>
</html>
"""

if __name__ == "__main__":
    t = threading.Thread(target=run_server)
    t.start()
    print(f"Visit http://127.0.0.1:{5000}/chat to start chatting.")