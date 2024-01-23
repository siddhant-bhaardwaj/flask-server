# server.py
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Ensure 'file' is in the request.files dictionary
        if 'file' not in request.files:
            return 'No file part', 400

        file = request.files['file']

        # Ensure a file is selected
        if file.filename == '':
            return 'No selected file', 400

        # Save the file to the 'uploads' directory
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        return 'Upload successful!'
    except Exception as e:
        return f'Error: {e}', 400

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)  # Create 'uploads' directory if not exists
    # Replace 'your_server_local_ip' with the actual local IP address of the server machine
    app.run(host='0.0.0.0', port=5000)
