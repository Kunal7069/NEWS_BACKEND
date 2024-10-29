from flask import Flask, jsonify
import requests
from flask_cors import CORS
import easyocr

app = Flask(__name__)
CORS(app)  
port = 3000


@app.route('/')
def home():
    return jsonify({'status':'OCR BACKEND IS RUNNING'})


@app.route('/scrap')
def scrap_portfolio():
    try:
        reader = easyocr.Reader(['en'])
        result=reader.readtext('code1.png', detail = 0)
        print(result)
        return jsonify(result)
        

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
