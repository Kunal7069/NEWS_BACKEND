from flask import Flask, jsonify, request
from flask_cors import CORS
import easyocr
import os
import tempfile  # Import tempfile module

app = Flask(__name__)
CORS(app)  
port = 8000

@app.route('/')
def home():
    return jsonify({'status': 'OCR BACKEND 2 IS RUNNING'})

@app.route('/scrap', methods=['POST'])
def scrap_portfolio():
    try:
        # Ensure an image file is provided
        if 'image' not in request.files:
            return jsonify({'error': 'No image file provided'}), 400
        
        image_file = request.files['image']

        # Create a temporary file using tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
            temp_file_path = temp_file.name  # Get the temporary file path
            image_file.save(temp_file_path)  # Save the uploaded file to the temp path

        # Use EasyOCR to read the text from the image
        reader = easyocr.Reader(['en'])
        result = reader.readtext(temp_file_path, detail=0)

        # Optionally, delete the temporary file
        os.remove(temp_file_path)

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
