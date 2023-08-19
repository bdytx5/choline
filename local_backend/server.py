

from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)



        return 'File uploaded successfully', 200
    return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(port=8000)
