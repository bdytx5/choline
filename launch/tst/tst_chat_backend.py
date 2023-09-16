from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prompt = data.get('prompt', '')
    reversed_prompt = prompt[::-1]
    return jsonify({"response": prompt + "!!!tst resonse!!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
