from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import FeatureExtraction as fe
import detect
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Create the uploads directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/predictparkinsons', methods=['POST'])
def predict():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file part'}), 400

    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(filename,"eshar")
        file.save(filepath)

        try:
            features = fe.extract_features(filepath)
            # Assuming you have a model loaded and predict function
            prediction = detect.predictParkinson(features)
            print({'prediction': prediction})
            return jsonify({'prediction': prediction}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)
