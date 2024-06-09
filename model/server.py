from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import FeatureExtraction as fe
import detect
import warnings
import sys
# warnings.filterwarnings("ignore", category=UserWarning, module='librosa')
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'

# # Create the uploads directory if it doesn't exist
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/predictparkinsons', methods=['POST'])
def predict():
    if 'audio' not in request.files:
        print("error" ,{'error': str(e)})
        return jsonify({'error': 'No audio file part'}), 400

    file = request.files['audio']
    if file.filename == '':
        print("error")
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = sys.path[0] + filename
        print(filename,"eshwar")
        file.save(filepath)

        try:
            print("called fe")
            features = fe.extract_features(filepath)
            print("finisied fe")
            # Assuming you have a model loaded and predict function
            prediction = detect.predictParkinson(features)
            print({'prediction': prediction})
            return jsonify({'prediction': prediction}), 200
        except Exception as e:
            print("error" ,{'error': str(e)})
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
