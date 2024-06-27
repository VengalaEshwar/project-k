from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import FeatureExtraction as fe
import detect
import warnings
import sys

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS

@app.route('/predictparkinsons', methods=['POST'])
def predict():
    if 'audioFile' not in request.files:
        print("error")
        return jsonify({'error': 'No audio file part'}), 400

    file = request.files['audioFile']
    if file.filename == '':
        print("error")
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(sys.path[0], filename)
        print(filename, "eshwar")
        file.save(filepath)

        try:
            print("called fe")
            features = fe.extract_features(filepath)
            print("finished fe")
            # Assuming you have a model loaded and predict function
            prediction = detect.predictParkinson(features)
            print({'prediction': prediction})
            return jsonify({'prediction': prediction}), 200
        except Exception as e:
            print("error", {'error': str(e)})
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
