from flask import Flask, request, render_template_string
import requests
import threading
import sys
from collections import deque

# Check for --test and --port in the command line arguments
##### NOTE --test --port 4000 as args with the tst_chat_backend.py script running will launch the app in test mode 
is_test = '--test' in sys.argv
port_index = sys.argv.index('--port') if '--port' in sys.argv else None
port = int(sys.argv[port_index + 1]) if port_index else 5000

# Decide the backend URL
backend_url = "http://127.0.0.1:8080/predict" if not is_test else f"http://127.0.0.1:{port}/predict"

# Number of tokens per word
tokens_per_word = 2

# Number of previous tokens to use as context, default 250
num_prev_tokens = 250

# Cache max length as an argument
cache_maxlen = int(sys.argv[sys.argv.index('--contextlen') + 1]) if '--contextlen' in sys.argv else 100

# Cache to hold previous chat messages and responses
chat_cache = deque(maxlen=cache_maxlen)

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
    
    # Update the chat cache
    chat_cache.append(new_prompt)

    # Concatenate all chat history to form a single prompt
    full_prompt = ''.join(chat_cache)

    # Create payload with concatenated prompt
    payload = {'prompt': full_prompt}

    try:
        response = requests.post(backend_url, json=payload)

        print(f"Received response: {response.text}")
        
        
        if response.status_code == 200:
            api_response = f"Bot: {response.text}\n"
            chat_cache.append(api_response)
            return api_response
            
        # if response.status_code == 200:
        #     api_response = f"Bot: {response.json()['response']}\n"
        #     chat_cache.append(api_response)
        #     return api_response.strip()
        else:
            return f"Failed to get a valid response: {response.text}"
    except Exception as e:
        print(f"Exception caught: {e}")
        return str(e)






html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Chat with API</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.3/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.3/theme/monokai.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.3/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.58.3/mode/python/python.min.js"></script>
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
                    document.getElementById('loader').style.display = 'none';
                    
                    // Split the API response by '```'
                    const parts = data.split('```');
                    for (let i = 0; i < parts.length; i++) {
                        const part = parts[i].trim();
                        if (i % 2 === 0) {
                            // normal text
                            document.getElementById('chat').innerHTML += '<p><strong>Bot:</strong> ' + part + '</p>';
                        } else {
                            // code snippet
                            const newEditorDiv = document.createElement('div');
                            document.getElementById('chat').appendChild(newEditorDiv);
                            const editor = CodeMirror(newEditorDiv, {
                                mode: 'python',
                                lineNumbers: true,
                                readOnly: true,
                                theme: 'monokai',
                                value: part
                            });
                            editor.setSize(null, "auto");
                        }
                    }
                    
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
    <p>Thanks for using Choline! To get a response, hit Shift+Enter.</p>
    <button onclick='clearChat()'>Clear Chat</button>
</body>
</html>
"""




if __name__ == "__main__":
    t = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000})
    t.start()
    print(f"Visit http://127.0.0.1:{port}/chat to start chatting.")