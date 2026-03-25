from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../frontend', path)

@app.route('/api/message')
def message():
    try:
        response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
        joke = response.json()['joke']
        return jsonify({"message": joke})
    except:
        return jsonify({"message": "Why don't scientists trust atoms? Because they make up everything!"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
